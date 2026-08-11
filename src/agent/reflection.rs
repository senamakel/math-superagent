//! Middleware that reflects on failures as they happen, inside any agent run.
//!
//! The solution loop in `orchestrator::solutions` reflects between attempts.
//! That is the right granularity for changing approach, and the wrong one for
//! a tool that has just failed three times in a row: by the time the attempt
//! ends, the run has already spent its budget repeating the same mistake.
//!
//! This middleware sits in every agent's stack and watches tool results. When
//! one fails, it appends a short, specific note to the result the model is
//! about to read. When the *same* tool fails repeatedly, the note escalates to
//! name the loop explicitly, because a model that cannot see it is repeating
//! itself will keep going until the budget runs out.

use std::collections::HashMap;
use std::sync::Mutex;

use async_trait::async_trait;
use tinyagents::harness::context::RunContext;
use tinyagents::harness::middleware::Middleware;
use tinyagents::harness::tool::ToolResult;

use crate::agent::Result;

/// Repeats of one failing tool before the note escalates.
const REPEAT_ESCALATION: usize = 2;

/// Recognises a tool call whose arguments were cut off mid-generation.
///
/// The provider returns a well-formed response whose `arguments` string is
/// simply incomplete — `{"agent": "tool_builder", "input": "` — because the
/// turn hit its output-token cap partway through writing them. The vendored
/// `truncated_empty` recovery does not cover this: that path needs a turn with
/// *no* tool calls, and here there is one. So the failure arrives as an
/// ordinary tool error, and the generic advice below is actively misleading —
/// it tells the model to work out what was wrong with its arguments, when the
/// arguments were right and merely unfinished. Observed twice on one problem,
/// each time as a multi-minute ladder of identical over-long retries.
fn truncated_arguments(content: &str) -> bool {
    content.contains("invalid JSON arguments")
        && (content.contains("EOF while parsing") || content.contains("control character"))
}

/// Tracks failures per tool within a single run.
#[derive(Debug, Default)]
pub struct ReflectionMiddleware {
    failures: Mutex<HashMap<String, usize>>,
}

impl ReflectionMiddleware {
    /// Creates a middleware with no recorded failures.
    #[must_use]
    pub fn new() -> Self {
        Self::default()
    }

    /// Records a failure for `tool` and returns how many it has now had.
    fn record(&self, tool: &str) -> usize {
        let Ok(mut failures) = self.failures.lock() else {
            // A poisoned lock must not fail the run; degrade to first-failure
            // advice, which is still better than nothing.
            return 1;
        };
        let count = failures.entry(tool.to_string()).or_insert(0);
        *count += 1;
        *count
    }

    /// Clears a tool's failure count once it succeeds again.
    fn clear(&self, tool: &str) {
        if let Ok(mut failures) = self.failures.lock() {
            failures.remove(tool);
        }
    }

    /// Builds the note appended to a failed tool result.
    fn note(tool: &str, count: usize, content: &str) -> String {
        if truncated_arguments(content) {
            return format!(
                "\n\n[reflection] `{tool}` was never called: the arguments stopped mid-JSON \
                 because the turn ran out of output tokens while still writing them. Nothing was \
                 wrong with your intent, so do not rephrase it — the call was simply too long to \
                 finish. Re-issue it now with the longest string argument cut down hard, to a few \
                 sentences. A brief for another agent does not need to restate the problem, the \
                 derivation so far, or anything already on disk: that agent reads the workspace \
                 files itself. Say what it must do and what to report back."
            );
        }
        if count > REPEAT_ESCALATION {
            format!(
                "\n\n[reflection] `{tool}` has now failed {count} times in this run. Repeating it \
                 is not working. Do not call it again with a similar argument. Either achieve the \
                 same end a different way, or record what is blocked in MEMORY.md and move on to \
                 a part of the problem that is not blocked."
            )
        } else {
            format!(
                "\n\n[reflection] `{tool}` failed. Before retrying, state to yourself what \
                 specifically was wrong with the call and change that thing. A retry that repeats \
                 the same argument will fail the same way."
            )
        }
    }
}

#[async_trait]
impl<State: Send + Sync + 'static> Middleware<State> for ReflectionMiddleware {
    fn name(&self) -> &'static str {
        "reflection"
    }

    async fn after_tool(
        &self,
        _ctx: &mut RunContext<()>,
        _state: &State,
        result: &mut ToolResult,
    ) -> Result<()> {
        let tool = result.name.clone();
        if result.is_error() {
            // A truncated call is not held against the tool. It never ran, so
            // counting it would escalate to "stop calling this tool" advice
            // about a tool that has done nothing wrong, and steer the run off
            // the delegation it actually needs.
            let count = if truncated_arguments(&result.content) {
                0
            } else {
                self.record(&tool)
            };
            let note = Self::note(&tool, count, &result.content);
            result.content.push_str(&note);
        } else {
            self.clear(&tool);
        }
        Ok(())
    }
}

#[cfg(test)]
mod test;
