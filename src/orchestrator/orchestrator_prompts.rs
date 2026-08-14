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
        "judge" => &["GOAL.md", "INDEX.md"],
        "reflection" => &["GOAL.md", "TASKS.md", "INDEX.md"],
        "pattern_finder" => &["GOAL.md", "code/lib/INDEX.md", "CONTEXT.md"],
        "scholar" => &[
            "GOAL.md",
            "TASKS.md",
            "research/CLAIMS.md",
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
        "reducer" => &[
            "GOAL.md",
            "research/BACKWARD.md",
            "research/CLAIMS.md",
            "research/THREADS.md",
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

impl RolePrompts {
    /// Loads each role's prompt: built-in policy, the workspace context that
    /// role is entitled to, then its `prompts/<role>.md` guidance.
    ///
    /// # Errors
    ///
    /// Returns an error when a workspace file is unreadable, oversized, or not
    /// UTF-8. A file that is simply absent is skipped.
    fn load(workspace: &Path) -> Result<Self> {
        let role = |name: &str, base: &str| -> Result<String> {
            let mut files: Vec<&str> = UNIVERSAL_CONTEXT.to_vec();
            files.extend_from_slice(role_context(name));
            let context = load_workspace_files(workspace, &files)?;
            let guidance = load_workspace_files(workspace, &[&format!("prompts/{name}.md")])?;
            Ok(workspace_prompt(base, &context, &guidance))
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
