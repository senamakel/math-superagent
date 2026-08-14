//! The state-graph runtime the agent loop is built on, and the seam holding it.
//!
//! Every explicit control-flow graph in this crate — the attempt/judge/reflect
//! solution loop, and the single-node graph each async sub-agent run is driven
//! by — is built with [`GraphBuilder`]. That runtime is `TinyFlows`', not
//! `TinyAgents`'.
//!
//! The two are the same runtime. It was written in `TinyAgents`, extracted into
//! `TinyFlows`, and is maintained there; `TinyFlows`' copy states so in its own
//! module documentation. What the newer copy adds is scheduling this loop
//! wants and the older one cannot express: a per-node concurrency bound
//! (`with_node_concurrency`), so one fanned-out node can be widened without
//! also widening the graph, and `Command::route`, which lets a single node emit
//! plain activations and `Send` packets together. `TinyAgents` keeps what
//! `TinyFlows` deliberately left behind — the harness, the model providers, the
//! tool runtime, and the orchestration task store — because agents are a host
//! concern in `TinyFlows`, injected through its capability traits, which is
//! exactly the role this crate plays.
//!
//! So the two crates are not alternatives here. `TinyAgents` runs a *turn*;
//! `TinyFlows` decides which turn runs next.
//!
//! # The seam
//!
//! The one place the split is visible is the error type. `TinyFlows`' graph has
//! its own [`tinyflows::graph::GraphError`] rather than `TinyAgentsError`,
//! which is what let it stop depending on the harness at all. Node handlers in
//! this crate call harness code and get `TinyAgentsError`; the graph they are
//! wired into wants `GraphError`; and the callers around the graph return
//! `crate::agent::Result`, which is `TinyAgentsError` again. [`into_graph`] and
//! [`from_graph`] are that round trip, and they are the only two functions that
//! should ever perform it — a conversion written inline at each call site is
//! how variants quietly become `Graph("...")` strings.
//!
//! Both directions preserve the variant wherever the two enums agree, so a
//! timeout stays a timeout and a cancellation stays a cancellation across a
//! graph boundary. That matters because the solution loop reads them: a run
//! that stops on its wall clock is kept with partial results, and one that
//! failed is not.

pub use tinyflows::graph::{
    ClosureStateReducer, Command, CompiledGraph, GraphBuilder, GraphError, GraphExecution,
    NodeContext, NodeResult,
};

/// The graph runtime's own result type.
///
/// Named separately from [`crate::agent::Result`], which is the harness's, so
/// a signature says which side of the seam it is on rather than leaving a
/// reader to work it out from the error it returns.
pub type GraphResult<T> = std::result::Result<T, GraphError>;

use tinyagents::TinyAgentsError;

/// Converts a harness error into the graph runtime's error type.
///
/// Used at the end of a node handler, where the handler has called harness code
/// and has to hand the graph something it can route on.
///
/// Variants that exist in both enums are preserved. `GraphError` has no
/// vocabulary for a provider, tool, or serialization failure — nothing in the
/// graph runtime can raise one — so those arrive as
/// [`GraphError::Graph`] carrying the rendered message, and [`from_graph`]
/// does not attempt to guess them back.
#[must_use]
pub fn into_graph(error: TinyAgentsError) -> GraphError {
    match error {
        TinyAgentsError::MissingStart => GraphError::MissingStart,
        TinyAgentsError::MissingNode(node) => GraphError::MissingNode(node),
        TinyAgentsError::MissingEdgeTarget(node) => GraphError::MissingEdgeTarget(node),
        TinyAgentsError::MissingRoute { node, route } => GraphError::MissingRoute { node, route },
        TinyAgentsError::RecursionLimit(limit) => GraphError::RecursionLimit(limit),
        TinyAgentsError::SubAgentDepth(depth) => GraphError::SubAgentDepth(depth),
        TinyAgentsError::NodeVisitLimit { node, limit } => {
            GraphError::NodeVisitLimit { node, limit }
        }
        TinyAgentsError::Validation(message) => GraphError::Validation(message),
        TinyAgentsError::Timeout(message) => GraphError::Timeout(message),
        TinyAgentsError::Cancelled => GraphError::Cancelled,
        TinyAgentsError::Interrupted { node, message } => GraphError::Interrupted { node, message },
        TinyAgentsError::InvalidConcurrentUpdate(message) => {
            GraphError::InvalidConcurrentUpdate(message)
        }
        TinyAgentsError::Checkpoint(message) => GraphError::Checkpoint(message),
        TinyAgentsError::Resume(message) => GraphError::Resume(message),
        other => GraphError::Graph(other.to_string()),
    }
}

/// Converts a graph runtime error back into the crate's harness error type.
///
/// Used where a graph is compiled or run — the caller returns
/// [`crate::agent::Result`], so the graph's own error has to become the
/// harness's before it leaves the function.
///
/// The variants that matter to the callers are the ones a bounded run ends on:
/// a timeout stays [`TinyAgentsError::Timeout`] and a cancellation stays
/// [`TinyAgentsError::Cancelled`], because the solution loop distinguishes a run
/// that met its wall clock — whose partial results are kept — from one that
/// failed.
#[must_use]
pub fn from_graph(error: GraphError) -> TinyAgentsError {
    match error {
        GraphError::MissingStart => TinyAgentsError::MissingStart,
        GraphError::MissingNode(node) => TinyAgentsError::MissingNode(node),
        GraphError::MissingEdgeTarget(node) => TinyAgentsError::MissingEdgeTarget(node),
        GraphError::MissingRoute { node, route } => TinyAgentsError::MissingRoute { node, route },
        GraphError::RecursionLimit(limit) => TinyAgentsError::RecursionLimit(limit),
        GraphError::SubAgentDepth(depth) => TinyAgentsError::SubAgentDepth(depth),
        GraphError::NodeVisitLimit { node, limit } => {
            TinyAgentsError::NodeVisitLimit { node, limit }
        }
        GraphError::Validation(message) => TinyAgentsError::Validation(message),
        GraphError::Timeout(message) => TinyAgentsError::Timeout(message),
        GraphError::Cancelled => TinyAgentsError::Cancelled,
        GraphError::Interrupted { node, message } => TinyAgentsError::Interrupted { node, message },
        GraphError::InvalidConcurrentUpdate(message) => {
            TinyAgentsError::InvalidConcurrentUpdate(message)
        }
        GraphError::Checkpoint(message) => TinyAgentsError::Checkpoint(message),
        GraphError::Resume(message) => TinyAgentsError::Resume(message),
        GraphError::Serialization(error) => TinyAgentsError::Serialization(error),
        other @ GraphError::Graph(_) => TinyAgentsError::Graph(other.to_string()),
    }
}

#[cfg(test)]
#[path = "flow_test.rs"]
mod test;
