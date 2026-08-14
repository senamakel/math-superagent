//! The goals child, on mocks.
#![allow(clippy::expect_used, clippy::panic)]

use serde_json::json;
use tinyflows::testkit::{Respond, TestHarness};
use tinyflows::validate::validate_all;

use super::super::schools::Thresholds;
use super::*;

#[test]
fn the_child_is_structurally_valid() {
    let failures = validate_all(&goals_workflow(&Thresholds::chisel()));
    assert!(failures.is_empty(), "{failures:?}");
}

/// The cadence is the whole reason this is a document rather than an `if`: an
/// operator changing how often the goal is decomposed edits one expression.
#[test]
fn the_cadence_carries_the_interval_the_rust_uses() {
    let cadence = cadence(&Thresholds::chisel());
    assert!(
        cadence.contains(&format!("< {}", Thresholds::chisel().reduction_interval)),
        "the interval is not the Rust constant: {cadence}"
    );
}

/// The cadence follows the school rather than the control.
///
/// The failure this guards against is silent: a school that decomposes on a
/// different interval would be handed a child built on the control's, and
/// nothing about the run would look wrong. Written against a threshold value
/// that no school currently holds, so it keeps testing the wiring rather than
/// whichever numbers the schools happen to have today.
#[test]
fn the_cadence_follows_the_school() {
    let patient = Thresholds {
        reduction_interval: Thresholds::chisel().reduction_interval + 4,
        ..Thresholds::chisel()
    };
    let cadence = cadence(&patient);
    assert!(
        cadence.contains(&format!("< {}", patient.reduction_interval)),
        "the child was built on the control's interval: {cadence}"
    );
    assert!(
        goals_workflow(&patient)
            .nodes
            .iter()
            .any(|node| serde_json::to_string(&node.config)
                .is_ok_and(|config| config.contains(&format!("< {}", patient.reduction_interval)))),
        "the school's interval never reached the graph the engine runs"
    );
}

/// A run that has reached its answer has no use for a decomposition of the goal
/// it reached, whatever the counter says.
#[tokio::test]
async fn a_solved_run_holds_even_when_the_interval_is_up() {
    let run = TestHarness::new(&goals_workflow(&Thresholds::chisel()))
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
    let run = TestHarness::new(&goals_workflow(&Thresholds::chisel()))
        .input(
            STATE_INPUT,
            json!({ "solved": false, "since_reduction": Thresholds::chisel().reduction_interval - 1 }),
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
        let run = TestHarness::new(&goals_workflow(&Thresholds::chisel()))
            .input(
                STATE_INPUT,
                json!({ "solved": false, "since_reduction": Thresholds::chisel().reduction_interval }),
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
