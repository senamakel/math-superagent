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
            store: RunStore::new(),
            steering: SteeringRegistry::new(),
            budget,
            tracer,
            langfuse: LangfuseClient::from_env().ok().map(Arc::new),
            slots: Arc::new(Semaphore::new(concurrency)),
            session: session_id(),
            memory: None,
            school: None,
        }
    }

    /// This manager seen from inside one school.
    ///
    /// A cheap clone: the registry, the concurrency semaphore, the run store,
    /// the tracer and the budget pool are all shared, which is the point of
    /// qualifying a name rather than standing up a second manager. Two schools
    /// running at once must compete for the same fifty slots and appear in the
    /// same trace, or the cap bounds nothing and the run is unreadable.
    ///
    /// What changes is only the naming: registering `goals` here registers
    /// `goals@<slug>`, and spawning `goals` here reaches that registration.
    /// Every bench in this crate names roles bare — `SPECIALISTS`,
    /// `INVENTION_BENCH` and the rest — so an agent built from a school-scoped
    /// handle can only reach its own school's copy of a role, and the solution
    /// loop keeps calling [`Self::run_to_completion`] with bare names.
    ///
    /// Scope only when more than one school is running. A single school must
    /// register unqualified, because the loop that drives it holds the
    /// unscoped manager, and an unqualified run is today's run to the byte.
    pub(in crate::orchestrator) fn for_school(&self, slug: &str) -> Self {
        Self {
            school: Some(Arc::from(slug)),
            ..self.clone()
        }
    }

    /// The name `name` is registered under from this handle.
    ///
    /// Idempotent: a name that already carries a school is left alone, so
    /// qualifying at both the turn-cap and the executor layer cannot produce
    /// `goals@chisel@chisel`.
    fn qualified(&self, name: String) -> String {
        match self.school.as_deref() {
            Some(school) if !name.contains('@') => format!("{name}@{school}"),
            _ => name,
        }
    }

    /// The registration a bare role name reaches from this handle.
    ///
    /// Falls back to the unqualified name when this school has no copy of the
    /// role, so a role registered once for the whole run — or a caller that
    /// already wrote the qualified name — still resolves.
    fn resolve(&self, agent: &str) -> String {
        let Some(school) = self.school.as_deref() else {
            return agent.to_string();
        };
        if agent.contains('@') {
            return agent.to_string();
        }
        let qualified = format!("{agent}@{school}");
        if self.knows_exactly(&qualified) {
            qualified
        } else {
            agent.to_string()
        }
    }

    /// Whether this exact registration name exists, without resolving it.
    fn knows_exactly(&self, agent: &str) -> bool {
        self.agents
            .read()
            .is_ok_and(|agents| agents.contains_key(agent))
    }

    /// Ingests every completed child session into Cognee.
    pub(super) fn with_session_memory(mut self, memory: VectorStore) -> Self {
        self.memory = Some(memory);
        self
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
        self.register_with_turn_cap(
            name,
            harness,
            system_prompt,
            self.budget.max_turn_output_tokens,
        )
    }

    /// Registers a specialist whose turns are capped differently to the run's.
    ///
    /// The cap reaches the provider through `RunConfig`, which is built here
    /// rather than in the harness, so passing a widened [`RunBudget`] to
    /// `specialist_harness` alone is not enough: that sets the ceiling the
    /// re-issue wrapper may grow *to*, while this sets what the first attempt
    /// asks for. Both have to move together or the role is cut off at the run's
    /// cap and then re-issued into the wider one, paying for the turn twice.
    ///
    /// Only the inventor uses it. See [`RunBudget::for_invention`].
    pub(crate) fn register_with_turn_cap(
        &self,
        name: impl Into<String>,
        harness: Arc<AgentHarness<()>>,
        system_prompt: impl Into<String>,
        max_turn_output_tokens: u32,
    ) -> Result<()> {
        // Qualified here as well as in `register_executor`, so the trace name
        // says which school produced a turn. The qualification is idempotent.
        let name = self.qualified(name.into());
        let role = name.clone();
        self.register_executor(
            name,
            Arc::new(HarnessExecutor {
                harness,
                system_prompt: system_prompt.into(),
                langfuse: self.langfuse.clone(),
                max_turn_output_tokens,
                role,
                session: self.session.clone(),
            }),
        )
    }

    pub(super) fn register_executor(
        &self,
        name: impl Into<String>,
        executor: Arc<dyn AgentExecutor>,
    ) -> Result<()> {
        let name = self.qualified(name.into());
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

    /// Reports whether this handle can reach an agent by that name.
    ///
    /// Resolved through the school, so a caller asking about `scholar` on a
    /// school-scoped handle is asking about that school's scholar.
    pub(super) fn knows(&self, agent: &str) -> bool {
        self.knows_exactly(&self.resolve(agent))
    }

    /// Looks up a registered agent by name.
    ///
    /// # Errors
    ///
    /// Returns an error when the registry lock is poisoned or the name is not
    /// registered — the second being how a typo in a delegation reaches the
    /// caller as a message rather than as a run that silently never happens.
    fn executor_for(&self, agent_name: &str) -> Result<Arc<dyn AgentExecutor>> {
        self.agents
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
            })
    }

    fn spawn(&self, agent_name: &str, input: String) -> Result<TaskId> {
        // Resolved once, and everything downstream — the run record, the trace
        // child, the session memory — is written under the resolved name, so
        // which school ran a turn is answerable from the record rather than
        // only from whoever spawned it.
        let agent_name = self.resolve(agent_name);
        let agent_name = agent_name.as_str();
        let executor = self.executor_for(agent_name)?;
        let sequence = NEXT_RUN_ID.fetch_add(1, Ordering::Relaxed);
        let task_id = TaskId::new(format!("agent-run-{sequence}"));
        self.store.insert(task_id.clone(), agent_name)?;

        let store = self.store.clone();
        let steering_registry = self.steering.clone();
        let spawned_task_id = task_id.clone();
        let run_id = task_id.as_str().to_string();
        let steering = SteeringHandle::allow_all();
        steering_registry.register(&task_id, steering.clone());
        let run_timeout = self.budget.run_timeout;
        let tracer = self
            .tracer
            .as_ref()
            .map(|tracer| tracer.child(format!("{agent_name}/{run_id}")));
        if let Some(tracer) = tracer.as_ref() {
            tracer.note(&format!("spawned: {}", preview_input(&input)));
        }
        // The run's own tracer is moved into the graph node; recording happens
        // after that node has finished, so it needs its own handle.
        let record_tracer = tracer.clone();
        let slots = self.slots.clone();
        let session_memory = self.memory.clone();
        let session_agent = agent_name.to_string();
        let session_input = input.clone();
        let session_run_id = run_id.clone();
        let follow_up = FOLLOW_UPS
            .iter()
            .find(|(after, _)| *after == base_role(agent_name))
            .map(|(_, steps)| FollowUp {
                manager: self.clone(),
                steps,
            });
        tokio::spawn(async move {
            // Queue for a slot before doing anything else. Acquiring here
            // rather than in `spawn` is what keeps a spawn cheap and
            // non-blocking: the caller gets its run id immediately and the
            // queue drains behind it. The run deadline starts after the wait,
            // so a queued run is not charged for time it spent waiting.
            let _permit = slots.acquire().await;
            store.mark_running(&spawned_task_id);
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
                                .await
                                .map_err(crate::agent::flow::into_graph)?;
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
                .map_err(|_| GraphError::Timeout("subagent run timed out".into()))
                .and_then(|result| result),
                Err(error) => Err(error),
            };
            let succeeded = record_outcome(
                outcome,
                &Recording {
                    memory: session_memory.as_ref(),
                    agent: &session_agent,
                    run_id: &session_run_id,
                    input: &session_input,
                    store: &store,
                    task_id: &spawned_task_id,
                    tracer: record_tracer.as_ref(),
                },
            )
            .await;
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

    /// Starts `agent` on `input` without waiting, returning its run id.
    ///
    /// The same detached spawn the model-visible `spawn_agent` tool performs,
    /// named for the `TinyFlows` [`TaskRunner`](super::runner::SubagentTaskRunner)
    /// that offers it to a `spawn` node. Separate from the private `spawn` only
    /// in visibility: a capability implementation lives outside this module and
    /// must not reach into it for anything wider.
    ///
    /// # Errors
    ///
    /// Returns an error when `agent` is not registered, or when the run
    /// registry refuses the new id.
    pub(super) fn spawn_detached(&self, agent: &str, input: String) -> Result<TaskId> {
        self.spawn(agent, input)
    }

    /// Reads a run's record, or nothing when the id was never issued.
    ///
    /// Returns an `Option` rather than this crate's `Result` because the one
    /// caller outside this module distinguishes "unknown ticket" from every
    /// other failure and has its own error type to say so in.
    pub(super) fn task_record(&self, task_id: &str) -> Option<RunRecord> {
        self.record(task_id).ok()
    }

    /// Asks a live run to stop, cooperatively.
    ///
    /// Delivered through the same steering channel a human directive uses, so a
    /// run stops at its next boundary rather than being killed mid-tool-call and
    /// leaving a half-written workspace file behind.
    ///
    /// # Errors
    ///
    /// Returns an error when the run is unknown, already terminal, or has no
    /// steering handle registered.
    pub(super) fn stop_run(&self, task_id: &str) -> Result<()> {
        self.steer(
            task_id,
            "Stop this run now. Write down what you have established so far and \
             finish; do not start anything new."
                .to_string(),
        )
    }

    fn record(&self, task_id: &str) -> Result<RunRecord> {
        let task_id = TaskId::new(task_id);
        self.store.get(&task_id).ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("unknown agent run `{task_id}`"))
        })
    }

    /// Lists runs that have been started and have not yet finished.
    ///
    /// Lets `await_agents` be called with no arguments, which is the shape a
    /// caller actually wants after a batch spawn: it knows it is waiting for
    /// "everything I just started" and should not have to copy run ids back
    /// out of a previous tool result to say so.
    fn outstanding_runs(&self) -> Vec<String> {
        self.store
            .list()
            .into_iter()
            .filter(|record| matches!(record.status, RunStatus::Pending | RunStatus::Running))
            .map(|record| record.task_id().to_string())
            .collect()
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
    ) -> Result<RunRecord> {
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
                allowed.clone(),
            )),
            Arc::new(AsyncSubagentTool::new(
                AsyncToolKind::SpawnMany,
                self.clone(),
                allowed.clone(),
            )),
            Arc::new(AsyncSubagentTool::new(
                AsyncToolKind::AwaitMany,
                self.clone(),
                allowed,
            )),
        ]
    }
}
