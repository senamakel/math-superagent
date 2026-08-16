use super::{collect, is_thread};
use crate::orchestrator::claims;

fn thread(root: &std::path::Path, slug: &str, block: &str) -> std::io::Result<()> {
    std::fs::write(
        root.join(format!("{}/{slug}.md", super::THREADS_DIR)),
        format!("# {slug}\n\n```thread\n{block}\n```\n\nWorking notes.\n"),
    )
}

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-threads-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join(super::THREADS_DIR))?;
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    Ok(root)
}

/// The table is the topic axis: one row per direction, with what it rests on
/// and what to do next.
#[test]
fn a_thread_becomes_a_row_naming_what_it_rests_on() -> std::io::Result<()> {
    let root = workspace("row")?;
    thread(
        &root,
        "polylog-evaluation",
        "question: Can G(n) be evaluated at n=10^5 without the DP?\n\
         status: open\n\
         rests-on: trollope-delange\n\
         next: check whether the skip budget decomposes over bit positions",
    )?;
    std::fs::write(
        root.join("research/L1.0/trollope.md"),
        "```claim\nid: trollope-delange\nstatement: The summatory bit count has a closed form.\n```\n",
    )?;

    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("[[polylog-evaluation]]"));
    assert!(rendered.contains("Can G(n) be evaluated"));
    assert!(rendered.contains("trollope-delange"));
    assert!(rendered.contains("decomposes over bit positions"));
    // Its claim is on disk, so nothing is reported as unsupported.
    assert!(!rendered.contains("## Resting on nothing recorded"));
    Ok(())
}

/// A known dead end is a result. The table keeps it, and keeps the reason,
/// because that is what stops the next attempt paying for it again.
#[test]
fn a_dead_thread_keeps_its_reason() -> std::io::Result<()> {
    let root = workspace("dead")?;
    thread(
        &root,
        "sprague-grundy",
        "question: Does Sprague-Grundy reduce the board?\n\
         status: dead\n\
         blocked-by: the game is strictly partizan, so Grundy values do not apply",
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("| [[sprague-grundy]] |"));
    assert!(rendered.contains("## What is in the way"));
    assert!(rendered.contains("strictly partizan"));
    Ok(())
}

/// A thread stuck without a stated blocker is a mood, and the table says so:
/// a blocker stated precisely is the next research request.
#[test]
fn a_blocked_thread_without_a_blocker_is_called_out() -> std::io::Result<()> {
    let root = workspace("moody")?;
    thread(
        &root,
        "vague",
        "question: Why is this hard?\nstatus: blocked",
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("no blocker recorded"));
    Ok(())
}

/// A direction resting on a belief nobody wrote down cannot be checked by
/// anyone downstream, so the mismatch is surfaced rather than assumed benign.
#[test]
fn a_thread_resting_on_an_unrecorded_claim_is_surfaced() -> std::io::Result<()> {
    let root = workspace("unsupported")?;
    thread(
        &root,
        "guesswork",
        "question: Does the surrogate hold?\nstatus: open\nrests-on: never-written-down",
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("## Resting on nothing recorded"));
    assert!(rendered.contains("`never-written-down`"));
    Ok(())
}

/// A file under `threads/` with no thread block is a note, and saying so is
/// better than listing it as a direction nobody can act on.
#[test]
fn a_file_without_a_thread_block_is_reported() -> std::io::Result<()> {
    let root = workspace("noblock")?;
    std::fs::write(
        root.join(format!("{}/stray.md", super::THREADS_DIR)),
        "# Stray\n\nJust some prose.\n",
    )?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("## Threads that could not be read"));
    assert!(rendered.contains("`stray` has no thread block"));
    Ok(())
}

/// An empty folder says how to open the first thread rather than nothing.
#[test]
fn an_empty_folder_says_how_to_start() -> std::io::Result<()> {
    let root = workspace("empty")?;
    let rendered = collect(&root).render(&claims::collect(&root));
    assert!(rendered.contains("No threads yet"));
    assert!(rendered.contains("research/threads/<name>.md"));
    Ok(())
}

/// Only a thread file re-derives the thread table.
#[test]
fn the_write_path_recognises_a_thread() {
    assert!(is_thread("research/threads/passes.md"));
    assert!(!is_thread("research/threads/INDEX.md"));
    assert!(!is_thread("research/L1.0/siegel.md"));
    assert!(!is_thread("derived/THREADS.md"));
}

/// The index keeps the question and the stance, and drops the working notes.
///
/// The obligation this ledger discharges is *do not re-open a dead direction*,
/// and a line reading `` `slug` (dead) — <question> `` discharges it. What a
/// role does not need before choosing a direction is what it rests on, what is
/// in the way, and the next concrete step — all of which are a `read_ledger`
/// away and none of which fit in a prompt thirteen roles carry.
#[test]
fn the_index_keeps_the_question_and_the_stance() -> std::io::Result<()> {
    let root = workspace("index")?;
    thread(
        &root,
        "polylog-evaluation",
        "question: Can G(n) be evaluated at n=10^5 without the DP?\n\
         status: open\n\
         next: check whether the skip budget decomposes over bit positions",
    )?;
    thread(
        &root,
        "brute-force-sieve",
        "question: Does a sieve reach the bound directly?\n\
         status: dead\n\
         blocked-by: the bound is 10^12 and the sieve is linear in it",
    )?;

    let index = super::index(&root);

    assert!(index.contains("polylog-evaluation"), "{index}");
    assert!(index.contains("brute-force-sieve"), "{index}");
    assert!(index.contains("(open)"), "the stance survives: {index}");
    assert!(index.contains("(dead)"), "a dead thread reads as dead: {index}");
    assert!(index.contains("Can G(n) be evaluated"), "{index}");
    assert!(
        !index.contains("skip budget decomposes"),
        "the next step is dropped: {index}"
    );
    assert!(
        !index.contains("the sieve is linear"),
        "the blocker is dropped: {index}"
    );
    assert!(
        index.contains(r#"read_ledger { ledger: "threads""#),
        "the index names the call that fetches the rest: {index}"
    );
    Ok(())
}
