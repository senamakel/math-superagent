//! Automatic version control over the agent's own workspace.
//!
//! A long investigation overwrites its own files: `solution.py` is rewritten a
//! dozen times, `memory.md` is edited as beliefs change, and a wrong turn
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

use std::path::{Path, PathBuf};
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

/// Tools whose success means the workspace changed on disk.
const WRITING_TOOLS: [&str; 4] = [
    "write_tool_file",
    "write_document",
    "edit_document",
    "download_document",
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
        if self.history_path().is_dir() {
            return Ok(());
        }
        self.git(&["init", "--quiet", "--initial-branch", "work"])
            .await?;
        // The history directory must never enter its own history, and neither
        // should installed packages or the event log.
        let excludes = self.history_path().join("info").join("exclude");
        if let Some(parent) = excludes.parent() {
            let _ = tokio::fs::create_dir_all(parent).await;
        }
        let _ = tokio::fs::write(
            &excludes,
            format!("{HISTORY_DIR}/\n.python-packages/\n__pycache__/\ntrace.jsonl\n"),
        )
        .await;
        Ok(())
    }

    /// Stages everything and commits, returning the short commit id.
    ///
    /// A commit with nothing staged is not an error: two tools can write the
    /// same content, and the second finding no change is normal.
    async fn commit(&self, message: &str) -> Result<Option<String>> {
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

/// Returns the path of the workspace history directory, for callers that need
/// to exclude it.
#[must_use]
pub(super) fn history_directory(workspace: &Path) -> PathBuf {
    workspace.join(HISTORY_DIR)
}

#[cfg(test)]
mod test;
