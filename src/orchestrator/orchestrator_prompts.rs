/// Every role's system prompt, assembled from its built-in policy plus the
/// workspace's own guidance files.
struct RolePrompts {
    orchestrator: String,
    research: String,
    tool_builder: String,
    coder: String,
    candidate: String,
    sat_solver: String,
    smt_solver: String,
    theorem_prover: String,
    symbolic_math: String,
    lean_prover: String,
    lean_scribe: String,
    goals: String,
    reflection: String,
    archivist: String,
    judge: String,
    pattern: String,
    inventor: String,
    reducer: String,
    weakener: String,
    searcher: String,
    refuter: String,
    librarian: String,
    scholar: String,
    curator: String,
    director: String,
}

/// Every role's assembled system prompt, for inspection.
///
/// A role's prompt is built from three sources — the shared method policy, the
/// built-in role prompt, and whichever workspace files that role is entitled
/// to — and until now the only way to see the result was to run the agent and
/// read a provider trace. That made the most consequential text in the runtime
/// the least reviewable, and a mistake in it (a rule that reads as optional, a
/// file routed to the wrong role, a prompt that has silently doubled in size)
/// invisible until it changed a run's behaviour.
///
/// The token estimates matter as much as the text. Every one of these is sent
/// on every model call in that role's run, so a prompt that has grown is a bill
/// that has grown, and the shared prefix is what the provider cache is keyed
/// on.
///
/// # Errors
///
/// Returns an error when a workspace file is unreadable, oversized, or not
/// UTF-8.
pub fn prompt_report(workspace: &Path) -> Result<String> {
    let reports = prompt_reports(workspace)?;
    let mut out = format!(
        "# Assembled agent prompts\n\nworkspace: {}\n\n\
         Each prompt is the shared method policy, then the role's built-in prompt, then the \
         workspace files that role receives.\n",
        workspace.display()
    );
    let total: u64 = reports.iter().map(|report| report.tokens).sum();
    for report in &reports {
        let _ = write!(
            out,
            "\n\n---\n\n## {}\n\n_{} chars, ~{} tokens_\n\n```text\n{}\n```",
            report.role,
            report.prompt.len(),
            report.tokens,
            report.prompt
        );
    }
    let _ = write!(
        out,
        "\n\n---\n\n_~{total} tokens across {} roles; the shared method policy is ~{} of them, \
         repeated in every one._\n",
        reports.len(),
        shared_policy_tokens()
    );
    Ok(out)
}

/// One role's assembled system prompt, with what it costs.
#[derive(Clone, Debug)]
pub struct PromptReport {
    /// The role's name, as the registry knows it.
    pub role: String,
    /// What the role may call, as the registry declares it.
    ///
    /// Empty for a role whose tools are registered straight onto a harness
    /// rather than declared — the two planners, whose grant is
    /// `build_planner_harness` and has no entry to read.
    pub tools: Vec<String>,
    /// The whole prompt, exactly as the runtime would send it.
    pub prompt: String,
    /// What it costs, by the runtime's own estimator.
    pub tokens: u64,
}

/// Every role's assembled prompt, one entry each.
///
/// [`prompt_report`] renders these into one document and is written in terms of
/// this rather than beside it, so there is one answer to *what does each role
/// receive* and one place a role added to the registry shows up. A caller that
/// wants the prompts separately — a file per agent, a table of what each costs,
/// a diff of one role across two workspaces — gets them here rather than by
/// parsing the report's headings back out, which is the drift this avoids.
///
/// # Errors
///
/// Returns an error when a workspace file is unreadable, oversized, or not
/// UTF-8.
pub fn prompt_reports(workspace: &Path) -> Result<Vec<PromptReport>> {
    let prompts = RolePrompts::load(workspace)?;
    let registry = default_registry(research_enabled_from_env())?;
    Ok(prompts
        .by_role()
        .into_iter()
        .map(|(role, prompt)| PromptReport {
            role: role.to_string(),
            prompt: prompt.to_string(),
            tokens: estimate_tokens(prompt),
            tools: role_tools(&registry, role),
        })
        .collect())
}

/// What `role` may call, as the registry grants it.
///
/// A prompt does not list a role's tools and should not: they are sent as
/// function schemas on every request, so writing them into the text would pay
/// for them twice and give a role two lists to disagree about. That makes them
/// invisible to a *reviewer*, which is a different problem and is what this
/// answers — the report shows what a role is told beside what it can do, off
/// the same registry the run builds its harnesses from.
///
/// The orchestrator is the one role with no entry to read: it is the top level
/// rather than a registered specialist. Its harness is built by the same
/// function as the goals planner's, so `planner_tools` derives its grant by
/// subtracting the tools that branch withholds, rather than restating it.
fn role_tools(registry: &AgentRegistry, role: &str) -> Vec<String> {
    if let Some(declared) = declared_tools(registry, role) {
        return declared;
    }
    // The orchestrator is the top level rather than a registered specialist, so
    // it has no entry. Its harness is built by the same function as the goals
    // planner's, from the same list, so its grant is derived from that one.
    declared_tools(registry, "goals")
        .map(|goals| planner_tools(&goals, role))
        .unwrap_or_default()
}

/// One role's declared tools, looking through a school's qualified name.
fn declared_tools(registry: &AgentRegistry, role: &str) -> Option<Vec<String>> {
    if let Some(definition) = registry.get(role) {
        return Some(definition.tools.clone());
    }
    schools::selected()
        .iter()
        .find_map(|school| registry.get(&school.role(role)))
        .map(|definition| definition.tools.clone())
}

/// What the shared method policy costs, which every role pays.
#[must_use]
pub fn shared_policy_tokens() -> u64 {
    estimate_tokens(SHARED_METHOD_POLICY)
}

impl RolePrompts {
    /// The roles carrying shell and file-write authority, paired with their
    /// prompts, in the order they are registered.
    fn code_writers(&mut self) -> [(&'static str, String); 7] {
        [
            ("tool_builder", std::mem::take(&mut self.tool_builder)),
            ("coder", std::mem::take(&mut self.coder)),
            ("sat_solver", std::mem::take(&mut self.sat_solver)),
            ("smt_solver", std::mem::take(&mut self.smt_solver)),
            ("theorem_prover", std::mem::take(&mut self.theorem_prover)),
            ("symbolic_math", std::mem::take(&mut self.symbolic_math)),
            ("lean_prover", std::mem::take(&mut self.lean_prover)),
        ]
    }

    /// The Lean scribe's prompt.
    ///
    /// Taken on its own rather than with the code writers, because the scribe
    /// does not get their harness: its grant is two verbs and the reads, where
    /// theirs is a shell and a patch tool. See `register_lean_scribe`.
    fn lean_scribe(&mut self) -> String {
        std::mem::take(&mut self.lean_scribe)
    }

    /// The support roles' prompts, in one move.
    ///
    /// A method rather than a struct literal at the call site, for the reason
    /// [`Self::code_writers`] is one: the list has grown past the point where
    /// spelling it inline leaves `from_env` readable, and a set of prompts is
    /// the kind of thing that should be assembled in one place so a role added
    /// to the registry and forgotten here fails to compile rather than silently
    /// running with an empty brief.
    fn support(&mut self) -> SupportPrompts {
        SupportPrompts {
            reflection: std::mem::take(&mut self.reflection),
            archivist: std::mem::take(&mut self.archivist),
            judge: std::mem::take(&mut self.judge),
            pattern: std::mem::take(&mut self.pattern),
            inventor: std::mem::take(&mut self.inventor),
            reducer: std::mem::take(&mut self.reducer),
            weakener: std::mem::take(&mut self.weakener),
            searcher: std::mem::take(&mut self.searcher),
            refuter: std::mem::take(&mut self.refuter),
            librarian: std::mem::take(&mut self.librarian),
            scholar: std::mem::take(&mut self.scholar),
            curator: std::mem::take(&mut self.curator),
            director: std::mem::take(&mut self.director),
        }
    }

    /// Returns each role's name paired with its assembled prompt.
    fn by_role(&self) -> Vec<(&'static str, &str)> {
        vec![
            ("orchestrator", self.orchestrator.as_str()),
            ("goals", self.goals.as_str()),
            ("research", self.research.as_str()),
            ("tool_builder", self.tool_builder.as_str()),
            ("coder", self.coder.as_str()),
            // Reported under the first slot's name because the six slots share
            // this prompt byte for byte; they differ in where their tools point,
            // which a prompt cannot show.
            ("candidate01", self.candidate.as_str()),
            ("sat_solver", self.sat_solver.as_str()),
            ("smt_solver", self.smt_solver.as_str()),
            ("theorem_prover", self.theorem_prover.as_str()),
            ("symbolic_math", self.symbolic_math.as_str()),
            ("lean_prover", self.lean_prover.as_str()),
            ("reflection", self.reflection.as_str()),
            ("archivist", self.archivist.as_str()),
            ("judge", self.judge.as_str()),
            ("pattern_finder", self.pattern.as_str()),
            ("inventor", self.inventor.as_str()),
            ("reducer", self.reducer.as_str()),
            ("weakener", self.weakener.as_str()),
            ("searcher", self.searcher.as_str()),
            ("refuter", self.refuter.as_str()),
            ("librarian", self.librarian.as_str()),
            ("scholar", self.scholar.as_str()),
            ("context_curator", self.curator.as_str()),
            ("director", self.director.as_str()),
        ]
    }
}

/// Where provisional work goes now that `SCRATCHPAD.md` is not routed into any
/// system prompt.
///
/// A file cost every model call in every role holding it, whether or not the
/// turn was about the numbers in it, and had to be read whole to append a line.
/// These are the same trade `remember_memory` and `recall_memory` make, over a
/// store no durable recall reaches — see [`vector::visible_datasets`].
///
/// They are granted to exactly the roles the file was routed to, and withheld
/// from the rest for the reason it was withheld from reflection: unsettled
/// arithmetic must not read as progress. `note_scratch` is narrower still — a
/// role that only *reads* what a solve is in the middle of has no provisional
/// work of its own to record.
const SCRATCH_TOOLS: [&str; 2] = ["note_scratch", "recall_scratch"];

/// The read half of [`SCRATCH_TOOLS`], for a role that judges provisional work
/// rather than producing it.
const SCRATCH_READ_TOOL: &str = "recall_scratch";

/// The workspace context every role receives.
///
/// `AGENTS.md` is the method policy and applies to everyone. Nothing else does.
const UNIVERSAL_CONTEXT: [&str; 1] = ["AGENTS.md"];

/// Workspace artifacts loaded into each role's system prompt, beyond
/// [`UNIVERSAL_CONTEXT`]. Durable knowledge is not duplicated here: every role
/// recalls it from Cognee with `recall_memory` and can store verified findings
/// with `remember_memory`.
///
/// `config/config.toml` used to head the two executing arms and no longer
/// reaches any prompt. Nothing in it was a fact only that file held. Its policy
/// lines — show the derivation, verify with code, cite external claims — are
/// the built-in prompts restated in TOML, so a role read them twice and had two
/// wordings to reconcile. Its `[artifacts]` names are stale (`tasks.md`, where
/// the runtime writes `TASKS.md`), which is worse than absent: a role that
/// believes them writes to a path no ledger derives from. And its one hard
/// number, `maximum_tool_runtime_seconds`, is enforced by `execute_command` and
/// named in the error a timeout returns, which is where a limit is actually
/// learned. A file is routed because a role cannot do its work without it, and
/// this one failed that test on every line.
///
/// Order matters, and only at the end: `CONTEXT.md` is moved last whatever
/// position an arm below writes it in. [`RolePrompts::for_school`] does the
/// move, and says why it is enforced there rather than trusted to the lists.
/// What the orchestrator reads: the run's goal, its plan, and every ledger a
/// decision about what to do next is made from.
///
/// The two planners read the same decision material and differ in one file,
/// which is the difference between deciding *who* works and driving the work.
/// The arms are separate rather than shared behind a `|` so that difference is
/// stated once and is visible.
const ORCHESTRATOR_CONTEXT: &[&str] = &[
    "GOAL.md",
    "derived/TASKS.md",
    "derived/CLAIMS.md",
    "derived/THREADS.md",
    "derived/APPROACHES.md",
    // The open gaps are the run's stock of ready-made tasks: a lemma with a
    // first move somebody could make today. A planner that cannot see them
    // plans around them.
    "derived/BACKWARD.md",
    // And the graph over them, which answers the question the flat list cannot:
    // which of those tasks can be handed to a sub-agent *now*, because
    // everything it rests on is settled. A planner routing work to concurrent
    // children needs exactly that distinction, and `BACKWARD.md` makes every
    // open gap look equally attackable.
    "derived/BLUEPRINT.md",
    // What the library gives without new work. A planner that cannot see this
    // schedules an attempt at something the run already holds, which is the
    // most expensive mistake available to it.
    "derived/ENTAILMENT.md",
    // The standing bet, and it is here for the reason none of the rest is: it
    // was written by an *earlier run*. Everything else in this list is this
    // investigation's own state, and a problem of this size is not settled
    // inside one container — so the one file that carries an argument across
    // runs belongs in front of the role that decides what the next run does.
    "derived/THESIS.md",
    // And the quantity the run is driving at, with how far apart its two sides
    // are. A planner that cannot see the gap schedules work that does not narrow
    // it, which is most work.
    "derived/REDUCTIONS.md",
    // What the other schools have said. A planner deciding what to spend the
    // next run on is the reader a dead end found once and paid for once was
    // written for.
    board::PATH,
    shared_context::CONTEXT_FILE,
];

/// What the goals agent reads: the orchestrator's material, plus the reuse
/// index.
///
/// It spawns `tool_builder` and `coder` and reads back what they wrote, so it
/// has to know which helper already exists; the orchestrator hands out
/// objectives and never chooses a module, and every role that does write code
/// carries this index itself.
const GOALS_CONTEXT: &[&str] = &[
    "GOAL.md",
    "derived/TASKS.md",
    "code/lib/INDEX.md",
    "derived/CLAIMS.md",
    "derived/THREADS.md",
    "derived/APPROACHES.md",
    "derived/BACKWARD.md",
    "derived/BLUEPRINT.md",
    "derived/ENTAILMENT.md",
    // The standing bet, and the quantity the run is driving at. Both are here
    // rather than left to recall for the same reason `TASKS.md` is: they are
    // what the *next* decision is made against, and a planner that has to fetch
    // them makes the decision first.
    "derived/THESIS.md",
    "derived/REDUCTIONS.md",
    board::PATH,
    shared_context::CONTEXT_FILE,
];

fn role_context(role: &str) -> &'static [&'static str] {
    match role {
        "goals" => GOALS_CONTEXT,
        "orchestrator" => ORCHESTRATOR_CONTEXT,
        "tool_builder" | "coder" | "sat_solver" | "smt_solver" | "theorem_prover"
        | "symbolic_math" | "lean_prover" => &[
            "GOAL.md",
            "derived/TASKS.md",
            "code/AGENTS.md",
            "code/INDEX.md",
            "code/lib/INDEX.md",
            "derived/CLAIMS.md",
            // What the run has already stated in Lean, one signature per row.
            // Sent to all seven rather than to `lean_prover` alone, and the
            // reason is the same one `code/lib/INDEX.md` is: this is the
            // reuse index. A signature says exactly what a lemma assumes,
            // which is the form the other six need when they are deciding
            // whether the thing they are about to compute is already settled —
            // and `lean_prover` needs it most, because the failure it prevents
            // is a role spending an attempt re-proving a lemma the kernel
            // accepted three attempts ago.
            lemmas::LEMMAS_PATH,
            // What the run is driving the problem down to. Sent to all seven,
            // and the reason is that a reduction target is the one thing that
            // makes a computation *worth* doing: the difference between sweeping
            // a range because it is sweepable and sweeping it because it closes
            // the gap between two bounds is this file.
            "derived/REDUCTIONS.md",
            "CONTEXT.md",
        ],
        // Not sent `research/APPROACHES.md`, though the judge now scores an
        // attempt partly on whether it opened a line of attack and closed an
        // alternative. That is the reason to withhold it rather than to send
        // it: the judge scores the *report*, and a judge holding the ledger
        // would credit an attempt for approaches it can see on disk but that
        // the report never mentions. The evidence has to be in the report, or
        // the score is not about the attempt.
        // Not sent the board either, and for the reason that decides who reads
        // it at all: a post is *asserted* rather than established — a hunch, a
        // dead end, a half-formed lesson, offered precisely because it is
        // unfinished — so it goes to the roles choosing what to do next and is
        // withheld from every role that weighs evidence or files sources. A
        // judge scoring an attempt beside a sibling's unevidenced sentence is
        // one prompt away from scoring the sentence. It is the same boundary
        // that keeps `research/CLAIMS.md` away from the director, which acts on
        // an assertion and must never file one.
        "judge" => &["GOAL.md", "INDEX.md"],
        // Sent the thesis and the reduction ledger because it is the role that
        // revises one and closes the other. Reflection is where a round's
        // evidence meets what the run believed before it, which is the only
        // moment in the loop that can notice a thesis its own `refuted-by` has
        // come true.
        "reflection" => &[
            "GOAL.md",
            "derived/TASKS.md",
            "derived/THESIS.md",
            "derived/REDUCTIONS.md",
            "INDEX.md",
            board::PATH,
        ],
        "pattern_finder" => &["GOAL.md", "code/lib/INDEX.md", board::PATH, "CONTEXT.md"],
        // The scholar writes the claim blocks, so it is the role that draws the
        // `follows-from:` edges — and the one that should see what those edges
        // already establish before recording a statement the library entails.
        "scholar" => &[
            "GOAL.md",
            "derived/TASKS.md",
            "derived/CLAIMS.md",
            "derived/ENTAILMENT.md",
            "derived/THREADS.md",
            "CONTEXT.md",
        ],
        "librarian" | "research" => &[
            "GOAL.md",
            "derived/CLAIMS.md",
            "derived/THREADS.md",
            "derived/APPROACHES.md",
            "derived/FRONTIER.md",
            "CONTEXT.md",
        ],
        // The inventor is also handed a dossier assembled from disk at the
        // moment it is delegated to, which is what it actually reasons from —
        // see [`dossier`] for why a prompt loaded at startup is the wrong
        // record for this role. These files remain because a run may reach the
        // inventor by a path that does not build one.
        "inventor" => &[
            "GOAL.md",
            "derived/THREADS.md",
            "derived/APPROACHES.md",
            "derived/CLAIMS.md",
            // The role asked for something genuinely different is the one that
            // most needs to know which different things a sibling has already
            // walked into.
            board::PATH,
            "CONTEXT.md",
        ],
        // Also handed a dossier built from disk at delegation time, for the
        // reason the inventor is.
        //
        // Not sent `research/APPROACHES.md`, and that exclusion is the role's
        // boundary rather than an oversight. The approach ledger is about
        // *method*, and a role holding it drifts into proposing methods — which
        // is the inventor's job and the one confusion this role must not
        // create. It is asked what would suffice, not how to get there.
        //
        // It is sent the graph over its own skeletons, and that is the one
        // check on this role nothing else performs: a decomposition whose gap
        // is proved by a skeleton that assumes the goal reads as sound in both
        // files and is circular across them. The reducer is the only role that
        // can fix it, and until `BLUEPRINT.md` existed it was the only role
        // that could not see it.
        "reducer" => &[
            "GOAL.md",
            "derived/BACKWARD.md",
            "derived/REDUCTIONS.md",
            "derived/BLUEPRINT.md",
            "derived/CLAIMS.md",
            "derived/THREADS.md",
            board::PATH,
            "CONTEXT.md",
        ],
        // The weakener is sent its own ladder, the goal it is lowering, and
        // what the run has actually established — that last one being what
        // decides which rung is next, since a rung the claims ledger already
        // covers is settled whether or not the ladder says so.
        //
        // It is denied `research/APPROACHES.md` for the reducer's reason, and
        // `research/BACKWARD.md` for one of its own: a proof skeleton is a
        // decomposition of the *full-strength* goal, and a role whose whole
        // job is to lower that goal should not be reading a document that
        // assumes it fixed. The two ledgers meet in the attempt, which is
        // where they should.
        "weakener" => &[
            "GOAL.md",
            "derived/WEAKENED.md",
            "derived/CLAIMS.md",
            "derived/THREADS.md",
            board::PATH,
            "CONTEXT.md",
        ],
        // The searcher is routed almost nothing, and that is the shape of the
        // role rather than an oversight. Everything it needs about the search
        // itself — the problem, the scorer, the programs that scored best —
        // changes with every candidate, so it arrives through `search_brief`
        // rather than through a system prompt assembled once per run. What is
        // routed is the run's standing beliefs, which do not change that fast
        // and which stop it hunting a construction the library already rules
        // out. It is denied the threads and the approach ledger for the reason
        // the judge is: a role scoring hundreds of candidates must not spend
        // its budget reading about the investigation around it.
        //
        // The archivist shares the arm because it needs the same three things
        // for the same reason: what a candidate is judged *against*, and
        // nothing about how the run arrived here. Which direction the run is
        // pursuing is not evidence about which of five diffs is correct, and a
        // role given the method ledger grades method instead of reading the
        // change in front of it.
        "searcher" | "archivist" => &["GOAL.md", "derived/CLAIMS.md", "CONTEXT.md"],

        // The refuter is sent the two ledgers holding statements somebody has
        // committed to proving, because those are the ones worth attacking, and
        // the claim ledger so it does not spend a cycle refuting something the
        // run already disproved. Not the threads or the approach ledger: which
        // direction the run is pursuing is irrelevant to whether the statement
        // is true, and a role given the method ledger drifts into commenting on
        // the method.
        "refuter" => &[
            "GOAL.md",
            "derived/BACKWARD.md",
            "derived/WEAKENED.md",
            "derived/CLAIMS.md",
            "CONTEXT.md",
        ],
        // The curator writes the shared brief, so it is the one role that
        // needs to see the brief *and* the material it is written from: what
        // the run is for, what it is attempting, what the library establishes,
        // and the provisional work that has not earned a place in the brief
        // yet — which it reads with `recall_scratch` rather than from a file.
        // It reads the rest — reflections, results, the note store — with its
        // tools too, because those are large and change constantly.
        "context_curator" => &[
            "GOAL.md",
            "derived/TASKS.md",
            "INDEX.md",
            "derived/CLAIMS.md",
            "derived/THREADS.md",
            "derived/APPROACHES.md",
            "derived/BACKWARD.md",
            "CONTEXT.md",
        ],
        // The director rewrites the files that say what the run is doing, so
        // it is sent those and only those. It gets `GOAL.md` and `TASKS.md`
        // because a directive is read against what the run was already for,
        // and `THREADS.md` because opening or closing a direction of attack is
        // most of what acting on a directive amounts to. It is not sent
        // `CLAIMS.md`: a directive is asserted rather than established, and a
        // role holding the evidence ledger while acting on an unevidenced
        // instruction is one prompt away from filing the instruction as a
        // finding.
        "director" => &[
            "GOAL.md",
            "derived/TASKS.md",
            "derived/THREADS.md",
            "derived/APPROACHES.md",
            "CONTEXT.md",
        ],
        _ => &[],
    }
}

/// Per-role prompt overlays, keyed by school slug and role name.
///
/// A table rather than a directory walk, because these are compiled-in assets:
/// probing the filesystem at startup would make a role's brief depend on what
/// happens to be beside the binary, and a typo in a slug would read as "this
/// school says nothing extra to that role" rather than failing to build. An
/// entry is added here with an `include_str!` beside it; there are none yet,
/// and a school whose whole policy fits in its method-policy overlay needs
/// none.
const SCHOOL_ROLE_OVERLAYS: [(&str, &str, &str); 0] = [];

/// The overlay `slug` writes for `role` in particular, or nothing.
fn school_role_overlay(slug: &str, role: &str) -> &'static str {
    SCHOOL_ROLE_OVERLAYS
        .iter()
        .find(|(school, name, _)| *school == slug && *name == role)
        .map_or("", |(_, _, overlay)| *overlay)
}

/// What the roles holding `post_board` are told the board is for.
///
/// This exists because registering a tool is not the same as asking for it. A
/// live three-school hour on Project Euler 1006 called `post_board` **zero**
/// times: all three schools reached a verdict, all three ran the reflection —
/// the role that holds the tool — and none posted. Nothing was broken. The
/// grant was right, `teams/BOARD.md` was routed to every reader, and no prompt
/// in this crate mentioned the board at all, so the only trace of it a model
/// saw was an unexplained entry in a tool list, inside a call whose
/// instructions end "Answer exactly these four things". It answered the four
/// things. A capability nobody is told to use is not a capability.
const BOARD_BRIEF: &str = include_str!("../prompts/board.md");

/// The roles that receive [`BOARD_BRIEF`].
///
/// Derived from nothing, and it has to be: the grant lives in
/// `orchestrator_registry`'s bench lists, which are `&'static str` arrays built
/// per role rather than a queryable map, so there is no honest way to read this
/// off the authority. A test asserts the two agree instead, because the failure
/// this guards is silent in both directions — a role told to post that cannot,
/// and a role that can post and was never asked.
const BOARD_ROLES: [&str; 3] = ["reflection", "inventor", "goals"];

/// What every role is told about the ledgers it can read.
///
/// Universal, because `list_ledgers` and `read_ledger` are granted with the
/// document tools and for the same reason: a role that cannot read what the run
/// already recorded records it again.
///
/// It is short on purpose. This one goes into all twenty-two prompts, so a
/// paragraph here costs twenty-two paragraphs — the arithmetic that made
/// `research/APPROACHES.md` worth 86 KB of prompt in the first place.
const LEDGER_BRIEF: &str = include_str!("../prompts/ledgers.md");

/// What the roles holding `record_entry` are additionally told.
///
/// Separate from [`LEDGER_BRIEF`] because most roles cannot write and would be
/// paying for instructions they cannot act on.
const LEDGER_WRITING_BRIEF: &str = include_str!("../prompts/ledger_writing.md");

/// What the two roles holding `define_ledger` are additionally told.
///
/// Separate again, and for a sharper version of the same reason: this is the
/// narrowest grant in the runtime and a paragraph about declaring an axis is
/// actively harmful in the twenty prompts that cannot declare one — it reads as
/// an invitation to ask somebody to.
const LEDGER_KEEPING_BRIEF: &str = include_str!("../prompts/ledger_keeping.md");

/// The roles that receive [`LEDGER_KEEPING_BRIEF`].
///
/// The two planners, matching `LEDGER_KEEPER_TOOLS` and the `keepers` call in
/// `build_planner_harness`. Not derived, for the reason [`LEDGER_WRITER_ROLES`]
/// is not, and asserted against the grant by a test for the same reason.
const LEDGER_KEEPER_ROLES: [&str; 2] = ["orchestrator", "goals"];

/// One line per ledger this workspace actually keeps, for `role`.
///
/// Written because [`LEDGER_BRIEF`] said *"`list_ledgers` names every one"* and
/// left it there — a tool call a model has to think to make before it can find
/// out what exists. That is precisely the shape of the `post_board` failure
/// this file already records: granted, described nowhere a role would read
/// before acting, and called zero times in a live three-school hour. A role
/// that does not know the `weakened` ledger exists does not call `list_ledgers`
/// to discover it; it writes the ladder into prose, and nothing walks prose.
///
/// It is derived from the registry rather than written down, so a ledger the
/// run *defines mid-flight* is named in the next prompt assembled — which is
/// the whole reason `define_ledger` is worth holding. A written list would be a
/// second answer to what exists, and the stale one.
///
/// Cheap enough to be universal: a dozen rows of slug, one truncated sentence,
/// and whether this role may write it. Which is the other half of the point —
/// "yours" and "read-only" are read off `writable_by`, so a role learns which
/// ledgers are its own from the same list, rather than from a refusal.
fn ledger_catalogue(workspace: &Path, role: &str) -> String {
    let (specs, _) = ledger::registry::all(workspace);
    if specs.is_empty() {
        return String::new();
    }
    let mut out = String::from(
        "**The ledgers this workspace keeps right now.** `list_ledgers` says more about any of \
         them — the fields, the statuses, how many entries.\n\n",
    );
    for spec in specs {
        let _ = writeln!(
            out,
            "- `{}` ({}) — {}{}",
            spec.slug,
            if spec.writable_by(role) {
                "yours to write"
            } else {
                "read-only for you"
            },
            text::truncate(spec.purpose.split('\n').next().unwrap_or_default(), 120),
            if spec.builtin {
                ""
            } else {
                " _(defined by this run)_"
            },
        );
    }
    out
}

/// The roles that receive [`LEDGER_WRITING_BRIEF`].
///
/// Derived from nothing, for the reason [`BOARD_ROLES`] is not: the grants live
/// in `orchestrator_registry`'s per-role `&'static str` arrays and in the
/// harness registrations, neither of which is a queryable map. A test asserts
/// the three agree.
///
/// The list exists at all because of what happened to `post_board` — granted to
/// three roles, mentioned in no prompt, and called **zero** times in a live
/// three-school hour. Five tools would be five times that failure.
/// The two roles the reader brief is withheld from.
///
/// Both are told, in their own prompts, not to read around the investigation,
/// and for the same reason: they are called many times against a small budget,
/// and reading is the thing that would consume it. A judge that starts pulling
/// ledgers stops judging, and a searcher scoring hundreds of candidates must
/// not spend its budget on the argument surrounding them.
///
/// They still *hold* the read tools, which is deliberate. The brief is an
/// instruction to go and read; withholding it is not the same as taking the
/// capability away, and a judge checking one claim in a report against the
/// ledger is exactly the use that should stay available.
const LEDGER_BRIEF_WITHHELD: [&str; 3] = ["judge", "searcher", "lean_scribe"];

const LEDGER_WRITER_ROLES: [&str; 6] = [
    "goals",
    "orchestrator",
    "director",
    "reflection",
    "reducer",
    // The archivist decides which candidate the run keeps, and the attempts
    // ledger is where that decision and the reasons the others were not kept
    // are written down. A decision nobody recorded is one the next round
    // re-litigates.
    "archivist",
];

/// What `role` is told about the ledgers, appended to its own guidance.
///
/// Returns the empty string only for a role the reader brief is withheld from
/// and that cannot write — which is the judge and the searcher, and nothing
/// else. See [`LEDGER_BRIEF_WITHHELD`].
///
/// `workspace` reaches [`ledger_catalogue`] only. The brief is static text and
/// the catalogue is this workspace's registry, and the two are assembled
/// together because they are one instruction: here is what exists, here is how
/// to reach it.
fn ledger_layer(workspace: &Path, role: &str) -> String {
    let mut layer = String::new();
    if !LEDGER_BRIEF_WITHHELD.contains(&role) {
        layer.push_str("\n\n");
        layer.push_str(LEDGER_BRIEF.trim());
        let catalogue = ledger_catalogue(workspace, role);
        if !catalogue.is_empty() {
            layer.push_str("\n\n");
            layer.push_str(catalogue.trim());
        }
    }
    if LEDGER_WRITER_ROLES.contains(&role) {
        layer.push_str("\n\n");
        layer.push_str(LEDGER_WRITING_BRIEF.trim());
    }
    if LEDGER_KEEPER_ROLES.contains(&role) {
        layer.push_str("\n\n");
        layer.push_str(LEDGER_KEEPING_BRIEF.trim());
    }
    layer
}

/// What a school adds to `role`'s brief, ready to prefix the built-in prompt.
///
/// Returns the empty string when the school says nothing — which is the whole
/// of [`schools::ALL`]'s control school, and is why this returns a prefix
/// rather than a section: an empty overlay must add nothing at all, not a blank
/// line and not a separator, or `chisel`'s assembled prompts stop being
/// byte-identical to the ones the runtime sent before schools existed.
///
/// It sits *after* the shared method policy and before the role prompt.
/// [`workspace_prompt`] puts the shared policy first because the provider cache
/// is keyed on that prefix, and a school is per-run text: leading with it would
/// give every school its own cache namespace and lose the one identical opening
/// block every role in every run shares.
///
/// `siblings` is whether more than one school is running. It gates
/// [`BOARD_BRIEF`] rather than the grant, because the board is the one part of
/// a school's brief that is not about *its* method: a school running alone has
/// nobody to tell, and telling it to post anyway would spend tokens on an
/// audience of one and take the control school's prompts away from the ones
/// this runtime sent before schools existed.
fn school_layer(school: &schools::School, role: &str, siblings: bool) -> String {
    let mut layer = String::new();
    let board = if siblings && BOARD_ROLES.contains(&role) {
        BOARD_BRIEF
    } else {
        ""
    };
    for part in [school.policy, school_role_overlay(school.slug, role), board] {
        let part = part.trim();
        if !part.is_empty() {
            layer.push_str(part);
            layer.push_str("\n\n");
        }
    }
    layer
}

impl RolePrompts {
    /// Loads each role's prompt: built-in policy, the workspace context that
    /// role is entitled to, then its `prompts/<role>.md` guidance.
    ///
    /// The control school's prompts, which are the prompts this runtime sent
    /// before schools existed. Shares its whole body with
    /// [`Self::for_school`] rather than restating it, so the two cannot drift.
    ///
    /// # Errors
    ///
    /// Returns an error when a workspace file is unreadable, oversized, or not
    /// UTF-8. A file that is simply absent is skipped.
    fn load(workspace: &Path) -> Result<Self> {
        Self::for_school(workspace, &schools::ALL[0], false)
    }

    /// The same prompts, with `school`'s policy layered into every one.
    ///
    /// `siblings` says whether this run has more than one school, and reaches
    /// only [`school_layer`]'s board brief — see there for why the board is
    /// told to a school with an audience and withheld from one without.
    ///
    /// # Errors
    ///
    /// Returns an error when a workspace file is unreadable, oversized, or not
    /// UTF-8. A file that is simply absent is skipped.
    fn for_school(workspace: &Path, school: &schools::School, siblings: bool) -> Result<Self> {
        let role = |name: &str, base: &str| -> Result<String> {
            let mut files: Vec<&str> = UNIVERSAL_CONTEXT.to_vec();
            files.extend_from_slice(role_context(name));
            // The shared brief goes last in every role, and that is enforced
            // here rather than left to twelve hand-written lists staying in
            // agreement. It is the file most likely to be *acted on* — the
            // curator writes it precisely to say what everyone should know
            // right now — and the end of a prompt is the position a model
            // weights most and the one a truncated prompt keeps. It is also the
            // most volatile: putting it last keeps every stable block above it
            // identical between calls, which is what the provider prompt cache
            // keys on. A stable sort, so nothing else moves.
            files.sort_by_key(|relative| *relative == shared_context::CONTEXT_FILE);
            let context = load_workspace_files(workspace, &files)?;
            // There is no `prompts/<role>.md` override, and the path that read
            // one is gone rather than left waiting for a file. The template
            // shipped nine, `scripts/run-agent` copied all nine into every
            // workspace, and each was an older wording of the built-in prompt
            // for that role — *"a turn that ends with notes and no executed
            // program has accomplished nothing"* in a workspace file, beside
            // the same rule in the policy leading the prompt. Two wordings of
            // one rule is two rules to reconcile, and a role reads the second
            // one last. A prompt is Rust now, with one statement per rule.
            // Appended to the role's own guidance rather than prepended to the
            // shared prefix: this text is per-role, and `workspace_prompt`
            // orders most-shared-to-least so the provider cache keys on a block
            // every agent has in common. A per-role brief at the front would
            // give each role its own cache namespace. It lands beside the
            // built-in role prompt and above the workspace state — see
            // `workspace_prompt` for why those two swapped.
            let guidance = ledger_layer(workspace, name);
            // Concatenated rather than branched: an empty layer leaves `base`
            // exactly as it was, and `workspace_prompt` trims what it is given,
            // so the control school's output is unchanged to the byte.
            let base = format!("{}{base}", school_layer(school, name, siblings));
            Ok(workspace_prompt(&base, &context, &guidance))
        };
        // A role assembled from its own instructions and nothing else.
        //
        // No workspace files, no ledger brief, no shared method policy. That
        // last one is the part that looks like a hole and is not: the policy is
        // prose, and prose is not what stops a role doing something — the tool
        // grant is, and the scribe's is two verbs. What the policy would buy
        // here is advice about conducting an investigation, to a role that is
        // handed one statement and asked for one file.
        //
        // The point is the size. `lean_prover`'s assembled prompt measures
        // ~20,000 tokens, 68% of it workspace state, against a model chosen for
        // being fast and free rather than for holding a run's context. Handing
        // that model the investigation would spend the tier's whole advantage
        // on text it cannot use.
        let bare = |name: &str, base: &str| -> String {
            format!("{}{}", school_layer(school, name, siblings), base).trim().to_string()
        };
        Ok(Self {
            orchestrator: role("orchestrator", ORCHESTRATOR_PROMPT)?,
            research: role("research", RESEARCH_PROMPT)?,
            tool_builder: role("tool_builder", TOOL_BUILDER_PROMPT)?,
            coder: role("coder", CODER_PROMPT)?,
            candidate: role("candidate", CANDIDATE_PROMPT)?,
            sat_solver: role("sat_solver", SAT_SOLVER_PROMPT)?,
            smt_solver: role("smt_solver", SMT_SOLVER_PROMPT)?,
            theorem_prover: role("theorem_prover", THEOREM_PROVER_PROMPT)?,
            symbolic_math: role("symbolic_math", SYMBOLIC_MATH_PROMPT)?,
            lean_prover: role("lean_prover", LEAN_PROVER_PROMPT)?,
            lean_scribe: bare("lean_scribe", LEAN_SCRIBE_PROMPT),
            goals: role("goals", GOALS_PROMPT)?,
            reflection: role("reflection", REFLECTION_PROMPT)?,
            archivist: role("archivist", ARCHIVIST_PROMPT)?,
            judge: role("judge", JUDGE_PROMPT)?,
            pattern: role("pattern_finder", PATTERN_PROMPT)?,
            inventor: role("inventor", INVENTOR_PROMPT)?,
            reducer: role("reducer", REDUCER_PROMPT)?,
            weakener: role("weakener", WEAKENER_PROMPT)?,
            searcher: role("searcher", SEARCHER_PROMPT)?,
            refuter: role("refuter", REFUTER_PROMPT)?,
            librarian: role("librarian", LIBRARIAN_PROMPT)?,
            scholar: role("scholar", SCHOLAR_PROMPT)?,
            curator: role("context_curator", CONTEXT_CURATOR_PROMPT)?,
            director: role("director", DIRECTOR_PROMPT)?,
        })
    }
}
