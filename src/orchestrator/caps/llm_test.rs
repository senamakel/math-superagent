//! Deterministic tests for the single-turn completion provider.
#![allow(clippy::expect_used)]

use super::*;
use crate::agent::MockModel;

fn provider(reply: &str) -> SingleTurnModel {
    SingleTurnModel::new(Arc::new(MockModel::constant(reply)))
}

#[tokio::test]
async fn a_prompt_becomes_one_turn_and_comes_back_as_text() {
    let value = provider("the answer")
        .complete(json!({ "prompt": "ask something" }), None)
        .await
        .expect("a prompt is a valid completion request");
    // `text` is the key the agent node reads a completion out of, so a
    // downstream node binds `=item.text` either way.
    assert_eq!(value["text"], json!("the answer"));
}

/// A caller that built a conversation meant it; sending the single prompt
/// instead would drop the history without saying so.
#[tokio::test]
async fn a_messages_array_wins_over_a_bare_prompt() {
    let value = provider("ok")
        .complete(
            json!({
                "prompt": "ignored",
                "messages": [
                    { "role": "system", "content": "be terse" },
                    { "role": "user", "content": "go" }
                ]
            }),
            None,
        )
        .await
        .expect("a conversation is a valid completion request");
    assert_eq!(value["text"], json!("ok"));
}

/// An empty turn costs a provider call to produce nothing, so it is refused
/// before the call rather than after it.
#[tokio::test]
async fn a_config_with_nothing_to_say_is_refused_before_the_call() {
    for config in [json!({}), json!({ "prompt": "   " }), json!({ "messages": [] })] {
        let error = provider("unused")
            .complete(config.clone(), None)
            .await
            .expect_err("an empty turn is refused");
        assert!(error.to_string().contains("prompt"), "{config}: {error}");
    }
}
