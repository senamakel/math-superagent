/// Builds the tools that reach outside the run, or nothing when research is off.
///
/// Both are withheld by not registering them rather than by asking the model
/// to abstain, because a prompt instruction is not a control. The encyclopedia
/// is gated with the web search and for the same reason: a self-contained
/// problem should test the runtime's reasoning rather than its ability to look
/// an answer up, and a catalogued sequence is the lookup most likely to hand a
/// run its closed form outright.
///
/// On a calibration run, `screen` wraps every one of them. That happens here,
/// at construction, rather than at registration, because these same `Arc`s are
/// handed to `caps::tools::WorkspaceTools` for the workflow path, which has no
/// harness and no middleware stack in between. Wrapping the value means both
/// paths carry the same screened object and there is no second place to
/// remember. `None` leaves them untouched, which is every ordinary run.
///
/// # Errors
///
/// Returns an error when the search key is missing while research is enabled.
fn search_tools(
    research_enabled: bool,
    documents: &WorkspaceDocuments,
    screen: Option<&screen::Screen>,
) -> Result<SearchTools> {
    if !research_enabled {
        return Ok(SearchTools::default());
    }
    Ok(SearchTools {
        exa: Some(screen::wrap_one(
            screen,
            Arc::new(ExaSearchTool::from_env()?) as Arc<dyn Tool<()>>,
        )),
        oeis: screen::wrap_all(screen, oeis::OeisTool::all(documents)),
        discovery: screen::wrap_all(
            screen,
            openalex::CitationGraphTool::all(documents)
                .into_iter()
                .chain(exa::tools(research_enabled, documents)?),
        ),
    })
}

/// The tools that reach outside the run, gathered so the research gate is one
/// decision rather than one per source.
#[derive(Clone, Default)]
struct SearchTools {
    /// General web search, absent when research is disabled.
    exa: Option<Arc<dyn Tool<()>>>,
    /// Source adapters. A list because a second one slots into a list and
    /// would have to rewrite an option.
    ///
    /// This one reaches the OEIS and nothing else, and it is deliberately the
    /// *narrow* list: it is registered into `pattern_finder` and `inventor`,
    /// which have no web search on purpose. A tool that reaches the open web
    /// must not be added here, because the registry says those roles cannot
    /// search and the harness is what actually decides.
    oeis: Vec<Arc<dyn Tool<()>>>,
    /// The ways onto the web that are not a query.
    ///
    /// Separate from [`Self::oeis`] because the two have different audiences,
    /// and a list is where that distinction is enforced rather than described:
    /// these go only to the roles the registry grants [`DISCOVERY_TOOLS`] to.
    /// Folding them into the adapters would have handed `pattern_finder` a deep
    /// research agent while the comment above its registration still read "the
    /// one search this role may have".
    discovery: Vec<Arc<dyn Tool<()>>>,
}

impl std::fmt::Debug for SearchTools {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("SearchTools")
            .field("exa", &self.exa.is_some())
            .field("oeis", &self.oeis.len())
            .field("discovery", &self.discovery.len())
            .finish()
    }
}

/// The ways onto the web that are not a query.
///
/// Grouped because they answer the questions a query cannot, and a role that
/// has one and not the others is a role that will fall back to rephrasing:
/// `citation_graph` asks what a paper's own author thought was load-bearing,
/// `find_similar_sources` uses a page rather than a phrase as the query,
/// `read_sources` reads twenty candidates without storing any of them, and
/// `deep_research` hands over a question the run cannot decompose into queries
/// itself.
///
/// All four reach the open web, so all four are withheld with `exa_search`
/// when research is off — by not being granted, not by being told to abstain.
const DISCOVERY_TOOLS: [&str; 4] = [
    "citation_graph",
    "find_similar_sources",
    "read_sources",
    "deep_research",
];

fn default_registry(research_enabled: bool) -> Result<AgentRegistry> {
    let document_tools = [
        "download_document",
        "read_document",
        "write_document",
        "edit_document",
        "index_document",
        "search_documents",
        "list_workspace",
        "describe_file",
        "refresh_index",
        // Derived from the library rather than written into it, and available
        // wherever the document tools are: the role that needs to know what
        // the run establishes, or that walks into a gap, is whichever one is
        // working.
        "search_claims",
        "request_research",
    ];
    // Every reasoning role's two ways back into what is already known: this
    // workspace's own record, and the note store that outlives it. They are
    // listed together because a caller deciding who to delegate to is asking
    // one question — can this role find out what the run already has.
    let memory_tools = ["recall_memory", "remember_memory", "relate_memory"];
    let mut registry = AgentRegistry::new();
    registry.register(
        AgentDefinition::new(
            "research",
            "Research Agent",
            if research_enabled {
                "Uses Exa to research current facts and return cited evidence."
            } else {
                "Web search is disabled this run; recalls and records saved notes only."
            },
        )
        .with_model("openrouter")
        .with_tools(
            research_enabled
                .then_some("exa_search")
                .into_iter()
                .chain(research_enabled.then_some("oeis_lookup"))
                .chain(research_enabled.then_some(DISCOVERY_TOOLS).into_iter().flatten())
                .chain(memory_tools)
                .chain(document_tools),
        ),
    )?;
    // The four roles carrying shell and file-write authority. They differ in
    // mandate rather than in tools, so listing them together is what makes the
    // fact that they share an authority boundary visible rather than buried in
    // four near-identical blocks.
    for (name, title, description) in [
        (
            "tool_builder",
            "Tool Builder Agent",
            "Writes and executes tools in the jailed /workspace directory.",
        ),
        (
            "coder",
            "Coding Agent",
            "Implements the solution program from an established result, and verifies it \
             against the oracle.",
        ),
        (
            "sat_solver",
            "Constraint Solving Agent",
            "Encodes a finite decision or optimisation problem for CP-SAT, SAT, or MILP, and \
             validates the model it gets back. A statement over a theory rather than a finite \
             encoding belongs to smt_solver.",
        ),
        (
            "smt_solver",
            "SMT Solving Agent",
            "Settles statements over arithmetic, arrays, and uninterpreted functions with Z3 \
             and cvc5, proving a universal claim by refuting its negation.",
        ),
        (
            "theorem_prover",
            "Automated Theorem Proving Agent",
            "Proves first-order statements from stated axioms with a saturation prover, and \
             reports which axioms the proof actually used.",
        ),
        (
            "symbolic_math",
            "Symbolic Mathematics Agent",
            "Derives and verifies closed forms, summations, recurrences, and exact algebra \
             with sympy, PARI/GP, and Singular.",
        ),
        (
            "lean_prover",
            "Lean Formalisation Agent",
            "Writes Lean 4 statements and proofs against Mathlib, and reports what the kernel \
             actually checked.",
        ),
    ] {
        registry.register(
            AgentDefinition::new(name, title, description)
                .with_model("openrouter")
                .with_tools(
                    ["write_tool_file", "execute_command", "apply_patch"]
                        .into_iter()
                        .chain(memory_tools)
                        .chain(SCRATCH_TOOLS)
                        .chain(document_tools),
                ),
        )?;
    }
    for definition in support_agents(research_enabled, document_tools, memory_tools) {
        registry.register(definition)?;
    }
    Ok(registry)
}

/// Returns the judge, reflection, pattern, curator, director, inventor, and
/// reducer definitions, plus the library roles.
///
/// Split out of [`default_registry`] to keep each function readable; these are
/// the agents the solution loop adds on top of the original three.
fn support_agents(
    research_enabled: bool,
    document_tools: [&'static str; 11],
    memory_tools: [&'static str; 3],
) -> Vec<AgentDefinition> {
    vec![
        // One tool: read a file. The judge answers four lines on twelve model
        // calls against an attempt that took the better part of an hour, and
        // every way of looking things up is an invitation to spend them
        // looking things up — a live judge already did exactly that with the
        // document tools alone. Recall is granted broadly and this is one of
        // the three roles it is withheld from, alongside the organizer and the
        // scratch's exclusions.
        AgentDefinition::new(
            "judge",
            "Judge",
            "Scores how an attempt was conducted and decides whether the run must start over.",
        )
        .with_model("openrouter")
        .with_tools([document_tools[1]]),
        AgentDefinition::new(
            "reflection",
            "Reflection Agent",
            "Judges one attempt, extracts the lesson, and decides whether it is really done.",
        )
        .with_model("openrouter")
        .with_tools(memory_tools.into_iter().chain(document_tools)),
        AgentDefinition::new(
            "pattern_finder",
            "Pattern Recognition Agent",
            "Finds exact structure in computed results: recurrences, polynomial degree, \
             periodicity, and common divisors.",
        )
        .with_model("openrouter")
        .with_tools(
            [
                "analyze_sequence",
                "find_linear_recurrence",
                // The one lookup whose query is not a phrasing problem: terms
                // it has computed either match a catalogued sequence or they
                // do not, so it cannot turn a bounded structural question into
                // a second investigation.
                "oeis_lookup",
                // It tests conjectures by computing more terms, so it needs to
                // write and run a program like any other worker.
                "write_tool_file",
                "execute_command",
                // A check too large to run inline becomes a commissioned
                // program rather than an abandoned question.
                "spawn_agent",
                "await_agent",
            ]
            .into_iter()
            .chain(memory_tools)
            .chain(SCRATCH_TOOLS)
            .chain(document_tools),
        ),
        // Reads widely and writes one file. It has no shell, no web search,
        // and no delegation on purpose: every one of those is a way for
        // curating what the run knows to turn into another investigation
        // beside it, and the brief it maintains is read by every role that
        // could do the investigating properly.
        AgentDefinition::new(
            "context_curator",
            "Context Curator Agent",
            "Keeps CONTEXT.md, the brief every reasoning role is sent, within its token budget \
             and current with what the run and durable memory now establish.",
        )
        .with_model("openrouter")
        .with_tools(
            [SCRATCH_READ_TOOL]
                .into_iter()
                .chain(memory_tools)
                .chain(document_tools),
        ),
        // Turns one sentence from a person into changes to the files that say
        // what the run is doing. It has the document tools and nothing that
        // computes: no shell, no tool writing, no delegation. A directive is
        // already the most powerful input the run takes — it outranks the
        // judge in the next attempt's prompt — and a role that could both
        // reinterpret the goal and run programs against it would be a second
        // investigation answering to nobody.
        AgentDefinition::new(
            "director",
            "Director Agent",
            "Carries an operator's directive into the workspace: what the run is doing next, \
             which directions are open, and what the shared brief says.",
        )
        .with_model("openrouter")
        .with_tools(
            [SCRATCH_READ_TOOL]
                .into_iter()
                .chain(memory_tools)
                .chain(document_tools),
        ),
        AgentDefinition::new(
            "inventor",
            "Inventor Agent",
            if research_enabled {
                "Proposes a genuinely different approach, checked against the literature."
            } else {
                "Proposes a genuinely different approach from its own reasoning."
            },
        )
        .with_model("openrouter")
        .with_tools(
            research_enabled
                .then_some("exa_search")
                .into_iter()
                .chain(research_enabled.then_some("oeis_lookup"))
                // A literature question it cannot settle from its own search
                // becomes one delegated check rather than an abandoned idea.
                // The singular pair, as with the pattern agent: this role asks
                // one focused question, where the planners fan out.
                .chain(["spawn_agent", "await_agent"])
                .chain(memory_tools)
                .chain(document_tools),
        ),
        // The document tools and the memory tools, and nothing else — the same
        // grant reflection has, and not by coincidence: both read the whole
        // workspace, write prose about it, and must not start solving.
        //
        // No `exa_search` or `oeis_lookup`: a role that can search turns "what
        // would suffice" into another literature survey, which is the
        // librarian's errand and is already commissioned at every diversify.
        // Nothing that computes, because a gap is discharged by a proof or a
        // claim, never by a program this role wrote. No delegation bench,
        // because a skeleton is checked by the forward loop attacking its gaps
        // — a bench here would be a second investigation beside the first. No
        // scratch, because a gap opened on arithmetic nobody has settled is a
        // task the forward loop cannot close.
        AgentDefinition::new(
            "reducer",
            "Reduction Agent",
            "Works backward from the goal: states the lemmas that would suffice to prove it, and \
             names the gaps between them and what the run has established.",
        )
        .with_model("openrouter")
        .with_tools(memory_tools.into_iter().chain(document_tools)),
    ]
    .into_iter()
    .chain(library_agents(
        research_enabled,
        document_tools,
        memory_tools,
    ))
    .collect()
}

/// Returns the librarian, scholar, and goals definitions.
///
/// Split from [`support_agents`] only to keep each function readable; these
/// are the roles that build and read the reference library, plus the worker
/// the solution loop drives.
fn library_agents(
    research_enabled: bool,
    document_tools: [&'static str; 11],
    memory_tools: [&'static str; 3],
) -> Vec<AgentDefinition> {
    vec![
        AgentDefinition::new(
            "librarian",
            "Librarian Agent",
            "Finds primary material, downloads it into the workspace reference library, and \
             indexes it for local search.",
        )
        .with_model("openrouter")
        .with_tools(
            research_enabled
                .then_some("exa_search")
                .into_iter()
                .chain(research_enabled.then_some("oeis_lookup"))
                // The role whose whole subject is coverage gets every way onto
                // the web there is. A librarian that can only rephrase a query
                // builds the library one vocabulary guess at a time, which is
                // the failure its own brief opens with.
                .chain(research_enabled.then_some(DISCOVERY_TOOLS).into_iter().flatten())
                .chain(memory_tools)
                .chain(document_tools),
        ),
        AgentDefinition::new(
            "scholar",
            "Scholar Agent",
            "Reads the downloaded reference library against the run's own goal and beliefs, \
             records what each source establishes, and maintains a navigable digest of it.",
        )
        .with_model("openrouter")
        .with_tools(
            memory_tools
                .into_iter()
                .chain([SCRATCH_READ_TOOL])
                .chain(document_tools),
        ),
        AgentDefinition::new(
            "goals",
            "Goals Agent",
            "Pursues a goal and delegates research, implementation, and verification.",
        )
        .with_model("openrouter")
        .with_tools(
            [
                "spawn_agent",
                // The prompt tells this role to fan out in one call rather than
                // one spawn per turn, and these are the tools that do it.
                // Advertising only the singular pair described a role that
                // could not follow its own instructions.
                "spawn_agents",
                "peek_agent",
                "steer_agent",
                "await_agent",
                "await_agents",
            ]
            .into_iter()
            .chain(memory_tools)
            .chain(SCRATCH_TOOLS)
            .chain(document_tools),
        ),
    ]
}
