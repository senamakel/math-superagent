//! Tests for the workflow-editing surface.
#![allow(clippy::expect_used)]

use serde_json::json;
use tinyflows::graph_ops::GraphOp;
use tinyflows::model::{Node, NodeKind};

use super::*;

/// A workspace that cleans up after itself.
struct Scratch {
    root: PathBuf,
}

impl Scratch {
    fn new(name: &str) -> Self {
        let root = std::env::temp_dir().join(format!("riemann-wf-{name}-{}", std::process::id()));
        let _ = std::fs::remove_dir_all(&root);
        std::fs::create_dir_all(&root).expect("a scratch workspace can be created");
        Self { root }
    }

    fn catalog(&self) -> WorkflowCatalog {
        WorkflowCatalog::open(&self.root).expect("the catalog opens")
    }
}

impl Drop for Scratch {
    fn drop(&mut self) {
        let _ = std::fs::remove_dir_all(&self.root);
    }
}

fn node(id: &str, kind: NodeKind) -> Node {
    Node {
        id: id.into(),
        kind,
        type_version: 1,
        name: id.to_string(),
        config: serde_json::Value::Null,
        ports: Vec::new(),
        position: None,
    }
}

fn saved(scratch: &Scratch) -> WorkflowCatalog {
    let catalog = scratch.catalog();
    let graph = crate::orchestrator::workflow::solution_loop("a problem", Vec::new());
    catalog.create("solve", &graph).expect("the loop saves");
    catalog
}

#[test]
fn the_loop_round_trips_through_the_catalog() {
    let scratch = Scratch::new("roundtrip");
    let catalog = saved(&scratch);
    let record = catalog.read("solve").expect("the document is there");
    assert!(record.graph.nodes.iter().any(|n| n.id.as_str() == "solve"));
}

/// The point of previewing: see the change without committing it.
#[test]
fn a_preview_shows_the_change_without_saving_it() {
    let scratch = Scratch::new("preview");
    let catalog = saved(&scratch);

    let ops = vec![GraphOp::AddNode {
        node: node("audit", NodeKind::Transform),
    }];
    let previewed = catalog.preview("solve", &ops).expect("the op is valid");
    assert!(previewed.nodes.iter().any(|n| n.id.as_str() == "audit"));

    // ...and the saved document is untouched.
    let stored = catalog.read("solve").expect("still there");
    assert!(!stored.nodes_contain("audit"));
}

/// Validation at the edit, not at the run. A graph that could not run is
/// refused when it is written.
#[test]
fn an_edit_that_would_not_run_is_refused_at_the_edit() {
    let scratch = Scratch::new("invalid");
    let catalog = saved(&scratch);

    // An edge to a node that does not exist.
    let ops = vec![GraphOp::AddEdge {
        edge: tinyflows::model::Edge {
            from_node: "solve".into(),
            from_port: "body".into(),
            to_node: "nowhere".into(),
            to_port: "main".into(),
        },
    }];
    let refused = catalog.preview("solve", &ops);
    assert!(refused.is_err(), "an edge to nowhere was accepted");
}

/// Two agents editing one workflow is ordinary here, and last-write-wins would
/// discard the loser's change without either of them learning it happened.
#[test]
fn a_stale_editor_is_refused_rather_than_overwriting() {
    let scratch = Scratch::new("concurrent");
    let catalog = saved(&scratch);

    // Both agents read the same fingerprint.
    let seen = catalog.fingerprint("solve").expect("a fingerprint");

    let first = catalog
        .apply_if_unchanged(
            "solve",
            &[GraphOp::AddNode {
                node: node("first", NodeKind::Transform),
            }],
            &seen,
        )
        .expect("the first edit applies");
    assert!(first.is_some(), "the first editor was refused");

    // The second is working from what it read before the first landed.
    let second = catalog
        .apply_if_unchanged(
            "solve",
            &[GraphOp::AddNode {
                node: node("second", NodeKind::Transform),
            }],
            &seen,
        )
        .expect("a stale edit is a signal, not a failure");
    assert!(second.is_none(), "a stale editor overwrote a newer document");

    // The first editor's change survived.
    let stored = catalog.read("solve").expect("still there");
    assert!(stored.nodes_contain("first"));
    assert!(!stored.nodes_contain("second"));
}

/// Re-reading and retrying is the intended answer to a refusal.
#[test]
fn a_refused_editor_succeeds_after_re_reading() {
    let scratch = Scratch::new("retry");
    let catalog = saved(&scratch);
    let stale = catalog.fingerprint("solve").expect("a fingerprint");
    catalog
        .apply_if_unchanged(
            "solve",
            &[GraphOp::AddNode {
                node: node("first", NodeKind::Transform),
            }],
            &stale,
        )
        .expect("applies");

    let fresh = catalog.fingerprint("solve").expect("a fresh fingerprint");
    assert_ne!(fresh, stale);
    let retried = catalog
        .apply_if_unchanged(
            "solve",
            &[GraphOp::AddNode {
                node: node("second", NodeKind::Transform),
            }],
            &fresh,
        )
        .expect("applies");
    assert!(retried.is_some());
}

/// A threshold is the change an outside agent is most likely to want, so it is
/// worth proving it is reachable as a patch rather than a rewrite.
#[test]
fn a_threshold_can_be_changed_by_patching_one_node() {
    let scratch = Scratch::new("threshold");
    let catalog = saved(&scratch);
    let seen = catalog.fingerprint("solve").expect("a fingerprint");

    let patched = catalog
        .apply_if_unchanged(
            "solve",
            &[GraphOp::UpdateNodeConfig {
                id: "solve".into(),
                config: json!({ "max_iterations": 12 }),
            }],
            &seen,
        )
        .expect("the patch applies")
        .expect("the document had not moved");

    let ceiling = patched
        .graph
        .nodes
        .iter()
        .find(|n| n.id.as_str() == "solve")
        .and_then(|n| n.config.get("max_iterations"))
        .cloned();
    assert_eq!(ceiling, Some(json!(12)));
}

/// Test-only convenience so the assertions above read as questions about the
/// graph rather than about iterators.
trait NodesContain {
    fn nodes_contain(&self, id: &str) -> bool;
}

impl NodesContain for tinyflows::store::WorkflowRecord {
    fn nodes_contain(&self, id: &str) -> bool {
        self.graph.nodes.iter().any(|node| node.id.as_str() == id)
    }
}
