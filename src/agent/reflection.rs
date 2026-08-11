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
    fn note(tool: &str, count: usize) -> String {
        if count > REPEAT_ESCALATION {
            format!(
                "\n\n[reflection] `{tool}` has now failed {count} times in this run. Repeating it \
                 is not working. Do not call it again with a similar argument. Either achieve the \
                 same end a different way, or record what is blocked in memory.md and move on to \
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
    fn name(&self) -> &str {
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
            let count = self.record(&tool);
            result.content.push_str(&Self::note(&tool, count));
        } else {
            self.clear(&tool);
        }
        Ok(())
    }
}

#[cfg(test)]
mod test;
