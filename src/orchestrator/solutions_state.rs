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
pub(super) struct Mailboxes {
    /// What the pattern team found, drained by the attempt and the reflection.
    pub(super) patterns: Mailbox,
    /// What a person asked for, drained by the attempt alone.
    pub(super) directives: Mailbox,
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
    state: SolutionState,
) -> Result<SolutionState> {
    let Mailboxes {
        patterns,
        directives,
    } = mailboxes;
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
    let diversify_agents = subagents.clone();
    let diversify_tracer = tracer;
    let attempt_mailbox = patterns.clone();
    let pattern_mailbox = patterns;
    let attempt_directives = directives;
    let reflect_teams = teams;

    let graph = GraphBuilder::<SolutionState, SolutionState>::overwrite()
        .add_node("attempt", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = attempt_agents.clone();
            let tracer = attempt_tracer.clone();
            let workspace = attempt_workspace.clone();
            let mailbox = attempt_mailbox.clone();
            let directives = attempt_directives.clone();
            async move {
                Ok(NodeResult::Update(
                    attempt_step(
                        &subagents,
                        tracer.as_ref(),
                        workspace.as_deref(),
                        &mailbox,
                        &directives,
                        state,
                    )
                    .await,
                ))
            }
        })
        .add_node("judge", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = judge_agents.clone();
            let tracer = judge_tracer.clone();
            let workspace = judge_workspace.clone();
            async move {
                Ok(NodeResult::Update(
                    judge_step(&subagents, tracer.as_ref(), workspace.as_deref(), state).await,
                ))
            }
        })
        .add_node("reflect", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = reflect_agents.clone();
            let mailbox = pattern_mailbox.clone();
            let teams = reflect_teams.clone();
            let tracer = reflect_tracer.clone();
            let workspace = reflect_workspace.clone();
            let memory = reflect_memory.clone();
            async move {
                Ok(NodeResult::Update(
                    reflect_step(
                        &subagents,
                        tracer.as_ref(),
                        workspace.as_deref(),
                        &memory,
                        &mailbox,
                        &teams,
                        state,
                    )
                    .await,
                ))
            }
        })
        .add_node(
            "diversify",
            move |state: SolutionState, _ctx: NodeContext| {
                let subagents = diversify_agents.clone();
                let tracer = diversify_tracer.clone();
                let workspace = diversify_workspace.clone();
                async move {
                    Ok(NodeResult::Update(
                        diversify_step(&subagents, tracer.as_ref(), workspace.as_deref(), state)
                            .await,
                    ))
                }
            },
        )
        .add_node(
            "done",
            |state: SolutionState, _ctx: NodeContext| async move { Ok(NodeResult::Update(state)) },
        );
    let graph = wire_routes(graph).compile()?;

    Ok(graph.run(state).await?.state)
}

/// Connects the loop's nodes, separately from building them.
///
/// The routing is the part of this design most likely to be wrong, so it is
/// worth reading in one piece rather than at the tail of the wiring.
fn wire_routes(
    builder: GraphBuilder<SolutionState, SolutionState>,
) -> GraphBuilder<SolutionState, SolutionState> {
    builder
        .set_entry("attempt")
        .add_edge("attempt", "judge")
        .add_conditional_edges(
            "judge",
            judged_route,
            [(Judged::Reflect, "reflect"), (Judged::Restart, "attempt")],
        )
        .add_conditional_edges(
            "reflect",
            route,
            [
                (Route::Solved, "done"),
                // Terminal too. The run has an answer and has twice said it
                // cannot build a second route to it; further attempts re-derive
                // what is already on disk.
                (Route::Reported, "done"),
                (Route::Retry, "attempt"),
                (Route::Diversify, "diversify"),
                // Same terminal node as a finished run. The loop stops rather
                // than diversifying, because diversification is three more
                // child runs into the same refusal.
                (Route::Blocked, "done"),
            ],
        )
        .add_edge("diversify", "attempt")
        .set_finish("done")
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
