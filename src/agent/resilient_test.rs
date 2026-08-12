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
    // Must stay under the vendored 600s default, or it changes nothing.
    assert!(millis < 600_000);
    // ...and well above the slowest legitimate call. A tight bound turns a
    // slow-but-working request into a guaranteed failure once the retry
    // ladder exhausts, which is worse than the hang it bounds.
    assert!(
        millis >= 300_000,
        "timeout {millis}ms is tight enough to truncate working calls"
    );
}

#[test]
fn a_turn_granted_a_bigger_output_budget_is_given_time_to_produce_it() {
    use tinyagents::harness::model::ModelRequest;
    use tinyagents::harness::providers::MockModel;

    // Upstream recovers a truncated turn by re-issuing it with `max_tokens`
    // doubled, clamped at four times. Generation time is linear in output
    // length, so a flat ceiling made that recovery unable to succeed: a live
    // turn produced 12,000 tokens in 281 seconds, and its 24,000-token retry
    // needed nine minutes against a seven-minute bound. Every recovery timed
    // out, spending a full timeout to accomplish nothing.
    let model = BoundedTimeoutModel::<()>::new(Arc::new(MockModel::constant("hi")));
    let ordinary = model
        .bound(ModelRequest::new(vec![]).with_max_tokens(12_000))
        .timeout_ms
        .expect("a timeout is applied when unset");
    let doubled = model
        .bound(ModelRequest::new(vec![]).with_max_tokens(24_000))
        .timeout_ms
        .expect("a timeout is applied when unset");
    let clamped = model
        .bound(ModelRequest::new(vec![]).with_max_tokens(48_000))
        .timeout_ms
        .expect("a timeout is applied when unset");

    // The bound scales with the output budget, so a doubled turn gets more
    // wall clock than an ordinary one.
    assert!(doubled > ordinary, "{doubled}ms must exceed {ordinary}ms");
    // An ordinary full-cap turn is no longer held to the flat floor: at the
    // observed tail rate it cannot produce 12,000 tokens inside seven
    // minutes, so the floor was cutting off exactly the turns worth keeping.
    assert!(
        ordinary > 12_000 * 1_000 / 13,
        "a full-cap turn needs longer than {ordinary}ms to be producible"
    );
    assert!(ordinary >= 420_000, "the flat bound is still a floor");

    // And it stops scaling before it outlives the run. This is the half of
    // the rule that was missing: `RunBudget` now caps a run at thirty minutes
    // and its turn output at 48,000 tokens, and 48,000 at the pessimistic rate
    // is sixty-seven minutes — so the request bound quietly became longer than
    // the run containing it, and a wedged call could no longer fail in time
    // for the retry ladder to do anything about it. A live sat_solver held one
    // outstanding call for over ten minutes with nothing that would ever cut
    // it off.
    assert!(
        clamped <= 1_200_000,
        "a request bound of {clamped}ms leaves the run no time to retry it"
    );
    assert_eq!(clamped, doubled, "both are held at the same ceiling");
}

#[test]
fn a_request_that_names_no_output_budget_keeps_the_flat_bound() {
    use tinyagents::harness::model::ModelRequest;
    use tinyagents::harness::providers::MockModel;

    let model = BoundedTimeoutModel::<()>::new(Arc::new(MockModel::constant("hi")));
    let bounded = model.bound(ModelRequest::new(vec![]));
    assert_eq!(bounded.timeout_ms, Some(420_000));
}

#[test]
fn an_explicit_request_timeout_is_left_alone() {
    use tinyagents::harness::model::ModelRequest;
    use tinyagents::harness::providers::MockModel;

    let model = BoundedTimeoutModel::<()>::new(Arc::new(MockModel::constant("hi")));
    let bounded = model.bound(ModelRequest::new(vec![]).with_timeout_ms(1_234));
    assert_eq!(bounded.timeout_ms, Some(1_234));
}
