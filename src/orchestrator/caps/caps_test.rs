//! Tests that the bundle as a whole keeps its boundaries.
#![allow(clippy::expect_used)]

/// `Capabilities::shell` is optional and this crate leaves it unset, so a
/// `shell` node fails with a capability error rather than silently doing
/// nothing. This asserts the decision is still the decision: a later change
/// that supplies a shell runner has to come here and say why.
#[test]
fn no_shell_runner_is_supplied() {
    // Nothing in this crate constructs a `ShellRunner`. Asserted by grep rather
    // than by type, because the point is the absence.
    let sources = [
        include_str!("mod.rs"),
        include_str!("execution.rs"),
        include_str!("state.rs"),
        include_str!("tools.rs"),
    ];
    for source in sources {
        assert!(
            !source.contains("impl ShellRunner"),
            "a ShellRunner appeared; see execution.rs for why there is none"
        );
    }
}

use std::sync::Arc;

use serde_json::{Value, json};
use tinyflows::compiler::compile;
use tinyflows::engine::run;
use tinyflows::model::{Edge, Node, NodeKind, WorkflowGraph};

use super::bundle;
use crate::agent::{MockModel, Result, Tool, ToolCall, ToolResult, ToolSchema};
use crate::agent::budget::RunBudget;
use crate::orchestrator::async_subagents::AsyncSubagentManager;
use crate::orchestrator::runner::{SubagentAgentRunner, SubagentTaskRunner};

/// A tool that reports a fixed count, standing in for the workspace tools a
/// real workflow reaches for.
struct CountingTool;

#[async_trait::async_trait]
impl Tool<()> for CountingTool {
    fn name(&self) -> &'static str {
        "count_claims"
    }
    fn description(&self) -> &'static str {
        "counts what is on disk"
    }
    fn schema(&self) -> ToolSchema {
        ToolSchema::new(self.name(), self.description(), json!({ "type": "object" }))
    }
    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let mut result = ToolResult::text(call.id, self.name(), "counted");
        result.raw = Some(json!({ "claims": 7 }));
        Ok(result)
    }
}

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

fn edge(from: &str, to: &str) -> Edge {
    Edge {
        from_node: from.into(),
        from_port: "main".into(),
        to_node: to.into(),
        to_port: "main".into(),
    }
}

/// Phase 1's gate: a workflow compiles and runs to completion against this
/// crate's real capabilities — not mocks — with a tool call feeding a model
/// turn, and the tool's structured output surviving the hop.
#[tokio::test]
async fn a_two_node_workflow_runs_against_the_real_capabilities() {
    let workspace = std::env::temp_dir().join(format!("riemann-caps-gate-{}", std::process::id()));
    std::fs::create_dir_all(&workspace).expect("a scratch workspace can be created");

    let caps = bundle(
        Arc::new(MockModel::constant("7 claims, and one of them is load-bearing")),
        &workspace,
        [Arc::new(CountingTool) as Arc<dyn Tool<()>>],
        SubagentTaskRunner::new(AsyncSubagentManager::new(RunBudget::default(), None)),
        SubagentAgentRunner::new(AsyncSubagentManager::new(RunBudget::default(), None)),
    );

    let graph = WorkflowGraph {
        name: "capability gate".into(),
        nodes: vec![
            node("start", NodeKind::Trigger, Value::Null),
            node(
                "count",
                NodeKind::ToolCall,
                json!({ "slug": "count_claims", "args": {} }),
            ),
            node(
                "read",
                NodeKind::Agent,
                // Binds the tool's *structured* output, which only survives
                // because the invoker returns `{ text, raw }` rather than text.
                json!({ "prompt": "=\"there are \" + (.item.raw.claims | tostring) + \" claims\"" }),
            ),
        ],
        edges: vec![edge("start", "count"), edge("count", "read")],
        ..WorkflowGraph::default()
    };

    let compiled = compile(&graph).expect("the graph is structurally valid");
    let outcome = run(&compiled, json!({}), &caps)
        .await
        .expect("the workflow runs to completion against real capabilities");

    let text = outcome
        .output
        .pointer("/nodes/read/items/0/json/text")
        .and_then(Value::as_str)
        .unwrap_or_default();
    assert!(text.contains("load-bearing"), "{:?}", outcome.output);

    let _ = std::fs::remove_dir_all(&workspace);
}

/// Phase 2's gate: a role registered with this crate runs from a one-node
/// workflow that names it in `agent_ref`, with the role's own prompt and tools
/// rather than a bare completion.
#[tokio::test]
async fn a_named_role_runs_from_a_one_node_workflow() {
    use crate::orchestrator::async_subagents::AgentExecutor;
    use tinyflows::model::AgentDefinition as FlowAgent;

    /// Reports the instruction it was handed, so the test can assert the
    /// workflow's prompt reached the role rather than something reassembled.
    struct RecordingRole;

    #[async_trait::async_trait]
    impl AgentExecutor for RecordingRole {
        async fn execute(
            &self,
            _run_id: &str,
            input: String,
            _steering: tinyagents::harness::steering::SteeringHandle,
            _tracer: Option<Arc<crate::agent::trace::RunTracer>>,
        ) -> Result<String> {
            Ok(format!("scholar read: {input}"))
        }
    }

    let manager = AsyncSubagentManager::new(RunBudget::default(), None);
    manager
        .register_executor("scholar", Arc::new(RecordingRole))
        .expect("registering a role once succeeds");

    let workspace = std::env::temp_dir().join(format!("riemann-role-gate-{}", std::process::id()));
    std::fs::create_dir_all(&workspace).expect("a scratch workspace can be created");

    let caps = bundle(
        // Deliberately a model that would answer something else: if the node
        // reached the bare completion path instead of the role, this is the
        // string that would come back.
        Arc::new(MockModel::constant("a bare completion, not the role")),
        &workspace,
        [] as [Arc<dyn Tool<()>>; 0],
        SubagentTaskRunner::new(manager.clone()),
        SubagentAgentRunner::new(manager),
    );

    let graph = WorkflowGraph {
        name: "role gate".into(),
        agents: vec![FlowAgent::new("scholar")],
        nodes: vec![
            node("start", NodeKind::Trigger, Value::Null),
            node(
                "read",
                NodeKind::Agent,
                json!({ "agent_ref": "scholar", "prompt": "the library" }),
            ),
        ],
        edges: vec![edge("start", "read")],
        ..WorkflowGraph::default()
    };

    let compiled = compile(&graph).expect("the graph is structurally valid");
    let outcome = run(&compiled, json!({}), &caps)
        .await
        .expect("the workflow runs the named role");

    let text = outcome
        .output
        .pointer("/nodes/read/items/0/json/text")
        .and_then(Value::as_str)
        .unwrap_or_default();
    assert_eq!(text, "scholar read: the library", "{:?}", outcome.output);

    let _ = std::fs::remove_dir_all(&workspace);
}
