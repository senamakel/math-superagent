//! Unit tests for the solution loop's routing policy and lesson extraction.
#![allow(clippy::expect_used)]

use super::{
    BLOCKED_THRESHOLD, MAX_ATTEMPTS, Mailbox, Route, STUCK_THRESHOLD, SolutionState,
    extract_lesson, provider_blocked, route,
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

    let first = continuation_briefing(1, false);
    assert!(first.contains("first attempt"));
    assert!(first.contains("run a program"));

    // The failure this exists to prevent: every attempt restarting at "read
    // the statement and write it down", so the run never executes anything.
    let third = continuation_briefing(3, false);
    assert!(third.contains("attempt 3"));
    assert!(third.contains("CONTINUE"));
    assert!(third.contains("Do not re-extract"));
    assert!(!third.contains("first attempt"));
}

#[test]
fn the_first_attempt_opens_with_an_oracle_run_of_its_own() {
    // Two live runs reached ten minutes with no execution because their goals
    // agent never delegated. The loop no longer depends on it for the first
    // one: the oracle task names the file, forbids optimisation, and asks for
    // the exact output so the attempt has something to check against.
    let prompt = super::oracle_prompt("Compute S(10^8).");
    assert!(prompt.contains("code/brute.py"), "{prompt}");
    assert!(prompt.contains("Compute S(10^8)."), "{prompt}");
    assert!(prompt.contains("worked example"), "{prompt}");
    // It must not turn into a second solver racing the real attempt.
    assert!(
        prompt.contains("do not derive the efficient method"),
        "{prompt}"
    );
    assert!(prompt.contains("already holds such a program"), "{prompt}");
}

#[test]
fn an_unreadable_judge_reply_never_throws_an_attempt_away() {
    use super::{Verdict, judge_verdict};
    // The expensive outcome needs the explicit word, in the same spirit as an
    // unparsable reflection not counting as solved.
    assert_eq!(judge_verdict("VERDICT: RESTART"), Verdict::Restart);
    assert_eq!(judge_verdict("verdict:restart"), Verdict::Restart);
    assert_eq!(judge_verdict("VERDICT: STEER"), Verdict::Steer);
    assert_eq!(judge_verdict("VERDICT: PROCEED"), Verdict::Proceed);
    assert_eq!(
        judge_verdict("the attempt was a disaster"),
        Verdict::Proceed
    );
    assert_eq!(judge_verdict(""), Verdict::Proceed);
}

#[test]
fn the_judges_score_and_guidance_are_read_when_they_are_there() {
    use super::{judge_guidance, judge_score};
    let reply = "SCORE: 2/5\nVERDICT: STEER\nBECAUSE: nothing ran.\nNEXT: run the oracle first.";
    assert_eq!(judge_score(reply), Some(2));
    assert_eq!(judge_guidance(reply), "run the oracle first.");
    // A score outside the rubric is no score at all rather than a wrong one.
    assert_eq!(judge_score("SCORE: 9/5"), None);
    assert_eq!(judge_score("no score here"), None);
    assert_eq!(judge_guidance("SCORE: 5/5\nVERDICT: PROCEED"), "");
}

#[test]
fn the_attempt_ceiling_outranks_a_restart() {
    use super::{Judged, MAX_ATTEMPTS, SolutionState, Verdict, judged_route};
    // A run at its last attempt must reflect on what it has rather than throw
    // it away and stop with nothing.
    let mut state = SolutionState::new("problem");
    state.judged = Verdict::Restart;
    state.attempts = 1;
    assert_eq!(judged_route(&state), Judged::Restart);
    state.attempts = MAX_ATTEMPTS;
    assert_eq!(judged_route(&state), Judged::Reflect);
    state.judged = Verdict::Proceed;
    state.attempts = 1;
    assert_eq!(judged_route(&state), Judged::Reflect);
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

#[test]
fn a_pattern_report_that_arrives_late_still_reaches_a_later_attempt() {
    // The pattern agent is detached so it cannot gate the loop, which only
    // helps if what it finds is not simply dropped. A live run sat 33 minutes
    // unable to start its next attempt while an awaited pattern agent worked.
    let mailbox = Mailbox::default();
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
    let mailbox = Mailbox::default();
    mailbox.post("first: no linear recurrence".to_string());
    mailbox.post("second: divisibility by 9".to_string());

    let collected = mailbox.collect();
    assert!(collected.contains("no linear recurrence"), "{collected}");
    assert!(collected.contains("divisibility by 9"), "{collected}");
}

#[test]
fn an_attempt_is_told_what_the_pattern_team_found() {
    use super::{attempt_prompt, observations_briefing};

    // Reflection was the only collector, so the team reached the work exactly
    // once per *completed* attempt — never on a first attempt that runs long.
    // A live Erdős–Gyárfás run spent forty minutes in attempt 1 while its
    // pattern team computed the survivor counts and identified the sequence,
    // and the agent directing the work re-commissioned the same enumeration.
    let mailbox = Mailbox::default();
    mailbox.post("every no-4 survivor for n<=16 has an 8-cycle".to_string());

    let observations = observations_briefing(&mailbox);
    let state = SolutionState::new("find the cycle lengths");
    let prompt = attempt_prompt(&state, "", &observations);

    assert!(prompt.contains("pattern team"), "{prompt}");
    assert!(prompt.contains("has an 8-cycle"), "{prompt}");
}

#[test]
fn an_attempt_with_nothing_from_the_pattern_team_says_nothing_about_it() {
    use super::{attempt_prompt, observations_briefing};

    // A heading announcing that no analysis arrived is worse than silence: it
    // spends context to tell the attempt something it cannot act on.
    let mailbox = Mailbox::default();
    let observations = observations_briefing(&mailbox);
    assert_eq!(observations, "");

    let state = SolutionState::new("find the cycle lengths");
    let prompt = attempt_prompt(&state, "", &observations);
    assert!(!prompt.contains("pattern team"), "{prompt}");
}

#[test]
fn an_empty_pattern_report_is_not_posted_as_context() {
    // A failed or silent pattern run must not present itself to the next
    // attempt as an analysis that found nothing to report.
    let mailbox = Mailbox::default();
    mailbox.post("   \n  ".to_string());
    assert_eq!(mailbox.collect(), "");
}

#[test]
fn a_restarted_run_is_told_it_is_continuing_even_on_its_first_attempt() {
    use super::continuation_briefing;

    // Every restart resets the attempt counter while the workspace survives,
    // so attempt 1 of a resumed run sits on programs, notes and beliefs it is
    // told to establish from scratch. A live solver spent fourteen minutes and
    // fifty-nine model calls on seventeen `read_document` calls and nothing
    // else, reconciling a statement it had been told to extract afresh against
    // thirty-one programs already on disk.
    let resumed = continuation_briefing(1, true);
    assert!(resumed.contains("CONTINUE"), "{resumed}");
    assert!(resumed.contains("recall_memory"), "{resumed}");
    assert!(
        !resumed.contains("first attempt"),
        "a resumed run must not be told to start fresh: {resumed}"
    );
    // A genuinely fresh workspace still gets the fresh briefing: the oracle
    // has to be written before anything can be continued from.
    let fresh = continuation_briefing(1, false);
    assert!(fresh.contains("first attempt"), "{fresh}");
}

#[test]
fn a_provider_wall_stops_the_loop_instead_of_spending_the_attempt_ceiling() {
    // What a live pair of runs actually did: OpenRouter refused every call with
    // `HTTP 403: Key limit exceeded`, and the loop burned all eight attempts in
    // seconds, recording the same quota error as the lesson each time. An
    // attempt that never reached the mathematics is not evidence about the
    // mathematics, so it must not be paid for out of the ceiling.
    let mut current = state();
    current.blocked = BLOCKED_THRESHOLD;
    assert_eq!(route(&current), Route::Blocked);

    // It outranks the ceiling, so the outcome says "blocked" rather than
    // "not solved within 8 attempts".
    current.attempts = MAX_ATTEMPTS;
    assert_eq!(route(&current), Route::Blocked);
    let outcome = current.outcome();
    assert!(outcome.contains("infrastructure failure"), "{outcome}");
    assert!(!outcome.starts_with("Not solved"), "{outcome}");
}

#[test]
fn one_provider_failure_is_absorbed_rather_than_ending_the_run() {
    // A single upstream blip is what the retry ladder and the rerouting model
    // exist to absorb. Ending a run on one would throw away work they would
    // have recovered.
    let mut current = state();
    current.blocked = BLOCKED_THRESHOLD - 1;
    assert_eq!(route(&current), Route::Retry);
}

#[test]
fn a_blocked_attempt_is_recognised_only_from_a_failed_delegation() {
    // The shape `delegate` writes when a child dies on its first turn.
    assert!(provider_blocked(
        "[goals failed: tool error: agent `goals` failed: model error: openrouter returned \
         HTTP 403: Key limit exceeded (daily limit)]"
    ));
    assert!(provider_blocked(
        "[goals failed: model error: openrouter returned HTTP 429: rate limit]"
    ));

    // An attempt that did real work and merely mentions a limit is not blocked.
    // A false positive here stops a run that was working, which is worse than
    // the wasted attempts this exists to prevent.
    assert!(!provider_blocked(
        "I computed D(14) = 5949063 and verified it three ways. The provider rate limit \
         slowed the run but every call eventually succeeded."
    ));
    // A genuine attempt that failed for a mathematical reason.
    assert!(!provider_blocked(
        "[goals failed: the derivation did not close; the recurrence is unproven]"
    ));
    assert!(!provider_blocked(""));
}
