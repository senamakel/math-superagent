use std::sync::Arc;

use async_trait::async_trait;
use serde_json::json;

use super::*;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// A tool that returns whatever text it was built with, and records whether it
/// ran at all.
struct Echo {
    reply: String,
    ran: Arc<std::sync::atomic::AtomicBool>,
}

#[async_trait]
impl Tool<()> for Echo {
    fn name(&self) -> &str {
        "exa_search"
    }
    fn description(&self) -> &str {
        "test double"
    }
    fn schema(&self) -> ToolSchema {
        ToolSchema::new("exa_search", "test double", json!({"type": "object"}))
    }
    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.ran.store(true, std::sync::atomic::Ordering::SeqCst);
        Ok(ToolResult::text(call.id, "exa_search", self.reply.clone()))
    }
}

fn workspace(name: &str) -> std::path::PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-screened-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the fixture workspace must be creatable");
    root
}

/// Builds a screened `Echo` with no adjudicator, so the deterministic stage —
/// the actual control — is what is under test.
fn screened(
    name: &str,
    reply: &str,
) -> (
    ScreenedTool,
    Arc<std::sync::atomic::AtomicBool>,
    std::path::PathBuf,
) {
    let ran = Arc::new(std::sync::atomic::AtomicBool::new(false));
    let root = workspace(name);
    let tool = ScreenedTool::new(
        Arc::new(Echo {
            reply: reply.to_string(),
            ran: Arc::clone(&ran),
        }),
        Arc::new(ScreenPolicy::for_test(
            &["de Grey"],
            &["chromatic number"],
            &["arxiv.org"],
        )),
        root.clone(),
        Arc::new("determine the chromatic number of the plane".to_string()),
        None,
    );
    (tool, ran, root)
}

fn call(arguments: serde_json::Value) -> ToolCall {
    ToolCall {
        id: "c1".to_string(),
        name: "exa_search".to_string(),
        arguments,
        invalid: None,
    }
}

#[tokio::test]
async fn a_clean_call_passes_through_untouched() {
    let (tool, ran, root) = screened("clean", "every edge has length exactly one");
    let result = tool
        .call(&(), call(json!({"query": "unit distance graphs"})))
        .await
        .expect("a clean call must succeed");
    assert_eq!(result.content, "every edge has length exactly one");
    assert!(ran.load(std::sync::atomic::Ordering::SeqCst));
    assert!(
        !root.join("config/screen.jsonl").exists(),
        "an allowed call must not write a ledger row"
    );
}

#[tokio::test]
async fn a_blocked_query_is_refused_without_running_the_tool() {
    let (tool, ran, root) = screened("blocked-args", "unreachable");
    let result = tool
        .call(&(), call(json!({"query": "de Grey chromatic plane"})))
        .await
        .expect("a refusal is a result, not an error");
    assert!(
        !ran.load(std::sync::atomic::Ordering::SeqCst),
        "the wrapped tool must not run when the arguments are refused"
    );
    assert!(result.content.contains("was not made"));
    assert!(
        std::fs::read_to_string(root.join("config/screen.jsonl"))
            .expect("a denial must be recorded")
            .contains(r#""stage":"arguments""#)
    );
}

#[tokio::test]
async fn a_blocked_result_is_withheld_after_the_tool_ran() {
    let (tool, ran, root) = screened("blocked-result", "a 2018 paper by Aubrey de Grey");
    let result = tool
        .call(&(), call(json!({"query": "unit distance"})))
        .await
        .expect("a refusal is a result, not an error");
    assert!(
        ran.load(std::sync::atomic::Ordering::SeqCst),
        "the call itself was clean, so the tool runs and the result is screened"
    );
    assert!(!result.content.contains("de Grey"));
    assert!(result.content.contains("withheld"));
    assert!(
        std::fs::read_to_string(root.join("config/screen.jsonl"))
            .expect("a denial must be recorded")
            .contains(r#""stage":"result""#)
    );
}

#[tokio::test]
async fn a_refusal_never_names_what_it_withheld() {
    // The refusal goes straight into the model's context. Naming the matched
    // term there would deliver the withheld name by the very mechanism meant to
    // stop it, and would make the hashed blocklist pointless.
    let (tool, _ran, _root) = screened("no-name", "a 2018 paper by Aubrey de Grey");
    let result = tool
        .call(&(), call(json!({"query": "unit distance"})))
        .await
        .expect("a refusal is a result");
    assert!(!result.content.to_lowercase().contains("grey"));
    assert!(!result.content.to_lowercase().contains("term"));
}

#[tokio::test]
async fn a_denied_host_is_refused_before_the_request_is_made() {
    let (tool, ran, root) = screened("denied-host", "unreachable");
    let result = tool
        .call(
            &(),
            call(json!({"urls": ["https://export.arxiv.org/abs/1804.02385"]})),
        )
        .await
        .expect("a refusal is a result");
    assert!(!ran.load(std::sync::atomic::Ordering::SeqCst));
    assert!(result.content.contains("was not made"));
    assert!(
        std::fs::read_to_string(root.join("config/screen.jsonl"))
            .expect("a denial must be recorded")
            .contains("denied-host")
    );
}

#[tokio::test]
async fn a_flagged_result_passes_when_no_adjudicator_is_configured() {
    // `[flag]` terms are chosen because they are too common to block. With the
    // semantic stage switched off they must not be promoted into denials, or an
    // operator disabling the adjudicator would silently withhold half the
    // legitimate literature.
    let (tool, _ran, _root) = screened("flag-no-model", "we bound the chromatic number here");
    let result = tool
        .call(&(), call(json!({"query": "bounds"})))
        .await
        .expect("a flagged result must still be delivered");
    assert_eq!(result.content, "we bound the chromatic number here");
}

#[tokio::test]
async fn a_tool_error_is_forwarded_rather_than_screened() {
    // An error result carries the tool's own diagnostic, not fetched material.
    // Screening it would replace a message the model can act on with a refusal
    // it cannot.
    struct Failing;
    #[async_trait]
    impl Tool<()> for Failing {
        fn name(&self) -> &str {
            "exa_search"
        }
        fn description(&self) -> &str {
            "test double"
        }
        fn schema(&self) -> ToolSchema {
            ToolSchema::new("exa_search", "test double", json!({"type": "object"}))
        }
        async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
            Ok(ToolResult::error(
                call.id,
                "exa_search".to_string(),
                "de Grey rate limit".to_string(),
            ))
        }
    }
    let tool = ScreenedTool::new(
        Arc::new(Failing),
        Arc::new(ScreenPolicy::for_test(&["de Grey"], &[], &[])),
        workspace("tool-error"),
        Arc::new(String::new()),
        None,
    );
    let result = tool
        .call(&(), call(json!({"query": "x"})))
        .await
        .expect("an error result is still a result");
    assert!(result.error.is_some(), "the error must be forwarded");
}

#[test]
fn every_url_shaped_argument_is_found_wherever_it_sits() {
    // Walked rather than looked up by field name: the screened tools spell it
    // `url`, `urls`, `source` and `links`, and a new one must not be missed.
    let found = url_arguments(&json!({
        "url": "https://a.example/one",
        "nested": {"urls": ["https://b.example/two", "not a url"]},
        "count": 3,
        "links": [{"href": "http://c.example/three"}]
    }));
    assert_eq!(found.len(), 3, "found {found:?}");
}
