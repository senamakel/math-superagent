//! Sampling parameters a provider requires as a pair.
//!
//! Mistral refuses greedy sampling unless `top_p` is sent as 1 alongside it:
//! HTTP 400, `code 3054`, `top_p must be 1 when using greedy sampling`.
//! Verified live against `labs-leanstral-1-5` — a bare `temperature: 0` is
//! rejected, and the same request with `top_p: 1` succeeds.
//!
//! The vendored builder cannot express this. `temperature` has an override
//! (`with_temperature_override`) but `top_p` does not, and the provider-options
//! escape hatch is no help either: both names are in the `RESERVED` list that
//! `provider_extra_options` filters out before anything reaches the wire. So
//! the only seam is the `ModelRequest`, which is what this wraps.
//!
//! Both halves are set here rather than one here and one at the builder,
//! because the constraint is on the *pair*: splitting them across two layers is
//! exactly how they would come apart, and the failure is a 400 on every call.

use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::Result;

/// Pins the greedy sampling pair on requests that have not chosen one.
///
/// Wraps a model whose provider requires `top_p == 1` whenever `temperature`
/// is zero. A request that already names a `top_p`, or that asks for genuine
/// sampling with a non-zero `temperature`, passes through untouched — the
/// wrapper supplies a default, it does not impose a policy.
pub struct GreedySamplingModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
}

impl<S: Send + Sync> std::fmt::Debug for GreedySamplingModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("GreedySamplingModel")
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> GreedySamplingModel<S> {
    /// Wraps `inner` so greedy requests carry the `top_p` its provider needs.
    #[must_use]
    pub fn new(inner: Arc<dyn ChatModel<S>>) -> Self {
        Self { inner }
    }

    /// Completes the sampling pair when the request left it open.
    ///
    /// An unset `temperature` counts as greedy: nothing in this crate sets one
    /// today, so the default path is the deterministic one, which is what a
    /// formalisation wants.
    fn pair(request: ModelRequest) -> ModelRequest {
        if request.top_p.is_some() {
            return request;
        }
        match request.temperature {
            None => request.with_temperature(0.0).with_top_p(1.0),
            Some(0.0) => request.with_top_p(1.0),
            Some(_) => request,
        }
    }
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for GreedySamplingModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        self.inner.invoke(state, Self::pair(request)).await
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        self.inner.stream(state, Self::pair(request)).await
    }
}

#[cfg(test)]
#[path = "sampling_test.rs"]
mod test;
