//! Unit tests for the model tier decision.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use tinyagents::harness::model::ChatModel;

use super::{ModelTier, ModelTiers};
use crate::agent::MockModel;
use crate::orchestrator::{MAX_REASONING_ROLES, REASONING_ROLES, SCRIBE_ROLES};

fn model() -> Arc<dyn ChatModel<()>> {
    Arc::new(MockModel::constant("ok"))
}

#[test]
fn a_scribe_role_runs_on_the_scribe_tier() {
    for role in SCRIBE_ROLES {
        assert_eq!(ModelTier::of(role), ModelTier::Scribe);
    }
}

#[test]
fn the_reasoning_roles_keep_their_tier() {
    for role in REASONING_ROLES {
        assert_eq!(ModelTier::of(role), ModelTier::Reasoning);
    }
}

#[test]
fn the_deepest_roles_keep_their_tier() {
    for role in MAX_REASONING_ROLES {
        assert_eq!(ModelTier::of(role), ModelTier::MaxReasoning);
    }
}

/// A school qualifies a registration; it must not drop a role a tier.
#[test]
fn a_schooled_role_stays_on_the_deepest_tier() {
    for role in MAX_REASONING_ROLES {
        assert_eq!(
            ModelTier::of(&format!("{role}@rising-sea")),
            ModelTier::MaxReasoning,
            "`{role}@rising-sea` fell off the deepest tier"
        );
    }
}

/// The tier a reader sees in the workflow document is the ladder the router
/// actually holds, spelled the same way.
#[test]
fn each_tier_is_named_after_the_ladder_it_selects() {
    assert_eq!(ModelTier::Default.as_str(), "default");
    assert_eq!(ModelTier::Reasoning.as_str(), "reasoning");
    assert_eq!(ModelTier::MaxReasoning.as_str(), "max-reasoning");
    assert_eq!(ModelTier::Scribe.as_str(), "scribe");
}

#[test]
fn an_ordinary_role_is_on_the_default_tier() {
    for role in ["coder", "research", "lean_prover", "tool_builder"] {
        assert_eq!(ModelTier::of(role), ModelTier::Default);
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
    assert_eq!(ModelTier::of("lean_scribe@rising-sea"), ModelTier::Scribe);
    assert_eq!(ModelTier::of("judge@rising-sea"), ModelTier::Reasoning);
    assert_eq!(ModelTier::of("coder@rising-sea"), ModelTier::Default);
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

/// The decision and the handout agree: whichever tier a role resolves to is the
/// model it is actually given.
///
/// Four distinct handles, compared by identity rather than by behaviour — two
/// mocks that answer the same string are indistinguishable by their answers,
/// which is exactly the mistake this is meant to catch.
#[test]
fn each_tier_hands_out_its_own_model() {
    let (default, reasoning, max_reasoning, scribe) = (model(), model(), model(), model());
    let tiers = ModelTiers::new(
        default.clone(),
        reasoning.clone(),
        max_reasoning.clone(),
        scribe.clone(),
    );

    for (role, expected) in [
        ("coder", &default),
        ("judge", &reasoning),
        ("inventor", &max_reasoning),
        ("lean_scribe", &scribe),
    ] {
        assert!(
            Arc::ptr_eq(&tiers.for_role(role), expected),
            "`{role}` was handed the wrong tier's model"
        );
    }

    // Transcript compression is nobody's role and must stay on the default: a
    // rewrite of a transcript on the Lean tier would spend the scarcest model
    // in the run on the job a fast general one does better.
    assert!(Arc::ptr_eq(tiers.default_tier(), &default));
}
