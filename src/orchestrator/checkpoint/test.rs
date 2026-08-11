//! Unit tests for workspace checkpointing.
#![allow(clippy::expect_used)]

use super::{HISTORY_DIR, WRITING_TOOLS, WorkspaceCheckpoint, history_directory, summarise};

#[test]
fn only_writing_tools_trigger_a_checkpoint() {
    assert!(WRITING_TOOLS.contains(&"write_tool_file"));
    assert!(WRITING_TOOLS.contains(&"edit_document"));
    // Reading and running must not create commits, or history becomes noise.
    assert!(!WRITING_TOOLS.contains(&"read_document"));
    assert!(!WRITING_TOOLS.contains(&"execute_command"));
    assert!(!WRITING_TOOLS.contains(&"exa_search"));
}

#[test]
fn commit_subjects_are_one_condensed_line() {
    assert_eq!(summarise("wrote 40 bytes to solution.py"), "wrote 40 bytes to solution.py");
    assert_eq!(summarise("first line\nsecond line"), "first line");
    assert_eq!(summarise("  padded\t words  "), "padded words");
    assert_eq!(summarise(""), "workspace updated");
    assert!(summarise(&"x".repeat(200)).chars().count() <= 72);
}

#[test]
fn history_lives_beside_the_workspace_not_inside_a_dot_git() {
    let path = history_directory(std::path::Path::new("/workspace"));
    assert!(path.ends_with(HISTORY_DIR));
    // A plain `.git` would make the outer repository treat this as an
    // embedded repository and refuse to track through it.
    assert_ne!(HISTORY_DIR, ".git");
}

#[tokio::test]
async fn checkpoints_commit_only_when_content_changed() {
    let directory = std::env::temp_dir().join(format!("math-agent-ckpt-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&directory);
    std::fs::create_dir_all(&directory).expect("temporary workspace is creatable");

    let checkpoint = WorkspaceCheckpoint::new(directory.clone(), None);
    std::fs::write(directory.join("seed.txt"), "seed").expect("write is possible");
    if checkpoint.commit("seed").await.is_err() {
        // git is unavailable in this environment; the middleware degrades to a
        // no-op by design, so there is nothing further to assert.
        let _ = std::fs::remove_dir_all(&directory);
        return;
    }
    assert!(history_directory(&directory).is_dir(), "history is created lazily");

    std::fs::write(directory.join("solution.py"), "print(1)").expect("write is possible");
    let first = checkpoint.commit("first").await.expect("commit succeeds");
    assert!(first.is_some(), "a new file must produce a commit");

    // Nothing changed: committing again must be a no-op, not an error.
    let second = checkpoint.commit("second").await.expect("commit succeeds");
    assert!(second.is_none(), "an unchanged tree must not commit");

    std::fs::write(directory.join("solution.py"), "print(2)").expect("write is possible");
    let third = checkpoint.commit("third").await.expect("commit succeeds");
    assert!(third.is_some(), "an edit must produce a commit");

    let _ = std::fs::remove_dir_all(&directory);
}
