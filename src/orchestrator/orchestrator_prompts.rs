/// Every role's system prompt, assembled from its built-in policy plus the
/// workspace's own guidance files.
struct RolePrompts {
    orchestrator: String,
    research: String,
    tool_builder: String,
    coder: String,
    sat_solver: String,
    smt_solver: String,
    theorem_prover: String,
    symbolic_math: String,
    lean_prover: String,
    goals: String,
    reflection: String,
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
    let prompts = RolePrompts::load(workspace)?;
    let mut out = format!(
        "# Assembled agent prompts\n\nworkspace: {}\n\n\
         Each prompt is the shared method policy, then the role's built-in prompt, then the \
         workspace files that role receives.\n",
        workspace.display()
    );
    let mut total = 0_u64;
    for (role, prompt) in prompts.by_role() {
        let tokens = estimate_tokens(prompt);
        total += tokens;
        let _ = write!(
            out,
            "\n\n---\n\n## {role}\n\n_{} chars, ~{tokens} tokens_\n\n```text\n{prompt}\n```",
            prompt.len()
        );
    }
    let _ = write!(
        out,
        "\n\n---\n\n_~{total} tokens across {} roles; the shared method policy is ~{} of them, \
         repeated in every one._\n",
        prompts.by_role().len(),
        estimate_tokens(SHARED_METHOD_POLICY)
    );
    Ok(out)
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
            ("sat_solver", self.sat_solver.as_str()),
            ("smt_solver", self.smt_solver.as_str()),
            ("theorem_prover", self.theorem_prover.as_str()),
            ("symbolic_math", self.symbolic_math.as_str()),
            ("lean_prover", self.lean_prover.as_str()),
            ("reflection", self.reflection.as_str()),
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
fn role_context(role: &str) -> &'static [&'static str] {
    match role {
        "orchestrator" | "goals" => &[
            "config/config.toml",
            "GOAL.md",
            "TASKS.md",
            "code/lib/INDEX.md",
            "research/CLAIMS.md",
            "research/THREADS.md",
            "research/APPROACHES.md",
            // The open gaps are the run's stock of ready-made tasks: a lemma
            // with a first move somebody could make today. A planner that
            // cannot see them plans around them.
            "research/BACKWARD.md",
            // And the graph over them, which answers the question the flat list
            // cannot: which of those tasks can be handed to a sub-agent *now*,
            // because everything it rests on is settled. A planner routing work
            // to concurrent children needs exactly that distinction, and
            // `BACKWARD.md` makes every open gap look equally attackable.
            "research/BLUEPRINT.md",
            // What the library gives without new work. A planner that cannot
            // see this schedules an attempt at something the run already holds,
            // which is the most expensive mistake available to it.
            "research/ENTAILMENT.md",
            // What the other schools have said. A planner deciding what to
            // spend the next run on is the reader a dead end found once and
            // paid for once was written for.
            board::PATH,
            "CONTEXT.md",
        ],
        "tool_builder" | "coder" | "sat_solver" | "smt_solver" | "theorem_prover"
        | "symbolic_math" | "lean_prover" => &[
            "config/config.toml",
            "GOAL.md",
            "TASKS.md",
            "code/AGENTS.md",
            "code/INDEX.md",
            "code/lib/INDEX.md",
            "research/CLAIMS.md",
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
        "reflection" => &["GOAL.md", "TASKS.md", "INDEX.md", board::PATH],
        "pattern_finder" => &["GOAL.md", "code/lib/INDEX.md", board::PATH, "CONTEXT.md"],
        // The scholar writes the claim blocks, so it is the role that draws the
        // `follows-from:` edges — and the one that should see what those edges
        // already establish before recording a statement the library entails.
        "scholar" => &[
            "GOAL.md",
            "TASKS.md",
            "research/CLAIMS.md",
            "research/ENTAILMENT.md",
            "research/THREADS.md",
            "CONTEXT.md",
        ],
        "librarian" | "research" => &[
            "GOAL.md",
            "research/CLAIMS.md",
            "research/THREADS.md",
            "research/APPROACHES.md",
            "research/FRONTIER.md",
            "CONTEXT.md",
        ],
        // The inventor is also handed a dossier assembled from disk at the
        // moment it is delegated to, which is what it actually reasons from —
        // see [`dossier`] for why a prompt loaded at startup is the wrong
        // record for this role. These files remain because a run may reach the
        // inventor by a path that does not build one.
        "inventor" => &[
            "GOAL.md",
            "research/THREADS.md",
            "research/APPROACHES.md",
            "research/CLAIMS.md",
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
            "research/BACKWARD.md",
            "research/BLUEPRINT.md",
            "research/CLAIMS.md",
            "research/THREADS.md",
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
            "research/WEAKENED.md",
            "research/CLAIMS.md",
            "research/THREADS.md",
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
        "searcher" => &["GOAL.md", "research/CLAIMS.md", "CONTEXT.md"],
        // The refuter is sent the two ledgers holding statements somebody has
        // committed to proving, because those are the ones worth attacking, and
        // the claim ledger so it does not spend a cycle refuting something the
        // run already disproved. Not the threads or the approach ledger: which
        // direction the run is pursuing is irrelevant to whether the statement
        // is true, and a role given the method ledger drifts into commenting on
        // the method.
        "refuter" => &[
            "GOAL.md",
            "research/BACKWARD.md",
            "research/WEAKENED.md",
            "research/CLAIMS.md",
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
            "TASKS.md",
            "INDEX.md",
            "research/CLAIMS.md",
            "research/THREADS.md",
            "research/APPROACHES.md",
            "research/BACKWARD.md",
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
            "TASKS.md",
            "research/THREADS.md",
            "research/APPROACHES.md",
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
const LEDGER_BRIEF_WITHHELD: [&str; 2] = ["judge", "searcher"];

const LEDGER_WRITER_ROLES: [&str; 5] = [
    "goals",
    "orchestrator",
    "director",
    "reflection",
    "reducer",
];

/// What `role` is told about the ledgers, appended to its own guidance.
///
/// Returns the empty string only for a role the reader brief is withheld from
/// and that cannot write — which is the judge and the searcher, and nothing
/// else. See [`LEDGER_BRIEF_WITHHELD`].
fn ledger_layer(role: &str) -> String {
    let mut layer = String::new();
    if !LEDGER_BRIEF_WITHHELD.contains(&role) {
        layer.push_str("\n\n");
        layer.push_str(LEDGER_BRIEF.trim());
    }
    if LEDGER_WRITER_ROLES.contains(&role) {
        layer.push_str("\n\n");
        layer.push_str(LEDGER_WRITING_BRIEF.trim());
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
            let context = load_workspace_files(workspace, &files)?;
            let guidance = load_workspace_files(workspace, &[&format!("prompts/{name}.md")])?;
            // Appended to the role's own guidance rather than prepended to the
            // shared prefix: this text is per-role, and `workspace_prompt`
            // orders most-shared-to-least so the provider cache keys on a block
            // every agent has in common. A per-role brief at the front would
            // give each role its own cache namespace.
            let guidance = format!("{guidance}{}", ledger_layer(name));
            // Concatenated rather than branched: an empty layer leaves `base`
            // exactly as it was, and `workspace_prompt` trims what it is given,
            // so the control school's output is unchanged to the byte.
            let base = format!("{}{base}", school_layer(school, name, siblings));
            Ok(workspace_prompt(&base, &context, &guidance))
        };
        Ok(Self {
            orchestrator: role("orchestrator", ORCHESTRATOR_PROMPT)?,
            research: role("research", RESEARCH_PROMPT)?,
            tool_builder: role("tool_builder", TOOL_BUILDER_PROMPT)?,
            coder: role("coder", CODER_PROMPT)?,
            sat_solver: role("sat_solver", SAT_SOLVER_PROMPT)?,
            smt_solver: role("smt_solver", SMT_SOLVER_PROMPT)?,
            theorem_prover: role("theorem_prover", THEOREM_PROVER_PROMPT)?,
            symbolic_math: role("symbolic_math", SYMBOLIC_MATH_PROMPT)?,
            lean_prover: role("lean_prover", LEAN_PROVER_PROMPT)?,
            goals: role("goals", GOALS_PROMPT)?,
            reflection: role("reflection", REFLECTION_PROMPT)?,
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
