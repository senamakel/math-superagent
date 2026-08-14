#![allow(clippy::expect_used)]

use super::*;

use tinyflows::graph::{GraphBuilder, NodeContext, NodeResult};

#[test]
fn preserves_a_timeout_across_the_seam() {
    let graph = into_graph(TinyAgentsError::Timeout("run timed out".into()));
    assert!(matches!(graph, GraphError::Timeout(ref message) if message == "run timed out"));
    assert!(matches!(
        from_graph(graph),
        TinyAgentsError::Timeout(message) if message == "run timed out"
    ));
}

#[test]
fn preserves_a_cancellation_across_the_seam() {
    assert!(matches!(
        into_graph(TinyAgentsError::Cancelled),
        GraphError::Cancelled
    ));
    assert!(matches!(
        from_graph(GraphError::Cancelled),
        TinyAgentsError::Cancelled
    ));
}

#[test]
fn round_trips_every_variant_the_two_enums_share() {
    let shared = [
        TinyAgentsError::MissingStart,
        TinyAgentsError::MissingNode("attempt".into()),
        TinyAgentsError::MissingEdgeTarget("judge".into()),
        TinyAgentsError::MissingRoute {
            node: "reflect".into(),
            route: "solved".into(),
        },
        TinyAgentsError::RecursionLimit(25),
        TinyAgentsError::SubAgentDepth(3),
        TinyAgentsError::NodeVisitLimit {
            node: "attempt".into(),
            limit: 8,
        },
        TinyAgentsError::Validation("bad input".into()),
        TinyAgentsError::Timeout("too slow".into()),
        TinyAgentsError::Cancelled,
        TinyAgentsError::Interrupted {
            node: "diversify".into(),
            message: "approve?".into(),
        },
        TinyAgentsError::InvalidConcurrentUpdate("state".into()),
        TinyAgentsError::Checkpoint("unwritable".into()),
        TinyAgentsError::Resume("no thread".into()),
    ];
    for error in shared {
        let rendered = error.to_string();
        let returned = from_graph(into_graph(error));
        // Equality is unavailable — `TinyAgentsError` carries a
        // `serde_json::Error` — so the rendered message stands in for the
        // variant, which is what a caller reading the failure sees anyway.
        assert_eq!(returned.to_string(), rendered);
    }
}

#[test]
fn degrades_a_harness_only_failure_to_a_graph_error() {
    // Nothing in the graph runtime can raise a tool failure, so it arrives as
    // the generic variant with its message intact rather than being invented
    // into a neighbouring one.
    let graph = into_graph(TinyAgentsError::Tool("exa refused".into()));
    assert!(matches!(graph, GraphError::Graph(ref message) if message.contains("exa refused")));
}

#[tokio::test]
async fn drives_a_two_node_loop_on_the_tinyflows_runtime() {
    // The migration's actual claim: a graph built the way the solution loop
    // builds one compiles and runs on TinyFlows' runtime, cycles through a
    // conditional edge, and returns its final state.
    let graph = GraphBuilder::<u32, u32>::overwrite()
        .add_node("attempt", |state: u32, _ctx: NodeContext| async move {
            Ok(NodeResult::Update(state + 1))
        })
        .add_node("done", |state: u32, _ctx: NodeContext| async move {
            Ok(NodeResult::Update(state))
        })
        .set_entry("attempt")
        .add_conditional_edges(
            "attempt",
            |state: &u32| if *state < 3 { "retry" } else { "stop" },
            [("retry", "attempt"), ("stop", "done")],
        )
        .set_finish("done")
        .compile()
        .expect("a graph with an entry, a finish, and routed edges compiles");

    let execution = graph
        .run(0)
        .await
        .expect("the loop runs to its finish node");
    assert_eq!(execution.state, 3);
}

#[tokio::test]
async fn a_fan_out_runs_its_arms_at_once_and_the_barrier_waits_for_all_of_them() {
    // The two primitives the diversify step now rests on, exercised together:
    // one node commands three successors, each writes its own slot, and the
    // merge runs once — after all three have arrived, not once per arrival.
    use std::sync::Arc;
    use std::sync::atomic::{AtomicUsize, Ordering};

    use tinyflows::graph::{ClosureStateReducer, Command};

    #[derive(Clone, Debug, Default, PartialEq, Eq)]
    struct State {
        slots: Vec<&'static str>,
        merges: usize,
    }

    #[derive(Clone, Debug)]
    enum Update {
        Slot(&'static str),
        Merged,
    }

    let live = Arc::new(AtomicUsize::new(0));
    let peak = Arc::new(AtomicUsize::new(0));

    let mut builder = GraphBuilder::<State, Update>::new()
        .set_reducer(ClosureStateReducer::new(
            |mut state: State, update: Update| {
                match update {
                    // Disjoint slots, so the order arms are committed in cannot
                    // change the result — sorted here only so the assertion can
                    // be written without depending on that order.
                    Update::Slot(name) => {
                        state.slots.push(name);
                        state.slots.sort_unstable();
                    }
                    Update::Merged => state.merges += 1,
                }
                Ok(state)
            },
        ))
        .with_parallel(true)
        .add_node("fan", |_state: State, _ctx: NodeContext| async move {
            Ok(NodeResult::Command(Command::goto(["a", "b", "c"])))
        });

    for arm in ["a", "b", "c"] {
        let live = live.clone();
        let peak = peak.clone();
        builder = builder.add_node(arm, move |_state: State, _ctx: NodeContext| {
            let live = live.clone();
            let peak = peak.clone();
            async move {
                // Records how many arms were inside a node at the same moment.
                // Without `with_parallel(true)` this never exceeds one, which is
                // the failure the loop would silently regress to.
                let now = live.fetch_add(1, Ordering::SeqCst) + 1;
                peak.fetch_max(now, Ordering::SeqCst);
                tokio::time::sleep(std::time::Duration::from_millis(50)).await;
                live.fetch_sub(1, Ordering::SeqCst);
                Ok(NodeResult::Update(Update::Slot(arm)))
            }
        });
    }

    let graph = builder
        .add_node("merge", |_state: State, _ctx: NodeContext| async move {
            Ok(NodeResult::Update(Update::Merged))
        })
        .set_entry("fan")
        .with_unconditional_fanout("fan", ["a", "b", "c"])
        .add_waiting_edge("a", "merge")
        .add_waiting_edge("b", "merge")
        .add_waiting_edge("c", "merge")
        .set_finish("merge")
        .compile()
        .expect("a fan-out with a registered barrier compiles");

    let execution = graph
        .run(State::default())
        .await
        .expect("the fan-out runs and the barrier clears");

    assert_eq!(execution.state.slots, ["a", "b", "c"]);
    // Once, not three times: a merge that ran per arrival would start an
    // attempt on the first arm home and discard the other two.
    assert_eq!(execution.state.merges, 1);
    assert!(
        peak.load(Ordering::SeqCst) > 1,
        "arms took turns instead of running together"
    );
}
