//! Graph-backed asynchronous subagent execution and control tools.

use std::collections::HashMap;
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::{Arc, RwLock};
use std::time::Duration;

use async_trait::async_trait;
use serde_json::{Value, json};
use tinyagents::harness::context::{RunConfig, RunContext};
use tinyagents::harness::events::{AgentEvent, EventSink};
use tinyagents::harness::ids::{RunId, TaskId};
use tinyagents::harness::observability::{
    AgentObservation, HarnessEventJournal, InMemoryEventJournal, JournalSink, LangfuseClient,
    LangfuseTraceConfig,
};
use tinyagents::harness::steering::{SteeringCommand, SteeringHandle};
use tokio::sync::Semaphore;

use crate::agent::budget::RunBudget;
use crate::agent::flow::{GraphBuilder, GraphError, GraphExecution, NodeContext, NodeResult};
use crate::agent::trace::RunTracer;
use crate::agent::{AgentHarness, Message, Result, Tool, ToolCall, ToolResult, ToolSchema};

use super::runs::{RunOutcome, RunRecord, RunStatus, RunStore, SteeringRegistry};
use super::vector::VectorStore;

static NEXT_RUN_ID: AtomicU64 = AtomicU64::new(1);

/// A completed research run hands its new sources to the scholar. The scholar
/// stores durable findings in Cognee, so no filing follow-up is needed.
const FOLLOW_UPS: [(&str, &[FollowUpStep]); 1] = [("research", &[DIGEST_AFTER_RESEARCH])];

/// One queued run in a trigger's follow-up sequence.
#[derive(Clone, Copy, Debug)]
struct FollowUpStep {
    agent: &'static str,
    brief: &'static str,
}

const DIGEST_AFTER_RESEARCH: FollowUpStep = FollowUpStep {
    agent: "scholar",
    brief: "The research agent just finished and the reference library has new material in it. \
            Read what is now in research/ against this investigation's goal, tasks, and current \
            beliefs. For each new source, record what it actually establishes and what that \
            implies here, under a thousand tokens. Store durable verified findings with \
            remember_memory, say which sources do not help and why, and flag anything that \
            contradicts recalled memory.",
};

/// Runs one `spawn_agents` call may launch.
///
/// Generous, because the point of the tool is to make width cheap: the
/// concurrency cap below is what actually bounds execution, and a caller that
/// has genuinely found sixteen independent pieces of work should not have to
/// issue four calls — each of which costs a full model turn — to start them.
/// The bound exists only so a malformed argument cannot start an unbounded
/// number of runs.
const MAX_BATCH_SPAWNS: usize = 16;

/// Everything one finished run needs to record itself.
struct Recording<'a> {
    memory: Option<&'a VectorStore>,
    agent: &'a str,
    run_id: &'a str,
    input: &'a str,
    store: &'a RunStore,
    task_id: &'a TaskId,
    /// Where a failure to record is said out loud.
    ///
    /// Session memory used to be written with the result discarded, so whether
    /// a run had recorded itself was unanswerable from the console or from
    /// `trace.jsonl` — the enqueue could time out, Cognee could refuse the
    /// document, and the run read exactly as it does when it worked. The write
    /// stays best effort; only its silence was the fault.
    tracer: Option<&'a Arc<RunTracer>>,
}

/// Writes one finished run to the session memory, saying so when it fails.
///
/// Best effort by design: the result is already in the task store, and a
/// memory server that is down must not turn a completed run into a failed one.
async fn record_session(into: &Recording<'_>, output: &str) {
    let Some(memory) = into.memory else {
        return;
    };
    if let Err(error) = memory
        .remember_session(into.agent, into.run_id, into.input, output)
        .await
        && let Some(tracer) = into.tracer
    {
        tracer.note(&format!(
            "session memory failed for {}/{}: {error}",
            into.agent, into.run_id
        ));
    }
}

/// Files a finished run's result into the task store and the session memory,
/// and reports whether it succeeded.
///
/// Lifted out of `spawn`, which is the one place in this module where a graph
/// is built, run, timed out, recorded, and followed up; the recording half
/// reads the same whichever way the run ended.
async fn record_outcome(
    outcome: std::result::Result<GraphExecution<RunState>, GraphError>,
    into: &Recording<'_>,
) -> bool {
    match outcome {
        Ok(execution) => {
            let response = execution.state.response.unwrap_or_default();
            record_session(into, &response).await;
            into.store.complete(into.task_id, RunOutcome::text(response));
            true
        }
        Err(error) => {
            let error = error.to_string();
            record_session(into, &format!("SESSION FAILED: {error}")).await;
            into.store.fail(into.task_id, error);
            false
        }
    }
}

/// Spawned runs allowed to execute at the same time.
///
/// A spawn is non-blocking and the model is encouraged to launch independent
/// work in parallel, so nothing previously bounded how many runs could be in
/// flight at once. Unbounded fan-out is not free: every run holds a full
/// transcript in memory and, more importantly, competes for the same provider
/// account, so a wide fan-out turns into upstream rate limiting, which the
/// retry ladder then absorbs as minutes of backoff across every run at once.
///
/// Fifty is deliberately well above any realistic fan-out rather than a tight
/// queue, and that headroom is load-bearing. A permit is held for a run's
/// whole life, including while it waits in `await_agent` for children it
/// spawned itself, so a parent occupies a slot while its children queue for
/// theirs. If the pool could be filled entirely by parents waiting on
/// children, the pool would deadlock. Keeping the cap far above the depth and
/// width the registry can actually produce is what makes that unreachable.
/// Lowering it towards the real fan-out would reintroduce exactly that risk.
const DEFAULT_MAX_CONCURRENT_AGENTS: usize = 50;

/// Reads the concurrent-run cap from the environment.
///
/// `MATH_AGENT_MAX_CONCURRENT_AGENTS` overrides the default. An unset, empty,
/// unparsable, or zero value keeps it, so a malformed override never silently
/// serialises the runtime or removes the bound.
fn max_concurrent_agents() -> usize {
    std::env::var("MATH_AGENT_MAX_CONCURRENT_AGENTS")
        .ok()
        .and_then(|value| value.trim().parse::<usize>().ok())
        .filter(|value| *value > 0)
        .unwrap_or(DEFAULT_MAX_CONCURRENT_AGENTS)
}

/// The role a possibly school-qualified name addresses.
///
/// `judge@rising-sea` is the judge. Every table keyed on a role name — the
/// budgets in [`super::definitions`], the reasoning-model split, the follow-up
/// sequences above — is keyed on the role rather than on the registration, so
/// each of them strips the suffix here rather than growing an entry per school.
/// One place, because a second answer to "which role is this" is a second
/// answer to what a role is allowed to spend.
pub(in crate::orchestrator) fn base_role(role: &str) -> &str {
    role.split_once('@').map_or(role, |(base, _)| base)
}

/// A follow-up sequence queued behind another run's completion.
struct FollowUp {
    manager: AsyncSubagentManager,
    steps: &'static [FollowUpStep],
}

impl FollowUp {
    /// Runs the sequence in order.
    ///
    /// Every failure is swallowed, and a failed step does not cancel the rest.
    /// A run that tidies the workspace must never be able to fail the
    /// investigation that triggered it, and an unregistered follow-up agent —
    /// a registry built without one — is simply nothing to do.
    async fn run(self) {
        for step in self.steps {
            if !self.manager.knows(step.agent) {
                continue;
            }
            let _ = self
                .manager
                .run_to_completion(step.agent, step.brief.to_string())
                .await;
        }
    }
}

#[async_trait]
pub(super) trait AgentExecutor: Send + Sync {
    async fn execute(
        &self,
        run_id: &str,
        input: String,
        steering: SteeringHandle,
        tracer: Option<Arc<RunTracer>>,
    ) -> Result<String>;
}

struct HarnessExecutor {
    harness: Arc<AgentHarness<()>>,
    system_prompt: String,
    langfuse: Option<Arc<LangfuseClient>>,
    max_turn_output_tokens: u32,
    /// Registry name of the specialist this executor runs, used as the
    /// Langfuse trace name so a trace says which role produced it.
    role: String,
    /// Identifies this process, so runs from different containers — or from
    /// the same container before and after a restart — never share a trace id.
    session: Arc<str>,
}

#[async_trait]
impl AgentExecutor for HarnessExecutor {
    async fn execute(
        &self,
        run_id: &str,
        input: String,
        steering: SteeringHandle,
        tracer: Option<Arc<RunTracer>>,
    ) -> Result<String> {
        let journal = Arc::new(InMemoryEventJournal::new());
        let durable: Arc<dyn HarnessEventJournal> = journal.clone();
        let journal_sink = Arc::new(JournalSink::new(durable, RunId::new(run_id)));
        let events = EventSink::with_stream_id(run_id);
        events.subscribe(journal_sink.clone());
        if let Some(tracer) = tracer {
            events.subscribe(tracer);
        }
        // Bound each turn's generation. Child runs do not inherit a cap that
        // was never set on the parent, and the specialists are exactly where
        // the long turns happen.
        let config =
            RunConfig::new(run_id).with_max_turn_output_tokens(self.max_turn_output_tokens);
        let context = RunContext::new(config, ())
            .with_steering(steering)
            .with_events(events);
        let result = self
            .harness
            .invoke_in_context(
                &(),
                context,
                vec![
                    Message::system(self.system_prompt.clone()),
                    Message::user(input),
                ],
            )
            .await;
        journal_sink.flush();
        self.export_to_langfuse(run_id, &journal).await;
        Ok(result?.text().unwrap_or_default())
    }
}

impl HarnessExecutor {
    /// Ships this specialist run's observations to Langfuse.
    ///
    /// Specialist runs are where most of the work happens, so a trace that
    /// covers only the orchestrator hides the part an operator needs when a run
    /// goes wrong. Delivery is best effort in both directions: a missing
    /// Langfuse configuration and a failed send are both ignored, because
    /// telemetry must never turn a completed derivation into a failed run.
    async fn export_to_langfuse(&self, run_id: &str, journal: &Arc<InMemoryEventJournal>) {
        let Some(langfuse) = self.langfuse.as_ref() else {
            return;
        };
        if let Ok(observations) = journal.read_from(run_id, 0).await {
            let observations = worth_exporting(observations);
            if !observations.is_empty() {
                let _ = langfuse
                    .send_observations(
                        trace_config(
                            &self.session,
                            &self.role,
                            run_id,
                            workspace_label().as_deref(),
                        ),
                        &observations,
                    )
                    .await;
            }
        }
    }
}

/// Drops the observations that say nothing a reader could act on.
///
/// Both middleware hooks fire on both sides of every model call and every tool
/// call, and each event carries only the middleware's name — no duration, no
/// outcome. On one measured run they were four fifths of the stream. Sending
/// them buries the model and tool observations an operator opens Langfuse to
/// read, and the sheer count is what makes a broad query on the legacy
/// observations endpoint fail outright. What they would have reported is
/// written to the run's own journal as a summary instead.
fn worth_exporting(observations: Vec<AgentObservation>) -> Vec<AgentObservation> {
    observations
        .into_iter()
        .filter(|record| {
            !matches!(
                record.event,
                AgentEvent::MiddlewareStarted { .. } | AgentEvent::MiddlewareCompleted { .. }
            )
        })
        .collect()
}

/// Names a run's Langfuse trace uniquely and describes what produced it.
///
/// The default configuration derives the trace id from the first observation's
/// run id, and run ids are allocated per process from one: every container's
/// first specialist run is `agent-run-1`. Two problems solved side by side, or
/// one problem restarted, therefore merged into a single trace whose
/// observations interleaved runs that shared nothing. Qualifying the id with
/// the session makes each run its own trace, and the session id groups the runs
/// that genuinely belong together.
fn trace_config(
    session: &str,
    role: &str,
    run_id: &str,
    workspace: Option<&str>,
) -> LangfuseTraceConfig {
    let workspace = workspace.map(str::to_string);
    let mut tags = vec![format!("agent:{role}")];
    if let Some(label) = workspace.as_ref() {
        tags.push(format!("problem:{label}"));
    }
    LangfuseTraceConfig {
        trace_id: Some(format!("{session}-{run_id}")),
        // Named for the role so the trace list reads as a list of agents rather
        // than of opaque ids, and one role's turns can be picked out by name.
        name: Some(format!("{role} · {run_id}")),
        // Langfuse groups and filters by user before anything else, and the
        // question asked of this data is almost always "what happened on 591",
        // so the problem occupies that dimension. Nothing here is a person.
        user_id: workspace.clone(),
        // One attempt at one problem: every agent the container ran, from the
        // orchestrator down, lands in the same session. A restart deliberately
        // opens a new one, because its runs share a workspace but not a state.
        session_id: Some(match workspace.as_ref() {
            Some(label) => format!("{label}@{session}"),
            None => session.to_string(),
        }),
        tags,
        metadata: json!({
            "agent": role,
            "run_id": run_id,
            "workspace": workspace,
        }),
        ..LangfuseTraceConfig::default()
    }
}

/// The workspace this container was started for, as the host wrapper named it.
///
/// Every container mounts its workspace at the same path, so the label
/// forwarded from `scripts/run-agent` is the only thing that distinguishes one
/// problem's traces from another's.
fn workspace_label() -> Option<String> {
    let label = std::env::var("MATH_AGENT_WORKSPACE_LABEL").ok()?;
    let trimmed = label.trim();
    if trimmed.is_empty() {
        return None;
    }
    Some(trimmed.to_string())
}

/// Builds an identifier for this process's runs.
///
/// Uniqueness across processes is what the trace id needs; the wall clock and
/// the process id together give that without a dependency, and a clock that
/// failed to read still yields a usable id from the process id alone.
fn session_id() -> Arc<str> {
    let nanos = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|since| since.as_nanos())
        .unwrap_or_default();
    Arc::from(format!("s{nanos:x}-{}", std::process::id()).as_str())
}

#[derive(Clone)]
pub(crate) struct AsyncSubagentManager {
    agents: Arc<RwLock<HashMap<String, Arc<dyn AgentExecutor>>>>,
    store: RunStore,
    steering: SteeringRegistry,
    budget: RunBudget,
    tracer: Option<Arc<RunTracer>>,
    langfuse: Option<Arc<LangfuseClient>>,
    /// Bounds how many spawned runs execute at once. See [`max_concurrent_agents`].
    slots: Arc<Semaphore>,
    /// Distinguishes this process's Langfuse traces from every other process's.
    session: Arc<str>,
    /// The school this handle registers into and delegates within.
    ///
    /// `None` is one school running, which is every run that existed before
    /// schools did: names are registered and resolved exactly as written. When
    /// it is set, [`Self::qualified`] registers `goals` as `goals@<slug>` and
    /// [`Self::resolve`] sends a bare `goals` to that same registration, which
    /// is what keeps a delegating agent inside its own school without a single
    /// bench, prompt, or loop step learning that schools exist. See
    /// [`Self::for_school`].
    school: Option<Arc<str>>,
    /// Best-effort sink for completed project/run-scoped agent sessions.
    memory: Option<VectorStore>,
}

impl std::fmt::Debug for AsyncSubagentManager {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let agents = self
            .agents
            .read()
            .map(|agents| agents.keys().cloned().collect::<Vec<_>>())
            .unwrap_or_default();
        formatter
            .debug_struct("AsyncSubagentManager")
            .field("agents", &agents)
            .finish_non_exhaustive()
    }
}

include!("async_subagents_manager.rs");
include!("async_subagents_tool.rs");
include!("async_subagents_arguments.rs");

#[cfg(test)]
#[path = "async_subagents_test.rs"]
mod test;
