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
    let _ = fs::create_dir_all(root.join(RESEARCH_DIR));
    root
}

/// Writes `bytes` of filler to a workspace-relative path.
fn write(root: &Path, relative: &str, bytes: usize) {
    let path = root.join(relative);
    if let Some(parent) = path.parent() {
        let _ = fs::create_dir_all(parent);
    }
    let _ = fs::write(path, "x".repeat(bytes));
}

/// Marks a file as written after everything already on disk.
fn touch(root: &Path, relative: &str) {
    let path = root.join(relative);
    let existing = fs::read_to_string(&path).unwrap_or_default();
    // A whole second, because a filesystem that stores modification times to
    // the second would otherwise record the rewrite as simultaneous.
    std::thread::sleep(std::time::Duration::from_millis(1_100));
    let _ = fs::write(path, existing);
}

#[test]
fn a_tidy_workspace_needs_nothing() {
    let root = workspace("tidy");
    write(&root, "context.md", 400);
    write(&root, "research/INDEX.md", 400);
    write(&root, "research/a.md", 100);
    touch(&root, "research/INDEX.md");
    touch(&root, "context.md");
    assert_eq!(plan(&root), Vec::new());
    assert_eq!(briefing(&root), None);
}

#[test]
fn an_oversized_root_is_the_first_thing_reported() {
    let root = workspace("oversized");
    // Over a thousand tokens at four characters each.
    write(&root, "context.md", 8_000);
    write(&root, "research/INDEX.md", 400);
    let first = plan(&root).into_iter().next().expect("a task");
    assert_eq!(first.fault, Fault::OverBudget);
    assert_eq!(first.node.path, "context.md");
    let brief = briefing(&root).unwrap_or_default();
    assert!(brief.contains("context.md"), "{brief}");
    assert!(brief.contains("link"), "{brief}");
}

#[test]
fn budget_outranks_structure_and_structure_outranks_freshness() {
    let root = workspace("priority");
    write(&root, "research/INDEX.md", 8_000);
    for index in 0..12 {
        write(&root, &format!("research/s{index:02}.md"), 100);
    }
    let faults: Vec<Fault> = plan(&root).into_iter().map(|task| task.fault).collect();
    let budget = faults
        .iter()
        .position(|fault| *fault == Fault::OverBudget)
        .expect("an over-budget node");
    let structure = faults
        .iter()
        .position(|fault| *fault == Fault::Unfolded)
        .expect("an unfolded level");
    let freshness = faults
        .iter()
        .position(|fault| matches!(fault, Fault::Stale(_)))
        .expect("a stale node");
    assert!(budget < structure, "{faults:?}");
    assert!(structure < freshness, "{faults:?}");
}

#[test]
fn a_level_wider_than_the_fanout_is_told_how_many_folds_it_needs() {
    let root = workspace("unfolded");
    write(&root, "research/INDEX.md", 400);
    for index in 0..23 {
        write(&root, &format!("research/s{index:02}.md"), 100);
    }
    touch(&root, "research/INDEX.md");
    let brief = briefing(&root).unwrap_or_default();
    // Twenty-three sources at ten to a fold is three folds, not two.
    assert!(brief.contains('3'), "{brief}");
    assert!(brief.contains("research/folds/"), "{brief}");
    assert!(brief.contains("research/s22.md"), "{brief}");
}

#[test]
fn a_root_folds_the_fold_nodes_once_they_exist() {
    let root = workspace("levels");
    write(&root, "research/INDEX.md", 400);
    for index in 0..15 {
        write(&root, &format!("research/s{index:02}.md"), 100);
    }
    write(&root, "research/folds/one.md", 100);
    write(&root, "research/folds/two.md", 100);
    touch(&root, "research/INDEX.md");
    let node = plan(&root)
        .into_iter()
        .find(|task| task.node.path == "research/INDEX.md")
        .map(|task| task.node);
    // Fifteen digests are no longer the root's problem once folds cover them,
    // so it is neither unfolded nor holding fifteen children.
    assert_eq!(
        node.map(|node| node.children),
        None,
        "the root should be settled once folds exist"
    );
}

#[test]
fn a_fold_covers_what_it_links_and_no_more() {
    let root = workspace("links");
    write(&root, "research/INDEX.md", 400);
    write(&root, "research/kept.md", 100);
    write(&root, "research/dropped.md", 100);
    let _ = fs::create_dir_all(root.join("research/folds"));
    let _ = fs::write(
        root.join("research/folds/topic.md"),
        "Establishes the bound. See [the source](../kept.md) and [a page](https://example.org/x).",
    );
    let children = linked_children(&root, "research/folds/topic.md");
    // The external URL is not a child, and a source the fold stopped linking
    // is not one either.
    assert_eq!(children, vec!["research/kept.md".to_string()]);
}

#[test]
fn a_parent_that_does_not_exist_yet_is_behind_every_child() {
    let root = workspace("missing");
    write(&root, "research/a.md", 100);
    write(&root, "research/b.md", 100);
    let changed = changed_since(
        &root,
        "research/INDEX.md",
        &["research/a.md".to_string(), "research/b.md".to_string()],
    );
    assert_eq!(changed.len(), 2);
}

#[test]
fn one_new_source_does_not_force_a_refold() {
    let root = workspace("threshold");
    write(&root, "research/INDEX.md", 400);
    write(&root, "research/a.md", 100);
    write(&root, "research/b.md", 100);
    write(&root, "context.md", 100);
    touch(&root, "research/INDEX.md");
    touch(&root, "context.md");
    write(&root, "research/c.md", 100);
    assert_eq!(
        plan(&root)
            .into_iter()
            .filter(|task| matches!(task.fault, Fault::Stale(_)))
            .count(),
        0,
        "a single new digest is cheaper left for the next batch"
    );
}

#[test]
fn originals_and_indexes_are_never_folded() {
    let root = workspace("leaves");
    write(&root, "research/paper.md", 100);
    write(&root, "research/paper.full.md", 90_000);
    write(&root, "research/INDEX.md", 400);
    assert_eq!(
        digests(&root.join(RESEARCH_DIR)),
        vec!["paper.md".to_string()],
        "the level-0 original and the index itself are not children"
    );
}

#[test]
fn only_one_task_is_asked_for_at_a_time() {
    let root = workspace("single");
    write(&root, "context.md", 8_000);
    write(&root, "research/INDEX.md", 8_000);
    let brief = briefing(&root).unwrap_or_default();
    assert!(brief.contains("context.md"), "{brief}");
    assert!(!brief.contains("research/INDEX.md"), "{brief}");
}
