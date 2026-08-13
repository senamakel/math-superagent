#[derive(Clone, Debug)]
struct RunState {
    run_id: String,
    input: String,
    response: Option<String>,
}

#[derive(Clone, Copy, Debug)]
enum AsyncToolKind {
    Spawn,
    SpawnMany,
    Peek,
    Steer,
    Await,
    AwaitMany,
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

    /// Launches a whole fan-out in one call.
    ///
    /// Every tool call costs the caller a full model turn — measured at a p90
    /// of 197 seconds on a live run — so issuing five spawns one at a time
    /// spends minutes of generation before any of the work starts. This makes
    /// width cheap: the concurrency cap, not the number of calls, is then what
    /// bounds execution.
    fn spawn_many(&self, call: &ToolCall) -> Result<Value> {
        let runs = call
            .arguments
            .get("runs")
            .and_then(Value::as_array)
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation(
                    "`runs` is required and must be a non-empty array".into(),
                )
            })?;
        if runs.len() > MAX_BATCH_SPAWNS {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "at most {MAX_BATCH_SPAWNS} runs may be launched in one call"
            )));
        }
        // Every brief is checked before any run starts. A batch that
        // half-launches is worse than one that is refused: the caller is told
        // the call failed while agents it did not account for are already
        // consuming budget.
        let mut planned = Vec::with_capacity(runs.len());
        for entry in runs {
            let agent = required_string(entry, "agent")?;
            if !self.allowed_agents.contains(&agent) {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "subagent `{agent}` is not allowed from this caller"
                )));
            }
            planned.push((agent, required_string(entry, "input")?));
        }
        let mut started = Vec::with_capacity(planned.len());
        for (agent, input) in planned {
            let run_id = self.manager.spawn(&agent, input)?;
            started.push(json!({ "agent": agent, "run_id": run_id }));
        }
        Ok(json!({ "runs": started, "status": "pending" }))
    }

    /// Collects several runs at once, waiting for them concurrently.
    ///
    /// Awaiting one at a time would re-serialise work the spawn just
    /// parallelised, and cost a turn for each.
    async fn await_many(&self, call: &ToolCall) -> Result<Value> {
        let wait_seconds = call
            .arguments
            .get("wait_seconds")
            .and_then(Value::as_u64)
            .unwrap_or_else(|| self.manager.max_await_seconds());
        let requested: Vec<String> = match call.arguments.get("run_ids") {
            Some(Value::Array(ids)) => ids
                .iter()
                .filter_map(Value::as_str)
                .map(str::to_string)
                .collect(),
            _ => self.manager.outstanding_runs(),
        };
        if requested.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "no runs to wait for: pass `run_ids`, or start runs first".into(),
            ));
        }
        // Waited concurrently, so the batch costs the slowest run rather than
        // the sum.
        let mut waits = tokio::task::JoinSet::new();
        for run_id in requested {
            let manager = self.manager.clone();
            waits.spawn(async move {
                match manager.await_record(&run_id, wait_seconds).await {
                    Ok(record) => record.to_json(),
                    Err(error) => json!({ "run_id": run_id, "error": error.to_string() }),
                }
            });
        }
        let mut finished = Vec::new();
        while let Some(joined) = waits.join_next().await {
            match joined {
                Ok(value) => finished.push(value),
                Err(error) => finished.push(json!({ "error": error.to_string() })),
            }
        }
        Ok(json!({ "runs": finished }))
    }
}

#[async_trait]
impl Tool<()> for AsyncSubagentTool {
    fn name(&self) -> &'static str {
        match self.kind {
            AsyncToolKind::Spawn => "spawn_agent",
            AsyncToolKind::SpawnMany => "spawn_agents",
            AsyncToolKind::AwaitMany => "await_agents",
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
                 never happens. Prefer spawn_agents when you have more than one thing to start."
            }
            AsyncToolKind::SpawnMany => {
                "Starts several subagents at once and returns all their run ids. Prefer this over \
                 repeated spawn_agent: every call you make costs a full turn, so launching five \
                 agents one at a time spends minutes of generation before any of them starts, \
                 while this launches them together. Split the work into pieces that do not depend \
                 on each other and launch every piece here in one call — the runtime executes \
                 dozens concurrently. Each brief is a few sentences; the agents read the \
                 workspace themselves."
            }
            AsyncToolKind::AwaitMany => {
                "Waits for several subagent runs and returns all their results together. Use it \
                 after spawn_agents: awaiting one run at a time serialises work that already ran \
                 in parallel, and costs a turn for each. Omit `run_ids` to wait for every run you \
                 have started that is still outstanding."
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
            AsyncToolKind::SpawnMany => json!({
                "type": "object",
                "properties": {
                    "runs": {
                        "type": "array",
                        "minItems": 1,
                        "maxItems": MAX_BATCH_SPAWNS,
                        "description": "Every independent piece of work to launch together.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "agent": {
                                    "type": "string",
                                    "enum": self.allowed_agents.as_ref()
                                },
                                "input": {
                                    "type": "string",
                                    "description": "A short brief: the task and what to report \
                                                    back.",
                                    "maxLength": 2000
                                }
                            },
                            "required": ["agent", "input"],
                            "additionalProperties": false
                        }
                    }
                },
                "required": ["runs"],
                "additionalProperties": false
            }),
            AsyncToolKind::AwaitMany => json!({
                "type": "object",
                "properties": {
                    "run_ids": {
                        "type": "array",
                        "items": { "type": "string" },
                        "description": "Runs to wait for. Omit to wait for every outstanding run."
                    },
                    "wait_seconds": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": self.manager.max_await_seconds()
                    }
                },
                "additionalProperties": false
            }),
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
            AsyncToolKind::SpawnMany => self.spawn_many(&call)?,
            AsyncToolKind::AwaitMany => self.await_many(&call).await?,
            AsyncToolKind::Peek => self
                .manager
                .record(&required_string(&call.arguments, "run_id")?)?
                .to_json(),
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
                self.manager
                    .await_record(&required_string(&call.arguments, "run_id")?, wait_seconds)
                    .await?
                    .to_json()
            }
        };
        Ok(ToolResult::text(
            call.id,
            self.name(),
            serde_json::to_string(&value)?,
        ))
    }

    /// Lets a wait outlive the per-tool ceiling it was never meant to obey.
    ///
    /// The run ceiling and the tool ceiling are separate limits, and a wait is
    /// governed by the first: a caller must be able to wait out a child using
    /// its full run budget, or the orchestrator is structurally unable to
    /// collect the result of the deepest work it delegated. The schema already
    /// says so — `wait_seconds` accepts up to the run ceiling — but the
    /// harness applied the ten-minute tool ceiling on top, so a wait for
    /// longer than that died with a timeout error rather than the child's
    /// result. A live `pattern_finder` asked for 600 seconds, was killed at
    /// exactly 600,000 ms, and lost the run it had commissioned.
    ///
    /// The deadline is the requested wait plus a grace, so the wait itself
    /// expires first and returns what it knows rather than being cut off. Only
    /// the awaiting kinds override this; every other call is a fast local
    /// operation and inherits the ordinary ceiling.
    fn timeout_policy(&self, call: &ToolCall) -> tinyagents::harness::tool::ToolTimeout {
        use tinyagents::harness::tool::ToolTimeout;
        if !matches!(self.kind, AsyncToolKind::Await | AsyncToolKind::AwaitMany) {
            return ToolTimeout::Inherit;
        }
        let maximum = self.manager.max_await_seconds();
        let requested = call
            .arguments
            .get("wait_seconds")
            .and_then(Value::as_u64)
            .unwrap_or(maximum)
            .min(maximum);
        ToolTimeout::Millis(
            requested
                .saturating_add(AWAIT_GRACE_SECONDS)
                .saturating_mul(1_000),
        )
    }
}
