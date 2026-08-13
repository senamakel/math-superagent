//! This crate's runtime, offered to `TinyFlows` as a capability bundle.
//!
//! `TinyFlows` runs no agent loop, executes nothing, and stores nothing. Every
//! effect a workflow has on the world goes through a trait the embedding host
//! implements, and this module is this crate's side of that: the
//! [`Capabilities`] bundle a workflow run is handed.
//!
//! Each implementation is an adapter over something that already exists here,
//! not a second copy of it. That is deliberate — two implementations of "run an
//! agent" or "call a tool" would drift, and the one a workflow reached would be
//! the one nobody was testing.
//!
//! | Capability | Backed by | Where |
//! |---|---|---|
//! | `tools` | the tool registry | [`tools`] |
//! | `state` | the workspace | [`state`] |
//! | `code` | *refused on purpose* | [`execution`] |
//! | `shell` | *not supplied on purpose* | [`execution`] |
//! | `tasks` | `AsyncSubagentManager` | [`super::runner`] |
//! | `llm` | one model turn, no tools | [`llm`] |
//! | `http` | *refused on purpose* | [`network`] |
//! | `resolver` | no catalog yet | [`resolver`] |
//! | `agent` | the role registry | [`super::runner`] |
//! | `memory` | *unset; the recall tools reach the same store* | — |
//!
//! # What is deliberately missing
//!
//! Execution. A `code` node is refused and a `shell` node has no runner,
//! because running a command here means declaring its complexity class first —
//! the enforcement of the method policy — and a second execution path would
//! skip that check. [`execution`] carries the full argument. A workflow that
//! needs to run something calls the `execute_command` tool like everything else
//! does.

use std::sync::Arc;

use tinyagents::harness::model::ChatModel;
use tinyflows::caps::Capabilities;

use super::runner::{SubagentAgentRunner, SubagentTaskRunner};
use crate::agent::Tool;

pub(crate) mod execution;
pub(crate) mod llm;
pub(crate) mod network;
pub(crate) mod resolver;
pub(crate) mod state;
pub(crate) mod tools;

/// Assembles the bundle a workflow run is handed.
///
/// `tools` is the run's authority: only these are callable from a `tool_call`
/// node, and a slug outside the set is refused by name. Pass exactly what the
/// workflow may use, not the whole registry — see [`tools`] for why that
/// matters here.
///
/// `agents` is what an `agent` node's `agent_ref` reaches. With it set, a role
/// runs with its own prompt, tools, and budget; without it, an `agent` node
/// would fall back to a bare tool-less completion, which is a different thing
/// wearing the same name.
///
/// `memory` is still unset, so a `memory` node fails with a capability error.
/// That is honest: a memory node has no meaningful no-op, and the recall tools
/// already reach the same store through `tool_call`.
pub(crate) fn bundle(
    model: Arc<dyn ChatModel<()>>,
    workspace: impl Into<std::path::PathBuf>,
    tools: impl IntoIterator<Item = Arc<dyn Tool<()>>>,
    tasks: SubagentTaskRunner,
    agents: SubagentAgentRunner,
) -> Capabilities {
    Capabilities {
        llm: Arc::new(llm::SingleTurnModel::new(model)),
        tools: Arc::new(tools::WorkspaceTools::new(tools)),
        http: Arc::new(network::RefusingHttpClient),
        code: Arc::new(execution::RefusingCodeRunner),
        state: Arc::new(state::WorkspaceState::new(workspace)),
        resolver: Arc::new(resolver::NoCatalog),
        agent: Some(Arc::new(agents)),
        shell: None,
        memory: None,
        tasks: Some(Arc::new(tasks)),
    }
}

#[cfg(test)]
#[path = "caps_test.rs"]
mod test;
