#![allow(clippy::expect_used)]

use std::path::{Path, PathBuf};

use super::{ATTEMPT_PREFIX, ATTEMPTS_DIR, Git, HISTORY_DIR, NEVER_COMMITTED, TRUNK, exclude_file};

/// A workspace with an initialised history and one commit on the trunk.
///
/// Every test needs a repository that already has a root commit, because a
/// branch cannot be created from an unborn `HEAD` and that is not the state any
/// of these operations run in: the checkpointer commits long before a candidate
/// is ever branched.
async fn workspace(name: &str) -> PathBuf {
    let path = std::env::temp_dir().join(format!("vcs-test-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).expect("the test workspace is created");
    std::fs::write(path.join("GOAL.md"), "find the answer\n").expect("the seed file is written");

    let git = Git::history(&path);
    git.initialise().await.expect("the history is created");
    git.stage_all().await.expect("the seed is staged");
    git.commit("seed").await.expect("the seed is committed");
    path
}

fn attempt(id: &str) -> String {
    format!("{ATTEMPT_PREFIX}{id}")
}

#[test]
fn history_lives_beside_the_workspace_not_inside_a_dot_git() {
    let path = Git::history(Path::new("/workspace")).git_dir().to_path_buf();
    assert!(path.ends_with(HISTORY_DIR));
    // A plain `.git` would make the outer repository treat this as an
    // embedded repository and refuse to track through it.
    assert_ne!(HISTORY_DIR, ".git");
}

/// The event log is the single largest thing a workspace produces and the one
/// nothing reads out of history.
///
/// Thirteen live workspaces held 71.6 GB of `.workspace-history` against 47 MB
/// of `research/`, and one of them committed `config/trace.jsonl` 137 times at
/// roughly 600 MB a commit. `AGENTS.md` already said the file was ignored; only
/// the outer `.gitignore` implemented it, and this exclude file is a separate
/// git directory that never got the rule.
#[test]
fn the_event_log_never_enters_the_workspace_history() {
    assert!(NEVER_COMMITTED.contains(&"config/trace.jsonl"));
    assert!(NEVER_COMMITTED.contains(&"config/console.log"));
    let rendered = exclude_file();
    assert!(rendered.contains("config/trace.jsonl\n"));
    // The history directory must still lead, or it enters its own history.
    assert!(rendered.starts_with(&format!("{HISTORY_DIR}/\n")));
}

/// A candidate's checkout is a worktree of this same repository, so committing
/// it into the trunk would store every candidate twice — and would land a
/// losing candidate's files in the trunk's tree, where the next attempt reads
/// them as the trunk's own work.
#[test]
fn candidate_checkouts_never_enter_the_trunks_history() {
    assert!(NEVER_COMMITTED.contains(&"attempts/"));
    assert!(exclude_file().contains(&format!("{ATTEMPTS_DIR}/\n")));
}

/// What the exclude file drops must be exactly what has a committed readable
/// counterpart beside it — never a reasoning artifact.
///
/// This is the rule that keeps the list from growing into "whatever is large":
/// `research/` is 0.05% of the tree and is what the product is for.
#[test]
fn nothing_a_reader_would_open_is_excluded() {
    for kept in [
        "research/",
        "research/CLAIMS.md",
        "code/out/",
        "GOAL.md",
        "config/config.toml",
        "config/DIRECTIVES.md",
    ] {
        assert!(
            !NEVER_COMMITTED.contains(&kept),
            "`{kept}` is what the derivation cites and must stay in history"
        );
    }
    // The hidden caches go, and each names a Markdown counterpart that stays.
    assert!(NEVER_COMMITTED.contains(&"config/.*.json"));
    assert!(!NEVER_COMMITTED.contains(&"research/FRONTIER.md"));
}

#[tokio::test]
async fn a_candidate_checkout_is_not_committed_into_the_trunk() {
    let path = workspace("excluded").await;
    let git = Git::history(&path);
    let checkout = path.join(ATTEMPTS_DIR).join("09");
    git.worktree_add(&checkout, &attempt("09"), TRUNK)
        .await
        .expect("the worktree is created");

    let staged = git.stage_all().await.expect("the trunk stages");
    assert!(
        !staged.contains(ATTEMPTS_DIR),
        "a candidate's checkout must not be staged into the trunk: {staged}"
    );
}

#[tokio::test]
async fn a_history_is_created_on_the_trunk_branch() {
    let path = workspace("init").await;
    let git = Git::history(&path);
    assert!(git.exists());
    let head = git.head_of(TRUNK).await;
    assert!(head.is_some(), "the trunk must have a commit");
}

#[tokio::test]
async fn initialising_an_existing_history_keeps_it() {
    let path = workspace("reinit").await;
    let git = Git::history(&path);
    let before = git.head_of(TRUNK).await;
    git.initialise().await.expect("a second init is harmless");
    assert_eq!(git.head_of(TRUNK).await, before);
}

#[tokio::test]
async fn a_worktree_round_trips_and_its_branch_outlives_it() {
    let path = workspace("worktree").await;
    let git = Git::history(&path);
    let checkout = path.join("attempts").join("01");
    let branch = attempt("01");

    git.worktree_add(&checkout, &branch, TRUNK)
        .await
        .expect("the worktree is created");
    assert!(checkout.join("GOAL.md").is_file(), "it starts from the trunk");

    let listed = git.worktrees().await.expect("worktrees are listed");
    assert!(
        listed.iter().any(|(_, found)| found == &branch),
        "the new branch must be listed: {listed:?}"
    );

    git.worktree_remove(&checkout)
        .await
        .expect("the worktree is removed");
    assert!(!checkout.exists(), "the checkout is gone");
    assert!(
        git.head_of(&branch).await.is_some(),
        "the branch must survive its checkout, or the work is unreviewable"
    );
}

#[tokio::test]
async fn a_candidate_commits_onto_its_own_branch_and_the_trunk_does_not_move() {
    let path = workspace("isolation").await;
    let git = Git::history(&path);
    let checkout = path.join("attempts").join("02");
    let branch = attempt("02");
    git.worktree_add(&checkout, &branch, TRUNK)
        .await
        .expect("the worktree is created");

    let trunk_before = git.head_of(TRUNK).await;

    let candidate = Git::worktree(&path, &checkout);
    std::fs::write(checkout.join("solution.py"), "print(42)\n").expect("the candidate writes");
    candidate.stage_all().await.expect("the candidate stages");
    candidate
        .commit("candidate 02")
        .await
        .expect("the candidate commits");

    assert_eq!(
        git.head_of(TRUNK).await,
        trunk_before,
        "a candidate's commit must not move the trunk"
    );
    assert!(
        !path.join("solution.py").exists(),
        "a candidate's file must not appear in the trunk work tree"
    );
    assert_eq!(
        git.subject_of(&branch).await.as_deref(),
        Some("candidate 02")
    );
}

#[tokio::test]
async fn a_diff_reports_what_the_candidate_did_and_not_what_the_trunk_did() {
    // The three-dot range is the whole point: the trunk moving on must not read
    // as the candidate having reverted it.
    let path = workspace("threedot").await;
    let git = Git::history(&path);
    let checkout = path.join("attempts").join("03");
    let branch = attempt("03");
    git.worktree_add(&checkout, &branch, TRUNK)
        .await
        .expect("the worktree is created");

    let candidate = Git::worktree(&path, &checkout);
    std::fs::write(checkout.join("solution.py"), "print(1)\n").expect("the candidate writes");
    candidate.stage_all().await.expect("staged");
    candidate.commit("candidate work").await.expect("committed");

    // The trunk moves on independently, as it does while candidates run.
    std::fs::write(path.join("NOTES.md"), "meanwhile\n").expect("the trunk writes");
    git.stage_all().await.expect("staged");
    git.commit("trunk work").await.expect("committed");

    let diff = git.diff(TRUNK, &branch, None).await.expect("a diff is read");
    assert!(diff.contains("solution.py"), "the candidate's file: {diff}");
    assert!(
        !diff.contains("NOTES.md"),
        "the trunk's own later work must not appear as the candidate's: {diff}"
    );

    let files = git
        .changed_files(TRUNK, &branch)
        .await
        .expect("the file list is read");
    assert_eq!(files, vec!["solution.py".to_string()]);
}

#[tokio::test]
async fn adopting_takes_only_the_named_paths() {
    let path = workspace("adopt").await;
    let git = Git::history(&path);
    let checkout = path.join("attempts").join("04");
    let branch = attempt("04");
    git.worktree_add(&checkout, &branch, TRUNK)
        .await
        .expect("the worktree is created");

    let candidate = Git::worktree(&path, &checkout);
    std::fs::write(checkout.join("solution.py"), "print('kept')\n").expect("written");
    std::fs::write(checkout.join("SCRATCH.md"), "my own account\n").expect("written");
    candidate.stage_all().await.expect("staged");
    candidate.commit("candidate 04").await.expect("committed");

    git.adopt_paths(&branch, &["solution.py".to_string()])
        .await
        .expect("the named path is adopted");

    assert_eq!(
        std::fs::read_to_string(path.join("solution.py")).expect("the adopted file is in the trunk"),
        "print('kept')\n"
    );
    assert!(
        !path.join("SCRATCH.md").exists(),
        "adoption is a decision about named files, not a merge of everything"
    );
}

#[tokio::test]
async fn attempt_branches_are_listed_and_ordinary_branches_are_not() {
    let path = workspace("listing").await;
    let git = Git::history(&path);
    for id in ["05", "06"] {
        git.worktree_add(&path.join("attempts").join(id), &attempt(id), TRUNK)
            .await
            .expect("the worktree is created");
    }
    let branches = git.attempt_branches().await.expect("branches are listed");
    assert_eq!(branches, vec![attempt("05"), attempt("06")]);
    assert!(
        !branches.iter().any(|branch| branch == TRUNK),
        "the trunk is not an attempt"
    );
}

#[tokio::test]
async fn a_missing_branch_reports_absence_rather_than_failing() {
    let path = workspace("absent").await;
    let git = Git::history(&path);
    assert_eq!(git.head_of("attempt/nope").await, None);
    assert_eq!(git.subject_of("attempt/nope").await, None);
}

#[tokio::test]
async fn a_diff_larger_than_the_budget_is_bounded_and_says_so() {
    let path = workspace("bounded").await;
    let git = Git::history(&path);
    let checkout = path.join("attempts").join("07");
    let branch = attempt("07");
    git.worktree_add(&checkout, &branch, TRUNK)
        .await
        .expect("the worktree is created");

    let candidate = Git::worktree(&path, &checkout);
    let bulky: String = (0..40_000).map(|n| format!("line {n}\n")).collect();
    std::fs::write(checkout.join("pool.txt"), bulky).expect("written");
    candidate.stage_all().await.expect("staged");
    candidate.commit("a large candidate").await.expect("committed");

    let diff = git.diff(TRUNK, &branch, None).await.expect("a diff is read");
    assert!(
        diff.contains("truncated from the middle"),
        "an oversized diff must be bounded and say so"
    );
    assert!(diff.len() < 40 * 1024, "actually bounded: {}", diff.len());
}

#[tokio::test]
async fn a_failing_git_command_reports_its_standard_error() {
    let path = workspace("failure").await;
    let git = Git::history(&path);
    let error = git
        .diff(TRUNK, "attempt/does-not-exist", None)
        .await
        .expect_err("diffing an absent branch fails");
    assert!(
        !error.to_string().is_empty(),
        "a failure must carry git's own reason"
    );
}

#[tokio::test]
async fn staging_nothing_reports_nothing_staged() {
    let path = workspace("empty").await;
    let git = Git::history(&path);
    let staged = git.stage_all().await.expect("staging an unchanged tree works");
    assert!(
        staged.trim().is_empty(),
        "an unchanged tree stages nothing: {staged:?}"
    );
}

#[tokio::test]
async fn pruning_forgets_a_checkout_deleted_behind_gits_back() {
    let path = workspace("prune").await;
    let git = Git::history(&path);
    let checkout = path.join("attempts").join("08");
    git.worktree_add(&checkout, &attempt("08"), TRUNK)
        .await
        .expect("the worktree is created");
    std::fs::remove_dir_all(&checkout).expect("the checkout is deleted outside git");

    git.worktree_prune().await.expect("pruning works");
    let listed = git.worktrees().await.expect("worktrees are listed");
    assert!(
        !listed.iter().any(|(found, _)| Path::new(found) == checkout),
        "a deleted checkout must not stay on the list: {listed:?}"
    );
}
