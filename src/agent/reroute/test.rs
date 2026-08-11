//! Unit tests for rerouting around an upstream provider failure.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::Mutex;

use async_trait::async_trait;
use tinyagents::TinyAgentsError;
use tinyagents::harness::model::{
    ChatModel, ModelRequest, ModelResponse, ModelStream, ProviderError,
};

use crate::agent::Result as ModelResult;

use super::{ReroutingModel, upstream_failed};

/// Builds the error `OpenRouter` raises when the provider it chose failed.
fn upstream(message: &str) -> TinyAgentsError {
    TinyAgentsError::Provider(Box::new(ProviderError {
        provider: "openrouter".to_string(),
        model: None,
        status: Some(400),
        code: None,
        message: message.to_string(),
        retryable: false,
        retry_after_ms: None,
    }))
}

/// A model that fails a scripted number of times before answering.
struct FlakyModel {
    /// Errors to raise, in order, before the first success.
    failures: Mutex<Vec<TinyAgentsError>>,
    calls: Mutex<usize>,
}

impl FlakyModel {
    fn new(failures: Vec<TinyAgentsError>) -> Arc<Self> {
        Arc::new(Self {
            failures: Mutex::new(failures.into_iter().rev().collect()),
            calls: Mutex::new(0),
        })
    }

    fn calls(&self) -> usize {
        *self.calls.lock().expect("the call counter is not poisoned")
    }

    fn next(&self) -> Option<TinyAgentsError> {
        *self.calls.lock().expect("the call counter is not poisoned") += 1;
        self.failures
            .lock()
            .expect("scripted failures are not poisoned")
            .pop()
    }
}

#[async_trait]
impl ChatModel<()> for FlakyModel {
    async fn invoke(&self, _state: &(), _request: ModelRequest) -> ModelResult<ModelResponse> {
        match self.next() {
            Some(error) => Err(error),
            None => Ok(ModelResponse::assistant("ok")),
        }
    }

    async fn stream(&self, _state: &(), _request: ModelRequest) -> ModelResult<ModelStream> {
        match self.next() {
            Some(error) => Err(error),
            None => Err(TinyAgentsError::Tool("no stream is scripted here".into())),
        }
    }
}

#[test]
fn an_upstream_provider_failure_is_recognised_by_status_and_message() {
    assert!(upstream_failed(&upstream("Provider returned error")));
    // Case is the provider's to choose and must not decide the classification.
    assert!(upstream_failed(&upstream("provider returned error")));
}

#[test]
fn a_malformed_request_is_not_rerouted() {
    // A real request-shape 400 is permanent. Retrying it would replace a fast
    // honest failure with a slow identical one.
    assert!(!upstream_failed(&upstream(
        "Invalid value for 'tool_choice'"
    )));
    // A 500 worded the same way belongs to the retry ladder underneath, which
    // classifies it as retryable on its own terms.
    assert!(!upstream_failed(&TinyAgentsError::Provider(Box::new(
        ProviderError {
            provider: "openrouter".to_string(),
            model: None,
            status: Some(500),
            code: None,
            message: "Provider returned error".to_string(),
            retryable: true,
            retry_after_ms: None,
        }
    ))));
    // A failure with no structure at all cannot be classified this way.
    assert!(!upstream_failed(&TinyAgentsError::Model(
        "openrouter returned HTTP 400: Provider returned error".into()
    )));
}

#[tokio::test]
async fn a_provider_failure_is_retried_rather_than_ending_the_run() {
    // The failure this exists to stop: a specialist meeting this on its first
    // turn dies before doing anything, and the solution loop records the
    // attempt that delegated to it as having executed nothing.
    let inner = FlakyModel::new(vec![upstream("Provider returned error")]);
    let model = ReroutingModel::new(inner.clone());

    let response = model
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("a rerouted call answers");

    assert_eq!(response.text().trim(), "ok");
    assert_eq!(inner.calls(), 2, "the call is made again after the failure");
}

#[tokio::test]
async fn a_provider_failing_every_time_returns_its_own_error() {
    // Three attempts in total, and the caller sees the provider's failure as
    // it stands rather than a summary of this wrapper's attempts — the run
    // and the reflection after it both reason about the real message.
    let inner = FlakyModel::new(vec![
        upstream("Provider returned error"),
        upstream("Provider returned error"),
        upstream("Provider returned error"),
    ]);
    let model = ReroutingModel::new(inner.clone());

    let error = model
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect_err("an unroutable model still fails");

    assert!(upstream_failed(&error), "the provider's error is preserved");
    assert_eq!(inner.calls(), 3, "one call plus two reroutes");
}

#[tokio::test]
async fn any_other_failure_is_returned_immediately() {
    let inner = FlakyModel::new(vec![TinyAgentsError::Model("connection reset".into())]);
    let model = ReroutingModel::new(inner.clone());

    model
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect_err("an unrelated failure is not swallowed");

    assert_eq!(inner.calls(), 1, "no reroute is spent on it");
}
