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
///
/// The goals child is walked too, and has to be: its nodes live inside a config
/// value rather than in `nodes`, so a step name that only appears there would
/// otherwise be checked by nothing.
#[test]
fn the_graph_and_the_tool_agree_on_the_step_names() {
    let graph = crate::orchestrator::workflow::solution_loop("a problem", Vec::new());
    let goals = crate::orchestrator::workflow_goals::goals_workflow();
    for node in graph.nodes.iter().chain(goals.nodes.iter()) {
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

/// The fold the whole fan-out rests on.
///
/// Three arms run concurrently and each returns a *whole* state carrying its own
/// slot and four empty ones. Folding them naively lets whichever arm the engine
/// finished last blank out the other two; this asserts the order-independence
/// that makes running them concurrently safe, by folding the same three arms in
/// every order and requiring the same answer.
#[test]
fn every_arms_findings_survive_the_fold_in_any_order() {
    use super::super::solutions::{Finding, Slot, SolutionState};

    let arm = |slot: Slot, text: &str| {
        let mut state = SolutionState::new("a problem");
        state.diversify_mut().set(Finding::new(slot, text));
        state.to_accumulator()
    };
    let arms = [
        arm(Slot::Library, "what the librarian gathered"),
        arm(Slot::Patterns, "what the numbers show"),
        arm(Slot::Chosen, "the line of attack"),
    ];

    let orders = [[0, 1, 2], [2, 1, 0], [1, 2, 0]];
    let mut folded = Vec::new();
    for order in orders {
        let ordered: Vec<Value> = order.iter().map(|index| arms[*index].clone()).collect();
        let base = SolutionState::new("a problem").to_accumulator();
        let merged = super::super::solutions::fold_evaluation(&base, &ordered);
        let state = SolutionState::from_accumulator("a problem", &merged);
        let sections: Vec<String> = SolutionState::diversify(&state)
            .sections()
            .iter()
            .map(|(_, text)| (*text).to_string())
            .collect();
        folded.push(sections);
    }

    for sections in &folded {
        assert!(
            sections.contains(&"what the librarian gathered".to_string())
                && sections.contains(&"what the numbers show".to_string())
                && sections.contains(&"the line of attack".to_string()),
            "an arm's findings were lost: {sections:?}"
        );
    }
    assert!(
        folded.windows(2).all(|pair| pair[0] == pair[1]),
        "the fold depends on the order the arms finished in: {folded:?}"
    );
}

/// The cadence counter is the loop's, and only a child that actually opened a
/// decomposition resets it. A cycle that came due and was declined by the gate
/// leaves it alone, so the next cycle asks again rather than waiting another
/// full interval for evidence that may have arrived meanwhile.
#[test]
fn only_an_opened_decomposition_resets_the_cadence() {
    use super::super::solutions::SolutionState;
    use super::super::workflow_goals::OPENED_FIELD;

    let child = |opened: bool| {
        json!({ "nodes": { "gate": { "items": [{ "json": { OPENED_FIELD: opened } }] } } })
    };
    let due = || {
        let mut state = SolutionState::new("a problem");
        state.since_reduction = 7;
        state
    };

    let opened = apply_goal_decision(due(), &json!({ DECISION_ARG: child(true) }));
    assert_eq!(opened.to_accumulator()["since_reduction"], json!(0));

    for declined in [child(false), Value::Null, json!({})] {
        let held = apply_goal_decision(due(), &json!({ DECISION_ARG: declined.clone() }));
        assert_eq!(
            held.to_accumulator()["since_reduction"],
            json!(7),
            "a declined cycle moved the counter: {declined}"
        );
    }
}
