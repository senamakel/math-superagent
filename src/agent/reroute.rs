//! Retries a call `OpenRouter` failed because the provider it routed to did.
//!
//! `OpenRouter` reports an upstream provider's failure as its own HTTP 400
//! carrying the message `Provider returned error`. That status is a lie about
//! whose fault it is: a 400 normally means the request was malformed, so the
//! retry ladder classifies it as permanent and does not try again. The request
//! was fine. The provider serving it was not, and the same request sent a
//! moment later — or to anyone else — succeeds.
//!
//! The cost of getting this wrong is not one call. Every model error inside a
//! child run propagates out as the child's whole result, so a specialist that
//! meets this on its first turn dies before doing anything, and the solution
//! loop records the attempt that delegated to it as having executed nothing. A
//! live run lost two of its eight attempts to exactly that, each ending with
//! the goals agent having failed on `openrouter returned HTTP 400: Provider
//! returned error` and a reflection correctly concluding that no program had
//! run — a full attempt spent on a provider hiccup.
//!
//! So this wrapper retries that one shape. It matches structurally on the
//! status *and* the message, because a genuine request-shape 400 — an
//! unsupported parameter, a malformed tool schema — is permanent, and retrying
//! it would replace a fast, honest failure with a slow, identical one.
//!
//! It sits outside the affinity wrapper, which is the point of putting it
//! here rather than deeper. [`crate::agent::sticky`] blocks the pinned
//! provider for exactly one request when a call fails, so a retry that passes
//! back through it asks `OpenRouter` to route anywhere *but* the provider that
//! just failed. A retry inside the pin would ask the broken provider again.

use std::sync::Arc;
use std::time::Duration;

use async_trait::async_trait;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::trace::RunTracer;
use crate::agent::{Result, TinyAgentsError};

/// How many extra attempts one call may spend on a rerouted provider failure.
///
/// Two, so a call can survive one bad provider and then one more. The block in
/// [`crate::agent::sticky`] lasts a single request, so consecutive retries
/// exclude only the most recent failure rather than narrowing the routing pool
/// with each attempt — which is what keeps a third attempt worth making.
///
/// Beyond that the evidence stops pointing at one unlucky route. A model
/// nobody can serve is a condition to report, not to sit in: the run's own
/// retry ladder is still underneath this, and a specialist that fails is
/// information the solution loop already knows how to use.
const MAX_REROUTES: usize = 2;

/// Pause before the first retry.
///
/// Short on purpose. The remedy here is a different provider, not the passage
/// of time, and the diversion is applied by the wrapper underneath as soon as
/// the next request is built. The pause exists only so a provider that failed
/// for a reason `OpenRouter` will notice — one dropping every request — is not
/// hammered inside a millisecond.
const FIRST_BACKOFF: Duration = Duration::from_secs(2);

/// The message `OpenRouter` uses for an upstream provider's failure.
const UPSTREAM_FAILURE: &str = "provider returned error";

/// Wraps a chat model so an upstream provider failure is routed around.
pub struct ReroutingModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    tracer: Option<Arc<RunTracer>>,
    agent: String,
}

impl<S: Send + Sync> std::fmt::Debug for ReroutingModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("ReroutingModel")
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> ReroutingModel<S> {
    /// Wraps `inner` so a provider failure is retried elsewhere.
    #[must_use]
    pub fn new(inner: Arc<dyn ChatModel<S>>) -> Self {
        Self {
            inner,
            tracer: None,
            agent: String::new(),
        }
    }

    /// Announces each reroute on the operator console.
    ///
    /// A retry that works leaves no other trace: the call simply takes a few
    /// seconds longer and returns, so a provider failing steadily is invisible
    /// until it exhausts the attempts and kills a specialist. The note names
    /// `agent` because several specialists route independently, and knowing
    /// which one is being bounced is most of the diagnosis.
    #[must_use]
    pub fn with_tracer(mut self, tracer: Arc<RunTracer>, agent: impl Into<String>) -> Self {
        self.tracer = Some(tracer);
        self.agent = agent.into();
        self
    }

    /// Reports the reroute about to be attempted.
    fn note(&self, attempt: usize, error: &TinyAgentsError) {
        if let Some(tracer) = self.tracer.as_ref() {
            tracer.note(&format!(
                "{} model PROVIDER FAILED ({error}); rerouting, attempt {} of {}",
                self.agent,
                attempt + 1,
                MAX_REROUTES + 1
            ));
        }
    }

    /// Reports an error this wrapper is passing straight through.
    ///
    /// Everything not worth rerouting is handed back to the harness, whose own
    /// retry ladder then re-issues it. That ladder announces itself as
    /// `model RETRY attempt N` and says nothing about *why*, because upstream's
    /// `AgentEvent::RetryScheduled` carries only a call id and an attempt
    /// number — so a live `pattern_finder` retried one call six times over
    /// three and a half minutes with the cause recorded in neither the console
    /// nor `trace.jsonl`. A repeated retry is a documented stall signal, and it
    /// was the one signal that arrived with nothing to diagnose from.
    ///
    /// This wrapper is outermost, so every provider failure passes through it
    /// exactly once before the ladder sees it. Noting it here is what makes the
    /// retry that follows readable, and it stays cheap for the same reason:
    /// one line per *failed* call, not per call.
    fn note_passthrough(&self, error: &TinyAgentsError) {
        if let Some(tracer) = self.tracer.as_ref() {
            tracer.note(&passthrough_note(&self.agent, error));
        }
    }
}

/// The line a pass-through failure prints.
///
/// Built here rather than inline so the wording can be asserted on. `note`
/// reaches the console and not `trace.jsonl`, so there is no journal to read
/// this back from — and the console is the right target, because
/// `docker logs` is where a stalled run is actually diagnosed.
///
/// Naming the agent is the load-bearing half. Several specialists fail
/// concurrently, so an unattributed cause says a call failed without saying
/// whose turn is about to be retried, which is most of what the reader needs.
fn passthrough_note(agent: &str, error: &TinyAgentsError) -> String {
    format!(
        "{agent} model call failed ({error}); the harness retry ladder decides what happens next"
    )
}

/// Returns whether an error is `OpenRouter` reporting an upstream failure.
///
/// Both halves are load-bearing. The status alone would catch every malformed
/// request, which is permanent and must fail fast. The message alone would
/// catch a genuine 500 that happens to be worded similarly, which the retry
/// ladder underneath already handles on its own terms.
pub(crate) fn upstream_failed(error: &TinyAgentsError) -> bool {
    let TinyAgentsError::Provider(provider) = error else {
        return false;
    };
    provider.status == Some(400)
        && provider
            .message
            .to_ascii_lowercase()
            .contains(UPSTREAM_FAILURE)
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for ReroutingModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        let mut backoff = FIRST_BACKOFF;
        for attempt in 0..MAX_REROUTES {
            match self.inner.invoke(state, request.clone()).await {
                Ok(response) => return Ok(response),
                Err(error) if upstream_failed(&error) => {
                    self.note(attempt, &error);
                    tokio::time::sleep(backoff).await;
                    backoff = backoff.saturating_mul(2);
                }
                Err(error) => {
                    self.note_passthrough(&error);
                    return Err(error);
                }
            }
        }
        // The last attempt is made outside the loop so its error is returned
        // as it stands. A run that has exhausted the reroutes must see the
        // provider's own failure, not a summary of this wrapper's attempts.
        self.inner.invoke(state, request).await
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        let mut backoff = FIRST_BACKOFF;
        for attempt in 0..MAX_REROUTES {
            match self.inner.stream(state, request.clone()).await {
                Ok(stream) => return Ok(stream),
                Err(error) if upstream_failed(&error) => {
                    self.note(attempt, &error);
                    tokio::time::sleep(backoff).await;
                    backoff = backoff.saturating_mul(2);
                }
                Err(error) => {
                    self.note_passthrough(&error);
                    return Err(error);
                }
            }
        }
        self.inner.stream(state, request).await
    }
}

#[cfg(test)]
#[path = "reroute_test.rs"]
mod test;
