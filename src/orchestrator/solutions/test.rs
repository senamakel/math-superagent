//! Unit tests for the solution loop's routing policy and lesson extraction.

use super::{MAX_ATTEMPTS, Route, STUCK_THRESHOLD, SolutionState, extract_lesson, route};

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
    current
        .lessons
        .push("verify with a second route".to_string());
    let outcome = current.outcome();
    assert!(outcome.contains("Not solved"));
    assert!(outcome.contains("reached the derivation"));
    assert!(outcome.contains("verify with a second route"));
}

#[test]
fn the_first_attempt_starts_fresh_and_later_ones_continue() {
    use super::continuation_briefing;

    let first = continuation_briefing(1);
    assert!(first.contains("first attempt"));
    assert!(first.contains("run a program"));

    // The failure this exists to prevent: every attempt restarting at "read
    // the statement and write it down", so the run never executes anything.
    let third = continuation_briefing(3);
    assert!(third.contains("attempt 3"));
    assert!(third.contains("CONTINUE"));
    assert!(third.contains("Do not re-extract"));
    assert!(!third.contains("first attempt"));
}

#[test]
fn reflection_filenames_encode_the_outcome() {
    use super::reflection_filename;
    // A directory listing alone should show which attempts taught anything.
    assert_eq!(reflection_filename(1700, 0), "reflections/1700_nothing.md");
    assert_eq!(
        reflection_filename(1700, 1),
        "reflections/1700_01_learnings.md"
    );
    assert_eq!(
        reflection_filename(1700, 12),
        "reflections/1700_12_learnings.md"
    );
}

#[test]
fn learnings_are_counted_from_the_lesson_block() {
    use super::count_learnings;

    assert_eq!(
        count_learnings("VERDICT: UNSOLVED\nPROGRESS: NO\nLESSON: use Pell theory."),
        1
    );
    // Bullets under LESSON are separate actionable points.
    let multi = "VERDICT: UNSOLVED\nLESSON:\n- stop enumerating x\n- use the convergents\n";
    assert_eq!(count_learnings(multi), 2);
    // An empty lesson teaches nothing.
    assert_eq!(
        count_learnings("VERDICT: SOLVED\nPROGRESS: YES\nLESSON:"),
        0
    );
    assert_eq!(count_learnings("no structure at all"), 0);
}
