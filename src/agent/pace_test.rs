//! Unit tests for the provider departure schedule.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::Mutex;
use std::time::Duration;

use async_trait::async_trait;
use tinyagents::harness::model::{ChatModel, ModelRequest, ModelResponse};
use tokio::time::Instant;

use crate::agent::Result as ModelResult;

use super::PacedModel;

/// A model that records when each call reached it.
struct RecordingModel {
    seen: Arc<Mutex<Vec<Instant>>>,
}

impl RecordingModel {
    fn new() -> (Arc<Self>, Arc<Mutex<Vec<Instant>>>) {
        let seen = Arc::new(Mutex::new(Vec::new()));
        (Arc::new(Self { seen: seen.clone() }), seen)
    }
}

#[async_trait]
impl ChatModel<()> for RecordingModel {
    async fn invoke(&self, _state: &(), _request: ModelRequest) -> ModelResult<ModelResponse> {
        self.seen
            .lock()
            .expect("recorded arrivals are not poisoned")
            .push(Instant::now());
        Ok(ModelResponse::assistant("ok"))
    }
}

fn request() -> ModelRequest {
    ModelRequest::new(Vec::new())
}

#[tokio::test(start_paused = true)]
async fn calls_are_spaced_by_the_configured_interval() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    // Two per second, so the gap under test is half a second.
    let model = Arc::new(PacedModel::new(inner, 2.0, 4));
    let start = Instant::now();

    for _ in 0..4 {
        model.invoke(&(), request()).await?;
    }

    let seen = seen.lock().expect("recorded arrivals are not poisoned");
    assert_eq!(seen.len(), 4);
    for (index, arrival) in seen.iter().enumerate() {
        let expected = Duration::from_millis(500) * u32::try_from(index).unwrap_or(u32::MAX);
        assert_eq!(arrival.duration_since(start), expected);
    }
    Ok(())
}

#[tokio::test(start_paused = true)]
async fn concurrent_callers_depart_on_the_schedule_rather_than_together() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    let model = Arc::new(PacedModel::new(inner, 2.0, 4));
    let start = Instant::now();

    let mut handles = Vec::new();
    for _ in 0..4 {
        let model = model.clone();
        handles.push(tokio::spawn(async move {
            model.invoke(&(), request()).await.map(|_| ())
        }));
    }
    for handle in handles {
        handle.await.expect("the spawned call did not panic")?;
    }

    let mut seen = seen
        .lock()
        .expect("recorded arrivals are not poisoned")
        .clone();
    seen.sort_unstable();
    assert_eq!(seen.len(), 4);
    let last = seen.last().expect("four arrivals were recorded");
    // Three intervals between the first and the fourth departure. Without the
    // schedule all four would leave at once and the account would reject them.
    assert_eq!(last.duration_since(start), Duration::from_millis(1500));
    Ok(())
}

#[tokio::test(start_paused = true)]
async fn a_non_positive_rate_leaves_the_calls_unpaced() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    let model = PacedModel::new(inner, 0.0, 1);
    let start = Instant::now();

    for _ in 0..3 {
        model.invoke(&(), request()).await?;
    }

    let seen = seen.lock().expect("recorded arrivals are not poisoned");
    assert_eq!(seen.len(), 3);
    for arrival in seen.iter() {
        assert_eq!(arrival.duration_since(start), Duration::ZERO);
    }
    Ok(())
}

#[tokio::test(start_paused = true)]
async fn only_one_call_is_in_flight_when_the_concurrency_is_one() -> ModelResult<()> {
    let (inner, seen) = RecordingModel::new();
    let model = Arc::new(PacedModel::new(inner, 1000.0, 1));

    let mut handles = Vec::new();
    for _ in 0..3 {
        let model = model.clone();
        handles.push(tokio::spawn(async move {
            model.invoke(&(), request()).await.map(|_| ())
        }));
    }
    for handle in handles {
        handle.await.expect("the spawned call did not panic")?;
    }

    assert_eq!(
        seen.lock()
            .expect("recorded arrivals are not poisoned")
            .len(),
        3
    );
    Ok(())
}
