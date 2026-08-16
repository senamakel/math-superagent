//! Automatic version control over the agent's own workspace.
//!
//! A long investigation overwrites its own files: `solution.py` is rewritten a
//! dozen times, workspace artifacts are edited as beliefs change, and a wrong turn
//! silently destroys the working version that preceded it. Nothing records
//! that a file used to be right. This middleware commits the workspace after
//! every successful write, so each state is recoverable and the sequence of
//! commits is a readable account of how the answer was reached.
//!
//! # Why a separate git directory
//!
//! The workspace is a subdirectory of the product repository, which is itself
//! a git repository and now tracks workspace contents. A conventional `.git`
//! here would make the outer repository see an embedded repository and refuse
//! to track through it. Keeping history in `.workspace-history` with an
//! explicit work tree avoids that entirely: the outer repository ignores one
//! directory and sees ordinary files.

#[cfg(test)]
use std::path::Path;
use std::path::PathBuf;
use std::process::Stdio;
use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::context::RunContext;
use tinyagents::harness::middleware::Middleware;
use tinyagents::harness::tool::ToolResult;

use crate::agent::Result;
use crate::agent::trace::RunTracer;

/// Directory holding the workspace's own git history.
const HISTORY_DIR: &str = ".workspace-history";
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
/// and none of those. The old comment even said "and the event log" while
/// listing nothing that matched it.
///
/// The cost was measured rather than feared. Across thirteen live conjecture
/// workspaces, `.workspace-history` held **71.6 GB against 47 MB of
/// `research/`** — the reasoning artifacts were 0.05% of the tree. One
/// workspace committed `config/trace.jsonl` 137 times at roughly 600 MB a
/// commit, and its five largest blobs were five copies of that one file. A
/// live run rewrites the trace continuously, so it is dirty at every checkpoint
/// and lands in every batch, which is the same argument the hidden JSON caches
/// already had recorded against them.
///
/// Each entry keeps a committed human-readable counterpart beside it, which is
/// what the derivation cites and what a reader opens: `research/FRONTIER.md`
/// beside `.frontier.json`, the counts and `INDEX.md` beside a level pool, and
/// the notes beside the trace. Nothing a reader would open is dropped.
const NEVER_COMMITTED: [&str; 10] = [
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
];

/// Renders the exclude file, history directory first.
///
/// The history directory must never enter its own history, and it is written
/// here rather than in [`NEVER_COMMITTED`] because it is the one entry that is
/// about the mechanism rather than about what a reader would open.
fn exclude_file() -> String {
    let mut out = format!("{HISTORY_DIR}/\n");
    for entry in NEVER_COMMITTED {
        out.push_str(entry);
        out.push('\n');
    }
    out
}

/// Tools whose success means the workspace changed on disk.
const WRITING_TOOLS: [&str; 9] = [
    "write_tool_file",
    "write_document",
    "edit_document",
    "download_document",
    "apply_patch",
    // The ledger tools write a queue or an entry file *and* the derived
    // Markdown beside it. A writing tool missing from this list is not an
    // error anywhere — its writes are simply never committed, and the loss
    // shows up as a workspace history with a gap in it.
    "record_entry",
    "close_entry",
    "define_ledger",
    "retire_ledger",
];

/// Commits the workspace after each successful write.
#[derive(Debug)]
pub(super) struct WorkspaceCheckpoint {
    workspace: PathBuf,
    tracer: Option<Arc<RunTracer>>,
}

impl WorkspaceCheckpoint {
    /// Creates the checkpointer.
    ///
    /// The history repository is created lazily on the first commit rather
    /// than here, so construction stays synchronous and a workspace that is
    /// never written to never grows a git directory.
    pub(super) fn new(workspace: PathBuf, tracer: Option<Arc<RunTracer>>) -> Self {
        Self { workspace, tracer }
    }

    fn history_path(&self) -> PathBuf {
        self.workspace.join(HISTORY_DIR)
    }

    /// Runs one git command against the workspace history, returning its
    /// standard output.
    async fn git(&self, arguments: &[&str]) -> Result<String> {
        let mut command = tokio::process::Command::new("git");
        command
            .arg("--git-dir")
            .arg(self.history_path())
            .arg("--work-tree")
            .arg(&self.workspace)
            .args(arguments)
            .current_dir(&self.workspace)
            .env("GIT_AUTHOR_NAME", COMMIT_NAME)
            .env("GIT_AUTHOR_EMAIL", COMMIT_EMAIL)
            .env("GIT_COMMITTER_NAME", COMMIT_NAME)
            .env("GIT_COMMITTER_EMAIL", COMMIT_EMAIL)
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

    async fn initialise(&self) -> Result<()> {
        if !self.history_path().is_dir() {
            self.git(&["init", "--quiet", "--initial-branch", "work"])
                .await?;
        }
        // Rewritten on every start rather than only at init, because a
        // workspace outlives the build that made it. Every conjecture on this
        // box was created before `NEVER_COMMITTED` existed, so a write guarded
        // by "the directory is missing" would have left all of them excluding
        // four paths forever — and the 71.6 GB this constant is about was
        // already on disk. The file is small, has one writer, and is derived
        // from a constant, so rewriting it is idempotent.
        //
        // This only stops the *growth*. Bytes already in a history stay until
        // someone rewrites it, which is not this middleware's business: the
        // repository forbids rewriting published history, and a workspace's
        // history is the record of how an answer was reached.
        let excludes = self.history_path().join("info").join("exclude");
        if let Some(parent) = excludes.parent() {
            let _ = tokio::fs::create_dir_all(parent).await;
        }
        let _ = tokio::fs::write(&excludes, exclude_file()).await;
        self.untrack_excluded().await;
        Ok(())
    }

    /// Stops tracking files that are now excluded but were committed before.
    ///
    /// Without this the exclude file changes nothing on any workspace that
    /// already exists, and every workspace on this box already exists. An
    /// ignore rule applies only to *untracked* paths: `config/trace.jsonl` was
    /// committed 137 times before it was excluded, so git considers it tracked
    /// and keeps committing it no matter what `info/exclude` says. That is the
    /// failure this method exists to close, and it is invisible without it —
    /// the exclude file would look correct while the history kept growing.
    ///
    /// `git rm --cached` stages a deletion and **leaves the file on disk**,
    /// which is the required behaviour on both counts: a live run is appending
    /// to `trace.jsonl` at that moment, and `./euler-tui --replay` reads it.
    ///
    /// Failure is swallowed like every other git call here. A workspace that
    /// cannot be untracked still checkpoints correctly; it only keeps paying
    /// for the bytes, which is where it started.
    async fn untrack_excluded(&self) {
        let Ok(listed) = self
            .git(&["ls-files", "--cached", "--ignored", "--exclude-standard"])
            .await
        else {
            return;
        };
        let paths: Vec<&str> = listed.lines().map(str::trim).filter(|p| !p.is_empty()).collect();
        if paths.is_empty() {
            return;
        }
        let mut arguments = vec!["rm", "--cached", "--quiet", "--ignore-unmatch", "--"];
        arguments.extend(paths.iter().copied());
        if self.git(&arguments).await.is_ok()
            && let Some(tracer) = self.tracer.as_ref()
        {
            tracer.note(&format!(
                "workspace history: untracked {} newly excluded path(s)",
                paths.len()
            ));
        }
    }

    /// Stages everything and commits, returning the short commit id.
    ///
    /// A commit with nothing staged is not an error: two tools can write the
    /// same content, and the second finding no change is normal.
    ///
    /// Serialised across the process. This middleware is attached to every
    /// agent harness and up to fifty sub-agents may run at once, so without the
    /// lock two of them reach `git add --all` on one index together: the loser
    /// fails, leaves a stranded `index.lock` behind, and — because a checkpoint
    /// failure is deliberately swallowed below — says so nowhere. A live
    /// Erdős–Gyárfás workspace still carries one such zero-byte lock file. The
    /// staged set is the whole work tree, so a serialised commit loses nothing:
    /// the run that waits commits everything the run before it did not.
    async fn commit(&self, message: &str) -> Result<Option<String>> {
        let _guard = super::worklock::commits().await;
        self.initialise().await?;
        self.git(&["add", "--all"]).await?;
        let staged = self.git(&["diff", "--cached", "--name-only"]).await?;
        if staged.trim().is_empty() {
            return Ok(None);
        }
        self.git(&["commit", "--quiet", "--message", message])
            .await?;
        let id = self.git(&["rev-parse", "--short", "HEAD"]).await?;
        Ok(Some(id.trim().to_string()))
    }
}

#[async_trait]
impl<State: Send + Sync + 'static> Middleware<State> for WorkspaceCheckpoint {
    fn name(&self) -> &'static str {
        "workspace_checkpoint"
    }

    async fn after_tool(
        &self,
        _ctx: &mut RunContext<()>,
        _state: &State,
        result: &mut ToolResult,
    ) -> Result<()> {
        if result.is_error() || !WRITING_TOOLS.contains(&result.name.as_str()) {
            return Ok(());
        }
        let message = format!("{}: {}", result.name, summarise(&result.content));
        match self.commit(&message).await {
            Ok(Some(id)) => {
                if let Some(tracer) = self.tracer.as_ref() {
                    tracer.note(&format!("workspace checkpoint {id} ({message})"));
                }
            }
            Ok(None) => {}
            Err(error) => {
                // Never fail a tool because its checkpoint failed: the work
                // itself succeeded and losing it would be the worse outcome.
                if let Some(tracer) = self.tracer.as_ref() {
                    tracer.note(&format!("workspace checkpoint failed: {error}"));
                }
            }
        }
        Ok(())
    }
}

/// Condenses a tool result into a one-line commit subject.
fn summarise(content: &str) -> String {
    let first = content.lines().next().unwrap_or("").trim();
    let condensed = first.split_whitespace().collect::<Vec<_>>().join(" ");
    if condensed.is_empty() {
        return "workspace updated".to_string();
    }
    condensed.chars().take(72).collect()
}

/// Returns the path of the workspace history directory.
#[cfg(test)]
fn history_directory(workspace: &Path) -> PathBuf {
    workspace.join(HISTORY_DIR)
}

#[cfg(test)]
#[path = "checkpoint_test.rs"]
mod test;
