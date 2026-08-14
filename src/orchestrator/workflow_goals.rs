//! The goals sub-workflow: what would suffice to prove the thing.
//!
//! The solution loop asks, every cycle, how the last attempt went. Nothing in
//! it ever asks what a proof of the goal would *consist of*, and the two
//! questions have different answers — an investigation can report genuine
//! progress every attempt, a bound pushed further and more cases verified, and
//! still end its budget with a great deal of data and no statement of what
//! would have been enough. A live Gilbreath workspace contains that statement
//! and it took sixteen operator directives to produce.
//!
//! So the loop asks it too, on a cadence, as a child workflow.
//!
//! # Why a sub-workflow rather than three more nodes in the loop
//!
//! Because it is a separate question with its own policy. The loop's graph is
//! about how an attempt is judged and what happens next; this is about how
//! often the goal is decomposed and what stops two decompositions colliding.
//! Inlining it would mix the two, and an operator changing the cadence would be
//! editing the routing graph to do it.
//!
//! It is also the first thing here with a *reason* to be a child: the cadence,
//! the gate, and the arm are one unit that can be reasoned about, tested, and
//! patched without reference to the ladder — which is exactly the boundary
//! [`tinyflows::model::NodeKind::SubWorkflow`] exists to draw.
//!
//! # What this costs the loop
//!
//! On most cycles, nothing: the cadence holds and the child returns in the time
//! it takes to evaluate one expression. On the cycle it does not hold, the
//! decomposition is awaited — it is one of the evaluation arms, running beside
//! the reflection rather than after it, so the pass costs the slowest arm and
//! not the sum.
//!
//! It was detached before, for a reason that was real: awaiting a reducer
//! *after* the reflection put a child run of unbounded length between the
//! reflection and the next attempt, which is the failure the mailboxes were
//! written about, where a live run sat 33 minutes unable to start an attempt it
//! was ready for. Running it *with* the reflection is what changed. What that
//! buys is that the next attempt sees this cycle's skeleton rather than the
//! previous one's.
//!
//! # What each half owns
//!
//! The cadence is here, in jq, because "how often" is the decision an operator
//! most wants to change without a rebuild. The fingerprint and the claim are in
//! [`reduce_arm`], because a workspace that has not moved and a reducer already
//! in flight are facts about the world rather than about the loop's state, and
//! neither is expressible as an expression over an accumulator.
//!
//! [`reduce_arm`]: super::solutions

use serde_json::{Value, json};
use tinyflows::model::{
    Edge, InputType, Node, NodeKind, TriggerKind, WorkflowGraph, WorkflowInput,
};

use super::schools::Thresholds;

/// The child's name, and how the loop's diagram labels the node that calls it.
pub(super) const GOALS_WORKFLOW: &str = "goals";

/// The input the child is handed: the state the reflection just produced.
///
/// Named rather than read off the trigger payload. A child seeded from its
/// input items addresses them as `run.trigger[0].json`, which is an
/// implementation detail of how the parent happened to be wired; a declared
/// input is the child's signature, validated before it runs.
pub(super) const STATE_INPUT: &str = "state";

/// The node whose output says whether a decomposition was opened.
pub(super) const GATE_NODE: &str = "gate";

/// The field that answer is carried in.
///
/// One name, shared by the step that writes it and the step that reads it, so
/// the two cannot disagree silently — the failure mode that made the loop's
/// restart arm unreachable for a release.
pub(super) const OPENED_FIELD: &str = "reduction_opened";

/// Whether this cycle is the one that decomposes the goal, as jq.
///
/// Two ways to decline and they are different: a solved run has no use for a
/// decomposition of a goal it has already reached, and a run inside the
/// interval has one recently enough. The interval comes from the school's
/// [`Thresholds`] for the reason every threshold in `super::workflow` does — a
/// second copy is a second answer, and here the second answer would be silent:
/// a school that decomposed on a different cadence would get the control's
/// instead, and nothing about the run would look wrong.
#[must_use]
pub(super) fn cadence(thresholds: &Thresholds) -> String {
    let interval = thresholds.reduction_interval;
    format!(
        "=if .inputs.{STATE_INPUT}.solved then \"hold\" \
         elif (.inputs.{STATE_INPUT}.since_reduction // 0) < {interval} then \"hold\" \
         else \"check\" end"
    )
}

/// Builds one node.
fn node(id: &str, kind: NodeKind, config: Value) -> Node {
    Node {
        id: id.into(),
        kind,
        type_version: 1,
        name: id.to_string(),
        config,
        ports: Vec::new(),
        position: None,
    }
}

/// Builds one edge on the named ports.
fn edge(from: &str, from_port: &str, to: &str) -> Edge {
    Edge {
        from_node: from.into(),
        from_port: from_port.to_string(),
        to_node: to.into(),
        to_port: "main".into(),
    }
}

/// Assembles the goals workflow.
///
/// Two terminal nodes rather than one, and deliberately not converged. A node
/// with more than one predecessor is a fan-in *barrier* in this engine — it
/// waits for all of them — so joining two arms only one of which ever runs
/// would hang the child. The parent reads whichever arm ran out of the child's
/// run state; see [`super::loop_steps`].
#[must_use]
pub(super) fn goals_workflow(thresholds: &Thresholds) -> WorkflowGraph {
    let nodes = vec![
        node(
            "goal_start",
            NodeKind::Trigger,
            json!({ "kind": TriggerKind::ExecuteByWorkflow }),
        ),
        node("due", NodeKind::Switch, json!({ "expression": cadence(thresholds) })),
        node(
            GATE_NODE,
            NodeKind::ToolCall,
            json!({
                "slug": super::loop_steps::TOOL,
                "args": { "step": "goal_gate", "state": format!("=.inputs.{STATE_INPUT}") },
            }),
        ),
        // A `set` rather than a passthrough, so the declined branch says what it
        // decided instead of being recognised by the absence of the other one.
        node(
            "held",
            NodeKind::Transform,
            json!({ "set": { OPENED_FIELD: false, "why": "not due" } }),
        ),
    ];

    let edges = vec![
        edge("goal_start", "main", "due"),
        edge("due", "check", GATE_NODE),
        edge("due", "hold", "held"),
    ];

    WorkflowGraph {
        id: Some(GOALS_WORKFLOW.into()),
        name: "goals".into(),
        inputs: vec![WorkflowInput {
            name: STATE_INPUT.into(),
            ty: InputType::Json,
            description: Some("The solution loop's state, as the reflection left it.".into()),
            required: true,
            default: None,
        }],
        nodes,
        edges,
        ..WorkflowGraph::default()
    }
}

/// Whether a child run opened a decomposition.
///
/// Reads the whole child run state and looks for the answer wherever it is,
/// rather than pointing at one node's first item. The child has two terminal
/// arms and only one of them runs, so a fixed pointer would have to name both
/// and would break the moment either is renamed — and the failure would be
/// silent, because a missing pointer reads exactly like "did not open".
#[must_use]
pub(super) fn opened(child: &Value) -> bool {
    carriers(child).any(|carrier| {
        carrier
            .get(OPENED_FIELD)
            .and_then(Value::as_bool)
            .unwrap_or_default()
    })
}

/// Every object in a child run state that could be carrying the gate's answer.
///
/// Reads the whole run state and looks for the answer wherever it is, rather
/// than pointing at one node's first item. The child has two terminal arms and
/// only one of them runs, so a fixed pointer would have to name both and would
/// break the moment either is renamed — and the failure would be silent,
/// because a missing pointer reads exactly like "did not open".
fn carriers(child: &Value) -> impl Iterator<Item = Value> + '_ {
    child
        .get("nodes")
        .and_then(Value::as_object)
        .into_iter()
        .flat_map(|nodes| nodes.values())
        .filter_map(|slot| slot.get("items").and_then(Value::as_array))
        .flatten()
        .flat_map(|item| {
            // Both shapes, because the child's two arms are different node
            // kinds: a `tool_call` wraps its result in the `{ json, text, raw }`
            // envelope, a `transform` passes its item through bare. Reading only
            // one would make the answer depend on which arm ran, which is
            // exactly what this must not do.
            let payload = item.get("json").cloned();
            let inner = payload
                .as_ref()
                .and_then(|json| json.get("json"))
                .cloned();
            [payload, inner].into_iter().flatten()
        })
}

#[cfg(test)]
#[path = "workflow_goals_test.rs"]
mod test;
