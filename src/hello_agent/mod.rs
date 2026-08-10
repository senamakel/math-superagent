//! Hello-world agent with basic tools and sub-agent delegation.

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::json;
use tinyagents::harness::subagent::{SubAgent, SubAgentTool};

use crate::agent::{
    AgentHarness, Message, ObservedAgent, Result, Tool, ToolCall, ToolResult, ToolSchema,
    openrouter_model_from_env,
};

const SYSTEM_PROMPT: &str = "You are a friendly hello-world agent. Use tools when they help. \
    Use add_numbers for arithmetic instead of calculating mentally. Delegate a focused piece of \
    work to spawn_subagent when the user asks for research, checking, or a second opinion. Keep \
    the final answer concise and mention useful tool results naturally.";

const SUBAGENT_PROMPT: &str = "You are a concise helper sub-agent. Complete only the delegated \
    task, report the useful result clearly, and do not invent tool output.";

/// A small OpenRouter-backed agent with deterministic tools and delegation.
#[derive(Debug)]
pub struct HelloAgent {
    inner: ObservedAgent,
}

impl HelloAgent {
    /// Loads the local provider and Langfuse configuration and constructs the
    /// parent and child agent loops.
    ///
    /// # Errors
    ///
    /// Returns an error when the required OpenRouter or Langfuse environment
    /// variables are missing or invalid.
    pub fn from_env() -> Result<Self> {
        let model = openrouter_model_from_env()?;

        let mut child_harness: AgentHarness<()> = AgentHarness::new();
        child_harness
            .register_model("openrouter", model.clone())
            .set_default_model("openrouter");
        let child = SubAgent::new(
            "spawn_subagent",
            "Delegates a focused task to a separate helper agent.",
            Arc::new(child_harness),
        )
        .with_system_prompt(SUBAGENT_PROMPT);

        let mut parent_harness: AgentHarness<()> = AgentHarness::new();
        parent_harness
            .register_model("openrouter", model)
            .set_default_model("openrouter")
            .register_tool(Arc::new(EchoTool))
            .register_tool(Arc::new(AddTool))
            .register_tool(Arc::new(SubAgentTool::new(Arc::new(child))));

        Ok(Self {
            inner: ObservedAgent::from_harness(parent_harness)?,
        })
    }

    /// Runs one task through the hello-world agent.
    ///
    /// The run and any delegated child work are exported to Langfuse under
    /// `run_id`.
    ///
    /// # Errors
    ///
    /// Returns any provider, tool, policy, or agent-loop error.
    pub async fn run(&self, run_id: impl Into<String>, task: impl Into<String>) -> Result<String> {
        let run = self
            .inner
            .invoke(
                run_id,
                vec![Message::system(SYSTEM_PROMPT), Message::user(task)],
            )
            .await?;
        Ok(run.text().unwrap_or_default())
    }
}

#[derive(Debug)]
struct EchoTool;

#[async_trait]
impl Tool<()> for EchoTool {
    fn name(&self) -> &str {
        "echo_text"
    }

    fn description(&self) -> &str {
        "Echoes a short text value exactly, useful for checking tool calls."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": { "text": { "type": "string" } },
                "required": ["text"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let text = call
            .arguments
            .get("text")
            .and_then(serde_json::Value::as_str)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation("text is required".into()))?;
        Ok(ToolResult::text(call.id, self.name(), text))
    }
}

#[derive(Debug)]
struct AddTool;

#[async_trait]
impl Tool<()> for AddTool {
    fn name(&self) -> &str {
        "add_numbers"
    }

    fn description(&self) -> &str {
        "Adds two numbers and returns their sum."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "a": { "type": "number" },
                    "b": { "type": "number" }
                },
                "required": ["a", "b"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let a = number_argument(&call, "a")?;
        let b = number_argument(&call, "b")?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            (a + b).to_string(),
        ))
    }
}

fn number_argument(call: &ToolCall, name: &str) -> Result<f64> {
    call.arguments
        .get(name)
        .and_then(serde_json::Value::as_f64)
        .ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("{name} must be a number"))
        })
}

#[cfg(test)]
mod test;
