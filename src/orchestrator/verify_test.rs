//! What the verification queue has to get right.
//!
//! The interesting failures here are not in any one function. They are in the
//! join: a node the ranking offers forever because nothing recorded the
//! attempt, a node offered again after the kernel already accepted it, a
//! decomposition asked for on a statement nobody has tried to prove yet. So
//! every test writes real skeleton, claim and verdict files and reads the
//! assignment back, rather than constructing a [`Target`] directly.
#![allow(clippy::expect_used)]

use std::fmt::Write as _;
use std::path::{Path, PathBuf};

use super::*;

/// The single best node, which is what most of these tests are about.
///
/// `next_batch` is the production entry point; a test asserting which node the
/// ranking prefers is asking for the head of that list, and says so more
/// clearly this way than by indexing one out at every call site.
fn next(workspace: &std::path::Path) -> Option<Assignment> {
    next_batch(workspace, 1).into_iter().next()
}


/// A clean workspace of its own per test, named so a failure says which.
fn workspace(name: &str) -> PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-verify-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the workspace is creatable");
    root
}

/// Writes a skeleton file with the given fenced blocks.
fn skeleton(root: &Path, slug: &str, header: &str, gaps: &[&str]) {
    let directory = root.join("research/backward");
    std::fs::create_dir_all(&directory).expect("the backward directory is creatable");
    let mut text = format!("# {slug}\n\n```skeleton\n{header}\n```\n");
    for gap in gaps {
        let _ = write!(text, "\n```gap\n{gap}\n```\n");
    }
    std::fs::write(directory.join(format!("{slug}.md")), text).expect("the skeleton is writable");
}

/// Writes a note carrying one claim block.
fn claim(root: &Path, name: &str, body: &str) {
    let directory = root.join("research/notes");
    std::fs::create_dir_all(&directory).expect("the notes directory is creatable");
    std::fs::write(
        directory.join(format!("{name}.md")),
        format!("# {name}\n\n```claim\n{body}\n```\n"),
    )
    .expect("the note is writable");
}

/// Files a passing kernel verdict for one node's source, as `lean_check` would.
fn passing_verdict(root: &Path, id: &str) {
    let directory = root.join(lean::VERDICT_DIR);
    std::fs::create_dir_all(&directory).expect("the verdict directory is creatable");
    let source = source_for(id);
    let record = serde_json::json!({
        "file": source,
        "compiled": true,
        "sorries": [],
        "axioms": [format!("'{id}' depends on axioms: [propext, Classical.choice]")],
        "verified": true,
    });
    std::fs::write(
        directory.join(format!("{}.json", source.replace('/', "_"))),
        serde_json::to_string_pretty(&record).expect("the record renders"),
    )
    .expect("the verdict is writable");
}

/// A workspace whose graph holds one established claim two lemmas rest on, and
/// one open lemma resting on nothing.
///
/// This is the shape the ranking exists to discriminate: the claim is what the
/// run is *already building on*, so a mistake in it is the one nothing above it
/// can catch, and the open lemma is a perfectly good thing to prove later.
fn two_kinds_of_target(name: &str) -> PathBuf {
    let root = workspace(name);
    claim(
        &root,
        "bound",
        "id: cauchy-bound\nstatement: |f| <= 2\nstatus: proved\n",
    );
    skeleton(
        &root,
        "main",
        "goal: the sum is finite\nimplies: the lemmas combine by summation\nrests-on: cauchy-bound\n",
        &[
            "id: tail\nlemma: the tail is o(1)\nstatus: open\ndischarged-by: cauchy-bound\nnext: sum the bound\n",
            "id: head\nlemma: the head is bounded\nstatus: open\nnext: expand\n",
        ],
    );
    root
}

/// The whole point of ranking rather than listing.
///
/// A claim the run has proved and two lemmas cite outranks an open lemma
/// nobody has built on yet, however tractable the second one looks.
#[test]
fn the_node_the_run_is_already_building_on_goes_first() {
    let root = two_kinds_of_target("ranked");

    let assignment = next(&root).expect("a graph with three settled-or-ready nodes offers one");

    assert_eq!(assignment.target.id, "cauchy-bound");
    assert!(
        assignment.target.established,
        "an established claim is what the run is building on"
    );
    assert_eq!(assignment.stage, Stage::Prove, "nothing has been tried yet");
}

/// A run with nothing decomposed has nothing to verify, and must not spend a
/// child run finding that out.
#[test]
fn an_empty_workspace_offers_nothing() {
    let root = workspace("empty");

    assert!(next(&root).is_none());
}

/// The recursion, and the reason there are two stages rather than one.
#[tokio::test]
async fn a_second_pass_on_the_same_node_asks_for_a_decomposition() {
    let root = two_kinds_of_target("second-pass");

    let first = next(&root).expect("the first pass offers a node");
    note_attempt(&root, &first.target.id, first.stage)
        .await
        .expect("the attempt record is writable");

    let second = next(&root).expect("the node is still worth one more pass");
    assert_eq!(second.target.id, first.target.id);
    assert_eq!(second.stage, Stage::Decompose);
}

/// The bound, and what it is worth.
///
/// Without it the highest-ranked node the prover cannot close is the highest
/// ranked node forever, and every remaining pass in the run re-attempts it.
#[tokio::test]
async fn a_node_that_survived_both_stages_stops_being_offered() {
    let root = two_kinds_of_target("bounded");

    for _ in 0..MAX_ATTEMPTS {
        let assignment = next(&root).expect("the node is offered until the bound");
        assert_eq!(assignment.target.id, "cauchy-bound");
        note_attempt(&root, &assignment.target.id, assignment.stage)
            .await
            .expect("the attempt record is writable");
    }

    let moved_on = next(&root).expect("the ranking offers the next node down");
    assert_ne!(
        moved_on.target.id, "cauchy-bound",
        "a node past the bound is skipped rather than re-attempted"
    );
}

/// The kernel has spoken, so there is nothing left to ask it.
///
/// Read from the filed verdict rather than from the graph's own standing,
/// because the two can disagree for an honest reason: a passing check that
/// nobody has yet written into a claim block leaves the node `established` in
/// the graph while `code/out/lean/` already holds the proof.
#[test]
fn a_node_the_kernel_already_accepted_is_not_offered_again() {
    let root = two_kinds_of_target("accepted");
    passing_verdict(&root, "cauchy-bound");

    let assignment = next(&root).expect("the other nodes are still open");

    assert_ne!(assignment.target.id, "cauchy-bound");
}

/// The file name is derived, not chosen, because the arm has to find the
/// verdict again a pass later.
#[test]
fn a_qualified_gap_key_becomes_one_addressable_source() {
    assert!(
        source_for("main/tail").starts_with("code/lean/main_tail-"),
        "the readable part leads: {}",
        source_for("main/tail")
    );
    assert!(
        source_for("cauchy-bound").starts_with("code/lean/cauchy_bound-"),
        "a hyphen is not a Lean identifier character"
    );
}

/// Two ids that fold to the same readable name still get their own file.
///
/// A live blueprint ranked `spectral-…-lower-bound/G-eigenvalue-bounds-degree`
/// alongside hyphenated siblings, so `a/b` against `a-b` is the shape that
/// actually occurs. Sharing a path would mean one statement's proof overwriting
/// the other's and one attempt record standing for both — and a kernel verdict
/// read back against the wrong statement.
#[test]
fn ids_differing_only_in_a_separator_do_not_share_a_file() {
    assert_ne!(source_for("main/tail"), source_for("main-tail"));
    assert_ne!(source_for("a/b/c"), source_for("a-b-c"));
}

/// The derived name has to survive a restart, so it is a pure function of the id.
#[test]
fn the_derived_name_is_stable_for_one_id() {
    assert_eq!(source_for("main/tail"), source_for("main/tail"));
    assert_eq!(
        source_for("cauchy-bound"),
        "code/lean/cauchy_bound-d85af71b.lean",
        "the fingerprint is a path, so a change to it is a compatibility break"
    );
}

/// A workspace written before the fingerprint keeps its attempt count.
///
/// The permissive missing-record reading is zero, and here that would hand a
/// node that had already spent both attempts a fresh pair on the most expensive
/// tool in the image.
#[tokio::test]
async fn a_record_under_the_old_name_still_counts() {
    let root = workspace("legacy-name");
    let directory = root.join(LEDGER_DIR);
    std::fs::create_dir_all(&directory).expect("the ledger directory is writable");
    std::fs::write(
        directory.join("main_tail.json"),
        r#"{"node": "main/tail", "attempts": 2, "stage": "decompose",
            "source": "code/lean/main_tail.lean"}"#,
    )
    .expect("the legacy record is writable");

    assert_eq!(attempts(&root, "main/tail"), 2);

    // And the next attempt moves the node onto the current name without
    // disturbing the old file, which stays as the record it is.
    note_attempt(&root, "main/tail", Stage::Decompose)
        .await
        .expect("the attempt record is writable");
    assert_eq!(attempts(&root, "main/tail"), 3);
    assert!(directory.join("main_tail.json").exists());
}

/// One node counts once, whichever names it is filed under.
#[tokio::test]
async fn a_node_filed_under_both_names_is_one_statement() {
    let root = workspace("both-names");
    let directory = root.join(LEDGER_DIR);
    std::fs::create_dir_all(&directory).expect("the ledger directory is writable");
    std::fs::write(
        directory.join("main_tail.json"),
        r#"{"node": "main/tail", "attempts": 1, "stage": "prove",
            "source": "code/lean/main_tail.lean"}"#,
    )
    .expect("the legacy record is writable");
    note_attempt(&root, "main/tail", Stage::Decompose)
        .await
        .expect("the attempt record is writable");

    let (_, attempted) = counts(&root);

    assert_eq!(attempted, 1, "one node, filed twice, is one statement");
}

/// Counting the attempt when it starts is what survives the ordinary ending.
///
/// The usual way a turn ends here is the run cap killing it, which leaves no
/// report. A record written afterwards would not exist, and the node would rank
/// first again on the next pass.
#[tokio::test]
async fn the_attempt_is_counted_before_the_prover_runs() {
    let root = workspace("counted");

    assert_eq!(attempts(&root, "some-node"), 0);
    note_attempt(&root, "some-node", Stage::Prove)
        .await
        .expect("the attempt record is writable");

    assert_eq!(attempts(&root, "some-node"), 1);
}

/// An unreadable record must not strand a node forever.
#[test]
fn a_corrupt_attempt_record_reads_as_no_attempts() {
    let root = workspace("corrupt");
    let directory = root.join(LEDGER_DIR);
    std::fs::create_dir_all(&directory).expect("the ledger directory is creatable");
    std::fs::write(directory.join("some-node.json"), "{ truncated")
        .expect("the record is writable");

    assert_eq!(attempts(&root, "some-node"), 0);
}

/// The briefing carries the kernel's own words when there were any.
///
/// A prover told "decompose this" decomposes the statement it would have
/// written anyway; one told which axiom the last attempt rested on knows what
/// the decomposition has to attack.
#[test]
fn a_failed_check_reaches_the_next_briefing_verbatim() {
    let root = two_kinds_of_target("objection");
    let directory = root.join(lean::VERDICT_DIR);
    std::fs::create_dir_all(&directory).expect("the verdict directory is creatable");
    let source = source_for("cauchy-bound");
    std::fs::write(
        directory.join(format!("{}.json", source.replace('/', "_"))),
        serde_json::json!({
            "file": source,
            "compiled": true,
            "sorries": [],
            "axioms": ["'main' depends on axioms: [propext, key_estimate]"],
            "verified": false,
        })
        .to_string(),
    )
    .expect("the verdict is writable");

    let assignment = next(&root).expect("a failed check leaves the node worth another pass");
    let briefing = assignment.briefing();

    assert!(
        briefing.contains("key_estimate"),
        "the objection names the axiom nothing proved: {briefing}"
    );
}

/// The denominator is statements the run was asked about, not files the kernel
/// saw.
///
/// A live run wrote `code/lean/ceil_test.lean` — five `#check` lines, no
/// theorem — and checked it twice while hunting the right Mathlib import. That
/// is what a prompt telling it to search Mathlib before proving anything asks
/// for, and every check files a verdict. Counting verdicts told the judge the
/// run had handed the kernel a file and had it refused, which reads as a failed
/// proof.
#[tokio::test]
async fn a_mathlib_name_probe_is_not_a_formalisation_attempt() {
    let root = two_kinds_of_target("probe");
    // The prover's scratch file, checked and refused, exactly as on disk.
    let directory = root.join(lean::VERDICT_DIR);
    std::fs::create_dir_all(&directory).expect("the verdict directory is creatable");
    std::fs::write(
        directory.join("code_lean_ceil_test.lean.json"),
        r#"{"file":"code/lean/ceil_test.lean","compiled":false,"sorries":[],
            "axioms":[],"declarations":[],"verified":false}"#,
    )
    .expect("the probe verdict is writable");

    assert_eq!(counts(&root), (0, 0), "no statement has been assigned yet");

    let assignment = next(&root).expect("the graph offers a target");
    note_attempt(&root, &assignment.target.id, assignment.stage)
        .await
        .expect("the attempt record is writable");

    assert_eq!(
        counts(&root),
        (0, 1),
        "one statement was asked about and is unproved; the probe is not in the denominator"
    );

    passing_verdict(&root, &assignment.target.id);
    assert_eq!(counts(&root), (1, 1));
}

/// The batch takes the ranking in order, and stops where it is told.
///
/// The ordering matters as much as the count: a batch that took an arbitrary
/// subset would spend the same budget on whatever the walk happened to reach
/// first, which is the thing the ranking exists to prevent.
#[test]
fn a_batch_takes_the_top_of_the_ranking_in_order() {
    let root = two_kinds_of_target("batched");

    let batch = next_batch(&root, 8);

    assert!(
        batch.len() > 1,
        "this fixture has several open nodes, so a batch must offer more than one"
    );
    assert_eq!(
        batch.first().map(|assignment| assignment.target.id.as_str()),
        Some("cauchy-bound"),
        "the batch must still lead with the node the run is building on"
    );
    let ordered = next_batch(&root, 1);
    assert_eq!(
        ordered.first().map(|assignment| &assignment.target.id),
        batch.first().map(|assignment| &assignment.target.id),
        "a batch of one and the head of a larger batch are the same node"
    );
    // No node is offered twice in one pass: two delegations for one statement
    // would both write the same file.
    let mut ids: Vec<&str> = batch
        .iter()
        .map(|assignment| assignment.target.id.as_str())
        .collect();
    let taken = ids.len();
    ids.sort_unstable();
    ids.dedup();
    assert_eq!(ids.len(), taken, "a node appears twice in one batch");
}

/// A limit is a ceiling, not a demand.
#[test]
fn a_batch_larger_than_the_ranking_returns_what_there_is() {
    let root = two_kinds_of_target("short");

    let batch = next_batch(&root, 1_000);

    assert!(!batch.is_empty());
    assert!(
        batch.len() < 1_000,
        "the fixture cannot supply a thousand nodes"
    );
}

/// Zero means zero, rather than the whole ranking.
///
/// Asserted because the guard is a bare early return, and the failure it
/// prevents — a misparsed override sweeping the entire blueprint in one pass —
/// looks nothing like a zero when it happens.
#[test]
fn a_batch_of_none_is_none() {
    let root = two_kinds_of_target("zero");

    assert!(next_batch(&root, 0).is_empty());
}
