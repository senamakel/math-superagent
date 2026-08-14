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

use super::schools::Thresholds;

/// The argument every step node carries its school's bounds in.
///
/// The graph is where they travel, because the graph is already per-school:
/// [`solution_loop_for`] builds one for each, and a step that had to be told
/// which school it belonged to some other way would be a second answer to a
/// question the document already answers. See [`thresholds_json`] for the shape
/// and [`thresholds_from`] for the read.
pub(super) const THRESHOLDS_ARG: &str = "thresholds";

/// The evaluation arms, and the barrier they converge on.
///
/// Six questions about one attempt, asked at once. They fan out from the
/// attempt because none of them reads another's output — each reads the same
/// report — so a pass costs the slowest of them rather than the sum, which is
/// what a serial chain of the same five cost.
///
/// The backward arm is absent from this list because it is two nodes rather
/// than one: the goals child decides whether this cycle decomposes, and
/// `goal_apply` folds what it decided back onto the loop's own path. It is the
/// branch's last node that converges, so `goal_apply` joins the list below.
pub(super) const EVAL_ARMS: [&str; 4] = [
    "reflect",
    "eval_patterns",
    "eval_invention",
    "eval_refutation",
];

/// The node that stops the work beside the run, once the run is over.
///
/// The teams were always cancelled — at `orchestrator_runtime`, after the whole
/// workflow returns. The judge is inside that workflow, so "after the workflow"
/// is after the judge, and everything the standing teams do between the loop
/// ending and the judge finishing is work on a question already answered.
///
/// A live `./euler 351` measured what that costs. The loop recorded `verdict
/// solved` at 29 minutes, on an answer two independent programs had agreed on
/// at 15. Thirty further sub-agents were then spawned across the next 62
/// minutes — librarian, scholar, `pattern_finder`, on their own cadence, none of
/// them able to change an outcome already reached — and the judge did not start
/// until minute 92. That is 85% of a 96-minute run, and roughly $32 of $35,
/// spent after the problem was solved.
///
/// A node of its own rather than a line inside the literature check, for the
/// same reason [`LIBRARY_ARM`] is a node: ending the work beside a run is a
/// visible act at a place a checkpoint can land, not a side effect of whichever
/// step happened to be holding the handles.
pub(super) const STAND_DOWN: &str = "stand_down";

/// The literature check that runs after the loop, and only on a solve.
///
/// A node of its own rather than a branch of the final judge, because it asks a
/// question about the *world* rather than about the run: is this already known,
/// and is the argument short enough to be suspicious? Every other sweep in this
/// graph runs while the run is stuck and looks for a way forward. This one runs
/// when the run thinks it is finished and looks for a reason to doubt it.
pub(super) const NOVELTY_NODE: &str = "novelty";

/// The node that scores the run, once, after the loop has finished.
///
/// Not an evaluation arm, and the difference is what the judge is *for*. The
/// reflection asks whether the answer is right and can end the run; the judge
/// asks whether the work was conducted in a way to be inherited. Asked after
/// every attempt that was a per-pass cost paid for a per-pass steer — and the
/// steer only reached anything because a further attempt followed it.
///
/// Asked once at the end it is an assessment of the whole run, which is the
/// question a reader of the outcome actually has. Mid-flight judgement has not
/// been lost: the standing `review` team spawns a judge against the workspace as
/// it stands and posts the verdict into the mailbox the next attempt drains, on
/// its own cadence rather than on every pass.
pub(super) const FINAL_JUDGE: &str = "judge";

/// The arm that returns before its work does.
///
/// A node like the others as far as the graph is concerned, and that is the
/// point of giving it one: the literature sweep is started here, visibly, at a
/// place a checkpoint can land, rather than as a side effect hidden inside
/// whichever step happened to be holding the subagent manager.
pub(super) const LIBRARY_ARM: &str = "eval_library";

/// Where the evaluation arms converge.
pub(super) const EVAL_MERGE: &str = "eval_merge";

/// The node that folds the goals child's decision back onto the loop's path.
pub(super) const GOAL_APPLY: &str = "goal_apply";

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

/// The accumulator field carrying whether the run has spent its wall clock.
///
/// Named once because three places have to agree on it: `initial_state` seeds
/// it, `eval_merge` stamps it at the end of every pass, and
/// [`terminal_condition`] ends the run on it. A literal in each is three
/// answers to the same question, and two of them are jq, where a typo is not a
/// compile error but a condition that is silently never true.
pub(super) const EXPIRED_FIELD: &str = "expired";

/// The loop head, and the accumulator's address.
pub(super) const LOOP_NODE: &str = "solve";

/// The node that calls the goals child from inside the loop.
pub(super) const GOALS_NODE: &str = "goals";

/// The node that calls it once more, before the loop starts.
///
/// The reducer works backward from the problem statement, so its input is
/// present before anything has been attempted. Asking here means every role in
/// the first attempt already has a statement of what would be enough — on a
/// conjecture run, where a cycle is the better part of an hour, waiting for a
/// completed one means that whole hour is spent without it.
///
/// It is the same child, through the same gate, so the first completed cycle
/// cannot open a second decomposition on top of this one.
pub(super) const SEED_GOALS_NODE: &str = "seed_goals";

/// The node that folds what the seed decomposition found into the loop's
/// opening state.
///
/// The seed used to be a call whose result nothing read, which was harmless
/// while the reduction was detached and wrote only to disk. It is awaited now,
/// so its skeleton is a thing the run has and would be thrown away without
/// this.
pub(super) const SEED_APPLY_NODE: &str = "seed_apply";

/// The node that runs stage one.
pub(super) const RESEARCH_NODE: &str = "research";

/// The node that folds stage one's findings into the loop's opening state.
pub(super) const SEED_CONTEXT_NODE: &str = "seed_context";

/// The freshest state on the body's path, once the arms have merged.
///
/// The accumulator is a pass behind while the body runs — the head folds at the
/// top of a pass — so anything downstream of the evaluation reads the merge
/// instead. It is the only node the routing and the escalation both follow.
pub(super) const BODY_STATE: &str = "=.nodes.eval_merge.item.json";

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
///
/// The numbers are the school's, not the constants', for the same reason the
/// Rust reads them off a parameter: several schools run at once and each brings
/// its own. The control school's are the constants, so its ladder is character
/// for character the one this generated before schools existed.
#[must_use]
pub(super) fn reflect_ladder(thresholds: &Thresholds) -> String {
    let Thresholds {
        max_attempts,
        stuck,
        blocked,
        computational,
        unverified,
        ..
    } = *thresholds;
    format!(
        "=if .item.json.blocked >= {blocked} then \"blocked\" \
         elif .item.json.solved or .item.json.attempts >= {max_attempts} then \"solved\" \
         elif .item.json.unverified >= {unverified} then \"reported\" \
         elif .item.json.unproductive >= {stuck} then \"diversify\" \
         elif .item.json.computational >= {computational} then \"diversify\" \
         else \"retry\" end"
    )
}

/// One school's bounds, as the graph carries them.
///
/// Written out field by field rather than derived, because [`Thresholds`] is
/// not a wire type and a `Debug` or a serde rendering would change the day
/// somebody renamed a field — silently, into a step that reads its default and
/// runs the control school's numbers under another school's name.
/// [`thresholds_from`] is the other half and is kept beside it.
#[must_use]
pub(super) fn thresholds_json(thresholds: &Thresholds) -> Value {
    json!({
        "max_attempts": thresholds.max_attempts,
        "stuck": thresholds.stuck,
        "blocked": thresholds.blocked,
        "computational": thresholds.computational,
        "unverified": thresholds.unverified,
        "max_restarts": thresholds.max_restarts,
        "reduction_interval": thresholds.reduction_interval,
    })
}

/// Reads a step's bounds back out of its arguments.
///
/// A missing or unreadable field falls back to the control school's value, on
/// the rule every override in this runtime follows: a malformed value keeps the
/// default rather than silently removing a bound.
#[must_use]
pub(super) fn thresholds_from(args: &Value) -> Thresholds {
    let carried = args.get(THRESHOLDS_ARG);
    let chisel = Thresholds::chisel();
    let read = |key: &str, fallback: usize| {
        carried
            .and_then(|carried| carried.get(key))
            .and_then(Value::as_u64)
            .and_then(|value| usize::try_from(value).ok())
            .unwrap_or(fallback)
    };
    Thresholds {
        max_attempts: read("max_attempts", chisel.max_attempts),
        stuck: read("stuck", chisel.stuck),
        blocked: read("blocked", chisel.blocked),
        computational: read("computational", chisel.computational),
        unverified: read("unverified", chisel.unverified),
        max_restarts: read("max_restarts", chisel.max_restarts),
        reduction_interval: read("reduction_interval", chisel.reduction_interval),
    }
}

/// When the loop is finished, as jq.
///
/// The terminal arms of [`reflect_ladder`], and deliberately the same numbers: a
/// run stops when the reflection judged it solved, when the provider blocked it,
/// when it has twice said it has an answer with only one route behind it, or
/// when it has spent its attempts. `retry` and `diversify` are absent because
/// both continue.
///
/// This exists because a `route` port cannot leave the loop directly. Every arm
/// routes back to the head — the head owns the accumulator — so recognising a
/// finished run is the head's job, and `until` is where it is written.
///
/// The attempt ceiling is here as well as in the ladder, and that is the fix for
/// a run that would otherwise never stop. The ladder routes `solved` at the
/// ceiling, but it does not *set* `solved`, so the head's `until` stayed false
/// and the only thing left to end the run was the engine's `max_iterations` —
/// which this graph was observed not to trip. A loop whose termination rests on
/// a counter the graph cannot see is a loop nobody can reason about; the ceiling
/// belongs in the condition that ends it, beside the other three, where the
/// ladder already agrees with it.
///
/// `expired` is the fifth arm and the only one that is not a count. The other
/// four all assume the run is still producing passes; a loop that has stopped
/// producing them stops approaching every one of them at once, which is exactly
/// how a live run sat for half an hour after a rejected verdict without
/// advancing `attempts` by one. See [`solutions::run_ceiling`] for what stamps
/// it and why the per-agent budget could not.
///
/// [`solutions::run_ceiling`]: super::solutions::run_ceiling
#[must_use]
pub(super) fn terminal_condition(thresholds: &Thresholds) -> String {
    let Thresholds {
        max_attempts,
        blocked,
        unverified,
        ..
    } = *thresholds;
    format!(
        "=.state.solved or .state.{EXPIRED_FIELD} or .state.attempts >= {max_attempts} \
         or .state.blocked >= {blocked} \
         or .state.unverified >= {unverified}"
    )
}

/// The accumulator's starting value.
///
/// Every counter the ladder reads, at zero. `since_reduction` starts at the
/// interval rather than at zero so the first cycle is already due — the goal is
/// decomposable from the problem statement alone, so waiting a full interval
/// buys nothing.
#[must_use]
pub(super) fn initial_state(problem: &str, thresholds: &Thresholds) -> Value {
    let mut state = json!({
        "problem": problem,
        "attempts": 0,
        "unproductive": 0,
        "blocked": 0,
        "computational": 0,
        "unverified": 0,
        "restarts": 0,
        "solved": false,
        "since_reduction": thresholds.reduction_interval,
        "lesson": "",
        "fresh_context": "",
        // The attempt report, carried so the run's final outcome can be built
        // from the accumulator alone. Without it the loop finishes holding
        // every counter and none of the prose those counters are about.
        "last_attempt": "",
    });
    // Seeded false rather than left absent so the condition that ends the run
    // has something to read before the first pass stamps it. It is not a field
    // of `SolutionState`: the ceiling is a fact about the run's clock rather
    // than about its mathematics, so the one place that knows the clock —
    // `eval_merge` — is the only place that writes it.
    if let Some(object) = state.as_object_mut() {
        object.insert(EXPIRED_FIELD.to_string(), Value::Bool(false));
    }
    state
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

/// A step under its own node id, reading a named state, with extras merged in.
///
/// The id and the step name are separate because two nodes now run the same
/// step: `goal_apply` folds the goals child's decision both before the loop and
/// inside it, and a graph cannot have two nodes called the same thing.
fn step_as(id: &str, name: &str, state: &Value, extra: &Value) -> Node {
    let mut args = json!({ "step": name, "state": state });
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

/// A step reading a named state, with extra arguments merged in.
fn step_with(id: &str, state: &str, extra: &Value) -> Node {
    step_as(id, id, &json!(state), extra)
}

/// Writes the school's bounds into a step node's arguments.
///
/// Does nothing to any other kind of node: a `switch` carries its bounds inside
/// the jq it already holds, and a `sub_workflow` carries whatever child it was
/// built with.
fn carry_thresholds(node: &mut Node, thresholds: &Thresholds) {
    if !matches!(node.kind, NodeKind::ToolCall) {
        return;
    }
    if let Some(args) = node
        .config
        .get_mut("args")
        .and_then(serde_json::Value::as_object_mut)
    {
        args.insert(
            THRESHOLDS_ARG.to_string(),
            thresholds_json(thresholds),
        );
    }
}

/// What the attempt's report is addressed as.
///
/// Every evaluation arm reads this and nothing else. They are concurrent, so an
/// arm reading another arm's output would be reading a node that may not have
/// run — and an arm reading the loop's accumulator would be reading the
/// *previous* pass, because the head folds at the top of a pass.
const ATTEMPT_OUTPUT: &str = "=.nodes.attempt.item.json";

/// Where the merge reads each arm's whole state from, as jq.
///
/// Derived from the arm list rather than written out, so an arm added to the
/// graph is an arm the merge folds. The list it is derived from is the same one
/// the edges are built from, which is what makes "every arm converges" and
/// "every arm is folded" one fact instead of two.
#[must_use]
fn arm_outputs() -> String {
    let arms: Vec<String> = eval_arm_ids()
        .into_iter()
        .map(|id| format!(".nodes.{id}.item.json"))
        .collect();
    format!("=[{}]", arms.join(", "))
}

/// Every node that converges on the merge.
///
/// The four questions about the attempt, the detached sweep that answers none
/// of them but must still be waited *for* — it returns immediately, so waiting
/// costs nothing and skipping it would let the pass race past the node that
/// starts the sweep — and the backward branch's last node.
fn eval_arm_ids() -> Vec<&'static str> {
    let mut ids = EVAL_ARMS.to_vec();
    ids.push(LIBRARY_ARM);
    ids.push(GOAL_APPLY);
    ids
}

/// A node that runs the goals child over `state`.
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

/// A node that runs the research child over `state`.
fn research_call(id: &str, state: &Value) -> Node {
    node(
        id,
        NodeKind::SubWorkflow,
        json!({
            "workflow": serde_json::to_value(super::workflow_research::research_workflow())
                .unwrap_or(Value::Null),
            "inputs": { super::workflow_research::STATE_INPUT: state },
        }),
    )
}

/// Assembles the solution loop.
///
/// Three stages. Establish what the run has and go looking for what it does not
/// (`research`, once); attempt (`solve`'s body); evaluate the attempt from five
/// directions at once and route on what they found together. The first and the
/// third are child workflows and a fan-out respectively, which is the whole
/// difference from the chain this replaced — the same questions in a line,
/// three of them hidden inside the reflection's own body.
///
/// `agents` is the derived role registry — see `super::definitions` — so the
/// graph carries the same roles, tool grants, and budgets the run does.
#[must_use]
/// The nodes that run once, before any attempt exists.
///
/// Split out so [`solution_loop`] reads as the loop it is named after. They
/// belong together for a reason beyond length: every one of them is a
/// *precondition* — what the workspace already holds, what the literature adds,
/// and what the goal decomposes into — and none of them ever runs again.
fn stage_one(opening: &Value) -> Vec<Node> {
    vec![
        node("start", NodeKind::Trigger, Value::Null),
        research_call(RESEARCH_NODE, opening),
        step_as(
            SEED_CONTEXT_NODE,
            "seed_context",
            opening,
            &json!({
                super::loop_steps::DECISION_ARG: format!("=.nodes.{RESEARCH_NODE}.item"),
            }),
        ),
        // The goal decomposed before the first attempt rather than after it.
        // See [`SEED_GOALS_NODE`]: the reducer works backward from the problem
        // statement, so its input exists before anything has been attempted.
        goals_call(
            SEED_GOALS_NODE,
            &json!(format!("=.nodes.{SEED_CONTEXT_NODE}.item.json")),
        ),
        step_as(
            SEED_APPLY_NODE,
            "goal_apply",
            &json!(format!("=.nodes.{SEED_CONTEXT_NODE}.item.json")),
            &json!({ super::loop_steps::DECISION_ARG: format!("=.nodes.{SEED_GOALS_NODE}.item") }),
        ),
    ]
}

pub(super) fn solution_loop(
    problem: &str,
    agents: Vec<tinyflows::model::AgentDefinition>,
) -> WorkflowGraph {
    solution_loop_for(problem, agents, &Thresholds::chisel())
}

/// The same loop, under one school's bounds.
///
/// Every school runs this graph — the schools are a method policy, a set of
/// prompt overlays and a [`Thresholds`], not a second loop — so what differs
/// between two of them is the numbers in the ladder, in the condition that ends
/// the run, and in the arguments each step carries.
pub(super) fn solution_loop_for(
    problem: &str,
    agents: Vec<tinyflows::model::AgentDefinition>,
    thresholds: &Thresholds,
) -> WorkflowGraph {
    let opening = initial_state(problem, thresholds);
    let seeded = format!("=.nodes.{SEED_APPLY_NODE}.item.json");
    let mut nodes = stage_one(&opening);
    nodes.extend([
        node(
            LOOP_NODE,
            NodeKind::Loop,
            json!({
                "max_iterations": thresholds.max_attempts,
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
                "until": terminal_condition(thresholds),
                // Seeded from stage one rather than from the literal, so the
                // first attempt starts from what the run established rather
                // than from the statement and eleven zeroes.
                "state": { "init": seeded, "update": state_update() },
            }),
        ),
        // Stage two. The only step that reads the accumulator, because it is the
        // only one that runs at the top of a pass, where the accumulator is what
        // the last pass folded.
        step("attempt"),
        // Stage three, and the reason this graph changed shape. Each of these
        // reads the attempt and nothing else.
        step_with("reflect", ATTEMPT_OUTPUT, &Value::Null),
        step_with("eval_patterns", ATTEMPT_OUTPUT, &Value::Null),
        step_with("eval_invention", ATTEMPT_OUTPUT, &Value::Null),
        // The one arm that is not an assessment of the attempt. The other four
        // ask how it went; this one asks whether the thing it is trying to
        // prove is true at all, which is a question nothing else in the loop
        // ever puts. It belongs in the fan-out rather than beside it because it
        // reads the same attempt, reads no other arm, and must not delay one.
        step_with("eval_refutation", ATTEMPT_OUTPUT, &Value::Null),
        step_with(LIBRARY_ARM, ATTEMPT_OUTPUT, &Value::Null),
        goals_call(GOALS_NODE, &json!(ATTEMPT_OUTPUT)),
        step_as(
            GOAL_APPLY,
            "goal_apply",
            &json!(ATTEMPT_OUTPUT),
            // `item` rather than `item.json`: a `sub_workflow` emits the child's
            // run state unwrapped, where a `tool_call` emits the
            // `{ json, text, raw }` envelope every other step here is addressed
            // through.
            &json!({ super::loop_steps::DECISION_ARG: format!("=.nodes.{GOALS_NODE}.item") }),
        ),
        step_as(
            EVAL_MERGE,
            "eval_merge",
            &json!(ATTEMPT_OUTPUT),
            &json!({ super::loop_steps::ARMS_ARG: arm_outputs() }),
        ),
        node(
            "route",
            NodeKind::Switch,
            json!({ "expression": reflect_ladder(thresholds) }),
        ),
        // The escalation. One node rather than three, because the two arms that
        // used to run only here now run on every pass; what is left that is
        // genuinely an escalation is blocking on the literature the run has been
        // gathering in the background rather than attempting without it.
        step_with("diversify_library", BODY_STATE, &Value::Null),
        step_with(
            STAND_DOWN,
            &format!("=.nodes.{LOOP_NODE}.state"),
            &Value::Null,
        ),
        // The loop's state rather than `stand_down`'s, even though
        // `stand_down` runs first. The edge is what orders them; the state is
        // the loop's, and routing it through a node whose whole job is a side
        // effect would say it had transformed something it did not.
        step_with(
            NOVELTY_NODE,
            &format!("=.nodes.{LOOP_NODE}.state"),
            &Value::Null,
        ),
        step_as(
            FINAL_JUDGE,
            "judge",
            &json!(format!("=.nodes.{LOOP_NODE}.state")),
            &Value::Null,
        ),
        node(PASS_NODE, NodeKind::Transform, Value::Null),
        node("report", NodeKind::Transform, Value::Null),
    ]);

    let mut edges = vec![
        edge("start", "main", RESEARCH_NODE),
        edge(RESEARCH_NODE, "main", SEED_CONTEXT_NODE),
        edge(SEED_CONTEXT_NODE, "main", SEED_GOALS_NODE),
        edge(SEED_GOALS_NODE, "main", SEED_APPLY_NODE),
        edge(SEED_APPLY_NODE, "main", LOOP_NODE),
        edge(LOOP_NODE, "body", "attempt"),
        // The run's last act, on the way out. It reads the accumulator because
        // by here that is the finished run: the head has folded every pass.
        // The literature check first, then the judge, then the report. In that
        // order because the judge is scoring the whole run and "this was
        // already published in 1974" is the single most important thing it
        // could be told before it does.
        edge(LOOP_NODE, "done", STAND_DOWN),
        edge(STAND_DOWN, "main", NOVELTY_NODE),
        edge(NOVELTY_NODE, "main", FINAL_JUDGE),
        edge(FINAL_JUDGE, "main", "report"),
        // The backward branch is two nodes, so it fans out from the attempt like
        // the others and converges from its own last node.
        edge("attempt", "main", GOALS_NODE),
        edge(GOALS_NODE, "main", GOAL_APPLY),
        edge(EVAL_MERGE, "main", "route"),
        edge("route", "retry", PASS_NODE),
        edge("route", "solved", PASS_NODE),
        edge("route", "reported", PASS_NODE),
        edge("route", "blocked", PASS_NODE),
        edge("route", "diversify", "diversify_library"),
        edge("diversify_library", "main", PASS_NODE),
        edge(PASS_NODE, "main", LOOP_NODE),
    ];
    // Every step, rather than the two that read a bound today. A list of which
    // steps need the school's numbers would be a list to keep in step with the
    // steps themselves, and the failure it produces is the quiet one: a step
    // that silently falls back to the control school's bounds while running
    // under another school's name.
    for node in &mut nodes {
        carry_thresholds(node, thresholds);
    }
    // One fan-out and one barrier, both built from the same list, so an arm
    // cannot be started without being waited for or waited for without being
    // started.
    for id in eval_arm_ids() {
        if id != GOAL_APPLY {
            edges.push(edge("attempt", "main", id));
        }
        edges.push(edge(id, "main", EVAL_MERGE));
    }

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
