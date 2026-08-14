//! Unit tests for registry and workspace boundaries.
#![allow(clippy::expect_used)]

use super::exec::validate_complexity;
use super::{
    AgentDefinition, AgentRegistry, COMPRESSION_TRIGGER_TOKENS, DELEGATES, DISCOVERY_TOOLS,
    GOALS_PROMPT,
    INVENTION_BENCH, LEAN_PROVER_PROMPT, LIBRARIAN_PROMPT, ORCHESTRATOR_PROMPT, REASONING_ROLES,
    SAT_SOLVER_PROMPT, SMT_SOLVER_PROMPT, SPECIALISTS, SYMBOLIC_MATH_PROMPT, THEOREM_PROVER_PROMPT,
    compression_policy, default_registry, role_context, workspace_prompt,
};
use crate::agent;

include!("orchestrator_registry_test.rs");
include!("orchestrator_roles_test.rs");
include!("orchestrator_policy_test.rs");
