//! An embeddable research runtime over a vendored `TinyAgents` harness and a
//! vendored `TinyFlows` state graph.
//!
//! The vendored `TinyAgents` runtime provides model and tool orchestration
//! without the full application's memory, channels, or Web3 domains, and runs
//! one agent turn. `TinyFlows` provides the state graph that decides which turn
//! runs next — the attempt/judge/reflect solution loop, and the graph each
//! detached sub-agent run is driven by. [`agent::flow`] is the seam between
//! them and documents why the split falls where it does.
//! [`HelloAgent`] supplies a minimal OpenRouter-backed loop with arithmetic,
//! echo, Exa search, and sub-agent delegation tools. Loop events are exported
//! to Langfuse on a best-effort basis.
//! [`OrchestratorAgent`] supplies a named specialist registry and delegates
//! research and tool-building work to isolated child agents.
//!
//! # Layout
//!
//! - `src/error/` holds the crate-wide [`Error`] enum and the [`Result`] alias
//!   returned by every fallible public function.
//! - Each feature area lives in its own module directory with a `mod.rs`
//!   module root, an optional `types.rs`, and a `test.rs` holding its unit
//!   tests.
//! - Every public item is re-exported from here, so downstream users have a
//!   single predictable surface.
//! - `agent` exposes the `TinyAgents` harness facade.
//! - [`HelloAgent`] exposes the runnable hello-world agent.
//! - [`OrchestratorAgent`] exposes the registry-backed multi-agent runtime.
//! - [`directives`] exposes the queue an operator directs a live run through.
//!   It is public because it is the whole external control surface: anything
//!   that can link this crate — the `euler-tui` viewer, `scripts/steer`, or a
//!   service standing in front of them — directs a run by calling
//!   [`directives::enqueue`], and nothing has to open a port into the sandbox
//!   to do it.
//!
//! # Example
//!
//! ```
//! use math_agent::{greet, Error};
//!
//! assert_eq!(greet("Ferris")?, "Hello, Ferris!");
//! assert_eq!(greet("   ").unwrap_err(), Error::EmptyName);
//! # Ok::<(), math_agent::Error>(())
//! ```
//!
pub mod agent;
pub mod directives;
mod error;
mod greeting;
mod hello_agent;
mod orchestrator;

pub use directives::Directive;
pub use error::{Error, Result};
pub use greeting::greet;
pub use hello_agent::HelloAgent;
pub use orchestrator::lean::{
    Outcome as LeanOutcome, Verdict as LeanVerdict, check_file as check_lean_file,
};
pub use orchestrator::{
    AgentDefinition, AgentRegistry, OrchestratorAgent, SubagentAgentRunner, SubagentTaskRunner,
    WorkflowCatalog, ledger_report, prompt_report, render_ledger,
};
#[cfg(feature = "graph-debug")]
pub use orchestrator::{render_flows, render_solution_loop};
