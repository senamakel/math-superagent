//! Tool and model wrappers that keep a long investigation alive.
//!
//! Two failure modes were each costing a whole specialist run:
//!
//! * A tool returning `Err` aborts the run that called it. Every accumulated
//!   message, derivation, and verified computation in that run is discarded,
//!   and the parent only learns that the child failed. Observed three times in
//!   one session: a Qdrant `409`, a path spelled `/workspace/solution.md`, and
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
use tinyagents::harness::model::{ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Default per-request provider timeout.
///
/// Well below the vendored 600-second default, so a wedged request fails while
/// the retry ladder can still do something useful with the remaining budget.
const DEFAULT_REQUEST_TIMEOUT: Duration = Duration::from_secs(150);

/// Wraps a tool so a recoverable failure answers the model instead of killing
/// the run.
///
/// The error text is returned as a `ToolResult` carrying an `error`, which is
/// the vendored harness's own mechanism for a failure the model should see and
/// correct. This does not weaken any boundary: a rejected call still did not
/// happen, and the rejection reason is what the model needs in order to stop
/// repeating it.
#[derive(Debug)]
pub struct ResilientTool<S: Send + Sync> {
    inner: Arc<dyn Tool<S>>,
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
    fn name(&self) -> &'static str {
        self.inner.name()
    }

    fn description(&self) -> &'static str {
        self.inner.description()
    }

    fn schema(&self) -> ToolSchema {
        self.inner.schema()
    }

    async fn call(&self, state: &S, call: ToolCall) -> Result<ToolResult> {
        let call_id = call.id.clone();
        match self.inner.call(state, call).await {
            Ok(result) => Ok(result),
            Err(error) => Ok(ToolResult::error(
                call_id,
                self.inner.name(),
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
        let millis = u64::try_from(self.timeout.as_millis()).unwrap_or(u64::MAX);
        request.with_timeout_ms(millis)
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
mod test;
