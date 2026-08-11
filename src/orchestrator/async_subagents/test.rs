//! Deterministic tests for graph-backed asynchronous subagent controls.

use std::sync::Arc;

use tinyagents::graph::OrchestrationTaskStatus;
use tinyagents::harness::steering::SteeringCommand;
use tokio::sync::Notify;

use super::{AgentExecutor, AsyncSubagentManager};
use crate::agent::Result;

struct SteerableExecutor {
    started: Arc<Notify>,
    release: Arc<Notify>,
}

#[async_trait::async_trait]
impl AgentExecutor for SteerableExecutor {
    async fn execute(
        &self,
        _run_id: &str,
        input: String,
        steering: tinyagents::harness::steering::SteeringHandle,
    ) -> Result<String> {
        self.started.notify_one();
        self.release.notified().await;
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
    let manager = AsyncSubagentManager::new();
    let started = Arc::new(Notify::new());
    let release = Arc::new(Notify::new());
    manager.register_executor(
        "worker",
        Arc::new(SteerableExecutor {
            started: started.clone(),
            release: release.clone(),
        }),
    )?;

    let run_id = manager.spawn("worker", "initial".into())?;
    started.notified().await;
    let running = manager.record(run_id.as_str())?;
    assert_eq!(running.status, OrchestrationTaskStatus::Running);

    manager.steer(run_id.as_str(), "focus on proof".into())?;
    release.notify_one();
    let completed = manager.await_record(run_id.as_str(), 1).await?;
    assert_eq!(completed.status, OrchestrationTaskStatus::Completed);
    assert_eq!(
        completed.result.and_then(|result| result.text),
        Some("initial:focus on proof".into())
    );
    Ok(())
}

#[tokio::test]
async fn independent_runs_can_execute_in_parallel() -> Result<()> {
    let manager = AsyncSubagentManager::new();
    let started = Arc::new(Notify::new());
    let release = Arc::new(Notify::new());
    manager.register_executor(
        "worker",
        Arc::new(SteerableExecutor {
            started: started.clone(),
            release: release.clone(),
        }),
    )?;

    let first = manager.spawn("worker", "first".into())?;
    let second = manager.spawn("worker", "second".into())?;
    started.notified().await;
    started.notified().await;
    assert_eq!(
        manager.record(first.as_str())?.status,
        OrchestrationTaskStatus::Running
    );
    assert_eq!(
        manager.record(second.as_str())?.status,
        OrchestrationTaskStatus::Running
    );

    release.notify_waiters();
    assert_eq!(
        manager.await_record(first.as_str(), 1).await?.status,
        OrchestrationTaskStatus::Completed
    );
    assert_eq!(
        manager.await_record(second.as_str(), 1).await?.status,
        OrchestrationTaskStatus::Completed
    );
    Ok(())
}
