//! Deterministic tests for graph-backed asynchronous subagent controls.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use tinyagents::harness::steering::SteeringCommand;
use tokio::sync::Semaphore;

use crate::agent::Tool as _;

use crate::orchestrator::runs::RunStatus;
use super::{AgentExecutor, AsyncSubagentManager, DEFAULT_MAX_CONCURRENT_AGENTS};
use crate::agent::Result;
use crate::agent::budget::RunBudget;
use crate::agent::trace::RunTracer;

struct SteerableExecutor {
    started: Arc<Semaphore>,
    release: Arc<Semaphore>,
}

#[async_trait::async_trait]
impl AgentExecutor for SteerableExecutor {
    async fn execute(
        &self,
        _run_id: &str,
        input: String,
        steering: tinyagents::harness::steering::SteeringHandle,
        _tracer: Option<Arc<RunTracer>>,
    ) -> Result<String> {
        self.started.add_permits(1);
        let _permit = self.release.acquire().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("test release semaphore closed: {error}"))
        })?;
        let redirect = steering
            .drain()
            .into_iter()
            .find_map(|command| match command {
                SteeringCommand::Redirect { instruction } => Some(instruction),
                _ => None,
            });
        Ok(format!("{input}:{}", redirect.unwrap_or_default()))
    }
}

#[tokio::test]
async fn spawn_returns_before_completion_then_peek_and_await_return_response() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    let started = Arc::new(Semaphore::new(0));
    let release = Arc::new(Semaphore::new(0));
    manager.register_executor(
        "worker",
        Arc::new(SteerableExecutor {
            started: started.clone(),
            release: release.clone(),
        }),
    )?;

    let run_id = manager.spawn("worker", "initial".into())?;
    let _started = started.acquire().await.map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("test start semaphore closed: {error}"))
    })?;
    let running = manager.record(run_id.as_str())?;
    assert_eq!(running.status, RunStatus::Running);

    manager.steer(run_id.as_str(), "focus on proof".into())?;
    release.add_permits(1);
    let completed = manager.await_record(run_id.as_str(), 1).await?;
    assert_eq!(completed.status, RunStatus::Completed);
    assert_eq!(
        completed.result.and_then(|result| result.text),
        Some("initial:focus on proof".into())
    );
    Ok(())
}

#[tokio::test]
async fn independent_runs_can_execute_in_parallel() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    let started = Arc::new(Semaphore::new(0));
    let release = Arc::new(Semaphore::new(0));
    manager.register_executor(
        "worker",
        Arc::new(SteerableExecutor {
            started: started.clone(),
            release: release.clone(),
        }),
    )?;

    let first = manager.spawn("worker", "first".into())?;
    let second = manager.spawn("worker", "second".into())?;
    let _started = started.acquire_many(2).await.map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("test start semaphore closed: {error}"))
    })?;
    assert_eq!(
        manager.record(first.as_str())?.status,
        RunStatus::Running
    );
    assert_eq!(
        manager.record(second.as_str())?.status,
        RunStatus::Running
    );

    release.add_permits(2);
    assert_eq!(
        manager.await_record(first.as_str(), 1).await?.status,
        RunStatus::Completed
    );
    assert_eq!(
        manager.await_record(second.as_str(), 1).await?.status,
        RunStatus::Completed
    );
    Ok(())
}

#[test]
fn the_default_cap_is_wide_enough_for_the_fan_out_the_registry_can_produce() {
    // The cap bounds provider concurrency; it is not a queue. A parent holds
    // its slot while awaiting children, so the default has to stay far above
    // the depth and width the registry can reach, or a pool full of parents
    // waiting on queued children would deadlock.
    const { assert!(DEFAULT_MAX_CONCURRENT_AGENTS >= 50) }
}

#[tokio::test]
async fn concurrent_runs_are_capped_and_the_queue_drains() -> Result<()> {
    let manager = AsyncSubagentManager::with_concurrency(RunBudget::default(), None, 2);
    let started = Arc::new(Semaphore::new(0));
    let release = Arc::new(Semaphore::new(0));
    manager.register_executor(
        "worker",
        Arc::new(SteerableExecutor {
            started: started.clone(),
            release: release.clone(),
        }),
    )?;

    let ids = (0..4)
        .map(|index| manager.spawn("worker", format!("task-{index}")))
        .collect::<Result<Vec<_>>>()?;

    // Two runs start; the other two wait for a slot rather than for input.
    let _first_pair = started.acquire_many(2).await.map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("test start semaphore closed: {error}"))
    })?;
    assert_eq!(started.available_permits(), 0);

    // Spawning stayed non-blocking: every run has an id and a record already.
    for id in &ids {
        assert!(manager.record(id.as_str()).is_ok());
    }

    // Releasing the running pair lets the queued pair through.
    release.add_permits(4);
    for id in &ids {
        assert_eq!(
            manager.await_record(id.as_str(), 5).await?.status,
            RunStatus::Completed
        );
    }
    Ok(())
}

#[tokio::test]
async fn a_missing_follow_up_agent_is_not_an_error() -> Result<()> {
    // A registry built without the scholar must still run research.
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    let started = Arc::new(Semaphore::new(0));
    let release = Arc::new(Semaphore::new(0));
    manager.register_executor(
        "research",
        Arc::new(SteerableExecutor {
            started: started.clone(),
            release: release.clone(),
        }),
    )?;

    let run_id = manager.spawn("research", "find it".into())?;
    release.add_permits(1);
    assert_eq!(
        manager.await_record(run_id.as_str(), 5).await?.status,
        RunStatus::Completed
    );
    Ok(())
}

#[test]
fn the_follow_up_chain_cannot_loop() {
    // A follow-up that was itself followed up would tidy forever. Steps run
    // sequentially inside one sequence, so this invariant is what bounds the
    // whole mechanism at a single level.
    for (_, steps) in super::FOLLOW_UPS {
        for step in steps {
            assert!(
                !super::FOLLOW_UPS
                    .iter()
                    .any(|(after, _)| *after == step.agent),
                "{} triggers a follow-up and is one",
                step.agent
            );
        }
    }
}

#[test]
fn research_is_followed_by_the_scholar_only() {
    let (_, steps) = super::FOLLOW_UPS
        .iter()
        .find(|(after, _)| *after == "research")
        .expect("research triggers a follow-up sequence");
    let agents: Vec<&str> = steps.iter().map(|step| step.agent).collect();
    assert_eq!(agents, vec!["scholar"]);
}

/// An executor that finishes immediately, echoing its brief.
struct EchoExecutor;

#[async_trait::async_trait]
impl AgentExecutor for EchoExecutor {
    async fn execute(
        &self,
        run_id: &str,
        input: String,
        _steering: tinyagents::harness::steering::SteeringHandle,
        _tracer: Option<Arc<RunTracer>>,
    ) -> Result<String> {
        Ok(format!("{run_id}:{input}"))
    }
}

#[tokio::test]
async fn one_call_launches_a_whole_fan_out_and_one_call_collects_it() -> Result<()> {
    // The reason this tool exists: each spawn_agent costs a full model turn,
    // measured at a p90 of 197s on a live run, so launching five agents one at
    // a time spent minutes before any of them started.
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    manager.register_executor("worker", Arc::new(EchoExecutor))?;
    let allowed = Arc::new(vec!["worker".to_string()]);
    let spawn = super::AsyncSubagentTool::new(
        super::AsyncToolKind::SpawnMany,
        manager.clone(),
        allowed.clone(),
    );

    let runs: Vec<serde_json::Value> = (0..5)
        .map(|n| serde_json::json!({ "agent": "worker", "input": format!("piece {n}") }))
        .collect();
    let result = spawn
        .call(
            &(),
            crate::agent::ToolCall {
                id: "call-1".into(),
                name: "spawn_agents".into(),
                invalid: None,
                arguments: serde_json::json!({ "runs": runs }),
            },
        )
        .await?;
    let started: serde_json::Value = serde_json::from_str(&result.content)?;
    let ids = started["runs"].as_array().expect("runs array");
    assert_eq!(ids.len(), 5);

    // Omitting run_ids collects everything outstanding, which is the shape a
    // caller wants right after a batch spawn.
    let await_tool =
        super::AsyncSubagentTool::new(super::AsyncToolKind::AwaitMany, manager.clone(), allowed);
    let collected = await_tool
        .call(
            &(),
            crate::agent::ToolCall {
                id: "call-2".into(),
                name: "await_agents".into(),
                invalid: None,
                arguments: serde_json::json!({ "wait_seconds": 10 }),
            },
        )
        .await?;
    let collected: serde_json::Value = serde_json::from_str(&collected.content)?;
    assert_eq!(collected["runs"].as_array().expect("runs array").len(), 5);
    Ok(())
}

#[tokio::test]
async fn a_batch_with_one_forbidden_agent_starts_nothing() -> Result<()> {
    // Half-launching is worse than refusing: the caller is told the call
    // failed while agents it never accounted for are already spending budget.
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    manager.register_executor("worker", Arc::new(EchoExecutor))?;
    let spawn = super::AsyncSubagentTool::new(
        super::AsyncToolKind::SpawnMany,
        manager.clone(),
        Arc::new(vec!["worker".to_string()]),
    );
    let result = spawn
        .call(
            &(),
            crate::agent::ToolCall {
                id: "call-1".into(),
                name: "spawn_agents".into(),
                invalid: None,
                arguments: serde_json::json!({ "runs": [
                    { "agent": "worker", "input": "allowed" },
                    { "agent": "intruder", "input": "not allowed" }
                ] }),
            },
        )
        .await;
    assert!(result.is_err(), "a forbidden agent must refuse the batch");
    assert!(
        manager.outstanding_runs().is_empty(),
        "nothing may have started"
    );
    Ok(())
}

#[test]
fn two_managers_never_share_a_trace_id() {
    // Run ids are allocated per process from one, so every container's first
    // specialist run is `agent-run-1`. Before the session qualified the trace
    // id, two problems solved side by side reported into a single Langfuse
    // trace whose observations interleaved runs that shared nothing.
    let first = AsyncSubagentManager::new(RunBudget::default(), None);
    let second = AsyncSubagentManager::new(RunBudget::default(), None);
    assert_ne!(
        first.session, second.session,
        "each process's runs need their own trace namespace"
    );
}

#[test]
fn a_trace_is_named_for_the_role_that_produced_it() {
    let config = super::trace_config("s-session", "scholar", "agent-run-1", None);
    assert_eq!(config.name.as_deref(), Some("scholar · agent-run-1"));
    assert_eq!(config.trace_id.as_deref(), Some("s-session-agent-run-1"));
    assert!(config.tags.contains(&"agent:scholar".to_string()));
    assert_eq!(config.metadata["agent"], "scholar");
    assert_eq!(config.metadata["run_id"], "agent-run-1");
}

#[test]
fn every_agent_on_one_problem_shares_a_session_and_a_user() {
    // Langfuse filters by user before anything else, and the question asked of
    // this data is "what happened on 591", so the problem occupies that
    // dimension. Grouping every role into one session is what makes a run
    // readable as one investigation rather than as unrelated traces.
    //
    let problem = Some("project-euler/591");
    let scholar = super::trace_config("s-1", "scholar", "agent-run-4", problem);
    let learner = super::trace_config("s-1", "reflection", "agent-run-5", problem);

    assert_eq!(scholar.user_id.as_deref(), Some("project-euler/591"));
    assert_eq!(learner.user_id, scholar.user_id);
    assert_eq!(
        scholar.session_id.as_deref(),
        Some("project-euler/591@s-1"),
        "one attempt at one problem is one session"
    );
    assert_eq!(learner.session_id, scholar.session_id);
    assert_ne!(
        scholar.trace_id, learner.trace_id,
        "each agent still gets its own trace inside that session"
    );
    assert!(
        scholar
            .tags
            .contains(&"problem:project-euler/591".to_string())
    );
}

#[test]
fn a_wait_outlives_the_per_tool_ceiling_it_was_never_meant_to_obey() {
    // The run ceiling and the tool ceiling are separate limits, and a wait is
    // governed by the first. A live `pattern_finder` asked for 600 seconds,
    // was killed at exactly 600,000 ms by the ten-minute tool ceiling, and
    // lost the run it had commissioned.
    //
    // The wait asked for here is the child's whole run budget, which is the
    // case the invariant is about: a caller collecting the deepest work it
    // delegated waits that long, and the tool ceiling must not cut it off.
    // Asking for a fixed 600 seconds tested the same thing only while the tool
    // ceiling happened to be ten minutes, and stopped meaning anything when it
    // was raised.
    use tinyagents::harness::tool::ToolTimeout;

    let budget = RunBudget::default();
    let manager = AsyncSubagentManager::new(budget, None);
    let tools = manager.tools(["worker"]);
    let waiting = tools
        .iter()
        .find(|tool| tool.name() == "await_agent")
        .expect("await_agent is registered");

    let full_run = budget.run_timeout.as_secs();
    assert!(
        budget.run_timeout > budget.tool_timeout,
        "the run ceiling is the outer limit, so a full-length wait is the case that needs the \
         exemption"
    );
    let asked = crate::agent::ToolCall {
        id: "call-1".into(),
        name: "await_agent".into(),
        invalid: None,
        arguments: serde_json::json!({ "run_id": "agent-run-1", "wait_seconds": full_run }),
    };
    let deadline = match waiting.timeout_policy(&asked) {
        ToolTimeout::Millis(deadline) => deadline,
        other => unreachable!("a wait carries its own deadline, not {other:?}"),
    };
    assert!(
        u128::from(deadline) > budget.tool_timeout.as_millis(),
        "the wait outlives the tool ceiling: {deadline}"
    );
    assert!(
        deadline > full_run * 1_000,
        "and outlives the wait it was asked for, so the wait returns rather than being cut off"
    );

    // Everything else is a fast local operation and keeps the ordinary ceiling.
    let spawning = tools
        .iter()
        .find(|tool| tool.name() == "spawn_agent")
        .expect("spawn_agent is registered");
    assert_eq!(
        spawning.timeout_policy(&asked),
        ToolTimeout::Inherit,
        "a spawn returns immediately and needs no exemption"
    );
}

/// Two schools register their own copy of a role on one manager.
///
/// One manager is the point: one semaphore, one run store, one trace. If a
/// second school needed a second manager, the concurrency cap would bound each
/// school rather than the run, which is the one thing it exists to do.
#[test]
fn two_schools_register_their_own_copy_of_a_role() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    for slug in ["chisel", "rising-sea"] {
        manager
            .for_school(slug)
            .register_executor("goals", Arc::new(EchoExecutor))?;
    }
    assert!(manager.knows_exactly("goals@chisel"));
    assert!(manager.knows_exactly("goals@rising-sea"));
    assert!(
        !manager.knows_exactly("goals"),
        "a scoped registration must not also claim the bare name"
    );
    Ok(())
}

/// A bare role name spawned from a school reaches that school's copy.
///
/// This is what lets every bench and every loop step keep naming roles bare: a
/// `goals@rising-sea` that delegated to a plain `tool_builder` would have left
/// its school without anything saying so.
#[tokio::test]
async fn a_school_resolves_a_bare_role_to_its_own_copy() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    for slug in ["chisel", "rising-sea"] {
        manager
            .for_school(slug)
            .register_executor("tool_builder", Arc::new(EchoExecutor))?;
    }
    let sea = manager.for_school("rising-sea");
    let run_id = sea.spawn("tool_builder", "compute".into())?;
    let record = sea.await_record(run_id.as_str(), 5).await?;
    assert_eq!(record.agent, "tool_builder@rising-sea");
    assert!(
        manager.spawn("tool_builder", "compute".into()).is_err(),
        "the unscoped manager has no unqualified copy to reach"
    );
    Ok(())
}

/// A role registered once for the whole run is still reachable from a school.
///
/// The fallback is what keeps a partially schooled registry usable rather than
/// turning a missing overlay into an unknown-agent error mid-run.
#[test]
fn a_school_falls_back_to_an_unqualified_registration() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    manager.register_executor("scholar", Arc::new(EchoExecutor))?;
    assert!(manager.for_school("adversarial").knows("scholar"));
    Ok(())
}

/// An unscoped manager registers and resolves exactly as it always did.
#[test]
fn one_school_is_the_run_that_existed_before_schools() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    manager.register_executor("judge", Arc::new(EchoExecutor))?;
    assert!(manager.knows_exactly("judge"));
    assert_eq!(manager.resolve("judge"), "judge");
    Ok(())
}

/// A qualified name is the role it qualifies, whoever asks.
#[test]
fn a_qualified_name_still_names_its_role() {
    assert_eq!(super::base_role("judge@rising-sea"), "judge");
    assert_eq!(super::base_role("judge"), "judge");
}

/// Operator direction reaches every live detached run, not just the loop.
///
/// This is the regression for the failure that cost two live investigations
/// hours apiece: a directive was posted to the mailbox and handed to the
/// director, both of which stop at the orchestrator, while the specialist it
/// was aimed at held the instruction it was spawned with and never heard it.
/// Three consecutive directives to stop re-confirming a settled number were
/// each acknowledged in the ledger while the role produced eight more
/// artifacts.
#[tokio::test]
async fn a_directive_reaches_every_live_run() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    let started = Arc::new(Semaphore::new(0));
    let release = Arc::new(Semaphore::new(0));
    manager.register_executor(
        "worker",
        Arc::new(SteerableExecutor {
            started: started.clone(),
            release: release.clone(),
        }),
    )?;

    let first = manager.spawn("worker", "first".into())?;
    let second = manager.spawn("worker", "second".into())?;
    let _started = started.acquire_many(2).await.map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("test start semaphore closed: {error}"))
    })?;

    let reached = manager.redirect_live("stop re-confirming K*");
    assert_eq!(reached.len(), 2, "both live runs must hear the directive");

    release.add_permits(2);
    for run in [&first, &second] {
        let completed = manager.await_record(run.as_str(), 1).await?;
        assert_eq!(
            completed.result.and_then(|result| result.text),
            Some(format!(
                "{}:stop re-confirming K*",
                if run == &first { "first" } else { "second" }
            )),
            "the directive must arrive as the run's own steering, not beside it"
        );
    }
    Ok(())
}

/// A finished run is skipped, not reported as a delivery failure.
///
/// The queue's exactly-once guarantee is the cursor, so a specialist that
/// completes between the drain and the redirect is ordinary. Counting it as
/// reached would overstate delivery; erroring on it would make one finished
/// role suppress the directive for every other.
#[tokio::test]
async fn a_finished_run_is_skipped_rather_than_failing_the_delivery() -> Result<()> {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    manager.register_executor("judge", Arc::new(EchoExecutor))?;
    let done = manager.spawn("judge", "already done".into())?;
    let _ = manager.await_record(done.as_str(), 1).await?;

    assert!(
        manager.redirect_live("late direction").is_empty(),
        "a terminal run is not a live delivery"
    );
    Ok(())
}
