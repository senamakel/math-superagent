//! Unit tests for per-agent provider affinity.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::Mutex;

use async_trait::async_trait;
use serde_json::{Value, json};
use tinyagents::harness::model::{
    ChatModel, ModelRequest, ModelResponse, ModelStream, Result as ModelResult,
};

use super::StickyProviderModel;

/// A model that records the provider options it was asked for and answers with
/// a body naming the provider that "served" the call.
struct RecordingModel {
    served_by: Mutex<Vec<Option<String>>>,
    seen: Arc<Mutex<Vec<Value>>>,
}

impl RecordingModel {
    fn new(served_by: Vec<Option<&str>>) -> (Arc<Self>, Arc<Mutex<Vec<Value>>>) {
        let seen = Arc::new(Mutex::new(Vec::new()));
        let model = Arc::new(Self {
            served_by: Mutex::new(
                served_by
                    .into_iter()
                    .rev()
                    .map(|slug| slug.map(str::to_string))
                    .collect(),
            ),
            seen: seen.clone(),
        });
        (model, seen)
    }
}

#[async_trait]
impl ChatModel<()> for RecordingModel {
    async fn invoke(&self, _state: &(), request: ModelRequest) -> ModelResult<ModelResponse> {
        self.seen
            .lock()
            .expect("recorded requests are not poisoned")
            .push(request.provider_options.clone());
        let served = self
            .served_by
            .lock()
            .expect("scripted providers are not poisoned")
            .pop()
            .flatten();
        let mut response = ModelResponse::assistant("ok");
        if let Some(served) = served {
            response.raw = Some(json!({ "provider": served }));
        }
        Ok(response)
    }

    async fn stream(&self, _state: &(), _request: ModelRequest) -> ModelResult<ModelStream> {
        unimplemented!("the sticky wrapper's streaming path is not exercised here")
    }
}

fn ordered_provider(options: &Value) -> Option<&str> {
    options
        .get("provider")?
        .get("order")?
        .get(0)?
        .as_str()
}

#[tokio::test]
async fn the_first_call_is_unsteered_and_later_calls_follow_the_provider_that_served_it() {
    let (inner, seen) = RecordingModel::new(vec![Some("deepinfra"), Some("deepinfra")]);
    let sticky = StickyProviderModel::new(inner);

    sticky
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the first call succeeds");
    sticky
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the second call succeeds");

    let seen = seen.lock().expect("recorded requests are not poisoned");
    // Nothing is known before the first response, so the baked preference on
    // the underlying model is left to do its job.
    assert_eq!(ordered_provider(&seen[0]), None);
    assert_eq!(ordered_provider(&seen[1]), Some("deepinfra"));
    assert_eq!(sticky.pinned().as_deref(), Some("deepinfra"));
}

#[tokio::test]
async fn a_fallback_moves_the_pin_instead_of_oscillating_back() {
    // The preferred provider serves the first call, a fallback serves the
    // second. Without re-pinning, the third call would route back to the
    // preferred provider and find its cache cold — the oscillation this
    // wrapper exists to stop.
    let (inner, seen) = RecordingModel::new(vec![Some("deepinfra"), Some("novita"), Some("novita")]);
    let sticky = StickyProviderModel::new(inner);

    for _ in 0..3 {
        sticky
            .invoke(&(), ModelRequest::new(Vec::new()))
            .await
            .expect("each call succeeds");
    }

    let seen = seen.lock().expect("recorded requests are not poisoned");
    assert_eq!(ordered_provider(&seen[1]), Some("deepinfra"));
    assert_eq!(ordered_provider(&seen[2]), Some("novita"));
    assert_eq!(sticky.pinned().as_deref(), Some("novita"));
}

#[tokio::test]
async fn the_pin_never_excludes_other_providers() {
    // An exclusive pin previously left requests hanging while other providers
    // serving the same model sat idle. Affinity must stay a preference.
    let (inner, seen) = RecordingModel::new(vec![Some("deepinfra"), Some("deepinfra")]);
    let sticky = StickyProviderModel::new(inner);

    sticky
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the first call succeeds");
    sticky
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the second call succeeds");

    let seen = seen.lock().expect("recorded requests are not poisoned");
    let provider = seen[1].get("provider").expect("the pin was applied");
    assert_eq!(provider.get("allow_fallbacks"), Some(&json!(true)));
    assert!(provider.get("only").is_none(), "{provider}");
}

#[tokio::test]
async fn a_response_without_a_named_provider_leaves_the_pin_alone() {
    let (inner, seen) = RecordingModel::new(vec![Some("deepinfra"), None, Some("deepinfra")]);
    let sticky = StickyProviderModel::new(inner);

    for _ in 0..3 {
        sticky
            .invoke(&(), ModelRequest::new(Vec::new()))
            .await
            .expect("each call succeeds");
    }

    let seen = seen.lock().expect("recorded requests are not poisoned");
    assert_eq!(ordered_provider(&seen[2]), Some("deepinfra"));
}

#[tokio::test]
async fn an_explicit_provider_choice_outranks_the_pin() {
    let (inner, seen) = RecordingModel::new(vec![Some("deepinfra"), Some("deepinfra")]);
    let sticky = StickyProviderModel::new(inner);

    sticky
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the first call succeeds");
    sticky
        .invoke(
            &(),
            ModelRequest::new(Vec::new())
                .with_provider_options(json!({ "provider": { "order": ["chosen"] } })),
        )
        .await
        .expect("the second call succeeds");

    let seen = seen.lock().expect("recorded requests are not poisoned");
    assert_eq!(ordered_provider(&seen[1]), Some("chosen"));
}

#[tokio::test]
async fn each_agent_keeps_its_own_affinity() {
    // Agents differ in their cached prefix, so sharing one pin would let one
    // agent's fallback evict every other agent's cache.
    let (inner, _) = RecordingModel::new(vec![Some("deepinfra"), Some("novita")]);
    let first = StickyProviderModel::new(inner.clone());
    let second = StickyProviderModel::new(inner);

    first
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the first agent's call succeeds");
    second
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the second agent's call succeeds");

    assert_eq!(first.pinned().as_deref(), Some("deepinfra"));
    assert_eq!(second.pinned().as_deref(), Some("novita"));
}
