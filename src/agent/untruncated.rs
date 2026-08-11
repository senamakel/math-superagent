//! Re-issues a turn the provider cut off at the output cap.
//!
//! The vendored loop already recovers one shape of truncation: a turn that
//! ends with `finish_reason == "length"`, no tool calls, and *no text* — the
//! model spent its whole budget on the hidden reasoning channel — is re-issued
//! with the cap doubled. That recovery requires the text to be empty
//! (`response.text().trim().is_empty()`), so it never fires for the shape that
//! costs the most.
//!
//! When a turn ends at the cap having produced text but no tool call, the loop
//! treats it as the turn's final answer and ends the run. The answer is a
//! sentence cut in half. A live run reached exactly this: its root agent
//! truncated at 12,000 tokens, recovered into a 24,000-token turn, spent that
//! entire doubled budget too, and its run then completed on the fragment —
//! after the mathematics underneath it was finished and cross-checked. The
//! result existed; the agent that would report it stopped mid-word, and the
//! child runs still working had nobody left to collect them.
//!
//! So this wrapper applies the same recovery to the case upstream excludes.
//! It sits outside the timeout, affinity, and accounting wrappers, so each
//! re-issue is bounded and routed on its own terms rather than inheriting the
//! cut-off attempt's, and is recorded as the separate paid call it is.
//!
//! It cannot fix a turn that has genuinely run out of things to say within any
//! budget, so growth is clamped exactly as upstream clamps it and the last
//! response is returned rather than an error: degrading to today's behaviour
//! is right, because a truncated answer still beats no answer.

use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::Result;
use crate::agent::trace::RunTracer;

/// How many times one turn may be re-issued after being cut off.
///
/// Two, matching the 4x clamp below: the first doubles the cap, the second
/// doubles it again and reaches the ceiling. A third would spend minutes of
/// generation to re-learn what the second established.
const MAX_REISSUES: u32 = 2;

/// Ceiling on cap growth, as a multiple of the turn's original cap.
///
/// The same 4x upstream uses. A turn needing more than four times the
/// configured budget is not being truncated by an unlucky cap; it is being
/// asked for the wrong thing, and the fix belongs in the prompt.
const MAX_CAP_GROWTH: u32 = 4;

/// Wraps a chat model so a turn cut off at the cap is asked for again.
pub struct UntruncatedModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    tracer: Option<Arc<RunTracer>>,
}

impl<S: Send + Sync> std::fmt::Debug for UntruncatedModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("UntruncatedModel")
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> UntruncatedModel<S> {
    /// Wraps `inner` so its truncated turns are re-issued.
    #[must_use]
    pub fn new(inner: Arc<dyn ChatModel<S>>) -> Self {
        Self {
            inner,
            tracer: None,
        }
    }

    /// Announces each re-issue on the operator console.
    ///
    /// Without this a re-issue is invisible where it matters most. The console
    /// prints one line per call the *loop* made, and a re-issue happens inside
    /// one of those, so a turn spending two attempts shows as `model call #2`
    /// followed by many minutes of nothing — indistinguishable from a wedged
    /// request, and the wrong diagnosis leads straight to killing a container
    /// that was working. The cost lands in `trace.jsonl` either way; what was
    /// missing is knowing to look.
    #[must_use]
    pub fn with_tracer(mut self, tracer: Arc<RunTracer>) -> Self {
        self.tracer = Some(tracer);
        self
    }
}

/// Returns whether a response was cut off with no tool call to act on.
///
/// A response carrying tool calls is not truncated in any way that matters:
/// the loop runs them and asks again, so the turn continues regardless of what
/// the provider says about length.
fn cut_off(response: &ModelResponse) -> bool {
    response.finish_reason.as_deref() == Some("length") && response.tool_calls().is_empty()
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for UntruncatedModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        let mut response = self.inner.invoke(state, request.clone()).await?;
        let Some(original) = request.max_tokens else {
            // With no cap of our own to raise, a re-issue would ask for the
            // identical thing and get the identical answer.
            return Ok(response);
        };
        let ceiling = original.saturating_mul(MAX_CAP_GROWTH);
        let mut cap = original;
        for _ in 0..MAX_REISSUES {
            if !cut_off(&response) || cap >= ceiling {
                break;
            }
            cap = cap.saturating_mul(2).min(ceiling);
            if let Some(tracer) = self.tracer.as_ref() {
                tracer.note(&format!(
                    "model TRUNCATED at {} output tokens with no tool call; re-issuing at {cap}",
                    cap / 2
                ));
            }
            response = self
                .inner
                .invoke(state, request.clone().with_max_tokens(cap))
                .await?;
        }
        Ok(response)
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        // The streaming path yields incrementally, so there is no completed
        // response to inspect before the caller has already consumed it.
        self.inner.stream(state, request).await
    }
}

#[cfg(test)]
mod test;
