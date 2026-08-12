#[test]
fn the_coding_agent_can_write_and_run_the_program_it_owns() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let coder = registry
        .get("coder")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("coder is registered".into()))?;
    for needed in ["write_tool_file", "execute_command"] {
        assert!(
            coder.tools.iter().any(|tool| tool == needed),
            "coder must have `{needed}`"
        );
    }
    // It implements from an established result rather than going to find one.
    assert!(!coder.tools.iter().any(|tool| tool == "exa_search"));
    Ok(())
}

#[test]
fn both_code_writing_roles_see_the_same_working_context() {
    // They differ in mandate, not in what they need to know: what is being
    // attempted and what is already built. The provisional numbers are not
    // among them any more: they are recalled on demand from the scratch.
    assert_eq!(role_context("coder"), role_context("tool_builder"));
    assert_eq!(role_context("sat_solver"), role_context("tool_builder"));
    assert_eq!(role_context("lean_prover"), role_context("tool_builder"));
    for role in ["smt_solver", "theorem_prover", "symbolic_math"] {
        assert_eq!(role_context(role), role_context("tool_builder"), "{role}");
    }
    assert!(!role_context("coder").contains(&"SCRATCHPAD.md"));
    assert!(role_context("coder").contains(&"code/lib/INDEX.md"));
    // An encoding rests on what the run believes about the objects it encodes,
    // and a bound the library already establishes removes constraints.
    assert!(role_context("sat_solver").contains(&"research/CLAIMS.md"));
}

#[test]
fn the_solving_agent_encodes_rather_than_searches() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let solver = registry
        .get("sat_solver")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("solver is registered".into()))?;
    // It writes the encoding and runs the engine over it, like any other
    // program: the solvers are libraries and binaries in the image, not tools
    // of their own, so a new engine is an image change rather than a schema.
    for needed in ["write_tool_file", "execute_command"] {
        assert!(
            solver.tools.iter().any(|tool| tool == needed),
            "solver must have `{needed}`"
        );
    }
    // It is handed a reduced problem, not a topic to go and investigate.
    assert!(!solver.tools.iter().any(|tool| tool == "exa_search"));
    // The planners can reach it, or it may as well not exist.
    assert!(SPECIALISTS.contains(&"sat_solver"));
    assert!(DELEGATES.contains(&"sat_solver"));
    Ok(())
}

#[test]
fn the_solver_prompt_states_the_verdicts_that_are_not_answers() {
    // The failure this role produces is reporting a solver's non-answer as an
    // answer: `FEASIBLE` on an optimisation problem is a bound, `UNKNOWN` is a
    // timeout, and `INFEASIBLE` is a result that must never be relaxed away.
    for verdict in ["FEASIBLE", "UNKNOWN", "INFEASIBLE", "UNSAT"] {
        assert!(
            SAT_SOLVER_PROMPT.contains(verdict),
            "the solver prompt must say what `{verdict}` means"
        );
    }
    // Every engine the image installs is named, or the role will reimplement
    // the search it exists to avoid.
    for engine in ["cp_model", "pysat", "z3", "cvc5", "cbc"] {
        assert!(
            SAT_SOLVER_PROMPT.contains(engine),
            "the solver prompt must name `{engine}`"
        );
    }
}

#[test]
fn the_formalisation_agent_must_report_what_the_kernel_checked() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let lean = registry.get("lean_prover").ok_or_else(|| {
        tinyagents::TinyAgentsError::Validation("lean_prover is registered".into())
    })?;
    for needed in ["write_tool_file", "execute_command"] {
        assert!(
            lean.tools.iter().any(|tool| tool == needed),
            "lean_prover must have `{needed}`"
        );
    }
    assert!(SPECIALISTS.contains(&"lean_prover"));
    assert!(DELEGATES.contains(&"lean_prover"));
    // The two ways a formalisation lies: an undeclared `sorry`, and a proof
    // resting on an axiom nobody looked at. Both are checkable mechanically
    // and the prompt has to name the check.
    for rule in ["sorry", "#print axioms", "sorryAx"] {
        assert!(
            LEAN_PROVER_PROMPT.contains(rule),
            "the lean prompt must require `{rule}`"
        );
    }
    // Mathlib is pre-built and read-only at runtime. A role that tries to
    // build it from source spends the entire run on it.
    assert!(LEAN_PROVER_PROMPT.contains("lake exe cache get"));
    Ok(())
}

#[test]
fn learning_and_research_indexes_are_not_prompt_context() {
    for role in SPECIALISTS.into_iter().chain(DELEGATES) {
        assert!(!role_context(role).contains(&"reflections/INDEX.md"));
        assert!(!role_context(role).contains(&"research/INDEX.md"));
    }
}

#[test]
fn the_shared_brief_reaches_the_roles_that_reason_and_not_the_ones_that_file() {
    // `CONTEXT.md` is the research team's synthesis: what the library means
    // for this problem, as against `research/INDEX.md`, which says only what
    // each file is. Every role that decides what to attempt, build, or propose
    // needs the synthesis; the roles that file and judge do not.
    for role in [
        "goals",
        "orchestrator",
        "tool_builder",
        "coder",
        "sat_solver",
        "smt_solver",
        "theorem_prover",
        "symbolic_math",
        "lean_prover",
        "pattern_finder",
        "scholar",
        "librarian",
        "research",
        "inventor",
        // The role that writes it has to see what it is amending.
        "context_curator",
    ] {
        assert!(
            role_context(role).contains(&"CONTEXT.md"),
            "{role} reasons about the mathematics and needs the shared brief"
        );
    }
    // Reflection judges an attempt against the criteria and the record. A
    // standing brief of what sources assert is exactly the material it must
    // not mistake for verification.
    assert!(!role_context("reflection").contains(&"CONTEXT.md"));
}

#[test]
fn the_curator_maintains_the_brief_and_cannot_investigate() -> agent::Result<()> {
    // Every tool it lacks is a way that curating what the run knows cannot
    // turn into a second investigation running beside the solve. It reads
    // widely — the workspace and both halves of durable memory — and the only
    // thing it produces is one file.
    let registry = default_registry(true)?;
    let definition = registry.get("context_curator").ok_or_else(|| {
        tinyagents::TinyAgentsError::Validation("context_curator is registered".into())
    })?;
    for expected in ["recall_memory", "relate_memory", "write_document"] {
        assert!(
            definition.tools.iter().any(|tool| tool == expected),
            "the curator needs {expected}"
        );
    }
    for forbidden in [
        "exa_search",
        "execute_command",
        "write_tool_file",
        "apply_patch",
        "spawn_agent",
    ] {
        assert!(
            !definition.tools.iter().any(|tool| tool == forbidden),
            "the curator must not hold {forbidden}"
        );
    }
    Ok(())
}

#[test]
fn the_brief_is_curated_by_a_standing_team_at_the_configured_rate() {
    // A brief nobody maintains is the state this team exists to end: the file
    // was written by whichever role happened to think of it, so it drifted
    // behind the run that reads it on every model call.
    let (name, agent, completion, budget, brief) = super::standing_teams()
        .into_iter()
        .find(|(name, ..)| *name == "context")
        .expect("the curator runs as a standing team");
    assert_eq!(agent, "context_curator");
    // Its file keeps changing underneath it, so "nothing to add right now" is
    // come back later rather than stop — the distinction that cost an earlier
    // background team its whole allowance on cycle one.
    assert_eq!(completion, super::teams::Completion::Standing);
    assert_eq!(budget.min_interval, super::shared_context::cycle_interval());
    assert!(brief.contains("NOTHING FURTHER"));
    assert_eq!(name, "context");
}

#[tokio::test]
async fn a_command_that_hits_the_ceiling_still_returns_what_it_printed() {
    use crate::agent::Tool as _;

    // `Command::output()` inside a `timeout` drops the read mid-flight, so a
    // program that printed for nine minutes and then hit the ceiling returned
    // the agent nothing at all. Two such commands cost one live run twenty of
    // its first forty-four minutes and taught it nothing either time.
    let root = std::env::temp_dir().join(format!("math-agent-timeout-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the workspace is creatable");
    let tool = super::ExecuteCommand::new(root.clone(), std::time::Duration::from_secs(1));

    let result = tool
        .call(
            &(),
            crate::agent::ToolCall {
                id: "call-1".into(),
                name: "execute_command".into(),
                invalid: None,
                arguments: serde_json::json!({
                    "command": "echo reached n=41; sleep 30",
                    "complexity": "linear in n",
                    "complexity_class": "linear"
                }),
            },
        )
        .await
        .expect("a killed command is a result, not an error");

    assert!(
        result.content.contains("reached n=41"),
        "how far it got survives the kill: {}",
        result.content
    );
    assert!(
        result.content.contains("timed out"),
        "the ceiling is reported: {}",
        result.content
    );
    let _ = std::fs::remove_dir_all(&root);
}

#[test]
fn every_reasoning_specialist_is_registered_and_reachable() -> agent::Result<()> {
    // Each answers a question the others answer badly: a finite encoding, a
    // theory, first-order axioms, exact algebra, a kernel-checked proof. A role
    // the planners cannot reach may as well not exist, which is how
    // `lean_prover` once shipped registered-but-unspawnable.
    let registry = default_registry(true)?;
    for role in [
        "sat_solver",
        "smt_solver",
        "theorem_prover",
        "symbolic_math",
        "lean_prover",
    ] {
        let agent = registry.get(role).ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("{role} is registered"))
        })?;
        for needed in ["write_tool_file", "execute_command"] {
            assert!(
                agent.tools.iter().any(|tool| tool == needed),
                "{role} must have `{needed}`"
            );
        }
        // Handed a reduced question, not a topic to go investigate.
        assert!(
            !agent.tools.iter().any(|tool| tool == "exa_search"),
            "{role}"
        );
        assert!(SPECIALISTS.contains(&role), "{role} unreachable from goals");
        assert!(
            DELEGATES.contains(&role),
            "{role} unreachable from orchestrator"
        );
    }
    Ok(())
}

#[test]
fn each_solver_prompt_names_the_verdict_that_is_not_an_answer() {
    // The shared failure of every automated prover: a status that means the
    // search gave up, reported as though it settled something.
    assert!(SMT_SOLVER_PROMPT.contains("unknown"));
    assert!(SMT_SOLVER_PROMPT.contains("get-unsat-core"));
    // The check that stops a vacuous proof: contradictory hypotheses make
    // everything follow, so `unsat` alone proves nothing.
    assert!(SMT_SOLVER_PROMPT.contains("already contradictory"));
    assert!(THEOREM_PROVER_PROMPT.contains("ResourceOut"));
    assert!(THEOREM_PROVER_PROMPT.contains("CounterSatisfiable"));
    assert!(THEOREM_PROVER_PROMPT.contains("consistent before believing"));
    // Symbolic work fails by agreeing numerically rather than exactly.
    assert!(SYMBOLIC_MATH_PROMPT.contains("simplify(A - B)"));
    assert!(SYMBOLIC_MATH_PROMPT.contains("unverified"));
}

#[test]
fn every_reasoning_role_can_reach_what_the_run_already_knows() -> agent::Result<()> {
    // The two ways back into what is established: this workspace's own record,
    // and the note store that outlives it. A role holding neither re-derives
    // what is on disk, which is the most expensive way to learn it was known.
    let registry = default_registry(true)?;
    for role in [
        "goals",
        "research",
        "coder",
        "sat_solver",
        "smt_solver",
        "theorem_prover",
        "symbolic_math",
        "lean_prover",
        "reflection",
        "pattern_finder",
        "inventor",
        "librarian",
        "scholar",
    ] {
        let definition = registry
            .get(role)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{role} registered")))?;
        for expected in ["recall_memory", "remember_memory"] {
            assert!(
                definition.tools.iter().any(|tool| tool == expected),
                "`{role}` must be able to reach `{expected}`"
            );
        }
    }

    let builder = registry.get("tool_builder").ok_or_else(|| {
        tinyagents::TinyAgentsError::Validation("tool_builder is registered".into())
    })?;
    assert!(builder.tools.iter().any(|tool| tool == "recall_memory"));
    assert!(builder.tools.iter().any(|tool| tool == "remember_memory"));
    Ok(())
}

#[test]
fn the_judge_reads_a_file_and_looks_nothing_up() -> agent::Result<()> {
    // Twelve model calls and five minutes, against an attempt that took the
    // better part of an hour. Every way of looking something up is a way of
    // spending them looking things up instead of answering, and a live judge
    // did exactly that with the document tools alone. So the judge holds one
    // tool — read a file, to check a claim in the report against disk — and
    // recall, which every other reasoning role gets, is withheld here for the
    // same reason `search_workspace` always was.
    let registry = default_registry(true)?;
    let definition = registry
        .get("judge")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("judge registered".into()))?;
    assert_eq!(definition.tools, vec!["read_document".to_string()]);
    Ok(())
}

#[test]
fn every_agent_but_the_judge_can_write_durable_memory() -> agent::Result<()> {
    // The judge is the one exemption, and it is a budget rather than a
    // preference: see `the_judge_reads_a_file_and_looks_nothing_up`. Everything
    // else that reasons must be able to leave what it established where the
    // next run finds it.
    let registry = default_registry(true)?;
    for role in registry.definitions() {
        if role.id == "judge" {
            assert!(
                !role.tools.iter().any(|tool| tool == "remember_memory"),
                "the judge must not carry durable memory"
            );
            continue;
        }
        assert!(
            role.tools.iter().any(|tool| tool == "remember_memory"),
            "{}",
            role.id
        );
    }
    Ok(())
}

#[test]
fn the_goals_prompt_says_a_turn_without_a_tool_call_produced_nothing() {
    // The failure this guards. `goals` reached the 12,000-token output ceiling
    // with no tool call four times across recent builds — once after eight
    // minutes of generation — leaving its run exactly where it started. The
    // prompt told it what to spawn and never told it that the text of a turn is
    // discarded, so a long deliberation read as work.
    //
    // Asserted rather than trusted because this is the one instruction whose
    // absence is invisible: a prompt that has lost it still reads complete, and
    // the cost shows up as a wall clock nobody attributes to a missing sentence.
    let lower = GOALS_PROMPT.to_ascii_lowercase();
    assert!(
        lower.contains("without a tool call"),
        "the goals prompt must say what an empty turn costs"
    );
    assert!(
        lower.contains("discarded"),
        "it must say the turn's text is not kept, which is why an empty turn is empty"
    );
    // The evidence has to travel with the rule. A bare instruction to be brief
    // is the kind a model weighs against the analysis it wants to write; the
    // measured eight minutes is what makes it a cost rather than a preference.
    assert!(
        lower.contains("eight minutes"),
        "it must carry the measurement, not just the instruction"
    );
}

#[test]
fn the_librarian_is_told_a_cited_source_must_be_in_the_library() {
    // A source named in a note but absent from `research/sources/` is recall,
    // not evidence — and recall is what this role exists to replace. A live
    // Erdős–Gyárfás run cited Wikipedia and Wolfram MathWorld in `ROOT.md` and
    // two summaries with neither downloaded: nothing in the workspace, nothing
    // in the 342-entry frontier, and no way to check what those pages said.
    let lower = LIBRARIAN_PROMPT.to_ascii_lowercase();
    assert!(
        lower.contains("cited"),
        "the rule about citing what is not held must survive edits"
    );
    assert!(
        lower.contains("encyclopedic entry"),
        "the canonical reference tier must be named, or it stays a search away"
    );
    // Breadth is the other half. A library of six papers on one method cannot
    // show the run the method it has no source for.
    assert!(
        lower.contains("wide before deep"),
        "the librarian must be told to cover the subject, not one thread of it"
    );
}

#[test]
fn a_planner_names_every_specialist_it_can_delegate_to() {
    // A role can be registered, tool-equipped, prompt-written, and provisioned
    // in the image, and still never run: the agent holding its delegation tool
    // has to know it exists. Both prompts enumerate a bench, and an enumeration
    // reads as complete, so a name missing from it is a role switched off.
    //
    // This is not hypothetical. `sat_solver`, `smt_solver`, `theorem_prover`,
    // `symbolic_math`, and `lean_prover` were all absent from the goals prompt,
    // and a live run on a closed-form probability problem — exactly what
    // `symbolic_math` exists for — spawned none of them and had `tool_builder`
    // do the exact arithmetic instead.
    // One role is exempt, because delegation is not the only way it runs: the
    // runtime runs `pattern_finder` as a standing team beside the solve, so a
    // planner that never names it still gets it. Every other role on these
    // benches runs if and only if it is delegated to.
    let self_starting = ["pattern_finder"];
    for (role, prompt, bench) in [
        ("goals", GOALS_PROMPT, SPECIALISTS.as_slice()),
        ("orchestrator", ORCHESTRATOR_PROMPT, DELEGATES.as_slice()),
    ] {
        for specialist in bench.iter().filter(|name| !self_starting.contains(*name)) {
            assert!(
                prompt.contains(specialist),
                "the {role} prompt must name `{specialist}`, or the role never runs"
            );
        }
    }
}

#[test]
fn a_search_strategy_is_not_a_complexity() {
    // The exact declaration a live Project Euler 185 run was allowed through
    // with: a method name, no bound, on ten quadrillion candidates, against a
    // `sat_solver` the run never spawned.
    let refused = validate_complexity("backtracking with pruning", "polynomial", None)
        .expect_err("a search strategy declared as a complexity must be refused");
    let message = refused.to_string();
    assert!(
        message.contains("sat_solver"),
        "the refusal must name the role that does this properly: {message}"
    );
    assert!(
        message.contains("oracle_bound"),
        "and how to declare it honestly if it is the oracle: {message}"
    );

    for prose in [
        "brute force over all assignments",
        "brute-force search",
        "exhaustive search of the state space",
        "branch and bound over candidates",
    ] {
        assert!(
            validate_complexity(prose, "polynomial", None).is_err(),
            "`{prose}` states no cost and must be refused"
        );
    }
}

#[test]
fn a_bounded_oracle_may_search_however_it_likes() {
    // Rule 8 requires the naive program and requires keeping it. A gate that
    // refused an honestly-bounded backtracking oracle would block the method
    // policy's own first step — which is the failure this function was
    // rewritten once already to stop committing.
    validate_complexity(
        "backtracking over all fillings",
        "polynomial",
        Some("n <= 7"),
    )
    .expect("a bounded oracle is legitimate however it searches");
    validate_complexity("exhaustive, O(n!)", "factorial", Some("n <= 8"))
        .expect("a declared factorial oracle with a bound stays legitimate");
}

#[test]
fn an_honest_polynomial_cost_still_passes() {
    // The list must not punish accuracy. "Enumerate the divisors" is a truthful
    // description of an O(sqrt n) method, and `enumerate` is deliberately not a
    // matched term for that reason.
    for prose in [
        "O(n log n) sort then a linear scan",
        "enumerate the divisors of n, O(sqrt(n))",
        "binary search over the answer, O(log n) probes",
        "O(n^3) Hungarian algorithm via scipy",
    ] {
        assert!(
            validate_complexity(prose, "polynomial", None).is_ok(),
            "`{prose}` is an honest cost and must be allowed"
        );
    }
}

#[test]
fn the_research_team_gathers_by_default_and_never_retires() {
    // The failure this closes. The team's brief opened "Keep this run's
    // reference library useful, which mostly means not adding to it", and made
    // fetching conditional on an attempt reporting STUCK or REQUESTS.md naming
    // a gap. Neither can hold at t=0 — attempt 1 has just started and a fresh
    // workspace has no REQUESTS.md — so it replied NOTHING FURTHER, and being
    // `Attainable` that retired it permanently. All four live runs lost their
    // research team inside ninety seconds and ran for hours with zero
    // `exa_search` calls.
    let (_, _, completion, _, brief) = super::standing_teams()
        .into_iter()
        .find(|(name, ..)| *name == "research")
        .expect("the research team is registered");

    assert_eq!(
        completion,
        super::teams::Completion::Standing,
        "one quiet cycle must pause the team, not end it"
    );
    let brief = brief.to_ascii_lowercase();
    assert!(
        brief.contains("exa_search"),
        "the strongest search instrument must be named, or it stays unused"
    );
    assert!(
        !brief.contains("mostly means not adding to it"),
        "the brief must not open by discouraging the team's own job"
    );
    // The guard against inventing URLs, which is what a role told to fetch does
    // when it cannot search.
    assert!(
        brief.contains("never download a url you have not seen"),
        "a fetch of an invented address succeeds and stores the wrong paper"
    );
}
