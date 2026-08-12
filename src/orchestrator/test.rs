//! Unit tests for registry and workspace boundaries.
#![allow(clippy::expect_used)]

use super::{
    AgentDefinition, AgentRegistry, COMPRESSION_TRIGGER_TOKENS, DELEGATES, LEAN_PROVER_PROMPT,
    SAT_SOLVER_PROMPT, SMT_SOLVER_PROMPT, SPECIALISTS, SYMBOLIC_MATH_PROMPT, THEOREM_PROVER_PROMPT,
    checked_workspace_path, compression_policy, default_registry, role_context,
    validate_complexity, workspace_prompt,
};
use crate::agent;

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
fn workspace_paths_reject_absolute_and_parent_traversal() {
    let workspace = std::path::Path::new("/workspace");
    assert!(checked_workspace_path(workspace, "tools/check.sh").is_ok());
    assert!(checked_workspace_path(workspace, "/etc/passwd").is_err());
    assert!(checked_workspace_path(workspace, "../outside").is_err());
    assert!(checked_workspace_path(workspace, "").is_err());
    assert!(checked_workspace_path(workspace, "tools/../../outside").is_err());
}

#[test]
fn workspace_paths_accept_the_mount_point_spelling_agents_are_given() {
    // Every prompt names files as `/workspace/solution.md`; that must resolve
    // to the same file as the relative spelling, not fail as traversal.
    let workspace = std::path::Path::new("/workspace");
    assert_eq!(
        checked_workspace_path(workspace, "/workspace/solution.md").ok(),
        checked_workspace_path(workspace, "solution.md").ok()
    );
    assert_eq!(
        checked_workspace_path(workspace, "/workspace/tools/check.sh").ok(),
        checked_workspace_path(workspace, "tools/check.sh").ok()
    );
}

#[test]
fn workspace_prefix_stripping_does_not_open_up_sibling_directories() {
    let workspace = std::path::Path::new("/workspace");
    assert!(checked_workspace_path(workspace, "/workspace-other/secret").is_err());
    assert!(checked_workspace_path(workspace, "/workspaces/secret").is_err());
    assert!(checked_workspace_path(workspace, "/workspace/../etc/passwd").is_err());
    assert!(checked_workspace_path(workspace, "/workspace").is_err());
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
    assert!(research.tools.iter().any(|tool| tool == "recall_research"));
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
    assert!(context.contains(&"MEMORY.md"));
    // Unsettled scratch work is not evidence of progress.
    assert!(!context.contains(&"SCRATCHPAD.md"));
}

#[test]
fn the_inventor_sees_what_already_failed() {
    // MEMORY.md carries the failed-approaches section. Without it the inventor
    // re-proposes exactly what it exists to avoid.
    assert!(role_context("inventor").contains(&"MEMORY.md"));
}

#[test]
fn the_pattern_agent_sees_the_raw_data_it_analyses() {
    let context = role_context("pattern_finder");
    assert!(context.contains(&"SCRATCHPAD.md"));
    assert!(context.contains(&"MEMORY.md"));
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

#[test]
fn oversized_command_output_keeps_the_end_where_the_answer_is() {
    use super::{MAX_COMMAND_OUTPUT_BYTES, truncate_output};

    // A verification script prints its working first and its conclusion last.
    // Keeping only the head discarded the answer of a run that had computed it.
    let mut raw = b"START-OF-RUN\n".to_vec();
    raw.resize(MAX_COMMAND_OUTPUT_BYTES * 2, b'x');
    raw.extend_from_slice(b"\n[final answer] 4,3,1\n");

    let rendered = truncate_output(&raw);
    assert!(
        rendered.contains("[final answer] 4,3,1"),
        "the tail must survive"
    );
    assert!(rendered.contains("START-OF-RUN"), "the head must survive");
    assert!(rendered.contains("truncated from the middle"));

    // Output that fits is passed through untouched.
    let small = b"answer: 661\n";
    assert_eq!(truncate_output(small), "answer: 661\n");
}

#[test]
fn every_built_in_prompt_is_present_and_bounded() {
    use super::{
        GOALS_PROMPT, INVENTOR_PROMPT, LIBRARIAN_PROMPT, ORCHESTRATOR_PROMPT, ORGANIZER_PROMPT,
        PATTERN_PROMPT, REFLECTION_PROMPT, RESEARCH_PROMPT, SCHOLAR_PROMPT, SHARED_METHOD_POLICY,
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
        ("organizer", ORGANIZER_PROMPT),
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
    // attempted, what is already built, and the provisional numbers.
    assert_eq!(role_context("coder"), role_context("tool_builder"));
    assert_eq!(role_context("sat_solver"), role_context("tool_builder"));
    assert_eq!(role_context("lean_prover"), role_context("tool_builder"));
    for role in ["smt_solver", "theorem_prover", "symbolic_math"] {
        assert_eq!(role_context(role), role_context("tool_builder"), "{role}");
    }
    assert!(role_context("coder").contains(&"SCRATCHPAD.md"));
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
fn the_reflections_index_reaches_the_roles_that_must_not_repeat_an_attempt() {
    // An index nobody reads is not a flow. These three each make a decision
    // that depends on what earlier attempts established.
    for role in ["orchestrator", "goals", "reflection", "inventor"] {
        assert!(
            role_context(role).contains(&"reflections/INDEX.md"),
            "{role} must see the reflections index"
        );
    }
    // It is not given to everyone: a role that neither plans nor judges gains
    // nothing from the attempt-by-attempt record and pays for it in context.
    for role in ["tool_builder", "coder", "scholar", "librarian", "organizer"] {
        assert!(
            !role_context(role).contains(&"reflections/INDEX.md"),
            "{role} does not need the reflections index"
        );
    }
    // Reflection still never sees provisional work.
    assert!(!role_context("reflection").contains(&"SCRATCHPAD.md"));
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
        "pattern_finder",
        "scholar",
        "librarian",
        "research",
        "inventor",
    ] {
        assert!(
            role_context(role).contains(&"CONTEXT.md"),
            "{role} reasons about the mathematics and needs the shared brief"
        );
    }
    // The organiser files rather than reasons; giving it opinions about the
    // mathematics is how a filing job turns into an editing one.
    assert!(!role_context("organizer").contains(&"CONTEXT.md"));
    // Reflection judges an attempt against the criteria and the record. A
    // standing brief of what sources assert is exactly the material it must
    // not mistake for verification.
    assert!(!role_context("reflection").contains(&"CONTEXT.md"));
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
fn the_organizer_skips_a_cycle_over_a_workspace_it_has_already_filed() {
    // Filing is cheap to do and expensive to decide: an organizer asked to
    // notice nothing changed must walk the workspace and spend a model call to
    // find out. Two live runs spent 49% and 38% of every model call they made
    // on the organizer, against 11% and 4% on the agent solving the problem.
    let root = std::env::temp_dir().join(format!("math-agent-filing-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    let filed = std::sync::Arc::new(std::sync::Mutex::new(None));

    // Nothing on disk at all: idle rather than indexing empty folders.
    assert_eq!(
        super::filing_unchanged(&root, &filed),
        Some(super::teams::Cycle::Idle)
    );

    let _ = std::fs::create_dir_all(root.join("code"));
    let _ = std::fs::write(root.join("code/solve.py"), "print(1)");
    // A new program: the cycle runs.
    assert_eq!(super::filing_unchanged(&root, &filed), None);
    // Nothing further has happened: it does not run again.
    assert_eq!(
        super::filing_unchanged(&root, &filed),
        Some(super::teams::Cycle::Idle)
    );

    // The trap this gate exists to avoid. The organizer's own output is an
    // INDEX.md, so counting one as a change would have the team waking itself
    // forever on the filing it just did — the pattern team's SCRATCHPAD.md
    // lesson, one folder wider.
    let _ = std::fs::write(root.join("code/INDEX.md"), "| solve.py | prints one |");
    assert_eq!(
        super::filing_unchanged(&root, &filed),
        Some(super::teams::Cycle::Idle),
        "an INDEX.md write must not wake the organizer that wrote it"
    );

    // Real new work still wakes it.
    let _ = std::fs::write(root.join("code/second.py"), "print(2)");
    assert_eq!(super::filing_unchanged(&root, &filed), None);
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
