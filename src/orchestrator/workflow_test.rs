//! The loop graph, driven on mocks.
#![allow(clippy::expect_used, clippy::panic)]

use serde_json::json;
use tinyflows::testkit::{Respond, TestHarness};
use tinyflows::validate::validate_all;

use super::*;
use crate::orchestrator::definitions::workflow_agents;
use crate::orchestrator::default_registry;
use crate::orchestrator::solutions::DIVERSIFY_MERGE;

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
    let run = run_with(json!({
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
    // One pass: solved on the first reflection must not attempt again.
    run.assert_call_count("agent", Some("goals"), 1);
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


/// The end-to-end gate for the switch: the whole loop, on the real capability
/// bundle and the real reflection parser, with only the roles themselves
/// standing in. Everything between the reflection's prose and the routing
/// decision is production code here — the tool invoker, `record_verdict`, the
/// envelope, the fold, and the ladder.
///
/// This is the piece that had to exist before a launcher could be switched: an
/// `agent` node returns text, and until the parser was wired the accumulator
/// had nothing to fold.
#[tokio::test]
async fn the_loop_runs_end_to_end_on_the_real_parser() {
    use std::sync::Arc;

    use tinyflows::compiler::compile;
    use tinyflows::engine::run;

    use crate::agent::budget::RunBudget;
    use crate::agent::{MockModel, Tool};
    use crate::orchestrator::async_subagents::{AgentExecutor, AsyncSubagentManager};
    use crate::orchestrator::caps;
    use crate::orchestrator::reflection_tool::ParseReflection;
    use crate::orchestrator::runner::{SubagentAgentRunner, SubagentTaskRunner};

    /// A role that answers with whatever it was registered to say.
    struct Fixed(&'static str);

    #[async_trait::async_trait]
    impl AgentExecutor for Fixed {
        async fn execute(
            &self,
            _run_id: &str,
            _input: String,
            _steering: tinyagents::harness::steering::SteeringHandle,
            _tracer: Option<Arc<crate::agent::trace::RunTracer>>,
        ) -> Result<String, tinyagents::TinyAgentsError> {
            Ok(self.0.to_string())
        }
    }

    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    for (role, reply) in [
        ("goals", "attempted the thing"),
        ("judge", "SCORE: 4\nVERDICT: PROCEED"),
        // The real parser reads this prose. No workspace is passed, so the
        // executable-artifact check cannot run and `solved` rests on the
        // verdict and the progress line agreeing — which is the documented
        // behaviour for an absent workspace, not a shortcut.
        (
            "reflection",
            "VERDICT: SOLVED\nPROGRESS: YES\nKIND: MATHEMATICAL\nLESSON: the bound is tight",
        ),
    ] {
        manager
            .register_executor(role, Arc::new(Fixed(reply)))
            .expect("registering a role once succeeds");
    }

    let workspace = std::env::temp_dir().join(format!("riemann-e2e-{}", std::process::id()));
    std::fs::create_dir_all(&workspace).expect("a scratch workspace can be created");

    let caps = caps::bundle(
        Arc::new(MockModel::constant("unused: every node names a role")),
        &workspace,
        [Arc::new(ParseReflection::new(None)) as Arc<dyn Tool<()>>],
        SubagentTaskRunner::new(manager.clone()),
        SubagentAgentRunner::new(manager),
    );

    let compiled = compile(&graph()).expect("the loop is structurally valid");
    let outcome = run(&compiled, json!({}), &caps)
        .await
        .expect("the loop runs to completion");

    let state = outcome
        .output
        .pointer(&format!("/nodes/{LOOP_NODE}/state"))
        .cloned()
        .unwrap_or(Value::Null);
    // The reflection's prose became the counter that ended the run, through
    // production code the whole way.
    assert_eq!(state["solved"], json!(true), "{state}");
    assert!(
        outcome.output.pointer("/nodes/report").is_some(),
        "the loop never reached its terminal node: {}",
        outcome.output
    );

    let _ = std::fs::remove_dir_all(&workspace);
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

/// The attempt's prose has to survive to the end, or a finished run holds every
/// counter and none of the text those counters are about.
#[tokio::test]
async fn the_attempt_report_reaches_the_accumulator() {
    let run = run_with(json!({
        "attempts": 1, "solved": true, "unproductive": 0, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0,
        "lesson": "done", "fresh_context": ""
    }))
    .await;

    let state = run
        .output()
        .pointer(&format!("/nodes/{LOOP_NODE}/state"))
        .cloned()
        .unwrap_or(Value::Null);
    assert_eq!(state["last_attempt"], json!("attempted"), "{state}");
}


/// The body must have exactly one exit, or the fold reads a stale node.
///
/// The engine's `nodes` map is cumulative, so if a diversify pass could return
/// to the loop head through the merge, the fold would keep reading that merge
/// long after the pass that produced it. Every pass ends at `reflect` instead.
#[test]
fn only_one_node_returns_to_the_loop_head() {
    let graph = graph();
    let returning: Vec<&str> = graph
        .edges
        .iter()
        .filter(|edge| edge.to_node.as_str() == LOOP_NODE)
        .map(|edge| edge.from_node.as_str())
        .collect();
    // `start` seeds the loop; everything else arrives through the one pass node.
    let mut returning: Vec<&str> = returning;
    returning.sort_unstable();
    returning.dedup();
    assert_eq!(
        returning,
        ["start", PASS_NODE],
        "more than one node returns to the loop head, so the fold can read a stale pass"
    );
    // ...and every body path really does reach it.
    for from in ["route", DIVERSIFY_MERGE] {
        assert!(
            graph
                .edges
                .iter()
                .any(|edge| edge.from_node.as_str() == from
                    && edge.to_node.as_str() == PASS_NODE),
            "`{from}` does not lead to the pass node"
        );
    }
}
