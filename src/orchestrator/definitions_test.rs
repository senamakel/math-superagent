//! Tests that the workflow registry says exactly what the run's does.
#![allow(clippy::expect_used, clippy::panic)]

use super::*;
use crate::orchestrator::default_registry;

fn registry(research_enabled: bool) -> AgentRegistry {
    default_registry(research_enabled).expect("the default registry builds")
}

/// The severe risk this whole module is shaped against: a role's authority
/// changing because the derivation drifted from the registry.
///
/// Asserts the *resolved* grant set per role, not the configuration meant to
/// produce it — a test that read the same list the code reads would pass
/// whatever that list said.
#[test]
fn every_role_is_granted_exactly_the_tools_it_has_today() {
    let registry = registry(true);
    let derived = workflow_agents(&registry);

    assert_eq!(derived.len(), registry.definitions().len());
    for definition in registry.definitions() {
        let agent = derived
            .iter()
            .find(|agent| agent.id == definition.id)
            .unwrap_or_else(|| panic!("`{}` is missing from the derived registry", definition.id));

        let granted: Vec<&str> = agent.tools.iter().map(|grant| grant.slug.as_str()).collect();
        assert_eq!(
            granted, definition.tools,
            "`{}` was granted a different tool set than it holds",
            definition.id
        );
    }
}

/// A pattern grant would widen a role silently: `TinyFlows` hands a trailing
/// `.*` to the harness verbatim and expects the harness to expand it, and this
/// crate's tool invoker matches exact slugs only. A pattern arriving here would
/// resolve to nothing at all, which is a role losing its tools rather than
/// gaining them — still a silent change of authority.
#[test]
fn no_grant_is_a_pattern() {
    for agent in workflow_agents(&registry(true)) {
        for grant in &agent.tools {
            assert!(
                !grant.slug.contains('*'),
                "`{}` carries the pattern grant `{}`",
                agent.id,
                grant.slug
            );
        }
    }
}

/// Research gating is enforced by not registering the tool. The derivation
/// reads the registry, so the gate has to hold on this path without being
/// reimplemented on it — that is the property, and this is the test of it.
#[test]
fn research_off_removes_the_search_grant_rather_than_relying_on_a_rule_here() {
    let gated = workflow_agents(&registry(false));
    for agent in &gated {
        for grant in &agent.tools {
            assert_ne!(
                grant.slug, "exa_search",
                "`{}` kept web search with research disabled",
                agent.id
            );
        }
    }

    // And the same registry with research on does grant it, or the assertion
    // above would pass on a registry that never had the tool.
    let ungated = workflow_agents(&registry(true));
    assert!(
        ungated
            .iter()
            .any(|agent| agent.tools.iter().any(|grant| grant.slug == "exa_search")),
        "no role has web search even with research enabled"
    );
}

/// Ids are the addressing key across all three surfaces — `agent_ref`, the
/// harness registry, and `spawn_agent`. A workflow naming a role must not be a
/// separate vocabulary from the run naming the same one.
#[test]
fn ids_match_the_registry_one_for_one() {
    let registry = registry(true);
    let derived: Vec<String> = workflow_agents(&registry)
        .into_iter()
        .map(|agent| agent.id)
        .collect();
    let expected: Vec<String> = registry
        .names()
        .into_iter()
        .map(ToString::to_string)
        .collect();
    assert_eq!(derived, expected);
}

/// The judge is capped tighter than a solve for a recorded reason: left with an
/// investigation's budget it investigates, and a live one spent four minutes
/// and fifteen model calls reading files while the finished attempt waited.
#[test]
fn a_judging_role_declares_a_narrower_budget_than_a_solving_one() {
    let derived = workflow_agents(&registry(true));
    let limits = |id: &str| {
        derived
            .iter()
            .find(|agent| agent.id == id)
            .unwrap_or_else(|| panic!("`{id}` is registered"))
            .limits
    };

    let judge = limits("judge");
    let research = limits("research");
    assert!(
        judge.max_steps < research.max_steps,
        "judge {:?} is not narrower than research {:?}",
        judge.max_steps,
        research.max_steps
    );
    // The wall clock is declared too: a role whose limits omitted its ceiling
    // would read as unbounded to anyone reading the workflow.
    assert!(judge.agent_timeout_secs.is_some());
}

/// The reasoning split lives in `REASONING_ROLES` and is applied when a harness
/// is built. It is applied here too, so a workflow reader can see which tier a
/// role runs on without reading Rust.
#[test]
fn the_reasoning_roles_are_published_as_a_different_tier() {
    let derived = workflow_agents(&registry(true));
    for agent in &derived {
        let expected = if REASONING_ROLES.contains(&agent.id.as_str()) {
            "reasoning"
        } else {
            "default"
        };
        assert_eq!(
            agent.model.as_deref(),
            Some(expected),
            "`{}` is on the wrong tier",
            agent.id
        );
    }
    // At least one of each, or the assertion above is vacuous.
    assert!(derived.iter().any(|a| a.model.as_deref() == Some("reasoning")));
    assert!(derived.iter().any(|a| a.model.as_deref() == Some("default")));
}
