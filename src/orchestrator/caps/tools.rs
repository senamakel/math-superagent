//! This crate's tools, offered to `TinyFlows` as a `tool_call` invoker.
//!
//! A `tool_call` node names a slug and passes arguments; a
//! [`Tool`](crate::agent::Tool) takes a [`ToolCall`](crate::agent::ToolCall)
//! and returns a [`ToolResult`](crate::agent::ToolResult). The two are the same
//! call with different spellings, so this is a lookup and a translation.
//!
//! # The allow-list is the authority boundary
//!
//! Tools are authority boundaries in this crate — the orchestrator has no
//! shell, research has no delegation — and an invoker holding *every* tool
//! would quietly dissolve that: any workflow node could reach any tool by
//! naming it. So an invoker is built from an explicit set, and a slug outside
//! that set is refused by name rather than searched for. Build one per role, or
//! one per workflow, with exactly the tools that role or workflow may use.

use std::collections::BTreeMap;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};
use tinyflows::caps::ToolInvoker;
use tinyflows::error::{EngineError, Result as EngineResult};

use crate::agent::{Tool, ToolCall};

/// A fixed set of this crate's tools, callable by slug.
#[derive(Clone)]
pub(crate) struct WorkspaceTools {
    tools: Arc<BTreeMap<String, Arc<dyn Tool<()>>>>,
}

impl std::fmt::Debug for WorkspaceTools {
    /// Lists the slugs rather than the tools, because what a reader wants from
    /// this type is which authority it carries.
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("WorkspaceTools")
            .field("slugs", &self.tools.keys().collect::<Vec<_>>())
            .finish()
    }
}

impl WorkspaceTools {
    /// Builds an invoker over exactly `tools`.
    ///
    /// A duplicate name is last-wins rather than an error, matching how the
    /// harness's own registry behaves when a role is assembled twice.
    pub(crate) fn new(tools: impl IntoIterator<Item = Arc<dyn Tool<()>>>) -> Self {
        Self {
            tools: Arc::new(
                tools
                    .into_iter()
                    .map(|tool| (tool.name().to_string(), tool))
                    .collect(),
            ),
        }
    }

    /// The slugs this invoker will answer to, sorted.
    ///
    /// Exposed so a test can assert the authority a role was granted, rather
    /// than asserting the configuration that was meant to produce it.
    pub(crate) fn slugs(&self) -> Vec<&str> {
        self.tools.keys().map(String::as_str).collect()
    }
}

#[async_trait]
impl ToolInvoker for WorkspaceTools {
    /// Runs `slug` with `args`.
    ///
    /// The result is returned as `{ text, raw }` rather than as bare text, so a
    /// workflow can bind either `=item.text` for the model-facing string or
    /// `=item.raw.<field>` for the structured value a tool chose to publish.
    /// Flattening to text would throw the second one away, and several of this
    /// crate's tools exist precisely to return structure.
    ///
    /// A tool that reports failure through
    /// [`ToolResult::error`](crate::agent::ToolResult) becomes an engine error
    /// rather than a successful result carrying an error string: a `tool_call`
    /// node's `on_error` policy is what should decide what happens next, and it
    /// never sees a failure that arrived as a success.
    ///
    /// # Errors
    ///
    /// Returns a capability error when `slug` is not in this invoker's set, or
    /// when the tool itself fails.
    async fn invoke(&self, slug: &str, args: Value, _conn: Option<&str>) -> EngineResult<Value> {
        let tool = self.tools.get(slug).ok_or_else(|| {
            EngineError::Capability(format!(
                "no tool `{slug}` here; this invoker holds {:?}",
                self.slugs()
            ))
        })?;
        let call = ToolCall {
            // The engine has no call ids, and nothing downstream correlates on
            // one — the node's own slot is the correlation. A stable literal
            // keeps a trace readable rather than filling it with noise.
            id: format!("workflow:{slug}"),
            name: slug.to_string(),
            arguments: args,
            // A workflow's arguments are resolved config, not model output, so
            // they cannot be the unparseable JSON this field exists to carry.
            invalid: None,
        };
        let result = tool
            .call(&(), call)
            .await
            .map_err(|error| EngineError::Capability(error.to_string()))?;
        if let Some(error) = result.error {
            return Err(EngineError::Capability(format!("`{slug}` failed: {error}")));
        }
        Ok(json!({ "text": result.content, "raw": result.raw }))
    }
}

#[cfg(test)]
#[path = "tools_test.rs"]
mod test;
