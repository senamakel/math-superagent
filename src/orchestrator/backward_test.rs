use super::{GapStance, Stance, collect, is_backward};
use crate::orchestrator::claims;

fn skeleton(root: &std::path::Path, slug: &str, body: &str) -> std::io::Result<()> {
    std::fs::write(
        root.join(format!("{}/{slug}.md", super::BACKWARD_DIR)),
        format!("# {slug}\n\n{body}\n\nWorking notes.\n"),
    )
}

/// A skeleton block and one gap block, in the shape the prompt asks for.
fn one_gap(header: &str, gap: &str) -> String {
    format!("```skeleton\n{header}\n```\n\n```gap\n{gap}\n```\n")
}

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-backward-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join(super::BACKWARD_DIR))?;
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    Ok(root)
}

/// The table is one row per decomposition, and the open gaps below it are what
/// the forward loop actually reads.
#[test]
fn a_skeleton_becomes_a_row_and_its_gaps_become_tasks() -> std::io::Result<()> {
    let root = workspace("row")?;
    skeleton(
        &root,
        "event-rate",
        &one_gap(
            "goal: b_k >= 1 for every k\n\
             implies: the recharge identity turns the goal into a lower bound on event density\n\
             status: live\n\
             rests-on: recharge-identity",
            "id: G-density\n\
             lemma: (2,4)-events occur with density at least 1/2 past k=10\n\
             status: open\n\
             thread: research/threads/regeneration.md\n\
             next: measure per-family event density on sequences surviving past k=10",
        ),
    )?;
    std::fs::write(
        root.join("research/L1.0/recharge.md"),
        "```claim\nid: recharge-identity\nstatement: b_k = b_1 + sum(j_i + 1) - (k-1).\n```\n",
    )?;

    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("| [[event-rate]] |"));
    assert!(rendered.contains("recharge identity turns the goal"));
    assert!(rendered.contains("live"));
    assert!(rendered.contains("## The open gaps — each one is a task"));
    assert!(rendered.contains("`G-density`"));
    assert!(rendered.contains("measure per-family event density"));
    assert!(rendered.contains("research/threads/regeneration.md"));
    // Its claim is on disk, so it is not listed as resting on nothing.
    assert!(!rendered.contains("## Resting on nothing recorded"));
    Ok(())
}

/// A gap nobody is attacking looks exactly like one being worked unless the
/// ledger says otherwise, and the difference is the reason gaps are tracked
/// separately at all.
#[test]
fn a_gap_with_no_thread_is_called_out() -> std::io::Result<()> {
    let root = workspace("threadless")?;
    skeleton(
        &root,
        "untouched",
        &one_gap(
            "goal: the conjecture holds\nimplies: L1 and L2 together give it",
            "id: G-l1\nlemma: L1 holds for all n\nstatus: open\nnext: check n <= 100",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("_no thread — nothing is attacking this_"));
    Ok(())
}

/// A gap nobody can begin is a research request rather than a task, and the
/// ledger says which one it is looking at.
#[test]
fn a_gap_with_no_first_step_is_called_out() -> std::io::Result<()> {
    let root = workspace("stepless")?;
    skeleton(
        &root,
        "vague",
        &one_gap(
            "goal: the conjecture holds\nimplies: L1 gives it",
            "id: G-l1\nlemma: L1 holds for all n\nstatus: open",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("no first step"));
    Ok(())
}

/// The single failure this ledger exists to prevent: a later turn restating a
/// lemma the run already closed.
#[test]
fn a_discharged_gap_keeps_what_closed_it() -> std::io::Result<()> {
    let root = workspace("discharged")?;
    skeleton(
        &root,
        "step-law",
        &one_gap(
            "goal: the step law holds for any array\n\
             implies: the drain law follows from it directly\n\
             status: live",
            "id: G-step\n\
             lemma: b_{k+1} >= b_k iff (x,y) = (2,4)\n\
             status: discharged\n\
             discharged-by: step-law-proved",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("## Gaps already discharged"));
    assert!(rendered.contains("step-law-proved"));
    // A discharged gap is not offered to the next attempt as a target.
    assert!(!rendered.contains("## The open gaps — each one is a task"));
    Ok(())
}

/// A closed gap with nothing naming what closed it cannot stop a restatement,
/// so the ledger says so rather than presenting it as settled.
#[test]
fn a_discharged_gap_without_a_closer_is_called_out() -> std::io::Result<()> {
    let root = workspace("uncloseed")?;
    skeleton(
        &root,
        "loose",
        &one_gap(
            "goal: G\nimplies: L gives it\nstatus: live",
            "id: G-l\nlemma: L holds\nstatus: discharged",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("nothing named"));
    Ok(())
}

/// A decomposition that does not recombine into the goal is the failure the
/// whole file exists to make visible, so the reason it broke is kept.
#[test]
fn a_broken_reduction_keeps_its_reason() -> std::io::Result<()> {
    let root = workspace("broken")?;
    skeleton(
        &root,
        "rule90-timing",
        "```skeleton\n\
         goal: regeneration happens at depth 2^j\n\
         implies: the Rule 90 interior forces an edge flip at those depths\n\
         status: broken\n\
         killed-by: the depth-2^j timing corollary was refuted at depth 48\n\
         ```\n",
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("## Reductions that broke, and why"));
    assert!(rendered.contains("refuted at depth 48"));
    Ok(())
}

/// A closed reduction's gaps are not offered as targets: proving one buys the
/// run nothing, because the reduction they belonged to is broken.
#[test]
fn a_broken_reduction_does_not_contribute_open_gaps() -> std::io::Result<()> {
    let root = workspace("closed-gaps")?;
    skeleton(
        &root,
        "dead",
        &one_gap(
            "goal: G\nimplies: L gives it\nstatus: broken\nkilled-by: L does not imply G",
            "id: G-l\nlemma: L holds\nstatus: open\nnext: check it",
        ),
    )?;
    let skeletons = collect(&root);
    assert!(skeletons.open_gaps().is_empty());
    assert!(
        !skeletons
            .render(&claims::collect(&root))
            .contains("## The open gaps — each one is a task")
    );
    Ok(())
}

/// Computed, not asked for. A prompt telling a role not to restate a closed
/// lemma is not a control; this row is.
#[test]
fn a_gap_reopened_after_discharge_is_visible() -> std::io::Result<()> {
    let root = workspace("reopened")?;
    skeleton(
        &root,
        "first",
        &one_gap(
            "goal: G\nimplies: L gives it\nstatus: live",
            "id: G-l\nlemma: L holds\nstatus: discharged\ndischarged-by: claim-l",
        ),
    )?;
    skeleton(
        &root,
        "second",
        &one_gap(
            "goal: G again\nimplies: L gives it\nstatus: sketched",
            "id: G-l\nlemma: L holds\nstatus: open\nnext: prove L",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("## Re-opened after being discharged"));
    assert!(rendered.contains("discharged elsewhere in this ledger"));
    Ok(())
}

/// A reduction taking an unrecorded belief as input proves the goal from
/// something nobody downstream can check.
#[test]
fn a_reduction_resting_on_no_claim_is_flagged() -> std::io::Result<()> {
    let root = workspace("unsupported")?;
    skeleton(
        &root,
        "floating",
        &one_gap(
            "goal: G\nimplies: L gives it\nrests-on: never-written-down",
            "id: G-l\nlemma: L holds\nstatus: open\nnext: prove L",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("## Resting on nothing recorded"));
    assert!(rendered.contains("`never-written-down`"));
    Ok(())
}

/// The load-bearing field. Three attractive lemmas that do not recombine into
/// the goal is what a decomposition role gets wrong, and a file that never
/// stated the inference cannot be checked for it.
#[test]
fn a_skeleton_that_never_says_how_the_lemmas_combine_is_a_fault() -> std::io::Result<()> {
    let root = workspace("no-implies")?;
    skeleton(
        &root,
        "listing",
        &one_gap(
            "goal: G\nstatus: sketched",
            "id: G-l\nlemma: L holds\nstatus: open\nnext: prove L",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("## Skeletons that could not be read"));
    assert!(rendered.contains("does not say how its lemmas imply the goal"));
    Ok(())
}

/// Faults for the shapes that cannot be used: no goal, no block, no gaps, and
/// a gap that cannot be tracked between two writes.
#[test]
fn the_unusable_shapes_are_each_named() -> std::io::Result<()> {
    let root = workspace("faults")?;
    skeleton(
        &root,
        "goalless",
        &one_gap(
            "implies: L gives it",
            "id: G-l\nlemma: L holds\nstatus: open\nnext: prove L",
        ),
    )?;
    skeleton(&root, "prose", "Just a paragraph, no block at all.\n")?;
    skeleton(
        &root,
        "gapless",
        "```skeleton\ngoal: G\nimplies: L gives it\nstatus: sketched\n```\n",
    )?;
    skeleton(
        &root,
        "anonymous",
        &one_gap("goal: G\nimplies: L gives it", "lemma: L holds\nstatus: open"),
    )?;
    skeleton(
        &root,
        "lemmaless",
        &one_gap("goal: G\nimplies: L gives it", "id: G-l\nstatus: open"),
    )?;
    skeleton(
        &root,
        "unclosed",
        "```skeleton\ngoal: G\nimplies: L gives it\n",
    )?;

    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("`goalless` names no goal"));
    assert!(rendered.contains("`prose` has no skeleton block"));
    assert!(rendered.contains("`gapless` has no gaps"));
    assert!(rendered.contains("`anonymous` has a gap with no id"));
    assert!(rendered.contains("`lemmaless` gap `G-l` states no lemma"));
    assert!(rendered.contains("`unclosed` has a skeleton block that was never closed"));
    Ok(())
}

/// An empty ledger says how to start one rather than rendering a bare heading.
#[test]
fn an_empty_ledger_says_how_to_write_the_first_skeleton() -> std::io::Result<()> {
    let root = workspace("empty")?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("_No skeletons yet."));
    assert!(rendered.contains("research/backward/<name>.md"));
    Ok(())
}

/// A missing directory is the ordinary state of a workspace that has never
/// reached a reduction, not an error.
#[test]
fn a_missing_directory_reads_as_no_skeletons() {
    let root = std::env::temp_dir().join("math-agent-backward-absent");
    let _ = std::fs::remove_dir_all(&root);
    assert!(collect(&root).open_gaps().is_empty());
    assert!(collect(&root).fingerprint().is_empty());
}

/// The stance vocabulary, including that a discharged reduction is the one
/// terminal state that is a result rather than a closure.
#[test]
fn stances_parse_and_only_failure_closes() {
    assert_eq!(Stance::parse("sketched"), Stance::Sketched);
    assert_eq!(Stance::parse("nonsense"), Stance::Sketched);
    assert_eq!(Stance::parse("active"), Stance::Live);
    assert_eq!(Stance::parse("Discharged"), Stance::Discharged);
    assert_eq!(Stance::parse("complete"), Stance::Discharged);
    assert_eq!(Stance::parse("broken — L is false"), Stance::Broken);
    assert_eq!(Stance::parse("exhausted"), Stance::Spent);
    assert!(Stance::Broken.is_closed());
    assert!(Stance::Spent.is_closed());
    assert!(!Stance::Discharged.is_closed());
    assert!(!Stance::Live.is_closed());
    assert_eq!(GapStance::parse("closed"), GapStance::Discharged);
    assert_eq!(GapStance::parse("false"), GapStance::Refuted);
    assert_eq!(GapStance::parse(""), GapStance::Open);
}

/// The alternative spellings a model reaches for are accepted, and keys nobody
/// defined are ignored rather than becoming faults.
#[test]
fn aliases_are_accepted_and_unknown_keys_ignored() -> std::io::Result<()> {
    let root = workspace("aliases")?;
    skeleton(
        &root,
        "aliased",
        &one_gap(
            "target: G\n\
             sufficient-because: L1 and L2 give it\n\
             stance: live\n\
             claims: known-claim\n\
             mood: optimistic",
            "gap: G-l1\n\
             statement: L1 holds\n\
             stance: open\n\
             next-step: check n <= 100\n\
             confidence: medium",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("| [[aliased]] |"));
    assert!(rendered.contains("L1 and L2 give it"));
    assert!(rendered.contains("`G-l1`"));
    assert!(rendered.contains("check n <= 100"));
    assert!(!rendered.contains("## Skeletons that could not be read"));
    Ok(())
}

/// A pipe in a field would otherwise split the row it is rendered into.
#[test]
fn a_pipe_in_a_field_does_not_break_the_table() -> std::io::Result<()> {
    let root = workspace("pipe")?;
    skeleton(
        &root,
        "piped",
        &one_gap(
            "goal: |S| >= 2 for every S\nimplies: the bound |x| <= 1 gives it",
            "id: G-s\nlemma: |S| >= 2\nstatus: open\nnext: enumerate S",
        ),
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("\\|S\\| >= 2 for every S"));
    Ok(())
}

/// The write path derives the table from these files, and must never treat the
/// table itself as one of them — a refresh triggering a refresh is a loop
/// nothing bounds.
#[test]
fn only_skeleton_files_drive_the_table() {
    assert!(is_backward("research/backward/event-rate.md"));
    assert!(!is_backward("research/BACKWARD.md"));
    assert!(!is_backward("research/backward/INDEX.md"));
    assert!(!is_backward("research/backward/notes.txt"));
    assert!(!is_backward("research/backwards/event-rate.md"));
    assert!(!is_backward("research/approaches/generating-function.md"));
    assert!(!is_backward("research/threads/regeneration.md"));
}

/// The control behind `ensure_skeleton_written`: what a turn has to move for it
/// to have done anything a downstream reader can see. A rewrite that only
/// changes prose has not, and mtime would call that a success.
#[test]
fn the_fingerprint_moves_on_a_gap_and_not_on_prose() -> std::io::Result<()> {
    let root = workspace("fingerprint")?;
    let header = "goal: G\nimplies: L gives it\nstatus: live";
    skeleton(
        &root,
        "tracked",
        &one_gap(header, "id: G-l\nlemma: L holds\nstatus: open\nnext: prove L"),
    )?;
    let before = collect(&root).fingerprint();

    // The same blocks under different prose: nothing downstream changed.
    std::fs::write(
        root.join(format!("{}/tracked.md", super::BACKWARD_DIR)),
        format!(
            "# tracked\n\n{}\n\nEntirely different working notes.\n",
            one_gap(header, "id: G-l\nlemma: L holds\nstatus: open\nnext: prove L")
        ),
    )?;
    assert_eq!(collect(&root).fingerprint(), before);

    // The gap closes: the fingerprint moves.
    skeleton(
        &root,
        "tracked",
        &one_gap(
            header,
            "id: G-l\nlemma: L holds\nstatus: discharged\ndischarged-by: claim-l",
        ),
    )?;
    assert_ne!(collect(&root).fingerprint(), before);
    Ok(())
}

/// The dossier is handed closed skeletons whole rather than as truncated rows,
/// because the inference and the reason it broke only stop a restatement if
/// they arrive together.
#[test]
fn a_closed_skeleton_renders_whole_for_the_dossier() -> std::io::Result<()> {
    let root = workspace("full")?;
    skeleton(
        &root,
        "spent-route",
        &one_gap(
            "goal: the conjecture holds\n\
             implies: the two lemmas below combine by induction on k\n\
             status: spent\n\
             rests-on: block-lemma\n\
             killed-by: the induction needs a uniform bound the run could not establish",
            "id: G-uniform\nlemma: the bound is uniform in k\nstatus: open\nnext: search",
        ),
    )?;
    let skeletons = collect(&root);
    let full: Vec<String> = skeletons.closed().map(super::Skeleton::full).collect();
    assert_eq!(full.len(), 1);
    let text = &full[0];
    assert!(text.contains("spent-route (spent)"));
    assert!(text.contains("combine by induction on k"));
    assert!(text.contains("uniform bound the run could not establish"));
    assert!(text.contains("Rests on: block-lemma"));
    assert!(text.contains("Gap `G-uniform` (open)"));
    Ok(())
}

/// What the next attempt is handed: the lemma and the move that starts on it.
#[test]
fn an_open_gap_briefs_the_next_attempt_with_its_first_step() -> std::io::Result<()> {
    let root = workspace("briefing")?;
    skeleton(
        &root,
        "event-rate",
        &one_gap(
            "goal: G\nimplies: the density bound gives it\nstatus: live",
            "id: G-density\n\
             lemma: events occur with density at least 1/2\n\
             status: open\n\
             next: measure density on survivors past k=10",
        ),
    )?;
    let skeletons = collect(&root);
    let gaps = skeletons.open_gaps();
    assert_eq!(gaps.len(), 1);
    let briefing = gaps[0].briefing();
    assert!(briefing.contains("`G-density` (event-rate)"));
    assert!(briefing.contains("density at least 1/2"));
    assert!(briefing.contains("first step: measure density on survivors"));
    Ok(())
}
