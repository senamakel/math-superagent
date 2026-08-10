//! Unit tests for registry and workspace boundaries.

use std::sync::Arc;

use tinyagents::harness::subagent::SubAgent;

use super::{
    AgentDefinition, AgentRegistry, COMPRESSION_TRIGGER_TOKENS, checked_workspace_path,
    compression_policy,
};
use crate::agent;

fn subagent(name: &str) -> Arc<SubAgent<(), ()>> {
    Arc::new(SubAgent::new(
        name,
        "test agent",
        Arc::new(agent::mock("done")),
    ))
}

#[test]
fn registry_resolves_agents_in_insertion_order() -> agent::Result<()> {
    let mut registry = AgentRegistry::new();
    registry
        .register(
            AgentDefinition::new("research", "Research", "finds evidence"),
            subagent("research"),
        )?
        .register(
            AgentDefinition::new("tool_builder", "Tool Builder", "builds tools"),
            subagent("tool_builder"),
        )?;

    assert_eq!(registry.names(), vec!["research", "tool_builder"]);
    assert!(registry.get("research").is_some());
    assert!(registry.get("missing").is_none());
    Ok(())
}

#[test]
fn registry_rejects_duplicate_ids() {
    let mut registry = AgentRegistry::new();
    registry
        .register(
            AgentDefinition::new("research", "Research", "finds evidence"),
            subagent("research"),
        )
        .expect("first registration should succeed");

    let duplicate = registry.register(
        AgentDefinition::new("research", "Other", "duplicate"),
        subagent("research"),
    );
    assert!(duplicate.is_err());
}

#[test]
fn workspace_paths_reject_absolute_and_parent_traversal() {
    let workspace = std::path::Path::new("/workspace");
    assert!(checked_workspace_path(workspace, "tools/check.sh").is_ok());
    assert!(checked_workspace_path(workspace, "/etc/passwd").is_err());
    assert!(checked_workspace_path(workspace, "../outside").is_err());
}

#[test]
fn compression_triggers_at_roughly_three_hundred_thousand_tokens() {
    let policy = compression_policy();
    assert_eq!(policy.trigger_budget(), COMPRESSION_TRIGGER_TOKENS);
}
