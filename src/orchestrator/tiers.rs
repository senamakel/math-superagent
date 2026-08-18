//! Which model a role runs on, decided in one place.
//!
//! There are four tiers and one question: given a role name, which model does
//! it get. Before this file the question had two answers — [`SupportAgents`]
//! resolved it for the support roles and [`super::definitions`] published it
//! for the workflow document — and the code writers had a third, which was to
//! not ask at all and take the run's default. Adding a tier to three places is
//! three chances for them to disagree about something a reader would take at
//! face value.
//!
//! So the tiers own both the models and the decision. `tier_for` is the only
//! thing that reads the role lists, `for_role` is the only thing that hands out
//! a model, and the name a workflow reader sees comes off the same enum.
//!
//! [`SupportAgents`]: super::orchestrator_agents

use std::sync::Arc;

use tinyagents::harness::model::ChatModel;

use super::async_subagents::base_role;
use super::{MAX_REASONING_ROLES, REASONING_ROLES, SCRIBE_ROLES};

/// Which of the run's models a role runs on.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(in crate::orchestrator) enum ModelTier {
    /// The run's default: fast, cheap, and what most roles want.
    Default,
    /// For roles whose work is judging rather than doing.
    Reasoning,
    /// For the few roles whose whole output is a judgement, on the deepest
    /// ladder the router holds.
    MaxReasoning,
    /// For roles that write Lean, on a model specialised for it.
    Scribe,
}

impl ModelTier {
    /// What the tier is called in the workflow document.
    ///
    /// The one place a tier is spelled, so a reader comparing the document to
    /// the run is comparing one string to itself.
    pub(in crate::orchestrator) fn as_str(self) -> &'static str {
        match self {
            Self::Default => "default",
            Self::Reasoning => "reasoning",
            Self::MaxReasoning => "max-reasoning",
            Self::Scribe => "scribe",
        }
    }
}

/// The run's models, and the decision about which role gets which.
pub(in crate::orchestrator) struct ModelTiers {
    default: Arc<dyn ChatModel<()>>,
    reasoning: Arc<dyn ChatModel<()>>,
    max_reasoning: Arc<dyn ChatModel<()>>,
    /// `None` when `MISTRAL_API_KEY` is unset. See [`ModelTiers::tier_for`].
    scribe: Option<Arc<dyn ChatModel<()>>>,
}

impl std::fmt::Debug for ModelTiers {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("ModelTiers")
            .field("scribe", &self.scribe.is_some())
            .finish_non_exhaustive()
    }
}

impl ModelTiers {
    /// Gathers the run's models.
    pub(in crate::orchestrator) fn new(
        default: Arc<dyn ChatModel<()>>,
        reasoning: Arc<dyn ChatModel<()>>,
        max_reasoning: Arc<dyn ChatModel<()>>,
        scribe: Option<Arc<dyn ChatModel<()>>>,
    ) -> Self {
        Self {
            default,
            reasoning,
            max_reasoning,
            scribe,
        }
    }

    /// The tier `role` actually runs on.
    ///
    /// Availability is part of the answer, not a separate question asked later:
    /// a run without `MISTRAL_API_KEY` reports `Default` for the scribe roles
    /// because that is what they will really use. A tier that named a model the
    /// run does not hold would make the workflow document a claim rather than a
    /// record.
    ///
    /// School-qualified names resolve through [`base_role`], so
    /// `lean_scribe@rising-sea` needs no row of its own.
    pub(in crate::orchestrator) fn tier_for(&self, role: &str) -> ModelTier {
        let role = base_role(role);
        if SCRIBE_ROLES.contains(&role) && self.scribe.is_some() {
            return ModelTier::Scribe;
        }
        // Asked before the reasoning tier, and the two lists are disjoint —
        // asserted in `tiers_test`, because a role in both would resolve by the
        // order of these two lines rather than by a decision anybody made.
        if MAX_REASONING_ROLES.contains(&role) {
            return ModelTier::MaxReasoning;
        }
        if REASONING_ROLES.contains(&role) {
            return ModelTier::Reasoning;
        }
        ModelTier::Default
    }

    /// The model `role` runs on.
    pub(in crate::orchestrator) fn for_role(&self, role: &str) -> Arc<dyn ChatModel<()>> {
        match self.tier_for(role) {
            ModelTier::Default => self.default.clone(),
            ModelTier::Reasoning => self.reasoning.clone(),
            ModelTier::MaxReasoning => self.max_reasoning.clone(),
            // `tier_for` only answers `Scribe` when the model is present, so
            // the fallback here is unreachable rather than a second policy.
            ModelTier::Scribe => self
                .scribe
                .clone()
                .unwrap_or_else(|| self.default.clone()),
        }
    }

    /// The run's default model, for the jobs that are nobody's role.
    ///
    /// Transcript compression is the one that matters: it is driven by whichever
    /// model the role holds, and compressing on a specialised Lean model would
    /// spend the scarcest thing in the run on a job the flash model does better.
    pub(in crate::orchestrator) fn default_tier(&self) -> &Arc<dyn ChatModel<()>> {
        &self.default
    }
}

#[cfg(test)]
#[path = "tiers_test.rs"]
mod test;
