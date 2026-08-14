//! The research sub-workflow: what the run knows before it attempts anything.
//!
//! Stage one of three. The loop's opening state is a problem statement and
//! eleven zeroes, and every role that then runs is handed that and told to go
//! and read the workspace itself. On a conjecture workspace — a research tree, a
//! claim ledger, threads, and whatever the last run left — that is a substantial
//! read, and each role paid for it separately while sharing none of it. A live
//! solver spent fourteen minutes and fifty-nine model calls on seventeen
//! `read_document` calls and nothing else.
//!
//! So it is asked once, here, before the loop starts: establish what is already
//! known, then go and find what is not.
//!
//! # Why a child rather than two nodes at the top of the loop graph
//!
//! Because it runs once and the loop runs eight times, and putting a
//! run-once stage inside a graph whose whole subject is repetition is how it
//! ends up repeated. The boundary also says what the stage is: everything in
//! here happens before an attempt exists, so nothing in here can read one.
//!
//! # Why the two nodes are in series
//!
//! The curator reads what is on disk and the librarian goes looking for what is
//! not. Running them concurrently would send the librarian out with the problem
//! statement as its only query, which is the weakest query the run will ever
//! have — the whole argument for the rescue sweep later in the loop is that a
//! query built from what the run knows beats one built from the statement. One
//! edge buys that.

use serde_json::{Value, json};
use tinyflows::model::{
    Edge, InputType, Node, NodeKind, TriggerKind, WorkflowGraph, WorkflowInput,
};

/// The child's name, and how the loop's diagram labels the node that calls it.
pub(super) const RESEARCH_WORKFLOW: &str = "research";

/// The input the child is handed: the loop's opening state.
pub(super) const STATE_INPUT: &str = "state";

/// The node that reads the workspace.
pub(super) const CONTEXT_NODE: &str = "context";

/// The node that starts the search for what the workspace does not have.
pub(super) const SURVEY_NODE: &str = "survey";

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
fn edge(from: &str, to: &str) -> Edge {
    Edge {
        from_node: from.into(),
        from_port: "main".into(),
        to_node: to.into(),
        to_port: "main".into(),
    }
}

/// Assembles the research workflow.
///
/// The survey is the same `eval_library` step the loop runs after every attempt:
/// it spawns the sweep and hands the state straight back. One step, two callers,
/// so a run does not have two different ideas of what "gather the literature"
/// means depending on when it asks.
#[must_use]
pub(super) fn research_workflow() -> WorkflowGraph {
    let nodes = vec![
        node(
            "research_start",
            NodeKind::Trigger,
            json!({ "kind": TriggerKind::ExecuteByWorkflow }),
        ),
        node(
            CONTEXT_NODE,
            NodeKind::ToolCall,
            json!({
                "slug": super::loop_steps::TOOL,
                "args": { "step": "init_context", "state": format!("=.inputs.{STATE_INPUT}") },
            }),
        ),
        node(
            SURVEY_NODE,
            NodeKind::ToolCall,
            json!({
                "slug": super::loop_steps::TOOL,
                "args": {
                    "step": "eval_library",
                    "state": format!("=.nodes.{CONTEXT_NODE}.item.json"),
                },
            }),
        ),
    ];

    let edges = vec![
        edge("research_start", CONTEXT_NODE),
        edge(CONTEXT_NODE, SURVEY_NODE),
    ];

    WorkflowGraph {
        id: Some(RESEARCH_WORKFLOW.into()),
        name: "research".into(),
        inputs: vec![WorkflowInput {
            name: STATE_INPUT.into(),
            ty: InputType::Json,
            description: Some("The solution loop's opening state.".into()),
            required: true,
            default: None,
        }],
        nodes,
        edges,
        ..WorkflowGraph::default()
    }
}

/// The state the child ended with, for the loop to start from.
///
/// The survey is the child's only terminal node, so unlike the goals child
/// there is no question of which arm ran — but the same envelope problem
/// applies, and the same reader answers it.
#[must_use]
pub(super) fn established(child: &Value) -> Option<Value> {
    child
        .get("nodes")
        .and_then(Value::as_object)
        .and_then(|nodes| nodes.get(SURVEY_NODE))
        .and_then(|slot| slot.get("items"))
        .and_then(Value::as_array)
        .and_then(|items| items.first())
        .and_then(|item| item.get("json"))
        .map(|json| json.get("json").unwrap_or(json).clone())
}

#[cfg(test)]
#[path = "workflow_research_test.rs"]
mod test;
