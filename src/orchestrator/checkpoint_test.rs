//! Unit tests for workspace checkpointing.
#![allow(clippy::expect_used)]

use super::super::vcs::{Git, HISTORY_DIR};
use super::{WRITING_TOOLS, WorkspaceCheckpoint, summarise};

/// Where the history of a workspace lives.
///
/// The exclude list and the repository verbs are [`super::super::vcs`]'s now;
/// what is tested here is the middleware's policy on top of them.
fn history_directory(workspace: &std::path::Path) -> std::path::PathBuf {
    Git::history(workspace).git_dir().to_path_buf()
}

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
    assert_eq!(
        summarise("wrote 40 bytes to solution.py"),
        "wrote 40 bytes to solution.py"
    );
    assert_eq!(summarise("first line\nsecond line"), "first line");
    assert_eq!(summarise("  padded\t words  "), "padded words");
    assert_eq!(summarise(""), "workspace updated");
    assert!(summarise(&"x".repeat(200)).chars().count() <= 72);
}

/// A file committed before it was excluded must stop being committed, and must
/// stay on disk.
///
/// This is the half of the fix that is easy to miss: an ignore rule applies
/// only to *untracked* paths, so adding `config/trace.jsonl` to the exclude
/// file changes nothing on a workspace that already committed it — which is
/// every workspace that exists. Without `untrack_excluded` the exclude file
/// would read correctly while the history kept growing at 600 MB a commit.
///
/// The file must survive on disk because a live run is appending to it and
/// `./euler-tui --replay` reads it, so `--cached` is load-bearing rather than
/// incidental.
#[tokio::test]
async fn a_previously_committed_event_log_is_untracked_but_left_on_disk() {
    let directory = std::env::temp_dir().join(format!("math-agent-untrack-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&directory);
    std::fs::create_dir_all(directory.join("config")).expect("temporary workspace is creatable");

    let checkpoint = WorkspaceCheckpoint::new(directory.clone(), None);
    let trace = directory.join("config").join("trace.jsonl");
    std::fs::write(&trace, "{\"event\":1}\n").expect("write is possible");
    std::fs::write(directory.join("GOAL.md"), "goal").expect("write is possible");

    // Reproduce a workspace made by the build *before* `NEVER_COMMITTED`: the
    // history exists and its exclude carries only the four original entries, so
    // the event log is committed and therefore tracked. Seeding this by hand is
    // the only way to reach the state — a fresh workspace never tracks the log,
    // so a test that let the middleware create one would pass without
    // exercising `untrack_excluded` at all.
    let git = Git::history(&directory);
    if git
        .run(&["init", "--quiet", "--initial-branch", "work"])
        .await
        .is_err()
    {
        // git is unavailable here; the middleware degrades to a no-op by design.
        let _ = std::fs::remove_dir_all(&directory);
        return;
    }
    let info = history_directory(&directory).join("info");
    std::fs::create_dir_all(&info).expect("git info directory is creatable");
    std::fs::write(
        info.join("exclude"),
        format!("{HISTORY_DIR}/\n.python-packages/\n__pycache__/\nraw/\n"),
    )
    .expect("write is possible");
    git.run(&["add", "--all"]).await.expect("staging succeeds");
    git.run(&["commit", "--quiet", "--message", "before the exclusion"])
        .await
        .expect("the seed commit succeeds");

    let seeded = git
        .run(&["ls-files"])
        .await
        .expect("listing tracked files succeeds");
    assert!(
        seeded
            .lines()
            .any(|line| line.trim() == "config/trace.jsonl"),
        "the fixture must start with the log tracked, or it proves nothing"
    );

    checkpoint
        .commit("after the exclusion")
        .await
        .expect("commit succeeds");

    let tracked = git
        .run(&["ls-files"])
        .await
        .expect("listing tracked files succeeds");
    assert!(
        !tracked.lines().any(|line| line.trim() == "config/trace.jsonl"),
        "the event log must not be tracked, but git listed:\n{tracked}"
    );
    assert!(
        tracked.lines().any(|line| line.trim() == "GOAL.md"),
        "what a reader opens must still be tracked, but git listed:\n{tracked}"
    );
    assert!(
        trace.is_file(),
        "untracking must not delete the log a live run is still appending to"
    );

    let _ = std::fs::remove_dir_all(&directory);
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
    assert!(
        history_directory(&directory).is_dir(),
        "history is created lazily"
    );

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

/// Concurrent checkpoints all land, and none leaves an `index.lock` behind.
///
/// The middleware is attached to every agent harness and up to fifty sub-agents
/// run at once, so several of them reaching `git add --all` together is the
/// ordinary case rather than a rare one. One git index cannot serve two of
/// those: the loser fails, and its failure is deliberately swallowed so the
/// tool whose work succeeded is not failed for it. The evidence that this
/// happened is a stranded zero-byte `.workspace-history/index.lock` in a live
/// Erdős–Gyárfás workspace, which is exactly what the loser leaves.
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn concurrent_checkpoints_all_land_and_leave_no_index_lock() {
    let directory =
        std::env::temp_dir().join(format!("math-agent-ckpt-race-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&directory);
    std::fs::create_dir_all(&directory).expect("temporary workspace is creatable");

    let checkpoint = std::sync::Arc::new(WorkspaceCheckpoint::new(directory.clone(), None));
    if checkpoint.commit("seed").await.is_err() {
        // git is unavailable here; the middleware degrades to a no-op by
        // design, so there is nothing to serialise and nothing to assert.
        let _ = std::fs::remove_dir_all(&directory);
        return;
    }

    let writers = 12;
    let mut tasks = tokio::task::JoinSet::new();
    for n in 0..writers {
        let checkpoint = std::sync::Arc::clone(&checkpoint);
        let directory = directory.clone();
        tasks.spawn(async move {
            std::fs::write(directory.join(format!("note{n}.md")), format!("finding {n}"))
                .expect("write is possible");
            checkpoint.commit(&format!("write_document: note{n}.md")).await
        });
    }
    while let Some(joined) = tasks.join_next().await {
        joined
            .expect("a checkpoint task must not panic")
            .expect("every concurrent checkpoint must succeed");
    }

    // A commit that found nothing staged is normal — the one before it staged
    // the whole work tree — so the property is that every file is tracked, not
    // that every call produced its own commit.
    let tracked = Git::history(&directory)
        .run(&["ls-files"])
        .await
        .expect("the history lists its files");
    for n in 0..writers {
        assert!(
            tracked.lines().any(|line| line == format!("note{n}.md")),
            "note{n}.md was written but never committed; tracked: {tracked}"
        );
    }
    assert!(
        !history_directory(&directory).join("index.lock").exists(),
        "a losing `git add` left its index lock behind"
    );

    let _ = std::fs::remove_dir_all(&directory);
}
