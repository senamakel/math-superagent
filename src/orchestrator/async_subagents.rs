//! Graph-backed asynchronous subagent execution and control tools.

use std::collections::HashMap;
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::{Arc, RwLock};
use std::time::Duration;

use async_trait::async_trait;
use serde_json::{Value, json};
use tinyagents::graph::{
    GraphBuilder, InMemoryTaskStore, NodeContext, NodeResult, OrchestrationTaskKind,
    OrchestrationTaskResult, OrchestrationTaskSpec, SteeringRegistry, TaskStore,
};
use tinyagents::harness::context::{RunConfig, RunContext};
use tinyagents::harness::events::EventSink;
use tinyagents::harness::ids::{RunId, TaskId};
use tinyagents::harness::observability::{
    HarnessEventJournal, InMemoryEventJournal, JournalSink, LangfuseClient, LangfuseTraceConfig,
};
use tinyagents::harness::steering::{SteeringCommand, SteeringHandle};
use tokio::sync::Semaphore;

use crate::agent::budget::RunBudget;
use crate::agent::trace::RunTracer;
use crate::agent::{AgentHarness, Message, Result, Tool, ToolCall, ToolResult, ToolSchema};

static NEXT_RUN_ID: AtomicU64 = AtomicU64::new(1);

/// Runs that automatically trigger a follow-up run when they succeed.
///
/// The tool-builder is the role that creates files, and the moment it finishes
/// is when the workspace is least tidy and most legible: the files are new,
/// their purpose is settled, and nothing else has happened since. Leaving the
/// tidying to whoever happens to run next means it competes with mathematics
/// for attention and reliably loses, so the index drifts out of step with the
/// directory exactly when it is most needed.
///
/// The research agent is the other role that leaves the workspace changed, and
/// it leaves it changed in the way that decays fastest. A download is raw
/// material: until someone reads it, it has cost the run context and taught it
/// nothing, and the moment it lands is the only moment anybody knows why it was
/// fetched. So research hands off to the scholar to say what each new source
/// actually establishes, and only then to the organizer, which files what the
/// scholar has just written. That order is the point — an organizer running
/// first would index excerpts nobody had read yet.
///
/// The follow-up is fire-and-forget. The caller's `await_agent` returns as soon
/// as the triggering run itself is done, because housekeeping must not sit on
/// the critical path of an investigation waiting for its result.
const FOLLOW_UPS: [(&str, &[FollowUpStep]); 2] = [
    ("tool_builder", &[ORGANIZE_AFTER_TOOLS]),
    ("research", &[DIGEST_AFTER_RESEARCH, ORGANIZE_AFTER_RESEARCH]),
];

/// One queued run in a trigger's follow-up sequence.
#[derive(Clone, Copy, Debug)]
struct FollowUpStep {
    agent: &'static str,
    brief: &'static str,
}

const ORGANIZE_AFTER_TOOLS: FollowUpStep = FollowUpStep {
    agent: "organizer",
    brief: "The tool-builder just finished. Bring the workspace back into order: refresh each \
            folder's INDEX.md so it matches what is on disk, describe every file that is now \
            undescribed, and correct any row whose description no longer matches its file. Keep \
            toolkits/INDEX.md in step with the files beside it. Do not change what any file says.",
};

const DIGEST_AFTER_RESEARCH: FollowUpStep = FollowUpStep {
    agent: "scholar",
    brief: "The research agent just finished and the reference library has new material in it. \
            Read what is now in research/ against this investigation's goal, tasks, and current \
            beliefs. For each new source, replace its placeholder excerpt with what it actually \
            establishes and what that implies here, under a thousand tokens. Say which sources do \
            not help and why, and flag anything that contradicts what memory.md asserts.",
};

const ORGANIZE_AFTER_RESEARCH: FollowUpStep = FollowUpStep {
    agent: "organizer",
    brief: "Research and reading have just finished. File what arrived: give each new source a \
            name that says what it is about, refresh research/INDEX.md so it is the way in and \
            reflects what the scholar wrote, and describe every file still undescribed. Do not \
            change what any file says.",
};

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

/// A housekeeping run queued behind another run's completion.
struct FollowUp {
    manager: AsyncSubagentManager,
    agent: String,
}

impl FollowUp {
    /// Runs the follow-up, one at a time across the whole runtime.
    ///
    /// Serialised deliberately: two organizers refreshing the same `INDEX.md`
    /// concurrently would each write the list it read, and the later write
    /// would silently drop the other's descriptions. Housekeeping is not on
    /// anyone's critical path, so waiting for the lock costs nothing.
    ///
    /// Every failure is swallowed. A run that tidies the workspace must never
    /// be able to fail the investigation that triggered it, and an unregistered
    /// follow-up agent — a registry built without one — is simply nothing to
    /// do.
    async fn run(self) {
        if !self.manager.knows(&self.agent) {
            return;
        }
        let _guard = self.manager.housekeeping.lock().await;
        let _ = self
            .manager
            .run_to_completion(&self.agent, FOLLOW_UP_BRIEF.to_string())
            .await;
    }
}

#[async_trait]
trait AgentExecutor: Send + Sync {
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
        if let Ok(observations) = journal.read_from(run_id, 0).await
            && !observations.is_empty()
        {
            let _ = langfuse
                .send_observations(LangfuseTraceConfig::default(), &observations)
                .await;
        }
    }
}

#[derive(Clone)]
pub(crate) struct AsyncSubagentManager {
    agents: Arc<RwLock<HashMap<String, Arc<dyn AgentExecutor>>>>,
    store: Arc<InMemoryTaskStore>,
    steering: SteeringRegistry,
    budget: RunBudget,
    tracer: Option<Arc<RunTracer>>,
    langfuse: Option<Arc<LangfuseClient>>,
    /// Bounds how many spawned runs execute at once. See [`max_concurrent_agents`].
    slots: Arc<Semaphore>,
    /// Serialises follow-up runs so two never rewrite one index at once.
    housekeeping: Arc<tokio::sync::Mutex<()>>,
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

impl AsyncSubagentManager {
    pub(crate) fn new(budget: RunBudget, tracer: Option<Arc<RunTracer>>) -> Self {
        Self::with_concurrency(budget, tracer, max_concurrent_agents())
    }

    /// Builds a manager with an explicit concurrent-run cap.
    ///
    /// Separate from [`Self::new`] so the cap can be exercised without setting
    /// a process-wide environment variable from a test.
    fn with_concurrency(
        budget: RunBudget,
        tracer: Option<Arc<RunTracer>>,
        concurrency: usize,
    ) -> Self {
        Self {
            agents: Arc::default(),
            store: Arc::new(InMemoryTaskStore::new()),
            steering: SteeringRegistry::new(),
            budget,
            tracer,
            langfuse: LangfuseClient::from_env().ok().map(Arc::new),
            slots: Arc::new(Semaphore::new(concurrency)),
            housekeeping: Arc::new(tokio::sync::Mutex::new(())),
        }
    }

    /// Longest an `await_agent` call may block, in seconds.
    ///
    /// A caller must be able to wait out a child that is using its full run
    /// budget, otherwise the orchestrator is structurally unable to collect
    /// the result of the deepest work it delegated.
    fn max_await_seconds(&self) -> u64 {
        self.budget.run_timeout.as_secs().max(60)
    }

    pub(crate) fn register(
        &self,
        name: impl Into<String>,
        harness: Arc<AgentHarness<()>>,
        system_prompt: impl Into<String>,
    ) -> Result<()> {
        self.register_executor(
            name,
            Arc::new(HarnessExecutor {
                harness,
                system_prompt: system_prompt.into(),
                langfuse: self.langfuse.clone(),
                max_turn_output_tokens: self.budget.max_turn_output_tokens,
            }),
        )
    }

    fn register_executor(
        &self,
        name: impl Into<String>,
        executor: Arc<dyn AgentExecutor>,
    ) -> Result<()> {
        let name = name.into();
        let mut agents = self.agents.write().map_err(|_| {
            tinyagents::TinyAgentsError::Tool("async subagent registry lock is poisoned".into())
        })?;
        if agents.insert(name.clone(), executor).is_some() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "async subagent `{name}` is already registered"
            )));
        }
        Ok(())
    }

    /// Reports whether an agent is registered under this name.
    fn knows(&self, agent: &str) -> bool {
        self.agents
            .read()
            .is_ok_and(|agents| agents.contains_key(agent))
    }

    fn spawn(&self, agent_name: &str, input: String) -> Result<TaskId> {
        let executor = self
            .agents
            .read()
            .map_err(|_| {
                tinyagents::TinyAgentsError::Tool("async subagent registry lock is poisoned".into())
            })?
            .get(agent_name)
            .cloned()
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation(format!(
                    "unknown async subagent `{agent_name}`"
                ))
            })?;
        let sequence = NEXT_RUN_ID.fetch_add(1, Ordering::Relaxed);
        let task_id = TaskId::new(format!("agent-run-{sequence}"));
        let spec = OrchestrationTaskSpec::new(
            task_id.clone(),
            OrchestrationTaskKind::SubAgent {
                agent: agent_name.to_string(),
            },
        )
        .with_timeout_ms(self.budget.run_timeout_ms())
        .with_input(json!({ "prompt": input }));
        self.store.insert(spec)?;

        let store = self.store.clone();
        let steering_registry = self.steering.clone();
        let spawned_task_id = task_id.clone();
        let run_id = task_id.as_str().to_string();
        let steering = SteeringHandle::allow_all();
        steering_registry.register(task_id.clone(), steering.clone());
        let run_timeout = self.budget.run_timeout;
        let tracer = self
            .tracer
            .as_ref()
            .map(|tracer| tracer.child(format!("{agent_name}/{run_id}")));
        if let Some(tracer) = tracer.as_ref() {
            tracer.note(&format!("spawned: {}", preview_input(&input)));
        }
        let slots = self.slots.clone();
        let follow_up = FOLLOW_UPS
            .iter()
            .find(|(after, _)| *after == agent_name)
            .map(|(_, then)| FollowUp {
                manager: self.clone(),
                agent: (*then).to_string(),
            });
        tokio::spawn(async move {
            // Queue for a slot before doing anything else. Acquiring here
            // rather than in `spawn` is what keeps a spawn cheap and
            // non-blocking: the caller gets its run id immediately and the
            // queue drains behind it. The run deadline starts after the wait,
            // so a queued run is not charged for time it spent waiting.
            let _permit = slots.acquire().await;
            let _ = store.mark_running(&spawned_task_id);
            let graph = GraphBuilder::<RunState, RunState>::overwrite()
                .add_node(
                    "subagent",
                    move |mut state: RunState, _context: NodeContext| {
                        let executor = executor.clone();
                        let steering = steering.clone();
                        let tracer = tracer.clone();
                        async move {
                            let response = executor
                                .execute(&state.run_id, state.input.clone(), steering, tracer)
                                .await?;
                            state.response = Some(response);
                            Ok(NodeResult::Update(state))
                        }
                    },
                )
                .set_entry("subagent")
                .set_finish("subagent")
                .compile()
                .map(|graph| graph.with_run_deadline(run_timeout));

            let outcome = match graph {
                Ok(graph) => tokio::time::timeout(
                    run_timeout,
                    graph.run(RunState {
                        run_id,
                        input,
                        response: None,
                    }),
                )
                .await
                .map_err(|_| tinyagents::TinyAgentsError::Timeout("subagent run timed out".into()))
                .and_then(|result| result),
                Err(error) => Err(error),
            };
            let succeeded = outcome.is_ok();
            match outcome {
                Ok(execution) => {
                    let response = execution.state.response.unwrap_or_default();
                    let _ =
                        store.complete(&spawned_task_id, OrchestrationTaskResult::text(response));
                }
                Err(error) => {
                    let _ = store.fail(&spawned_task_id, error.to_string());
                }
            }
            steering_registry.deregister(&spawned_task_id);
            if succeeded && let Some(follow_up) = follow_up {
                // Spawned separately so this run's slot is released first.
                // Chaining inline would make every in-flight tool-builder hold
                // two slots, one of them doing nothing but waiting.
                tokio::spawn(async move { follow_up.run().await });
            }
        });
        Ok(task_id)
    }

    /// Spawns `agent` and waits for its final text.
    ///
    /// The graph-backed solution loop needs a plain call-and-wait, unlike the
    /// model-visible tools where spawning and awaiting are deliberately
    /// separate so a model can run work in parallel.
    ///
    /// # Errors
    ///
    /// Returns an error when the agent is unknown or the run failed or timed
    /// out without producing a response.
    pub(crate) async fn run_to_completion(&self, agent: &str, input: String) -> Result<String> {
        let task_id = self.spawn(agent, input)?;
        let record = self
            .await_record(task_id.as_str(), self.max_await_seconds())
            .await?;
        if let Some(error) = record.error {
            return Err(tinyagents::TinyAgentsError::Tool(format!(
                "agent `{agent}` failed: {error}"
            )));
        }
        record.result.and_then(|result| result.text).ok_or_else(|| {
            tinyagents::TinyAgentsError::Tool(format!(
                "agent `{agent}` produced no response before its deadline"
            ))
        })
    }

    fn record(&self, task_id: &str) -> Result<tinyagents::graph::OrchestrationTaskRecord> {
        let task_id = TaskId::new(task_id);
        self.store.get(&task_id).ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("unknown agent run `{task_id}`"))
        })
    }

    fn steer(&self, task_id: &str, instruction: String) -> Result<()> {
        let task_id = TaskId::new(task_id);
        let record = self.store.get(&task_id).ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("unknown agent run `{task_id}`"))
        })?;
        if !record.status.is_live() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "agent run `{task_id}` is already terminal"
            )));
        }
        let handle = self.steering.get(&task_id).ok_or_else(|| {
            tinyagents::TinyAgentsError::Tool(format!(
                "agent run `{task_id}` has no steering handle"
            ))
        })?;
        handle.send(SteeringCommand::Redirect { instruction });
        Ok(())
    }

    async fn await_record(
        &self,
        task_id: &str,
        wait_seconds: u64,
    ) -> Result<tinyagents::graph::OrchestrationTaskRecord> {
        let deadline = tokio::time::Instant::now()
            + Duration::from_secs(wait_seconds.min(self.max_await_seconds()));
        loop {
            let record = self.record(task_id)?;
            if record.status.is_terminal() || tokio::time::Instant::now() >= deadline {
                return Ok(record);
            }
            tokio::time::sleep(Duration::from_millis(200)).await;
        }
    }

    pub(crate) fn tools(
        &self,
        allowed_agents: impl IntoIterator<Item = &'static str>,
    ) -> Vec<Arc<dyn Tool<()>>> {
        let allowed = Arc::new(
            allowed_agents
                .into_iter()
                .map(str::to_string)
                .collect::<Vec<_>>(),
        );
        vec![
            Arc::new(AsyncSubagentTool::new(
                AsyncToolKind::Spawn,
                self.clone(),
                allowed.clone(),
            )),
            Arc::new(AsyncSubagentTool::new(
                AsyncToolKind::Peek,
                self.clone(),
                allowed.clone(),
            )),
            Arc::new(AsyncSubagentTool::new(
                AsyncToolKind::Steer,
                self.clone(),
                allowed.clone(),
            )),
            Arc::new(AsyncSubagentTool::new(
                AsyncToolKind::Await,
                self.clone(),
                allowed,
            )),
        ]
    }
}

#[derive(Clone, Debug)]
struct RunState {
    run_id: String,
    input: String,
    response: Option<String>,
}

#[derive(Clone, Copy, Debug)]
enum AsyncToolKind {
    Spawn,
    Peek,
    Steer,
    Await,
}

#[derive(Debug)]
struct AsyncSubagentTool {
    kind: AsyncToolKind,
    manager: AsyncSubagentManager,
    allowed_agents: Arc<Vec<String>>,
}

impl AsyncSubagentTool {
    fn new(
        kind: AsyncToolKind,
        manager: AsyncSubagentManager,
        allowed_agents: Arc<Vec<String>>,
    ) -> Self {
        Self {
            kind,
            manager,
            allowed_agents,
        }
    }
}

#[async_trait]
impl Tool<()> for AsyncSubagentTool {
    fn name(&self) -> &'static str {
        match self.kind {
            AsyncToolKind::Spawn => "spawn_agent",
            AsyncToolKind::Peek => "peek_agent",
            AsyncToolKind::Steer => "steer_agent",
            AsyncToolKind::Await => "await_agent",
        }
    }

    fn description(&self) -> &'static str {
        match self.kind {
            AsyncToolKind::Spawn => {
                "Starts a subagent asynchronously and immediately returns its run id. Keep `input` \
                 to a short brief — say what the agent must do and what to report back, in a few \
                 sentences. Do not restate the problem, the derivation so far, or the contents of \
                 any file: the agent is given the workspace and reads it itself. A brief long \
                 enough to exhaust the turn's output budget is cut off mid-argument and the call \
                 never happens."
            }
            AsyncToolKind::Peek => {
                "Returns the current status and any completed response for a subagent run."
            }
            AsyncToolKind::Steer => "Redirects a live subagent with an additional instruction.",
            AsyncToolKind::Await => "Waits for a subagent run and returns its status and response.",
        }
    }

    fn schema(&self) -> ToolSchema {
        let parameters = match self.kind {
            AsyncToolKind::Spawn => json!({
                "type": "object",
                "properties": {
                    "agent": { "type": "string", "enum": self.allowed_agents.as_ref() },
                    "input": {
                        "type": "string",
                        "description": "A short brief: the task and what to report back. A few \
                                        sentences, not a transcript — the agent reads the \
                                        workspace itself.",
                        "maxLength": 2000
                    }
                },
                "required": ["agent", "input"],
                "additionalProperties": false
            }),
            AsyncToolKind::Peek => run_id_schema(None),
            AsyncToolKind::Steer => json!({
                "type": "object",
                "properties": {
                    "run_id": { "type": "string" },
                    "instruction": { "type": "string" }
                },
                "required": ["run_id", "instruction"],
                "additionalProperties": false
            }),
            AsyncToolKind::Await => run_id_schema(Some(self.manager.max_await_seconds())),
        };
        ToolSchema::new(self.name(), self.description(), parameters)
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let value = match self.kind {
            AsyncToolKind::Spawn => {
                let agent = required_string(&call.arguments, "agent")?;
                if !self.allowed_agents.contains(&agent) {
                    return Err(tinyagents::TinyAgentsError::Validation(format!(
                        "subagent `{agent}` is not allowed from this caller"
                    )));
                }
                let input = required_string(&call.arguments, "input")?;
                let run_id = self.manager.spawn(&agent, input)?;
                json!({ "run_id": run_id, "status": "pending" })
            }
            AsyncToolKind::Peek => serde_json::to_value(
                self.manager
                    .record(&required_string(&call.arguments, "run_id")?)?,
            )?,
            AsyncToolKind::Steer => {
                let run_id = required_string(&call.arguments, "run_id")?;
                self.manager
                    .steer(&run_id, required_string(&call.arguments, "instruction")?)?;
                json!({ "run_id": run_id, "accepted": true })
            }
            AsyncToolKind::Await => {
                let wait_seconds = call
                    .arguments
                    .get("wait_seconds")
                    .and_then(Value::as_u64)
                    .unwrap_or_else(|| self.manager.max_await_seconds());
                serde_json::to_value(
                    self.manager
                        .await_record(&required_string(&call.arguments, "run_id")?, wait_seconds)
                        .await?,
                )?
            }
        };
        Ok(ToolResult::text(
            call.id,
            self.name(),
            serde_json::to_string(&value)?,
        ))
    }
}

fn run_id_schema(max_wait_seconds: Option<u64>) -> Value {
    match max_wait_seconds {
        Some(maximum) => json!({
            "type": "object",
            "properties": {
                "run_id": { "type": "string" },
                "wait_seconds": { "type": "integer", "minimum": 0, "maximum": maximum }
            },
            "required": ["run_id"],
            "additionalProperties": false
        }),
        None => json!({
            "type": "object",
            "properties": { "run_id": { "type": "string" } },
            "required": ["run_id"],
            "additionalProperties": false
        }),
    }
}

/// Shortens a spawn prompt for the operator-facing console line.
fn preview_input(input: &str) -> String {
    const PREVIEW_CHARS: usize = 160;
    let collapsed = input.split_whitespace().collect::<Vec<_>>().join(" ");
    if collapsed.chars().count() <= PREVIEW_CHARS {
        return collapsed;
    }
    let kept = collapsed.chars().take(PREVIEW_CHARS).collect::<String>();
    format!("{kept}...")
}

fn required_string(arguments: &Value, name: &str) -> Result<String> {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .map(ToOwned::to_owned)
        .ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("{name} must be a non-empty string"))
        })
}

#[cfg(test)]
mod test;
