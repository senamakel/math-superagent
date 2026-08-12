//! Per-call provider, model, token, and cost accounting.
//!
//! The event stream cannot answer the questions an operator actually asks
//! after a long run. `ModelCompleted` carries token counts, but it names
//! neither the provider that served the call nor what it cost. With
//! `allow_fallbacks` enabled the provider genuinely varies from call to call,
//! so "which route did this run use, was the affinity holding, and what did
//! the investigation cost" could not be answered from `trace.jsonl` at all.
//!
//! All four figures are in the provider's response body — `OpenRouter`
//! reports `provider`, `model`, and a `usage` object carrying `cost` on every
//! response — so they are read here, in a model wrapper, rather than derived
//! from an event that never saw the body.
//!
//! Cost is recorded as the provider reports it. Deriving it from a local price
//! table would mean maintaining prices per model per provider and silently
//! reporting fiction whenever one changed.

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::Value;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::Result;
use crate::agent::trace::{ModelAccounting, RunTracer};

/// Wraps a chat model so every call is accounted for in the trace.
pub struct AccountingModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    /// The agent whose calls this wrapper is reporting.
    agent: String,
    tracer: Arc<RunTracer>,
}

impl<S: Send + Sync> std::fmt::Debug for AccountingModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("AccountingModel")
            .field("agent", &self.agent)
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> AccountingModel<S> {
    /// Wraps `inner`, reporting its calls as `agent`.
    #[must_use]
    pub fn new(
        inner: Arc<dyn ChatModel<S>>,
        agent: impl Into<String>,
        tracer: Arc<RunTracer>,
    ) -> Self {
        Self {
            inner,
            agent: agent.into(),
            tracer,
        }
    }

    fn record(&self, response: &ModelResponse) {
        let Some(raw) = response.raw.as_ref() else {
            // The streaming path discards the body, and a mock has none. A
            // missing record is better than a fabricated one.
            return;
        };
        self.tracer
            .record_model_cost(&accounting_from(&self.agent, raw));
    }
}

/// Reads the accounting figures out of a provider response body.
pub(crate) fn accounting_from(agent: &str, raw: &Value) -> ModelAccounting {
    let usage = raw.get("usage");
    let number = |parent: Option<&Value>, key: &str| -> u64 {
        parent
            .and_then(|value| value.get(key))
            .and_then(Value::as_u64)
            .unwrap_or_default()
    };
    let nested =
        |key: &str, child: &str| -> u64 { number(usage.and_then(|usage| usage.get(key)), child) };

    ModelAccounting {
        agent: agent.to_string(),
        provider: text(raw, "provider"),
        model: text(raw, "model"),
        input_tokens: number(usage, "prompt_tokens"),
        cached_tokens: nested("prompt_tokens_details", "cached_tokens"),
        output_tokens: number(usage, "completion_tokens"),
        reasoning_tokens: nested("completion_tokens_details", "reasoning_tokens"),
        usd: usage
            .and_then(|usage| usage.get("cost"))
            .and_then(Value::as_f64)
            .unwrap_or_default(),
    }
}

fn text(raw: &Value, key: &str) -> Option<String> {
    raw.get(key)
        .and_then(Value::as_str)
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .map(str::to_string)
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for AccountingModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        let response = self.inner.invoke(state, request).await?;
        self.record(&response);
        Ok(response)
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        self.inner.stream(state, request).await
    }
}

#[cfg(test)]
#[path = "accounting_test.rs"]
mod test;
