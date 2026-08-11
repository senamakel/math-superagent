//! Unit tests for the workspace summary tree.
#![allow(clippy::expect_used)]

use std::fs;
use std::path::{Path, PathBuf};

use super::*;

/// A workspace under the crate's target directory, named for its test.
fn workspace(name: &str) -> PathBuf {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("target")
        .join("context-tree-tests")
        .join(name);
    let _ = fs::remove_dir_all(&root);
    let _ = fs::create_dir_all(&root);
    root
}

/// Writes `bytes` of filler to a workspace-relative path.
fn write(root: &Path, relative: &str, bytes: usize) {
    text(root, relative, &"x".repeat(bytes));
}

/// Writes exact content to a workspace-relative path.
fn text(root: &Path, relative: &str, body: &str) {
    let path = root.join(relative);
    if let Some(parent) = path.parent() {
        let _ = fs::create_dir_all(parent);
    }
    let _ = fs::write(path, body);
}

/// Fills a batch with `count` notes.
fn fill(root: &Path, folder: &str, count: usize) {
    for index in 0..count {
        write(root, &format!("{folder}/s{index:02}.md"), 100);
    }
}

/// Rewrites a file so it counts as written after everything already on disk.
fn touch(root: &Path, relative: &str) {
    let path = root.join(relative);
    let existing = fs::read_to_string(&path).unwrap_or_default();
    // A whole second, because a filesystem storing modification times to the
    // second would otherwise record the rewrite as simultaneous.
    std::thread::sleep(std::time::Duration::from_millis(1_100));
    let _ = fs::write(path, existing);
}

/// The faults a plan reports, in order.
fn faults(root: &Path) -> Vec<Fault> {
    plan(root).into_iter().map(|task| task.fault).collect()
}

#[test]
fn a_batch_folder_names_its_level_and_its_number() {
    assert_eq!(batch_of("L0.0"), Some((0, 0)));
    assert_eq!(batch_of("L2.7"), Some((2, 7)));
    assert_eq!(batch_of("L1.12"), Some((1, 12)));
    // Every workspace was laid out flat before batches existed, so a bare
    // level still reads as its first batch.
    assert_eq!(batch_of("L1"), Some((1, 0)));
    assert_eq!(batch_of("Lib"), None);
    assert_eq!(batch_of("research"), None);
    assert_eq!(batch_dir(0, 3), "L0.3");
}

#[test]
fn notes_join_the_open_batch_and_a_full_one_opens_the_next() {
    let root = workspace("open-batch");
    // Nothing yet: the first batch is the open one.
    assert_eq!(open_batch(&root, "research", 0), 0);
    fill(&root, "research/L0.0", FANOUT - 1);
    assert_eq!(open_batch(&root, "research", 0), 0);
    write(&root, "research/L0.0/last.md", 100);
    // Full: the next batch opens rather than the batch overflowing.
    assert_eq!(open_batch(&root, "research", 0), 1);
    fill(&root, "research/L0.1", 2);
    assert_eq!(open_batch(&root, "research", 0), 1);
    // Levels are independent.
    assert_eq!(open_batch(&root, "research", 1), 0);
}

#[test]
fn a_full_batch_asks_to_be_sealed_one_level_up() {
    let root = workspace("seal");
    fill(&root, "research/L0.0", FANOUT);
    write(&root, "research/ROOT.md", 400);
    touch(&root, "research/ROOT.md");
    let task = plan(&root)
        .into_iter()
        .find(|task| matches!(task.fault, Fault::Unsealed { .. }))
        .expect("a full batch is unsealed");
    assert_eq!(task.node.path, "research/L0.0");
    assert_eq!(
        task.fault,
        Fault::Unsealed {
            summary: "research/L1.0/L0.0.md".to_string()
        }
    );
    let brief = briefing(&root).unwrap_or_default();
    assert!(brief.contains("research/L1.0/L0.0.md"), "{brief}");
    assert!(brief.contains("[[note-name]]"), "{brief}");
}

#[test]
fn a_sealed_batch_is_not_asked_for_again() {
    let root = workspace("sealed-once");
    fill(&root, "research/L0.0", FANOUT);
    write(&root, "research/L1.0/L0.0.md", 400);
    write(&root, "research/ROOT.md", 400);
    touch(&root, "research/ROOT.md");
    // A batch summarised repeatedly drifts from what it covers, so once its
    // note exists the tree stops asking.
    assert!(
        !faults(&root)
            .iter()
            .any(|fault| matches!(fault, Fault::Unsealed { .. })),
        "{:?}",
        faults(&root)
    );
}

#[test]
fn a_seal_must_link_back_to_everything_it_compressed() {
    let root = workspace("seal-links");
    fill(&root, "research/L0.0", FANOUT);
    // A seal naming only two of the ten notes has replaced the other eight
    // rather than compressed them: nothing points at their detail any more.
    text(
        &root,
        "research/L1.0/L0.0.md",
        "Together these establish the bound. See [[s00]] and [[s01]].",
    );
    write(&root, "research/ROOT.md", 400);
    touch(&root, "research/ROOT.md");
    let task = plan(&root)
        .into_iter()
        .find(|task| matches!(task.fault, Fault::Unlinked { .. }))
        .expect("a seal that drops links is reported");
    assert_eq!(task.node.path, "research/L1.0/L0.0.md");
    let Fault::Unlinked { batch, missing } = task.fault else {
        unreachable!("matched above")
    };
    assert_eq!(batch, "research/L0.0");
    assert_eq!(missing.len(), FANOUT - 2, "{missing:?}");
    assert!(missing.contains(&"research/L0.0/s09.md".to_string()));

    let brief = briefing(&root).unwrap_or_default();
    assert!(brief.contains("research/L0.0/s09.md"), "{brief}");
    assert!(brief.contains("directory, not a fold"), "{brief}");
}

#[test]
fn a_seal_that_links_its_whole_batch_is_accepted() {
    let root = workspace("seal-linked");
    fill(&root, "research/L0.0", FANOUT);
    let body = (0..FANOUT)
        .map(|index| format!("[[s{index:02}]] contributes a term."))
        .collect::<Vec<_>>()
        .join(" ");
    text(&root, "research/L1.0/L0.0.md", &body);
    write(&root, "research/ROOT.md", 400);
    touch(&root, "research/ROOT.md");
    assert!(
        !faults(&root)
            .iter()
            .any(|fault| matches!(fault, Fault::Unlinked { .. })),
        "{:?}",
        faults(&root)
    );
}

#[test]
fn a_batch_still_filling_is_left_alone() {
    let root = workspace("filling");
    fill(&root, "research/L0.0", FANOUT - 1);
    write(&root, "research/ROOT.md", 400);
    touch(&root, "research/ROOT.md");
    assert!(
        !faults(&root)
            .iter()
            .any(|fault| matches!(fault, Fault::Unsealed { .. })),
        "a batch under the fan-out is not ready to seal"
    );
}

#[test]
fn originals_are_exempt_from_the_cap_every_level_above_them_is_held_to() {
    let root = workspace("originals");
    // A real reference page converted to 91,190 characters.
    write(&root, "research/L0.0/paper.full.md", 91_190);
    write(&root, "research/L1.0/paper.md", 400);
    write(&root, "research/ROOT.md", 400);
    touch(&root, "research/ROOT.md");
    assert!(
        !faults(&root).contains(&Fault::OverBudget),
        "{:?}",
        faults(&root)
    );
}

#[test]
fn a_fold_that_outgrew_its_cap_is_reported_before_any_sealing() {
    let root = workspace("priority");
    // A seal gets four times a root's budget, so "too big" starts higher.
    write(&root, "research/L1.0/sprawling.md", 40_000);
    fill(&root, "research/L0.0", FANOUT);
    write(&root, "research/ROOT.md", 400);
    touch(&root, "research/ROOT.md");
    let faults = faults(&root);
    let budget = faults
        .iter()
        .position(|fault| *fault == Fault::OverBudget)
        .expect("an over-budget node");
    let sealing = faults
        .iter()
        .position(|fault| matches!(fault, Fault::Unsealed { .. }))
        .expect("a batch waiting to seal");
    assert!(budget < sealing, "{faults:?}");
}

#[test]
fn a_seal_is_given_room_to_be_detailed_and_a_root_is_not() {
    // The cap exists because a file is re-sent on every model call. That is
    // true of the roots a system prompt carries and false of a seal, which is
    // read on demand — and reading the two the same way produced a live seal
    // of 1,417 bytes covering 7,800 bytes of notes, one line per source.
    let root = workspace("budgets");
    // Comfortably over a root's thousand tokens, comfortably under a seal's.
    write(&root, "research/L1.0/detailed.md", 8_000);
    write(&root, "research/ROOT.md", 8_000);
    write(&root, "CONTEXT.md", 8_000);
    touch(&root, "research/ROOT.md");
    let over: Vec<String> = plan(&root)
        .into_iter()
        .filter(|task| task.fault == Fault::OverBudget)
        .map(|task| task.node.path)
        .collect();
    assert!(over.contains(&"CONTEXT.md".to_string()), "{over:?}");
    assert!(over.contains(&"research/ROOT.md".to_string()), "{over:?}");
    assert!(
        !over.contains(&"research/L1.0/detailed.md".to_string()),
        "a detailed seal is the point, not a fault: {over:?}"
    );
    const { assert!(SEAL_TOKENS > ROOT_TOKENS) };
}

#[test]
fn the_run_wide_brief_is_a_root_in_its_own_right() {
    let root = workspace("context");
    write(&root, "CONTEXT.md", 8_000);
    write(&root, "research/ROOT.md", 400);
    write(&root, "research/L0.0/a.md", 100);
    let first = plan(&root).into_iter().next().expect("a task");
    assert_eq!(first.node.path, "CONTEXT.md");
    assert_eq!(first.fault, Fault::OverBudget);
}

#[test]
fn the_root_is_not_the_index_and_neither_is_a_note() {
    let root = workspace("root-vs-index");
    write(&root, "research/L1.0/ROOT.md", 100);
    write(&root, "research/L1.0/INDEX.md", 100);
    write(&root, "research/L1.0/real.md", 100);
    // The tree's own files are never notes inside it: a fold summarising the
    // index would be summarising a directory listing.
    assert_eq!(
        super::notes(&root, "research/L1.0"),
        vec!["research/L1.0/real.md".to_string()]
    );
}

#[test]
fn a_fold_covers_what_it_links_across_the_whole_tree() {
    let root = workspace("links");
    write(&root, "research/L1.0/kept.md", 100);
    write(&root, "research/L1.0/dropped.md", 100);
    text(
        &root,
        "research/L2.0/topic.md",
        "Establishes the bound. See [[kept]] and [a page](https://example.org/x).",
    );
    // A wikilink names a note, not a path, so the whole tree is searched. The
    // external URL is not a child, and a note the fold stopped linking is not
    // one either.
    assert_eq!(
        linked(&root, "research/L2.0/topic.md"),
        vec!["research/L1.0/kept.md".to_string()]
    );
}

#[test]
fn reflections_carry_a_tree_of_their_own() {
    let root = workspace("reflections");
    fill(&root, "reflections/L0.0", FANOUT);
    let sealing = plan(&root)
        .into_iter()
        .find(|task| matches!(task.fault, Fault::Unsealed { .. }))
        .map(|task| task.node.path);
    assert_eq!(sealing, Some("reflections/L0.0".to_string()));
}

#[test]
fn a_tidy_tree_needs_nothing() {
    let root = workspace("tidy");
    write(&root, "research/L0.0/paper.full.md", 90_000);
    write(&root, "research/L1.0/paper.md", 400);
    write(&root, "research/ROOT.md", 400);
    write(&root, "CONTEXT.md", 400);
    touch(&root, "research/ROOT.md");
    touch(&root, "CONTEXT.md");
    assert_eq!(plan(&root), Vec::new());
    assert_eq!(briefing(&root), None);
}

#[test]
fn one_new_note_does_not_force_a_rewrite() {
    let root = workspace("threshold");
    write(&root, "research/ROOT.md", 400);
    write(&root, "research/L1.0/a.md", 100);
    write(&root, "research/L1.0/b.md", 100);
    write(&root, "CONTEXT.md", 100);
    touch(&root, "research/ROOT.md");
    touch(&root, "CONTEXT.md");
    write(&root, "research/L1.0/c.md", 100);
    assert_eq!(
        faults(&root)
            .into_iter()
            .filter(|fault| matches!(fault, Fault::Stale(_)))
            .count(),
        0,
        "a single new note is cheaper left for the next batch"
    );
}
