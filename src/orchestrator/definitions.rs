//! This crate's roles, restated as `TinyFlows` agent definitions.
//!
//! A `WorkflowGraph` carries its own registry of reusable agent types, and an
//! `agent` node selects one by `agent_ref`. This module produces that registry
//! from the [`AgentRegistry`](super::AgentRegistry) the run already assembled.
//!
//! # Derived, never restated
//!
//! The tempting shape here is a hand-written list of nineteen definitions. It
//! is also the one thing this module must not be. Tool grants are authority
//! boundaries in this crate — the orchestrator has no shell, research has no
//! delegation, and research's own reach is withheld by *not registering* a tool
//! rather than by asking a model to abstain. A second list would be a second
//! answer to "what may this role touch", and the two would agree only until the
//! first time somebody edited one of them.
//!
//! So the registry that the run builds is the only source. Every field below is
//! read off it, `research_enabled` included: a run with research off has no
//! `exa_search` in its registry, so the derived definition has no grant for it,
//! and the gate holds on this path without being reimplemented on it.
//!
//! # What is added rather than derived
//!
//! Two things the harness registry does not carry, because until now nothing
//! outside the harness needed them written down:
//!
//! - **Limits.** [`RunBudget`] bounds a run host-side; `AgentLimits` is the
//!   author's declared version of the same intent, forwarded to whoever runs
//!   the loop. They are advisory in the model and enforced here, which is the
//!   right way round — see [`limits_for`].
//! - **The reasoning-model split.** `REASONING_ROLES` names the roles that run
//!   on the stronger model. That lives in the orchestrator as a constant and is
//!   applied when a harness is built, so it is applied here too rather than
//!   left for the reader to rediscover.

use tinyflows::model::{AgentDefinition as FlowAgent, AgentLimits, ToolGrant};

use crate::agent::budget::RunBudget;

use super::async_subagents::base_role;
use super::{AgentRegistry, ModelTiers};

/// The budget a role runs on.
///
/// The narrowed budgets are not a detail: a judge left with an investigation's
/// allowance investigates — a live one spent four minutes and fifteen model
/// calls reading files while the finished attempt waited on it. Housekeeping
/// has the same shape and the same fix. Carrying them here keeps a definition
/// honest about what the role is actually given.
/// A school qualifies a registration — `judge@rising-sea` — and the budget is
/// the *judge's* whichever school is asking, so the suffix is stripped here
/// rather than every school growing a row of its own in the match below.
fn budget_for(role: &str) -> RunBudget {
    let base = RunBudget::from_env();
    match base_role(role) {
        "judge" | "reflection" => base.for_judging(),
        "context_curator" | "librarian" => base.for_housekeeping(),
        "inventor" => base.for_invention(),
        _ => base,
    }
}

/// Restates a budget as the limits an author would have declared.
///
/// `AgentLimits` is explicitly advisory in `TinyFlows` — the agent loop runs
/// host-side, so the engine never sees a step or a tool call and cannot enforce
/// a cap on either. That is fine here, because the host applying them is this
/// crate: the same [`RunBudget`] reaches the harness through `RunPolicy` and is
/// enforced there. These are the declared intent, published so a workflow
/// reader can see what a role is bounded by without reading Rust.
///
/// The wall clock is deliberately included. Whatever else a narrowed budget
/// bounds, the graceful cap must be the one that trips, and a role whose
/// declared limits omitted its ceiling would read as unbounded.
fn limits_for(role: &str) -> AgentLimits {
    let budget = budget_for(role);
    AgentLimits {
        max_steps: u32::try_from(budget.max_model_calls).ok(),
        max_tool_calls: u32::try_from(budget.max_tool_calls).ok(),
        agent_timeout_secs: u32::try_from(budget.run_timeout.as_secs()).ok(),
        tool_timeout_secs: u32::try_from(budget.tool_timeout.as_secs()).ok(),
    }
}

/// Derives the workflow agent registry from the run's own registry.
///
/// Ids match one for one, so an `agent_ref` a workflow names is the same string
/// the harness resolves and the same string `spawn_agent` takes. Anything else
/// would make a workflow's roles a separate vocabulary from the run's.
pub(super) fn workflow_agents(registry: &AgentRegistry, models: &ModelTiers) -> Vec<FlowAgent> {
    registry
        .definitions()
        .into_iter()
        .map(|definition| {
            let mut agent = FlowAgent::new(definition.id.clone());
            agent.name.clone_from(&definition.name);
            agent.description.clone_from(&definition.description);
            // The harness registry pins a *registry alias* (`openrouter`),
            // which means nothing outside this process. What a workflow reader
            // wants to know is which tier the role runs on, so the split is
            // published as the concrete choice it actually is.
            // Asked of the tiers rather than reconstructed from a list, so a
            // run whose scribe tier is unconfigured publishes `default` for it
            // — which is what that role will really use. See `tiers::tier_for`.
            agent.model = Some(models.tier_for(&definition.id).as_str().to_string());
            agent.tools = definition
                .tools
                .iter()
                .map(|slug| ToolGrant {
                    slug: slug.clone(),
                    connection_ref: None,
                })
                .collect();
            agent.limits = limits_for(&definition.id);
            agent
        })
        .collect()
}

#[cfg(test)]
#[path = "definitions_test.rs"]
mod test;
