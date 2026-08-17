//! Unit tests for the model tier decision.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use tinyagents::harness::model::ChatModel;

use super::{ModelTier, ModelTiers};
use crate::agent::MockModel;
use crate::orchestrator::{REASONING_ROLES, SCRIBE_ROLES};

fn model() -> Arc<dyn ChatModel<()>> {
    Arc::new(MockModel::constant("ok"))
}

fn tiers(with_scribe: bool) -> ModelTiers {
    ModelTiers::new(model(), model(), with_scribe.then(model))
}

#[test]
fn a_scribe_role_runs_on_the_scribe_tier_when_the_model_is_there() {
    let tiers = tiers(true);
    for role in SCRIBE_ROLES {
        assert_eq!(tiers.tier_for(role), ModelTier::Scribe);
    }
}

#[test]
fn a_scribe_role_falls_back_to_the_default_when_the_key_is_unset() {
    let tiers = tiers(false);
    for role in SCRIBE_ROLES {
        assert_eq!(
            tiers.tier_for(role),
            ModelTier::Default,
            "a run without the key must report the tier it will really use"
        );
    }
}

#[test]
fn the_reasoning_roles_keep_their_tier() {
    let tiers = tiers(true);
    for role in REASONING_ROLES {
        assert_eq!(tiers.tier_for(role), ModelTier::Reasoning);
    }
}

#[test]
fn an_ordinary_role_is_on_the_default_tier() {
    let tiers = tiers(true);
    for role in ["coder", "research", "lean_prover", "tool_builder"] {
        assert_eq!(tiers.tier_for(role), ModelTier::Default);
    }
}

#[test]
fn the_prover_is_not_a_scribe_role() {
    assert!(
        !SCRIBE_ROLES.contains(&"lean_prover"),
        "the prover keeps the judgement on the run's own model; only the writing goes down"
    );
}

#[test]
fn no_role_is_in_two_tiers() {
    for role in SCRIBE_ROLES {
        assert!(
            !REASONING_ROLES.contains(&role),
            "`{role}` is in two tier lists, so which model it runs on depends on read order"
        );
    }
}

#[test]
fn a_school_qualified_name_keeps_its_tier() {
    let tiers = tiers(true);
    assert_eq!(tiers.tier_for("lean_scribe@rising-sea"), ModelTier::Scribe);
    assert_eq!(tiers.tier_for("judge@rising-sea"), ModelTier::Reasoning);
    assert_eq!(tiers.tier_for("coder@rising-sea"), ModelTier::Default);
}

#[test]
fn the_published_tier_names_are_distinct() {
    let names = [
        ModelTier::Default.as_str(),
        ModelTier::Reasoning.as_str(),
        ModelTier::Scribe.as_str(),
    ];
    let mut sorted = names.to_vec();
    sorted.sort_unstable();
    sorted.dedup();
    assert_eq!(sorted.len(), names.len(), "two tiers publish the same name");
}
