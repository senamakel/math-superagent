/// Assembles the research agent's harness: search the web, and remember what
/// it found.
/// What the two planning roles' harnesses are built from.
struct Planners<'a> {
    model: &'a Arc<dyn ChatModel<()>>,
    budget: RunBudget,
    tracer: &'a Arc<RunTracer>,
    documents: &'a WorkspaceDocuments,
    vector_store: &'a VectorStore,
}

/// Registers the goals agent and returns the orchestrator's harness.
///
/// They are built together because they are the same role at two depths: both
/// decompose a problem and delegate it, and both need the same way back into
/// what the run already knows. Splitting them meant the orchestrator quietly
/// had neither recall tool — it could read a path it already knew and nothing
/// else, and a planner that cannot find what has already been tried delegates
/// it again.
///
/// The difference between them is the bench. The goals agent sees the
/// specialists; the orchestrator additionally sees the roles the solution loop
/// drives, so a single-turn run can reach them.
///
/// # Errors
///
/// Returns an error when `goals` is already registered.
fn register_planners(
    subagents: &AsyncSubagentManager,
    parts: &Planners<'_>,
    goals_prompt: String,
) -> Result<AgentHarness<()>> {
    let goals = build_planner_harness(subagents, parts, "goals", SPECIALISTS);
    subagents.register("goals", Arc::new(goals), goals_prompt)?;
    Ok(build_planner_harness(
        subagents,
        parts,
        "orchestrator",
        DELEGATES,
    ))
}

/// Assembles one planner's harness: its delegation bench, the document tools,
/// and both ways back into what the run already knows.
fn build_planner_harness<const N: usize>(
    subagents: &AsyncSubagentManager,
    parts: &Planners<'_>,
    role: &'static str,
    bench: [&'static str; N],
) -> AgentHarness<()> {
    let mut harness = specialist_harness(parts.model.clone(), parts.budget, role, parts.tracer);
    for tool in subagents.tools(bench) {
        register_resilient(&mut harness, tool);
    }
    for tool in parts.documents.tools() {
        register_resilient(&mut harness, tool);
    }
    register_memory(&mut harness, parts.vector_store);
    // The goals agent drives an attempt and carries its half-finished
    // arithmetic between turns; the orchestrator delegates and has none.
    if role == "goals" {
        register_scratch(&mut harness, parts.vector_store, true);
    }
    harness
}

fn build_research_harness(
    model: &Arc<dyn ChatModel<()>>,
    budget: RunBudget,
    tracer: &Arc<RunTracer>,
    documents: &WorkspaceDocuments,
    vector_store: &VectorStore,
    search: SearchTools,
) -> AgentHarness<()> {
    let SearchTools { exa, oeis } = search;
    let mut harness = specialist_harness(model.clone(), budget, "research", tracer);
    for tool in exa.into_iter().chain(oeis) {
        register_resilient(&mut harness, tool);
    }
    register_memory(&mut harness, vector_store);
    for tool in documents.tools() {
        register_resilient(&mut harness, tool);
    }
    harness
}

/// What every code-writing role's harness is built from.
struct CodeWriters<'a> {
    model: &'a Arc<dyn ChatModel<()>>,
    budget: RunBudget,
    tracer: &'a Arc<RunTracer>,
    workspace: &'a Path,
    documents: &'a WorkspaceDocuments,
    checkpoint: &'a Arc<dyn tinyagents::harness::middleware::Middleware<()>>,
    /// The saved note store, so a role about to implement a result can check
    /// whether the run already established it.
    vector_store: &'a VectorStore,
}

/// Registers the roles carrying shell and file-write authority.
///
/// They differ in mandate rather than in tools. The tool-builder writes
/// experiments and toolkit helpers; the coder writes the implementation the run
/// stands behind; the SAT solver encodes a finite question rather than writing
/// a search for it; the Lean prover produces the one artifact in this runtime
/// that is not evidence but proof. Splitting them is what lets each prompt be
/// strict about one thing rather than one prompt hedging between four, and
/// their failure modes have nothing in common — a program that ran but is
/// wrong, an `UNKNOWN` reported as solved, a `sorry` left undeclared.
///
/// Building them from one list is what keeps the shared authority boundary
/// visible: a tool granted here reaches all four, which is a decision worth
/// seeing rather than one buried in four near-identical blocks.
///
/// There is exactly one exception, and it is written as a branch rather than a
/// second list so that it stays visible as an exception. `lean_check` reaches
/// `lean_prover` alone, because it is the only tool here whose result decides
/// what a *claim* may say: a `status: formalised` row is backed by a verdict
/// this tool filed, so granting it more widely would let a role with no
/// formalisation mandate mint the ledger's strongest evidence class. See
/// [`super::lean`].
///
/// # Errors
///
/// Returns an error when a name is already registered.
fn register_code_writing_agents(
    subagents: &AsyncSubagentManager,
    parts: &CodeWriters<'_>,
    roles: [(&str, String); 7],
) -> Result<()> {
    for (name, prompt) in roles {
        let mut harness = build_tool_builder_harness(
            parts.model,
            parts.budget,
            parts.tracer,
            parts.workspace,
            parts.documents,
        );
        if name == lean::LEAN_ROLE {
            register_resilient(
                &mut harness,
                Arc::new(lean::LeanCheck::new(
                    parts.workspace.to_path_buf(),
                    parts.budget.tool_timeout,
                )),
            );
        }
        harness.push_middleware(parts.checkpoint.clone());
        register_memory(&mut harness, parts.vector_store);
        register_scratch(&mut harness, parts.vector_store, true);
        subagents.register(name, Arc::new(harness), prompt)?;
    }
    Ok(())
}

/// Assembles the tool-builder's harness: the only role with shell and
/// file-write authority.
fn build_tool_builder_harness(
    model: &Arc<dyn ChatModel<()>>,
    budget: RunBudget,
    tracer: &Arc<RunTracer>,
    workspace: &Path,
    documents: &WorkspaceDocuments,
) -> AgentHarness<()> {
    let mut harness = specialist_harness(model.clone(), budget, "tool_builder", tracer);
    register_resilient(
        &mut harness,
        Arc::new(WriteToolFile::new(workspace.to_path_buf())),
    );
    register_resilient(
        &mut harness,
        Arc::new(ExecuteCommand::new(
            workspace.to_path_buf(),
            budget.tool_timeout,
        )),
    );
    for tool in documents.tools() {
        register_resilient(&mut harness, tool);
    }
    // Diff-shaped editing, for the role that actually writes code. A patch
    // changes a few lines instead of re-emitting the file, and carries a
    // change across several files in one atomic call — which is what keeps a
    // helper under `code/lib/` and its row in `code/lib/INDEX.md` from
    // drifting apart.
    register_resilient(&mut harness, patch::tool(documents.clone()));
    harness
}

/// The shared pieces every support agent's harness is assembled from.
struct SupportAgents<'a> {
    model: &'a Arc<dyn ChatModel<()>>,
    /// The stronger model, for the one support agent whose output is a
    /// judgement rather than a report. See [`crate::agent`]'s reasoning model.
    reasoning: &'a Arc<dyn ChatModel<()>>,
    budget: RunBudget,
    tracer: &'a Arc<RunTracer>,
    documents: &'a WorkspaceDocuments,
    vector_store: VectorStore,
    exa: Option<Arc<dyn Tool<()>>>,
    /// The OEIS adapter, empty when research is disabled.
    ///
    /// Held as a list rather than an option because a source adapter is one of
    /// a family: the shape a second one slots into is a list, and the shape it
    /// would have to rewrite is an option.
    oeis: Vec<Arc<dyn Tool<()>>>,
    /// The jail root, for the one support agent allowed to execute.
    workspace: PathBuf,
    /// Delegation tools, so the pattern agent can commission a computation.
    delegation: Vec<Arc<dyn Tool<()>>>,
}

impl SupportAgents<'_> {
    /// The model `role` runs on.
    ///
    /// One place decides it, so which roles are on the stronger model is a
    /// list to read rather than a property to reconstruct from five call
    /// sites. See [`REASONING_ROLES`].
    fn model_for(&self, role: &str) -> Arc<dyn ChatModel<()>> {
        if REASONING_ROLES.contains(&role) {
            self.reasoning.clone()
        } else {
            self.model.clone()
        }
    }
}

/// Role prompts for the four agents the solution loop adds.
struct SupportPrompts {
    reflection: String,
    judge: String,
    pattern: String,
    inventor: String,
    reducer: String,
    weakener: String,
    librarian: String,
    scholar: String,
    curator: String,
    director: String,
}

/// Registers the pattern agent, which is the tool-richest of the support roles.
///
/// Split out of [`register_support_agents`] because of that: it computes as
/// well as observes, so it carries shell authority, file-write authority,
/// delegation, and the one lookup it is allowed, and inlining all of it buried
/// the four other registrations beside it.
fn register_pattern_agent(
    subagents: &AsyncSubagentManager,
    parts: &SupportAgents<'_>,
    prompt: String,
) -> Result<()> {
    let mut pattern = specialist_harness(
        parts.model_for("pattern_finder"),
        parts.budget,
        "pattern_finder",
        parts.tracer,
    );
    for tool in PatternTool::all() {
        register_resilient(&mut pattern, tool);
    }
    for tool in parts.documents.tools() {
        register_resilient(&mut pattern, tool);
    }
    // The pattern agent computes as well as observes. Its own tools answer
    // only what holds across terms it is handed, so without a way to generate
    // more terms it can neither test a conjecture past the data that suggested
    // it nor find the first term that breaks one — which is the finding worth
    // having. It gets shell and file-write authority for that, and delegation
    // besides, so a check too large to run inline becomes a commissioned
    // program rather than an abandoned question.
    register_resilient(
        &mut pattern,
        Arc::new(WriteToolFile::new(parts.workspace.clone())),
    );
    register_resilient(
        &mut pattern,
        Arc::new(ExecuteCommand::new(
            parts.workspace.clone(),
            parts.budget.tool_timeout,
        )),
    );
    for tool in parts.delegation.iter().cloned() {
        register_resilient(&mut pattern, tool);
    }
    // The one search this role may have. It has no web search on purpose — a
    // bounded structural question must not turn into a second investigation —
    // and an encyclopedia lookup keyed on terms it has already computed cannot
    // become one: the terms either match a catalogued sequence or they do not.
    // It is also the role holding the terms, so making it ask another agent to
    // run the lookup would spend a child run to pass a list of integers along.
    for tool in parts.oeis.iter().cloned() {
        register_resilient(&mut pattern, tool);
    }
    register_memory(&mut pattern, &parts.vector_store);
    register_scratch(&mut pattern, &parts.vector_store, true);
    subagents.register("pattern_finder", Arc::new(pattern), prompt)
}

/// Registers the inventor, the one role that is neither the run's model nor the
/// run's turn cap.
///
/// Split out of [`register_support_agents`] for the reason the pattern agent
/// was: it differs from its neighbours in three ways at once — the reasoning
/// model, a widened turn budget, and a delegation bench — and inlining the
/// argument for each buried the registrations either side of it.
///
/// The turn cap is the recent one. A reasoning model asked for three lines of
/// attack with the mathematics named in each was being cut off at the run's
/// 12,000-token cap with no tool call to show for it, so the widened budget has
/// to reach both [`specialist_harness`], which sets how far a cut-off turn may
/// be re-issued, and the registration, which sets what the first attempt asks
/// for. See [`RunBudget::for_invention`].
fn register_inventor(
    subagents: &AsyncSubagentManager,
    parts: &SupportAgents<'_>,
    prompt: String,
) -> Result<()> {
    let budget = parts.budget.for_invention();
    let mut inventor = specialist_harness(
        parts.model_for("inventor"),
        budget,
        "inventor",
        parts.tracer,
    );
    if let Some(exa) = parts.exa.clone() {
        register_resilient(&mut inventor, exa);
    }
    for tool in parts.oeis.iter().cloned() {
        register_resilient(&mut inventor, tool);
    }
    for tool in parts.documents.tools() {
        register_resilient(&mut inventor, tool);
    }
    // The one delegation bench outside the two planners. See [`INVENTION_BENCH`]
    // for why the inventor has one and why it holds exactly one role.
    for tool in subagents.tools(INVENTION_BENCH) {
        register_resilient(&mut inventor, tool);
    }
    register_memory(&mut inventor, &parts.vector_store);
    subagents.register_with_turn_cap(
        "inventor",
        Arc::new(inventor),
        prompt,
        budget.max_turn_output_tokens,
    )
}

/// Registers the reducer, which reasons backward from the goal.
///
/// Split out of [`register_support_agents`] for the reason the inventor is: it
/// carries a widened turn cap and a deliberately narrow tool set, and the
/// argument for each belongs beside it rather than inlined between two other
/// registrations.
///
/// The turn cap is the inventor's, and the shape it exists for is the same. A
/// reasoning model asked for a decomposition *with the mathematics stated* —
/// the goal, the lemmas, and the inference combining them — is exactly the turn
/// that was being cut off at the run's 12,000-token cap with no tool call to
/// show for it. See [`RunBudget::for_invention`].
///
/// The tool set is the narrowest of any role that writes: the document tools
/// and the memory tools, and nothing else. Every exclusion is stated on the
/// registry definition; the one worth repeating here is that it has no
/// delegation bench, unlike the inventor. The inventor needs one because a new
/// line of attack has to be checked against something outside the run before it
/// is worth writing down. A skeleton is checked by the forward loop attacking
/// its gaps, which is the loop itself.
fn register_reducer(
    subagents: &AsyncSubagentManager,
    parts: &SupportAgents<'_>,
    prompt: String,
) -> Result<()> {
    let budget = parts.budget.for_invention();
    let mut reducer =
        specialist_harness(parts.model_for("reducer"), budget, "reducer", parts.tracer);
    for tool in parts.documents.tools() {
        register_resilient(&mut reducer, tool);
    }
    // All three memory tools. A discharged reduction — this conjecture reduces
    // to these lemmas, and here is the claim that closed each — is the most
    // durable thing this runtime produces about a problem, and a later run
    // re-deriving it is the most expensive way to learn it was known.
    register_memory(&mut reducer, &parts.vector_store);
    subagents.register_with_turn_cap(
        "reducer",
        Arc::new(reducer),
        prompt,
        budget.max_turn_output_tokens,
    )
}

/// Registers the weakener, which lowers the target rather than reaching it.
///
/// Assembled exactly as the reducer is, and that is the argument for it rather
/// than a coincidence: both take the goal and produce a document about what to
/// attack instead of attacking anything, so both need a widened turn for the
/// mathematics and neither may compute. Where they differ is only in what the
/// document says — lemmas that would imply the goal, against targets that
/// deliberately would not.
///
/// It holds all three memory tools for the reducer's reason, and the reason is
/// if anything stronger here. A ladder of weakened versions of a famous problem,
/// with the difficulty that defeats each rung named beside it, is a durable fact
/// about the *problem* rather than about this run's approach to it: it survives
/// the method that produced it, and a later run rebuilding it pays the full cost
/// of rediscovering where the difficulty lives.
fn register_weakener(
    subagents: &AsyncSubagentManager,
    parts: &SupportAgents<'_>,
    prompt: String,
) -> Result<()> {
    let budget = parts.budget.for_invention();
    let mut weakener = specialist_harness(
        parts.model_for("weakener"),
        budget,
        "weakener",
        parts.tracer,
    );
    for tool in parts.documents.tools() {
        register_resilient(&mut weakener, tool);
    }
    register_memory(&mut weakener, &parts.vector_store);
    subagents.register_with_turn_cap(
        "weakener",
        Arc::new(weakener),
        prompt,
        budget.max_turn_output_tokens,
    )
}

/// Registers the reflection, pattern, inventor, reducer, and librarian agents.
///
/// Each gets only the tools its role needs: reflection has no research or
/// execution tools at all, so it cannot drift into solving the problem it is
/// supposed to be judging.
fn register_support_agents(
    subagents: &AsyncSubagentManager,
    parts: &SupportAgents<'_>,
    prompts: SupportPrompts,
) -> Result<()> {
    let mut reflection = specialist_harness(
        parts.model_for("reflection"),
        parts.budget,
        "reflection",
        parts.tracer,
    );
    for tool in parts.documents.tools() {
        register_resilient(&mut reflection, tool);
    }
    register_memory(&mut reflection, &parts.vector_store);
    subagents.register("reflection", Arc::new(reflection), prompts.reflection)?;

    // The judge is as tool-poor as reflection, and for the same reason: a
    // judge that can start solving stops judging. It reads the workspace only
    // to check a claim in the report against what is on disk.
    let mut judge = specialist_harness(
        parts.model_for("judge"),
        parts.budget.for_judging(),
        "judge",
        parts.tracer,
    );
    for tool in parts.documents.tools() {
        register_resilient(&mut judge, tool);
    }
    // No `register_memory` here, and that is the boundary rather than an
    // omission: recall is the invitation to investigate, and the judge is the
    // one role whose budget cannot absorb it.
    subagents.register("judge", Arc::new(judge), prompts.judge)?;

    register_pattern_agent(subagents, parts, prompts.pattern)?;

    register_inventor(subagents, parts, prompts.inventor)?;

    register_reducer(subagents, parts, prompts.reducer)?;
    register_weakener(subagents, parts, prompts.weakener)?;

    let mut librarian = specialist_harness(
        parts.model_for("librarian"),
        parts.budget,
        "librarian",
        parts.tracer,
    );
    if let Some(exa) = parts.exa.clone() {
        register_resilient(&mut librarian, exa);
    }
    for tool in parts.oeis.iter().cloned() {
        register_resilient(&mut librarian, tool);
    }
    for tool in parts.documents.tools() {
        register_resilient(&mut librarian, tool);
    }
    register_memory(&mut librarian, &parts.vector_store);
    subagents.register("librarian", Arc::new(librarian), prompts.librarian)?;

    // The scholar reads; it does not fetch. Withholding `exa_search` is what
    // keeps it digesting the library the run already has instead of drifting
    // into another search, which is the librarian's job and already done.
    let mut scholar = specialist_harness(
        parts.model_for("scholar"),
        parts.budget,
        "scholar",
        parts.tracer,
    );
    for tool in parts.documents.tools() {
        register_resilient(&mut scholar, tool);
    }
    register_memory(&mut scholar, &parts.vector_store);
    // Reads what the solve is in the middle of, so a paper can be judged
    // against the derivation it might settle. It produces no provisional work
    // of its own.
    register_scratch(&mut scholar, &parts.vector_store, false);
    subagents.register("scholar", Arc::new(scholar), prompts.scholar)?;

    // The curator reads far more of memory than it writes: `recall_memory` and
    // `relate_memory` are most of its job, because what an earlier run
    // established about this problem is invisible to this one until somebody
    // carries it into the file every role is sent. It keeps the write half on
    // the same boundary as every other role, and its prompt is what keeps that
    // honest — what it has to record is a contradiction between recalled
    // memory and this run's results, which is durable and which nothing else
    // is placed to notice, and not its own synthesis, which would be the run
    // citing itself.
    // Narrowed for the same reason housekeeping was, and on the evidence of
    // the same failure. Curating is bounded work — read what changed, rewrite
    // one file — and a role left with an investigation's budget investigates.
    // A live Erdős–Gyárfás run had the curator as its largest consumer at 55
    // model calls against `tool_builder`'s 38, growing five times faster than
    // the role actually doing the mathematics, and spending 69 `read_document`
    // calls walking `code/` and `research/` file by file.
    //
    // Rate was already bounded and was not enough. `TeamBudget::paced` floors
    // the interval between cycle *starts*, so throttling it to fifteen minutes
    // left one cycle in three minutes — still the top consumer, because that
    // single cycle cost eleven model calls. Frequency and length are separate
    // axes and both need a bound; this is the second one.
    let mut curator = specialist_harness(
        parts.model_for("context_curator"),
        parts.budget.for_housekeeping(),
        "context_curator",
        parts.tracer,
    );
    for tool in parts.documents.tools() {
        register_resilient(&mut curator, tool);
    }
    register_memory(&mut curator, &parts.vector_store);
    register_scratch(&mut curator, &parts.vector_store, false);
    subagents.register("context_curator", Arc::new(curator), prompts.curator)?;

    // Housekeeping's budget, for the same reason the curator has it: acting on
    // a directive is bounded work — read what the run is doing, rewrite the
    // files that say so — and a role left with an investigation's allowance
    // investigates. The bound matters more here than there, because this role
    // is woken by a person rather than by a schedule, and a directive that
    // turned into eleven model calls of its own would make asking for
    // something the most expensive thing an operator can do.
    let mut director = specialist_harness(
        parts.model_for("director"),
        parts.budget.for_housekeeping(),
        "director",
        parts.tracer,
    );
    for tool in parts.documents.tools() {
        register_resilient(&mut director, tool);
    }
    register_memory(&mut director, &parts.vector_store);
    register_scratch(&mut director, &parts.vector_store, false);
    subagents.register("director", Arc::new(director), prompts.director)?;

    Ok(())
}
