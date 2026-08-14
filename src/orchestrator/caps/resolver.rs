//! Resolving a `sub_workflow` node's child graph by id.
//!
//! A `sub_workflow` node either embeds its child graph inline or names a
//! `workflow_id` for the host to look up. This crate has no saved-workflow
//! catalog yet, so the lookup half refuses and says so; an inline child is
//! unaffected, because the engine never calls a resolver for one.
//!
//! This is the one refusal in this module that *is* a gap rather than a
//! decision. When the workflow store lands, this becomes a lookup over it.

use async_trait::async_trait;
use tinyflows::caps::WorkflowResolver;
use tinyflows::error::{EngineError, Result as EngineResult};
use tinyflows::model::WorkflowGraph;

/// A resolver with no catalog behind it.
#[derive(Clone, Copy, Debug, Default)]
pub(crate) struct NoCatalog;

#[async_trait]
impl WorkflowResolver for NoCatalog {
    /// Always fails, naming the workflow that could not be found.
    ///
    /// # Errors
    ///
    /// Always returns a capability error. A `sub_workflow` node that embeds its
    /// child inline never reaches this.
    async fn resolve(&self, workflow_id: &str) -> EngineResult<WorkflowGraph> {
        Err(EngineError::Capability(format!(
            "no workflow catalog here, so `{workflow_id}` cannot be resolved; embed the child \
             graph inline instead"
        )))
    }
}

#[cfg(test)]
#[path = "resolver_test.rs"]
mod test;
