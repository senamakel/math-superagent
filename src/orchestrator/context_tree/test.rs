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
fn a_tidy_tree_needs_nothing() {
    let root = workspace("tidy");
    write(&root, "research/L0/paper.full.md", 90_000);
    write(&root, "research/L1/paper.md", 400);
    write(&root, "research/INDEX.md", 400);
    write(&root, "context.md", 400);
    touch(&root, "research/INDEX.md");
    touch(&root, "context.md");
    assert_eq!(plan(&root), Vec::new());
    assert_eq!(briefing(&root), None);
}

#[test]
fn originals_are_exempt_from_the_cap_every_level_above_them_is_held_to() {
    let root = workspace("originals");
    // A real reference page converted to 91,190 characters. It is the level
    // the tree exists to keep, so it is never the thing reported as too big.
    write(&root, "research/L0/paper.full.md", 91_190);
    write(&root, "research/L1/paper.md", 400);
    write(&root, "research/INDEX.md", 400);
    touch(&root, "research/INDEX.md");
    assert!(
        !faults(&root).contains(&Fault::OverBudget),
        "{:?}",
        faults(&root)
    );
}

#[test]
fn an_oversized_root_is_the_first_thing_reported() {
    let root = workspace("oversized");
    // Over a thousand tokens at four characters each.
    write(&root, "context.md", 8_000);
    write(&root, "research/INDEX.md", 400);
    write(&root, "research/L1/a.md", 100);
    let first = plan(&root).into_iter().next().expect("a task");
    assert_eq!(first.fault, Fault::OverBudget);
    assert_eq!(first.node.path, "context.md");
    let brief = briefing(&root).unwrap_or_default();
    assert!(brief.contains("context.md"), "{brief}");
    assert!(brief.contains("[[note-name]]"), "{brief}");
}

#[test]
fn a_digest_that_outgrew_its_own_cap_is_reported_like_any_other_node() {
    let root = workspace("fat-digest");
    write(&root, "research/INDEX.md", 400);
    write(&root, "research/L1/sprawling.md", 9_000);
    touch(&root, "research/INDEX.md");
    let first = plan(&root).into_iter().next().expect("a task");
    assert_eq!(first.node.path, "research/L1/sprawling.md");
    assert_eq!(first.fault, Fault::OverBudget);
}

#[test]
fn budget_outranks_structure_and_structure_outranks_freshness() {
    let root = workspace("priority");
    write(&root, "research/INDEX.md", 8_000);
    for index in 0..12 {
        write(&root, &format!("research/L1/s{index:02}.md"), 100);
    }
    let faults = faults(&root);
    let budget = faults
        .iter()
        .position(|fault| *fault == Fault::OverBudget)
        .expect("an over-budget node");
    let structure = faults
        .iter()
        .position(|fault| matches!(fault, Fault::Unfolded(_)))
        .expect("an outgrown level");
    let freshness = faults
        .iter()
        .position(|fault| matches!(fault, Fault::Stale(_)))
        .expect("a stale node");
    assert!(budget < structure, "{faults:?}");
    assert!(structure < freshness, "{faults:?}");
}

#[test]
fn a_level_wider_than_the_fanout_is_told_where_the_next_one_goes() {
    let root = workspace("unfolded");
    write(&root, "research/INDEX.md", 400);
    for index in 0..23 {
        write(&root, &format!("research/L1/s{index:02}.md"), 100);
    }
    touch(&root, "research/INDEX.md");
    let brief = briefing(&root).unwrap_or_default();
    // Twenty-three notes at ten to a fold is three folds, not two.
    assert!(brief.contains('3'), "{brief}");
    assert!(brief.contains("research/L2/"), "{brief}");
    assert!(brief.contains("research/L1/s22.md"), "{brief}");
}

#[test]
fn the_index_folds_the_highest_level_present() {
    let root = workspace("levels");
    write(&root, "research/INDEX.md", 400);
    for index in 0..15 {
        write(&root, &format!("research/L1/s{index:02}.md"), 100);
    }
    write(&root, "research/L2/one.md", 100);
    write(&root, "research/L2/two.md", 100);
    touch(&root, "research/INDEX.md");
    let children = plan(&root)
        .into_iter()
        .find(|task| task.node.path == "research/INDEX.md")
        .map(|task| task.node.children);
    // Fifteen notes stop being the index's problem once L2 covers them, so
    // the index is settled rather than reported as fifteen-wide.
    assert_eq!(children, None, "{:?}", faults(&root));
}

#[test]
fn a_flat_folder_is_read_as_the_first_level_it_always_was() {
    let root = workspace("flat");
    // Every workspace started flat and several are running now.
    write(&root, "research/paper.md", 100);
    write(&root, "research/other.md", 100);
    write(&root, "research/INDEX.md", 400);
    assert_eq!(
        levels(&root, "research"),
        vec![(
            1,
            vec![
                "research/other.md".to_string(),
                "research/paper.md".to_string()
            ]
        )]
    );
}

#[test]
fn reflections_carry_a_tree_of_their_own() {
    let root = workspace("reflections");
    for index in 0..12 {
        write(&root, &format!("reflections/L0/17{index:02}_1_learnings.md"), 100);
    }
    let outgrown = plan(&root)
        .into_iter()
        .find(|task| matches!(task.fault, Fault::Unfolded(_)))
        .map(|task| task.node.path);
    assert_eq!(outgrown, Some("reflections/L0".to_string()));
}

#[test]
fn a_fold_covers_what_it_links_and_no_more() {
    let root = workspace("links");
    write(&root, "research/L1/kept.md", 100);
    write(&root, "research/L1/dropped.md", 100);
    text(
        &root,
        "research/L2/topic.md",
        "Establishes the bound. See [[kept]] and [a page](https://example.org/x).",
    );
    let children = linked_children(
        &root,
        "research/L2/topic.md",
        &[
            "research/L1/kept.md".to_string(),
            "research/L1/dropped.md".to_string(),
        ],
    );
    // The external URL is not a child, and a note the fold stopped linking is
    // not one either.
    assert_eq!(children, vec!["research/L1/kept.md".to_string()]);
}

#[test]
fn both_link_spellings_resolve_to_the_same_note() {
    let root = workspace("spellings");
    write(&root, "research/L1/paper.md", 100);
    for body in [
        "[[paper]]",
        "[[paper.md]]",
        "[[paper|the source]]",
        "[[paper#Theorem 2]]",
        "[the source](../L1/paper.md)",
    ] {
        text(&root, "research/L2/topic.md", body);
        assert_eq!(
            linked_children(
                &root,
                "research/L2/topic.md",
                &["research/L1/paper.md".to_string()]
            ),
            vec!["research/L1/paper.md".to_string()],
            "{body}"
        );
    }
}

#[test]
fn a_parent_that_does_not_exist_yet_is_behind_every_note_below_it() {
    let root = workspace("missing");
    write(&root, "research/L1/a.md", 100);
    write(&root, "research/L1/b.md", 100);
    let changed = changed_since(
        &root,
        "research/INDEX.md",
        &["research/L1/a.md".to_string(), "research/L1/b.md".to_string()],
    );
    assert_eq!(changed.len(), 2);
}

#[test]
fn one_new_note_does_not_force_a_refold() {
    let root = workspace("threshold");
    write(&root, "research/INDEX.md", 400);
    write(&root, "research/L1/a.md", 100);
    write(&root, "research/L1/b.md", 100);
    write(&root, "context.md", 100);
    touch(&root, "research/INDEX.md");
    touch(&root, "context.md");
    write(&root, "research/L1/c.md", 100);
    assert_eq!(
        faults(&root)
            .into_iter()
            .filter(|fault| matches!(fault, Fault::Stale(_)))
            .count(),
        0,
        "a single new note is cheaper left for the next batch"
    );
}

#[test]
fn only_one_task_is_asked_for_at_a_time() {
    let root = workspace("single");
    write(&root, "context.md", 8_000);
    write(&root, "research/INDEX.md", 8_000);
    write(&root, "research/L1/a.md", 100);
    let brief = briefing(&root).unwrap_or_default();
    assert!(brief.contains("context.md"), "{brief}");
    assert!(!brief.contains("research/INDEX.md"), "{brief}");
}
