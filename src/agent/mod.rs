//! Slim `OpenHuman` agent runtime.
//!
//! This facade vendors `OpenHuman`'s provider-neutral `tinyagents` engine while
//! deliberately leaving out the application domains that are not needed here:
//! persistent memory, external channels, and Web3 integrations.

pub use tinyagents::harness::message::Message;
pub use tinyagents::harness::model::ModelResponse;
pub use tinyagents::harness::providers::MockModel;
pub use tinyagents::harness::runtime::AgentHarness;
pub use tinyagents::harness::tool::{Tool, ToolCall, ToolResult, ToolSchema};
pub use tinyagents::{Result, TinyAgentsError};

/// The default slim harness state, which has no application-owned memory or
/// channel context.
pub type SlimAgent = AgentHarness<()>;

/// Creates an offline harness suitable for deterministic development and tests.
#[must_use]
pub fn mock(text: impl Into<String>) -> SlimAgent {
    let mut harness = SlimAgent::new();
    harness
        .register_model("mock", std::sync::Arc::new(MockModel::constant(text)))
        .set_default_model("mock");
    harness
}

#[cfg(test)]
mod test;
