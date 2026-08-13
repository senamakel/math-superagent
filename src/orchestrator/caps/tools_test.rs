//! Deterministic tests for offering this crate's tools to `TinyFlows`.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use super::*;
use crate::agent::{Result, ToolResult, ToolSchema};

/// A tool that reports what it was handed, so a test can assert the translation
/// rather than the tool.
struct EchoTool {
    name: &'static str,
    fail: bool,
}

#[async_trait]
impl Tool<()> for EchoTool {
    fn name(&self) -> &str {
        self.name
    }

    fn description(&self) -> &'static str {
        "echoes its arguments"
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(self.name(), self.description(), json!({ "type": "object" }))
    }

    async fn call(&self, _state: &(), call: crate::agent::ToolCall) -> Result<ToolResult> {
        if self.fail {
            return Err(tinyagents::TinyAgentsError::Tool("refused".into()));
        }
        let mut result = ToolResult::text(call.id, self.name(), "did the thing");
        result.raw = Some(call.arguments);
        Ok(result)
    }
}

fn invoker() -> WorkspaceTools {
    WorkspaceTools::new([
        Arc::new(EchoTool {
            name: "read_file",
            fail: false,
        }) as Arc<dyn Tool<()>>,
        Arc::new(EchoTool {
            name: "broken",
            fail: true,
        }) as Arc<dyn Tool<()>>,
    ])
}

/// Both halves of a result survive: several of this crate's tools exist to
/// return structure, and flattening to text would discard it.
#[tokio::test]
async fn a_result_carries_both_its_text_and_its_structure() {
    let value = invoker()
        .invoke("read_file", json!({ "path": "GOAL.md" }), None)
        .await
        .expect("a held tool runs");

    assert_eq!(value["text"], json!("did the thing"));
    assert_eq!(value["raw"], json!({ "path": "GOAL.md" }));
}

/// The authority boundary. An invoker built without a tool must refuse it by
/// name rather than reaching for some wider registry.
#[tokio::test]
async fn a_tool_outside_the_set_is_refused_and_the_set_is_named() {
    let error = invoker()
        .invoke("execute_command", json!({}), None)
        .await
        .expect_err("a tool this invoker does not hold cannot be called");

    let rendered = error.to_string();
    assert!(rendered.contains("execute_command"), "{rendered}");
    // The message lists what *is* available, so a misnamed slug is one read
    // rather than a hunt through the registry.
    assert!(rendered.contains("read_file"), "{rendered}");
}

/// A failure must reach the node as a failure, or `on_error` never sees it.
#[tokio::test]
async fn a_failing_tool_becomes_an_error_rather_than_a_successful_result() {
    let error = invoker()
        .invoke("broken", json!({}), None)
        .await
        .expect_err("a tool that fails fails the call");
    assert!(error.to_string().contains("refused"), "{error}");
}

#[test]
fn the_granted_slugs_are_readable_for_an_assertion() {
    // Tests assert the authority a role ends up with, not the config meant to
    // produce it, so the resolved set has to be readable.
    assert_eq!(invoker().slugs(), ["broken", "read_file"]);
}
