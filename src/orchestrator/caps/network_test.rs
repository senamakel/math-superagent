//! Deterministic tests for the deliberately absent network path.
#![allow(clippy::expect_used)]

use super::*;

/// The controls this refusal protects are research gating, the response
/// bounds, and the request ledger — all three of which live in the tools.
#[tokio::test]
async fn an_http_node_is_refused_and_pointed_at_the_supported_path() {
    let error = RefusingHttpClient
        .request(serde_json::json!({ "url": "https://example.invalid" }), None)
        .await
        .expect_err("this host does not make requests from an `http_request` node");
    let rendered = error.to_string();
    assert!(rendered.contains("tool_call"), "{rendered}");
    assert!(rendered.contains("research gating"), "{rendered}");
}
