/// Joins the labelled sections that have content into one briefing.
///
/// Empty sections are dropped rather than rendered as a heading with nothing
/// under it: a child asked to act on "Research:\n\n" reasonably concludes the
/// research found nothing, which is a different claim from its not having run.
fn merge_context(sections: &[(&str, &str)]) -> String {
    let mut merged = String::new();
    for (label, body) in sections {
        if body.trim().is_empty() {
            continue;
        }
        if !merged.is_empty() {
            merged.push_str("\n\n");
        }
        let _ = write!(merged, "{label}:\n{}", body.trim());
    }
    merged
}

/// Where something working outside the loop leaves text for a later attempt.
///
/// The pattern agent used to be awaited beside the reflection, and that made
/// it a gate on the whole loop: a live run sat 33 minutes unable to start its
/// next attempt because the pattern agent it had already collected a verdict
/// beside was still working. Nothing bounds a pattern run against the loop —
/// it has its own budget of hundreds of model calls — so the gate had no
/// ceiling.
///
/// Detaching it is safe precisely because nothing in the routing decision
/// reads it: `route` turns on the reflection's verdict alone. So the run is
/// spawned, the loop proceeds on the reflection, and whatever the pattern
/// agent finds is posted here and picked up by the next attempt that asks. A
/// structural observation is worth as much one attempt later; a stalled loop
/// is not.
///
/// Human direction arrives the same way and for a stronger version of the same
/// reason. A person is slower than any support agent, so a loop that waited on
/// one would be that 33-minute gate with no bound at all. Two mailboxes are
/// therefore built from this one type — one carrying what the pattern team
/// found, one carrying what an operator asked for — and they differ only in
/// the heading their contents are rendered under.
#[derive(Clone, Default)]
pub(super) struct Mailbox(Arc<std::sync::Mutex<Vec<String>>>);

impl Mailbox {
    /// Leaves a finished report for the next attempt.
    pub(super) fn post(&self, report: String) {
        if report.trim().is_empty() {
            return;
        }
        if let Ok(mut slot) = self.0.lock() {
            slot.push(report);
        }
    }

    /// Takes every report that has arrived since the last collection.
    ///
    /// More than one can be waiting when a pattern run outlives the attempt
    /// that started it, which is the normal case now that they are detached.
    pub(super) fn collect(&self) -> String {
        let Ok(mut slot) = self.0.lock() else {
            return String::new();
        };
        let reports = std::mem::take(&mut *slot);
        reports.join("\n\n")
    }
}

/// What the loop is handed by the work running beside it.
///
/// Grouped rather than passed as two more parameters, because they are one
/// idea: everything that reaches an attempt without the loop having asked for
/// it arrives through a mailbox, and a third one — a second kind of team, an
/// operator channel that is not text — belongs in here rather than in `run`'s
/// signature.
#[derive(Clone)]
pub(super) struct Mailboxes {
    /// What the pattern team found, drained by the attempt and the reflection.
    pub(super) patterns: Mailbox,
    /// What a person asked for, drained by the attempt alone.
    pub(super) directives: Mailbox,
    /// The lemmas that would suffice to prove the goal, drained by the attempt
    /// alone.
    ///
    /// The third one this struct's own doc anticipated. It carries open gaps
    /// rather than prose, and it is separate from `patterns` for the reason
    /// `directives` is: a target and a piece of gathered material are different
    /// kinds of thing, and one mailbox cannot render both under the right
    /// heading.
    pub(super) skeletons: Mailbox,
}

/// Builds and runs the solution loop over the registered specialists.
///
/// # Errors
///
/// Returns an error only when the graph itself cannot be compiled or executed;
/// a failing child agent is folded into the state as a lesson instead.
pub(super) async fn run(
    subagents: AsyncSubagentManager,
    tracer: Option<Arc<RunTracer>>,
    workspace: Option<PathBuf>,
    memory: VectorStore,
    teams: Vec<TeamHandle>,
    mailboxes: Mailboxes,
    mut state: SolutionState,
) -> Result<SolutionState> {
    let attempt_agents = subagents.clone();
    let attempt_tracer = tracer.clone();
    let judge_agents = subagents.clone();
    let judge_tracer = tracer.clone();
    let reflect_agents = subagents.clone();
    let reflect_tracer = tracer.clone();
    let attempt_workspace = workspace.clone();
    let reflect_workspace = workspace.clone();
    let judge_workspace = workspace.clone();
    let diversify_workspace = workspace;
    let reflect_memory = memory;
    let diversify_tracer = tracer;
    // Assembled once. The gate in it is the run's only one, so a reduction that
    // outlives the cycle that opened it cannot be joined by a second one
    // writing the same file.
    let beside = Beside {
        patterns: mailboxes.patterns.clone(),
        reduction: Reduction {
            outbox: mailboxes.skeletons.clone(),
            gate: ReductionGate::default(),
        },
        teams,
    };
    let attempt_mailboxes = mailboxes;
    open_initial_reduction(
        &subagents,
        diversify_tracer.as_ref(),
        diversify_workspace.as_deref(),
        &beside.reduction,
        &mut state,
    );

    let library_agents = subagents.clone();
    let pattern_agents = subagents.clone();
    let invention_agents = subagents;
    let invention_workspace = diversify_workspace.clone();

    let graph = GraphBuilder::<SolutionState, LoopUpdate>::new()
        .set_reducer(ClosureStateReducer::new(reduce))
        // Without this the runtime runs one node at a time, and the three
        // diversify arms would take turns rather than run together.
        .with_parallel(true)
        .add_node("attempt", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = attempt_agents.clone();
            let tracer = attempt_tracer.clone();
            let workspace = attempt_workspace.clone();
            let mailboxes = attempt_mailboxes.clone();
            async move {
                Ok(NodeResult::Update(LoopUpdate::whole(
                    attempt_step(
                        &subagents,
                        tracer.as_ref(),
                        workspace.as_deref(),
                        &mailboxes,
                        state,
                    )
                    .await,
                )))
            }
        })
        .add_node("judge", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = judge_agents.clone();
            let tracer = judge_tracer.clone();
            let workspace = judge_workspace.clone();
            async move {
                Ok(NodeResult::Update(LoopUpdate::whole(
                    judge_step(&subagents, tracer.as_ref(), workspace.as_deref(), state).await,
                )))
            }
        })
        .add_node("reflect", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = reflect_agents.clone();
            let beside = beside.clone();
            let tracer = reflect_tracer.clone();
            let workspace = reflect_workspace.clone();
            let memory = reflect_memory.clone();
            async move {
                Ok(NodeResult::Update(LoopUpdate::whole(
                    reflect_step(
                        &subagents,
                        tracer.as_ref(),
                        workspace.as_deref(),
                        &memory,
                        &beside,
                        state,
                    )
                    .await,
                )))
            }
        })
        .add_node(
            "diversify",
            move |_state: SolutionState, _ctx: NodeContext| {
                let tracer = diversify_tracer.clone();
                async move { Ok(diversify_open(tracer.as_ref())) }
            },
        )
        .add_node(
            "diversify_library",
            move |state: SolutionState, _ctx: NodeContext| {
                let subagents = library_agents.clone();
                async move { Ok(diversify_library_arm(&subagents, &state).await) }
            },
        )
        .add_node(
            "diversify_patterns",
            move |state: SolutionState, _ctx: NodeContext| {
                let subagents = pattern_agents.clone();
                async move { Ok(diversify_pattern_arm(&subagents, &state).await) }
            },
        )
        .add_node(
            "diversify_invention",
            move |state: SolutionState, _ctx: NodeContext| {
                let subagents = invention_agents.clone();
                let workspace = invention_workspace.clone();
                async move {
                    Ok(diversify_invention_arm(&subagents, workspace.as_deref(), &state).await)
                }
            },
        )
        .add_node(
            DIVERSIFY_MERGE,
            |state: SolutionState, _ctx: NodeContext| async move {
                Ok(NodeResult::Update(LoopUpdate::whole(diversify_merge(
                    state,
                ))))
            },
        )
        .add_node(
            "done",
            |state: SolutionState, _ctx: NodeContext| async move {
                Ok(NodeResult::Update(LoopUpdate::whole(state)))
            },
        );
    let graph = wire_routes(graph).compile().map_err(from_graph)?;

    Ok(graph.run(state).await.map_err(from_graph)?.state)
}

/// Decomposes the goal beside the first attempt, before any cycle completes.
///
/// The cadence in [`open_reduction`] counts completed cycles, which made the
/// earliest possible skeleton arrive after a full attempt/judge/reflect pass —
/// on a conjecture run, the better part of an hour during which every role
/// works without a statement of what would be enough. Nothing justifies that
/// wait: the reducer works backward from the problem statement, so its input is
/// present before the run starts, and the arm is detached, so opening it here
/// delays the graph by nothing.
///
/// It goes through the same gate as every later reduction, so the first
/// completed cycle cannot open a second one on top of this one, and a workspace
/// resumed mid-investigation is decomposed from what is already on disk rather
/// than from the statement alone.
fn open_initial_reduction(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    reduction: &Reduction,
    state: &mut SolutionState,
) {
    open_reduction(subagents, tracer, workspace, reduction, state);
}

/// The node the loop starts at.
pub(super) const ENTRY: &str = "attempt";

/// The node the loop ends at.
pub(super) const FINISH: &str = "done";

/// The edges that always fire, as `(from, to)`.
///
/// `diversify` is deliberately absent: it fans out with a [`Command`] rather
/// than a static edge, because the builder holds one static successor per node
/// and a fan-out needs three. Its destinations are declared in
/// [`DIVERSIFY_ARMS`] and wired below.
pub(super) const DIRECT_EDGES: [(&str, &str); 2] =
    [("attempt", "judge"), (DIVERSIFY_MERGE, "attempt")];

/// Where the judge sends the run, as `(verdict, node)`.
pub(super) const JUDGE_ROUTES: [(Judged, &str); 2] =
    [(Judged::Reflect, "reflect"), (Judged::Restart, "attempt")];

/// Where the reflection sends the run, as `(verdict, node)`.
pub(super) const REFLECT_ROUTES: [(Route, &str); 5] = [
    (Route::Solved, "done"),
    // Terminal too. The run has an answer and has twice said it cannot build a
    // second route to it; further attempts re-derive what is already on disk.
    (Route::Reported, "done"),
    (Route::Retry, "attempt"),
    (Route::Diversify, "diversify"),
    // Same terminal node as a finished run. The loop stops rather than
    // diversifying, because diversification is three more child runs into the
    // same refusal.
    (Route::Blocked, "done"),
];

/// Connects the loop's nodes, separately from building them.
///
/// The routing is the part of this design most likely to be wrong, so it is
/// worth reading in one piece rather than at the tail of the wiring.
///
/// The edges are the constants above rather than literals here, because
/// `super::diagram` renders the same loop and a diagram that describes the
/// wiring separately is a diagram that goes quietly out of date. Reading both
/// from one table means a rendered picture cannot disagree with what runs.
fn wire_routes(
    builder: GraphBuilder<SolutionState, LoopUpdate>,
) -> GraphBuilder<SolutionState, LoopUpdate> {
    let mut builder = builder
        .set_entry(ENTRY)
        .add_conditional_edges("judge", judged_route, JUDGE_ROUTES)
        .add_conditional_edges("reflect", route, REFLECT_ROUTES)
        // Declared unconditional because it is: `diversify` runs every arm
        // every time. The barrier below relies on that promise — a node that
        // *chose* between arms would leave the merge waiting on one that never
        // runs, and the runtime cannot tell the two apart without being told.
        .with_unconditional_fanout("diversify", DIVERSIFY_ARMS);
    for arm in DIVERSIFY_ARMS {
        // A waiting edge rather than a plain one: the merge activates once
        // *every* registered predecessor has finished, which is what makes it a
        // join rather than three separate arrivals each starting an attempt.
        builder = builder.add_waiting_edge(arm, DIVERSIFY_MERGE);
    }
    for (from, to) in DIRECT_EDGES {
        builder = builder.add_edge(from, to);
    }
    builder.set_finish(FINISH)
}

/// Pulls the `LESSON:` line out of a reflection, falling back to the whole text.
fn extract_lesson(reflection: &str) -> String {
    for line in reflection.lines() {
        let trimmed = line.trim();
        if let Some(rest) = trimmed
            .strip_prefix("LESSON:")
            .or_else(|| trimmed.strip_prefix("lesson:"))
        {
            let lesson = rest.trim();
            if !lesson.is_empty() {
                return lesson.to_string();
            }
        }
    }
    let condensed = reflection.trim();
    if condensed.is_empty() {
        "The reflection step returned nothing usable.".to_string()
    } else {
        condensed.chars().take(400).collect()
    }
}
