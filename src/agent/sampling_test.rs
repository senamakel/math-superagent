//! Unit tests for the greedy sampling pair.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::Mutex;

use async_trait::async_trait;
use tinyagents::harness::model::{ChatModel, ModelRequest, ModelResponse};

use crate::agent::Result as ModelResult;

use super::GreedySamplingModel;

/// The `(temperature, top_p)` pairs a wrapped model was handed.
type Seen = Arc<Mutex<Vec<(Option<f64>, Option<f64>)>>>;

/// A model that records the sampling parameters it was handed.
struct RecordingModel {
    seen: Seen,
}

impl RecordingModel {
    fn new() -> (Arc<Self>, Seen) {
        let seen = Arc::new(Mutex::new(Vec::new()));
        (Arc::new(Self { seen: seen.clone() }), seen)
    }
}

#[async_trait]
impl ChatModel<()> for RecordingModel {
    async fn invoke(&self, _state: &(), request: ModelRequest) -> ModelResult<ModelResponse> {
        self.seen
            .lock()
            .expect("recorded requests are not poisoned")
            .push((request.temperature, request.top_p));
        Ok(ModelResponse::assistant("ok"))
    }
}

fn request() -> ModelRequest {
    ModelRequest::new(Vec::new())
}

#[tokio::test]
async fn an_unset_pair_becomes_greedy_with_the_top_p_the_provider_requires() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    let model = GreedySamplingModel::new(inner);

    model.invoke(&(), request()).await?;

    let seen = seen.lock().expect("recorded requests are not poisoned");
    assert_eq!(seen.as_slice(), [(Some(0.0), Some(1.0))]);
    Ok(())
}

#[tokio::test]
async fn a_zero_temperature_gains_the_top_p_that_makes_it_legal() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    let model = GreedySamplingModel::new(inner);

    model.invoke(&(), request().with_temperature(0.0)).await?;

    let seen = seen.lock().expect("recorded requests are not poisoned");
    assert_eq!(seen.as_slice(), [(Some(0.0), Some(1.0))]);
    Ok(())
}

#[tokio::test]
async fn a_caller_that_chose_a_top_p_keeps_it() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    let model = GreedySamplingModel::new(inner);

    model.invoke(&(), request().with_top_p(0.95)).await?;

    let seen = seen.lock().expect("recorded requests are not poisoned");
    assert_eq!(seen.as_slice(), [(None, Some(0.95))]);
    Ok(())
}

#[tokio::test]
async fn a_request_that_asks_for_sampling_is_left_alone() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    let model = GreedySamplingModel::new(inner);

    model.invoke(&(), request().with_temperature(1.0)).await?;

    let seen = seen.lock().expect("recorded requests are not poisoned");
    assert_eq!(seen.as_slice(), [(Some(1.0), None)]);
    Ok(())
}
