//! Renders the solution loop to an image with `TinyFlows`' graph renderer.
//!
//! Behind the `graph-debug` feature, because it writes files and pulls in raster
//! encoders that a run has no use for. Nothing in a run reaches this module; it
//! exists so a reader can look at the loop rather than reconstruct it from
//! `wire_routes`.
//!
//! # Why this is not a drawing
//!
//! `TinyFlows` renders a [`WorkflowGraph`] — the declarative workflow model —
//! while this crate's loop is built with the lower-level
//! [`GraphBuilder`](crate::agent::flow::GraphBuilder) state graph, which
//! exposes no way to read its edges back. So the two cannot be bridged
//! automatically, and the obvious alternative — writing the picture out by hand
//! — produces a diagram that is right on the day it is written and wrong from
//! the first routing change nobody remembers to mirror.
//!
//! Instead the loop's edges live in one table (`ENTRY`, `FINISH`,
//! `DIRECT_EDGES`, `JUDGE_ROUTES`, `REFLECT_ROUTES` in `solutions_state.rs`),
//! `wire_routes` builds the running graph from it, and [`solution_loop`] builds
//! the picture from it. A route added to the loop appears in the next render
//! without anyone maintaining a second copy; a route removed disappears from
//! it. The verdict labels are the same `Display` implementations the runtime
//! resolves a branch by, so an edge cannot be captioned with a word the router
//! does not actually produce.
//!
//! What this still does *not* prove is that a node does what its name says.
//! The topology is shared; the handlers are not.

use std::path::Path;

use tinyflows::model::{Edge, Node, NodeKind, WorkflowGraph};
use tinyflows::visualization::render_graph;

use crate::error::{Error, Result};

use super::solutions::{
    DIRECT_EDGES, DIVERSIFY_ARMS, DIVERSIFY_MERGE, ENTRY, FINISH, JUDGE_ROUTES, REFLECT_ROUTES,
};

/// The loop's nodes, as `(id, name)`.
///
/// Names are short and ASCII because the renderer is: it draws a name at
/// double scale inside a fixed 240px box and truncates on character count
/// rather than width, so anything past about thirteen characters runs out of
/// the box, and its 8x8 font has no glyph for an em dash. What each node is
/// *for* is in `docs/solution-loop.md`; a picture that tried to carry it would
/// carry it illegibly.
///
/// Node identity still comes from the edge table: a node named here but
/// unreachable renders detached, which is the renderer's way of showing
/// exactly that mistake.
const NODES: [(&str, &str); 9] = [
    ("attempt", "attempt"),
    ("judge", "judge"),
    ("reflect", "reflect"),
    ("diversify", "diversify"),
    ("diversify_library", "library"),
    ("diversify_patterns", "patterns"),
    ("diversify_invention", "invention"),
    (DIVERSIFY_MERGE, "merge"),
    ("done", "done"),
];

/// Builds the solution loop as a `TinyFlows` workflow graph.
///
/// The result is a description for rendering and inspection, not something to
/// run: the nodes carry no configuration, because the work each one does is a
/// Rust handler in `solutions_state.rs` rather than a workflow node kind.
///
/// The renderer captions an edge `from_port -> to_port`, so the verdict goes
/// in `from_port` and the destination in `to_port`: an edge reads
/// `solved -> done`. An unconditional edge is captioned `always`, so a reader
/// can tell a branch that happens to have one arm from an edge that is not a
/// branch. The verdicts are the routers' own `Display` output — the string the
/// runtime resolves a branch by — so a caption cannot name a route the router
/// does not produce. The renderer truncates a caption at eighteen characters,
/// which bites only `reported unverified`; the arrow still shows where it
/// goes.
#[must_use]
pub(super) fn solution_loop() -> WorkflowGraph {
    let mut graph = WorkflowGraph {
        name: format!("solution loop: {ENTRY} -> {FINISH}"),
        ..WorkflowGraph::default()
    };
    graph.nodes = NODES
        .iter()
        .map(|(id, name)| Node {
            id: (*id).into(),
            // Every node but the terminal one runs an agent turn; `done` only
            // passes the final state through.
            kind: if *id == FINISH {
                NodeKind::Transform
            } else {
                NodeKind::Agent
            },
            type_version: 1,
            name: (*name).to_string(),
            config: serde_json::Value::Null,
            ports: Vec::new(),
            position: None,
        })
        .collect();

    let mut edges: Vec<Edge> = DIRECT_EDGES
        .iter()
        .map(|(from, to)| edge(from, "always", to))
        .collect();
    // The fan-out and the join. Captioned distinctly from `always` because they
    // are the two edges in the loop that are not one-in-one-out: `fanout` marks
    // three successors leaving together, and `join` marks an arrival the merge
    // waits on rather than acts on.
    edges.extend(
        DIVERSIFY_ARMS
            .iter()
            .map(|arm| edge("diversify", "fanout", arm)),
    );
    edges.extend(
        DIVERSIFY_ARMS
            .iter()
            .map(|arm| edge(arm, "join", DIVERSIFY_MERGE)),
    );
    edges.extend(
        JUDGE_ROUTES
            .iter()
            .map(|(verdict, to)| edge("judge", &verdict.to_string(), to)),
    );
    edges.extend(
        REFLECT_ROUTES
            .iter()
            .map(|(verdict, to)| edge("reflect", &verdict.to_string(), to)),
    );
    graph.edges = edges;
    graph
}

/// One captioned edge.
fn edge(from: &str, caption: &str, to: &str) -> Edge {
    Edge {
        from_node: from.into(),
        from_port: caption.to_string(),
        to_node: to.into(),
        to_port: to.to_string(),
    }
}

/// Renders the solution loop to `path`, which must end in `.png`, `.jpg`, or
/// `.jpeg`.
///
/// # Errors
///
/// Returns [`Error::GraphRender`] when the extension is not one the renderer
/// supports, or when the file could not be written. Parent directories are not
/// created; a missing one is reported rather than filled in, because the only
/// caller passes a path a person just typed.
pub fn render_solution_loop(path: impl AsRef<Path>) -> Result<()> {
    let path = path.as_ref();
    render_graph(&solution_loop(), path).map_err(|error| Error::GraphRender {
        path: path.display().to_string(),
        reason: error.to_string(),
    })
}

#[cfg(test)]
#[path = "diagram_test.rs"]
mod test;
