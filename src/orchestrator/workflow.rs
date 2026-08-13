//! The solution loop as a `WorkflowGraph`.
//!
//! The same attempt/judge/reflect loop `solutions` runs on the state graph,
//! authored declaratively: a `loop` head carrying the run's counters as its
//! accumulator, `switch` nodes carrying the routing ladder as jq, and the
//! diversify arms as parallel successors converging on a `merge`.
//!
//! # Where the state lives
//!
//! The question that decides whether this is expressible at all. A workflow's
//! data flow is per-node items, which has nowhere to keep eight counters that
//! accumulate across attempts — but a `loop` node holds an *accumulator*:
//! `state.init` seeds it, `state.update` folds each pass's output into it, it
//! survives checkpoint and resume, and it is addressable from anywhere in the
//! graph as `=nodes.solve.state`. That is [`SolutionState`](super::solutions),
//! and the loop head is its sole writer.
//!
//! # Why the thresholds are generated
//!
//! Every number in the routing ladder is read from the Rust constant rather
//! than typed into the JSON. `MAX_ATTEMPTS` is eight, `UNVERIFIED_THRESHOLD` is
//! two, and each carries a paragraph naming the live run that produced it — a
//! second copy in a JSON document would be a second answer to a question the
//! repository has already paid to answer once.
//!
//! It also removes the failure this whole migration is most exposed to. Two
//! engines deciding the same run differently is invisible in a live run and
//! obvious only in a diff, and a ladder reading `>` where the Rust reads `>=`
//! is exactly that kind of drift. Sharing the numbers cannot prevent an
//! operator being wrong, which is what the parity harness is for, but it
//! removes the whole class of failure where the two simply disagree about a
//! constant.

use serde_json::{Value, json};
use tinyflows::model::{Edge, Node, NodeKind, WorkflowGraph};

use super::solutions::{
    BLOCKED_THRESHOLD, COMPUTATIONAL_THRESHOLD, MAX_ATTEMPTS, MAX_RESTARTS, STUCK_THRESHOLD,
    UNVERIFIED_THRESHOLD,
};

/// The loop head, and the accumulator's address.
pub(super) const LOOP_NODE: &str = "solve";

/// The diversify arms, matching the state graph's.
pub(super) const ARMS: [(&str, &str); 3] = [
    ("diversify_library", "librarian"),
    ("diversify_patterns", "pattern_finder"),
    ("diversify_invention", "inventor"),
];

/// The routing ladder out of the reflection, as jq.
///
/// The order is load-bearing and is the Rust function's, arm for arm. `blocked`
/// is checked before anything else because an attempt that died on the provider
/// is not evidence about the mathematics, and a live pair of runs once burned
/// all eight attempts on an `HTTP 403` and reported "not solved within 8
/// attempts" — which reads as a mathematical failure and is not one. `reported`
/// sits above both stuck arms because a run that has twice failed to find a
/// second route accumulates exactly the unproductive count that would otherwise
/// send it to diversify, and diversifying spends three child runs hunting a new
/// line of attack on a problem whose answer is already on disk.
#[must_use]
pub(super) fn reflect_ladder() -> String {
    format!(
        "=if .nodes.{LOOP_NODE}.state.blocked >= {BLOCKED_THRESHOLD} then \"blocked\" \
         elif .nodes.{LOOP_NODE}.state.solved or .nodes.{LOOP_NODE}.state.attempts >= \
         {MAX_ATTEMPTS} then \"solved\" \
         elif .nodes.{LOOP_NODE}.state.unverified >= {UNVERIFIED_THRESHOLD} then \"reported\" \
         elif .nodes.{LOOP_NODE}.state.unproductive >= {STUCK_THRESHOLD} then \"diversify\" \
         elif .nodes.{LOOP_NODE}.state.computational >= {COMPUTATIONAL_THRESHOLD} then \
         \"diversify\" \
         else \"retry\" end"
    )
}

/// The ladder out of the judge, as jq.
///
/// Two rules the Rust carries and this must not lose. A restart is bounded by
/// `MAX_RESTARTS`, because a judge that dislikes the run's whole approach would
/// otherwise reset it until the attempt ceiling stopped the loop and the run
/// would end having explored nothing to its conclusion. And the attempt ceiling
/// outranks a restart, so a run on its last attempt reflects on what it has
/// rather than stopping with nothing.
#[must_use]
pub(super) fn judge_ladder() -> String {
    format!(
        "=if .nodes.{LOOP_NODE}.state.attempts >= {MAX_ATTEMPTS} then \"reflect\" \
         elif .nodes.{LOOP_NODE}.state.restarts >= {MAX_RESTARTS} then \"reflect\" \
         elif .item.json.verdict == \"restart\" then \"restart\" \
         else \"reflect\" end"
    )
}

/// When the loop is finished, as jq.
///
/// The three terminal arms of [`reflect_ladder`], and deliberately the same
/// numbers: a run stops when the reflection judged it solved, when the provider
/// blocked it, or when it has twice said it has an answer with only one route
/// behind it. `retry` and `diversify` are absent because both continue.
///
/// This exists because a `route` port cannot leave the loop directly. Every arm
/// routes back to the head — the head owns the accumulator — so recognising a
/// finished run is the head's job, and `until` is where it is written.
#[must_use]
pub(super) fn terminal_condition() -> String {
    format!(
        "=.state.solved or .state.blocked >= {BLOCKED_THRESHOLD} \
         or .state.unverified >= {UNVERIFIED_THRESHOLD}"
    )
}

/// The accumulator's starting value.
///
/// Every counter the ladder reads, at zero. `since_reduction` starts at the
/// interval rather than at zero so the first cycle is already due — the goal is
/// decomposable from the problem statement alone, so waiting a full interval
/// buys nothing.
#[must_use]
pub(super) fn initial_state(problem: &str) -> Value {
    json!({
        "problem": problem,
        "attempts": 0,
        "unproductive": 0,
        "blocked": 0,
        "computational": 0,
        "unverified": 0,
        "restarts": 0,
        "solved": false,
        "since_reduction": super::solutions::REDUCTION_INTERVAL,
        "lesson": "",
        "fresh_context": "",
    })
}

/// How each pass folds into the accumulator.
///
/// Object form, so each key is resolved independently and merged over the
/// previous value — an update naming one key leaves the rest alone. Every
/// counter is written as an *assignment* computed from the previous value
/// rather than as an increment of it, because the fold is at-least-once: an
/// activation replayed after a resume applies the update twice, and an
/// idempotent update is immune where `+= 1` is not.
///
/// Consecutive counters reset to zero on a productive pass rather than
/// decaying, which is what "consecutive" means and what makes a run that makes
/// thin but genuine progress every time never reach diversify.
#[must_use]
pub(super) fn state_update() -> Value {
    // The `=` prefix belongs to the whole expression, once. Writing it here as
    // well as in the path produced `==.nodes…`, which is not an expression at
    // all: every binding resolved to null, the accumulator never moved, and the
    // ladder read its seed values on every pass. The run still completed and
    // still reported success — which is exactly the failure
    // `assert_no_null_bindings` exists to catch, and did.
    // Read off the parser, not the reflection: an `agent` node returns prose,
    // and the counters are a function of that prose *and* of what is on disk.
    // `parse_reflection` is where those meet, and its structured output lands
    // in `raw` because the tool invoker returns `{ text, raw }`.
    let reflect = ".nodes.parse.item.json";
    // `// .state.<key>` is load-bearing on two passes, not one. The loop head
    // runs *before* the body on the first activation, so there is no reflection
    // to fold and every field would otherwise be assigned null — wiping the
    // seed. And a reflection that omits a field would wipe that field for the
    // rest of the run. Falling back to the previous value makes the fold a
    // merge of what was reported over what was already known, which is what a
    // fold should be.
    let fold = |key: &str| format!("={reflect}.{key} // .state.{key}");
    json!({
        "attempts": fold("attempts"),
        "solved": fold("solved"),
        "unproductive": fold("unproductive"),
        "blocked": fold("blocked"),
        "computational": fold("computational"),
        "unverified": fold("unverified"),
        "restarts": fold("restarts"),
        "lesson": fold("lesson"),
        "fresh_context": fold("fresh_context"),
    })
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

/// An `agent` node that runs a registered role.
fn role(id: &str, agent_ref: &str, prompt: &str) -> Node {
    node(
        id,
        NodeKind::Agent,
        json!({ "agent_ref": agent_ref, "prompt": prompt }),
    )
}

/// Assembles the solution loop.
///
/// `agents` is the derived role registry — see `super::definitions` — so the
/// graph carries the same roles, tool grants, and budgets the run does.
#[must_use]
pub(super) fn solution_loop(
    problem: &str,
    agents: Vec<tinyflows::model::AgentDefinition>,
) -> WorkflowGraph {
    let mut nodes = vec![
        node("start", NodeKind::Trigger, Value::Null),
        node(
            LOOP_NODE,
            NodeKind::Loop,
            json!({
                "max_iterations": MAX_ATTEMPTS,
                // Reaching the ceiling is not a failure: the run reports the
                // furthest progress it reached, which is what `on_exceeded`
                // continuing to the `done` port expresses.
                "on_exceeded": "continue",
                // How the loop actually stops. Every terminal verdict routes
                // back to this head — there is nowhere else to route, since the
                // head owns the accumulator — so the head has to be the one
                // that recognises a finished run and leaves through `done`.
                // Checked against the post-fold accumulator, so the verdict
                // that just arrived is the one it reads.
                "until": terminal_condition(),
                "state": { "init": initial_state(problem), "update": state_update() },
            }),
        ),
        role(
            "attempt",
            "goals",
            "Take the next step on this problem, briefed by the last lesson.",
        ),
        role(
            "judge",
            "judge",
            "Score how the attempt just finished was conducted.",
        ),
        node(
            "judged",
            NodeKind::Switch,
            json!({ "expression": judge_ladder() }),
        ),
        role(
            "reflect",
            "reflection",
            "Is the answer right, and what did this attempt teach the next one?",
        ),
        node(
            "parse",
            NodeKind::ToolCall,
            json!({
                "slug": "parse_reflection",
                "args": {
                    "reflection": "=.item.text",
                    "state": format!("=.nodes.{LOOP_NODE}.state"),
                    "last_attempt": "=.nodes.attempt.item.text",
                    "problem": format!("=.nodes.{LOOP_NODE}.state.problem"),
                },
            }),
        ),
        node(
            "route",
            NodeKind::Switch,
            json!({ "expression": reflect_ladder() }),
        ),
        node("diversify_merge", NodeKind::Merge, Value::Null),
        node("report", NodeKind::Transform, Value::Null),
    ];
    nodes.extend(
        ARMS.iter()
            .map(|(id, agent)| role(id, agent, "Break the stall from your own angle.")),
    );

    let mut edges = vec![
        edge("start", "main", LOOP_NODE),
        edge(LOOP_NODE, "body", "attempt"),
        edge(LOOP_NODE, "done", "report"),
        edge("attempt", "main", "judge"),
        edge("judge", "main", "judged"),
        edge("judged", "reflect", "reflect"),
        // A restart discards the direction and re-enters the attempt without
        // reflecting, so it costs a judge call rather than a judge call plus a
        // reflection about to be thrown away.
        edge("judged", "restart", "attempt"),
        edge("reflect", "main", "parse"),
        edge("parse", "main", "route"),
        edge("route", "retry", LOOP_NODE),
        edge("route", "solved", LOOP_NODE),
        edge("route", "reported", LOOP_NODE),
        edge("route", "blocked", LOOP_NODE),
        edge("route", "diversify", "diversify_library"),
        edge("route", "diversify", "diversify_patterns"),
        edge("route", "diversify", "diversify_invention"),
        edge("diversify_merge", "main", LOOP_NODE),
    ];
    edges.extend(
        ARMS.iter()
            .map(|(id, _)| edge(id, "main", "diversify_merge")),
    );

    WorkflowGraph {
        name: "solution loop".into(),
        agents,
        nodes,
        edges,
        ..WorkflowGraph::default()
    }
}

#[cfg(test)]
#[path = "workflow_test.rs"]
mod test;
