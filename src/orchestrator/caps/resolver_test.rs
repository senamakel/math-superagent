//! Deterministic tests for the absent workflow catalog.
#![allow(clippy::expect_used)]

use super::*;

#[tokio::test]
async fn a_workflow_id_cannot_be_resolved_and_the_message_says_what_to_do() {
    let error = NoCatalog
        .resolve("deep_dive")
        .await
        .expect_err("there is no catalog");
    let rendered = error.to_string();
    assert!(rendered.contains("deep_dive"), "{rendered}");
    assert!(rendered.contains("inline"), "{rendered}");
}
