//! Turning a reflection's prose into the counters the loop routes on.
//!
//! The workflow's `loop` head folds an object; an `agent` node returns text. So
//! something has to read `VERDICT: SOLVED`, `PROGRESS: NO`, and `KIND:
//! COMPUTATIONAL` out of a reply and produce the seven numbers the routing
//! ladder reads. This is that step, as a `tool_call` node between the
//! reflection and the routing switch.
//!
//! # Why a tool and not a `code` node or a parser prompt
//!
//! Because the logic already exists and is the most expensive code in this
//! crate to have got right. [`record_verdict`](super::solutions) is where every
//! counter the loop routes on is moved, and each of its rules was added after a
//! live run ended on the case it rules out — a claimed answer with no program
//! on disk, a `SOLVED` beside `PROGRESS: NO`, a provider failure counted as an
//! unproductive attempt. Re-expressing that in jq or in a scripting language
//! would be a second implementation of the part of this system least able to
//! afford one.
//!
//! An `output_parser` sub-port was the other candidate and is worse on both
//! counts: it spends a model call to parse something a function already parses,
//! and it cannot see the workspace — and two of the three conditions on
//! `solved` are facts about disk, not about the text.
//!
//! So this tool calls that function. Not a copy of it, not a port of it: the
//! same function, reached through a tool boundary, which is what keeps the two
//! engines' counters identical by construction rather than by comparison.

use std::path::PathBuf;

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

use super::solutions::{SolutionState, record_verdict};

/// The counter names the loop's accumulator folds.
///
/// Named once, here, because three places have to agree on them: the state this
/// tool rebuilds, the object it returns, and the fold in `workflow.rs` that
/// reads it. A test asserts the last two match.
#[cfg(test)]
pub(super) const COUNTERS: [&str; 7] = [
    "attempts",
    "solved",
    "unproductive",
    "blocked",
    "computational",
    "unverified",
    "restarts",
];

/// Reads a reflection's verdict into the loop's counters.
pub(super) struct ParseReflection {
    workspace: Option<PathBuf>,
}

impl ParseReflection {
    /// Builds the tool over the workspace whose disk the verdict is checked
    /// against.
    ///
    /// The workspace is not optional in spirit: two of the three conditions on
    /// `solved` are questions about what is on disk. It is `Option` only
    /// because `record_verdict` already treats an absent workspace as "cannot
    /// check", which is what a unit test wants.
    pub(super) fn new(workspace: Option<PathBuf>) -> Self {
        Self { workspace }
    }
}

/// Rebuilds the state `record_verdict` expects from the accumulator's counters.
///
/// The loop head owns the accumulator, so what arrives here is a plain object
/// of numbers. `record_verdict` reads counters and `last_attempt` — the latter
/// because a provider failure has to be counted before progress is judged, or
/// reflection on an `HTTP 403` registers as an unproductive attempt and drives
/// the run into diversifying, which is three more child runs into the same wall.
fn state_from(args: &Value) -> SolutionState {
    // Saturating rather than `as`, which truncates on a 32-bit target. A
    // counter arriving larger than `usize` is nonsense anyway; clamping keeps
    // it nonsense in the direction that stops the loop rather than one that
    // silently wraps it to zero and runs forever.
    let counter = |key: &str| {
        usize::try_from(
            args.get("state")
                .and_then(|state| state.get(key))
                .and_then(Value::as_u64)
                .unwrap_or_default(),
        )
        .unwrap_or(usize::MAX)
    };
    let mut state = SolutionState::new(
        args.get("problem")
            .and_then(Value::as_str)
            .unwrap_or_default(),
    );
    state.attempts = counter("attempts");
    state.unproductive = counter("unproductive");
    state.blocked = counter("blocked");
    state.computational = counter("computational");
    state.unverified = counter("unverified");
    state.restarts = counter("restarts");
    state.solved = args
        .get("state")
        .and_then(|state| state.get("solved"))
        .and_then(Value::as_bool)
        .unwrap_or_default();
    state.last_attempt = args
        .get("last_attempt")
        .and_then(Value::as_str)
        .unwrap_or_default()
        .to_string();
    state
}

/// The counters, as the fold reads them.
fn counters_of(state: &SolutionState, progressed: bool) -> Value {
    json!({
        "attempts": state.attempts,
        "solved": state.solved,
        "unproductive": state.unproductive,
        "blocked": state.blocked,
        "computational": state.computational,
        "unverified": state.unverified,
        "restarts": state.restarts,
        // Not a counter the ladder reads, but the reason several of them moved.
        // A workflow reader tracing why a run diversified wants it.
        "progressed": progressed,
    })
}

#[async_trait]
impl Tool<()> for ParseReflection {
    fn name(&self) -> &'static str {
        "parse_reflection"
    }

    fn description(&self) -> &'static str {
        "Reads a reflection's verdict into the counters the solution loop routes on."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "reflection": {
                        "type": "string",
                        "description": "The reflection agent's reply, verbatim."
                    },
                    "state": {
                        "type": "object",
                        "description": "The loop's current counters."
                    },
                    "last_attempt": {
                        "type": "string",
                        "description": "The attempt report, read for a provider failure."
                    },
                    "problem": { "type": "string", "description": "The problem as posed." }
                },
                "required": ["reflection", "state"],
                "additionalProperties": false
            }),
        )
    }

    /// Applies the reflection to the counters.
    ///
    /// # Errors
    ///
    /// Returns an error when `reflection` is missing. An empty one is *not* an
    /// error: `record_verdict` treats an unparsable reply as "no verdict", which
    /// leaves the loop running rather than declaring anything, and that is the
    /// behaviour a missing field should inherit rather than override.
    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let reflection = call
            .arguments
            .get("reflection")
            .and_then(Value::as_str)
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation(
                    "parse_reflection needs a `reflection`".into(),
                )
            })?;
        let mut state = state_from(&call.arguments);
        // The same function the state graph calls, not a copy of it. No tracer:
        // the workflow's own observer records the step, and a second commentary
        // on the same decision would double every line in the console.
        let progressed = record_verdict(
            reflection,
            None,
            self.workspace.as_deref().filter(|path| path.exists()),
            &mut state,
        );
        let counters = counters_of(&state, progressed);
        let mut result = ToolResult::text(call.id, self.name(), counters.to_string());
        result.raw = Some(counters);
        Ok(result)
    }
}

/// The workspace path a tool built for `workspace` checks against.
#[cfg(test)]
pub(super) fn workspace_of(tool: &ParseReflection) -> Option<&std::path::Path> {
    tool.workspace.as_deref()
}

#[cfg(test)]
#[path = "reflection_tool_test.rs"]
mod test;
