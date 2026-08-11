//! Run budgets for long mathematical investigations.
//!
//! `TinyAgents` defaults a run to 25 model calls, 50 tool calls, and no wall
//! clock cap, and fails the whole run when a cap trips. Those defaults suit a
//! short question-answering turn. A research problem that has to be understood,
//! researched, derived, implemented, and verified needs a much larger budget,
//! and losing every intermediate result at the cap is the worst possible
//! outcome. This module centralises the budget and reads overrides from the
//! environment so a single run can be widened without a rebuild.

use std::time::Duration;

use tinyagents::harness::limits::LimitBehavior;
use tinyagents::harness::runtime::{PayloadCapture, RunPolicy};

/// Model calls allowed in one agent run before it stops with partial results.
const DEFAULT_MAX_MODEL_CALLS: usize = 250;
/// Tool calls allowed in one agent run.
///
/// Deliberately far above what `DEFAULT_MAX_MODEL_CALLS` turns of parallel tool
/// calling can reach, so the model-call cap is the one that actually trips.
/// `LimitBehavior::StopWithPartial` is honoured on the model-call path in the
/// vendored agent loop but not on the tool-call path, which still fails the run
/// outright (`vendor/tinyagents/src/harness/agent_loop/tools.rs`). Until that is
/// fixed upstream, keeping the tool cap out of reach is what makes a budgeted
/// stop graceful instead of destructive. Do not narrow this to "just above" the
/// model cap: one model turn can request several tool calls at once.
const DEFAULT_MAX_TOOL_CALLS: usize = 4_000;
/// Wall-clock ceiling for one agent run, in minutes.
const DEFAULT_RUN_MINUTES: u64 = 120;
/// Wall-clock ceiling for a single tool call, in minutes.
const DEFAULT_TOOL_MINUTES: u64 = 10;
/// Output tokens allowed in one model turn.
///
/// Left unset, a turn ran to 9,361 tokens and took 2.9 minutes, and longer
/// turns took over seven. The model was not hanging: it was writing an essay
/// where a decision was wanted. Generation is linear in output length, so an
/// uncapped turn is an uncapped wall clock, and a run spends its budget on
/// prose nobody reads instead of on executing anything.
///
/// Four thousand tokens is far more than any single decision, tool call, or
/// derivation step needs, while bounding a turn to roughly a minute. Raising
/// this trades wall clock for verbosity; it does not buy better reasoning.
const DEFAULT_TURN_OUTPUT_TOKENS: u32 = 4_000;

/// Attempts allowed for one model call, counting the first try.
///
/// The vendored defaults are four attempts backing off from 200ms, which suits
/// a fast API returning a clean 503. They do not suit this runtime: a provider
/// stream that drops mid-body surfaces as a decode failure, and three retries
/// spaced under two seconds all hit the same bad minute and exhaust before the
/// condition clears. Both a longer ladder and a slower one are needed.
const DEFAULT_MODEL_ATTEMPTS: usize = 7;
/// First backoff between model-call attempts, in milliseconds.
const DEFAULT_BACKOFF_MS: u64 = 2_000;
/// Longest backoff between model-call attempts, in milliseconds.
const DEFAULT_MAX_BACKOFF_MS: u64 = 60_000;

/// The resolved budget shared by the orchestrator and every specialist.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct RunBudget {
    /// Maximum model calls in one agent run.
    pub max_model_calls: usize,
    /// Maximum tool calls in one agent run.
    pub max_tool_calls: usize,
    /// Maximum wall-clock time for one agent run.
    pub run_timeout: Duration,
    /// Maximum wall-clock time for one tool call.
    pub tool_timeout: Duration,
    /// Maximum output tokens for one model turn.
    pub max_turn_output_tokens: u32,
}

impl Default for RunBudget {
    fn default() -> Self {
        Self {
            max_model_calls: DEFAULT_MAX_MODEL_CALLS,
            max_tool_calls: DEFAULT_MAX_TOOL_CALLS,
            run_timeout: Duration::from_secs(DEFAULT_RUN_MINUTES * 60),
            tool_timeout: Duration::from_secs(DEFAULT_TOOL_MINUTES * 60),
            max_turn_output_tokens: DEFAULT_TURN_OUTPUT_TOKENS,
        }
    }
}

impl RunBudget {
    /// Reads the budget from the environment, falling back to the defaults.
    ///
    /// Recognised variables are `MATH_AGENT_MAX_MODEL_CALLS`,
    /// `MATH_AGENT_MAX_TOOL_CALLS`, `MATH_AGENT_RUN_MINUTES`, and
    /// `MATH_AGENT_TOOL_MINUTES`. A missing, empty, unparsable, or zero value
    /// keeps the default, so a malformed override never silently disables a
    /// budget.
    #[must_use]
    pub fn from_env() -> Self {
        let defaults = Self::default();
        Self {
            max_model_calls: positive_env("MATH_AGENT_MAX_MODEL_CALLS")
                .and_then(|value| usize::try_from(value).ok())
                .unwrap_or(defaults.max_model_calls),
            max_tool_calls: positive_env("MATH_AGENT_MAX_TOOL_CALLS")
                .and_then(|value| usize::try_from(value).ok())
                .unwrap_or(defaults.max_tool_calls),
            run_timeout: positive_env("MATH_AGENT_RUN_MINUTES")
                .map_or(defaults.run_timeout, |value| {
                    Duration::from_secs(value.saturating_mul(60))
                }),
            tool_timeout: positive_env("MATH_AGENT_TOOL_MINUTES")
                .map_or(defaults.tool_timeout, |value| {
                    Duration::from_secs(value.saturating_mul(60))
                }),
            max_turn_output_tokens: positive_env("MATH_AGENT_TURN_OUTPUT_TOKENS")
                .and_then(|value| u32::try_from(value).ok())
                .unwrap_or(defaults.max_turn_output_tokens),
        }
    }

    /// Returns the tool timeout in milliseconds, saturating at `u64::MAX`.
    #[must_use]
    pub fn tool_timeout_ms(&self) -> u64 {
        u64::try_from(self.tool_timeout.as_millis()).unwrap_or(u64::MAX)
    }

    /// Returns the run timeout in milliseconds, saturating at `u64::MAX`.
    #[must_use]
    pub fn run_timeout_ms(&self) -> u64 {
        u64::try_from(self.run_timeout.as_millis()).unwrap_or(u64::MAX)
    }

    /// Builds the run policy that enforces this budget.
    ///
    /// The policy stops with partial results instead of erroring at a cap, so
    /// a long investigation still returns the work it completed, and it
    /// captures model and tool payloads so the Langfuse trace shows what each
    /// agent actually sent and received.
    #[must_use]
    pub fn run_policy(&self) -> RunPolicy {
        let mut policy = RunPolicy::default();
        policy.limits.max_model_calls = self.max_model_calls;
        policy.limits.max_tool_calls = self.max_tool_calls;
        policy.limits.max_wall_clock_ms = Some(self.run_timeout_ms());
        policy.limits.behavior = LimitBehavior::StopWithPartial;
        policy.capture = PayloadCapture::all();

        // The loop takes the stricter of these two caps, so raising the retry
        // policy alone would change nothing: `RunLimits::max_retries_per_call`
        // defaults to 3 and would silently win.
        policy.limits.max_retries_per_call = DEFAULT_MODEL_ATTEMPTS.saturating_sub(1);
        policy.retry.max_attempts = DEFAULT_MODEL_ATTEMPTS;
        policy.retry.initial_backoff_ms = DEFAULT_BACKOFF_MS;
        policy.retry.max_backoff_ms = DEFAULT_MAX_BACKOFF_MS;
        // Jitter matters because runs are launched together and retry in
        // lockstep otherwise, so every attempt lands in the same bad instant.
        policy.retry.jitter = true;
        policy
    }
}

fn positive_env(name: &str) -> Option<u64> {
    std::env::var(name)
        .ok()?
        .trim()
        .parse::<u64>()
        .ok()
        .filter(|value| *value > 0)
}

#[cfg(test)]
mod test;
