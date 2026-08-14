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

/// The measured failure this node exists for: a run that had its answer kept
/// paying three standing teams for another hour, because the only cancellation
/// was after the whole workflow — judge included — had returned.
///
/// A standing team never retires on its own (`Completion::Standing` maps
/// "nothing further to do" to `Idle`, not `Finished`), so nothing but this call
/// ends one.
#[tokio::test]
async fn the_end_of_the_run_stops_the_work_beside_it() {
    use std::sync::atomic::{AtomicU64, Ordering};

    let cycles = Arc::new(AtomicU64::new(0));
    let counted = cycles.clone();
    let team = crate::orchestrator::teams::spawn(
        "research",
        crate::orchestrator::teams::TeamBudget::acquiring(),
        None,
        None,
        move |_inbox| {
            let counted = counted.clone();
            async move {
                counted.fetch_add(1, Ordering::Relaxed);
                // Standing work: there is always one more source to fetch, so
                // the team never reports itself finished.
                crate::orchestrator::teams::Cycle::Worked
            }
        },
    );

    assert!(!team.is_cancelled(), "it starts running");
    stand_down(std::slice::from_ref(&team), None);
    assert!(
        team.is_cancelled(),
        "the run has ended, so the work beside it is asked to stop"
    );
}

/// Cancelling nothing is not an error. A run whose teams never started — every
/// unit test, and any run with the teams disabled — must still leave the loop
/// through this node.
#[test]
fn standing_down_with_no_teams_is_not_a_failure() {
    stand_down(&[], None);
}

/// The mechanism by which "first verified solve wins" reaches a school that is
/// still working.
///
/// Asserted on the decision rather than on a `LoopSteps`, which needs a live
/// subagent manager and a vector store — the clock and the flag are the whole
/// of what this is about, and `LoopSteps::expired` is one line delegating here.
#[test]
fn a_sibling_school_solving_stops_this_one() {
    use std::sync::atomic::{AtomicBool, Ordering};

    let started = std::time::Instant::now();
    let ceiling = std::time::Duration::from_hours(1);
    let solved = AtomicBool::new(false);
    assert!(
        !stop_requested(started, ceiling, Some(&solved)),
        "a school with time left and no sibling arrived keeps going"
    );
    solved.store(true, Ordering::Relaxed);
    assert!(
        stop_requested(started, ceiling, Some(&solved)),
        "a school whose sibling verified a solution stops, with the clock untouched"
    );
}

/// A run built without `in_school` is the run this loop has always been.
///
/// `None` rather than a flag that is merely never set, because the two differ
/// in the failure that matters: a shared flag left in place by a single-school
/// run is a stop condition nobody owns.
#[test]
fn a_run_with_no_school_stops_only_on_its_clock() {
    let started = std::time::Instant::now();
    assert!(
        !stop_requested(started, std::time::Duration::from_hours(1), None),
        "a fresh run has not spent its ceiling"
    );
    assert!(
        stop_requested(started, std::time::Duration::ZERO, None),
        "a run that has spent its ceiling still stops on the clock alone"
    );
}
