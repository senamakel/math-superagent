//! Unit tests for the in-run reflection middleware.

use super::{REPEAT_ESCALATION, ReflectionMiddleware};

#[test]
fn a_first_failure_asks_for_a_changed_retry() {
    let note = ReflectionMiddleware::note("download_document", 1);
    assert!(note.contains("download_document"));
    assert!(note.contains("change that thing"));
    assert!(!note.contains("times in this run"));
}

#[test]
fn repeated_failures_escalate_to_naming_the_loop() {
    let note = ReflectionMiddleware::note("download_document", REPEAT_ESCALATION + 1);
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
