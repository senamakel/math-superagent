//! Unit tests for the tool and model resilience wrappers.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::json;

use super::{BoundedTimeoutModel, ResilientTool};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

#[derive(Debug)]
struct AlwaysFails;

#[async_trait]
impl Tool<()> for AlwaysFails {
    fn name(&self) -> &'static str {
        "always_fails"
    }

    fn description(&self) -> &'static str {
        "Fails every call."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(self.name(), self.description(), json!({ "type": "object" }))
    }

    async fn call(&self, _state: &(), _call: ToolCall) -> Result<ToolResult> {
        Err(tinyagents::TinyAgentsError::Validation(
            "downloaded document is not UTF-8".into(),
        ))
    }
}

#[derive(Debug)]
struct AlwaysSucceeds;

#[async_trait]
impl Tool<()> for AlwaysSucceeds {
    fn name(&self) -> &'static str {
        "always_succeeds"
    }

    fn description(&self) -> &'static str {
        "Succeeds every call."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(self.name(), self.description(), json!({ "type": "object" }))
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        Ok(ToolResult::text(call.id, self.name(), "fine"))
    }
}

fn call(id: &str) -> ToolCall {
    ToolCall {
        id: id.to_string(),
        name: "any".to_string(),
        arguments: json!({}),
        invalid: None,
    }
}

#[tokio::test]
async fn a_failing_tool_answers_the_model_instead_of_ending_the_run() -> Result<()> {
    let tool = ResilientTool::new(Arc::new(AlwaysFails));
    let result = tool.call(&(), call("call-1")).await?;

    assert!(result.is_error());
    assert_eq!(result.call_id, "call-1");
    assert!(result.content.contains("not UTF-8"));
    // The model must be told the call had no effect, or it cannot reason about
    // whether to retry or change approach.
    assert!(result.content.contains("did not run"));
    Ok(())
}

#[tokio::test]
async fn a_successful_tool_is_passed_through_unchanged() -> Result<()> {
    let tool = ResilientTool::new(Arc::new(AlwaysSucceeds));
    let result = tool.call(&(), call("call-2")).await?;

    assert!(!result.is_error());
    assert_eq!(result.content, "fine");
    Ok(())
}

#[test]
fn wrapping_preserves_the_tool_identity_the_model_sees() {
    let tool = ResilientTool::new(Arc::new(AlwaysFails));
    assert_eq!(tool.name(), "always_fails");
    assert_eq!(tool.description(), "Fails every call.");
    assert_eq!(tool.schema().name, "always_fails");
}

#[test]
fn requests_without_a_timeout_get_a_bounded_one() {
    use tinyagents::harness::model::ModelRequest;
    use tinyagents::harness::providers::MockModel;

    let model = BoundedTimeoutModel::<()>::new(Arc::new(MockModel::constant("hi")));
    let bounded = model.bound(ModelRequest::new(vec![]));
    let millis = bounded.timeout_ms.expect("a timeout is applied when unset");
    assert!(millis > 0);
    // Must stay under the vendored 600s default, or it changes nothing.
    assert!(millis < 600_000);
}

#[test]
fn an_explicit_request_timeout_is_left_alone() {
    use tinyagents::harness::model::ModelRequest;
    use tinyagents::harness::providers::MockModel;

    let model = BoundedTimeoutModel::<()>::new(Arc::new(MockModel::constant("hi")));
    let bounded = model.bound(ModelRequest::new(vec![]).with_timeout_ms(1_234));
    assert_eq!(bounded.timeout_ms, Some(1_234));
}
