//! The loop graph, driven on mocks.
#![allow(clippy::expect_used, clippy::panic)]

use serde_json::json;
use tinyflows::testkit::{Respond, TestHarness};
use tinyflows::validate::validate_all;

use super::*;
use crate::orchestrator::definitions::workflow_agents;
use crate::orchestrator::default_registry;

fn graph() -> WorkflowGraph {
    let registry = default_registry(true).expect("the default registry builds");
    solution_loop("find the largest x", workflow_agents(&registry))
}

/// One loop state, as `run_loop_step` returns it.
///
/// Every step now returns the whole state, so a test fixes the state once and
/// the routing is what the test is about. The steps' own behaviour is covered
/// where it lives — `solutions_test.rs` for the policy, `loop_steps_test.rs`
/// for the tool boundary.
fn verdict(fields: Value) -> Respond {
    Respond::value(fields)
}

/// A run where every step reports the same state, so the ladder decides.
async fn run_with(state: Value) -> tinyflows::testkit::TestRun {
    TestHarness::new(&graph())
        .mock_tool("run_loop_step", verdict(state))
        .run()
        .await
        .expect("the loop runs to completion on mocks")
}

#[test]
fn the_graph_is_structurally_valid() {
    let graph = graph();
    let failures = validate_all(&graph);
    assert!(failures.is_empty(), "{failures:?}");
}

/// The whole point of authoring this declaratively: a threshold appears in the
/// document, and it is the one the Rust uses rather than a second copy.
#[test]
fn the_ladder_carries_the_thresholds_the_rust_uses() {
    let ladder = reflect_ladder();
    assert!(
        ladder.contains(&format!(">= {MAX_ATTEMPTS}")),
        "the attempt ceiling is not the Rust constant: {ladder}"
    );
    assert!(
        ladder.contains(&format!(">= {UNVERIFIED_THRESHOLD}")),
        "the unverified threshold is not the Rust constant: {ladder}"
    );
    // Order is load-bearing: `blocked` outranks everything, and `reported`
    // outranks both stuck arms.
    let at = |needle: &str| ladder.find(needle).unwrap_or(usize::MAX);
    assert!(at("blocked") < at("solved"));
    assert!(at("reported") < at("diversify"));
}

/// The failure a green run hides. Every `=`-binding in the ladder addresses
/// `nodes.solve.state`, and a typo there resolves to `null` — which routes to
/// the `default` port and reports success. This caught two real bugs when it
/// was written: a doubled `=` prefix that made every fold expression a literal,
/// and a fold with no fallback that wiped the seed on the first pass.
///
/// The loop's own `state.update` bindings are excluded, and the exclusion is
/// narrow on purpose. The `loop` node injects `state` into the scope itself
/// before resolving those expressions, so the trace recorder — which resolves
/// against the generic `{ item, items, run, nodes }` scope — cannot see it and
/// records them as null. That they are *not* null is asserted directly below,
/// against the accumulator the run actually produced.
#[tokio::test]
async fn no_binding_in_the_loop_resolves_to_nothing() {
    let run = run_with(json!({
        "attempts": 1, "solved": true, "unproductive": 0, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "done", "fresh_context": ""
    }))
    .await;
    run.assert_completed();

    let unexplained: Vec<String> = run
        .trace()
        .null_bindings()
        .iter()
        .filter(|(node, binding)| {
            !(*node == LOOP_NODE && binding.location.starts_with("state.update"))
        })
        .map(|(node, binding)| format!("{node}.{} = {}", binding.location, binding.expression))
        .collect();
    assert!(unexplained.is_empty(), "{unexplained:#?}");
}

/// The accumulator is the thing the whole graph rests on, so it is asserted
/// against the run's own output rather than inferred from the routing. This is
/// also what makes the exclusion above safe: if the fold silently stopped
/// working, the excluded bindings would be genuinely null and this would fail.
#[tokio::test]
async fn the_accumulator_carries_the_reflection_forward() {
    // A whole state, because the fold replaces rather than merges: a step
    // returns everything it knows, and a fixture that returned only the
    // counters would be testing a step that had lost the problem statement.
    let run = run_with(json!({
        "problem": "find the largest x",
        "attempts": 3, "solved": true, "unproductive": 1, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "the lesson", "fresh_context": "gathered"
    }))
    .await;

    let state = run
        .output()
        .pointer(&format!("/nodes/{LOOP_NODE}/state"))
        .cloned()
        .unwrap_or(Value::Null);
    assert_eq!(state["attempts"], json!(3), "{state}");
    assert_eq!(state["solved"], json!(true), "{state}");
    assert_eq!(state["lesson"], json!("the lesson"), "{state}");
    assert_eq!(state["unproductive"], json!(1), "{state}");
    // The seed survives a fold that never mentions it.
    assert_eq!(state["problem"], json!("find the largest x"), "{state}");
}

#[tokio::test]
async fn a_solved_reflection_leaves_the_loop() {
    let run = run_with(json!({
        "attempts": 1, "solved": true, "unproductive": 0, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "done", "fresh_context": ""
    }))
    .await;
    run.assert_node_ran("report");
    // One pass. Four steps run in it — attempt, judge, reflect, and the merge
    // is not reached — so a second pass would show as more than four.
    run.assert_call_count(tinyflows::testkit::capability::TOOLS, Some("run_loop_step"), 3);
}

/// The arm that catches a run doing well by its own report and going nowhere.
#[tokio::test]
async fn a_stuck_run_fans_out_to_every_diversify_arm() {
    let run = run_with(json!({
        "attempts": 1, "solved": false, "unproductive": STUCK_THRESHOLD, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "no progress", "fresh_context": ""
    }))
    .await;
    for (arm, _) in ARMS {
        run.assert_node_ran(arm);
    }
    run.assert_node_ran("diversify_merge");
}

/// A provider failure is not evidence about the mathematics, so it outranks
/// every other arm — including the attempt ceiling.
#[tokio::test]
async fn a_blocked_run_stops_without_diversifying() {
    let run = run_with(json!({
        "attempts": 1, "solved": false, "unproductive": STUCK_THRESHOLD, "blocked": BLOCKED_THRESHOLD,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "provider refused", "fresh_context": ""
    }))
    .await;
    run.assert_node_ran("report");
    // Blocked outranks the stuck arms, so no arm may have run even though the
    // unproductive count alone would have sent it there.
    for (arm, _) in ARMS {
        run.assert_node_skipped(arm);
    }
}

/// An answer with one route behind it, said twice, is terminal — and it must
/// not be read as "stuck", because the unproductive count it accumulates would
/// otherwise spend three child runs on a problem whose answer is on disk.
#[tokio::test]
async fn a_twice_unverified_run_reports_rather_than_diversifying() {
    let run = run_with(json!({
        "attempts": 2, "solved": false, "unproductive": STUCK_THRESHOLD, "blocked": 0,
        "computational": 0, "unverified": UNVERIFIED_THRESHOLD, "restarts": 0,
        "lesson": "no second route", "fresh_context": ""
    }))
    .await;
    run.assert_node_ran("report");
    for (arm, _) in ARMS {
        run.assert_node_skipped(arm);
    }
}

/// Progress that is only ever a bigger instance of the same computation routes
/// to diversify too. This is the arm the counter was added for: every attempt
/// establishes something, none of them changes the method, so the unproductive
/// arm never fires.
#[tokio::test]
async fn a_run_that_only_scales_is_sent_to_diversify() {
    let run = run_with(json!({
        "attempts": 2, "solved": false, "unproductive": 0, "blocked": 0,
        "computational": COMPUTATIONAL_THRESHOLD, "unverified": 0, "restarts": 0,
        "lesson": "bigger n", "fresh_context": ""
    }))
    .await;
    run.assert_node_ran("diversify_merge");
}

/// The diagnosis catches what the assertions above do not think to look for.
#[tokio::test]
async fn a_completed_run_has_nothing_to_diagnose() {
    let run = run_with(json!({
        "attempts": 1, "solved": true, "unproductive": 0, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "done", "fresh_context": ""
    }))
    .await;
    run.assert_clean_diagnosis();
}


/// The end-to-end gate for the cutover: the loop, on the real engine, with the
/// real state serialization at every boundary.
///
/// Only the step *bodies* stand in — those need a live subagent manager and a
/// vector store. Everything between them is production code: `to_accumulator`
/// writes the state, the engine folds it, `from_accumulator` reads it back for
/// the ladder, and `outcome` turns the finished accumulator into the report a
/// caller sees.
#[tokio::test]
async fn the_loop_runs_end_to_end_on_the_real_state_serialization() {
    use crate::orchestrator::solutions::SolutionState;

    let mut solved = SolutionState::new("find the largest x");
    solved.attempts = 2;
    solved.solved = true;
    solved.last_attempt = "the proof, in full".into();
    solved.lessons = vec!["the bound is tight".into()];

    let run = TestHarness::new(&graph())
        // The real serialization, not a hand-written fixture: if a field stopped
        // round-tripping, this is where the loop would start reading nulls.
        .mock_tool("run_loop_step", Respond::value(solved.to_accumulator()))
        .run()
        .await
        .expect("the loop runs to completion");

    run.assert_completed();
    run.assert_node_ran("report");

    let finished = run
        .output()
        .pointer(&format!("/nodes/{LOOP_NODE}/state"))
        .cloned()
        .unwrap_or(Value::Null);
    let report = SolutionState::from_accumulator("", &finished).outcome();
    assert!(report.contains("Solved after 2 attempt(s)"), "{report}");
    assert!(report.contains("the proof, in full"), "{report}");
}

/// The two engines must *report* the same, not only route the same. The report
/// wording is written against specific ways a run can end, so rebuilding the
/// state from the accumulator and calling the same `outcome` is what makes the
/// switch invisible to whoever reads the result.
#[test]
fn a_finished_accumulator_reports_what_the_state_graph_would() {
    use crate::orchestrator::solutions::SolutionState;

    let endings = [
        json!({ "attempts": 2, "solved": true, "unverified": 0, "blocked": 0,
                "last_attempt": "the proof", "lesson": "" }),
        json!({ "attempts": 3, "solved": false, "unverified": UNVERIFIED_THRESHOLD, "blocked": 0,
                "last_attempt": "one route only", "lesson": "" }),
        json!({ "attempts": 1, "solved": false, "unverified": 0, "blocked": BLOCKED_THRESHOLD,
                "last_attempt": "[goals] failed: model error", "lesson": "" }),
        json!({ "attempts": MAX_ATTEMPTS, "solved": false, "unverified": 0, "blocked": 0,
                "last_attempt": "the furthest it got", "lesson": "try the other reduction" }),
    ];

    for ending in endings {
        // What the workflow path produces.
        let rebuilt = SolutionState::from_accumulator("a problem", &ending);

        // What the state graph would have produced from the same run.
        let count = |key: &str| {
            usize::try_from(ending[key].as_u64().unwrap_or(0)).unwrap_or(usize::MAX)
        };
        let mut direct = SolutionState::new("a problem");
        direct.attempts = count("attempts");
        direct.solved = ending["solved"].as_bool().unwrap_or(false);
        direct.unverified = count("unverified");
        direct.blocked = count("blocked");
        direct.last_attempt = ending["last_attempt"].as_str().unwrap_or("").to_string();
        let lesson = ending["lesson"].as_str().unwrap_or("");
        if !lesson.is_empty() {
            direct.lessons.push(lesson.to_string());
        }

        assert_eq!(rebuilt.outcome(), direct.outcome(), "{ending}");
    }
}

/// The whole state crosses the boundary and comes back, not only the counters.
/// A field dropped in the round trip is a field silently reset on every pass,
/// and the dangerous ones are the quiet ones — `steer` is the judge's direction
/// for the next attempt, `since_reduction` paces the decomposition arm.
#[test]
fn every_field_survives_the_accumulator_round_trip() {
    use crate::orchestrator::solutions::{SolutionState, Verdict};

    let mut original = SolutionState::new("find the largest x");
    original.attempts = 4;
    original.unproductive = 2;
    original.blocked = 1;
    original.computational = 3;
    original.unverified = 1;
    original.restarts = 2;
    original.since_reduction = 2;
    original.solved = true;
    original.last_attempt = "what the attempt said".into();
    original.fresh_context = "gathered material".into();
    original.steer = "try the other reduction".into();
    original.judged = Verdict::Restart;
    original.scores = vec![3, 4, 2];
    original.lessons = vec!["first".into(), "second".into()];

    let returned = SolutionState::from_accumulator("", &original.to_accumulator());

    assert_eq!(returned.to_accumulator(), original.to_accumulator());
    // Spot-checked individually too, so a round trip that lost a field on both
    // sides at once would still fail.
    assert_eq!(returned.steer, "try the other reduction");
    assert_eq!(returned.since_reduction, 2);
    assert_eq!(returned.judged, Verdict::Restart);
    assert_eq!(returned.scores, vec![3, 4, 2]);
    assert_eq!(returned.lessons.len(), 2);
    assert_eq!(returned.problem(), "find the largest x");
}


/// The gap that let an unreachable restart arm ship: the parity harness feeds
/// the ladders a scope it builds itself, so a ladder can be provably correct
/// and still read a field no step emits.
///
/// This checks the other half — that every `.item.json.<field>` and
/// `.state.<field>` the ladders read is one a real state actually carries.
#[test]
fn the_ladders_read_fields_a_step_actually_emits() {
    use crate::orchestrator::solutions::SolutionState;

    let emitted = SolutionState::new("a problem").to_accumulator();
    let mut missing = Vec::new();

    for ladder in [reflect_ladder(), judge_ladder(), terminal_condition()] {
        for prefix in [".item.json.", ".state.", &format!(".nodes.{LOOP_NODE}.state.")] {
            let mut rest = ladder.as_str();
            while let Some(at) = rest.find(prefix) {
                rest = &rest[at + prefix.len()..];
                let field: String = rest
                    .chars()
                    .take_while(|c| c.is_alphanumeric() || *c == '_')
                    .collect();
                if !field.is_empty() && emitted.get(&field).is_none() {
                    missing.push(field);
                }
            }
        }
    }

    missing.sort_unstable();
    missing.dedup();
    assert!(
        missing.is_empty(),
        "the ladders read fields no state carries: {missing:?}"
    );
}

/// The restart arm, end to end. A judge that wants the run to start over must
/// actually reach another attempt rather than being routed to a reflection.
#[tokio::test]
async fn a_restart_verdict_reaches_another_attempt() {
    use crate::orchestrator::solutions::{SolutionState, Verdict};

    let mut restarting = SolutionState::new("a problem");
    restarting.attempts = 1;
    restarting.judged = Verdict::Restart;

    let run = TestHarness::new(&graph())
        .mock_tool("run_loop_step", Respond::value(restarting.to_accumulator()))
        .run()
        .await
        .expect("the loop runs to completion");

    // A restart re-enters the attempt without reflecting, so the run keeps
    // attempting until the ceiling rather than settling after one pass.
    let attempts = run
        .trace()
        .steps
        .iter()
        .filter(|step| step.node_id == "attempt")
        .count();
    assert!(
        attempts > 1,
        "the restart arm never re-attempted; it is unreachable"
    );
}
