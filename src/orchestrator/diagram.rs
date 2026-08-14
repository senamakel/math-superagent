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

use tinyflows::model::WorkflowGraph;
use tinyflows::visualization::render_graph;

use crate::error::{Error, Result};

use super::solutions::DIVERSIFY_MERGE;

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
const NODES: [(&str, &str); 13] = [
    ("start", "start"),
    (super::workflow::SEED_GOALS_NODE, "seed goals"),
    (super::workflow::LOOP_NODE, "solve"),
    ("attempt", "attempt"),
    ("judge", "judge"),
    ("reflect", "reflect"),
    (super::workflow::GOALS_NODE, "goals"),
    ("goal_apply", "cadence"),
    ("diversify_library", "library"),
    ("diversify_patterns", "patterns"),
    ("diversify_invention", "invention"),
    (DIVERSIFY_MERGE, "merge"),
    ("report", "report"),
];


/// The solution loop, as the engine runs it.
///
/// Previously this assembled a parallel description of the loop from the state
/// graph's routing tables, and the tests below existed to stop the two drifting.
/// There is nothing to drift from now: the loop *is* a `WorkflowGraph`, so the
/// diagram renders that graph rather than a drawing of it. A picture that can
/// disagree with what runs is no longer expressible here.
///
/// Node names are shortened for the renderer, which draws a name at double
/// scale inside a fixed 240px box and truncates on character count rather than
/// width — so anything past about thirteen characters runs out of its box.
#[must_use]
pub(super) fn solution_loop() -> WorkflowGraph {
    let mut graph = super::workflow::solution_loop("", Vec::new());
    graph.name = "solution loop".to_string();
    for node in &mut graph.nodes {
        if let Some((_, short)) = NODES.iter().find(|(id, _)| *id == node.id.as_str()) {
            node.name = (*short).to_string();
        }
    }
    graph
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
