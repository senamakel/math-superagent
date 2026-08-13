//! The registry of in-flight child agent runs.
//!
//! Every sub-agent this orchestrator starts is detached: `spawn` returns a run
//! id immediately and the work drains behind it, so something has to hold what
//! became of a run between starting it and asking. That is this module — a
//! status per run, its final text or its failure, and the steering handle a
//! live run can still be redirected through.
//!
//! It used to be TinyAgents' orchestration task store, reached through
//! `tinyagents::graph`. The graph runtime moved to TinyFlows (see
//! [`crate::agent::flow`]), which carries no task store at all, deliberately:
//! what a host does with a detached run is the host's business, and TinyFlows
//! keeps agents themselves behind capability traits. This crate is that host,
//! so the registry lives here.
//!
//! It is deliberately narrower than what it replaces. The store it came from
//! also carried a JSONL backend, a detached-task registry, a filter type, and a
//! set of model-visible orchestration tools; none of that was ever reached from
//! here, and this crate exposes its own `spawn_agent` / `await_agents` tools
//! (see `async_subagents_tool.rs`) rather than the generic ones. What is kept is
//! what a caller reads: the status, the result, and the error.

use std::collections::{BTreeMap, HashMap};
use std::sync::{Arc, Mutex};

use tinyagents::TinyAgentsError;
use tinyagents::harness::ids::TaskId;
use tinyagents::harness::steering::SteeringHandle;

use crate::agent::Result;

/// Where a run has got to.
///
/// The two predicates below are the only questions asked of it, and they are
/// not complements: a `Pending` run is neither live-and-steerable nor finished.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum RunStatus {
    /// Accepted and queued, not yet holding a concurrency slot.
    Pending,
    /// Executing now.
    Running,
    /// Finished with a response.
    Completed,
    /// Finished without one.
    Failed,
}

impl RunStatus {
    /// Whether the run is executing and can still be steered.
    ///
    /// A queued run is not live: nothing is reading its steering handle yet, so
    /// a redirect sent to one would be silently dropped.
    pub(super) fn is_live(self) -> bool {
        matches!(self, Self::Running)
    }

    /// Whether the run has finished, either way.
    ///
    /// This is what ends an await loop, so it must be true for a failure as
    /// well as a success — a waiter that only recognised success would block
    /// until its deadline on every failed run.
    pub(super) fn is_terminal(self) -> bool {
        matches!(self, Self::Completed | Self::Failed)
    }

    /// The lowercase name a model reads in a tool result.
    ///
    /// The same four words the previous record serialized to, so a prompt or a
    /// transcript that refers to a run being `running` still reads true.
    pub(super) fn as_str(self) -> &'static str {
        match self {
            Self::Pending => "pending",
            Self::Running => "running",
            Self::Completed => "completed",
            Self::Failed => "failed",
        }
    }
}

/// What a finished run produced.
#[derive(Clone, Debug, Default)]
pub(super) struct RunOutcome {
    /// The run's final text, when it produced one.
    pub(super) text: Option<String>,
}

impl RunOutcome {
    /// Wraps a run's final text.
    pub(super) fn text(text: impl Into<String>) -> Self {
        Self {
            text: Some(text.into()),
        }
    }
}

/// One run, as the registry holds it.
#[derive(Clone, Debug)]
pub(super) struct RunRecord {
    task_id: TaskId,
    /// The registered agent name the run was started against.
    pub(super) agent: String,
    /// Where the run has got to.
    pub(super) status: RunStatus,
    /// The run's output, once it has completed.
    pub(super) result: Option<RunOutcome>,
    /// Why the run failed, once it has failed.
    pub(super) error: Option<String>,
}

impl RunRecord {
    /// The run's id.
    pub(super) fn task_id(&self) -> &TaskId {
        &self.task_id
    }

    /// Renders the record as the JSON a model sees from `await_agent`,
    /// `await_agents`, and `peek_agent`.
    ///
    /// Written out here rather than derived, so the shape a model reads is
    /// stated in one place and changes deliberately. The record it replaced was
    /// derived, and what reached the model was the derivation: a nested `spec`
    /// object that echoed the whole prompt back — the caller wrote it, so it is
    /// the one thing in the record the caller already knows — beside four
    /// `SystemTime` structs rendered as `{secs_since_epoch, nanos_since_epoch}`.
    /// This is the same information a caller acts on, flat and readable:
    /// which run, which agent, where it got to, and what it produced.
    ///
    /// `result` and `error` are omitted while absent rather than sent as
    /// `null`, so a pending run does not read as one that finished empty.
    pub(super) fn to_json(&self) -> serde_json::Value {
        let mut value = serde_json::json!({
            "run_id": self.task_id.as_str(),
            "agent": self.agent,
            "status": self.status.as_str(),
        });
        if let Some(text) = self.result.as_ref().and_then(|result| result.text.as_ref())
            && let Some(object) = value.as_object_mut()
        {
            object.insert("result".into(), serde_json::Value::String(text.clone()));
        }
        if let Some(error) = self.error.as_ref()
            && let Some(object) = value.as_object_mut()
        {
            object.insert("error".into(), serde_json::Value::String(error.clone()));
        }
        value
    }
}

/// Every run started in this process, by id.
///
/// Ordered rather than hashed so [`Self::list`] returns runs in a stable order.
/// `outstanding_runs` feeds that listing straight into an `await_agents` call
/// with no arguments, and a set of waits that reordered itself between two
/// identical calls would be a needless source of irreproducible runs.
///
/// A poisoned lock is treated as an empty registry rather than a panic. Library
/// code here must not panic, and a registry that has lost its contents is a
/// run that reports its children as unknown — recoverable — where a panic
/// inside a detached task is not.
#[derive(Clone, Debug, Default)]
pub(super) struct RunStore {
    inner: Arc<Mutex<BTreeMap<String, RunRecord>>>,
}

impl RunStore {
    /// Creates an empty registry.
    pub(super) fn new() -> Self {
        Self::default()
    }

    /// Records a newly accepted run as [`RunStatus::Pending`].
    ///
    /// # Errors
    ///
    /// Returns an error when `task_id` is already registered. Ids are minted
    /// from one process-wide counter, so a collision means two managers are
    /// sharing a store with independent counters — a real fault, and one worth
    /// refusing rather than resolving by overwriting a live run's record.
    pub(super) fn insert(&self, task_id: TaskId, agent: impl Into<String>) -> Result<()> {
        let mut guard = self.lock()?;
        if guard.contains_key(task_id.as_str()) {
            return Err(TinyAgentsError::Validation(format!(
                "agent run `{task_id}` is already registered"
            )));
        }
        guard.insert(
            task_id.as_str().to_string(),
            RunRecord {
                task_id,
                agent: agent.into(),
                status: RunStatus::Pending,
                result: None,
                error: None,
            },
        );
        Ok(())
    }

    /// Returns the record for `task_id`, if it is registered.
    pub(super) fn get(&self, task_id: &TaskId) -> Option<RunRecord> {
        self.lock().ok()?.get(task_id.as_str()).cloned()
    }

    /// Returns every registered run, oldest id first.
    pub(super) fn list(&self) -> Vec<RunRecord> {
        self.lock()
            .map(|guard| guard.values().cloned().collect())
            .unwrap_or_default()
    }

    /// Moves a run to [`RunStatus::Running`].
    pub(super) fn mark_running(&self, task_id: &TaskId) {
        self.update(task_id, |record| record.status = RunStatus::Running);
    }

    /// Files a run's output and marks it [`RunStatus::Completed`].
    pub(super) fn complete(&self, task_id: &TaskId, result: RunOutcome) {
        self.update(task_id, |record| {
            record.status = RunStatus::Completed;
            record.result = Some(result);
        });
    }

    /// Files why a run failed and marks it [`RunStatus::Failed`].
    pub(super) fn fail(&self, task_id: &TaskId, error: impl Into<String>) {
        self.update(task_id, |record| {
            record.status = RunStatus::Failed;
            record.error = Some(error.into());
        });
    }

    /// Applies `change` to a registered run, and does nothing for an unknown
    /// one.
    ///
    /// Every caller is a detached task reporting on its own run after the fact,
    /// where an unknown id means the registry is gone and there is nobody left
    /// to return an error to.
    fn update(&self, task_id: &TaskId, change: impl FnOnce(&mut RunRecord)) {
        if let Ok(mut guard) = self.lock()
            && let Some(record) = guard.get_mut(task_id.as_str())
        {
            change(record);
        }
    }

    /// Locks the registry, reporting a poisoned lock as a validation failure.
    fn lock(&self) -> Result<std::sync::MutexGuard<'_, BTreeMap<String, RunRecord>>> {
        self.inner
            .lock()
            .map_err(|_| TinyAgentsError::Validation("agent run registry lock is poisoned".into()))
    }
}

/// The steering handle for each live run.
///
/// Kept beside [`RunStore`] rather than inside it because the two have
/// different lifetimes: a record outlives its run so a caller can read what
/// happened, while a handle is deregistered the moment the run ends, and a
/// handle held past that point would accept a redirect nothing will ever read.
#[derive(Clone, Default)]
pub(super) struct SteeringRegistry {
    inner: Arc<Mutex<HashMap<String, SteeringHandle>>>,
}

impl std::fmt::Debug for SteeringRegistry {
    /// Written by hand because `SteeringHandle` is not `Debug`. Only the count
    /// is printed: a handle is a channel into a live run and has nothing
    /// readable in it, and the question a reader has of this type is how many
    /// runs are still steerable.
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let live = self.inner.lock().map(|guard| guard.len());
        formatter
            .debug_struct("SteeringRegistry")
            .field("live", &live.unwrap_or_default())
            .finish()
    }
}

impl SteeringRegistry {
    /// Creates an empty registry.
    pub(super) fn new() -> Self {
        Self::default()
    }

    /// Registers the handle for `task_id`, replacing any prior one.
    pub(super) fn register(&self, task_id: TaskId, handle: SteeringHandle) {
        if let Ok(mut guard) = self.inner.lock() {
            guard.insert(task_id.as_str().to_string(), handle);
        }
    }

    /// Drops the handle for `task_id`.
    pub(super) fn deregister(&self, task_id: &TaskId) {
        if let Ok(mut guard) = self.inner.lock() {
            guard.remove(task_id.as_str());
        }
    }

    /// Returns the handle for `task_id`, if the run is still steerable.
    pub(super) fn get(&self, task_id: &TaskId) -> Option<SteeringHandle> {
        self.inner.lock().ok()?.get(task_id.as_str()).cloned()
    }
}

#[cfg(test)]
#[path = "runs_test.rs"]
mod test;
