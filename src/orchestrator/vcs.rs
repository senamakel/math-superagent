//! The one git repository a workspace has, and the operations over it.
//!
//! [`super::checkpoint`] has committed the workspace after every write since
//! long before this module existed, into a separate git directory with an
//! explicit work tree. That machinery was private to the checkpointer and did
//! one thing: `add --all`, `commit`, `rev-parse`. Nothing could branch off it,
//! and no role could see it — a workspace had a complete history that only the
//! runtime could read.
//!
//! This is that invocation lifted out and given the rest of its verbs, so a run
//! can put several candidate solutions on their own branches, look at what each
//! changed as a diff, and keep the one that won.
//!
//! # Why a separate git directory, still
//!
//! The workspace is a subdirectory of the product repository, which is itself a
//! git repository and tracks workspace contents. A conventional `.git` here
//! would make the outer repository see an embedded repository and refuse to
//! track through it. Keeping history in `.workspace-history` with an explicit
//! work tree avoids that entirely: the outer repository ignores one directory
//! and sees ordinary files.
//!
//! # What this deliberately does not offer
//!
//! There is no "run this git command" entry point, and adding one would undo
//! the reason the module is shaped as a list of verbs. A tool taking an
//! arbitrary command line is [`super::exec`] by another name, reachable by
//! roles that were deliberately not given a shell, and no argument validation
//! can put that back. Every operation below is a function with checked
//! arguments.

use std::path::{Path, PathBuf};
use std::process::Stdio;

use crate::agent::Result;

/// Directory holding the workspace's own git history.
pub(super) const HISTORY_DIR: &str = ".workspace-history";

/// Where a candidate's own checkout lives, relative to the workspace root.
///
/// A sibling of `code/` and `research/` rather than a hidden dot-directory,
/// because the archivist has to read what a candidate wrote in order to decide
/// whether to keep it, and the hidden-entry list is what stops a file being
/// read at all.
pub(super) const ATTEMPTS_DIR: &str = "attempts";

/// Where the attempts ledger is rendered.
///
/// Beside the branches it is about rather than in the ledger module, because the
/// ledger is a declaration and this is a fact about the workspace layout.
pub(super) const ATTEMPTS_PATH: &str = "research/ATTEMPTS.md";

/// The branch the trunk of an investigation lives on.
pub(super) const TRUNK: &str = "work";

/// Prefix every candidate branch carries.
///
/// A prefix rather than a naming convention in a prompt, so listing the
/// candidates is a question git can answer and not one that depends on a role
/// having named things consistently.
pub(super) const ATTEMPT_PREFIX: &str = "attempt/";

/// Longest a git invocation may take before it is abandoned.
const GIT_TIMEOUT: std::time::Duration = std::time::Duration::from_secs(30);

/// Identity used for workspace commits.
const COMMIT_NAME: &str = "math-agent";

/// Address used for workspace commits. Non-routable by design.
const COMMIT_EMAIL: &str = "math-agent@localhost";

/// What the workspace's own history never records.
///
/// This list and the repository's `.gitignore` answer the same question about
/// the same files, and until this constant existed they disagreed. `AGENTS.md`
/// states that `trace.jsonl`, `console.log`, the bulky enumeration pools and the
/// hidden `config/.*.json` state are ignored "because a reader would never open
/// one"; the outer `.gitignore` implements that, and this exclude file — a
/// *separate* git directory with its own `info/exclude` — carried four entries
/// and none of those.
///
/// The cost was measured rather than feared. Across thirteen live conjecture
/// workspaces, `.workspace-history` held **71.6 GB against 47 MB of
/// `research/`** — the reasoning artifacts were 0.05% of the tree. One
/// workspace committed `config/trace.jsonl` 137 times at roughly 600 MB a
/// commit, and its five largest blobs were five copies of that one file.
///
/// Each entry keeps a committed human-readable counterpart beside it, which is
/// what the derivation cites and what a reader opens. Nothing a reader would
/// open is dropped.
const NEVER_COMMITTED: [&str; 11] = [
    ".python-packages/",
    "__pycache__/",
    "*.py[cod]",
    "raw/",
    // Runtime event logs. Megabytes per run, rewritten continuously, and the
    // same events are readable locally or in Langfuse. `config/` also holds
    // `config.toml` and `problem.url`, which are small and worth keeping, so
    // the bulky entries are named rather than the folder.
    "config/trace.jsonl",
    "config/console.log",
    // The run's hidden derived state — `.document-index.json`, `.frontier.json`,
    // `.requests.json`. A machine-readable cache rewritten faster than the
    // checkpoint interval, each with a committed Markdown counterpart.
    "config/.*.json",
    // Enumeration output that regrows by rerunning the program beside it. One
    // workspace's two pool files came to 527 MB, against 47 MB of reasoning
    // artifacts across every workspace on the box.
    "out/**/*_pool.txt",
    "out/**/*_classes.txt",
    "data/level_[0-9][0-9].txt",
    // Every candidate's own checkout. These are *linked worktrees* of this same
    // repository, each on its own branch, so their contents are already fully
    // recorded — committing them into the trunk as ordinary files would store
    // every candidate a second time and, worse, land a losing candidate's
    // solution in the trunk's tree where the next attempt would read it as the
    // trunk's own work.
    "attempts/",
];

/// Renders the exclude file, history directory first.
///
/// The history directory must never enter its own history, and it is written
/// here rather than in [`NEVER_COMMITTED`] because it is about the mechanism
/// rather than about what a reader would open.
fn exclude_file() -> String {
    let mut out = format!("{HISTORY_DIR}/\n");
    for entry in NEVER_COMMITTED {
        out.push_str(entry);
        out.push('\n');
    }
    out
}

/// How much of one git invocation's output is kept.
///
/// Smaller than the shell tool's ceiling because the callers differ in kind: a
/// program's output is evidence a run wants in full, and a diff is something a
/// role reads to make one decision. A diff that does not fit in this is one to
/// narrow with a path filter, which is why [`Git::diff`] takes one.
const MAX_GIT_OUTPUT: usize = 24 * 1024;

/// One workspace's history, addressed either directly or through a checkout.
///
/// Cheap to construct and holds no handle, so a caller makes one per operation
/// rather than threading it around.
#[derive(Clone, Debug)]
pub(super) struct Git {
    /// The trunk's git directory, named explicitly.
    ///
    /// `None` for a linked worktree, and that is not a shortcut. A linked
    /// worktree has its *own* `HEAD` and index under
    /// `.workspace-history/worktrees/<name>`, and naming the trunk's git
    /// directory instead points every command at the trunk's `HEAD` — so a
    /// candidate's commit lands on `work` and the isolation the branch was for
    /// is silently gone. Letting git discover the checkout's `.git` file is how
    /// it finds the right one.
    explicit: Option<PathBuf>,
    work_tree: PathBuf,
    /// Where the trunk's history lives, whichever way commands are addressed.
    history: PathBuf,
}

impl Git {
    /// The history of `workspace`, with the workspace itself as the work tree.
    pub(super) fn history(workspace: &Path) -> Self {
        let history = workspace.join(HISTORY_DIR);
        Self {
            explicit: Some(history.clone()),
            work_tree: workspace.to_path_buf(),
            history,
        }
    }

    /// The same repository, addressed through one candidate's checkout.
    ///
    /// A linked worktree shares the object store, which is what makes a
    /// candidate's branch visible to the archivist reading from the trunk
    /// without anything being pushed anywhere.
    pub(super) fn worktree(workspace: &Path, checkout: &Path) -> Self {
        Self {
            explicit: None,
            work_tree: checkout.to_path_buf(),
            history: workspace.join(HISTORY_DIR),
        }
    }

    /// Where the history lives.
    pub(super) fn git_dir(&self) -> &Path {
        &self.history
    }

    /// Whether the history has been created yet.
    pub(super) fn exists(&self) -> bool {
        self.history.is_dir()
    }

    /// Runs one git command, returning its standard output.
    ///
    /// # Errors
    ///
    /// Returns the command's standard error when git exits non-zero, and a
    /// timeout message when it outlives [`GIT_TIMEOUT`].
    pub(super) async fn run(&self, arguments: &[&str]) -> Result<String> {
        let mut command = tokio::process::Command::new("git");
        if let Some(git_dir) = self.explicit.as_ref() {
            command
                .arg("--git-dir")
                .arg(git_dir)
                .arg("--work-tree")
                .arg(&self.work_tree);
        }
        command
            .args(arguments)
            .current_dir(&self.work_tree)
            .env("GIT_AUTHOR_NAME", COMMIT_NAME)
            .env("GIT_AUTHOR_EMAIL", COMMIT_EMAIL)
            .env("GIT_COMMITTER_NAME", COMMIT_NAME)
            .env("GIT_COMMITTER_EMAIL", COMMIT_EMAIL)
            // A candidate's checkout is created by `worktree add`, so the
            // work tree may legitimately not exist yet when the trunk runs a
            // command. Without this git refuses to start in that state.
            .env("GIT_DISCOVERY_ACROSS_FILESYSTEM", "1")
            .stdin(Stdio::null())
            .kill_on_drop(true);
        let output = tokio::time::timeout(GIT_TIMEOUT, command.output())
            .await
            .map_err(|_| tinyagents::TinyAgentsError::Tool("git timed out".into()))?
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("failed to run git: {error}"))
            })?;
        if output.status.success() {
            Ok(String::from_utf8_lossy(&output.stdout).into_owned())
        } else {
            Err(tinyagents::TinyAgentsError::Tool(
                String::from_utf8_lossy(&output.stderr).trim().to_string(),
            ))
        }
    }

    /// Runs one git command and bounds what it returns.
    ///
    /// For the reading verbs, whose output a role pays for by the token.
    async fn read(&self, arguments: &[&str]) -> Result<String> {
        let raw = self.run(arguments).await?;
        Ok(super::capture::clamp(&raw, MAX_GIT_OUTPUT))
    }

    /// Creates the history if it is not there, on branch [`TRUNK`], and writes
    /// what it must never record.
    ///
    /// The exclude file is rewritten on every call rather than only at
    /// creation, because a workspace outlives the build that made it: every
    /// workspace on this box predates the current list, so a write guarded by
    /// "the directory is missing" would leave all of them excluding whatever
    /// they were created with, forever. The file is small, has one writer and is
    /// derived from a constant, so rewriting it is idempotent.
    pub(super) async fn initialise(&self) -> Result<()> {
        if !self.exists() {
            self.run(&["init", "--quiet", "--initial-branch", TRUNK])
                .await?;
        }
        let excludes = self.history.join("info").join("exclude");
        if let Some(parent) = excludes.parent() {
            let _ = tokio::fs::create_dir_all(parent).await;
        }
        let _ = tokio::fs::write(&excludes, exclude_file()).await;
        Ok(())
    }

    /// Stops tracking files that are now excluded but were committed before,
    /// returning how many.
    ///
    /// Without this the exclude file changes nothing on any workspace that
    /// already exists, and every workspace on this box already exists. An
    /// ignore rule applies only to *untracked* paths: `config/trace.jsonl` was
    /// committed 137 times before it was excluded, so git considers it tracked
    /// and keeps committing it no matter what `info/exclude` says.
    ///
    /// `git rm --cached` stages a deletion and **leaves the file on disk**,
    /// which is the required behaviour on both counts: a live run is appending
    /// to `trace.jsonl` at that moment, and `./euler-tui --replay` reads it.
    pub(super) async fn untrack_excluded(&self) -> Result<usize> {
        let listed = self
            .run(&["ls-files", "--cached", "--ignored", "--exclude-standard"])
            .await?;
        let paths: Vec<&str> = listed
            .lines()
            .map(str::trim)
            .filter(|path| !path.is_empty())
            .collect();
        if paths.is_empty() {
            return Ok(0);
        }
        let mut arguments = vec!["rm", "--cached", "--quiet", "--ignore-unmatch", "--"];
        arguments.extend(paths.iter().copied());
        self.run(&arguments).await?;
        Ok(paths.len())
    }

    /// Stages everything in the work tree and returns what is staged.
    pub(super) async fn stage_all(&self) -> Result<String> {
        self.run(&["add", "--all"]).await?;
        self.run(&["diff", "--cached", "--name-only"]).await
    }

    /// Commits what is staged, returning the short commit id.
    pub(super) async fn commit(&self, message: &str) -> Result<String> {
        self.run(&["commit", "--quiet", "--message", message])
            .await?;
        Ok(self.run(&["rev-parse", "--short", "HEAD"]).await?.trim().to_string())
    }

    /// The short id of a branch's head, or `None` when the branch is absent.
    pub(super) async fn head_of(&self, branch: &str) -> Option<String> {
        self.run(&["rev-parse", "--short", branch])
            .await
            .ok()
            .map(|id| id.trim().to_string())
            .filter(|id| !id.is_empty())
    }

    /// The subject line of a branch's head commit.
    pub(super) async fn subject_of(&self, branch: &str) -> Option<String> {
        self.run(&["log", "-1", "--format=%s", branch])
            .await
            .ok()
            .map(|line| line.trim().to_string())
            .filter(|line| !line.is_empty())
    }

    /// Every branch carrying [`ATTEMPT_PREFIX`], in creation order.
    pub(super) async fn attempt_branches(&self) -> Result<Vec<String>> {
        let listed = self
            .run(&[
                "for-each-ref",
                "--format=%(refname:short)",
                "--sort=creatordate",
                "refs/heads/attempt",
            ])
            .await?;
        Ok(listed
            .lines()
            .map(str::trim)
            .filter(|line| !line.is_empty())
            .map(ToString::to_string)
            .collect())
    }

    /// Adds a linked worktree at `checkout`, creating `branch` from `from`.
    ///
    /// `--no-checkout` is deliberately not used: a candidate starts from the
    /// trunk's files because it is a variation on them, not a blank sheet.
    pub(super) async fn worktree_add(
        &self,
        checkout: &Path,
        branch: &str,
        from: &str,
    ) -> Result<()> {
        let checkout = checkout.to_string_lossy().into_owned();
        self.run(&["worktree", "add", "-b", branch, &checkout, from])
            .await
            .map(|_| ())
    }

    /// Removes a linked worktree, keeping its branch.
    ///
    /// The branch is what the work *is*; the checkout is only where it
    /// happened. Removing the directory and keeping the branch is what lets a
    /// finished candidate stop costing disk without becoming unreviewable.
    pub(super) async fn worktree_remove(&self, checkout: &Path) -> Result<()> {
        let checkout = checkout.to_string_lossy().into_owned();
        self.run(&["worktree", "remove", "--force", &checkout])
            .await
            .map(|_| ())
    }

    /// Drops worktree records whose directories are gone.
    pub(super) async fn worktree_prune(&self) -> Result<()> {
        self.run(&["worktree", "prune"]).await.map(|_| ())
    }

    /// The checkouts that currently exist, as `(path, branch)`.
    pub(super) async fn worktrees(&self) -> Result<Vec<(String, String)>> {
        let listed = self.run(&["worktree", "list", "--porcelain"]).await?;
        let mut found = Vec::new();
        let mut path = String::new();
        for line in listed.lines() {
            if let Some(rest) = line.strip_prefix("worktree ") {
                path = rest.trim().to_string();
            } else if let Some(rest) = line.strip_prefix("branch ") {
                let branch = rest.trim().trim_start_matches("refs/heads/").to_string();
                found.push((std::mem::take(&mut path), branch));
            }
        }
        Ok(found)
    }

    /// What `branch` changed relative to where it left `base`.
    ///
    /// Three dots, not two: a candidate is judged on what *it* did, and a
    /// two-dot diff would also report everything the trunk did meanwhile as
    /// though the candidate had reverted it.
    pub(super) async fn diff(&self, base: &str, branch: &str, path: Option<&str>) -> Result<String> {
        let range = format!("{base}...{branch}");
        let mut arguments = vec!["diff", "--no-color", &range];
        if let Some(path) = path {
            arguments.push("--");
            arguments.push(path);
        }
        self.read(&arguments).await
    }

    /// The same comparison as a per-file summary.
    pub(super) async fn diff_stat(&self, base: &str, branch: &str) -> Result<String> {
        let range = format!("{base}...{branch}");
        self.read(&["diff", "--no-color", "--stat", &range]).await
    }

    /// The files `branch` changed relative to `base`.
    pub(super) async fn changed_files(&self, base: &str, branch: &str) -> Result<Vec<String>> {
        let range = format!("{base}...{branch}");
        let listed = self.run(&["diff", "--name-only", &range]).await?;
        Ok(listed
            .lines()
            .map(str::trim)
            .filter(|line| !line.is_empty())
            .map(ToString::to_string)
            .collect())
    }

    /// Every file a branch has, whether or not it changed there.
    ///
    /// Adoption needs this and the change list separately, because the two
    /// answer different questions: a path the branch never had cannot be
    /// adopted at all, and a path it has but did not change can be — it just
    /// copies what the trunk already had, which is worth saying rather than
    /// refusing.
    pub(super) async fn files_on(&self, branch: &str) -> Result<Vec<String>> {
        let listed = self
            .run(&["ls-tree", "-r", "--name-only", branch])
            .await?;
        Ok(listed
            .lines()
            .map(str::trim)
            .filter(|line| !line.is_empty())
            .map(ToString::to_string)
            .collect())
    }

    /// One branch's commit subjects, newest first.
    pub(super) async fn log(&self, branch: &str, limit: usize) -> Result<String> {
        let limit = format!("--max-count={limit}");
        self.read(&["log", "--no-color", "--format=%h %s", &limit, branch])
            .await
    }

    /// Copies the named paths out of `branch` into the work tree and stages
    /// them.
    ///
    /// This is what adopting a candidate does, and it is deliberately not a
    /// merge. A merge takes everything the branch touched, including the
    /// candidate's own notes and its ledger writes; adoption is a decision
    /// about *named files*, so the trunk keeps its own record of why it changed
    /// rather than inheriting a losing candidate's account of itself.
    pub(super) async fn adopt_paths(&self, branch: &str, paths: &[String]) -> Result<()> {
        let mut arguments = vec!["checkout", branch, "--"];
        arguments.extend(paths.iter().map(String::as_str));
        self.run(&arguments).await.map(|_| ())
    }
}

#[cfg(test)]
#[path = "vcs_test.rs"]
mod test;
