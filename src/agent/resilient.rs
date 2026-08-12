//! Tool and model wrappers that keep a long investigation alive.
//!
//! Two failure modes were each costing a whole specialist run:
//!
//! * A tool returning `Err` aborts the run that called it. Every accumulated
//!   message, derivation, and verified computation in that run is discarded,
//!   and the parent only learns that the child failed. Observed three times in
//!   one session: a memory-service `409`, a path spelled `/workspace/solution.md`, and
//!   a PDF that was not UTF-8. None of those is unrecoverable — the model can
//!   fix its arguments or pick another source if it is simply told what went
//!   wrong.
//! * A stalled provider request runs to the vendored 600-second default
//!   timeout before failing, then retries up to the policy's attempt limit. A
//!   single wedged call can therefore consume tens of minutes of a run's
//!   wall-clock budget while the container sits idle.

use std::sync::Arc;
use std::time::Duration;

use async_trait::async_trait;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use tinyagents::harness::tool::ToolPolicy;

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Default per-request provider timeout.
///
/// This has to sit between two failure modes, and it was first set far too
/// low. At 150 seconds every attempt at a legitimately slow call timed out,
/// the retry ladder exhausted on a request that would have succeeded, and two
/// runs died having done nothing — a self-inflicted outage strictly worse than
/// the hang it was meant to bound. Calls of several minutes are normal for a
/// reasoning model given a large system prompt and a full transcript.
///
/// Seven minutes is long enough that a working call is never cut off, and
/// still under the vendored 600-second default, so a genuinely wedged request
/// fails with retries left in the budget. Raise it before lowering it:
/// truncating good calls is the more expensive mistake.
const DEFAULT_REQUEST_TIMEOUT: Duration = Duration::from_mins(7);

/// Slowest generation rate, in output tokens per second, a request is given
/// time for.
///
/// A flat timeout silently assumed every turn is allowed the same number of
/// output tokens, and upstream `truncated_empty` recovery breaks that
/// assumption: a turn that ends at the cap having emitted no tool call is
/// re-issued with `max_tokens` doubled, clamped at four times. Generation time
/// is linear in output length, so the recovery attempt needs proportionally
/// more wall clock and was given none.
///
/// That made the recovery structurally unable to succeed. A live turn produced
/// 12,000 tokens in 281 seconds — about 43 per second — and truncated. Its
/// retry at 24,000 tokens therefore needed some nine minutes against a
/// seven-minute ceiling, and at the 4x clamp roughly nineteen. Every
/// truncation recovery timed out, burning a full timeout per attempt to
/// accomplish nothing, which is exactly the self-inflicted outage the flat
/// timeout was raised to 7 minutes to avoid.
///
/// Thirty was chosen from that measurement and is too optimistic. Across four
/// live runs the rate is 27–33 tokens per second in the ordinary case but
/// falls much further in the tail: one `tool_builder` turn produced 4,653
/// tokens in 383 seconds, **12.2 per second**. At that rate a turn allowed the
/// full 12,000-token cap needs some sixteen minutes, against the 400 seconds
/// thirty would have granted it — so the slowest turns, which are the ones
/// carrying the most work, are exactly the ones a rate-derived bound would cut
/// off. Worse, truncation recovery doubles the cap, so the retry needs twice
/// the wall clock and the doubling makes the timeout *more* likely rather than
/// less.
///
/// Twelve is the slowest rate actually observed. It keeps the bound a safety
/// ceiling rather than a limit a working call can reach, which is the whole
/// point: a cap that trips routinely costs more than the long turns it
/// prevents.
const MIN_OUTPUT_TOKENS_PER_SECOND: u64 = 12;

/// Wraps a tool so a recoverable failure answers the model instead of killing
/// the run.
///
/// The error text is returned as a `ToolResult` carrying an `error`, which is
/// the vendored harness's own mechanism for a failure the model should see and
/// correct. This does not weaken any boundary: a rejected call still did not
/// happen, and the rejection reason is what the model needs in order to stop
/// repeating it.
pub struct ResilientTool<S: Send + Sync> {
    inner: Arc<dyn Tool<S>>,
}

impl<S: Send + Sync> std::fmt::Debug for ResilientTool<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("ResilientTool")
            .field("tool", &self.inner.name())
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> ResilientTool<S> {
    /// Wraps `inner` so its errors are reported rather than propagated.
    #[must_use]
    pub fn new(inner: Arc<dyn Tool<S>>) -> Self {
        Self { inner }
    }
}

#[async_trait]
impl<S: Send + Sync + 'static> Tool<S> for ResilientTool<S> {
    fn name(&self) -> &str {
        self.inner.name()
    }

    fn description(&self) -> &str {
        self.inner.description()
    }

    fn schema(&self) -> ToolSchema {
        self.inner.schema()
    }

    /// Forwards the wrapped tool's safety classification.
    ///
    /// Falling back to the default here would silently declassify every
    /// filesystem and network tool in the runtime and disarm policy
    /// enforcement, which is the opposite of what this wrapper is for.
    fn policy(&self) -> ToolPolicy {
        self.inner.policy()
    }

    fn display_label(&self, call: &ToolCall) -> Option<String> {
        self.inner.display_label(call)
    }

    fn display_detail(&self, call: &ToolCall) -> Option<String> {
        self.inner.display_detail(call)
    }

    async fn call(&self, state: &S, call: ToolCall) -> Result<ToolResult> {
        let call_id = call.id.clone();
        match self.inner.call(state, call).await {
            Ok(result) => Ok(result),
            Err(error) => Ok(ToolResult::error(
                call_id,
                self.inner.name().to_string(),
                format!(
                    "{error}\n\nThis call did not run. Correct the arguments and try again, or \
                     use a different approach. Do not repeat the identical call."
                ),
            )),
        }
    }
}

/// Wraps a chat model so every request carries a bounded timeout.
///
/// The vendored provider applies its own 600-second default only when the
/// request leaves `timeout_ms` unset, and the agent loop never sets it, so
/// without this a stalled connection blocks for ten minutes before the first
/// retry. A request that already specifies a timeout is passed through
/// untouched.
pub struct BoundedTimeoutModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    timeout: Duration,
}

impl<S: Send + Sync> std::fmt::Debug for BoundedTimeoutModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("BoundedTimeoutModel")
            .field("timeout", &self.timeout)
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> BoundedTimeoutModel<S> {
    /// Wraps `inner` with the default per-request timeout.
    #[must_use]
    pub fn new(inner: Arc<dyn ChatModel<S>>) -> Self {
        Self {
            inner,
            timeout: request_timeout_from_env(),
        }
    }

    fn bound(&self, request: ModelRequest) -> ModelRequest {
        if request.timeout_ms.is_some() {
            return request;
        }
        let millis =
            u64::try_from(self.allowance(request.max_tokens).as_millis()).unwrap_or(u64::MAX);
        request.with_timeout_ms(millis)
    }

    /// Returns the wall clock a request asking for `max_tokens` output is
    /// given.
    ///
    /// The configured timeout is a floor, so an ordinary turn is bounded
    /// exactly as before and only a request granted an unusually large output
    /// budget — which upstream only does to recover a truncated turn — is
    /// given longer.
    fn allowance(&self, max_tokens: Option<u32>) -> Duration {
        let Some(tokens) = max_tokens else {
            return self.timeout;
        };
        let needed = Duration::from_secs(u64::from(tokens) / MIN_OUTPUT_TOKENS_PER_SECOND);
        needed.max(self.timeout)
    }
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for BoundedTimeoutModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        self.inner.invoke(state, self.bound(request)).await
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        self.inner.stream(state, self.bound(request)).await
    }
}

/// Reads the per-request provider timeout, in seconds, from the environment.
///
/// `MATH_AGENT_REQUEST_SECONDS` overrides the default; a missing, empty,
/// unparsable, or zero value keeps it.
fn request_timeout_from_env() -> Duration {
    std::env::var("MATH_AGENT_REQUEST_SECONDS")
        .ok()
        .and_then(|value| value.trim().parse::<u64>().ok())
        .filter(|seconds| *seconds > 0)
        .map_or(DEFAULT_REQUEST_TIMEOUT, Duration::from_secs)
}

#[cfg(test)]
#[path = "resilient_test.rs"]
mod test;
