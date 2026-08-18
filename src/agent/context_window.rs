//! Model wrapper for endpoints whose context size is known out of band.

use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::Result;

/// Delegates model calls while publishing an explicit context window.
pub(super) struct ContextWindowModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    profile: ModelProfile,
}

impl<S: Send + Sync> ContextWindowModel<S> {
    /// Wraps `inner` and replaces only its advertised input-token ceiling.
    pub(super) fn new(inner: Arc<dyn ChatModel<S>>, max_input_tokens: u64) -> Self {
        let mut profile = inner.profile().cloned().unwrap_or_default();
        profile.max_input_tokens = Some(max_input_tokens);
        Self { inner, profile }
    }
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for ContextWindowModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        Some(&self.profile)
    }

    fn cache_identity(&self) -> Option<String> {
        self.inner.cache_identity()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        self.inner.invoke(state, request).await
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        self.inner.stream(state, request).await
    }
}
