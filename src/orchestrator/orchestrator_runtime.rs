
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
        let screen = start_screen(&workspace, &model, &tracer)?;
        let async_subagents = AsyncSubagentManager::new(budget, Some(tracer.clone()))
            .with_session_memory(vector_store.clone());
        // Every download is filed in this project's library dataset as well as
        // under `research/`, so what the run gathered is reachable by wording
        // rather than only by a path someone remembers.
        let documents = WorkspaceDocuments::new(workspace.clone())?
            .with_library(vector_store.clone())
            .with_screen(screen.clone())
            // Wrapped in accounting here rather than inside the tool, so a
            // chunk read appears in `model_accounting` under its own name and a
            // run interrogating a 400 KB survey can see what that cost it.
            .with_reader(Arc::new(AccountingModel::new(
                model.clone(),
                "chunk_reader",
                tracer.clone(),
            )));
        // Commits the workspace after every successful write, so a rewritten
        // solution or an edited belief is recoverable rather than lost.
        let checkpoint: Arc<dyn tinyagents::harness::middleware::Middleware<()>> = Arc::new(
            checkpoint::WorkspaceCheckpoint::new(workspace.clone(), Some(tracer.clone())),
        );
        let search = search_tools(research_enabled, &documents, screen.as_ref())?;

        // Every school gets its own copy of every role, because a role's prompt
        // is where the school actually lives. They share one manager, and so
        // one concurrency semaphore, one trace and one budget pool: two schools
        // competing for the same fifty slots is the point, and a second manager
        // would give each of them fifty.
        let schools = schools::selected();
        let mut opening: Option<(AgentHarness<()>, String)> = None;
        for school in &schools {
            // Qualified only when there is more than one. A lone school
            // registers unqualified, so the single-school run is today's run to
            // the byte rather than today's run with a suffix on every name.
            let scoped = if schools.len() > 1 {
                async_subagents.for_school(school.slug)
            } else {
                async_subagents.clone()
            };
            let orchestrator_harness = register_school(
                &scoped,
                school,
                &Roster {
                    model: &model,
                    reasoning: &reasoning,
                    budget,
                    tracer: &tracer,
                    workspace: &workspace,
                    documents: &documents,
                    checkpoint: &checkpoint,
                    vector_store: &vector_store,
                    search: &search,
                    siblings: schools.len() > 1,
                },
            )?;
            // `run` gives one agent a single turn, so it belongs to one school:
            // the first selected, which is the control unless an operator
            // deliberately ordered the list otherwise. Schools are a property
            // of the solution loop, and a single-turn delegation is not one.
            if opening.is_none() {
                opening = Some(orchestrator_harness);
            }
        }
        // `schools::selected` never returns an empty list — a malformed
        // override keeps the control rather than removing it — so this is a
        // guard against that guarantee being weakened later, not a case an
        // operator can reach.
        let (orchestrator_harness, system_prompt) = opening.ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation("no school was selected for this run".into())
        })?;

        let registry = Arc::new(default_registry(research_enabled)?);

        Ok(Self {
            inner: ObservedAgent::from_harness(orchestrator_harness)?.with_tracer(tracer.clone()),
            registry,
            system_prompt,
            subagents: async_subagents,
            schools,
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
        // Each school drains its own mailboxes, so each needs its own. One
        // shared mailbox would be emptied by whichever school asked first, and
        // the others would never see the report at all — `Mailbox::collect`
        // takes what is there and leaves nothing behind, which is right for one
        // reader and silently wrong for several.
        let mut lanes = Vec::new();
        for school in &self.schools {
            let library = solutions::Mailbox::default();
            let direction = solutions::Mailbox::default();
            let skeletons = solutions::Mailbox::default();
            lanes.push((
                *school,
                library.clone(),
                direction.clone(),
                skeletons.clone(),
            ));
        }

        // One set of standing teams for the whole run, not one per school.
        // Three librarians on one library is waste rather than diversity: what
        // differs between schools is how they attack the problem, and gathering
        // a source is the same job whoever asked for it. So the teams post once
        // and every school's mailbox receives it, and the directive queue keeps
        // its single consumer — the cursor is what makes delivery exactly-once,
        // and a second reader of the same file would break that rather than
        // share it.
        let libraries: Vec<solutions::Mailbox> =
            lanes.iter().map(|lane| lane.1.clone()).collect();
        let directions: Vec<solutions::Mailbox> =
            lanes.iter().map(|lane| lane.2.clone()).collect();
        let support = self.spawn_support_teams(problem, &libraries, &directions);

        let lanes: Vec<_> = lanes
            .into_iter()
            .map(|(school, library, direction, skeletons)| {
                let mailboxes = solutions::Mailboxes {
                    patterns: library.clone(),
                    directives: direction,
                    skeletons: skeletons.clone(),
                };
                let beside = solutions::Beside {
                    // The same mailbox the standing teams post to, and the same
                    // one the attempt drains. A literature sweep and a team
                    // report are both "what arrived beside the loop since the
                    // last attempt", so they are rendered under that one
                    // heading rather than two.
                    library,
                    reduction: solutions::Reduction {
                        outbox: skeletons,
                        // One gate per school rather than one per run. Its
                        // purpose is that two decompositions cannot be in
                        // flight writing the same skeleton, and within a school
                        // that is still exactly what it prevents. Across
                        // schools a shared gate would be worse than useless: it
                        // would make one school wait on another's reduction,
                        // which is the serialisation the schools exist to
                        // avoid.
                        gate: solutions::ReductionGate::default(),
                    },
                    teams: support.clone(),
                };
                (school, beside, mailboxes)
            })
            .collect();

        let outcome = self.run_schools(problem, lanes).await;

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

    /// Runs every selected school concurrently and reports what each reached.
    ///
    /// The schools share the workspace and the standing teams, and are
    /// otherwise independent: each drives its own loop, on its own thresholds,
    /// against its own copy of every role.
    ///
    /// **First verified solve wins, and there is no scheduler.** When one school
    /// reaches a genuine solve the others are asked to stand down, and the run
    /// reports its answer. `docs/tao-gap-analysis.md` is right that deciding to
    /// fund the branch that is *not* winning is a judgement this runtime cannot
    /// make well, so it does not try: the split is equal and fixed, and the only
    /// cross-school decision is the one that needs no judgement.
    ///
    /// Standing down is asked for rather than imposed. Aborting a task
    /// mid-attempt would drop it between a write and the ledger re-derivation
    /// that follows, so instead a flag is set, every school reads it at its own
    /// next pass boundary — beside `expired`, which exists for the same reason —
    /// and each ends its own loop tidily.
    async fn run_schools(
        &self,
        problem: &str,
        lanes: Vec<(schools::School, solutions::Beside, solutions::Mailboxes)>,
    ) -> Result<String> {
        let solved = Arc::new(std::sync::atomic::AtomicBool::new(false));
        let mut running = tokio::task::JoinSet::new();
        for (school, beside, mailboxes) in lanes {
            let lane = self.school_lane(problem, school, beside, mailboxes, &solved)?;
            running.spawn(lane);
        }
        let mut reached: Vec<(&'static str, String)> = Vec::new();
        let mut failure: Option<tinyagents::TinyAgentsError> = None;
        // Tracked rather than inferred from the reports. Deciding "did anything
        // work" by looking at the wording of the outcomes would make the run's
        // exit depend on prose the model influences.
        let mut any_finished = false;
        while let Some(finished) = running.join_next().await {
            match finished {
                Ok((slug, Ok(state))) => {
                    any_finished = true;
                    if state.solved {
                        solved.store(true, std::sync::atomic::Ordering::Relaxed);
                        self.tracer
                            .note(&format!("school {slug}: solved; the others stand down"));
                    }
                    reached.push((slug, state.outcome()));
                }
                Ok((slug, Err(error))) => {
                    // One school failing is a lesson about that school, not
                    // about the run: the others are still working and one of
                    // them may yet arrive. The error is kept only for the case
                    // where every school fails, which has nothing to report and
                    // must not read as a mathematical result.
                    self.tracer
                        .note(&format!("school {slug}: the loop failed: {error}"));
                    reached.push((slug, format!("the {slug} loop failed: {error}")));
                    failure.get_or_insert(error);
                }
                Err(error) => {
                    // The lane panicked or was cancelled. Nothing was returned,
                    // so there is no outcome to report for it and it must not
                    // count as a school that finished.
                    self.tracer
                        .note(&format!("a school ended abnormally: {error}"));
                }
            }
        }
        match failure {
            // Not one school completed its loop, so the run has no answer and
            // nothing to choose between. Returning the first failure is honest;
            // folding them into a summary would read as a run that concluded
            // something.
            Some(error) if !any_finished => Err(error),
            _ => Ok(combined_outcome(&reached)),
        }
    }

    /// Builds one school's whole run as a future that owns everything it needs.
    ///
    /// Owned rather than borrowing `self`, because the lanes are spawned onto
    /// the runtime and a borrow would tie every school's lifetime to this
    /// frame. Everything it captures is either an `Arc` or a cheap clone that
    /// shares its backing — the manager's semaphore and registry above all, so
    /// three schools compete for one concurrency cap rather than three.
    ///
    /// The report is built by rebuilding a `SolutionState` from the accumulator
    /// and calling the same `outcome` the state graph calls, rather than by
    /// describing the numbers here. That wording is written against specific
    /// ways a run can end — an answer with one route behind it must not be
    /// called solved, a provider failure must not read as a mathematical one —
    /// and a second version of it would get one of them wrong.
    fn school_lane(
        &self,
        problem: &str,
        school: schools::School,
        beside: solutions::Beside,
        mailboxes: solutions::Mailboxes,
        solved: &Arc<std::sync::atomic::AtomicBool>,
    ) -> Result<impl std::future::Future<Output = (&'static str, Result<solutions::SolutionState>)> + Send + use<>>
    {
        let graph = workflow::solution_loop_for(
            problem,
            self.workflow_agents(),
            &school.thresholds,
        );
        // Scoped only when more than one school is running, matching how they
        // were registered: a lone school registered unqualified, so a scoped
        // handle would resolve every role by falling back anyway.
        let subagents = if self.schools.len() > 1 {
            self.subagents.for_school(school.slug)
        } else {
            self.subagents.clone()
        };
        let steps = Arc::new(
            loop_steps::LoopSteps::new(
                subagents,
                Some(self.tracer.clone()),
                Some(self.workspace.clone()),
                self.memory.clone(),
                beside,
                mailboxes,
            )
            .in_school(school.slug, Arc::clone(solved)),
        ) as Arc<dyn Tool<()>>;
        let capabilities = self.workflow_capabilities([steps])?;
        let problem = problem.to_string();
        Ok(async move {
            (
                school.slug,
                run_compiled_loop(&graph, &capabilities, &problem).await,
            )
        })
    }
}

/// Everything every school's roster is built from.
///
/// Gathered into one value because it is the same for all of them: the model,
/// the budget, the workspace and the stores are the run's, and what a school
/// changes is only which prompts its roles are given. Passing nine arguments to
/// [`register_school`] once per school would say the opposite.
struct Roster<'a> {
    model: &'a Arc<dyn ChatModel<()>>,
    reasoning: &'a Arc<dyn ChatModel<()>>,
    budget: RunBudget,
    tracer: &'a Arc<RunTracer>,
    workspace: &'a PathBuf,
    documents: &'a WorkspaceDocuments,
    checkpoint: &'a Arc<dyn tinyagents::harness::middleware::Middleware<()>>,
    vector_store: &'a VectorStore,
    search: &'a SearchTools,
    /// Whether this run has more than one school, and so whether the roles
    /// holding `post_board` are told there is anybody to post to.
    siblings: bool,
}

/// Registers one school's copy of every role, and returns its orchestrator.
///
/// `subagents` is the school-scoped handle, which is what makes the names
/// qualified: `register("research", …)` here registers `research@<slug>`, and
/// every bench in this crate names roles bare, so an agent built from this
/// handle can only reach this school's copies. See
/// [`AsyncSubagentManager::for_school`].
fn register_school(
    subagents: &AsyncSubagentManager,
    school: &schools::School,
    parts: &Roster<'_>,
) -> Result<(AgentHarness<()>, String)> {
    let mut prompts = RolePrompts::for_school(parts.workspace, school, parts.siblings)?;

    let mut research_harness = build_research_harness(
        parts.model,
        parts.budget,
        parts.tracer,
        parts.documents,
        parts.vector_store,
        parts.search.clone(),
    );
    research_harness.push_middleware(parts.checkpoint.clone());
    subagents.register(
        "research",
        Arc::new(research_harness),
        std::mem::take(&mut prompts.research),
    )?;

    register_code_writing_agents(
        subagents,
        &CodeWriters {
            model: parts.model,
            budget: parts.budget,
            tracer: parts.tracer,
            workspace: parts.workspace,
            documents: parts.documents,
            checkpoint: parts.checkpoint,
            vector_store: parts.vector_store,
        },
        prompts.code_writers(),
    )?;

    register_support_agents(
        subagents,
        &SupportAgents {
            model: parts.model,
            reasoning: parts.reasoning,
            budget: parts.budget,
            tracer: parts.tracer,
            documents: parts.documents,
            vector_store: parts.vector_store.clone(),
            search: parts.search.clone(),
            workspace: parts.workspace.clone(),
            // Resolved through the scoped handle, so a pattern agent
            // delegating to `tool_builder` reaches its own school's.
            delegation: subagents.tools(PATTERN_DELEGATES),
            school: school.slug,
        },
        prompts.support(),
    )?;

    let orchestrator_harness = register_planners(
        subagents,
        &Planners {
            model: parts.model,
            budget: parts.budget,
            tracer: parts.tracer,
            documents: parts.documents,
            vector_store: parts.vector_store,
        },
        std::mem::take(&mut prompts.goals),
    )?;
    Ok((orchestrator_harness, prompts.orchestrator))
}

/// The run's report when more than one school worked the problem.
///
/// One school's outcome is returned unchanged, so a single-school run reports
/// exactly what it always did — the wording in
/// [`SolutionState::outcome`](solutions::SolutionState::outcome) is written
/// against specific ways a run can end and must not be wrapped in anything that
/// weakens it.
///
/// With several, every school is named, with the bet it was making, and
/// reported. That is the *"report how many distinct approaches a run actually
/// pursued"* that `docs/tao-proposals.md` asks for as the honest small version
/// of funding an orthogonal branch — except that here it is a by-product of the
/// run having actually pursued them, rather than a count of how often it did
/// not. The stance is carried because an outcome is only readable against what
/// the school was trying: "the goal did not move" is a failure for the chisel
/// and an ordinary week for the rising sea.
fn combined_outcome(reached: &[(&'static str, String)]) -> String {
    if let [(_, only)] = reached {
        return only.clone();
    }
    let mut out = String::from("Several schools worked this problem.\n");
    for (slug, outcome) in reached {
        let stance = schools::ALL
            .iter()
            .find(|school| school.slug == *slug)
            .map_or("", |school| school.stance);
        let _ = write!(out, "\n## {slug}\n\n_{stance}_\n\n{}\n", outcome.trim());
    }
    out
}

/// Compiles and runs one loop graph, and reports the state it ended in.
///
/// A free function rather than a method, so a lane can own it: the future a
/// school is spawned as must not borrow the orchestrator.
async fn run_compiled_loop(
    graph: &tinyflows::model::WorkflowGraph,
    capabilities: &tinyflows::caps::Capabilities,
    problem: &str,
) -> Result<solutions::SolutionState> {
    let compiled = tinyflows::compiler::compile(graph).map_err(|error| {
        tinyagents::TinyAgentsError::Graph(format!("the loop graph is invalid: {error}"))
    })?;
    let finished = tinyflows::engine::run(&compiled, serde_json::json!({}), capabilities)
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Graph(format!("the loop graph failed: {error}"))
        })?;
    let accumulator = finished
        .output
        .pointer(&format!("/nodes/{}/state", workflow::LOOP_NODE))
        .cloned()
        .unwrap_or(serde_json::Value::Null);
    // The judge runs on the way out, after the head has folded its last pass,
    // so its score is in its own output and not in the accumulator. Reading
    // only the accumulator would spend a whole agent run scoring the work and
    // then report a state that had never heard of it.
    let accumulator = finished
        .output
        .pointer(&format!("/nodes/{}/item/json", workflow::FINAL_JUDGE))
        .cloned()
        .unwrap_or(accumulator);
    Ok(solutions::SolutionState::from_accumulator(
        problem,
        &accumulator,
    ))
}

impl OrchestratorAgent {
    /// Starts the long-lived teams that work alongside the solution loop.
    ///
    /// Each gets its own budget and wall clock: `RunBudget` bounds a single
    /// agent run, and a team runs many, so a per-run bound says nothing about
    /// what the team as a whole costs. A team that exhausts its allowance stops
    /// and says so while the others carry on.
    ///
    /// One set of teams serves every school, so what a team finds is delivered
    /// to *all* of `patterns`, and a drained directive to all of `directives`.
    /// A single shared mailbox would not do: `Mailbox::collect` takes what is
    /// there and leaves nothing, so the first school to ask would consume a
    /// report meant for all of them, and the loss would be silent.
    fn spawn_support_teams(
        &self,
        problem: &str,
        patterns: &[solutions::Mailbox],
        directives: &[solutions::Mailbox],
    ) -> Vec<teams::TeamHandle> {
        let mut handles = Vec::new();
        // Scoped exactly as a lane's is, and for a reason that cost a live run
        // its whole steering channel. With two or more schools every role is
        // registered *only* school-qualified, so a bare `director` is unknown,
        // the gate below skipped all three standing teams, and it did so
        // silently: the run looked healthy, the librarian and pattern spend in
        // the trace came from the loop's own arms, and seven operator
        // directives sat unread behind a cursor that never moved for an hour.
        // One school's registration is the right handle because these teams
        // serve the whole run — the directive queue keeps its single consumer,
        // so the team must run as some one school rather than each.
        let subagents = match self.schools.split_first() {
            Some((first, rest)) if !rest.is_empty() => self.subagents.for_school(first.slug),
            _ => self.subagents.clone(),
        };
        for (name, agent, completion, budget, brief) in standing_teams() {
            if !subagents.knows(agent) {
                continue;
            }
            let subagents = subagents.clone();
            let workspace = self.workspace.clone();
            let outbox = patterns.to_vec();
            let direction = directives.to_vec();
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
                                    // Delivered to every school, not to the
                                    // first one that asks.
                                    for mailbox in &outbox {
                                        mailbox.post(reply.clone());
                                    }
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
