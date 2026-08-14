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

/// A reset and an increment on the same counter compose.
///
/// The fold's whole reason for summing deltas rather than picking a winner. The
/// reflection zeroes `unproductive` on a productive attempt and the judge adds
/// one for a restart, concurrently, from the same base — so "last arm wins"
/// gives 0 or 4 depending on which finished last, and neither is the answer.
#[test]
fn a_reset_and_an_increment_on_one_counter_compose() {
    use super::super::solutions::{SolutionState, fold_evaluation};

    let base = {
        let mut state = SolutionState::new("a problem");
        state.unproductive = 3;
        state.to_accumulator()
    };
    let reflected = {
        let mut state = SolutionState::from_accumulator("a problem", &base);
        state.unproductive = 0;
        state.to_accumulator()
    };
    let judged = {
        let mut state = SolutionState::from_accumulator("a problem", &base);
        state.unproductive = 4;
        state.restarts = 1;
        state.to_accumulator()
    };

    for arms in [
        vec![reflected.clone(), judged.clone()],
        vec![judged.clone(), reflected.clone()],
    ] {
        let merged = fold_evaluation(&base, &arms);
        assert_eq!(
            merged.get("unproductive"),
            Some(&json!(1)),
            "3, reset to 0, plus the restart's 1: {merged}"
        );
        assert_eq!(merged.get("restarts"), Some(&json!(1)), "{merged}");
    }
}

/// A counter cannot be folded below zero.
///
/// Two arms each resetting the same counter give two negative deltas, and a
/// count is a `usize` on the other side of the boundary — an unclamped sum would
/// deserialize as either a very large number or a zero, and the first would
/// trip every threshold in the ladder at once.
#[test]
fn a_counter_folded_below_zero_is_clamped() {
    use super::super::solutions::{SolutionState, fold_evaluation};

    let base = {
        let mut state = SolutionState::new("a problem");
        state.unproductive = 2;
        state.to_accumulator()
    };
    let reset = {
        let mut state = SolutionState::from_accumulator("a problem", &base);
        state.unproductive = 0;
        state.to_accumulator()
    };
    let merged = fold_evaluation(&base, &[reset.clone(), reset]);
    assert_eq!(merged.get("unproductive"), Some(&json!(0)), "{merged}");
}

/// Everything each arm appended survives, and nothing is duplicated.
#[test]
fn every_arms_lesson_survives_the_fold() {
    use super::super::solutions::{SolutionState, fold_evaluation};

    let base = {
        let mut state = SolutionState::new("a problem");
        state.lessons.push("what an earlier attempt taught".into());
        state.to_accumulator()
    };
    let with = |lesson: &str| {
        let mut state = SolutionState::from_accumulator("a problem", &base);
        state.lessons.push(lesson.into());
        state.to_accumulator()
    };

    let merged = fold_evaluation(&base, &[with("the reflection's lesson")]);
    let lessons = merged
        .get("lessons")
        .and_then(Value::as_array)
        .cloned()
        .unwrap_or_default();
    assert_eq!(lessons.len(), 2, "{merged}");
    assert_eq!(lessons[0], json!("what an earlier attempt taught"));
    assert_eq!(lessons[1], json!("the reflection's lesson"));
}

/// The tag every arm stamps itself with never becomes part of the state.
///
/// It exists so the fold can order the arms before reading them. A tag that
/// survived the merge would be routed on, checkpointed, and eventually read by
/// something that thought it meant a step.
#[test]
fn the_arm_tag_does_not_survive_the_merge() {
    use super::super::solutions::{ARM_FIELD, SolutionState, fold_evaluation};

    let base = SolutionState::new("a problem").to_accumulator();
    let mut arm = base.clone();
    if let Some(object) = arm.as_object_mut() {
        object.insert(ARM_FIELD.to_string(), json!("judge"));
    }
    let merged = fold_evaluation(&base, &[arm]);
    assert!(merged.get(ARM_FIELD).is_none(), "{merged}");
}
