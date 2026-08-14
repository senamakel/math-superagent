//! The solution loop as a `WorkflowGraph`.
//!
//! The attempt/judge/reflect loop, authored declaratively: a `loop` head
//! carrying the run's counters as its accumulator, `switch` nodes carrying the
//! routing ladder as jq, the diversify arms as concurrent successors converging
//! on a `merge`, and the goal's decomposition as a child workflow — see
//! [`super::workflow_goals`].
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

/// The body's single exit, and the only node the fold reads.
///
/// Every path back to the loop head goes through here: a retry, each terminal
/// verdict, and a diversify once its arms have merged. That is what makes the
/// fold correct rather than merely usually correct.
///
/// The engine's `nodes` map is cumulative — a node's output stays addressable
/// long after the pass that produced it — so a fold reading "the merge if it
/// ran, else the reflection" would keep reading a merge from three passes ago
/// for the rest of the run, silently reverting the state each time. A node
/// every pass runs is never stale.
///
/// The obvious alternative, routing the merge straight back into `attempt`, is
/// worse and was tried: it makes an inner cycle the loop head never sees, so
/// `max_iterations` cannot bound it and a run that keeps diversifying never
/// terminates.
pub(super) const PASS_NODE: &str = "pass";

/// The loop head, and the accumulator's address.
pub(super) const LOOP_NODE: &str = "solve";

/// The node that calls the goals child from inside the loop.
pub(super) const GOALS_NODE: &str = "goals";

/// The node that calls it once more, before the loop starts.
///
/// The reducer works backward from the problem statement, so its input is
/// present before anything has been attempted, and the arm is detached, so
/// asking here delays the graph by nothing. Waiting for a completed cycle would
/// mean that on a conjecture run — where an attempt/judge/reflect pass is the
/// better part of an hour — every role spent that hour working without a
/// statement of what would be enough.
///
/// It is the same child, through the same gate, so the first completed cycle
/// cannot open a second decomposition on top of this one.
pub(super) const SEED_GOALS_NODE: &str = "seed_goals";

/// The freshest state on the body's path, once the cycle's steps have run.
///
/// The accumulator is a pass behind while the body runs — the head folds at the
/// top of a pass — so anything downstream of the reflection reads the last step
/// that touched the state instead. `goal_apply` is that step: it is on every
/// path out of the reflection, and it is the last thing before the routing.
pub(super) const BODY_STATE: &str = "=.nodes.goal_apply.item.json";

/// The diversify arms, matching the state graph's.
pub(super) const ARMS: [(&str, &str); 3] = [
    ("diversify_library", "librarian"),
    ("diversify_patterns", "pattern_finder"),
    ("diversify_invention", "inventor"),
];

/// The routing ladder out of the reflection, as jq.
///
/// Reads `.item.json` — the reflection step's own output — rather than the
/// accumulator. The loop head folds at the *top* of a pass, so during pass N
/// the accumulator still holds pass N−1's state: a ladder reading it would
/// route this attempt on the last one's verdict, always one behind. A constant
/// mock hides that completely, since N−1 and N look identical.
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
        "=if .item.json.blocked >= {BLOCKED_THRESHOLD} then \"blocked\" \
         elif .item.json.solved or .item.json.attempts >= {MAX_ATTEMPTS} then \"solved\" \
         elif .item.json.unverified >= {UNVERIFIED_THRESHOLD} then \"reported\" \
         elif .item.json.unproductive >= {STUCK_THRESHOLD} then \"diversify\" \
         elif .item.json.computational >= {COMPUTATIONAL_THRESHOLD} then \"diversify\" \
         else \"retry\" end"
    )
}

/// The ladder out of the judge, as jq.
///
/// Reads the judge step's own output for the same reason [`reflect_ladder`]
/// does. It mattered most here while a restart re-entered `attempt` directly:
/// the accumulator was frozen for the whole restart cycle, so `restarts` never
/// appeared to grow, the cap never tripped, and a judge that kept saying restart
/// span to the graph's recursion limit. The restart now goes back through the
/// head, which fixes that independently — and reading the step's own output is
/// still right, because the head has not folded this pass yet.
///
/// Reads `judged`, which is what `SolutionState::to_accumulator` calls the
/// judge's verdict. It read `verdict` until a breakdown of the graph caught it:
/// nothing emits that field, so the comparison was `null == "restart"`, the
/// restart arm was unreachable, and a judge that wanted the run to start over
/// was silently overruled on every attempt. The parity harness did not catch it
/// because it feeds the ladder a scope it builds itself — proving the ladder
/// right while the graph fed it something else.
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
        "=if .item.json.attempts >= {MAX_ATTEMPTS} then \"reflect\" \
         elif .item.json.restarts >= {MAX_RESTARTS} then \"reflect\" \
         elif .item.json.judged == \"restart\" then \"restart\" \
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
        // The attempt report, carried so the run's final outcome can be built
        // from the accumulator alone. Without it the loop finishes holding
        // every counter and none of the prose those counters are about.
        "last_attempt": "",
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
    // The program form: one expression producing the whole next accumulator.
    // Each step returns the entire state, because a step may touch anything on
    // it — a lesson, a steer, the reduction cadence — and an update naming
    // fields would silently freeze whatever it forgot to name.
    //
    // `// .state` keeps the previous value when there is nothing to fold, which
    // is every activation the loop head makes before its body has run.
    json!(format!("=.nodes.{PASS_NODE}.item.json // .nodes.{LOOP_NODE}.state"))
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

/// A node that runs one of the loop's steps.
///
/// A `tool_call` rather than an `agent` node, and the difference is the whole
/// argument in `super::loop_steps`: a bare `agent_ref` would run the role and
/// lose the mailbox drain that carries a directive, the salvage that rescues a
/// timed-out attempt, and the arms opened beside the loop. The engine owns the
/// routing — which is what a declarative loop is for — and the steps stay the
/// Rust written against live runs.
fn step(id: &str) -> Node {
    step_with(id, &format!("=.nodes.{LOOP_NODE}.state"), &Value::Null)
}

/// A step reading a named state, with extra arguments merged in.
///
/// Two steps need one or the other. `diversify_merge` reads the arms' own
/// outputs rather than the accumulator, because the accumulator predates them;
/// `goal_apply` reads the reflection's output, because the accumulator is a
/// pass behind by the time the body runs.
fn step_with(id: &str, state: &str, extra: &Value) -> Node {
    let mut args = json!({ "step": id, "state": state });
    if let (Some(args), Some(extra)) = (args.as_object_mut(), extra.as_object()) {
        for (key, value) in extra {
            args.insert(key.clone(), value.clone());
        }
    }
    node(
        id,
        NodeKind::ToolCall,
        json!({ "slug": super::loop_steps::TOOL, "args": args }),
    )
}

/// Where the merge reads each arm's findings from, as jq.
///
/// The arms are concurrent nodes and each returns a whole state, so their
/// findings exist only in their own outputs. This node used to read the loop's
/// accumulator like every other step, which meant a diversify spent three child
/// agent runs and merged none of what they found.
#[must_use]
fn arm_outputs() -> String {
    let arms: Vec<String> = ARMS
        .iter()
        .map(|(id, _)| format!(".nodes.{id}.item.json"))
        .collect();
    format!("=[{}]", arms.join(", "))
}

/// A node that runs the goals child over `state`.
///
/// Both callers build it here rather than each writing the config out, so the
/// two cannot disagree about which child they are calling or how it is seeded.
fn goals_call(id: &str, state: &Value) -> Node {
    node(
        id,
        NodeKind::SubWorkflow,
        json!({
            "workflow": serde_json::to_value(super::workflow_goals::goals_workflow())
                .unwrap_or(Value::Null),
            "inputs": { super::workflow_goals::STATE_INPUT: state },
        }),
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
        // The only step that reads the accumulator, because it is the only one
        // that runs at the top of a pass, where the accumulator is what the last
        // pass folded. Every step after it reads the step before it.
        step("attempt"),
        step_with("judge", "=.nodes.attempt.item.json", &Value::Null),
        node(
            "judged",
            NodeKind::Switch,
            json!({ "expression": judge_ladder() }),
        ),
        step_with("reflect", "=.nodes.judge.item.json", &Value::Null),
        // The other question nothing in the loop asks by itself: not what else
        // could get the run there, but what would be enough. A child workflow
        // rather than three more nodes here, because the cadence and the gate
        // are its own policy — see `super::workflow_goals`, which also says why
        // calling it costs the loop nothing.
        goals_call(GOALS_NODE, &json!("=.nodes.reflect.item.json")),
        // The same child, before the first attempt. See [`SEED_GOALS_NODE`]:
        // seeded with the loop's own opening state, which starts the cadence at
        // the interval so this call is already due.
        goals_call(SEED_GOALS_NODE, &initial_state(problem)),
        step_with(
            "goal_apply",
            "=.nodes.reflect.item.json",
            // `item` rather than `item.json`: a `sub_workflow` emits the child's
            // run state unwrapped, where a `tool_call` emits the
            // `{ json, text, raw }` envelope every other step here is addressed
            // through.
            &json!({ super::loop_steps::DECISION_ARG: format!("=.nodes.{GOALS_NODE}.item") }),
        ),
        node(
            "route",
            NodeKind::Switch,
            json!({ "expression": reflect_ladder() }),
        ),
        step_with(
            "diversify_merge",
            BODY_STATE,
            &json!({ super::loop_steps::ARMS_ARG: arm_outputs() }),
        ),
        node(PASS_NODE, NodeKind::Transform, Value::Null),
        node("report", NodeKind::Transform, Value::Null),
    ];
    nodes.extend(
        ARMS.iter()
            .map(|(id, _)| step_with(id, BODY_STATE, &Value::Null)),
    );

    let mut edges = vec![
        edge("start", "main", SEED_GOALS_NODE),
        edge(SEED_GOALS_NODE, "main", LOOP_NODE),
        edge(LOOP_NODE, "body", "attempt"),
        edge(LOOP_NODE, "done", "report"),
        edge("attempt", "main", "judge"),
        edge("judge", "main", "judged"),
        edge("judged", "reflect", "reflect"),
        // A restart skips the reflection, so it costs a judge call rather than a
        // judge call plus a reflection about to be thrown away — but it goes
        // back through the head like every other path rather than straight into
        // another attempt.
        //
        // Re-entering `attempt` directly was tried and is wrong twice over. The
        // accumulator is only folded at the head, so the second attempt would
        // read the state from *before* the first one and the judge's own
        // `restarts` increment would be undone — a judge that keeps asking to
        // restart then spins until the graph's recursion limit, because the cap
        // that is supposed to stop it is reset every time round. And it makes an
        // inner cycle the head never sees, so `max_iterations` cannot bound it
        // either. Through the head, a restart costs an iteration, which is
        // right: a restart *is* another attempt.
        edge("judged", "restart", PASS_NODE),
        edge("reflect", "main", GOALS_NODE),
        edge(GOALS_NODE, "main", "goal_apply"),
        edge("goal_apply", "main", "route"),
        edge("route", "retry", PASS_NODE),
        edge("route", "solved", PASS_NODE),
        edge("route", "reported", PASS_NODE),
        edge("route", "blocked", PASS_NODE),
        edge(PASS_NODE, "main", LOOP_NODE),
        edge("route", "diversify", "diversify_library"),
        edge("route", "diversify", "diversify_patterns"),
        edge("route", "diversify", "diversify_invention"),
        // Through the pass node like every other path, not straight back to
        // the head. Two things were tried first and both were wrong: returning
        // to the head directly gives the fold two nodes to read and it
        // eventually reads the stale one, and returning into `attempt` makes an
        // inner cycle the head never sees, so `max_iterations` cannot bound a
        // run that keeps diversifying.
        edge("diversify_merge", "main", PASS_NODE),
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
