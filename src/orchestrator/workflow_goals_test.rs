//! The goals child, on mocks.
#![allow(clippy::expect_used, clippy::panic)]

use serde_json::json;
use tinyflows::testkit::{Respond, TestHarness};
use tinyflows::validate::validate_all;

use super::*;

#[test]
fn the_child_is_structurally_valid() {
    let failures = validate_all(&goals_workflow());
    assert!(failures.is_empty(), "{failures:?}");
}

/// The cadence is the whole reason this is a document rather than an `if`: an
/// operator changing how often the goal is decomposed edits one expression.
#[test]
fn the_cadence_carries_the_interval_the_rust_uses() {
    let cadence = cadence();
    assert!(
        cadence.contains(&format!("< {REDUCTION_INTERVAL}")),
        "the interval is not the Rust constant: {cadence}"
    );
}

/// A run that has reached its answer has no use for a decomposition of the goal
/// it reached, whatever the counter says.
#[tokio::test]
async fn a_solved_run_holds_even_when_the_interval_is_up() {
    let run = TestHarness::new(&goals_workflow())
        .input(STATE_INPUT, json!({ "solved": true, "since_reduction": 99 }))
        .mock_tool(super::super::loop_steps::TOOL, Respond::value(json!({})))
        .run()
        .await
        .expect("the child runs to completion");

    run.assert_node_ran("held");
    run.assert_node_skipped(GATE_NODE);
    assert!(!opened(run.output()), "{}", run.output());
}

#[tokio::test]
async fn a_run_inside_the_interval_holds() {
    let run = TestHarness::new(&goals_workflow())
        .input(
            STATE_INPUT,
            json!({ "solved": false, "since_reduction": REDUCTION_INTERVAL - 1 }),
        )
        .mock_tool(super::super::loop_steps::TOOL, Respond::value(json!({})))
        .run()
        .await
        .expect("the child runs to completion");

    run.assert_node_ran("held");
    run.assert_node_skipped(GATE_NODE);
}

/// Due, so the gate is asked. Whether it opens is the gate's business — the
/// fingerprint and the claim are facts about the workspace, not about the
/// state — so the mock answers both ways and the reading is what is checked.
#[tokio::test]
async fn a_due_run_asks_the_gate_and_reports_what_it_said() {
    for admitted in [true, false] {
        let run = TestHarness::new(&goals_workflow())
            .input(
                STATE_INPUT,
                json!({ "solved": false, "since_reduction": REDUCTION_INTERVAL }),
            )
            .mock_tool(
                super::super::loop_steps::TOOL,
                Respond::value(json!({ OPENED_FIELD: admitted })),
            )
            .run()
            .await
            .expect("the child runs to completion");

        run.assert_node_ran(GATE_NODE);
        run.assert_node_skipped("held");
        assert_eq!(opened(run.output()), admitted, "{}", run.output());
    }
}

/// The reading has to survive not knowing which arm ran, because that is the
/// shape the parent sees: one run state, two possible terminal nodes.
#[test]
fn a_child_that_reported_nothing_reads_as_not_opened() {
    assert!(!opened(&json!(null)));
    assert!(!opened(&json!({})));
    assert!(!opened(&json!({ "nodes": {} })));
    assert!(!opened(
        &json!({ "nodes": { "held": { "items": [{ "json": { OPENED_FIELD: false } }] } } })
    ));
}
