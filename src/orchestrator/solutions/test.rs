//! Unit tests for the solution loop's routing policy and lesson extraction.
#![allow(clippy::expect_used)]

use super::{
    MAX_ATTEMPTS, PatternMailbox, Route, STUCK_THRESHOLD, SolutionState, extract_lesson, route,
};

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

#[test]
fn a_claimed_solution_with_no_program_is_not_accepted() {
    use super::has_executable_artifact;

    let dir = std::env::temp_dir().join(format!("math-agent-ev-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&dir);
    std::fs::create_dir_all(&dir).expect("temp workspace");

    // Notes alone are the confabulation signature: a confident write-up with
    // nothing that ever ran.
    std::fs::write(dir.join("solution.md"), "The answer is 1,2,3").expect("write");
    assert!(!has_executable_artifact(&dir));

    // An empty program is no better than none.
    std::fs::write(dir.join("solution.py"), "").expect("write");
    assert!(!has_executable_artifact(&dir));

    std::fs::write(dir.join("solution.py"), "print(6)").expect("write");
    assert!(has_executable_artifact(&dir));

    let _ = std::fs::remove_dir_all(&dir);
}

#[tokio::test]
async fn a_reflection_is_indexed_with_its_verdict_and_lesson() {
    let workspace = std::env::temp_dir().join("math-agent-reflection-index");
    let _ = std::fs::remove_dir_all(&workspace);
    std::fs::create_dir_all(&workspace).expect("create test workspace");

    super::log_reflection(
        Some(&workspace),
        3,
        "VERDICT: UNSOLVED\nPROGRESS: YES\nLESSON: the frame enumeration recomputes primitive \
         frames for every n; cache them across calls.",
        None,
    )
    .await;

    let index = std::fs::read_to_string(workspace.join("reflections").join("INDEX.md"))
        .expect("reflections index was written");
    // The row has to carry what a reader needs without opening the file:
    // which attempt, how it was judged, and what it taught.
    assert!(index.contains("Attempt 3"), "{index}");
    assert!(index.contains("unsolved"), "{index}");
    assert!(index.contains("cache them across calls"), "{index}");
    // And it must name the file it describes.
    assert!(index.contains("_learnings.md"), "{index}");

    // A second reflection joins the table rather than replacing it.
    super::log_reflection(
        Some(&workspace),
        4,
        "VERDICT: SOLVED\nPROGRESS: YES\n",
        None,
    )
    .await;
    let index = std::fs::read_to_string(workspace.join("reflections").join("INDEX.md"))
        .expect("reflections index still there");
    assert!(index.contains("Attempt 3"), "{index}");
    assert!(index.contains("Attempt 4"), "{index}");
    assert!(index.contains("solved"), "{index}");
    let _ = std::fs::remove_dir_all(&workspace);
}

#[test]
fn a_pattern_report_that_arrives_late_still_reaches_a_later_attempt() {
    // The pattern agent is detached so it cannot gate the loop, which only
    // helps if what it finds is not simply dropped. A live run sat 33 minutes
    // unable to start its next attempt while an awaited pattern agent worked.
    let mailbox = PatternMailbox::default();
    assert_eq!(mailbox.collect(), "", "nothing has been posted yet");

    mailbox.post("period 6 in the residues".to_string());
    let collected = mailbox.collect();
    assert!(collected.contains("period 6"), "got: {collected}");
    assert_eq!(
        mailbox.collect(),
        "",
        "a report is delivered once, not to every later attempt"
    );
}

#[test]
fn several_pattern_runs_outliving_their_attempts_are_all_delivered() {
    // Detaching means a run can outlive the attempt that started it, so more
    // than one report can be waiting. Keeping only the newest would silently
    // discard the analysis an attempt paid for.
    let mailbox = PatternMailbox::default();
    mailbox.post("first: no linear recurrence".to_string());
    mailbox.post("second: divisibility by 9".to_string());

    let collected = mailbox.collect();
    assert!(collected.contains("no linear recurrence"), "{collected}");
    assert!(collected.contains("divisibility by 9"), "{collected}");
}

#[test]
fn an_empty_pattern_report_is_not_posted_as_context() {
    // A failed or silent pattern run must not present itself to the next
    // attempt as an analysis that found nothing to report.
    let mailbox = PatternMailbox::default();
    mailbox.post("   \n  ".to_string());
    assert_eq!(mailbox.collect(), "");
}
