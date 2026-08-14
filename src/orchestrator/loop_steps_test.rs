//! Tests for the step boundary the workflow graph calls through.
#![allow(clippy::expect_used)]

use super::*;

/// A workflow naming a step that does not exist must fail rather than run,
/// change nothing, and let the loop route on a state nobody advanced.
#[test]
fn only_the_declared_steps_are_runnable() {
    for step in STEPS {
        assert!(known_step(step), "`{step}` is declared but not runnable");
    }
    for step in ["", "attemp", "reflection", "diversify", "run_loop_step"] {
        assert!(!known_step(step), "`{step}` should not be runnable");
    }
}

/// The graph names every step it calls, and this tool runs every step the graph
/// names. A mismatch either way is a node that fails at run time.
#[test]
fn the_graph_and_the_tool_agree_on_the_step_names() {
    let graph = crate::orchestrator::workflow::solution_loop("a problem", Vec::new());
    for node in &graph.nodes {
        let Some(step) = node
            .config
            .get("args")
            .and_then(|args| args.get("step"))
            .and_then(Value::as_str)
        else {
            continue;
        };
        assert!(
            known_step(step),
            "the graph calls step `{step}`, which the tool does not run"
        );
    }
}
