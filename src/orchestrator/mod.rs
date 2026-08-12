//! Registry-backed orchestrator with research and tool-building specialists.
include!("orchestrator_core.rs");
include!("orchestrator_runtime.rs");
include!("orchestrator_teams.rs");
include!("orchestrator_registry.rs");
include!("orchestrator_prompts.rs");
include!("orchestrator_agents.rs");
include!("orchestrator_environment.rs");

#[cfg(test)]
#[path = "orchestrator_test.rs"]
mod test;
