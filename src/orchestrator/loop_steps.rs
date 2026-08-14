//! The loop's steps, as one tool the workflow graph calls.
//!
//! A workflow node that simply named a role would run the role and lose
//! everything around it. The state graph's node bodies are not thin wrappers on
//! a delegation — they are where the mailboxes are drained, the prompt is
//! assembled from what the run has learned, a timed-out attempt is salvaged,
//! the pattern arm is opened beside the reflection, and the goal is decomposed
//! on its own cadence. None of that is expressible as an `agent_ref`, and none
//! of it is optional:
//!
//! - **Directives.** `./steer` is the whole external control surface, and a
//!   directive reaches a run by being drained from a mailbox in `attempt_step`.
//!   A loop that skipped that would accept direction and act on none of it.
//! - **Salvage.** The ordinary way an attempt ends is its run cap killing it,
//!   which destroys its report and leaves every file it wrote. The salvage path
//!   is what turns that into a usable attempt instead of a blank one.
//! - **The arms beside the loop.** The pattern agent runs after every attempt,
//!   because the exploitable regularity is usually visible in the first terms a
//!   run computes and waiting for the loop to get stuck means spending the
//!   budget the pattern would have saved.
//!
//! So the engine owns the **routing** — which is what a declarative loop is
//! actually for, and what an outside agent edits — and the steps stay the Rust
//! that was written against a hundred live runs. Splitting it the other way
//! would have meant reimplementing all of the above in JSON.
//!
//! # The state crosses as JSON and comes back whole
//!
//! Each call rebuilds a [`SolutionState`] from the accumulator, runs the step,
//! and returns the whole state. The loop head then replaces its accumulator
//! with it. That keeps the head the sole writer — the property the fan-out
//! depends on — while letting a step mutate whatever it needs to.

use std::path::PathBuf;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::trace::RunTracer;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

use super::async_subagents::AsyncSubagentManager;
use super::solutions::{
    Beside, Mailboxes, SolutionState, attempt_step, diversify_invention_arm, diversify_library_arm,
    diversify_merge, diversify_pattern_arm, judge_step, novelty_arm, reflect_step, refutation_arm,
};
use super::vector::VectorStore;

/// The steps a workflow node may ask for.
///
/// A closed set, matched by name. An unknown step is an error rather than a
/// no-op: a workflow naming a step that does not exist would otherwise run,
/// change nothing, and route on a state nobody advanced.
const STEPS: [&str; 15] = [
    "init_context",
    "seed_context",
    "attempt",
    "judge",
    "reflect",
    "eval_patterns",
    "eval_invention",
    "eval_refutation",
    "eval_library",
    "eval_merge",
    "goal_gate",
    "goal_apply",
    "diversify_library",
    "novelty",
    "stand_down",
];

/// The slug a workflow node names this tool by.
///
/// Here rather than spelled at each call site, so a graph and this tool cannot
/// disagree about it — a `tool_call` naming a slug the registry does not hold
/// fails the node, and a graph is not compiled against these strings.
pub(super) const TOOL: &str = "run_loop_step";

/// The argument the merge reads the arms' findings from.
pub(super) const ARMS_ARG: &str = "arms";

/// The argument `goal_apply` reads the goals child's run state from.
pub(super) const DECISION_ARG: &str = "decision";

/// Everything one step needs from the run.
pub(super) struct LoopSteps {
    subagents: AsyncSubagentManager,
    tracer: Option<Arc<RunTracer>>,
    workspace: Option<PathBuf>,
    memory: VectorStore,
    beside: Beside,
    mailboxes: Mailboxes,
    /// When this run started, for the loop's own wall-clock ceiling.
    ///
    /// Taken at construction rather than at the first pass, because the tool is
    /// built immediately before the engine runs and stage one is inside that —
    /// a clock started at the first `eval_merge` would not count the research
    /// child, which on a live run was eight minutes of the budget it is meant
    /// to bound.
    started: std::time::Instant,
}

impl std::fmt::Debug for LoopSteps {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter.debug_struct("LoopSteps").finish_non_exhaustive()
    }
}

impl LoopSteps {
    /// Builds the tool over one run's context.
    pub(super) fn new(
        subagents: AsyncSubagentManager,
        tracer: Option<Arc<RunTracer>>,
        workspace: Option<PathBuf>,
        memory: VectorStore,
        beside: Beside,
        mailboxes: Mailboxes,
    ) -> Self {
        Self {
            subagents,
            tracer,
            workspace,
            memory,
            beside,
            mailboxes,
            started: std::time::Instant::now(),
        }
    }

    /// Whether this run has spent its wall-clock ceiling.
    fn expired(&self) -> bool {
        self.started.elapsed() >= super::solutions::run_ceiling()
    }

    /// Runs one step against `state`, and returns the accumulator it produced.
    ///
    /// Returning JSON rather than a [`SolutionState`] because one step has
    /// something to say that is not part of the state: `goal_gate` reports
    /// whether it opened a decomposition, which the loop needs in order to
    /// reset the cadence and which has no business becoming a permanent field.
    /// Opens a decomposition if the gate admits one, and says whether it did.
    async fn open_decomposition(&self, state: &SolutionState) -> Value {
        let (opened, _) = super::solutions::reduce_arm(
            &self.subagents,
            self.tracer.as_ref(),
            self.workspace.as_deref(),
            &self.beside.reduction,
            state,
        )
        .await;
        let mut carried = state.to_accumulator();
        if let Some(object) = carried.as_object_mut() {
            object.insert(
                super::workflow_goals::OPENED_FIELD.to_string(),
                Value::Bool(opened),
            );
        }
        carried
    }

    /// Folds the evaluation arms into one state, and stamps the clock.
    fn merge_evaluation(&self, state: &SolutionState, args: &Value) -> Value {
        let arms: Vec<Value> = args
            .get(ARMS_ARG)
            .and_then(Value::as_array)
            .cloned()
            .unwrap_or_default();
        let merged = super::solutions::fold_evaluation(&state.to_accumulator(), &arms);
        let merged = SolutionState::from_accumulator("", &merged);
        let mut merged = super::solutions::evaluation_merge(merged);
        // Stamped after the fold rather than on an arm. Every pass ends here,
        // so this is the last thing written before the head tests `until` — and
        // an arm that stamped it would send a clock reading through
        // `fold_evaluation`, which folds numbers as deltas from the base and
        // would turn one into arithmetic on timestamps.
        merged.expired = self.expired();
        merged.to_accumulator()
    }

    async fn run(&self, step: &str, state: SolutionState, args: &Value) -> Result<Value> {
        let tracer = self.tracer.as_ref();
        // The school's bounds, read off the node's own arguments rather than
        // held on this tool. One `LoopSteps` serves every school's graph —
        // there is one subagent manager, one budget pool and one workspace —
        // so which school a step belongs to is a property of the step, and the
        // graph is where it is already written down. A node built without them
        // reads the control school's, which is what every graph did before
        // schools existed.
        let thresholds = super::workflow::thresholds_from(args);
        let workspace = self.workspace.as_deref();
        // Two steps say something that is not part of the state, so they are
        // answered before the match and their extra field is folded into the
        // returned object afterwards.
        if step == "goal_gate" {
            return Ok(self.open_decomposition(&state).await);
        }
        // The barrier the evaluation arms converge on. It reads whole states
        // rather than one, so it cannot go through the match below, which is
        // written for a step that takes the state and returns it.
        if step == "eval_merge" {
            return Ok(self.merge_evaluation(&state, args));
        }
        // Stage one crossing back into the loop. Like `goal_apply` it reads a
        // child's whole run state rather than an accumulator, and like
        // `eval_merge` what it returns is not the state it was handed.
        if step == "seed_context" {
            let decision = args.get(DECISION_ARG).cloned().unwrap_or(Value::Null);
            return Ok(super::workflow_research::established(&decision)
                .unwrap_or_else(|| state.to_accumulator()));
        }
        // Every step, with how long it took, and a live run is why. `./euler
        // 351` recorded `verdict solved` at minute 29 and its judge did not
        // start until minute 92, and the console said nothing at all in
        // between: sixty-two minutes with no orchestrator line to attribute
        // them to. Which node was holding is exactly the question the log
        // should answer and could not, so the answer had to be guessed at from
        // which sub-agents happened to be spawning. Cheap — one note per node
        // per pass, against a run that makes a thousand model calls — and the
        // only thing that turns "the run stalled" into a defect report.
        let started = std::time::Instant::now();
        if let Some(tracer) = tracer {
            tracer.note(&format!("solution loop: step {step} entered"));
        }
        let next = match step {
            "attempt" => {
                attempt_step(&self.subagents, tracer, workspace, &self.mailboxes, state).await
            }
            "judge" => judge_step(&self.subagents, tracer, workspace, &thresholds, state).await,
            "reflect" => {
                reflect_step(
                    &self.subagents,
                    tracer,
                    workspace,
                    &self.memory,
                    &self.beside,
                    &thresholds,
                    state,
                )
                .await
            }
            "init_context" => init_context_step(&self.subagents, tracer, state).await,
            // The arm reads the state and the fold writes it, so the read has
            // to finish first — `&state` while `state` is being moved into the
            // fold is the same aliasing the concurrent version avoids by giving
            // each arm its own activation.
            "eval_patterns" => {
                let findings = diversify_pattern_arm(&self.subagents, &state).await;
                fold_arm(state, findings)
            }
            "eval_invention" => {
                let findings = diversify_invention_arm(&self.subagents, workspace, &state).await;
                fold_arm(state, findings)
            }
            "eval_refutation" => {
                let findings = refutation_arm(&self.subagents, workspace, &state).await;
                fold_arm(state, findings)
            }
            // The one arm that returns before its work does. It starts the
            // literature sweep and hands the state straight back, so the
            // barrier below is never waiting on it — see `open_library` for why
            // this is the arm that can afford to arrive an attempt late.
            "eval_library" => {
                super::solutions::open_library(
                    &self.subagents,
                    tracer,
                    &self.beside.library,
                    &state,
                );
                state
            }
            // The escalation, and the only place the sweep is awaited: a run
            // that has stopped making progress should not attempt again before
            // reading what it just gathered.
            "diversify_library" => {
                let findings = diversify_library_arm(&self.subagents, &state).await;
                diversify_merge(fold_arm(state, findings))
            }
            // Runs once, after the loop, and does nothing unless the run
            // ended believing it was solved — the arm itself makes that call,
            // so the graph does not need a switch to express it.
            // The first node after the loop, and the whole of what it does is
            // stop the standing teams. They are `Completion::Standing`, so
            // nothing retires them on their own, and every cycle they take from
            // here on is work on a question the loop has already answered.
            "stand_down" => {
                stand_down(&self.beside.teams, tracer);
                state
            }
            "novelty" => {
                let findings = novelty_arm(&self.subagents, workspace, &state).await;
                fold_arm(state, findings)
            }
            "goal_apply" => apply_goal_decision(state, args),
            _ => {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "unknown loop step `{step}`; expected one of {STEPS:?}"
                )));
            }
        };
        if let Some(tracer) = tracer {
            tracer.note(&format!(
                "solution loop: step {step} finished in {:.1}s",
                started.elapsed().as_secs_f64()
            ));
        }
        let mut carried = next.to_accumulator();
        // Stamped unconditionally rather than for the steps that fan out, so
        // there is no second list of which nodes are arms to disagree with the
        // graph. The merge strips it, and on the paths that do not reach a merge
        // it is inert: the next `to_accumulator` writes a fresh object, so it
        // survives exactly one hop and nothing reads it.
        if let Some(object) = carried.as_object_mut() {
            object.insert(
                super::solutions::ARM_FIELD.to_string(),
                Value::String(step.to_string()),
            );
        }
        Ok(carried)
    }
}

/// Establishes what the run is working on, before the first attempt.
///
/// The loop's opening state is a problem statement and eleven zeroes. Every
/// role that then runs is handed that and told to read the workspace itself,
/// which on a conjecture workspace — a research tree, a claim ledger, threads,
/// and whatever the last run left — is a substantial read that each of them
/// pays for separately and none of them shares.
///
/// The curator does it once and writes down what it found, so the first attempt
/// starts from what is already established rather than from the statement. On a
/// fresh Project Euler problem it finds an empty workspace and says so in a
/// sentence, which costs one child run.
async fn init_context_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    mut state: SolutionState,
) -> SolutionState {
    if let Some(tracer) = tracer {
        tracer.note("solution loop: establishing the run's context");
    }
    state.fresh_context = super::solutions::curate_context(subagents, &state).await;
    state
}

/// Resets the decomposition cadence when the goals child opened one.
///
/// The counter lives in the loop's accumulator, whose sole writer is the loop
/// head, and the child that decides is a separate run that cannot reach it. So
/// the decision crosses back as the child's run state and is applied here, on
/// the loop's own path, which is the only place a write to the accumulator is
/// well defined.
///
/// A cycle that declined deliberately leaves the counter alone: the cadence has
/// come due and been held, so the next cycle asks again rather than waiting
/// another full interval for evidence that may have arrived meanwhile.
fn apply_goal_decision(mut state: SolutionState, args: &Value) -> SolutionState {
    let decision = args.get(DECISION_ARG).cloned().unwrap_or(Value::Null);
    if super::workflow_goals::opened(&decision) {
        state.since_reduction = 0;
    }
    state
}

/// Whether `step` is one this tool runs.
///
/// Pure, so it is testable without a run's context — the tool itself needs a
/// live subagent manager and a vector store, which a unit test has no business
/// standing up. What can go wrong here is a workflow naming a step that does
/// not exist, and that is answerable from the name alone.
pub(super) fn known_step(step: &str) -> bool {
    STEPS.contains(&step)
}

/// Files one arm's findings into the state's slots.
///
/// The arms write disjoint slots, so folding them one at a time here gives the
/// same state as the concurrent fan-out does — the property the parallel
/// version rests on, reused rather than restated.
/// Stops the standing teams, because the run they stand beside has ended.
///
/// They were always stopped — in `orchestrator_runtime`, after the whole
/// workflow returns. The final judge runs *inside* that workflow, so every
/// cycle a team takes between the loop ending and the judge finishing was work
/// on a question already answered, and nothing in the code said otherwise
/// because the call looked correct where it was.
///
/// What it cost is measured. A live `./euler 351` recorded `verdict solved` at
/// minute 29 on an answer two independent programs had agreed on at 15, then
/// spawned thirty more sub-agents over the following 62 minutes and did not
/// start its judge until minute 92 — 85% of the run, and roughly $32 of $35,
/// after the problem was solved.
///
/// Cancelling is a request rather than a kill: a team finishes the cycle it is
/// in and does not start another. That is the right strength here. Work already
/// in flight has been paid for and may as well be filed, and a team torn down
/// mid-write is how a half-written note reaches the workspace.
fn stand_down(teams: &[super::teams::TeamHandle], tracer: Option<&Arc<RunTracer>>) {
    for team in teams {
        team.cancel();
        if let Some(tracer) = tracer {
            tracer.note(&format!(
                "team {}: stood down after {} cycle(s), the run has ended",
                team.name(),
                team.cycles()
            ));
        }
    }
}

fn fold_arm(mut state: SolutionState, findings: Vec<super::solutions::Finding>) -> SolutionState {
    for finding in findings {
        state.diversify_mut().set(finding);
    }
    state
}

#[async_trait]
impl Tool<()> for LoopSteps {
    fn name(&self) -> &'static str {
        TOOL
    }

    fn description(&self) -> &'static str {
        "Runs one step of the solution loop and returns the whole updated state."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "step": { "type": "string", "enum": STEPS },
                    "state": { "type": "object", "description": "The loop's accumulator." },
                    ARMS_ARG: {
                        "type": "array",
                        "description": "Each diversify arm's state, for the merge to fold.",
                        "items": { "type": "object" }
                    },
                    DECISION_ARG: {
                        "type": "object",
                        "description": "The goals child's run state, for the cadence to read."
                    },
                    super::workflow::THRESHOLDS_ARG: {
                        "type": "object",
                        "description": "The school's bounds. Absent means the control school's."
                    }
                },
                "required": ["step", "state"],
                "additionalProperties": false
            }),
        )
    }

    /// Runs the named step.
    ///
    /// # Errors
    ///
    /// Returns an error when the step is missing or unknown. A step that fails
    /// internally does not: a failing specialist becomes a lesson rather than a
    /// failure, which is the loop's own rule and is unchanged here.
    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let step = call
            .arguments
            .get("step")
            .and_then(Value::as_str)
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation("run_loop_step needs a `step`".into())
            })?;
        if !known_step(step) {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "unknown loop step `{step}`; expected one of {STEPS:?}"
            )));
        }
        let accumulator = call.arguments.get("state").cloned().unwrap_or(Value::Null);
        let state = SolutionState::from_accumulator("", &accumulator);
        let carried = self.run(step, state, &call.arguments).await?;
        let mut result = ToolResult::text(call.id, self.name(), carried.to_string());
        result.raw = Some(carried);
        Ok(result)
    }
}

#[cfg(test)]
#[path = "loop_steps_test.rs"]
mod test;
