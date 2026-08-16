#![allow(clippy::expect_used)]

//! What the statement graph has to get right.
//!
//! Every test here writes real skeleton and note files and reads the derived
//! graph back, rather than constructing `Node`s directly. The bugs this file
//! exists to catch live in the join between two files written by two roles at
//! two different times, so a test that skipped the parse would not see them.

use std::fmt::Write as _;
use std::path::Path;

use super::*;

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

/// A clean workspace of its own per test, named so a failure says which.
fn workspace(name: &str) -> std::path::PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-blueprint-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the workspace is creatable");
    root
}

/// The one thing this file exists to produce.
///
/// A gap whose only dependency is a proved claim is workable today; a gap
/// resting on an unproved lemma is not. `BACKWARD.md` shows both as open, and
/// a role reading it has no way to tell them apart.
#[test]
fn a_lemma_resting_only_on_settled_work_is_ready() {
    let root = workspace("ready");
    claim(
        &root,
        "bound",
        "id: cauchy-bound\nstatement: |f| <= 2\nstatus: proved\n",
    );
    skeleton(
        &root,
        "main",
        "goal: the sum is finite\nimplies: the two lemmas combine by summation\nrests-on: cauchy-bound\n",
        &[
            "id: tail-bound\nlemma: the tail is o(1)\nstatus: open\nnext: sum the bound\n",
            "id: head-bound\nlemma: the head is bounded\nstatus: open\ndischarged-by:\nnext: expand\n",
        ],
    );

    let blueprint = collect(&root);
    let ready: Vec<&str> = blueprint.ready().iter().map(|node| node.id.as_str()).collect();

    assert!(
        ready.contains(&"main/tail-bound"),
        "a gap with no unsettled dependency is ready, got {ready:?}"
    );
    assert!(
        !ready.contains(&"main"),
        "the goal rests on two open lemmas, so it is blocked, got {ready:?}"
    );
}

/// A blocked node must not be offered as work.
#[test]
fn a_goal_over_open_lemmas_is_blocked_not_ready() {
    let root = workspace("blocked");
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: lemma one gives it directly\n",
        &["id: one\nlemma: the hard part\nstatus: open\nnext: try induction\n"],
    );

    let blueprint = collect(&root);
    let (_, ready, blocked) = blueprint.counts();

    assert_eq!(ready, 1, "only the lemma is ready");
    assert_eq!(blocked, 1, "the goal above it is blocked");
}

/// The failure a flat ledger cannot see.
///
/// Two skeletons, each proving what the other assumes. Every individual file
/// reads as a sound reduction; together they prove nothing.
#[test]
fn a_reduction_proving_itself_is_reported_as_circular() {
    let root = workspace("circular");
    skeleton(
        &root,
        "alpha",
        "goal: A holds\nimplies: B gives A\n",
        &["id: beta\nlemma: B holds\nstatus: open\nnext: see the other skeleton\n"],
    );
    skeleton(
        &root,
        "beta",
        "goal: B holds\nimplies: A gives B\n",
        &["id: alpha\nlemma: A holds\nstatus: open\nnext: see the other skeleton\n"],
    );

    let blueprint = collect(&root);

    assert!(
        blueprint.is_circular(),
        "alpha needs beta and beta needs alpha, which is a cycle"
    );
    assert!(
        blueprint.render().contains("Circular — read this first"),
        "the cycle is reported above everything else"
    );
}

/// An acyclic graph must not be accused of circularity.
///
/// The cycle search walks shared nodes more than once, and a diamond is the
/// shape that makes a naive visited-set implementation report a false loop.
#[test]
fn a_diamond_dependency_is_not_a_cycle() {
    let root = workspace("diamond");
    claim(
        &root,
        "base",
        "id: base\nstatement: the base estimate\nstatus: proved\n",
    );
    skeleton(
        &root,
        "left",
        "goal: the left branch\nimplies: base gives it\nrests-on: base\n",
        &["id: l\nlemma: left lemma\nstatus: discharged\ndischarged-by: base\n"],
    );
    skeleton(
        &root,
        "right",
        "goal: the right branch\nimplies: base gives it\nrests-on: base\n",
        &["id: r\nlemma: right lemma\nstatus: discharged\ndischarged-by: base\n"],
    );
    skeleton(
        &root,
        "top",
        "goal: the theorem\nimplies: the branches combine\nrests-on: left, right\n",
        &["id: join\nlemma: the branches combine\nstatus: open\nnext: combine them\n"],
    );

    let blueprint = collect(&root);

    assert!(
        !blueprint.is_circular(),
        "two paths to one node is a diamond, not a cycle:\n{}",
        blueprint.render()
    );
}

/// A kernel check has to reach the proposition it was written for.
///
/// This is the join `lean_check` was built for, one level up. Formalising a
/// lemma that leaves the goal above it reading exactly as before would make
/// the strongest artifact the runtime produces invisible to the planner.
#[test]
fn a_kernel_verdict_propagates_to_the_lemma_it_discharges() {
    let root = workspace("kernel");
    std::fs::create_dir_all(root.join(super::super::lean::VERDICT_DIR))
        .expect("the verdict directory is creatable");
    std::fs::write(
        root.join(super::super::lean::VERDICT_DIR)
            .join("code_bound.lean.json"),
        r#"{"file":"code/bound.lean","compiled":true,"sorries":[],
            "axioms":["'main' depends on axioms: [propext]"],"verified":true}"#,
    )
    .expect("the verdict is writable");
    claim(
        &root,
        "bound",
        "id: bound\nstatement: the bound\nstatus: formalised\nformalisation: code/bound.lean\n",
    );
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the bound gives it\n",
        &["id: b\nlemma: the bound\nstatus: discharged\ndischarged-by: bound\n"],
    );

    let blueprint = collect(&root);
    let (verified, _, _) = blueprint.counts();

    assert!(
        verified >= 1,
        "the kernel-checked claim stands at verified:\n{}",
        blueprint.render()
    );
}

/// A refuted lemma must break what rests on it.
///
/// The direction that matters: a false lemma left local would leave the goal
/// above it looking live, and the next attempt would spend itself on it.
#[test]
fn a_refuted_lemma_breaks_the_goal_above_it() {
    let root = workspace("refuted");
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the lemma gives it\n",
        &["id: one\nlemma: the false thing\nstatus: refuted\n"],
    );

    let blueprint = collect(&root);
    let rendered = blueprint.render();

    assert!(
        rendered.contains("| `main` | goal | refuted |"),
        "the goal inherits the refutation:\n{rendered}"
    );
}

/// An id nobody wrote is a fault worth naming, not a silent no-op.
#[test]
fn a_dependency_on_nothing_is_reported() {
    let root = workspace("dangling");
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the missing claim gives it\nrests-on: not-written-down\n",
        &["id: one\nlemma: a lemma\nstatus: open\nnext: start\n"],
    );

    let rendered = collect(&root).render();

    assert!(
        rendered.contains("`not-written-down`"),
        "the missing dependency is named:\n{rendered}"
    );
    assert!(
        rendered.contains("Resting on nothing that exists"),
        "and it is filed under its own heading:\n{rendered}"
    );
}

/// An asserted claim is a reason to believe, not a settled dependency.
///
/// The permissive reading is the dangerous one: a goal reported ready because
/// it rests on a sentence somebody typed is exactly the confusion the claim
/// ledger's status field exists to prevent.
#[test]
fn an_asserted_claim_does_not_settle_what_rests_on_it() {
    let root = workspace("asserted");
    claim(
        &root,
        "guess",
        "id: guess\nstatement: probably true\nstatus: asserted\n",
    );
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the guess gives it\nrests-on: guess\n",
        &["id: one\nlemma: a lemma\nstatus: discharged\ndischarged-by: guess\n"],
    );

    let blueprint = collect(&root);
    let ready: Vec<&str> = blueprint.ready().iter().map(|node| node.id.as_str()).collect();

    assert!(
        !ready.contains(&"main"),
        "an asserted claim does not make the goal above it ready, got {ready:?}"
    );
}

/// An empty workspace must render a file that says so rather than an error.
#[test]
fn an_empty_workspace_renders_an_invitation() {
    let root = workspace("empty");
    let rendered = collect(&root).render();

    assert!(
        rendered.contains("Nothing to graph yet"),
        "an empty graph says what to write:\n{rendered}"
    );
}

/// The briefing is what reaches the next attempt, so it must carry the work.
#[test]
fn the_briefing_names_the_ready_lemmas() {
    let root = workspace("briefing");
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the lemma gives it\n",
        &["id: one\nlemma: the attackable part\nstatus: open\nnext: induct\n"],
    );

    let briefing = collect(&root).briefing();

    assert!(
        briefing.contains("main/one"),
        "the ready lemma reaches the attempt: {briefing}"
    );
    assert!(
        briefing.contains("the attackable part"),
        "with its statement, not only its id: {briefing}"
    );
}

/// Nothing ready and nothing circular is not worth spending prompt on.
#[test]
fn a_settled_graph_briefs_nothing() {
    let root = workspace("settled");
    claim(
        &root,
        "done",
        "id: done\nstatement: proved\nstatus: proved\n",
    );

    assert!(
        collect(&root).briefing().is_empty(),
        "a graph with no open work adds nothing to the prompt"
    );
}

/// PE 351 reached this state live inside ninety minutes: all three lemmas
/// discharged, the goal still blocked on claims nobody had verified. The empty
/// ready list told it the decomposition was at fault, which was both wrong and
/// the opposite of what to do next.
#[test]
fn a_goal_left_blocked_by_its_claims_is_not_a_decomposition_problem() {
    let root = workspace("goal-only");
    claim(&root, "base", "id: base\nstatement: the tool\nstatus: asserted\n");
    skeleton(
        &root,
        "alpha",
        "goal: the theorem\nimplies: the theorem\nstatus: live\nrests-on: base\n",
        &["id: A1\nlemma: the one lemma\nstatus: discharged\ndischarged-by: base\n"],
    );

    let graph = collect(&root);
    let rendered = graph.render();
    assert!(
        !rendered.contains("decomposition problem"),
        "no lemma is blocked, so the decomposition is not what is wrong: {rendered}"
    );
    assert!(
        rendered.contains("what remains open is the goal itself"),
        "the reader should be sent to what the goal rests on: {rendered}"
    );
}

/// The ranking is Scholze's criterion, and the criterion is about *load*.
///
/// He states it as a rule about what to formalise — "as it will be used as a
/// black box, a mistake in this proof could remain uncaught" — and prices its
/// absence against himself: an argument that "passed judgment of top
/// mathematicians, but then it turned out to contain a fatal mistake". What
/// makes a node dangerous is how many other nodes cite it, not how interesting
/// it is.
#[test]
fn the_verification_queue_is_ordered_by_what_rests_on_each_node() {
    let root = workspace("targets");
    claim(&root, "wide", "id: wide\nstatement: the estimate\nstatus: proved\n");
    claim(&root, "narrow", "id: narrow\nstatement: a side fact\nstatus: proved\n");
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the lemmas combine\nrests-on: wide\n",
        &[
            "id: one\nlemma: the first step\nstatus: open\ndischarged-by: wide\nnext: expand\n",
            "id: two\nlemma: the second step\nstatus: open\ndischarged-by: wide\nnext: expand\n",
            "id: three\nlemma: the third step\nstatus: open\ndischarged-by: narrow\nnext: expand\n",
        ],
    );

    let targets = collect(&root).targets();
    let ids: Vec<&str> = targets.iter().map(|target| target.id.as_str()).collect();

    assert_eq!(
        ids.first(),
        Some(&"wide"),
        "three nodes rest on `wide` and one on `narrow`: {ids:?}"
    );
    let wide = targets.first().expect("the queue is not empty");
    assert_eq!(wide.load, 3);
    assert!(wide.established, "the run is already building on it");
}

/// The two kinds of candidate are not interchangeable, and the order between
/// them is the argument rather than a tie-break.
///
/// A node the run treats as settled is being used as a black box right now, so
/// a mistake in it compounds silently. An open node has to be *proved* before
/// the kernel can check it, and the kernel is an expensive way to discover that
/// nobody has proved it yet.
#[test]
fn an_established_node_outranks_an_open_one_that_more_rests_on() {
    let root = workspace("established-first");
    claim(&root, "held", "id: held\nstatement: the estimate\nstatus: proved\n");
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the lemmas combine\n",
        &[
            "id: open-hub\nlemma: the hub\nstatus: open\nnext: expand\n",
            "id: a\nlemma: first user\nstatus: open\ndischarged-by: open-hub\nnext: expand\n",
            "id: b\nlemma: second user\nstatus: open\ndischarged-by: open-hub\nnext: expand\n",
            "id: c\nlemma: third user\nstatus: open\ndischarged-by: held\nnext: expand\n",
        ],
    );

    let targets = collect(&root).targets();
    let first = targets.first().expect("the queue is not empty");

    assert_eq!(
        first.id, "held",
        "an established node comes first even though more rests on the open hub"
    );
}

/// A node the kernel has already checked is not a candidate, and neither is one
/// nothing could establish.
#[test]
fn the_queue_holds_only_nodes_a_check_could_settle() {
    let root = workspace("queue-membership");
    // A real passing verdict, not a claim that says `formalised`. The ledger
    // downgrades the second to `asserted`, so a test that wrote only the word
    // would be asserting that an unchecked claim is excluded — the opposite of
    // what this is about.
    std::fs::create_dir_all(root.join(super::super::lean::VERDICT_DIR))
        .expect("the verdict directory is creatable");
    std::fs::write(
        root.join(super::super::lean::VERDICT_DIR)
            .join("code_done.lean.json"),
        r#"{"file":"code/done.lean","compiled":true,"sorries":[],
            "axioms":["'done' depends on axioms: [propext]"],"verified":true}"#,
    )
    .expect("the verdict is writable");
    claim(
        &root,
        "done",
        "id: done\nstatement: checked already\nstatus: formalised\nformalisation: code/done.lean\n",
    );
    skeleton(
        &root,
        "main",
        "goal: the theorem\nimplies: the lemmas combine\n",
        &[
            "id: blocked\nlemma: rests on an open lemma\nstatus: open\ndischarged-by: leaf\nnext: expand\n",
            "id: leaf\nlemma: the open leaf\nstatus: open\nnext: expand\n",
            "id: gone\nlemma: broken\nstatus: refuted\nnext: expand\n",
        ],
    );

    let ids: Vec<String> = collect(&root)
        .targets()
        .into_iter()
        .map(|target| target.id)
        .collect();

    assert!(
        !ids.iter().any(|id| id == "done"),
        "the kernel has already spoken: {ids:?}"
    );
    assert!(
        !ids.iter().any(|id| id.ends_with("/blocked")),
        "a blocked node cannot be proved before the thing under it is: {ids:?}"
    );
    assert!(
        !ids.iter().any(|id| id.ends_with("/gone")),
        "a refuted node is false: {ids:?}"
    );
    assert!(
        ids.iter().any(|id| id.ends_with("/leaf")),
        "the ready leaf is a candidate: {ids:?}"
    );
}
