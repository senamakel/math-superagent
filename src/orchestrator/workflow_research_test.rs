//! The research child, driven on mocks.
#![allow(clippy::expect_used, clippy::panic)]

use serde_json::json;
use tinyflows::testkit::{Respond, TestHarness};
use tinyflows::validate::validate_all;

use super::*;

#[test]
fn the_child_is_structurally_valid() {
    let failures = validate_all(&research_workflow());
    assert!(failures.is_empty(), "{failures:?}");
}

/// Both nodes name a step the tool actually runs.
///
/// A graph is not compiled against these strings, so a step renamed on one side
/// fails the node at runtime — on the first live run, after the container is up
/// and the statement is fetched.
#[test]
fn both_nodes_name_a_step_the_tool_runs() {
    for node in research_workflow().nodes {
        let Some(step) = node.config.pointer("/args/step").and_then(Value::as_str) else {
            continue;
        };
        assert!(
            super::super::loop_steps::known_step(step),
            "`{}` runs `{step}`, which is not a step",
            node.id
        );
    }
}

/// The survey reads what the curator established, not the input.
///
/// The whole reason the two are in series. A survey seeded from the child's own
/// input would go to the literature with the problem statement as its only
/// query, which is the weakest query the run will ever have — and the failure is
/// silent, because a search on a poor query still returns papers.
#[tokio::test]
async fn the_survey_reads_what_the_curator_established() {
    let established = json!({ "problem": "a problem", "fresh_context": "what the curator found" });

    let run = TestHarness::new(&research_workflow())
        .input(STATE_INPUT, json!({ "problem": "a problem", "fresh_context": "" }))
        .mock_tool(
            super::super::loop_steps::TOOL,
            Respond::sequence([
                Respond::value(established.clone()),
                Respond::value(established.clone()),
            ]),
        )
        .run()
        .await
        .expect("the child runs to completion on mocks");

    let handed = run
        .trace()
        .calls_from(SURVEY_NODE)
        .first()
        .and_then(|call| call.args.pointer("/state/fresh_context"))
        .and_then(Value::as_str)
        .unwrap_or_default()
        .to_string();
    assert_eq!(
        handed, "what the curator found",
        "the survey was seeded with something other than the curator's finding"
    );
}

/// What the child established crosses back to the parent.
///
/// The parent seeds the loop's accumulator from this, so a reader that returned
/// nothing would leave the run starting from the statement and eleven zeroes,
/// having paid for stage one and used none of it — with nothing in the trace to
/// say so.
#[tokio::test]
async fn what_the_child_established_reaches_the_parent() {
    let found = json!({ "problem": "a problem", "fresh_context": "what stage one found" });

    let run = TestHarness::new(&research_workflow())
        .input(STATE_INPUT, json!({ "problem": "a problem" }))
        .mock_tool(super::super::loop_steps::TOOL, Respond::value(found.clone()))
        .run()
        .await
        .expect("the child runs to completion on mocks");

    let state = established(&run.output()).unwrap_or(Value::Null);
    assert_eq!(
        state.get("fresh_context"),
        Some(&json!("what stage one found")),
        "the parent cannot read what the child established: {state}"
    );
}

/// A child that produced nothing is readable as nothing rather than as a panic.
#[test]
fn an_empty_run_state_reads_as_nothing_established() {
    assert!(established(&json!({})).is_none());
    assert!(established(&json!({ "nodes": {} })).is_none());
}
