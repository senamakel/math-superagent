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
    assert!(prompt.contains("Do not search the answer space"));
    assert!(prompt.contains("Understand by computing"));
    // The rule that actually prevents a run spending itself on documentation.
    assert!(prompt.contains("no program executed"));
    assert!(prompt.contains("Verify independently"));
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
        "librarian",
    ] {
        assert!(
            registry.contains(expected),
            "`{expected}` must be registered"
        );
    }
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

#[test]
fn only_executing_roles_receive_the_runtime_configuration() {
    for role in ["tool_builder", "goals", "orchestrator"] {
        assert!(
            role_context(role).contains(&"config/config.toml"),
            "`{role}` acts on the runtime limits"
        );
    }
    for role in ["reflection", "inventor", "pattern_finder", "librarian"] {
        assert!(
            !role_context(role).contains(&"config/config.toml"),
            "`{role}` does not execute anything"
        );
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
    assert!(context.contains(&"TASKS.md"), "it rewrites the plan");
    assert!(
        context.contains(&"GOAL.md"),
        "a directive is read against it"
    );
    assert!(
        context.contains(&"research/THREADS.md"),
        "opening and closing directions is most of the job"
    );
    assert!(!context.contains(&"research/CLAIMS.md"));
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
    assert!(assembled.ends_with("role ctx"));
    // Trimmed, so an editor adding a trailing newline to a prompt file cannot
    // silently invalidate every cached prefix.
    assert!(!assembled.contains("\n\n\n"), "{assembled}");
}
