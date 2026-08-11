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
use tinyagents::harness::ids::TaskId;
use tinyagents::harness::steering::{SteeringCommand, SteeringHandle};

use crate::agent::{AgentHarness, Message, Result, Tool, ToolCall, ToolResult, ToolSchema};

const RUN_TIMEOUT: Duration = Duration::from_mins(10);
const MAX_AWAIT_SECONDS: u64 = 599;
static NEXT_RUN_ID: AtomicU64 = AtomicU64::new(1);

#[async_trait]
trait AgentExecutor: Send + Sync {
    async fn execute(
        &self,
        run_id: &str,
        input: String,
        steering: SteeringHandle,
    ) -> Result<String>;
}

struct HarnessExecutor {
    harness: Arc<AgentHarness<()>>,
    system_prompt: String,
}

#[async_trait]
impl AgentExecutor for HarnessExecutor {
    async fn execute(
        &self,
        run_id: &str,
        input: String,
        steering: SteeringHandle,
    ) -> Result<String> {
        let context = RunContext::new(RunConfig::new(run_id), ()).with_steering(steering);
        let run = self
            .harness
            .invoke_in_context(
                &(),
                context,
                vec![
                    Message::system(self.system_prompt.clone()),
                    Message::user(input),
                ],
            )
            .await?;
        Ok(run.text().unwrap_or_default())
    }
}

#[derive(Clone)]
pub(super) struct AsyncSubagentManager {
    agents: Arc<RwLock<HashMap<String, Arc<dyn AgentExecutor>>>>,
    store: Arc<InMemoryTaskStore>,
    steering: SteeringRegistry,
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
    pub(super) fn new() -> Self {
        Self {
            agents: Arc::default(),
            store: Arc::new(InMemoryTaskStore::new()),
            steering: SteeringRegistry::new(),
        }
    }

    pub(super) fn register(
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
        .with_timeout_ms(RUN_TIMEOUT.as_millis() as u64)
        .with_input(json!({ "prompt": input }));
        self.store.insert(spec)?;

        let store = self.store.clone();
        let steering_registry = self.steering.clone();
        let spawned_task_id = task_id.clone();
        let run_id = task_id.as_str().to_string();
        let steering = SteeringHandle::allow_all();
        steering_registry.register(task_id.clone(), steering.clone());
        tokio::spawn(async move {
            let _ = store.mark_running(&spawned_task_id);
            let graph = GraphBuilder::<RunState, RunState>::overwrite()
                .add_node(
                    "subagent",
                    move |mut state: RunState, _context: NodeContext| {
                        let executor = executor.clone();
                        let steering = steering.clone();
                        async move {
                            let response = executor
                                .execute(&state.run_id, state.input.clone(), steering)
                                .await?;
                            state.response = Some(response);
                            Ok(NodeResult::Update(state))
                        }
                    },
                )
                .set_entry("subagent")
                .set_finish("subagent")
                .compile()
                .map(|graph| graph.with_run_deadline(RUN_TIMEOUT));

            let outcome = match graph {
                Ok(graph) => tokio::time::timeout(
                    RUN_TIMEOUT,
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
        });
        Ok(task_id)
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
        let deadline =
            tokio::time::Instant::now() + Duration::from_secs(wait_seconds.min(MAX_AWAIT_SECONDS));
        loop {
            let record = self.record(task_id)?;
            if record.status.is_terminal() || tokio::time::Instant::now() >= deadline {
                return Ok(record);
            }
            tokio::time::sleep(Duration::from_millis(20)).await;
        }
    }

    pub(super) fn tools(
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
                "Starts a subagent asynchronously and immediately returns its run id."
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
                    "input": { "type": "string" }
                },
                "required": ["agent", "input"],
                "additionalProperties": false
            }),
            AsyncToolKind::Peek => run_id_schema(false),
            AsyncToolKind::Steer => json!({
                "type": "object",
                "properties": {
                    "run_id": { "type": "string" },
                    "instruction": { "type": "string" }
                },
                "required": ["run_id", "instruction"],
                "additionalProperties": false
            }),
            AsyncToolKind::Await => run_id_schema(true),
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
                    .unwrap_or(MAX_AWAIT_SECONDS);
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

fn run_id_schema(with_wait: bool) -> Value {
    if with_wait {
        json!({
            "type": "object",
            "properties": {
                "run_id": { "type": "string" },
                "wait_seconds": { "type": "integer", "minimum": 0, "maximum": MAX_AWAIT_SECONDS }
            },
            "required": ["run_id"],
            "additionalProperties": false
        })
    } else {
        json!({
            "type": "object",
            "properties": { "run_id": { "type": "string" } },
            "required": ["run_id"],
            "additionalProperties": false
        })
    }
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
