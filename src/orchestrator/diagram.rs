//! Renders this crate's flows to images with `TinyFlows`' graph renderer.
//!
//! Behind the `graph-debug` feature, because it writes files and pulls in raster
//! encoders that a run has no use for. Nothing in a run reaches this module; it
//! exists so a reader can look at a flow rather than reconstruct it from the
//! code that builds it.
//!
//! # Why this is not a drawing
//!
//! It renders the [`WorkflowGraph`]s the engine actually runs. There was a
//! period when it could not: the loop was built with the lower-level state
//! graph, which exposes no way to read its edges back, so the diagram was
//! assembled from a parallel routing table and a pair of tests existed to stop
//! the two drifting. The alternative then on offer — writing the picture out by
//! hand — produces a diagram that is right on the day it is written and wrong
//! from the first routing change nobody remembers to mirror.
//!
//! Neither applies now. A flow *is* a graph, so the picture is that graph and a
//! picture that disagrees with what runs is no longer expressible here. What
//! this still does *not* prove is that a node does what its name says: the
//! topology is shared, the handlers are not.

use std::path::Path;

use tinyflows::model::WorkflowGraph;
use tinyflows::visualization::render_graph;

use crate::error::{Error, Result};

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
const NODES: [(&str, &str); 19] = [
    ("start", "start"),
    (super::workflow::RESEARCH_NODE, "research"),
    (super::workflow::SEED_CONTEXT_NODE, "seed ctx"),
    (super::workflow::SEED_GOALS_NODE, "seed goals"),
    (super::workflow::SEED_APPLY_NODE, "seed apply"),
    (super::workflow::LOOP_NODE, "solve"),
    ("attempt", "attempt"),
    ("judge", "judge"),
    ("reflect", "reflect"),
    ("eval_patterns", "patterns"),
    ("eval_invention", "invention"),
    ("eval_refutation", "refute"),
    (super::workflow::LIBRARY_ARM, "library"),
    (super::workflow::GOALS_NODE, "goals"),
    (super::workflow::GOAL_APPLY, "cadence"),
    (super::workflow::EVAL_MERGE, "merge"),
    ("diversify_library", "escalate"),
    (super::workflow::NOVELTY_NODE, "novelty"),
    ("report", "report"),
];

// The research child's nodes, which the loop's own list has no reason to name.
const RESEARCH_NODES: [(&str, &str); 3] = [
    ("research_start", "start"),
    (super::workflow_research::CONTEXT_NODE, "context"),
    (super::workflow_research::SURVEY_NODE, "survey"),
];


/// Every graph this crate runs, as `(file stem, the graph)`.
///
/// A list, and therefore something that can fall behind — so a test walks the
/// loop's `sub_workflow` nodes and fails on a child no flow draws. That is the
/// half worth enforcing: a top-level graph nobody renders is visible the moment
/// someone looks for it, while an embedded child is a whole flow that runs
/// inside a config value and appears in no picture at all.
///
/// The goals child appears twice in the loop — once seeded before the first
/// attempt, once after every reflection — and is drawn once, because both calls
/// embed the same graph.
#[must_use]
pub(super) fn flows() -> Vec<(&'static str, WorkflowGraph)> {
    vec![
        ("solution-loop", solution_loop()),
        ("goals", shorten(super::workflow_goals::goals_workflow())),
        (
            "research",
            shorten(super::workflow_research::research_workflow()),
        ),
    ]
}

/// Replaces node names with the short ones the renderer can draw.
fn shorten(mut graph: WorkflowGraph) -> WorkflowGraph {
    for node in &mut graph.nodes {
        if let Some((_, short)) = NODES
            .iter()
            .chain(RESEARCH_NODES.iter())
            .find(|(id, _)| *id == node.id.as_str())
        {
            node.name = (*short).to_string();
        }
    }
    graph
}

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
    let mut graph = shorten(super::workflow::solution_loop("", Vec::new()));
    graph.name = "solution loop".to_string();
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

/// Renders every flow into `directory`, one `<stem>.png` each.
///
/// Returns what it wrote, in the order the flows are listed.
///
/// # Errors
///
/// Returns [`Error::GraphRender`] for the first flow that could not be written.
/// The directory is not created; a missing one is reported rather than filled
/// in, for the reason [`render_solution_loop`] gives.
pub fn render_flows(directory: impl AsRef<Path>) -> Result<Vec<std::path::PathBuf>> {
    let directory = directory.as_ref();
    let mut written = Vec::new();
    for (stem, graph) in flows() {
        let path = directory.join(format!("{stem}.png"));
        render_graph(&graph, &path).map_err(|error| Error::GraphRender {
            path: path.display().to_string(),
            reason: error.to_string(),
        })?;
        written.push(path);
    }
    Ok(written)
}

#[cfg(test)]
#[path = "diagram_test.rs"]
mod test;
