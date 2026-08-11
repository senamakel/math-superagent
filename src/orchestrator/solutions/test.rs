//! Unit tests for the solution loop's routing policy and lesson extraction.

use super::{MAX_ATTEMPTS, Route, SolutionState, STUCK_THRESHOLD, extract_lesson, route};

fn state() -> SolutionState {
    SolutionState::new("find the largest x")
}

#[test]
fn a_verified_solution_ends_the_loop() {
    let mut current = state();
    current.solved = true;
    assert_eq!(route(&current), Route::Solved);
}

#[test]
fn productive_attempts_simply_retry() {
    let mut current = state();
    current.attempts = 1;
    current.unproductive = 0;
    assert_eq!(route(&current), Route::Retry);
}

#[test]
fn repeated_unproductive_attempts_diversify_instead_of_retrying() {
    let mut current = state();
    current.attempts = 3;
    current.unproductive = STUCK_THRESHOLD;
    assert_eq!(route(&current), Route::Diversify);
}

#[test]
fn the_loop_terminates_at_the_attempt_ceiling_even_when_unsolved() {
    let mut current = state();
    current.attempts = MAX_ATTEMPTS;
    current.unproductive = STUCK_THRESHOLD * 4;
    // Must not diversify forever: the ceiling wins over the stuck rule.
    assert_eq!(route(&current), Route::Solved);
}

#[test]
fn lessons_are_extracted_from_the_reflection_verdict() {
    let reflection = "VERDICT: UNSOLVED\nPROGRESS: NO\nLESSON: Stop enumerating x and use the \
                      continued fraction of sqrt(D) instead.";
    assert_eq!(
        extract_lesson(reflection),
        "Stop enumerating x and use the continued fraction of sqrt(D) instead."
    );
}

#[test]
fn an_unusable_reflection_still_yields_a_lesson() {
    assert!(extract_lesson("").contains("nothing usable"));
    // No LESSON: line - fall back to the text rather than losing it.
    assert!(extract_lesson("the attempt timed out").contains("timed out"));
}

#[test]
fn outcome_reports_progress_even_when_unsolved() {
    let mut current = state();
    current.attempts = 2;
    current.last_attempt = "reached the derivation but did not verify".to_string();
    current.lessons.push("verify with a second route".to_string());
    let outcome = current.outcome();
    assert!(outcome.contains("Not solved"));
    assert!(outcome.contains("reached the derivation"));
    assert!(outcome.contains("verify with a second route"));
}
