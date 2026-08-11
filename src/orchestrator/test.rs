//! Unit tests for registry and workspace boundaries.

use super::{
    AgentDefinition, AgentRegistry, COMPRESSION_TRIGGER_TOKENS, checked_workspace_path,
    compression_policy, default_registry, role_context, validate_complexity, workspace_prompt,
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
    assert!(first.starts_with("\n\nMethod policy"));
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
    assert!(validate_complexity("time O(2^n), space O(n)", "polynomial").is_err());
    assert!(validate_complexity("time O(n log n), space O(n)", "quasilinear").is_ok());
    assert!(validate_complexity("time O(n), space O(n)", "exponential").is_err());
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
fn pattern_finder_gets_the_sequence_tools_and_no_shell() -> agent::Result<()> {
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
    assert!(!patterns.tools.iter().any(|tool| tool == "execute_command"));
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
    assert!(context.contains(&"goal.md"));
    assert!(context.contains(&"memory.md"));
    // Unsettled scratch work is not evidence of progress.
    assert!(!context.contains(&"scratchpad.md"));
}

#[test]
fn the_inventor_sees_what_already_failed() {
    // memory.md carries the failed-approaches section. Without it the inventor
    // re-proposes exactly what it exists to avoid.
    assert!(role_context("inventor").contains(&"memory.md"));
}

#[test]
fn the_pattern_agent_sees_the_raw_data_it_analyses() {
    let context = role_context("pattern_finder");
    assert!(context.contains(&"scratchpad.md"));
    assert!(context.contains(&"memory.md"));
}

#[test]
fn only_executing_roles_receive_the_runtime_configuration() {
    for role in ["tool_builder", "goals", "orchestrator"] {
        assert!(
            role_context(role).contains(&"config.toml"),
            "`{role}` acts on the runtime limits"
        );
    }
    for role in ["reflection", "inventor", "pattern_finder", "librarian"] {
        assert!(
            !role_context(role).contains(&"config.toml"),
            "`{role}` does not execute anything"
        );
    }
}

#[test]
fn an_unknown_role_receives_no_working_files() {
    assert!(role_context("nonexistent").is_empty());
}
