//! Unit tests for the hello-world agent's deterministic tools.

use serde_json::json;

use super::{AddTool, EchoTool};
use crate::agent::{Tool, ToolCall};

#[tokio::test]
async fn adds_two_numbers() -> crate::agent::Result<()> {
    let result = AddTool
        .call(&(), ToolCall::new("add-1", "add_numbers", json!({"a": 20, "b": 22})))
        .await?;

    assert_eq!(result.content, "42");
    Ok(())
}

#[tokio::test]
async fn echoes_text() -> crate::agent::Result<()> {
    let result = EchoTool
        .call(&(), ToolCall::new("echo-1", "echo_text", json!({"text": "hello"})))
        .await?;

    assert_eq!(result.content, "hello");
    Ok(())
}

#[tokio::test]
async fn rejects_missing_add_argument() {
    let result = AddTool
        .call(&(), ToolCall::new("add-2", "add_numbers", json!({"a": 1})))
        .await;

    assert!(result.is_err());
}
