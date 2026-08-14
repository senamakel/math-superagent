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
    diversify_merge, diversify_pattern_arm, judge_step, reflect_step,
};
use super::vector::VectorStore;

/// The steps a workflow node may ask for.
///
/// A closed set, matched by name. An unknown step is an error rather than a
/// no-op: a workflow naming a step that does not exist would otherwise run,
/// change nothing, and route on a state nobody advanced.
const STEPS: [&str; 7] = [
    "attempt",
    "judge",
    "reflect",
    "diversify_library",
    "diversify_patterns",
    "diversify_invention",
    "diversify_merge",
];

/// Everything one step needs from the run.
pub(super) struct LoopSteps {
    subagents: AsyncSubagentManager,
    tracer: Option<Arc<RunTracer>>,
    workspace: Option<PathBuf>,
    memory: VectorStore,
    beside: Beside,
    mailboxes: Mailboxes,
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
        }
    }

    /// Runs one step against `state`.
    async fn run(&self, step: &str, state: SolutionState) -> Result<SolutionState> {
        let tracer = self.tracer.as_ref();
        let workspace = self.workspace.as_deref();
        Ok(match step {
            "attempt" => {
                attempt_step(&self.subagents, tracer, workspace, &self.mailboxes, state).await
            }
            "judge" => judge_step(&self.subagents, tracer, workspace, state).await,
            "reflect" => {
                reflect_step(
                    &self.subagents,
                    tracer,
                    workspace,
                    &self.memory,
                    &self.beside,
                    state,
                )
                .await
            }
            // The arm reads the state and the fold writes it, so the read has
            // to finish first — `&state` while `state` is being moved into the
            // fold is the same aliasing the concurrent version avoids by giving
            // each arm its own activation.
            "diversify_library" => {
                let findings = diversify_library_arm(&self.subagents, &state).await;
                fold_arm(state, findings)
            }
            "diversify_patterns" => {
                let findings = diversify_pattern_arm(&self.subagents, &state).await;
                fold_arm(state, findings)
            }
            "diversify_invention" => {
                let findings =
                    diversify_invention_arm(&self.subagents, workspace, &state).await;
                fold_arm(state, findings)
            }
            "diversify_merge" => diversify_merge(state),
            _ => {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "unknown loop step `{step}`; expected one of {STEPS:?}"
                )));
            }
        })
    }
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
fn fold_arm(mut state: SolutionState, findings: Vec<super::solutions::Finding>) -> SolutionState {
    for finding in findings {
        state.diversify_mut().set(finding);
    }
    state
}

#[async_trait]
impl Tool<()> for LoopSteps {
    fn name(&self) -> &'static str {
        "run_loop_step"
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
                    "state": { "type": "object", "description": "The loop's accumulator." }
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
        let next = self.run(step, state).await?;
        let carried = next.to_accumulator();
        let mut result = ToolResult::text(call.id, self.name(), carried.to_string());
        result.raw = Some(carried);
        Ok(result)
    }
}

#[cfg(test)]
#[path = "loop_steps_test.rs"]
mod test;
