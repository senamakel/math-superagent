//! This crate's agents, offered to `TinyFlows` as background work.
//!
//! [`AsyncSubagentManager`] already does what a `spawn` node needs: it starts a
//! child agent, returns a run id immediately, and files the result under that id
//! when the run ends. [`TaskRunner`] is the shape `TinyFlows` asks for that in,
//! so this is an adapter and not a second implementation — a ticket *is* a run
//! id, and polling one reads the registry in [`super::runs`].
//!
//! # What this buys
//!
//! A workflow graph can start one of this crate's specialists and carry on. Two
//! spellings, and the difference between them is the whole point:
//!
//! ```text
//!   spawn ──> gate     collect it later; the gate's release policy decides
//!                      whether to wait for all of them, a quorum, or whatever
//!                      arrived before a deadline
//!
//!   spawn ──> void     file and forget: nothing collects it, and the branch
//!                      says so out loud
//! ```
//!
//! `void` is what makes the second one legible. A branch could always dead-end
//! by having no outgoing edge, but an unwired port reads exactly like a
//! forgotten one — `void` is the author saying "this is a side effect and
//! nothing waits on it". It adds no concurrency of its own; the overlap comes
//! from `spawn`, which is to say from here.
//!
//! # What it does not change
//!
//! The solution loop is built on the state-graph runtime, which has no node
//! kinds and therefore no `spawn` and no `void` — see [`crate::agent::flow`].
//! Nothing in this module is reached by a run today. It is the half of the
//! bridge this crate owns, and it is the half that has to exist first: a
//! workflow that spawns a specialist is unwritable until the host can start
//! one.

use async_trait::async_trait;
use serde_json::Value;
use tinyflows::caps::{AgentRunner, TaskRunner, TaskSpec, TaskState};
use tinyflows::error::{EngineError, Result as EngineResult};

use super::async_subagents::AsyncSubagentManager;
use super::runs::RunStatus;

/// Starts this crate's specialists on behalf of a `spawn` node.
#[derive(Clone, Debug)]
pub struct SubagentTaskRunner {
    manager: AsyncSubagentManager,
}

impl SubagentTaskRunner {
    /// Wraps a manager as a task runner.
    pub(super) fn new(manager: AsyncSubagentManager) -> Self {
        Self { manager }
    }
}

/// Reads the agent name and prompt out of a task spec.
///
/// Only [`TaskSpec::Tool`] is accepted, and the mapping is deliberate rather
/// than incidental: a `spawn` node names a slug and passes arguments, which is
/// exactly "which specialist, and what to ask it". The other two shapes are
/// refused rather than approximated — a `Workflow` spec wants a child graph run,
/// which is the engine's job and not an agent's, and an `Http` spec wants a
/// request this crate would have to invent an agent for. Guessing either would
/// start the wrong work and report success.
fn agent_and_prompt(spec: &TaskSpec) -> EngineResult<(&str, String)> {
    let TaskSpec::Tool { slug, args } = spec else {
        return Err(EngineError::Capability(
            "this host starts agents, so a spawn must be a tool spec naming one".into(),
        ));
    };
    let prompt = args
        .get("prompt")
        .and_then(Value::as_str)
        .ok_or_else(|| EngineError::Capability(format!("spawn of `{slug}` has no `prompt`")))?;
    if prompt.trim().is_empty() {
        return Err(EngineError::Capability(format!(
            "spawn of `{slug}` has an empty `prompt`"
        )));
    }
    Ok((slug.as_str(), prompt.to_string()))
}

#[async_trait]
impl TaskRunner for SubagentTaskRunner {
    /// Starts `spec` and returns the run id as its ticket.
    ///
    /// # Errors
    ///
    /// Returns a capability error when the spec is not a tool spec, carries no
    /// prompt, or names an agent this registry does not hold. An unknown agent
    /// fails here rather than settling as a failed ticket, because it is a fault
    /// in the workflow rather than in the work: no retry or gate policy will
    /// make a name that was never registered start running.
    async fn start(&self, spec: TaskSpec) -> EngineResult<String> {
        let (agent, prompt) = agent_and_prompt(&spec)?;
        self.manager
            .spawn_detached(agent, prompt)
            .map(|task_id| task_id.as_str().to_string())
            .map_err(|error| EngineError::Capability(error.to_string()))
    }

    /// Reports where `ticket` has got to.
    ///
    /// A completed run with no text settles as [`TaskState::Done`] carrying
    /// `null` rather than as a failure: the run did finish, and an agent that
    /// returns nothing is a thin result, not a broken one. The distinction
    /// matters to a gate, which routes the two differently.
    ///
    /// # Errors
    ///
    /// Returns a capability error only for a ticket this runner never issued,
    /// which is what the trait reserves an error for.
    async fn poll(&self, ticket: &str) -> EngineResult<TaskState> {
        let record = self
            .manager
            .task_record(ticket)
            .ok_or_else(|| EngineError::Capability(format!("unknown ticket `{ticket}`")))?;
        Ok(match record.status {
            RunStatus::Pending => TaskState::Pending,
            RunStatus::Running => TaskState::Running,
            RunStatus::Completed => TaskState::Done(
                record
                    .result
                    .and_then(|result| result.text)
                    .map_or(Value::Null, Value::String),
            ),
            RunStatus::Failed => TaskState::Failed(
                record
                    .error
                    .unwrap_or_else(|| "the run failed without saying why".to_string()),
            ),
        })
    }

    /// Asks `ticket` to stop.
    ///
    /// Cooperative, because that is all this runtime has: a live run is sent a
    /// stop instruction through its steering handle and decides when to act on
    /// it, and a run that has already settled is left alone. The trait calls
    /// cancellation best effort, and this is what best effort means here — the
    /// call returns once the instruction is queued, not once the run has ended.
    ///
    /// # Errors
    ///
    /// Returns a capability error for a ticket this runner never issued.
    async fn cancel(&self, ticket: &str) -> EngineResult<()> {
        let record = self
            .manager
            .task_record(ticket)
            .ok_or_else(|| EngineError::Capability(format!("unknown ticket `{ticket}`")))?;
        if record.status.is_terminal() {
            return Ok(());
        }
        self.manager
            .stop_run(ticket)
            .map_err(|error| EngineError::Capability(error.to_string()))
    }
}

/// Runs this crate's registered roles for an `agent` node.
///
/// An `agent` node whose config carries an `agent_ref` routes here instead of
/// taking a bare completion, so the role runs with its own prompt, its own
/// tools, and its own budget — the whole point of a role existing. Without
/// this, an `agent` node would reach [`LlmProvider`](tinyflows::caps::LlmProvider)
/// and get a single tool-less turn, which is a different thing wearing the same
/// name.
///
/// Shares the manager with [`SubagentTaskRunner`], so a role reached from an
/// `agent` node and the same role reached from a `spawn` node are one registry
/// and one concurrency pool rather than two.
#[derive(Clone, Debug)]
pub struct SubagentAgentRunner {
    manager: AsyncSubagentManager,
}

impl SubagentAgentRunner {
    /// Wraps a manager as an agent runner.
    pub(super) fn new(manager: AsyncSubagentManager) -> Self {
        Self { manager }
    }
}

/// Reads the instruction out of an `agent` node's resolved config.
///
/// Three spellings are accepted because three are in use: `prompt` is what an
/// `agent` node writes, `input` is what the assembled request carries, and a
/// bare string config is what the shortest possible node looks like. Accepting
/// all three costs nothing and turns a silent empty turn into a run that did
/// what the author meant.
fn instruction_from(request: &Value) -> EngineResult<String> {
    let text = request
        .as_str()
        .map(str::to_string)
        .or_else(|| {
            ["prompt", "input", "text"]
                .iter()
                .find_map(|key| request.get(key).and_then(Value::as_str))
                .map(str::to_string)
        })
        .ok_or_else(|| {
            EngineError::Capability(
                "an agent node needs a `prompt`, an `input`, or a bare string".into(),
            )
        })?;
    if text.trim().is_empty() {
        return Err(EngineError::Capability(
            "an agent node was given an empty prompt".into(),
        ));
    }
    Ok(text)
}

#[async_trait]
impl AgentRunner for SubagentAgentRunner {
    /// Runs `agent_ref` to completion and returns what it said.
    ///
    /// Returns `{ text }`, matching what [`LlmProvider`](tinyflows::caps::LlmProvider)
    /// returns, so a downstream node binds `=item.text` without knowing which
    /// path produced the turn.
    ///
    /// This waits, unlike [`SubagentTaskRunner`], and the difference is the
    /// node kind rather than an inconsistency: an `agent` node is a step in a
    /// sequence and its successor needs the answer, while a `spawn` node exists
    /// precisely so the branch does not wait. A workflow that wants an agent to
    /// run beside the graph uses `spawn`.
    ///
    /// # Errors
    ///
    /// Returns a capability error when the config carries no instruction, when
    /// `agent_ref` is not registered, or when the run failed or produced
    /// nothing before its deadline.
    async fn run_agent(
        &self,
        agent_ref: &str,
        request: Value,
        _conn: Option<&str>,
    ) -> EngineResult<Value> {
        let instruction = instruction_from(&request)?;
        let response = self
            .manager
            .run_to_completion(agent_ref, instruction)
            .await
            .map_err(|error| EngineError::Capability(error.to_string()))?;
        Ok(serde_json::json!({ "text": response }))
    }
}

/// The tool-spec shape a `spawn` node uses to start `agent` with `prompt`.
///
/// Here rather than at the call sites so a workflow and this runner cannot
/// disagree about the argument name.
#[cfg(test)]
fn spawn_spec(agent: &str, prompt: &str) -> TaskSpec {
    TaskSpec::Tool {
        slug: agent.to_string(),
        args: serde_json::json!({ "prompt": prompt }),
    }
}

#[cfg(test)]
#[path = "runner_test.rs"]
mod test;
