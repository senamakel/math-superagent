//! Unit tests for re-issuing a turn cut off at the output cap.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::Mutex;

use async_trait::async_trait;
use tinyagents::harness::model::{ChatModel, ModelRequest, ModelResponse, ModelStream};

use crate::agent::Result as ModelResult;

use super::UntruncatedModel;

/// Answers with a scripted sequence and records each request's cap.
struct ScriptedModel {
    replies: Mutex<Vec<ModelResponse>>,
    caps: Arc<Mutex<Vec<Option<u32>>>>,
}

impl ScriptedModel {
    fn new(replies: Vec<ModelResponse>) -> (Arc<Self>, Arc<Mutex<Vec<Option<u32>>>>) {
        let caps = Arc::new(Mutex::new(Vec::new()));
        let model = Arc::new(Self {
            replies: Mutex::new(replies.into_iter().rev().collect()),
            caps: caps.clone(),
        });
        (model, caps)
    }
}

#[async_trait]
impl ChatModel<()> for ScriptedModel {
    async fn invoke(&self, _state: &(), request: ModelRequest) -> ModelResult<ModelResponse> {
        self.caps
            .lock()
            .expect("recorded caps are not poisoned")
            .push(request.max_tokens);
        Ok(self
            .replies
            .lock()
            .expect("scripted replies are not poisoned")
            .pop()
            .unwrap_or_else(|| ModelResponse::assistant("exhausted")))
    }

    async fn stream(&self, _state: &(), _request: ModelRequest) -> ModelResult<ModelStream> {
        Err(tinyagents::TinyAgentsError::Tool(
            "the streaming path is not exercised here".into(),
        ))
    }
}

fn truncated(text: &str) -> ModelResponse {
    let mut response = ModelResponse::assistant(text);
    response.finish_reason = Some("length".into());
    response
}

fn finished(text: &str) -> ModelResponse {
    let mut response = ModelResponse::assistant(text);
    response.finish_reason = Some("stop".into());
    response
}

#[tokio::test]
async fn a_turn_cut_off_mid_answer_is_asked_for_again_with_a_bigger_cap() {
    // The gap upstream leaves: its recovery requires the text to be empty, so
    // a turn that produced half an answer and hit the cap is accepted as the
    // final answer. A live root agent ended its run on exactly that fragment,
    // after the mathematics under it was finished and cross-checked.
    let (inner, caps) = ScriptedModel::new(vec![
        truncated("the answer is S = 4988098253"),
        finished("the answer is S = 498809825393729, verified two ways"),
    ]);
    let model = UntruncatedModel::new(inner);

    let response = model
        .invoke(&(), ModelRequest::new(Vec::new()).with_max_tokens(12_000))
        .await
        .expect("the call succeeds");

    assert!(
        response.text().contains("verified two ways"),
        "{response:?}"
    );
    let caps = caps.lock().expect("recorded caps are not poisoned");
    assert_eq!(caps.as_slice(), &[Some(12_000), Some(24_000)]);
}

#[tokio::test]
async fn a_complete_turn_is_returned_without_a_second_call() {
    let (inner, caps) = ScriptedModel::new(vec![finished("done")]);
    let model = UntruncatedModel::new(inner);

    model
        .invoke(&(), ModelRequest::new(Vec::new()).with_max_tokens(12_000))
        .await
        .expect("the call succeeds");

    assert_eq!(
        caps.lock().expect("recorded caps are not poisoned").len(),
        1,
        "a turn that finished must not be paid for twice"
    );
}

#[tokio::test]
async fn cap_growth_stops_at_four_times_the_original() {
    // A turn needing more than four times its budget is being asked the wrong
    // question, and re-issuing forever would spend the run on one turn.
    let (inner, caps) = ScriptedModel::new(vec![
        truncated("one"),
        truncated("two"),
        truncated("three"),
        truncated("four"),
    ]);
    let model = UntruncatedModel::new(inner);

    let response = model
        .invoke(&(), ModelRequest::new(Vec::new()).with_max_tokens(10_000))
        .await
        .expect("the call succeeds");

    let caps = caps.lock().expect("recorded caps are not poisoned");
    assert_eq!(caps.as_slice(), &[Some(10_000), Some(20_000), Some(40_000)]);
    // Still truncated after the ceiling: the fragment is returned rather than
    // an error, because a truncated answer beats no answer.
    assert_eq!(response.text(), "three");
}

#[tokio::test]
async fn a_request_with_no_cap_of_its_own_is_left_alone() {
    // Nothing to raise, so a re-issue would ask for the identical thing.
    let (inner, caps) = ScriptedModel::new(vec![truncated("half"), finished("whole")]);
    let model = UntruncatedModel::new(inner);

    let response = model
        .invoke(&(), ModelRequest::new(Vec::new()))
        .await
        .expect("the call succeeds");

    assert_eq!(response.text(), "half");
    assert_eq!(
        caps.lock().expect("recorded caps are not poisoned").len(),
        1
    );
}
