//! This crate's model, offered to `TinyFlows` as a completion provider.
//!
//! An `agent` node whose config names a registered `agent_ref` runs through
//! [`AgentRunner`](tinyflows::caps::AgentRunner) — that is the path this crate
//! cares about, and it is where the roles, their tools, and their budgets live.
//! [`LlmProvider`] is the *other* path: a bare completion, used by an `agent`
//! node with no `agent_ref` and by an `output_parser` node repairing malformed
//! structured output.
//!
//! Both of those are single turns with no tools, which is what this provides:
//! one call, no loop, no tool registry. Anything that needs a tool needs a
//! role, and a role is an `agent_ref`.
//!
//! # The request shape
//!
//! The engine passes the node's resolved config verbatim, so what arrives is
//! whatever the workflow author wrote. Two spellings are read — `prompt` for a
//! single instruction, or `messages` for a conversation — and a config carrying
//! neither is refused rather than sent as an empty turn, because an empty turn
//! costs a provider call to produce nothing.

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};
use tinyagents::harness::model::{ChatModel, ModelRequest};
use tinyflows::caps::LlmProvider;
use tinyflows::error::{EngineError, Result as EngineResult};

use crate::agent::Message;

/// One model turn, for the nodes that need a completion rather than a role.
#[derive(Clone)]
pub(crate) struct SingleTurnModel {
    model: Arc<dyn ChatModel<()>>,
}

impl std::fmt::Debug for SingleTurnModel {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter.debug_struct("SingleTurnModel").finish()
    }
}

impl SingleTurnModel {
    /// Wraps a model as a completion provider.
    pub(crate) fn new(model: Arc<dyn ChatModel<()>>) -> Self {
        Self { model }
    }
}

/// Reads the messages out of a node's resolved config.
///
/// `messages` wins over `prompt` when both are present, because a caller that
/// built a conversation meant it; silently sending the single prompt instead
/// would drop the history without saying so.
fn messages_from(request: &Value) -> EngineResult<Vec<Message>> {
    if let Some(messages) = request.get("messages").and_then(Value::as_array) {
        let built: Vec<Message> = messages
            .iter()
            .filter_map(|message| {
                let content = message.get("content").and_then(Value::as_str)?;
                Some(match message.get("role").and_then(Value::as_str) {
                    Some("system") => Message::system(content),
                    _ => Message::user(content),
                })
            })
            .collect();
        if !built.is_empty() {
            return Ok(built);
        }
    }
    let prompt = request
        .get("prompt")
        .and_then(Value::as_str)
        .filter(|prompt| !prompt.trim().is_empty())
        .ok_or_else(|| {
            EngineError::Capability(
                "a completion needs a non-empty `prompt`, or a `messages` array".into(),
            )
        })?;
    Ok(vec![Message::user(prompt)])
}

#[async_trait]
impl LlmProvider for SingleTurnModel {
    /// Runs one turn.
    ///
    /// Returns `{ text }`, which is the shape the `agent` node reads a
    /// completion out of, so a downstream node binds `=item.text` whether the
    /// turn came from here or from a registered role.
    ///
    /// # Errors
    ///
    /// Returns a capability error when the config carries no prompt or
    /// messages, or when the provider call fails.
    async fn complete(&self, request: Value, _conn: Option<&str>) -> EngineResult<Value> {
        let messages = messages_from(&request)?;
        let response = self
            .model
            .invoke(
                &(),
                ModelRequest {
                    messages,
                    ..ModelRequest::default()
                },
            )
            .await
            .map_err(|error| EngineError::Capability(error.to_string()))?;
        Ok(json!({ "text": Message::Assistant(response.message).text() }))
    }
}

#[cfg(test)]
#[path = "llm_test.rs"]
mod test;
