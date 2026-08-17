//! Unit tests for provider-boundary fallback.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::atomic::{AtomicUsize, Ordering};

use async_trait::async_trait;
use tinyagents::harness::message::Message;
use tinyagents::harness::model::{ChatModel, ModelRequest, ModelResponse, ProviderError};

use super::ProviderFallbackModel;
use crate::agent::{Result, TinyAgentsError};

#[derive(Debug)]
struct ScriptedModel {
    calls: Arc<AtomicUsize>,
    result: Result<&'static str>,
}

#[async_trait]
impl ChatModel<()> for ScriptedModel {
    async fn invoke(&self, _state: &(), _request: ModelRequest) -> Result<ModelResponse> {
        self.calls.fetch_add(1, Ordering::Relaxed);
        match &self.result {
            Ok(text) => Ok(ModelResponse::assistant(*text)),
            Err(TinyAgentsError::Provider(error)) => Err(TinyAgentsError::Provider(error.clone())),
            Err(TinyAgentsError::Validation(error)) => {
                Err(TinyAgentsError::Validation(error.clone()))
            }
            Err(error) => Err(TinyAgentsError::Model(error.to_string())),
        }
    }
}

fn request() -> ModelRequest {
    ModelRequest::new(vec![Message::user("hello")])
}

fn model(result: Result<&'static str>) -> (Arc<dyn ChatModel<()>>, Arc<AtomicUsize>) {
    let calls = Arc::new(AtomicUsize::new(0));
    (
        Arc::new(ScriptedModel {
            calls: calls.clone(),
            result,
        }),
        calls,
    )
}

#[tokio::test]
async fn a_successful_primary_never_spends_the_fallback() -> Result<()> {
    let (primary, primary_calls) = model(Ok("primary"));
    let (fallback, fallback_calls) = model(Ok("fallback"));
    let route = ProviderFallbackModel::new(primary, "surplus", fallback, "openrouter");

    let response = route.invoke(&(), request()).await?;

    assert_eq!(response.text(), "primary");
    assert_eq!(primary_calls.load(Ordering::Relaxed), 1);
    assert_eq!(fallback_calls.load(Ordering::Relaxed), 0);
    Ok(())
}

#[tokio::test]
async fn a_provider_failure_moves_to_openrouter_once() -> Result<()> {
    let failure = ProviderError {
        provider: "surplus".to_string(),
        model: Some("deepseek-v4-flash-0731".to_string()),
        status: Some(503),
        code: Some("no_healthy_sellers".to_string()),
        message: "all sellers are unhealthy".to_string(),
        retryable: true,
        retry_after_ms: None,
        raw: None,
    };
    let (primary, primary_calls) = model(Err(TinyAgentsError::Provider(Box::new(failure))));
    let (fallback, fallback_calls) = model(Ok("fallback"));
    let route = ProviderFallbackModel::new(primary, "surplus", fallback, "openrouter");

    let response = route.invoke(&(), request()).await?;

    assert_eq!(response.text(), "fallback");
    assert_eq!(primary_calls.load(Ordering::Relaxed), 1);
    assert_eq!(fallback_calls.load(Ordering::Relaxed), 1);
    Ok(())
}

#[tokio::test]
async fn a_caller_validation_error_is_not_sent_to_a_second_provider() {
    let (primary, primary_calls) = model(Err(TinyAgentsError::Validation("bad request".into())));
    let (fallback, fallback_calls) = model(Ok("fallback"));
    let route = ProviderFallbackModel::new(primary, "surplus", fallback, "openrouter");

    let error = route
        .invoke(&(), request())
        .await
        .expect_err("a caller error remains an error");

    assert!(matches!(error, TinyAgentsError::Validation(_)));
    assert_eq!(primary_calls.load(Ordering::Relaxed), 1);
    assert_eq!(fallback_calls.load(Ordering::Relaxed), 0);
}
