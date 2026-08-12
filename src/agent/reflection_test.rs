//! Unit tests for the in-run reflection middleware.

use super::{REPEAT_ESCALATION, ReflectionMiddleware, truncated_arguments};

#[test]
fn a_first_failure_asks_for_a_changed_retry() {
    let note = ReflectionMiddleware::note("download_document", 1, "boom");
    assert!(note.contains("download_document"));
    assert!(note.contains("change that thing"));
    assert!(!note.contains("times in this run"));
}

#[test]
fn repeated_failures_escalate_to_naming_the_loop() {
    let note = ReflectionMiddleware::note("download_document", REPEAT_ESCALATION + 1, "boom");
    assert!(note.contains("has now failed"));
    assert!(note.contains("Do not call it again"));
    assert!(note.contains("move on"));
}

#[test]
fn failure_counts_accumulate_per_tool_and_reset_on_success() {
    let middleware = ReflectionMiddleware::new();
    assert_eq!(middleware.record("exa_search"), 1);
    assert_eq!(middleware.record("exa_search"), 2);
    // A different tool has its own count.
    assert_eq!(middleware.record("read_document"), 1);
    // Success clears only the tool that succeeded.
    middleware.clear("exa_search");
    assert_eq!(middleware.record("exa_search"), 1);
    assert_eq!(middleware.record("read_document"), 2);
}

/// The exact text a truncated `spawn_agent` produced on Project Euler 579.
const TRUNCATED: &str = "openai response contained invalid JSON arguments for tool call \
                         `chatcmpl-tool-beb298396246d1bf` (`spawn_agent`): EOF while parsing a \
                         string at line 1 column 36; raw arguments: \"{\\\"agent\\\": \
                         \\\"tool_builder\\\", \\\"input\\\": \\\"\"";

#[test]
fn a_truncated_call_is_recognised_and_an_ordinary_failure_is_not() {
    assert!(truncated_arguments(TRUNCATED));
    assert!(!truncated_arguments(
        "http status 403 for https://example.com"
    ));
    // A genuinely malformed argument the model must fix is not truncation.
    assert!(!truncated_arguments(
        "`path` is required and must be a non-empty string"
    ));
}

#[test]
fn a_truncated_call_is_told_to_shorten_rather_than_to_rethink() {
    let note = ReflectionMiddleware::note("spawn_agent", 1, TRUNCATED);
    assert!(note.contains("ran out of output tokens"));
    assert!(note.contains("cut down hard"));
    // The misleading generic advice must not appear: the arguments were right.
    assert!(!note.contains("change that thing"));
}

#[test]
fn a_truncated_call_does_not_escalate_against_the_tool() {
    // Even at a count that would otherwise escalate, the advice stays
    // "shorten and re-issue" rather than "stop calling this tool".
    let note = ReflectionMiddleware::note("spawn_agent", REPEAT_ESCALATION + 5, TRUNCATED);
    assert!(note.contains("Re-issue it now"));
    assert!(!note.contains("Do not call it again"));
}
