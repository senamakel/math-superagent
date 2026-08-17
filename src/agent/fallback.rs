//! Cross-provider failover for OpenAI-compatible model transports.
//!
//! The primary and fallback keep their own clients, base URLs, credentials,
//! model ids, and request defaults. That separation is the control: an
//! `OpenRouter` routing object must never leak into a Surplus request, while a
//! failed Surplus call can still be reissued through `OpenRouter` unchanged.

use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::{Result, TinyAgentsError};

/// A primary model with one independently configured provider fallback.
pub struct ProviderFallbackModel<S: Send + Sync> {
    primary: Arc<dyn ChatModel<S>>,
    fallback: Arc<dyn ChatModel<S>>,
    primary_name: String,
    fallback_name: String,
}

impl<S: Send + Sync> std::fmt::Debug for ProviderFallbackModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("ProviderFallbackModel")
            .field("primary", &self.primary_name)
            .field("fallback", &self.fallback_name)
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> ProviderFallbackModel<S> {
    /// Routes provider and transport failures from `primary` to `fallback`.
    #[must_use]
    pub fn new(
        primary: Arc<dyn ChatModel<S>>,
        primary_name: impl Into<String>,
        fallback: Arc<dyn ChatModel<S>>,
        fallback_name: impl Into<String>,
    ) -> Self {
        Self {
            primary,
            fallback,
            primary_name: primary_name.into(),
            fallback_name: fallback_name.into(),
        }
    }
}

fn should_fallback(error: &TinyAgentsError) -> bool {
    matches!(
        error,
        TinyAgentsError::Model(_) | TinyAgentsError::Provider(_) | TinyAgentsError::Timeout(_)
    )
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for ProviderFallbackModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.primary.profile()
    }

    fn cache_identity(&self) -> Option<String> {
        Some(format!(
            "provider-fallback:{}:{}",
            self.primary.cache_identity()?,
            self.fallback.cache_identity()?
        ))
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        match self.primary.invoke(state, request.clone()).await {
            Ok(response) => Ok(response),
            Err(error) if should_fallback(&error) => self.fallback.invoke(state, request).await,
            Err(error) => Err(error),
        }
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        match self.primary.stream(state, request.clone()).await {
            Ok(stream) => Ok(stream),
            Err(error) if should_fallback(&error) => self.fallback.stream(state, request).await,
            Err(error) => Err(error),
        }
    }
}

#[cfg(test)]
#[path = "fallback_test.rs"]
mod test;
