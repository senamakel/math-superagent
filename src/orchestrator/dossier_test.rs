//! Unit tests for the inventor's dossier: what it includes, in what order, and
//! what it does when it does not fit.
#![allow(clippy::expect_used)]

use super::{DEFAULT_DOSSIER_TOKENS, build, build_reduction};

/// The dossier at the budget a run actually uses.
fn inventor(root: &std::path::Path) -> String {
    build(root, DEFAULT_DOSSIER_TOKENS)
}

/// The reducer's, at the same budget.
fn reducer(root: &std::path::Path) -> String {
    build_reduction(root, DEFAULT_DOSSIER_TOKENS)
}

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-dossier-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/approaches"))?;
    std::fs::create_dir_all(root.join("research/backward"))?;
    std::fs::create_dir_all(root.join("reflections"))?;
    std::fs::create_dir_all(root.join("code/lib"))?;
    Ok(root)
}

fn write(root: &std::path::Path, relative: &str, content: &str) -> std::io::Result<()> {
    std::fs::write(root.join(relative), content)
}

/// The sections arrive in the order the argument for them runs: the goal, then
/// what has been closed, then what is established.
#[test]
fn sections_arrive_in_priority_order() -> std::io::Result<()> {
    let root = workspace("order")?;
    write(
        &root,
        "GOAL.md",
        "Prove every graph of girth 5 is 4-colourable.",
    )?;
    write(
        &root,
        "research/APPROACHES.md",
        "# Approaches\n\nA table of approaches.",
    )?;
    write(
        &root,
        "research/THREADS.md",
        "# Threads\n\nA table of threads.",
    )?;
    write(
        &root,
        "research/CLAIMS.md",
        "# Claims\n\nA table of claims.",
    )?;
    write(&root, "TASKS.md", "Some tasks.")?;

    let dossier = inventor(&root);
    let goal = dossier.find("GOAL.md").expect("the goal is included");
    let approaches = dossier
        .find("research/APPROACHES.md")
        .expect("the approaches are included");
    let threads = dossier
        .find("research/THREADS.md")
        .expect("the threads are included");
    let claims = dossier
        .find("research/CLAIMS.md")
        .expect("the claims are included");
    let tasks = dossier.find("TASKS.md").expect("the tasks are included");
    assert!(goal < approaches, "the goal precedes the approaches");
    assert!(approaches < threads, "the approaches precede the threads");
    assert!(threads < claims, "the threads precede the claims");
    assert!(claims < tasks, "the ranked sections precede the remainder");
    Ok(())
}

/// A closed approach arrives whole. Its idea is what the inventor must not
/// propose again, and the table row truncates it.
#[test]
fn a_closed_approach_arrives_whole() -> std::io::Result<()> {
    let root = workspace("closed")?;
    write(&root, "GOAL.md", "A goal.")?;
    let long = "encode the skip budget as a bivariate generating function and read the answer off \
                the diagonal, which works whenever the recursion is linear in the budget and the \
                boundary terms vanish at the origin";
    write(
        &root,
        "research/approaches/generating-function.md",
        &format!(
            "```approach\nidea: {long}\nstatus: refuted\n\
             killed-by: the boundary terms do not vanish, so the diagonal is not the answer\n```\n"
        ),
    )?;

    let dossier = inventor(&root);
    assert!(dossier.contains("boundary terms vanish at the origin"));
    assert!(dossier.contains("the diagonal is not the answer"));
    Ok(())
}

/// The goal survives a budget too small for anything else. Every other section
/// is read against what a result has to satisfy, so cutting it would make the
/// rest unreadable.
#[test]
fn the_goal_survives_a_budget_too_small_for_the_rest() -> std::io::Result<()> {
    let root = workspace("tiny")?;
    write(
        &root,
        "GOAL.md",
        "Prove the conjecture for every n above eleven.",
    )?;
    write(&root, "research/CLAIMS.md", &"claim text. ".repeat(500))?;

    // Sixty tokens is far less than the claims alone.
    let dossier = build(&root, 60);
    assert!(dossier.contains("every n above eleven"));
    assert!(!dossier.contains("research/CLAIMS.md"));
    Ok(())
}

/// A cut is announced. An inventor handed half a ledger and not told so
/// re-proposes what was in the other half, which is the failure this exists to
/// prevent.
#[test]
fn a_cut_section_says_it_was_cut() -> std::io::Result<()> {
    let root = workspace("cut")?;
    write(&root, "GOAL.md", "A goal.")?;
    write(
        &root,
        "research/CLAIMS.md",
        &"a distinctive claim sentence. ".repeat(400),
    )?;

    let dossier = build(&root, 200);
    assert!(dossier.contains("research/CLAIMS.md"));
    assert!(dossier.contains("was cut here to fit this dossier's budget"));
    assert!(dossier.contains("Read the file for the rest"));
    Ok(())
}

/// An oversized file is truncated rather than erroring. A diversify must not be
/// able to kill a run that has been going for ten hours.
#[test]
fn an_oversized_file_is_truncated_rather_than_fatal() -> std::io::Result<()> {
    let root = workspace("oversized")?;
    write(&root, "GOAL.md", "A goal.")?;
    // Larger than MAX_WORKSPACE_CONTEXT_BYTES, which the startup path rejects.
    write(&root, "research/CLAIMS.md", &"x".repeat(400 * 1024))?;

    let dossier = inventor(&root);
    assert!(!dossier.is_empty());
    assert!(dossier.contains("was cut here"));
    Ok(())
}

/// The total stays within budget, so a large workspace cannot silently hand the
/// inventor a prompt several times the size it was told to build.
#[test]
fn the_total_stays_within_budget() -> std::io::Result<()> {
    let root = workspace("budget")?;
    write(&root, "GOAL.md", "A goal.")?;
    for relative in [
        "research/APPROACHES.md",
        "research/THREADS.md",
        "research/CLAIMS.md",
        "CONTEXT.md",
        "reflections/INDEX.md",
        "TASKS.md",
        "research/FRONTIER.md",
        "research/REQUESTS.md",
        "code/lib/INDEX.md",
    ] {
        write(&root, relative, &"filler text. ".repeat(2_000))?;
    }

    let tokens = 1_000usize;
    let dossier = build(&root, 1_000);
    // The budget bounds the section bodies; the headings, the lead paragraph
    // and the cut markers are the runtime's own framing on top of it.
    let allowance = tokens * super::CHARS_PER_TOKEN * 2;
    assert!(
        dossier.chars().count() < allowance,
        "dossier was {} chars against an allowance of {allowance}",
        dossier.chars().count()
    );
    Ok(())
}

/// A missing file is the ordinary state of most of a workspace for most of a
/// run, and is skipped rather than announced or fatal.
#[test]
fn missing_files_are_skipped_silently() -> std::io::Result<()> {
    let root = workspace("missing")?;
    write(&root, "GOAL.md", "A goal.")?;

    let dossier = inventor(&root);
    assert!(dossier.contains("A goal."));
    assert!(!dossier.contains("research/CLAIMS.md"));
    assert!(!dossier.contains("TASKS.md"));
    Ok(())
}

/// An empty workspace produces nothing rather than a heading with nothing under
/// it: a child handed an empty record reasonably concludes the run has found
/// nothing, which is a different claim from the record not having been read.
#[test]
fn an_empty_workspace_produces_no_dossier() -> std::io::Result<()> {
    let root = workspace("blank")?;
    assert!(inventor(&root).is_empty());
    Ok(())
}

/// The regression this module exists for: the dossier reflects what was written
/// after the run started, not the workspace as it was when prompts were loaded.
#[test]
fn work_written_after_the_run_started_is_included() -> std::io::Result<()> {
    let root = workspace("fresh")?;
    write(&root, "GOAL.md", "A goal.")?;
    let before = inventor(&root);
    assert!(!before.contains("bipartite contraction"));

    // Something the run learns hours in.
    write(
        &root,
        "research/approaches/contraction.md",
        "```approach\nidea: bipartite contraction of odd cycles\nstatus: refuted\n\
         killed-by: the degree bound is not preserved\n```\n",
    )?;

    let after = inventor(&root);
    assert!(after.contains("bipartite contraction"));
    assert!(after.contains("degree bound is not preserved"));
    Ok(())
}

/// The reducer's ordering is nearly the inverse of the inventor's, and the
/// ordering *is* the argument. The claim ledger comes second, ahead of its own
/// ledger, because the cheapest result available to this role is noticing that
/// a lemma it was about to call a gap is already proved — and a claim ledger
/// truncated away is a lemma proved twice.
#[test]
fn the_reduction_dossier_leads_with_the_goal_then_what_is_established()
-> std::io::Result<()> {
    let root = workspace("reduction-order")?;
    write(&root, "GOAL.md", "Prove b_k >= 1 for every k.")?;
    write(&root, "research/CLAIMS.md", "# Claims\n\nA table of claims.")?;
    write(
        &root,
        "research/BACKWARD.md",
        "# Backward\n\nA table of skeletons.",
    )?;
    write(&root, "research/THREADS.md", "# Threads\n\nA table.")?;
    write(&root, "TASKS.md", "Some tasks.")?;

    let dossier = reducer(&root);
    let goal = dossier.find("GOAL.md").expect("the goal is included");
    let claims = dossier
        .find("research/CLAIMS.md")
        .expect("the claims are included");
    let backward = dossier
        .find("research/BACKWARD.md")
        .expect("the skeletons are included");
    let threads = dossier
        .find("research/THREADS.md")
        .expect("the threads are included");
    let tasks = dossier.find("TASKS.md").expect("the tasks are included");
    assert!(goal < claims, "the goal precedes what the run established");
    assert!(claims < backward, "the claims precede the ledger they close");
    assert!(backward < threads);
    assert!(threads < tasks, "the ranked sections precede the remainder");
    // The method ledger is this role's boundary, in the dossier as in its
    // prompt context: a role holding it drifts into proposing methods.
    assert!(!dossier.contains("research/APPROACHES.md"));
    Ok(())
}

/// A closed reduction reaches the reducer whole rather than as a truncated row,
/// for the reason a closed approach reaches the inventor whole: the inference
/// and the reason it broke only prevent a restatement if they arrive together.
#[test]
fn a_closed_reduction_reaches_the_reducer_whole() -> std::io::Result<()> {
    let root = workspace("reduction-closed")?;
    write(&root, "GOAL.md", "A goal.")?;
    let before = reducer(&root);
    assert!(!before.contains("uniform in k"));

    write(
        &root,
        "research/backward/induction.md",
        "```skeleton\ngoal: the conjecture holds\n\
         implies: the two lemmas combine by induction on k\nstatus: spent\n\
         killed-by: the induction needs a bound uniform in k\n```\n",
    )?;

    let after = reducer(&root);
    assert!(after.contains("Decompositions this run has already closed"));
    assert!(after.contains("combine by induction on k"));
    assert!(after.contains("uniform in k"));
    Ok(())
}
