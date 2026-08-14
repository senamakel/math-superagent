//! The workflow as a document an outside agent can read and change.
//!
//! This is the payoff the migration was for. A `WorkflowGraph` is JSON, so the
//! control flow stops being Rust an agent has to recompile and becomes a
//! document it can read, patch, and have validated before anything runs.
//!
//! # Patches, not rewrites
//!
//! Every change goes through [`GraphOp`]s — `add_node`, `update_node_config`
//! (an RFC 7386 merge patch), `add_edge`, `rename_node`. `TinyFlows` states the
//! reason in its own module docs, and it is the reason worth repeating here:
//! re-emitting a whole graph on every change is token-heavy and the largest
//! source of accidental regressions, because a dropped node or a mangled edge
//! looks exactly like the graph the author meant. A patch fails as
//! *"op 3 (`add_edge`) failed"* instead.
//!
//! # Three things stand between a proposed change and a run
//!
//! - **Preview.** [`preview`] applies the ops and validates the result without
//!   saving, so an agent can look at what it is about to do.
//! - **Validation.** Every save runs `validate_all`, so a graph that would
//!   deadlock, route to a missing node, or dead-end a lane is refused at the
//!   edit rather than discovered mid-run.
//! - **Optimistic concurrency.** [`apply_if_unchanged`] takes the fingerprint
//!   the agent last read and refuses the write if the document moved underneath
//!   it. Two agents editing one workflow is the ordinary case here, not the
//!   exotic one, and last-write-wins would silently discard the loser's change.
//!
//! # Where it lives
//!
//! Under the workspace, beside everything else a run writes, because a
//! workflow *is* part of the record of how an answer was reached: the loop that
//! produced a derivation is as much a part of it as the derivation. Committed
//! for the same reason the derivation is.

use std::path::{Path, PathBuf};
use std::sync::Arc;

use tinyflows::graph_ops::GraphOp;
use tinyflows::model::WorkflowGraph;
use tinyflows::store::{
    FileWorkflowStore, WorkflowRecord, WorkflowStore, apply_workflow_ops_if_unchanged,
    create_workflow, preview_workflow_ops,
};
use tinyflows::store::types::fingerprint;

use crate::error::{Error, Result};

/// Where a workspace keeps its workflow documents and their run records.
const WORKFLOW_DIR: &str = "config/workflows";

/// The state directory beside them: revisions, locks, proposals, journal.
const STATE_DIR: &str = "config/workflow-state";

/// A workspace's workflow catalog.
#[derive(Clone)]
pub struct WorkflowCatalog {
    store: Arc<dyn WorkflowStore>,
}

impl std::fmt::Debug for WorkflowCatalog {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter.debug_struct("WorkflowCatalog").finish()
    }
}

/// Renders a store failure as this crate's error.
fn failed(action: &str, error: &impl std::fmt::Display) -> Error {
    Error::Workflow {
        action: action.to_string(),
        reason: error.to_string(),
    }
}

impl WorkflowCatalog {
    /// Opens the catalog under `workspace`, creating its directories.
    ///
    /// # Errors
    ///
    /// Returns an error when the directories cannot be created.
    pub fn open(workspace: impl AsRef<Path>) -> Result<Self> {
        let workspace = workspace.as_ref();
        let documents: PathBuf = workspace.join(WORKFLOW_DIR);
        let state = workspace.join(STATE_DIR);
        for directory in [&documents, &state] {
            std::fs::create_dir_all(directory).map_err(|error| Error::Workflow {
                action: format!("opening {}", directory.display()),
                reason: error.to_string(),
            })?;
        }
        Ok(Self {
            store: Arc::new(FileWorkflowStore::new(
                vec![documents],
                state.join("runs"),
            )),
        })
    }

    /// Saves `graph` as a new document under `id`.
    ///
    /// # Errors
    ///
    /// Returns an error when the graph fails validation or cannot be written.
    /// A graph that would not run is refused here rather than at the run, which
    /// is the whole point of validating at the edit.
    pub fn create(&self, id: &str, graph: &WorkflowGraph) -> Result<WorkflowRecord> {
        // Built by hand rather than with a derive: this crate has no direct
        // serde dependency, and the shape is one inserted key over the graph's
        // own serialization.
        let mut document = serde_json::to_value(graph)
            .map_err(|error| failed("serializing the workflow", &error))?;
        if let Some(map) = document.as_object_mut() {
            map.insert("id".into(), serde_json::Value::String(id.to_string()));
        }
        let document = document.to_string();
        create_workflow(&self.store, &document, id).map_err(|error| failed("creating", &error))
    }

    /// Reads a document back.
    ///
    /// # Errors
    ///
    /// Returns an error when `id` is not in the catalog.
    pub fn read(&self, id: &str) -> Result<WorkflowRecord> {
        self.store
            .get(id)
            .map_err(|error| failed("reading", &error))?
            .ok_or_else(|| Error::Workflow {
                action: "reading".into(),
                reason: format!("no workflow `{id}`"),
            })
    }

    /// The fingerprint of `id`'s graph, which an editor passes back to
    /// [`Self::apply_if_unchanged`].
    ///
    /// # Errors
    ///
    /// Returns an error when `id` is not in the catalog.
    pub fn fingerprint(&self, id: &str) -> Result<String> {
        Ok(fingerprint(&self.read(id)?.graph))
    }

    /// Applies `ops` and returns the result *without* saving.
    ///
    /// # Errors
    ///
    /// Returns an error when an op is malformed or the resulting graph fails
    /// validation. Both are the answer an editor wants before committing.
    pub fn preview(&self, id: &str, ops: &[GraphOp]) -> Result<WorkflowGraph> {
        preview_workflow_ops(&self.store, id, ops).map_err(|error| failed("previewing", &error))
    }

    /// Applies `ops` only if the document still matches `expected`.
    ///
    /// Returns `Ok(None)` when the document moved underneath the editor, which
    /// is a signal to re-read and retry rather than a failure — and is why this
    /// exists instead of a plain apply. Two agents editing one workflow is
    /// ordinary here, and last-write-wins would discard the loser's change
    /// without either of them learning that it happened.
    ///
    /// # Errors
    ///
    /// Returns an error when an op is malformed, the resulting graph fails
    /// validation, or the write fails.
    pub fn apply_if_unchanged(
        &self,
        id: &str,
        ops: &[GraphOp],
        expected: &str,
    ) -> Result<Option<WorkflowRecord>> {
        apply_workflow_ops_if_unchanged(&self.store, id, ops, expected)
            .map_err(|error| failed("applying", &error))
    }
}

#[cfg(test)]
#[path = "authoring_test.rs"]
mod test;
