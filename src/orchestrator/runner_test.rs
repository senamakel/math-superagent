//! Deterministic tests for offering this crate's agents to `TinyFlows`.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use tokio::sync::Semaphore;

use serde_json::json;

use super::*;
use crate::agent::Result;
use crate::agent::budget::RunBudget;
use crate::orchestrator::async_subagents::AgentExecutor;

/// An executor that reports when it started and blocks until released, so a
/// test can observe a ticket while its work is genuinely still running.
struct HeldExecutor {
    started: Arc<Semaphore>,
    release: Arc<Semaphore>,
    fail: bool,
}

#[async_trait]
impl AgentExecutor for HeldExecutor {
    async fn execute(
        &self,
        _run_id: &str,
        input: String,
        _steering: tinyagents::harness::steering::SteeringHandle,
        _tracer: Option<Arc<crate::agent::trace::RunTracer>>,
    ) -> Result<String> {
        self.started.add_permits(1);
        let _permit = self.release.acquire().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("test release semaphore closed: {error}"))
        })?;
        if self.fail {
            return Err(tinyagents::TinyAgentsError::Tool("refused".into()));
        }
        Ok(format!("did: {input}"))
    }
}

fn runner_with(fail: bool) -> (SubagentTaskRunner, Arc<Semaphore>, Arc<Semaphore>) {
    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    let started = Arc::new(Semaphore::new(0));
    let release = Arc::new(Semaphore::new(0));
    manager
        .register_executor(
            "scholar",
            Arc::new(HeldExecutor {
                started: started.clone(),
                release: release.clone(),
                fail,
            }),
        )
        .expect("registering an executor once succeeds");
    (SubagentTaskRunner::new(manager), started, release)
}

/// The whole point of a `spawn`: the ticket comes back while the work is still
/// going, so the branch carries on instead of blocking on the agent.
#[tokio::test]
async fn a_ticket_comes_back_while_the_agent_is_still_running() {
    let (runner, started, release) = runner_with(false);

    let ticket = runner
        .start(spawn_spec("scholar", "read the library"))
        .await
        .expect("a registered agent starts");

    let _running = started.acquire().await.expect("the agent starts");
    assert_eq!(
        runner.poll(&ticket).await.expect("the ticket is known"),
        TaskState::Running
    );

    release.add_permits(1);
    let settled = loop {
        let state = runner.poll(&ticket).await.expect("the ticket is known");
        if state.is_settled() {
            break state;
        }
        tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    };
    assert_eq!(
        settled,
        TaskState::Done(Value::String("did: read the library".into()))
    );
}

/// A gate routes a failure differently from a thin result, so the two must not
/// arrive as the same state.
#[tokio::test]
async fn a_failed_run_settles_as_failed_rather_than_as_an_empty_result() {
    let (runner, started, release) = runner_with(true);

    let ticket = runner
        .start(spawn_spec("scholar", "read the library"))
        .await
        .expect("a registered agent starts");
    let _running = started.acquire().await.expect("the agent starts");
    release.add_permits(1);

    let settled = loop {
        let state = runner.poll(&ticket).await.expect("the ticket is known");
        if state.is_settled() {
            break state;
        }
        tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    };
    assert!(
        matches!(settled, TaskState::Failed(ref why) if why.contains("refused")),
        "{settled:?}"
    );
}

/// A name that was never registered is a fault in the workflow, not in the
/// work: no gate policy or retry makes it start, so it fails at the spawn.
#[tokio::test]
async fn an_unregistered_agent_is_refused_at_the_spawn() {
    let (runner, _started, _release) = runner_with(false);
    let error = runner
        .start(spawn_spec("nobody", "do a thing"))
        .await
        .expect_err("an unknown agent cannot be started");
    assert!(error.to_string().contains("nobody"), "{error}");
}

#[tokio::test]
async fn a_spec_that_names_no_agent_or_prompt_is_refused() {
    let (runner, _started, _release) = runner_with(false);

    // The engine's other spec shapes want a child graph run and an HTTP
    // request. Approximating either would start the wrong work and report
    // success, so both are refused.
    let http = runner
        .start(TaskSpec::Http {
            request: json!({ "url": "https://example.invalid" }),
        })
        .await
        .expect_err("this host starts agents, not requests");
    assert!(http.to_string().contains("tool spec"), "{http}");

    let promptless = runner
        .start(TaskSpec::Tool {
            slug: "scholar".into(),
            args: json!({}),
        })
        .await
        .expect_err("an agent with nothing to do is not startable");
    assert!(promptless.to_string().contains("prompt"), "{promptless}");

    let blank = runner
        .start(spawn_spec("scholar", "   "))
        .await
        .expect_err("whitespace is not an instruction");
    assert!(blank.to_string().contains("prompt"), "{blank}");
}

#[tokio::test]
async fn an_unknown_ticket_is_an_error_rather_than_a_settled_state() {
    let (runner, _started, _release) = runner_with(false);
    // The trait reserves an error for exactly this, so a gate waiting on a
    // ticket the host has forgotten hears about it instead of waiting forever.
    assert!(runner.poll("agent-run-999").await.is_err());
    assert!(runner.cancel("agent-run-999").await.is_err());
}

/// Cancelling something that has already finished is not a failure — a gate
/// that gives up on a straggler may well cancel a ticket that settled first.
#[tokio::test]
async fn cancelling_a_settled_run_is_accepted_and_does_nothing() {
    let (runner, started, release) = runner_with(false);
    let ticket = runner
        .start(spawn_spec("scholar", "read the library"))
        .await
        .expect("a registered agent starts");
    let _running = started.acquire().await.expect("the agent starts");
    release.add_permits(1);
    while !runner
        .poll(&ticket)
        .await
        .expect("the ticket is known")
        .is_settled()
    {
        tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    }

    runner.cancel(&ticket).await.expect("a settled ticket is fine to cancel");
    assert!(
        runner
            .poll(&ticket)
            .await
            .expect("the ticket is known")
            .is_settled()
    );
}
