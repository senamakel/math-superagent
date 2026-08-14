
impl OrchestratorAgent {
    /// Loads provider configuration and assembles the built-in registry.
    ///
    /// The runtime must be launched by the Docker wrapper, which sets
    /// `MATH_AGENT_CONTAINER=1` and mounts the selected workspace at `/workspace`.
    ///
    /// # Errors
    ///
    /// Returns an error when `Docker` runtime markers, workspace, `OpenRouter`,
    /// Exa, or Langfuse configuration are unavailable.
    pub fn from_env() -> Result<Self> {
        let _ = dotenvy::dotenv();
        require_container_runtime()?;
        let workspace = workspace_from_env()?;
        // Bound every provider request: the vendored default only applies when
        // the request leaves `timeout_ms` unset, and the agent loop never sets
        // it, so a stalled connection otherwise blocks for ten minutes before
        // the first retry.
        let model: Arc<dyn ChatModel<()>> =
            Arc::new(BoundedTimeoutModel::new(openrouter_model_from_env()?));
        // The one role that is not on the run's default model. It gets the same
        // timeout bound, because a stalled connection is a property of the
        // transport rather than of the model behind it.
        let reasoning: Arc<dyn ChatModel<()>> =
            Arc::new(BoundedTimeoutModel::new(openrouter_reasoning_model()?));
        let budget = RunBudget::from_env();
        let research_enabled = research_enabled_from_env();
        let tracer = start_tracer(&workspace, budget, research_enabled);
        convert_problem_statement(&workspace);
        let vector_store = VectorStore::from_env()?;
        let async_subagents = AsyncSubagentManager::new(budget, Some(tracer.clone()))
            .with_session_memory(vector_store.clone());
        // Every download is filed in this project's library dataset as well as
        // under `research/`, so what the run gathered is reachable by wording
        // rather than only by a path someone remembers.
        let documents =
            WorkspaceDocuments::new(workspace.clone())?.with_library(vector_store.clone());
        // Commits the workspace after every successful write, so a rewritten
        // solution or an edited belief is recoverable rather than lost.
        let checkpoint: Arc<dyn tinyagents::harness::middleware::Middleware<()>> = Arc::new(
            checkpoint::WorkspaceCheckpoint::new(workspace.clone(), Some(tracer.clone())),
        );
        let mut prompts = RolePrompts::load(&workspace)?;

        let search = search_tools(research_enabled, &documents)?;

        let mut research_harness = build_research_harness(
            &model,
            budget,
            &tracer,
            &documents,
            &vector_store,
            search.clone(),
        );
        research_harness.push_middleware(checkpoint.clone());
        async_subagents.register(
            "research",
            Arc::new(research_harness),
            std::mem::take(&mut prompts.research),
        )?;

        register_code_writing_agents(
            &async_subagents,
            &CodeWriters {
                model: &model,
                budget,
                tracer: &tracer,
                workspace: &workspace,
                documents: &documents,
                checkpoint: &checkpoint,
                vector_store: &vector_store,
            },
            prompts.code_writers(),
        )?;

        register_support_agents(
            &async_subagents,
            &SupportAgents {
                model: &model,
                reasoning: &reasoning,
                budget,
                tracer: &tracer,
                documents: &documents,
                vector_store: vector_store.clone(),
                search: search.clone(),
                workspace: workspace.clone(),
                delegation: async_subagents.tools(PATTERN_DELEGATES),
            },
            prompts.support(),
        )?;

        let orchestrator_harness = register_planners(
            &async_subagents,
            &Planners {
                model: &model,
                budget,
                tracer: &tracer,
                documents: &documents,
                vector_store: &vector_store,
            },
            std::mem::take(&mut prompts.goals),
        )?;

        let registry = Arc::new(default_registry(research_enabled)?);

        Ok(Self {
            inner: ObservedAgent::from_harness(orchestrator_harness)?.with_tracer(tracer.clone()),
            registry,
            system_prompt: prompts.orchestrator,
            subagents: async_subagents,
            tracer,
            workspace,
            memory: vector_store,
        })
    }

    /// Runs the graph-backed solution loop over a problem.
    ///
    /// Unlike [`Self::run`], which gives the orchestrator a single turn and
    /// trusts it to delegate well, this drives an explicit attempt, reflect,
    /// diversify cycle. Use it when the problem is hard enough that the first
    /// approach is likely to be wrong.
    ///
    /// # Errors
    ///
    /// Returns an error only when the loop graph cannot be compiled or run; a
    /// failing specialist becomes a lesson rather than a failure.
    pub async fn solve(&self, problem: impl Into<String>) -> Result<String> {
        let problem = problem.into();
        self.solve_on_workflow(&problem).await
    }

    /// Runs the same loop on the workflow engine.
    ///
    /// The support teams still run beside it, unchanged: they are host-side
    /// tasks with their own budgets, they outlive any single graph run, and
    /// folding them into the graph would tie their lifetime to it — which is
    /// the thing `teams.rs` exists to prevent.
    ///
    /// The tool set is deliberately narrow. A `tool_call` node can reach
    /// anything the bundle holds, and the only tool this graph calls is the
    /// reflection parser — which `workflow_capabilities` supplies itself. Every
    /// other tool a role uses reaches it through the role, where the per-role
    /// grants still apply.
    ///
    /// # Errors
    ///
    /// Returns an error when the graph fails to compile or the run fails. A
    /// failing specialist is still a lesson rather than a failure: that is the
    /// roles' behaviour, not the engine's, and it is unchanged here.
    async fn solve_on_workflow(&self, problem: &str) -> Result<String> {
        let patterns = solutions::Mailbox::default();
        let directives = solutions::Mailbox::default();
        let skeletons = solutions::Mailbox::default();
        let support = self.spawn_support_teams(problem, &patterns, &directives);

        // The same mailboxes and beside-arms the state graph gave its steps.
        // They are what carries a directive into an attempt and what opens the
        // pattern and reduction arms, and the steps drain them exactly as
        // before — see `loop_steps`.
        let mailboxes = solutions::Mailboxes {
            patterns: patterns.clone(),
            directives,
            skeletons: skeletons.clone(),
        };
        let beside = solutions::Beside {
            // The same mailbox the standing teams post to, and the same one the
            // attempt drains. A literature sweep and a team report are both
            // "what arrived beside the loop since the last attempt", so they
            // are rendered under that one heading rather than two.
            library: patterns,
            reduction: solutions::Reduction {
                outbox: skeletons,
                // One gate for the run, so a reduction that outlives the cycle
                // that opened it cannot be joined by a second one writing the
                // same file.
                gate: solutions::ReductionGate::default(),
            },
            teams: support.clone(),
        };

        let outcome = self.run_workflow_loop(problem, beside, mailboxes).await;

        // The teams are normally already stopped: the loop's `stand_down` node
        // does it the moment the loop ends, so they take no cycles while the
        // novelty check and the judge run. This stays as the backstop for the
        // paths that never reach that node — a workflow error, a compile
        // failure — and it reports which case happened, because "the run
        // finished and the teams were still going" is the defect this pair of
        // calls exists to make visible rather than to hide.
        for team in &support {
            let already = team.is_cancelled();
            team.cancel();
            self.tracer.note(&format!(
                "team {}: {} cycle(s) alongside the solve, {}",
                team.name(),
                team.cycles(),
                if already {
                    "stood down when the loop ended"
                } else {
                    "still running at the end of the run"
                }
            ));
        }

        let outcome = match outcome {
            Ok(outcome) => outcome,
            Err(error) => {
                self.record_session(
                    "solution-loop",
                    problem,
                    &format!("SESSION FAILED: {error}"),
                )
                .await;
                return Err(error);
            }
        };
        self.record_session("solution-loop", problem, &outcome).await;
        Ok(outcome)
    }

    /// Compiles and runs the loop graph, and reports what it reached.
    ///
    /// The report is built by rebuilding a `SolutionState` from the
    /// accumulator and calling the same `outcome` the state graph calls, rather
    /// than by describing the numbers here. That wording is written against
    /// specific ways a run can end — an answer with one route behind it must
    /// not be called solved, a provider failure must not read as a
    /// mathematical one — and a second version of it would get one of them
    /// wrong.
    async fn run_workflow_loop(
        &self,
        problem: &str,
        beside: solutions::Beside,
        mailboxes: solutions::Mailboxes,
    ) -> Result<String> {
        let graph = self.workflow_graph(problem);
        let steps = Arc::new(loop_steps::LoopSteps::new(
            self.subagents.clone(),
            Some(self.tracer.clone()),
            Some(self.workspace.clone()),
            self.memory.clone(),
            beside,
            mailboxes,
        )) as Arc<dyn Tool<()>>;
        let capabilities = self.workflow_capabilities([steps])?;
        let compiled = tinyflows::compiler::compile(&graph).map_err(|error| {
            tinyagents::TinyAgentsError::Graph(format!("the loop graph is invalid: {error}"))
        })?;
        let finished = tinyflows::engine::run(&compiled, serde_json::json!({}), &capabilities)
            .await
            .map_err(|error| {
                tinyagents::TinyAgentsError::Graph(format!("the loop graph failed: {error}"))
            })?;
        let accumulator = finished
            .output
            .pointer(&format!("/nodes/{}/state", workflow::LOOP_NODE))
            .cloned()
            .unwrap_or(serde_json::Value::Null);
        // The judge runs on the way out, after the head has folded its last
        // pass, so its score is in its own output and not in the accumulator.
        // Reading only the accumulator would spend a whole agent run scoring the
        // work and then report a state that had never heard of it.
        let accumulator = finished
            .output
            .pointer(&format!("/nodes/{}/item/json", workflow::FINAL_JUDGE))
            .cloned()
            .unwrap_or(accumulator);
        Ok(solutions::SolutionState::from_accumulator(problem, &accumulator).outcome())
    }

    /// Starts the long-lived teams that work alongside the solution loop.
    ///
    /// Each gets its own budget and wall clock: `RunBudget` bounds a single
    /// agent run, and a team runs many, so a per-run bound says nothing about
    /// what the team as a whole costs. A team that exhausts its allowance stops
    /// and says so while the others carry on.
    fn spawn_support_teams(
        &self,
        problem: &str,
        patterns: &solutions::Mailbox,
        directives: &solutions::Mailbox,
    ) -> Vec<teams::TeamHandle> {
        let mut handles = Vec::new();
        for (name, agent, completion, budget, brief) in standing_teams() {
            if !self.subagents.knows(agent) {
                continue;
            }
            let subagents = self.subagents.clone();
            let workspace = self.workspace.clone();
            let outbox = patterns.clone();
            let direction = directives.clone();
            let tracer = self.tracer.clone();
            // What the pattern team has already looked at. Idleness has to be
            // decided *before* the agent runs: asking it to notice that
            // nothing changed costs a model call and a read of the workspace
            // to discover, which is most of what a working cycle costs. A live
            // team spent thirty `read_document` calls in two minutes doing
            // exactly that on runs that had produced almost nothing.
            let analysed = Arc::new(std::sync::Mutex::new(None::<u64>));
            let prompt = format!("{brief}\n\nProblem this run is solving:\n{problem}");
            handles.push(teams::spawn(
                name,
                budget,
                Some(self.tracer.clone()),
                Some(self.workspace.clone()),
                move |inbox: Vec<teams::TeamMessage>| {
                    let subagents = subagents.clone();
                    let outbox = outbox.clone();
                    let direction = direction.clone();
                    let tracer = tracer.clone();
                    let ledger_workspace = workspace.clone();
                    let analysed = analysed.clone();
                    let mut prompt = prompt.clone();
                    // The pattern agent reads results, so a cycle over results
                    // it has already seen can only repeat itself or invent
                    // something. Decided before the agent runs, so an idle
                    // cycle costs a directory walk rather than a model call.
                    let skip = match name {
                        "patterns" => results_unchanged(&workspace, &analysed),
                        // Nothing queued is the normal case for this team —
                        // it wakes every twenty seconds and a person types
                        // rarely — so the check has to be the cheap one, and
                        // it has to happen here rather than in the brief. A
                        // model asked to notice its own queue is empty has
                        // already been paid for the call that discovers it.
                        "director" => directives_waiting(&workspace),
                        // The curator writes `CONTEXT.md`, so its own file is
                        // excluded from what it watches: counting it would
                        // have the team waking itself forever on the brief it
                        // just wrote.
                        "context" => workspace_unchanged(
                            &workspace,
                            &analysed,
                            &[shared_context::CONTEXT_FILE],
                        ),
                        _ => None,
                    };
                    // The standing is the one fact that changes between
                    // cycles and the one that decides what a cycle is for, so
                    // it is computed per cycle rather than baked into the
                    // brief at spawn.
                    if name == "context" {
                        let _ = write!(prompt, "\n\n{}", shared_context::briefing(&workspace));
                    }
                    // Taken here, before the agent runs, and posted to the
                    // loop's mailbox on the way past. That ordering is what
                    // makes the verbatim delivery independent of this team
                    // succeeding: the next attempt gets what the operator
                    // typed even if the director's own model call fails, which
                    // is the failure most worth surviving — a directive is the
                    // one input to a run that cannot be regenerated.
                    let taken = if name == "director" && skip.is_none() {
                        take_directives(&workspace, &direction, &tracer)
                    } else {
                        Vec::new()
                    };
                    for directive in &taken {
                        let _ = write!(
                            prompt,
                            "\n\nDirective {} from {}:\n{}",
                            directive.id, directive.from, directive.text
                        );
                    }
                    for message in &inbox {
                        let _ = write!(prompt, "\n\nFrom {}: {}", message.from, message.body);
                    }
                    async move {
                        if let Some(skip) = skip {
                            return skip;
                        }
                        let result = subagents.run_to_completion(agent, prompt).await;
                        // The receipt is written whatever happened, a failed
                        // cycle included. On a channel that never blocks, an
                        // operator who sees nothing cannot tell a directive
                        // still queued from one that was picked up and lost,
                        // and the second is the one they need to know about.
                        if !taken.is_empty() {
                            let outcome = match &result {
                                Ok(reply) => reply.trim().to_string(),
                                Err(error) => format!(
                                    "The director could not act on this: {error}. The next \
                                     attempt was still given it verbatim."
                                ),
                            };
                            for directive in &taken {
                                if let Err(error) =
                                    directives::record(&ledger_workspace, directive, &outcome)
                                {
                                    tracer.note(&format!("directive receipt failed: {error}"));
                                }
                            }
                        }
                        match result {
                            // A team whose goal is open-ended needs a way to
                            // say it has run out of useful work, or it spends
                            // its whole allowance re-tidying a tidy workspace.
                            Ok(reply) if reply.to_uppercase().contains("NOTHING FURTHER") => {
                                completion.nothing_further()
                            }
                            Ok(reply) => {
                                // A structural finding is worth as much an
                                // attempt later, so it is left where the next
                                // reflection collects it rather than
                                // interrupting the solve to deliver it.
                                if name == "patterns" {
                                    outbox.post(reply);
                                }
                                teams::Cycle::Worked
                            }
                            // A failed cycle is not a reason to end the team:
                            // the next one may well succeed, and a support team
                            // that quits on one error stops serving the solve
                            // for the rest of the run.
                            Err(_) => teams::Cycle::Idle,
                        }
                    }
                },
            ));
        }
        handles
    }

    /// Returns the registry used for delegation.
    ///
    #[must_use]
    pub fn registry(&self) -> &Arc<AgentRegistry> {
        &self.registry
    }

    /// Runs one orchestrated task and returns the final combined answer.
    ///
    /// # Errors
    ///
    /// Returns any provider, specialist, tool, policy, or loop error.
    pub async fn run(&self, run_id: impl Into<String>, task: impl Into<String>) -> Result<String> {
        let run_id = run_id.into();
        let task = task.into();
        let run = self
            .inner
            .invoke(
                run_id.clone(),
                vec![
                    Message::system(self.system_prompt.clone()),
                    Message::user(task.clone()),
                ],
            )
            .await;
        let run = match run {
            Ok(run) => run,
            Err(error) => {
                self.record_session(&run_id, &task, &format!("SESSION FAILED: {error}"))
                    .await;
                return Err(error);
            }
        };
        let output = run.text().unwrap_or_default();
        self.record_session(&run_id, &task, &output).await;
        Ok(output)
    }

    /// Writes one orchestrator run to the session memory, saying so when it
    /// fails.
    ///
    /// Best effort, as it has always been — the answer is already returned to
    /// the caller and a memory server that is down must not turn a finished
    /// solve into a failed one. What is new is that a failure is *said*: the
    /// four call sites discarded the result, so a session nobody recorded and a
    /// session recorded fine read identically on the console and in
    /// `trace.jsonl`.
    async fn record_session(&self, run_id: &str, input: &str, output: &str) {
        if let Err(error) = self
            .memory
            .remember_session("orchestrator", run_id, input, output)
            .await
        {
            self.tracer.note(&format!(
                "session memory failed for orchestrator/{run_id}: {error}"
            ));
        }
    }
}
