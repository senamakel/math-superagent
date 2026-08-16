#[test]
fn registry_resolves_agents_in_insertion_order() -> agent::Result<()> {
    let mut registry = AgentRegistry::new();
    registry
        .register(AgentDefinition::new(
            "research",
            "Research",
            "finds evidence",
        ))?
        .register(AgentDefinition::new(
            "tool_builder",
            "Tool Builder",
            "builds tools",
        ))?;

    assert_eq!(registry.names(), vec!["research", "tool_builder"]);
    assert!(registry.get("research").is_some());
    assert!(registry.get("missing").is_none());
    Ok(())
}

#[test]
fn registry_rejects_duplicate_ids() -> agent::Result<()> {
    let mut registry = AgentRegistry::new();
    registry.register(AgentDefinition::new(
        "research",
        "Research",
        "finds evidence",
    ))?;

    let duplicate = registry.register(AgentDefinition::new("research", "Other", "duplicate"));
    assert!(duplicate.is_err());
    Ok(())
}

#[test]
fn the_pattern_team_skips_a_cycle_over_results_it_has_already_seen() {
    // Idleness has to be decided before the agent runs. Asking it to notice
    // that nothing changed costs a model call and a walk of the workspace to
    // discover — most of what a working cycle costs — and a live team spent
    // thirty `read_document` calls in two minutes doing exactly that.
    let root = std::env::temp_dir().join(format!("math-agent-pattern-idle-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    let _ = std::fs::create_dir_all(&root);
    let seen = std::sync::Arc::new(std::sync::Mutex::new(None));

    // Nothing computed yet: idle rather than analysing an empty folder.
    assert_eq!(
        super::results_unchanged(&root, &seen),
        Some(super::teams::Cycle::Idle)
    );

    let _ = std::fs::create_dir_all(root.join("code/out"));
    let _ = std::fs::write(root.join("code/out/first.txt"), "1 2 3");
    // New results: the cycle runs.
    assert_eq!(super::results_unchanged(&root, &seen), None);
    // Same results: it does not run again.
    assert_eq!(
        super::results_unchanged(&root, &seen),
        Some(super::teams::Cycle::Idle)
    );

    let _ = std::fs::write(root.join("code/out/second.txt"), "5 8 13");
    assert_eq!(super::results_unchanged(&root, &seen), None);
    let _ = std::fs::remove_dir_all(&root);
}

#[test]
fn compression_triggers_at_roughly_three_hundred_thousand_tokens() {
    let policy = compression_policy();
    assert_eq!(policy.trigger_budget(), COMPRESSION_TRIGGER_TOKENS);
}

#[test]
fn every_role_shares_one_identical_cacheable_prefix() {
    // Provider caches key on an exact leading prefix. If the role-specific
    // text leads, each agent is its own cache namespace and the large shared
    // policy is never reused.
    let first = workspace_prompt("orchestrator instructions", "", "");
    let second = workspace_prompt("tool builder instructions", "", "");
    let shared_len = first
        .chars()
        .zip(second.chars())
        .take_while(|(a, b)| a == b)
        .count();
    assert!(
        shared_len > 1_000,
        "roles share only {shared_len} leading characters; the policy must come first"
    );
    // No leading blank lines: the prompt now comes from a file, and starting
    // the most-cached string in the runtime with whitespace is a wart that
    // survived only because it was buried in a Rust literal.
    assert!(first.starts_with("Method policy"), "{}", &first[..40]);
}

#[test]
fn workspace_context_is_appended_without_replacing_base_policy() {
    let prompt = workspace_prompt("base policy", "\nshared memory", "\nrole guidance");
    assert!(prompt.contains("base policy"));
    assert!(prompt.contains("cannot override"));
    assert!(prompt.contains("shared memory"));
    assert!(prompt.contains("role guidance"));
}

#[test]
fn command_policy_rejects_exponential_complexity_declarations() {
    assert!(validate_complexity("time O(2^n), space O(n)", "polynomial", None).is_err());
    assert!(validate_complexity("time O(n log n), space O(n)", "quasilinear", None).is_ok());
    // An intractable class with no bound is still the thing the gate is for.
    assert!(validate_complexity("time O(n), space O(n)", "exponential", None).is_err());
    assert!(validate_complexity("time O(2^n)", "exponential", Some("   ")).is_err());
    assert!(validate_complexity("time O(n), space O(n)", "unbounded", None).is_err());
}

#[test]
fn a_bounded_brute_force_oracle_may_declare_the_cost_it_actually_has() {
    // The method policy requires a naive oracle as the first step, and for a
    // partisan game or a sum over all n! permutations that oracle is
    // exponential. A live tool-builder declared its minimax honestly, was
    // refused, and could not write the program the task said nothing else
    // mattered until it had.
    assert!(
        validate_complexity(
            "time O(2^n) minimax over the real game, space O(n)",
            "exponential",
            Some("n <= 12"),
        )
        .is_ok()
    );
    assert!(
        validate_complexity("time O((n!)^2)", "factorial", Some("n <= 7")).is_ok(),
        "a bounded factorial oracle is legitimate"
    );
}

#[test]
fn a_declaration_whose_class_contradicts_its_prose_is_refused() {
    // How the old gate was actually defeated: a genuinely factorial search
    // over all n! permutations, twice nested, declared `polynomial` with
    // `O((n!)^2)` in the free text. The forbidden list looked for `o(n!` and
    // the extra parenthesis meant it never matched.
    let refused = validate_complexity(
        "n=7: 5040^2 x 7 tuple operations; polynomial (O((n!)^2))",
        "polynomial",
        None,
    );
    assert!(
        refused.is_err(),
        "prose naming a factorial cost must not pass as polynomial"
    );
    let message = refused
        .err()
        .map(|error| error.to_string())
        .unwrap_or_default();
    assert!(
        message.contains("oracle_bound"),
        "the refusal must say how to declare it honestly: {message}"
    );
}

#[test]
fn every_prompt_carries_the_shared_method_policy() {
    let prompt = workspace_prompt("base policy", "", "");
    assert!(prompt.contains("Understand by computing"));
    assert!(prompt.contains("candidate answers"));
    // The rule that actually prevents a run spending itself on documentation.
    assert!(prompt.contains("no program executed"));
    assert!(prompt.contains("second, different route"));
    // The obligations the workspace's own `AGENTS.md` used to restate. It now
    // carries the workspace's layout and nothing about method, so the policy is
    // the only place these are stated and has to keep stating them.
    assert!(prompt.contains("oracle"));
    assert!(prompt.contains("counterexample"));
    assert!(prompt.contains("`.full.md`"));
}

#[test]
fn disabling_research_removes_exa_from_the_advertised_tools() -> agent::Result<()> {
    let enabled = default_registry(true)?;
    let research = enabled
        .get("research")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("research is registered".into()))?;
    assert!(research.tools.iter().any(|tool| tool == "exa_search"));

    let disabled = default_registry(false)?;
    let research = disabled
        .get("research")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("research is registered".into()))?;
    assert!(!research.tools.iter().any(|tool| tool == "exa_search"));
    assert!(research.tools.iter().any(|tool| tool == "recall_memory"));
    Ok(())
}

#[test]
fn the_registry_advertises_every_agent_the_solution_loop_drives() -> agent::Result<()> {
    let registry = default_registry(true)?;
    for expected in [
        "research",
        "tool_builder",
        "goals",
        "reflection",
        "pattern_finder",
        "inventor",
        "reducer",
        "librarian",
    ] {
        assert!(
            registry.contains(expected),
            "`{expected}` must be registered"
        );
    }
    Ok(())
}

/// The reducer reads the whole workspace and writes one kind of file. Every
/// other authority is withheld, and each exclusion is a different failure: a
/// role that can search turns "what would suffice" into a literature survey,
/// one that can compute discharges its own gaps with a program it wrote, and
/// one with a bench runs a second investigation beside the first.
#[test]
fn the_reducer_can_write_notes_but_cannot_compute_or_search() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let reducer = registry
        .get("reducer")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("reducer is registered".into()))?;
    for required in [
        "read_document",
        "write_document",
        "search_claims",
        "request_research",
        "recall_memory",
        "remember_memory",
        "relate_memory",
    ] {
        assert!(
            reducer.tools.iter().any(|tool| tool == required),
            "reducer must have `{required}`"
        );
    }
    for forbidden in [
        "exa_search",
        "oeis_lookup",
        "execute_command",
        "write_tool_file",
        "apply_patch",
        "spawn_agent",
        "await_agent",
        "note_scratch",
        "recall_scratch",
    ] {
        assert!(
            !reducer.tools.iter().any(|tool| tool == forbidden),
            "reducer must not have `{forbidden}`"
        );
    }
    Ok(())
}

/// It holds no research tool either way, so `--no-research` changes nothing
/// about it — which is what having no `research_enabled` branch in its
/// definition is supposed to mean.
#[test]
fn the_reducer_is_the_same_role_with_research_disabled() -> agent::Result<()> {
    let enabled = default_registry(true)?;
    let disabled = default_registry(false)?;
    let tools = |registry: &super::AgentRegistry| {
        registry
            .get("reducer")
            .map(|definition| definition.tools.clone())
    };
    assert_eq!(tools(&enabled), tools(&disabled));
    Ok(())
}

#[test]
fn reflection_has_no_research_or_execution_authority() -> agent::Result<()> {
    // Reflection judges an attempt. Giving it search or a shell would let it
    // drift into solving the problem it is supposed to be assessing.
    let registry = default_registry(true)?;
    let reflection = registry.get("reflection").ok_or_else(|| {
        tinyagents::TinyAgentsError::Validation("reflection is registered".into())
    })?;
    for forbidden in [
        "exa_search",
        "execute_command",
        "write_tool_file",
        "spawn_agent",
    ] {
        assert!(
            !reflection.tools.iter().any(|tool| tool == forbidden),
            "reflection must not have `{forbidden}`"
        );
    }
    Ok(())
}

#[test]
fn pattern_finder_can_test_a_conjecture_but_not_search() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let patterns = registry.get("pattern_finder").ok_or_else(|| {
        tinyagents::TinyAgentsError::Validation("pattern_finder is registered".into())
    })?;
    assert!(patterns.tools.iter().any(|tool| tool == "analyze_sequence"));
    assert!(
        patterns
            .tools
            .iter()
            .any(|tool| tool == "find_linear_recurrence")
    );
    // It computes more terms to attack a conjecture: a fit over the data that
    // suggested it is weak evidence, and the sequence tools cannot extend a
    // sequence, only describe the terms handed to them.
    assert!(patterns.tools.iter().any(|tool| tool == "execute_command"));
    assert!(patterns.tools.iter().any(|tool| tool == "write_tool_file"));
    // Searching is still somebody else's job. The pattern agent reasons from
    // the run's own numbers, and a search tool here turns a bounded structural
    // question into a second investigation.
    assert!(!patterns.tools.iter().any(|tool| tool == "exa_search"));
    Ok(())
}

/// The four ways onto the web that are not a query reach exactly two roles.
///
/// They are gated with `exa_search` because they reach the same open web, and
/// granted no more widely because everything else about the boundary already
/// says so: the pattern agent is denied search so a bounded structural question
/// cannot become a second investigation, and giving it a deep research agent
/// would be a larger version of the same mistake.
#[test]
fn discovery_tools_reach_the_two_gathering_roles_and_are_gated_with_search()
-> agent::Result<()> {
    let enabled = default_registry(true)?;
    for role in ["research", "librarian"] {
        let agent = enabled
            .get(role)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{role} registered")))?;
        for tool in DISCOVERY_TOOLS {
            assert!(
                agent.tools.iter().any(|granted| granted == tool),
                "`{role}` must have `{tool}`"
            );
        }
    }
    for role in ["pattern_finder", "inventor", "scholar", "reducer", "coder"] {
        let agent = enabled
            .get(role)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{role} registered")))?;
        for tool in DISCOVERY_TOOLS {
            assert!(
                !agent.tools.iter().any(|granted| granted == tool),
                "`{role}` must not reach the web through `{tool}`"
            );
        }
    }
    // Withheld by not being granted, on the rule the whole research gate rests
    // on: a prompt instruction is not a control.
    let disabled = default_registry(false)?;
    for role in ["research", "librarian"] {
        let agent = disabled
            .get(role)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{role} registered")))?;
        for tool in DISCOVERY_TOOLS {
            assert!(
                !agent.tools.iter().any(|granted| granted == tool),
                "`{role}` keeps `{tool}` with research disabled"
            );
        }
    }
    Ok(())
}

#[test]
fn disabling_research_also_withholds_search_from_inventor_and_librarian() -> agent::Result<()> {
    let registry = default_registry(false)?;
    for role in ["inventor", "librarian"] {
        let agent = registry
            .get(role)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{role} registered")))?;
        assert!(
            !agent.tools.iter().any(|tool| tool == "exa_search"),
            "`{role}` must not have search when research is disabled"
        );
    }
    Ok(())
}

#[test]
fn reflection_sees_the_criteria_it_judges_against_but_not_scratch_work() {
    let context = role_context("reflection");
    // Judging "solved" against criteria it cannot see is guesswork, and a
    // wrong SOLVED ends the whole investigation.
    assert!(context.contains(&"GOAL.md"));
    // Unsettled scratch work is not evidence of progress. It is no longer a
    // file, so the boundary is now the tool: reflection must not be able to
    // reach the scratch at all.
    assert!(!context.contains(&"SCRATCHPAD.md"));
}

#[test]
fn only_the_roles_doing_provisional_work_can_reach_the_scratch() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let tools = |role: &str| -> agent::Result<Vec<String>> {
        Ok(registry
            .get(role)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{role} registered")))?
            .tools
            .clone())
    };
    for role in [
        "tool_builder",
        "coder",
        "lean_prover",
        "pattern_finder",
        "goals",
    ] {
        let held = tools(role)?;
        for tool in super::SCRATCH_TOOLS {
            assert!(
                held.iter().any(|name| name == tool),
                "`{role}` does provisional work and needs `{tool}`"
            );
        }
    }
    // Reads what a solve is in the middle of; produces none of its own.
    for role in ["scholar", "context_curator"] {
        let held = tools(role)?;
        assert!(held.iter().any(|name| name == super::SCRATCH_READ_TOOL));
        assert!(
            !held.iter().any(|name| name == "note_scratch"),
            "`{role}` has no provisional work of its own to record"
        );
    }
    // The judge answers four lines on twelve model calls, and reflection must
    // not read unsettled arithmetic as progress — the reason SCRATCHPAD.md was
    // withheld from both when it was still a file.
    for role in ["reflection", "judge"] {
        let held = tools(role)?;
        for tool in super::SCRATCH_TOOLS {
            assert!(
                !held.iter().any(|name| name == tool),
                "`{role}` must not reach the scratch"
            );
        }
    }
    Ok(())
}

#[test]
fn the_inventor_sees_what_already_failed() {
    assert!(super::INVENTOR_PROMPT.contains("recall_memory"));
}

#[test]
fn the_pattern_agent_sees_the_raw_data_it_analyses() {
    let context = role_context("pattern_finder");
    assert!(context.contains(&"code/lib/INDEX.md"));
    assert!(super::PATTERN_PROMPT.contains("recall_memory"));
    // Its provisional work is recalled rather than routed into every call.
    assert!(!context.contains(&"SCRATCHPAD.md"));
    assert!(super::PATTERN_PROMPT.contains("note_scratch"));
}

/// `config/config.toml` reaches no prompt at all, and that is the assertion.
///
/// It used to head the two executing arms. Nothing in it was a fact only that
/// file held: its policy lines restate the built-in prompts in TOML, its
/// `[artifacts]` names are stale — `tasks.md` where the runtime writes
/// `derived/TASKS.md`, so a role that believed them wrote where no ledger derives from
/// — and its one hard number is enforced by `execute_command` and named in the
/// error a timeout returns, which is where a limit is actually learned. This
/// is a test rather than a comment because a routed file is the cheapest thing
/// in the runtime to add back.
#[test]
fn no_role_receives_the_runtime_configuration() -> agent::Result<()> {
    use super::{RolePrompts, schools};

    // Every role the runtime assembles a prompt for, rather than a list here
    // that a new role would not be added to.
    let school = schools::ALL.first().expect("a school is defined");
    let prompts = RolePrompts::for_school(template_workspace(), school, true)?;
    for (role, _) in prompts.by_role() {
        assert!(
            !role_context(role).contains(&"config/config.toml"),
            "`{role}` is routed a file it cannot learn anything from"
        );
    }
    Ok(())
}

/// The shared brief is the last workspace file in every role that gets one,
/// whatever order that role's list is written in. Asserted on the assembled
/// prompt rather than on the list, because the sort is the thing under test.
#[test]
fn the_shared_brief_is_the_last_file_every_role_is_sent() {
    let prompts = super::RolePrompts::load(template_workspace()).expect("the prompts assemble");
    for (role, prompt) in prompts.by_role() {
        let Some(brief) = prompt.find("\n## CONTEXT.md\n") else {
            continue;
        };
        for relative in super::UNIVERSAL_CONTEXT
            .iter()
            .chain(role_context(role).iter())
            .filter(|relative| **relative != super::shared_context::CONTEXT_FILE)
        {
            if let Some(other) = prompt.find(&format!("\n## {relative}\n")) {
                assert!(
                    other < brief,
                    "`{role}` reads `{relative}` after the shared brief"
                );
            }
        }
    }
}

#[test]
fn an_unknown_role_receives_no_working_files() {
    assert!(role_context("nonexistent").is_empty());
}

/// A directive is asserted, not established. The role that acts on one is kept
/// away from the evidence ledger so that an instruction cannot be filed beside
/// the things the run actually proved.
#[test]
fn the_director_reads_the_plan_but_not_the_claim_ledger() {
    let context = role_context("director");
    assert!(context.contains(&"derived/TASKS.md"), "it rewrites the plan");
    assert!(
        context.contains(&"GOAL.md"),
        "a directive is read against it"
    );
    assert!(
        context.contains(&"derived/THREADS.md"),
        "opening and closing directions is most of the job"
    );
    assert!(!context.contains(&"derived/CLAIMS.md"));
    assert!(
        !context.contains(&"config/config.toml"),
        "it never executes"
    );
}

/// The director directs; it does not compute. A role that could both
/// reinterpret the goal and run programs against it would be a second
/// investigation answering to nobody.
#[test]
fn the_director_cannot_execute_or_delegate() -> agent::Result<()> {
    let registry = default_registry(false)?;
    let director = registry
        .get("director")
        .expect("the director is registered");
    for withheld in [
        "execute_command",
        "write_tool_file",
        "apply_patch",
        "spawn_agent",
        "exa_search",
    ] {
        assert!(
            !director.tools.iter().any(|tool| tool == withheld),
            "`{withheld}` would make the director a solver"
        );
    }
    assert!(
        director.tools.iter().any(|tool| tool == "write_document"),
        "it has to be able to rewrite the plan"
    );
    Ok(())
}

/// The four standing teams, and the one whose allowance is shaped by waiting
/// rather than by working.
#[test]
fn the_director_team_is_budgeted_to_outlast_a_run_of_idling() {
    let teams = super::standing_teams();
    let (_, agent, completion, budget, _) = teams
        .into_iter()
        .find(|(name, ..)| *name == "director")
        .expect("the director stands beside the solve");
    assert_eq!(agent, "director");
    // Direction can arrive at any moment, so the team never retires itself.
    assert_eq!(completion, super::teams::Completion::Standing);
    // Every cycle counts, idle ones included. At the twenty-second idle
    // backoff a custodial forty-cycle allowance would retire this team
    // thirteen minutes into an eight-hour run, and nothing would say that
    // direction had stopped being read.
    assert!(
        budget.max_cycles >= 2000,
        "an idling team must outlive the solve, got {}",
        budget.max_cycles
    );
    // And no rate floor: a floor is a delay between a person typing and the
    // run noticing. What bounds the spending is the queue check in front of
    // the model call.
    assert_eq!(budget.min_interval, std::time::Duration::ZERO);
}

/// A parsed field no prompt asks for is a field nothing ever writes.
///
/// The entailment closure shipped derived, routed, and documented in its own
/// derived file — and a live run wrote no edges at all, because the claim-block
/// schema in the one prompt that writes claim blocks never mentioned
/// `follows-from`. The whole of that feature depended on one line of prose that
/// was not there.
#[test]
fn the_scholar_is_told_about_every_claim_field_the_ledger_reads() {
    use super::SCHOLAR_PROMPT;

    for field in [
        "id",
        "statement",
        "hypotheses",
        "holds-here",
        "status",
        "bearing",
        "anchor",
        "contradicts",
        "follows-from",
        "answers",
    ] {
        assert!(
            SCHOLAR_PROMPT.contains(field),
            "the claim parser reads `{field}` and the only role that writes claim blocks is \
             never told it exists"
        );
    }
}

#[test]
fn every_built_in_prompt_is_present_and_bounded() {
    use super::{
        GOALS_PROMPT, INVENTOR_PROMPT, LIBRARIAN_PROMPT, ORCHESTRATOR_PROMPT, PATTERN_PROMPT,
        REFLECTION_PROMPT, RESEARCH_PROMPT, SCHOLAR_PROMPT, SHARED_METHOD_POLICY,
        TOOL_BUILDER_PROMPT,
    };

    // The prompts live in `src/prompts/*.md` and are included at compile time.
    // A renamed or emptied file must fail here rather than in a live run.
    for (name, prompt) in [
        ("method_policy", SHARED_METHOD_POLICY),
        ("orchestrator", ORCHESTRATOR_PROMPT),
        ("research", RESEARCH_PROMPT),
        ("tool_builder", TOOL_BUILDER_PROMPT),
        ("reflection", REFLECTION_PROMPT),
        ("pattern_finder", PATTERN_PROMPT),
        ("inventor", INVENTOR_PROMPT),
        ("librarian", LIBRARIAN_PROMPT),
        ("scholar", SCHOLAR_PROMPT),
        ("goals", GOALS_PROMPT),
    ] {
        assert!(
            prompt.trim().len() > 200,
            "{name} prompt is missing or stub"
        );
        // Every prompt is re-sent on every model call in its role's run, so an
        // accidental paste of a whole document into one is a bill, not a typo.
        assert!(
            prompt.len() < 20_000,
            "{name} prompt has grown unreasonably"
        );
    }
}

#[test]
fn the_method_policy_leads_every_assembled_prompt() {
    use super::{SHARED_METHOD_POLICY, workspace_prompt};

    // The provider cache is keyed on the exact leading prefix, so the one part
    // every role shares has to come first or none of them share a prefix.
    let assembled = workspace_prompt("ROLE BODY", "\n\nshared ctx", "\n\nrole ctx");
    assert!(
        assembled.starts_with(SHARED_METHOD_POLICY.trim()),
        "the shared policy must lead"
    );
    assert!(assembled.contains("ROLE BODY"));
    // The gradient is volatility, not topic. A role's own guidance is fixed for
    // the workspace, so it sits with the built-in prompt it continues; the
    // workspace state moves on every write, so it goes last and takes the cache
    // miss alone. These were once the other way round, and a single
    // `record_entry` re-sent the guidance uncached for a change unrelated to it.
    assert!(
        assembled.contains("ROLE BODY\n\nrole ctx"),
        "the role's guidance belongs with the prompt it continues: {assembled}"
    );
    assert!(
        assembled.ends_with("shared ctx"),
        "the most volatile block must be last: {assembled}"
    );
    // Trimmed, so an editor adding a trailing newline to a prompt file cannot
    // silently invalidate every cached prefix.
    assert!(!assembled.contains("\n\n\n"), "{assembled}");
}

/// The searcher's authority is a set of absences, so the absences are asserted.
///
/// A scored search learns to attack its own verifier: `AlphaEvolve` satisfied a
/// minimum-distance constraint by stacking points nearly on top of one another,
/// and Tao's team rewrote every verifier in exact arithmetic in response. The
/// defence here is that the role physically cannot reach `score.py` — it holds
/// no file-write tool and no shell, so `submit_candidate` is its only route to
/// disk and that route writes into `candidates/` and scores what it wrote in
/// the same call.
///
/// This is exactly the kind of boundary that erodes one convenient grant at a
/// time, which is why it is a test rather than a comment.
#[test]
fn the_searcher_cannot_reach_the_scorer_it_is_judged_by() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let searcher = registry
        .get("searcher")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("searcher is registered".into()))?;

    for granted in ["search_brief", "submit_candidate"] {
        assert!(
            searcher.tools.iter().any(|tool| tool == granted),
            "the searcher needs `{granted}` to search at all"
        );
    }
    for withheld in ["write_tool_file", "execute_command", "apply_patch"] {
        assert!(
            !searcher.tools.iter().any(|tool| tool == withheld),
            "`{withheld}` would let the searcher edit the verifier that scores it"
        );
    }
    Ok(())
}

/// The refuter may write its axiomatisation but may not write its own search.
///
/// It needs `write_tool_file`, because the axiomatisation is the whole job and
/// the whole risk — the same reason `theorem_prover` has it. It must not have
/// `execute_command`: a role hunting a counterexample with a shell writes its
/// own search over small cases, which is the answer-space search the method
/// policy prohibits, in the language most likely to hide its own bugs, by the
/// role least able to notice. `find_counterexample` is the engine it is for.
#[test]
fn the_refuter_gets_an_engine_rather_than_a_shell() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let refuter = registry
        .get("refuter")
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation("refuter is registered".into()))?;

    for granted in ["find_counterexample", "write_tool_file"] {
        assert!(
            refuter.tools.iter().any(|tool| tool == granted),
            "the refuter needs `{granted}`"
        );
    }
    assert!(
        !refuter.tools.iter().any(|tool| tool == "execute_command"),
        "a shell would let the refuter hand-roll the search the engine exists to run"
    );
    Ok(())
}

/// The kernel check belongs to the role whose mandate is formalisation.
///
/// `lean_check` decides what `research/CLAIMS.md` may call formalised, which is
/// the ledger's strongest evidence class. Granting it more widely would let a
/// role with no formalisation mandate mint that class — so the grant is
/// asserted to reach exactly one role, in a list that otherwise shares every
/// tool.
#[test]
fn only_the_lean_prover_can_mint_a_formalised_claim() -> agent::Result<()> {
    let registry = default_registry(true)?;
    let mut holders = Vec::new();
    for name in [
        "tool_builder",
        "coder",
        "sat_solver",
        "smt_solver",
        "theorem_prover",
        "symbolic_math",
        "lean_prover",
        "searcher",
        "refuter",
        "reducer",
        "weakener",
        "research",
    ] {
        let Some(definition) = registry.get(name) else {
            continue;
        };
        if definition.tools.iter().any(|tool| tool == "lean_check") {
            holders.push(name);
        }
    }
    assert_eq!(holders, ["lean_prover"]);
    Ok(())
}

/// Where a school's prompts are assembled from, for the tests below.
///
/// The template workspace rather than a temporary directory: it carries the
/// `AGENTS.md` and `prompts/` files a real run has, so these assert on the
/// assembly a run actually sends rather than on a bare built-in prompt.
fn template_workspace() -> &'static std::path::Path {
    std::path::Path::new("workspace/template")
}

/// The control school's prompts are the prompts this runtime already sent.
///
/// Byte-identical, not merely similar. A school is only ever evidence if the
/// control is running beside it unchanged, and an empty policy that added so
/// much as a blank line would have moved the control.
#[test]
fn the_control_school_changes_no_prompt_by_one_byte() {
    use super::{RolePrompts, schools};

    let loaded = RolePrompts::load(template_workspace()).expect("prompts assemble");
    let chisel = RolePrompts::for_school(template_workspace(), &schools::ALL[0], false)
        .expect("the control school's prompts assemble");
    assert_eq!(loaded.by_role(), chisel.by_role());
}

/// Every role that may post to the board is told the board exists.
///
/// This is the test the live run needed and did not have. Three schools ran an
/// hour on Project Euler 1006, all three reached a verdict, all three ran the
/// reflection — and `post_board` was called zero times, because the grant was
/// in the registry and the instruction was nowhere. Registering a tool and
/// asking for it are two different things, and only one of them was done.
#[test]
fn every_role_holding_the_board_tool_is_told_what_it_is_for() {
    use super::{BOARD_ROLES, BOARD_TOOLS, RolePrompts, schools};

    // The tool's own name, which is what is being asserted and which no other
    // prompt in this crate mentions. A prose phrase was tried first and is the
    // wrong marker: `board.md` is hard-wrapped, so a sentence spanning two
    // lines never matches, and the test failed for a reason that had nothing to
    // do with the behaviour under test.
    let distinctive = "post_board";

    for school in schools::ALL {
        let prompts = RolePrompts::for_school(template_workspace(), &school, true)
            .expect("prompts assemble");
        for (role, prompt) in prompts.by_role() {
            let told = prompt.contains(distinctive);
            let granted = BOARD_ROLES.contains(&role);
            assert_eq!(
                told, granted,
                "`{role}` in `{}`: told about the board = {told}, holds it = {granted}",
                school.slug
            );
        }
    }

    // And the list this brief is routed by agrees with the bench that grants
    // the tool. Neither can be derived from the other — the grants live in
    // per-role `&'static str` arrays — so the agreement is asserted here.
    let registry = default_registry(true).expect("the registry builds");
    for role in BOARD_ROLES {
        assert!(
            registry
                .get(role)
                .is_some_and(|bench| bench.tools.iter().any(|tool| *tool == BOARD_TOOLS[0])),
            "`{role}` is told to post to the board but is not a role that was granted \
             `post_board`"
        );
    }
}

/// A school running alone is not told to talk to itself.
///
/// The board costs tokens in every one of those prompts and has no audience in
/// a single-school run, and adding it unconditionally would also move the
/// control off the prompts this runtime sent before schools existed — which
/// [`the_control_school_changes_no_prompt_by_one_byte`] exists to prevent.
#[test]
fn a_lone_school_is_never_told_about_the_board() {
    use super::{RolePrompts, schools};

    let alone = RolePrompts::for_school(template_workspace(), &schools::ALL[0], false)
        .expect("prompts assemble");
    for (role, prompt) in alone.by_role() {
        assert!(
            !prompt.contains("post_board"),
            "`{role}` is running alone and was told to post to a board nobody reads"
        );
    }
}

/// A school's policy reaches every role, and only that school's.
#[test]
fn a_school_policy_reaches_every_role_and_no_other_school() {
    use super::{RolePrompts, schools};

    // A phrase from `src/prompts/schools/rising-sea.md`, distinctive enough
    // that it cannot arrive from anywhere else.
    let distinctive = "Change the ground under it";
    let sea = RolePrompts::for_school(template_workspace(), &schools::ALL[1], false)
        .expect("the rising-sea prompts assemble");
    let chisel = RolePrompts::for_school(template_workspace(), &schools::ALL[0], false)
        .expect("the control school's prompts assemble");
    for (role, prompt) in sea.by_role() {
        assert!(
            prompt.contains(distinctive),
            "`{role}` was never told which school it is working in"
        );
    }
    for (role, prompt) in chisel.by_role() {
        assert!(
            !prompt.contains(distinctive),
            "`{role}` in the control school is carrying another school's policy"
        );
    }
}

/// The shared method policy still leads every prompt in every school.
///
/// The provider cache is keyed on the exact leading prefix, so a school layered
/// in *front* of the shared policy would give each school its own cache
/// namespace and lose the one identical opening block every role shares.
#[test]
fn the_method_policy_still_leads_every_prompt_in_every_school() {
    use super::{RolePrompts, SHARED_METHOD_POLICY, schools};

    for school in schools::ALL {
        let prompts =
            RolePrompts::for_school(template_workspace(), &school, false).expect("prompts assemble");
        for (role, prompt) in prompts.by_role() {
            assert!(
                prompt.starts_with(SHARED_METHOD_POLICY.trim()),
                "`{role}` in `{}` does not open with the shared method policy",
                school.slug
            );
        }
    }
}

/// The school's policy sits between the shared policy and the role's own brief.
#[test]
fn a_school_policy_sits_after_the_shared_policy_and_before_the_role_prompt() {
    use super::{JUDGE_PROMPT, RolePrompts, SHARED_METHOD_POLICY, schools};

    let sea = RolePrompts::for_school(template_workspace(), &schools::ALL[1], false)
        .expect("the rising-sea prompts assemble");
    let judge = sea
        .by_role()
        .into_iter()
        .find(|(role, _)| *role == "judge")
        .map(|(_, prompt)| prompt.to_string())
        .expect("the judge has a prompt");
    let shared = SHARED_METHOD_POLICY.trim().len();
    let school = judge
        .find(schools::ALL[1].policy.trim())
        .expect("the school policy is in the prompt");
    let role = judge
        .find(JUDGE_PROMPT.trim())
        .expect("the role prompt is in the prompt");
    assert!(shared < school, "the school policy preceded the shared one");
    assert!(school < role, "the role prompt preceded the school policy");
}

/// The board reaches the roles that decide what to do next, and no others.
///
/// A post is asserted rather than established — a hunch, a dead end, a lesson
/// offered because it is unfinished — so it goes to the roles choosing the next
/// move and is withheld from every role that weighs evidence or files sources.
#[test]
fn the_board_reaches_the_roles_that_decide_what_to_do_next() {
    use super::{RolePrompts, board, schools};

    let root = std::env::temp_dir().join(format!(
        "math-agent-board-context-{}",
        std::process::id()
    ));
    let _ = std::fs::create_dir_all(root.join("teams"));
    let _ = std::fs::write(
        root.join(board::PATH),
        "# Board\n\n- rising-sea, dead-end: the sheaf route needs f D-finite and it is not\n",
    );
    let prompts =
        RolePrompts::for_school(&root, &schools::ALL[1], false).expect("the rising-sea prompts assemble");
    let prompt_for = |role: &str| {
        prompts
            .by_role()
            .into_iter()
            .find(|(name, _)| *name == role)
            .map(|(_, prompt)| prompt.to_string())
            .expect("the role has a prompt")
    };
    let inventor = prompt_for("inventor");
    assert!(
        inventor.contains(board::PATH),
        "the inventor is not sent the board"
    );
    assert!(
        inventor.contains("needs f D-finite"),
        "the board is listed but its contents never arrive"
    );
    assert!(
        !prompt_for("judge").contains(board::PATH),
        "the judge is scoring an attempt beside a sibling's unevidenced sentence"
    );
    let _ = std::fs::remove_dir_all(&root);

    for role in [
        "orchestrator",
        "goals",
        "inventor",
        "reducer",
        "weakener",
        "reflection",
        "pattern_finder",
    ] {
        assert!(
            role_context(role).contains(&board::PATH),
            "`{role}` decides what to do next and cannot see what the others found"
        );
    }
    for role in ["judge", "scholar", "librarian", "searcher", "refuter"] {
        assert!(
            !role_context(role).contains(&board::PATH),
            "`{role}` weighs evidence and must not be reading assertions beside it"
        );
    }
}

/// Only the three roles that report may post to the board.
#[test]
fn only_the_roles_that_report_may_post_to_the_board() {
    let registry = default_registry(true).expect("the default registry builds");
    let posts = |role: &str| {
        registry
            .get(role)
            .expect("the role is registered")
            .tools
            .iter()
            .any(|tool| tool == "post_board")
    };
    for role in ["reflection", "inventor", "goals"] {
        assert!(posts(role), "`{role}` cannot tell the other schools anything");
    }
    for role in [
        "judge",
        "scholar",
        "librarian",
        "searcher",
        "refuter",
        "research",
        "context_curator",
    ] {
        assert!(
            !posts(role),
            "`{role}` can post an assertion the run will read as a finding"
        );
    }
}

/// Every standing team's agent is registered when several schools run.
///
/// The gate in `spawn_support_teams` is a bare-name lookup, and a multi-school
/// registry holds only school-qualified ids. A live three-school run therefore
/// started none of its standing teams — no director, so seven operator
/// directives sat unread for an hour behind a cursor that never moved, and the
/// run looked entirely healthy while it happened. The failure is silent by
/// construction (`continue`), so it needs a test rather than an assertion in
/// the path.
#[test]
fn a_multi_school_registry_still_declares_every_standing_team() -> agent::Result<()> {
    use super::{schooled_registry, schools, standing_teams};

    let selected = schools::ALL;
    let registry = schooled_registry(true, &selected)?;
    let declared: Vec<String> = registry
        .definitions()
        .iter()
        .map(|definition| definition.id.clone())
        .collect();
    for (name, agent, ..) in standing_teams() {
        let qualified = selected[0].role(agent);
        assert!(
            declared.contains(&qualified),
            "the {name} team's agent `{agent}` must be registered as `{qualified}`; \
             a bare-name lookup finds nothing in a multi-school registry"
        );
    }
    Ok(())
}

/// Every role that may write a ledger is told how, and no role is told to use
/// a tool it does not hold.
///
/// The `post_board` failure, guarded against at five times the surface. That
/// tool was granted to three roles, mentioned in no prompt, and called **zero**
/// times in a live three-school hour — the grant was right and the instruction
/// was nowhere, so the only trace a model saw was an unexplained entry in a
/// tool list. Five ledger tools arriving the same way would be a bigger version
/// of exactly that.
///
/// The assertion runs in both directions on purpose. A role told to record and
/// unable to is an error it discovers mid-turn; a role able to record and never
/// asked is silent, costs nothing visible, and is what actually happened.
#[test]
fn every_role_that_may_write_a_ledger_is_told_how() {
    use super::{LEDGER_WRITER_ROLES, LEDGER_WRITE_TOOLS, RolePrompts, schools};

    // The tool's own name, which nothing else in this crate's prompts mentions.
    // A prose phrase is the wrong marker here for the reason the board test
    // records: the briefs are hard-wrapped, so a sentence spanning two lines
    // never matches and the test fails for a reason unrelated to the behaviour.
    let distinctive = "record_entry";

    for school in schools::ALL {
        let prompts = RolePrompts::for_school(template_workspace(), &school, true)
            .expect("prompts assemble");
        for (role, prompt) in prompts.by_role() {
            let told = prompt.contains(distinctive);
            let granted = LEDGER_WRITER_ROLES.contains(&role);
            assert_eq!(
                told, granted,
                "`{role}` in `{}`: told how to record = {told}, may record = {granted}",
                school.slug
            );
        }
    }

    // And the brief's list agrees with the bench that grants the tools. Neither
    // can be derived from the other, so the agreement is asserted rather than
    // arranged.
    // The orchestrator is the top level rather than a specialist: its harness
    // is returned by `register_planners` and never registered, so it has no
    // registry entry to assert against and its authority is the harness alone.
    let registry = default_registry(true).expect("the registry builds");
    for role in LEDGER_WRITER_ROLES.into_iter().filter(|role| *role != "orchestrator") {
        for wanted in LEDGER_WRITE_TOOLS {
            assert!(
                registry
                    .get(role)
                    .is_some_and(|bench| bench.tools.iter().any(|tool| *tool == wanted)),
                "`{role}` is told how to record into a ledger but was never granted `{wanted}`"
            );
        }
    }
}

/// Everything that can read a ledger is told the rendered copy is shortened.
///
/// This is the half of the split that decides whether the whole design works.
/// The files in a prompt are bounded now, so a role that does not know
/// `read_ledger` exists is strictly worse off than before the bound: it reads a
/// truncated list, concludes the run holds nothing more, and re-proposes what
/// was cut. Cheaper and dumber is not the trade.
#[test]
fn every_role_that_can_read_a_ledger_is_told_the_copy_is_shortened() {
    use super::{LEDGER_BRIEF_WITHHELD, RolePrompts, schools};

    let prompts = RolePrompts::for_school(template_workspace(), &schools::ALL[0], false)
        .expect("prompts assemble");
    for (role, prompt) in prompts.by_role() {
        let told = prompt.contains("read_ledger");
        let withheld = LEDGER_BRIEF_WITHHELD.contains(&role);
        assert_eq!(
            told, !withheld,
            "`{role}`: told the rendered ledgers are shortened = {told}, withheld = {withheld}"
        );
    }

    // And the read tools really are universal, since the brief above tells
    // every role to use them.
    let registry = default_registry(true).expect("the registry builds");
    for (role, _) in prompts.by_role() {
        if role == "judge" || role == "orchestrator" {
            // The judge is deliberately tool-poor and the orchestrator is the
            // top level rather than a registered specialist; for both, the
            // harness rather than the registry is what decides.
            continue;
        }
        assert!(
            registry
                .get(role)
                .is_some_and(|bench| bench.tools.iter().any(|tool| *tool == "read_ledger")),
            "`{role}` is told to pull from a ledger but was never granted `read_ledger`"
        );
    }
}

/// A role is told which ledgers exist, not told to go and ask.
///
/// The brief used to say "`list_ledgers` names every one" and stop there, which
/// is a capability behind a call a model has to think to make. The catalogue is
/// derived from the registry, so a ledger this run defined is named in the next
/// prompt assembled — and each line says whether this role may write it, which
/// is the other question a role would otherwise learn from a refusal.
#[test]
fn every_role_that_reads_a_ledger_is_told_which_ledgers_exist() {
    use super::{LEDGER_BRIEF_WITHHELD, RolePrompts, schools};

    let prompts = RolePrompts::for_school(template_workspace(), &schools::ALL[0], false)
        .expect("prompts assemble");
    for (role, prompt) in prompts.by_role() {
        if LEDGER_BRIEF_WITHHELD.contains(&role) {
            continue;
        }
        assert!(
            prompt.contains("The ledgers this workspace keeps right now"),
            "`{role}` is told to read ledgers without being told which exist"
        );
        assert!(
            prompt.contains("- `tasks` ("),
            "`{role}`'s catalogue does not name the task ledger"
        );
    }

    // Written where the role may write, read-only where it may not, and both
    // read off `writable_by` rather than restated.
    let by_role: std::collections::HashMap<&str, &str> = prompts.by_role().into_iter().collect();
    assert!(
        by_role["goals"].contains("- `tasks` (yours to write)"),
        "the planner keeps the task list"
    );
    assert!(
        by_role["librarian"].contains("- `tasks` (read-only for you)"),
        "the librarian does not"
    );
}

/// The two roles that may declare a ledger are told how, and no others are.
///
/// `define_ledger` was granted to both planners' harnesses and named in no
/// prompt — the `post_board` failure exactly, and the reason a run that needed
/// an axis wrote prose instead. The reverse direction matters as much: a role
/// that cannot declare one must not be told about declaring one, or it spends a
/// turn asking somebody to.
#[test]
fn only_the_planners_are_told_how_to_declare_a_ledger() {
    use super::{LEDGER_KEEPER_ROLES, RolePrompts, schools};

    for school in schools::ALL {
        let prompts =
            RolePrompts::for_school(template_workspace(), &school, true).expect("prompts assemble");
        for (role, prompt) in prompts.by_role() {
            let told = prompt.contains("define_ledger");
            let keeps = LEDGER_KEEPER_ROLES.contains(&role);
            assert_eq!(
                told, keeps,
                "`{role}` in `{}`: told how to declare = {told}, may declare = {keeps}",
                school.slug
            );
        }
    }
}


/// A role granted the candidate tools is told what they are for.
///
/// The `post_board` failure again, and this test exists because the same
/// mistake was made once more while building these: `spawn_candidates` was
/// granted to `goals`, wired into its harness, and mentioned in no prompt — so a
/// live run held the tool for nine minutes and never called it, because the only
/// trace the model saw was an unexplained entry in a tool list. A grant without
/// an instruction is not a capability.
#[test]
fn the_roles_that_explore_candidates_are_told_how() {
    use super::{RolePrompts, VCS_READING_TOOLS, VCS_WRITING_TOOLS, schools};

    let prompts =
        RolePrompts::for_school(template_workspace(), &schools::ALL[0], true).expect("prompts");
    let by_role: std::collections::HashMap<&str, &str> = prompts.by_role().into_iter().collect();

    let goals = by_role.get("goals").expect("the goals prompt");
    assert!(
        goals.contains("spawn_candidates"),
        "the role holding `spawn_candidates` is never told what it is for"
    );
    assert!(
        goals.contains("archivist"),
        "the role that starts candidates must know who keeps one"
    );

    let archivist = by_role.get("archivist").expect("the archivist prompt");
    for tool in VCS_READING_TOOLS.into_iter().chain(VCS_WRITING_TOOLS) {
        assert!(
            archivist.contains(tool),
            "the archivist holds `{tool}` and its brief never mentions it"
        );
    }
}

/// The archivist is reachable by delegation.
///
/// It is the only role that may keep a candidate, so a bench that omits it
/// leaves `spawn_candidates` starting work nobody can adopt — the branches sit
/// there and the run ends having paid for them.
#[test]
fn the_archivist_is_on_a_bench_somebody_can_reach() {
    use super::{DELEGATES, SPECIALISTS};

    assert!(
        SPECIALISTS.contains(&"archivist"),
        "the goals agent starts the candidates and cannot reach the role that keeps one"
    );
    assert!(DELEGATES.contains(&"archivist"));
}

/// The ceiling reaches a prompt, and not only the function that computes it.
///
/// A bound that is never applied is the failure this repository keeps
/// recording. `shared_context::ceiling` is unit-tested on its own, but what
/// decides whether a role's prompt is bounded is that `load_workspace_files`
/// calls it on *every* routed file — including the ones no other bound covers.
/// This asserts that end to end, on a real assembly, with an oversized
/// `GOAL.md`: the one file every role receives, and until the ceiling existed
/// the one with nothing between it and the model.
#[test]
fn an_oversized_workspace_file_reaches_a_prompt_already_cut() {
    use super::{RolePrompts, schools, shared_context};

    let root = std::env::temp_dir().join(format!(
        "math-agent-ceiling-prompt-{}",
        std::process::id()
    ));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the workspace is creatable");
    // Over the ten-thousand-token ceiling and well under the 256 KB byte guard,
    // which is a separate control: past that a routed file fails the run at
    // startup rather than being cut, and this is about the range in between —
    // where a file grows by a paragraph a cycle and nothing was watching.
    let huge = "a paragraph the goal picked up and nobody removed. ".repeat(1_200);
    std::fs::write(root.join("GOAL.md"), &huge).expect("the goal is writable");

    let prompts =
        RolePrompts::for_school(&root, &schools::ALL[0], false).expect("prompts assemble");
    let (role, prompt) = prompts
        .by_role()
        .into_iter()
        .find(|(name, _)| *name == "judge")
        .expect("the judge is a role");

    assert!(
        prompt.len() < huge.len(),
        "`{role}` carries a cut copy, not the whole file"
    );
    assert!(
        prompt.contains("was cut here for this prompt"),
        "and is told it was cut, so it opens the file rather than trusting the fragment"
    );
    assert!(
        shared_context::ceiling("GOAL.md", &huge).is_some(),
        "the fixture is genuinely over the ceiling"
    );

    let _ = std::fs::remove_dir_all(&root);
}

/// The workspace seed ships no role guidance, and no scaffolded run gets any.
///
/// It shipped nine files, `scripts/run-agent` copied all nine into every
/// workspace, and each one restated what the built-in prompt for that role
/// already said — a second, older wording of the same instruction, carried in
/// every model call that role made. The override path still exists; what is
/// gone is a copy of it in thirty-nine workspaces that nobody wrote and nobody
/// could edit meaningfully, because editing one would only make it disagree
/// with the Rust.
#[test]
fn the_workspace_seed_ships_no_role_prompts() {
    assert!(
        !template_workspace().join("prompts").exists(),
        "the seed carries per-workspace role guidance again"
    );
}
