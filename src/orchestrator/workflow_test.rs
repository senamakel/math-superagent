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
        // The goals child's own expressions. The engine passes an inline
        // `workflow` graph through untouched — its `=` values belong to the
        // child's scope, not this one — but the recorder resolves every config
        // string it walks, so the child's `=.inputs.state` is recorded as null
        // against a scope that has no `inputs`. That they resolve where they are
        // actually evaluated is asserted in `workflow_goals_test.rs`, which runs
        // the child and reads what the gate was handed.
        .filter(|(_, binding)| !binding.location.starts_with("workflow."))
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
    // The seed call's gate, then one pass: attempt, judge, reflect, goal_apply.
    // The merge is not reached, and the in-loop goals child holds rather than
    // asking, so a second pass would show as more than five.
    run.assert_call_count(
        tinyflows::testkit::capability::TOOLS,
        Some(super::super::loop_steps::TOOL),
        5,
    );
    // The goals child ran and declined: this fixture carries no
    // `since_reduction`, so the cadence reads zero and holds.
    run.assert_node_ran(GOALS_NODE);
}

/// The escalation, which is now one node rather than three.
///
/// Two of the three arms it used to fan out to — the pattern agent and the
/// inventor — run on every pass in the evaluation, so what is left that is
/// genuinely an escalation is blocking on the literature the run has otherwise
/// been gathering in the background.
#[tokio::test]
async fn a_stuck_run_escalates_to_the_literature() {
    let run = run_with(json!({
        "attempts": 1, "solved": false, "unproductive": STUCK_THRESHOLD, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "no progress", "fresh_context": ""
    }))
    .await;
    run.assert_node_ran("diversify_library");
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
    // Blocked outranks the stuck arms, so the escalation may not have run even
    // though the unproductive count alone would have sent it there.
    run.assert_node_skipped("diversify_library");
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
    run.assert_node_skipped("diversify_library");
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
    run.assert_node_ran("diversify_library");
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

    for ladder in [reflect_ladder(), terminal_condition()] {
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

/// The restart arm is gone from the graph, and that has to stay deliberate.
///
/// A restart used to be a route: the judge ran first and a restart verdict
/// skipped the reflection. The judge and the reflection are concurrent now, so
/// by the time anything routes there is no reflection left to skip — the
/// restart's whole effect is what `judge_step` writes into the state, and
/// `MAX_RESTARTS` is enforced there. This asserts the graph does not quietly
/// grow the port back, because a `restart` port with nowhere to go is a verdict
/// silently dropped.
#[test]
fn nothing_in_the_graph_routes_on_a_restart() {
    let graph = graph();
    let ports: Vec<&str> = graph
        .edges
        .iter()
        .map(|edge| edge.from_port.as_str())
        .collect();
    assert!(
        !ports.contains(&"restart"),
        "the graph has a restart port again: {ports:?}"
    );
}

/// The state chains through a pass rather than every step reading the pass's
/// opening accumulator.
///
/// The loop head folds at the *top* of a pass, so `nodes.solve.state` is what
/// the *previous* pass ended with for the whole of this one. Every step reading
/// it meant the judge scored the previous attempt's report and the reflection
/// overwrote both — the attempt's counters and the judge's verdict were computed
/// and then thrown away, once per pass, with nothing in the trace to say so. A
/// fixed mock hides it completely, which is why the mock here answers each call
/// differently and the assertion is on what each step was *handed*.
#[tokio::test]
async fn each_step_is_handed_what_the_step_before_it_produced() {
    use crate::orchestrator::solutions::SolutionState;

    let marked = |mark: &str, solved: bool| {
        let mut state = SolutionState::new("find the largest x");
        state.attempts = 1;
        state.solved = solved;
        state.last_attempt = mark.to_string();
        Respond::value(state.to_accumulator())
    };

    let run = TestHarness::new(&graph())
        .mock_tool(
            super::super::loop_steps::TOOL,
            // attempt, judge, reflect, goal_apply. The last is solved, so the
            // fold ends the run after one pass.
            Respond::sequence([
                // The seed call to the goals child, before the loop starts.
                marked("the seed decomposition", false),
                marked("what the attempt found", false),
                marked("what the judge made of it", false),
                marked("what the reflection concluded", false),
                marked("what the goals step passed on", true),
            ]),
        )
        .run()
        .await
        .expect("the loop runs to completion on mocks");

    let handed = |node: &str| {
        run.trace()
            .calls_from(node)
            .first()
            .and_then(|call| call.args.pointer("/state/last_attempt"))
            .and_then(Value::as_str)
            .unwrap_or_default()
            .to_string()
    };

    assert_eq!(handed("judge"), "what the attempt found");
    assert_eq!(handed("reflect"), "what the judge made of it");
    assert_eq!(handed("goal_apply"), "what the reflection concluded");
}

/// The arms' findings reach the merge.
///
/// Each arm is its own node returning its own whole state, so what they found
/// exists only in their outputs. An earlier merge read the loop's accumulator
/// instead — which predates all of them — so the arms' child agent runs were
/// spent and the next attempt's briefing was composed out of empty slots.
/// Nothing failed; the run simply carried on knowing none of it.
#[tokio::test]
async fn the_merge_is_handed_every_arms_output() {
    let stuck = json!({
        "attempts": 1, "solved": false, "unproductive": STUCK_THRESHOLD, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0, "since_reduction": 0,
        "lesson": "no progress", "fresh_context": "", "last_attempt": "the loop's own state"
    });
    // What only an arm returns. The accumulator and the arms are both states of
    // the same shape, so a merge reading the wrong one still receives three
    // plausible objects — this is what tells them apart.
    let mut from_arm = stuck.clone();
    from_arm["last_attempt"] = json!("what an arm found");
    let mut finished = stuck.clone();
    finished["solved"] = json!(true);

    let run = TestHarness::new(&graph())
        .mock_tool(
            super::super::loop_steps::TOOL,
            // Stage one and the attempt answer with the loop's own state; every
            // evaluation arm answers with something only an arm could have
            // produced; the merge reports solved so the run ends.
            Respond::sequence([
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                Respond::value(from_arm.clone()),
                Respond::value(from_arm.clone()),
                Respond::value(from_arm.clone()),
                Respond::value(from_arm.clone()),
                Respond::value(from_arm.clone()),
                Respond::value(from_arm.clone()),
                Respond::value(finished),
            ]),
        )
        .run()
        .await
        .expect("the loop runs to completion on mocks");

    let arms = run
        .trace()
        .calls_from(EVAL_MERGE)
        .first()
        .and_then(|call| call.args.get(super::super::loop_steps::ARMS_ARG).cloned())
        .unwrap_or(Value::Null);

    let arms = arms.as_array().cloned().unwrap_or_default();
    assert_eq!(arms.len(), eval_arm_ids().len(), "{arms:#?}");
    for arm in &arms {
        assert_eq!(
            arm.get("last_attempt"),
            Some(&json!("what an arm found")),
            "the merge was handed something other than an arm's output: {arm}"
        );
    }
}

/// The goals child is handed the reflection's state, not the accumulator.
///
/// The cadence counter it reads is moved by the reflection, and the accumulator
/// is a pass behind while the body runs — so a child seeded from the accumulator
/// would decide this cycle's decomposition on last cycle's count.
#[tokio::test]
async fn the_goals_child_reads_the_reflection_the_loop_just_made() {
    use crate::orchestrator::solutions::SolutionState;
    use crate::orchestrator::workflow_goals::{GATE_NODE, STATE_INPUT};

    let mut due = SolutionState::new("find the largest x");
    due.attempts = 1;
    due.solved = false;
    due.since_reduction = crate::orchestrator::solutions::REDUCTION_INTERVAL;
    let mut done = due.clone();
    done.solved = true;

    let run = TestHarness::new(&graph())
        .mock_tool(
            super::super::loop_steps::TOOL,
            Respond::sequence([
                // The seed call, then attempt and judge.
                Respond::value(due.to_accumulator()),
                Respond::value(due.to_accumulator()),
                Respond::value(due.to_accumulator()),
                // The reflection: due, so the in-loop child must ask its gate.
                Respond::value(due.to_accumulator()),
                Respond::value(done.to_accumulator()),
            ]),
        )
        .run()
        .await
        .expect("the loop runs to completion on mocks");

    run.assert_node_ran(GOALS_NODE);

    // The child's own run state, as the parent received it. Its `gate` node
    // having run is the assertion: the gate is only reachable through the
    // cadence switch, and the cadence only comes due on the count the reflection
    // just moved. Seeded from the accumulator instead, the child would have read
    // the previous pass's count and held.
    let child = run
        .output()
        .pointer(&format!("/nodes/{GOALS_NODE}/items/0/json"))
        .cloned()
        .unwrap_or(Value::Null);
    assert_eq!(
        child.pointer(&format!("/run/inputs/{STATE_INPUT}/since_reduction")),
        Some(&json!(crate::orchestrator::solutions::REDUCTION_INTERVAL)),
        "the child was seeded with the wrong state: {child}"
    );
    assert!(
        child.pointer(&format!("/nodes/{GATE_NODE}")).is_some(),
        "the cadence was due and the gate was not asked: {child}"
    );
    assert!(
        child.pointer("/nodes/held").is_none(),
        "the child both asked and held: {child}"
    );
}

/// The evaluation arms run at the same time, not one after another.
///
/// The property the fan-out exists for, and the one no assertion about routing
/// can see: arms wired to the same port still produce the right answer run
/// sequentially, just N times slower. Each arm here takes the same measurable
/// time, so a sequential engine would take all of them end to end.
///
/// This is the whole claim of the three-stage shape. The five questions about
/// an attempt used to be asked in a line — and three of them were not even
/// nodes, they were spawns hidden inside the reflection's body, which meant the
/// graph could not show them, bound them, or checkpoint between them.
///
/// Timing rather than instrumentation, because concurrency is a wall-clock claim
/// and the margin is wide rather than tight.
#[tokio::test]
async fn the_evaluation_arms_run_concurrently() {
    use std::time::{Duration, Instant};

    let arm_time = Duration::from_millis(300);
    let stuck = json!({
        "attempts": 1, "solved": false, "unproductive": STUCK_THRESHOLD, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0, "since_reduction": 0,
        "lesson": "no progress", "fresh_context": ""
    });
    let mut finished = stuck.clone();
    finished["solved"] = json!(true);
    let slow = || Respond::Delay(arm_time, Box::new(Respond::value(stuck.clone())));

    let started = Instant::now();
    let run = TestHarness::new(&graph())
        .mock_tool(
            super::super::loop_steps::TOOL,
            Respond::sequence([
                // Stage one and the attempt answer immediately; only the arms
                // are slow, so what is measured is the fan-out alone.
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                Respond::value(stuck.clone()),
                slow(),
                slow(),
                slow(),
                slow(),
                slow(),
                slow(),
                Respond::value(finished),
            ]),
        )
        .run()
        .await
        .expect("the loop runs to completion on mocks");
    let elapsed = started.elapsed();

    for arm in eval_arm_ids() {
        run.assert_node_ran(arm);
    }
    assert!(
        elapsed < arm_time * 3,
        "the arms took {elapsed:?}, which is more than three of the {arm_time:?} each one costs — \
         six of them ran in something close to sequence"
    );
}

/// The goal is decomposed beside the *first* attempt, not after it.
///
/// The reducer works backward from the problem statement, so its input exists
/// before anything has been attempted; the arm is detached, so asking costs the
/// graph nothing. Waiting for a completed cycle means that on a conjecture run —
/// where one attempt/judge/reflect pass is the better part of an hour — every
/// role spends that hour working without a statement of what would be enough.
#[tokio::test]
async fn the_goal_is_decomposed_before_the_first_attempt() {
    let run = run_with(json!({
        "attempts": 1, "solved": true, "unproductive": 0, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "done", "fresh_context": ""
    }))
    .await;

    run.assert_node_ran(SEED_GOALS_NODE);
    let seed = run
        .output()
        .pointer(&format!("/nodes/{SEED_GOALS_NODE}/items/0/json"))
        .cloned()
        .unwrap_or(Value::Null);
    // The seed carries the loop's own opening state, whose cadence starts *at*
    // the interval — so this call is already due and reaches the gate.
    assert!(
        seed.pointer("/nodes/gate").is_some(),
        "the seed call held rather than asking: {seed}"
    );

    // And it ran before the loop, which is the whole point.
    let order = |node: &str| {
        run.trace()
            .steps
            .iter()
            .position(|step| step.node_id == node)
            .unwrap_or(usize::MAX)
    };
    assert!(
        order(SEED_GOALS_NODE) < order("attempt"),
        "the seed decomposition ran after the first attempt"
    );
}
