//! Unit tests for re-issuing a turn cut off at the output cap.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::Mutex;

use async_trait::async_trait;
use tinyagents::harness::message::Message;
use tinyagents::harness::model::{ChatModel, ModelRequest, ModelResponse, ModelStream};

use crate::agent::Result as ModelResult;

use super::UntruncatedModel;

/// The output cap each request carried, in call order.
type RecordedCaps = Arc<Mutex<Vec<Option<u32>>>>;

/// Answers with a scripted sequence and records each request's cap.
struct ScriptedModel {
    replies: Mutex<Vec<ModelResponse>>,
    caps: RecordedCaps,
}

impl ScriptedModel {
    fn new(replies: Vec<ModelResponse>) -> (Arc<Self>, RecordedCaps) {
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
async fn a_turn_that_truncates_again_is_not_escalated_a_second_time() {
    // The second doubling was measured and was pure cost: a live turn that
    // truncated at twice its cap went on to spend 22.8 minutes generating the
    // full 48,000 tokens and still emitted no tool call, while the *first*
    // doubling is what unblocked a stuck run. Generation time is linear in
    // output length, so the third attempt is the most expensive and the least
    // likely to work.
    let (inner, caps) =
        ScriptedModel::new(vec![truncated("one"), truncated("two"), truncated("three")]);
    let model = UntruncatedModel::new(inner);

    let response = model
        .invoke(&(), ModelRequest::new(Vec::new()).with_max_tokens(10_000))
        .await
        .expect("the call succeeds");

    let caps = caps.lock().expect("recorded caps are not poisoned");
    assert_eq!(
        caps.as_slice(),
        &[Some(10_000), Some(20_000)],
        "one re-issue at twice the cap, and no more"
    );
    // Still truncated after the single re-issue: the fragment is returned
    // rather than an error, because a truncated answer beats no answer, and
    // upstream's own recovery still has its ladder.
    assert_eq!(response.text(), "two");
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

#[tokio::test]
async fn a_reissued_turn_keeps_the_cap_it_was_cut_off_at() {
    // Measuring the reasoning channel removed the doubling. Every turn that
    // reached the old doubled ceiling reported `out=24000` against
    // `reasoning_tokens=23999` — one visible token — so it was not short of
    // room, and a larger budget bought a longer silence and a second full
    // generation to pay for it. The room now lives in `RunBudget`'s 48,000 cap.
    let (inner, caps) = ScriptedModel::new(vec![truncated("cut off"), finished("done")]);
    let model = UntruncatedModel::new(inner);

    let response = model
        .invoke(&(), ModelRequest::new(Vec::new()).with_max_tokens(12_000))
        .await
        .expect("a cut-off turn is asked again");

    assert_eq!(response.text(), "done");
    assert_eq!(
        *caps.lock().expect("recorded caps are not poisoned"),
        vec![Some(12_000), Some(12_000)],
        "the re-issue carries the reason, not a bigger budget"
    );
}

#[test]
fn a_reissued_turn_is_told_its_last_one_was_discarded() {
    // More room alone is not the fix. `cut_off` already requires no tool call
    // at all, and a turn doing genuine long work emits tool calls — so what
    // reaches this wrapper is a model writing an essay, and doubling its budget
    // buys a longer essay. PE236's `tool_builder` truncated at 12,000, was
    // re-issued at 24,000, and had produced nothing five minutes later.
    let request = ModelRequest::new(vec![Message::user("solve it")]).with_max_tokens(12_000);
    let retry = super::reissued(&request, 24_000);

    assert_eq!(retry.max_tokens, Some(24_000), "the room is still given");
    assert_eq!(
        retry.messages.len(),
        request.messages.len() + 1,
        "exactly one message is added"
    );

    // Appended, not prepended: it must be the most recent thing said rather
    // than one more line of standing policy at the top of a long prompt.
    let last = retry.messages.last().expect("the appended instruction");
    let rendered = format!("{last:?}").to_ascii_lowercase();
    assert!(
        rendered.contains("produced nothing"),
        "the model must be told the turn was discarded: {rendered}"
    );
    assert!(
        rendered.contains("call a tool"),
        "and what to do instead: {rendered}"
    );
    // The original request must not be mutated — it is re-used on the
    // non-truncated path and by the caller's own retry ladder.
    assert_eq!(request.messages.len(), 1);
    assert_eq!(request.max_tokens, Some(12_000));
}
