//! Per-agent provider affinity, so a run keeps hitting the prompt cache.
//!
//! `OpenRouter` prompt caching is per provider. These agents carry a large
//! fixed prefix — the method policy, the role prompt, and the workspace
//! context — so a turn served by the provider that served the previous turn
//! reads most of that prefix from cache, and a turn served by a different one
//! re-sends all of it at full price.
//!
//! Preferring a single provider through `provider.order` gets most of the way
//! there, but not all of it: `allow_fallbacks` is deliberately on, so a busy
//! preferred provider cannot stall the runtime. Every fallback then costs
//! twice — once for the cold call on the new provider, and again on the next
//! turn when routing swings back to the preferred one and finds *its* cache
//! cold too. A run can oscillate between two providers and never cache at all.
//!
//! This wrapper closes that gap. It watches which provider actually served
//! each response and pins subsequent requests to that one. The pin is a
//! preference, not an exclusion: `allow_fallbacks` stays on, so a provider
//! that goes away is routed around and simply becomes the new pin. An
//! exclusive `provider.only` pin was tried and left requests hanging for
//! minutes while other providers serving the same model sat idle.
//!
//! Affinity is per wrapper instance, and the registry gives each specialist
//! its own. That is the right grain: agents differ in their prefix, so they
//! have nothing to gain from sharing a provider, and pinning them together
//! would make one agent's fallback evict every other agent's cache.
//!
//! A pin that survived a failed request would undo all of that. A provider
//! that accepts a connection and then never answers is not "unavailable", so
//! `allow_fallbacks` does not route around it: the retry reads the pin, asks
//! for the same provider first, and hangs again. Three runs did exactly this
//! at once — each sat out the full seven-minute request timeout, retried, and
//! went straight back to the provider that had just failed to answer. So a
//! failure hands the pin to `blocked`, and the *next* request asks
//! `OpenRouter` to route anywhere but there.
//!
//! That diversion lasts exactly one request. A block held until the next
//! success would be a slow way to strand a run: if the failure was not the
//! provider's fault, or the model is served by that provider alone, an
//! indefinite exclusion turns a recoverable stall into a run that cannot
//! reach the model at all.

use std::sync::Arc;
use std::sync::RwLock;

use async_trait::async_trait;
use serde_json::{Value, json};
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::Result;

/// Wraps a chat model so one agent keeps returning to one provider.
pub struct StickyProviderModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    /// The provider that served this agent's most recent response.
    pinned: Arc<RwLock<Option<String>>>,
    /// A provider whose request just failed, to be skipped once.
    blocked: Arc<RwLock<Option<String>>>,
}

impl<S: Send + Sync> std::fmt::Debug for StickyProviderModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("StickyProviderModel")
            .field("pinned", &self.pinned())
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> StickyProviderModel<S> {
    /// Wraps `inner` with its own provider affinity.
    #[must_use]
    pub fn new(inner: Arc<dyn ChatModel<S>>) -> Self {
        Self {
            inner,
            pinned: Arc::new(RwLock::new(None)),
            blocked: Arc::new(RwLock::new(None)),
        }
    }

    /// Returns the provider this agent is currently pinned to, if any.
    #[must_use]
    pub fn pinned(&self) -> Option<String> {
        self.pinned.read().ok().and_then(|slug| slug.clone())
    }

    /// Applies the pin to a request, leaving an explicit choice alone.
    ///
    /// A caller that set `provider` itself outranks the affinity: the pin is
    /// an optimisation, and silently overriding a deliberate route would make
    /// the escape hatch useless.
    fn steer(&self, request: ModelRequest) -> ModelRequest {
        if request.provider_options.get("provider").is_some() {
            return request;
        }
        // A provider that just failed is skipped for one request. That takes
        // priority over the pin, because after a failure they name the same
        // provider and following the pin is what hangs.
        let choice = match self.take_blocked() {
            Some(blocked) => json!({ "ignore": [blocked], "allow_fallbacks": true }),
            None => match self.pinned() {
                Some(provider) => json!({ "order": [provider], "allow_fallbacks": true }),
                None => return request,
            },
        };
        let mut options = match request.provider_options.clone() {
            Value::Object(map) => map,
            _ => serde_json::Map::new(),
        };
        options.insert("provider".to_string(), choice);
        request.with_provider_options(Value::Object(options))
    }

    /// Consumes the one-request exclusion, if one is set.
    fn take_blocked(&self) -> Option<String> {
        self.blocked.write().ok()?.take()
    }

    /// Records that the pinned provider failed to answer.
    ///
    /// The pin is cleared as well as blocked, so a request after the diverted
    /// one asks for nothing in particular rather than returning to a route
    /// that has not answered since.
    fn fault(&self) {
        let Some(provider) = self.pinned() else {
            return;
        };
        if let Ok(mut slot) = self.blocked.write() {
            *slot = Some(provider);
        }
        if let Ok(mut slot) = self.pinned.write() {
            *slot = None;
        }
    }

    /// Records the provider that served a response.
    ///
    /// `OpenRouter` names it in the response body. Nothing else in the
    /// response identifies the route, so a body without it — a provider that
    /// does not report one, or the streaming path, which discards the raw
    /// body — simply leaves the previous pin in place rather than clearing it.
    fn observe(&self, response: &ModelResponse) {
        let Some(provider) = response
            .raw
            .as_ref()
            .and_then(|raw| raw.get("provider"))
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|provider| !provider.is_empty())
        else {
            return;
        };
        if self.pinned().as_deref() == Some(provider) {
            return;
        }
        if let Ok(mut slot) = self.pinned.write() {
            *slot = Some(provider.to_string());
        }
    }
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for StickyProviderModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        let response = match self.inner.invoke(state, self.steer(request)).await {
            Ok(response) => response,
            Err(error) => {
                self.fault();
                return Err(error);
            }
        };
        self.observe(&response);
        Ok(response)
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        // The streaming path cannot learn a pin, because the accumulated
        // terminal response carries no raw body. It can still honour one, and
        // a stream that fails to open is the same evidence as a failed call.
        match self.inner.stream(state, self.steer(request)).await {
            Ok(stream) => Ok(stream),
            Err(error) => {
                self.fault();
                Err(error)
            }
        }
    }
}

#[cfg(test)]
#[path = "sticky_test.rs"]
mod test;
