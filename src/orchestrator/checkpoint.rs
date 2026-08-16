//! Automatic version control over the agent's own workspace.
//!
//! A long investigation overwrites its own files: `solution.py` is rewritten a
//! dozen times, workspace artifacts are edited as beliefs change, and a wrong turn
//! silently destroys the working version that preceded it. Nothing records
//! that a file used to be right. This middleware commits the workspace after
//! every successful write, so each state is recoverable and the sequence of
//! commits is a readable account of how the answer was reached.
//!
//! The repository it commits into, and every verb over it, is
//! [`super::vcs`]. What stays here is the policy: which tools mean the
//! workspace changed, what the commit is called, and the rule that a failed
//! checkpoint never fails the work it was recording.

use std::path::PathBuf;
use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::context::RunContext;
use tinyagents::harness::middleware::Middleware;
use tinyagents::harness::tool::ToolResult;

use super::vcs::Git;
use crate::agent::Result;
use crate::agent::trace::RunTracer;

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
        let git = Git::history(&self.workspace);
        git.initialise().await?;
        if let Ok(untracked) = git.untrack_excluded().await
            && untracked > 0
            && let Some(tracer) = self.tracer.as_ref()
        {
            tracer.note(&format!(
                "workspace history: untracked {untracked} newly excluded path(s)"
            ));
        }
        let staged = git.stage_all().await?;
        if staged.trim().is_empty() {
            return Ok(None);
        }
        git.commit(message).await.map(Some)
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

#[cfg(test)]
#[path = "checkpoint_test.rs"]
mod test;
