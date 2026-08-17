//! Unit tests for the solution loop's routing policy and lesson extraction.
#![allow(clippy::expect_used)]

use super::{
    BLOCKED_THRESHOLD, COMPUTATIONAL_THRESHOLD, MAX_ATTEMPTS, Mailbox, Progress, REDUCTION_INTERVAL,
    ReductionGate, Route, STUCK_THRESHOLD, SolutionState, UNVERIFIED_THRESHOLD, approach_slugs,
    evidence_briefing, extract_lesson, gap_briefing, kind_of, provider_blocked, record_verdict,
    route, skeleton_fingerprint,
};
use super::{Finding, Slot, diversify_merge};
use crate::orchestrator::schools::{ALL, Thresholds};

/// The control school's bounds.
///
/// Every assertion below was written against the constants, and `chisel()` is
/// read off exactly those constants — so these tests say the same thing they
/// said before `route` took its bounds as an argument, rather than a weaker
/// version of it.
fn chisel() -> Thresholds {
    Thresholds::chisel()
}

fn state() -> SolutionState {
    SolutionState::new("find the largest x")
}

#[test]
fn a_verified_solution_ends_the_loop() {
    let mut current = state();
    current.solved = true;
    assert_eq!(route(&current, &chisel()), Route::Solved);
}

#[test]
fn productive_attempts_simply_retry() {
    let mut current = state();
    current.attempts = 1;
    current.unproductive = 0;
    assert_eq!(route(&current, &chisel()), Route::Retry);
}

#[test]
fn repeated_unproductive_attempts_diversify_instead_of_retrying() {
    let mut current = state();
    current.attempts = 3;
    current.unproductive = STUCK_THRESHOLD;
    assert_eq!(route(&current, &chisel()), Route::Diversify);
}

/// The regression the whole change exists to prevent. A run that pushes the
/// same computation to a larger size every attempt reports PROGRESS: YES every
/// time, so `unproductive` never accumulates and the stuck rule never fires.
/// Before the kind was counted, such a run could spend its entire budget
/// scaling one method and never once reach the inventor.
#[test]
fn scaling_the_same_method_diversifies_even_while_reporting_progress() {
    let mut current = state();
    current.attempts = 3;
    // Every attempt progressed, so the stuck rule is dormant by construction.
    current.unproductive = 0;
    current.computational = COMPUTATIONAL_THRESHOLD;
    assert_eq!(route(&current, &chisel()), Route::Diversify);
}

/// One scale-up is what an attempt looks like, not a pattern. The loop only
/// intervenes on the second.
#[test]
fn a_single_scale_up_still_retries() {
    let mut current = state();
    current.attempts = 2;
    current.computational = COMPUTATIONAL_THRESHOLD - 1;
    assert_eq!(route(&current, &chisel()), Route::Retry);
}

/// An attempt that established something standing on its own has changed what
/// the run is doing, so the scaling count starts again.
#[test]
fn mathematical_progress_clears_the_scaling_count() {
    let mut current = state();
    current.computational = COMPUTATIONAL_THRESHOLD;
    // What `reflect_step` does with each verdict.
    match kind_of("KIND: MATHEMATICAL") {
        Progress::Mathematical => current.computational = 0,
        Progress::Computational => current.computational += 1,
        Progress::Unstated => {}
    }
    assert_eq!(current.computational, 0);
    assert_eq!(route(&current, &chisel()), Route::Retry);
}

/// A reply the parser cannot read must not move the loop. Treating silence as
/// "scaling again" would divert a working run on two malformed replies.
#[test]
fn an_unreadable_kind_moves_nothing() {
    assert_eq!(
        kind_of("VERDICT: UNSOLVED\nPROGRESS: YES"),
        Progress::Unstated
    );
    assert_eq!(kind_of("KIND: SOMETHING ELSE"), Progress::Unstated);
    // Both spacings the reflection actually produces are read.
    assert_eq!(kind_of("KIND:COMPUTATIONAL"), Progress::Computational);
    assert_eq!(kind_of("KIND: COMPUTATIONAL"), Progress::Computational);
    assert_eq!(kind_of("KIND:MATHEMATICAL"), Progress::Mathematical);
}

/// A provider outage is not evidence about the mathematics, so it outranks the
/// scaling rule as it outranks every other one: diversifying into the same wall
/// is three more child runs into it.
#[test]
fn a_provider_wall_outranks_the_scaling_rule() {
    let mut current = state();
    current.computational = COMPUTATIONAL_THRESHOLD * 2;
    current.blocked = BLOCKED_THRESHOLD;
    assert_eq!(route(&current, &chisel()), Route::Blocked);
}

#[test]
fn the_loop_terminates_at_the_attempt_ceiling_even_when_unsolved() {
    let mut current = state();
    current.attempts = MAX_ATTEMPTS;
    current.unproductive = STUCK_THRESHOLD * 4;
    // Must not diversify forever: the ceiling wins over the stuck rule.
    assert_eq!(route(&current, &chisel()), Route::Solved);
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
fn the_salvage_task_asks_for_one_executed_result_and_nothing_else() {
    // Five consecutive attempts across two live runs ended
    // `[goals failed: run timed out]` with no artifact, because the attempt was
    // exactly one delegation. The salvage exists to make a dead planner cost one
    // child rather than the whole attempt, so it must ask for execution and must
    // not invite a second plan.
    let prompt = super::salvage_prompt("Compute S(10^8).");
    assert!(prompt.contains("Compute S(10^8)."), "{prompt}");
    assert!(prompt.contains("code/out/"), "{prompt}");
    assert!(prompt.contains("never been run"), "{prompt}");
    assert!(prompt.contains("Do not plan"), "{prompt}");
    // A salvage that starts something open-ended repeats the failure it exists
    // to absorb.
    assert!(
        prompt.contains("cannot finish in this run"),
        "{prompt}"
    );
    // Being blocked is a reportable outcome; silence is not.
    assert!(prompt.contains("what blocks it"), "{prompt}");
}

#[test]
fn a_failed_planner_still_reports_what_the_salvage_executed() {
    // The report the judge and reflection score must carry both halves: the
    // failure, so the loop can see the planner died, and the salvage output, so
    // an attempt that executed something is not scored as though it produced
    // nothing.
    let report = format!(
        "[goals failed: {}]\n\nSalvaged by direct execution:\n{}",
        "run timed out: subagent run timed out", "ran code/out/brute.captured.txt; matched 3/3"
    );
    assert!(report.contains("goals failed"), "{report}");
    assert!(report.contains("Salvaged by direct execution"), "{report}");
    assert!(report.contains("matched 3/3"), "{report}");
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

/// The attempt ceiling still outranks a restart, and it is now the only thing
/// that has to.
///
/// A restart stopped being a route when the judge and the reflection became
/// concurrent — there is no reflection left to skip — so what is left to check
/// is that a run at its ceiling ends on the reflection's terms rather than the
/// judge's. The reflect ladder is the only ladder, and `solved` is what it
/// answers at the ceiling however the judge scored the attempt.
#[test]
fn the_attempt_ceiling_outranks_a_restart() {
    use super::{MAX_ATTEMPTS, Route, SolutionState, Verdict, route};

    let mut state = SolutionState::new("problem");
    state.judged = Verdict::Restart;
    state.attempts = MAX_ATTEMPTS;
    assert_eq!(route(&state, &chisel()), Route::Solved);
    state.attempts = 1;
    assert_eq!(route(&state, &chisel()), Route::Retry);
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
fn a_finished_cycle_opens_an_invention_only_when_the_loop_will_try_again() {
    use super::{Route, route};

    // The inventor used to run only inside `diversify`, which needs two
    // completed attempt/judge/reflect cycles. A run whose attempts take the
    // better part of an hour never gets there: across a day of live runs on
    // three workspaces it was spawned once, and the approach ledger it writes
    // never existed on disk. Opening it at the end of every cycle is the
    // pattern agent's argument one role wider.
    //
    // The gate is `route`, so this asserts the four cases without a provider.
    let mut retry = state();
    retry.attempts = 1;
    retry.unproductive = 0;
    assert_eq!(route(&retry, &chisel()), Route::Retry, "the cycle that opens one");

    // Diversify runs the same arm one step later and awaits it; opening one
    // here too would spend two inventor runs on a single cycle.
    let mut stuck = state();
    stuck.attempts = 3;
    stuck.unproductive = STUCK_THRESHOLD;
    assert_eq!(route(&stuck, &chisel()), Route::Diversify);

    // A run that has stopped has nobody to hand a new line of attack to.
    let mut solved = state();
    solved.solved = true;
    assert_eq!(route(&solved, &chisel()), Route::Solved);

    let mut blocked = state();
    blocked.attempts = 2;
    blocked.blocked = BLOCKED_THRESHOLD;
    assert_eq!(route(&blocked, &chisel()), Route::Blocked);
}

#[test]
fn an_attempt_is_told_what_arrived_beside_the_loop() {
    use super::{attempt_prompt, observations_briefing};

    // Reflection was the only collector, so what ran beside the loop reached
    // the work exactly once per *completed* attempt — never on a first attempt
    // that runs long. A live Erdős–Gyárfás run spent forty minutes in attempt 1
    // while its pattern team computed the survivor counts and identified the
    // sequence, and the agent directing the work re-commissioned the same
    // enumeration.
    //
    // The mailbox carries the inventor's proposals too, which is why the
    // heading names neither role: both are things that arrived since the last
    // attempt, and both are worth as much an attempt late.
    let mailbox = Mailbox::default();
    mailbox.post("every no-4 survivor for n<=16 has an 8-cycle".to_string());
    mailbox.post("Proposed lines of attack\nan ear decomposition argument".to_string());

    let observations = observations_briefing(&mailbox);
    let state = SolutionState::new("find the cycle lengths");
    let prompt = attempt_prompt(&state, "", &observations, "", "", "");

    assert!(prompt.contains("beside the loop"), "{prompt}");
    assert!(prompt.contains("has an 8-cycle"), "{prompt}");
    assert!(prompt.contains("ear decomposition"), "{prompt}");
}

#[test]
fn an_attempt_with_an_empty_mailbox_says_nothing_about_it() {
    use super::{attempt_prompt, observations_briefing};

    // A heading announcing that no analysis arrived is worse than silence: it
    // spends context to tell the attempt something it cannot act on.
    let mailbox = Mailbox::default();
    let observations = observations_briefing(&mailbox);
    assert_eq!(observations, "");

    let state = SolutionState::new("find the cycle lengths");
    let prompt = attempt_prompt(&state, "", &observations, "", "", "");
    assert!(!prompt.contains("beside the loop"), "{prompt}");
}

/// The whole point of the channel is that the attempt is told a person asked
/// for this, and that it outranks what the run inferred on its own.
#[test]
fn an_attempt_carries_operator_direction_above_the_judge() {
    use super::{attempt_prompt, direction_briefing};

    let mailbox = Mailbox::default();
    mailbox.post("check the n=14 bound against a sieve".to_string());
    let direction = direction_briefing(&mailbox);

    let mut state = SolutionState::new("find the cycle lengths");
    state.steer = "tighten the enumeration".to_string();
    let prompt = attempt_prompt(&state, "", "", &direction, "", "");

    assert!(prompt.contains("check the n=14 bound"), "{prompt}");
    assert!(prompt.contains("Direction from the operator"), "{prompt}");
    // Both are present, and the one a person wrote comes first — a prompt that
    // buried it under the judge's steer would have the attempt reading it as
    // one more piece of automated advice.
    let operator = prompt.find("Direction from the operator");
    let judge = prompt.find("The judge reviewed");
    assert!(operator < judge, "operator direction must lead: {prompt}");
}

/// A directive is asserted, never established. Presenting it as something the
/// run knows is how an instruction becomes a false premise the attempt builds
/// on.
#[test]
fn operator_direction_is_labelled_as_an_instruction_not_a_finding() {
    use super::direction_briefing;

    let mailbox = Mailbox::default();
    mailbox.post("the recurrence is order three".to_string());
    let direction = direction_briefing(&mailbox);

    assert!(direction.contains("operator"), "{direction}");
    assert!(direction.contains("takes precedence"), "{direction}");
    // And it says what to do when the operator is wrong, because they can be.
    assert!(direction.contains("say so plainly"), "{direction}");
}

/// An empty mailbox renders nothing at all, the same as the pattern team's.
/// A heading saying nobody said anything spends context to report a non-event.
#[test]
fn an_attempt_with_no_direction_says_nothing_about_it() {
    use super::{attempt_prompt, direction_briefing};

    let direction = direction_briefing(&Mailbox::default());
    assert_eq!(direction, "");

    let state = SolutionState::new("find the cycle lengths");
    let prompt = attempt_prompt(&state, "", "", &direction, "", "");
    assert!(!prompt.contains("operator"), "{prompt}");
}

/// Delivered once. The mailbox is drained by the attempt, so a directive must
/// not reappear in every later prompt for the rest of the run.
#[test]
fn a_directive_reaches_one_attempt_rather_than_every_later_one() {
    use super::direction_briefing;

    let mailbox = Mailbox::default();
    mailbox.post("stop enumerating and prove the bound".to_string());
    assert!(direction_briefing(&mailbox).contains("prove the bound"));
    assert_eq!(direction_briefing(&mailbox), "");
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
    assert_eq!(route(&current, &chisel()), Route::Blocked);

    // It outranks the ceiling, so the outcome says "blocked" rather than
    // "not solved within 8 attempts".
    current.attempts = MAX_ATTEMPTS;
    assert_eq!(route(&current, &chisel()), Route::Blocked);
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
    assert_eq!(route(&current, &chisel()), Route::Retry);
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

fn approaches_workspace(name: &str) -> std::path::PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-invention-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("a temporary workspace");
    root
}

#[test]
fn approach_slugs_reads_the_directory_and_treats_a_missing_one_as_empty() {
    // The discriminator behind the write-verification control. A workspace
    // that has never reached a diversify has no `research/approaches/` at all
    // — that was true of all three concurrent live runs — so a missing
    // directory has to measure as empty rather than as an error.
    let root = approaches_workspace("missing");
    assert!(approach_slugs(Some(&root)).is_empty());
    assert!(approach_slugs(None).is_empty());

    let dir = root.join("research/approaches");
    std::fs::create_dir_all(&dir).expect("the approaches directory");
    assert!(
        approach_slugs(Some(&root)).is_empty(),
        "an empty directory is the same as no directory"
    );

    std::fs::write(dir.join("cycle-space-basis.md"), "x").expect("an approach file");
    let after = approach_slugs(Some(&root));
    assert_eq!(after.len(), 1);
    assert!(after.contains(&std::ffi::OsString::from("cycle-space-basis.md")));

    // Directories under it are not approaches. The comparison must move only
    // when a proposal lands, and a subfolder is not one.
    std::fs::create_dir(dir.join("scratch")).expect("a subdirectory");
    assert_eq!(approach_slugs(Some(&root)).len(), 1);
}

#[test]
fn a_rewritten_approach_does_not_count_as_a_proposal() {
    // The comparison is by name added, not by count or mtime. A turn that
    // rewrote an existing approach has not proposed anything, and mtime would
    // call that a success.
    let root = approaches_workspace("rewrite");
    let dir = root.join("research/approaches");
    std::fs::create_dir_all(&dir).expect("the approaches directory");
    std::fs::write(dir.join("cycle-space-basis.md"), "before").expect("an approach file");

    let before = approach_slugs(Some(&root));
    std::fs::write(dir.join("cycle-space-basis.md"), "after, and longer").expect("a rewrite");
    assert_eq!(
        approach_slugs(Some(&root)),
        before,
        "rewriting one file is not proposing a new line of attack"
    );

    std::fs::write(dir.join("girth-expansion.md"), "new").expect("a second approach");
    assert_ne!(approach_slugs(Some(&root)), before);
}

/// The cadence has to fire on the first completed cycle, not once the counter
/// has climbed to the interval.
///
/// This is `open_invention`'s recorded evidence one role wider. A gate needing
/// several completed attempt/judge/reflect cycles is a gate a run whose
/// attempts take the better part of an hour never reaches — across a day of
/// live runs the inventor was spawned once and its ledger never existed on
/// disk. Detached, an early first reduction costs one child run and the
/// skeleton reaches the attempt after next.
#[test]
fn a_fresh_run_is_due_a_reduction_on_its_first_completed_cycle() {
    let current = state();
    assert!(
        current.since_reduction >= REDUCTION_INTERVAL,
        "a run that has never decomposed its goal is already due one"
    );
}

/// The reduction opened beside the first attempt is opened from a state that
/// has attempted nothing, so anything it reads has to come from the problem
/// statement rather than from the loop's own output. This is what makes
/// opening it at the start sound rather than merely early: were the reducer's
/// brief assembled from lessons or verdicts, an initial reduction would be
/// briefed on an empty run and waste the child.
#[test]
fn the_initial_reduction_is_due_before_any_attempt_has_run() {
    let current = state();
    assert_eq!(
        current.attempts, 0,
        "the initial reduction is opened before the graph starts"
    );
    assert!(
        !current.solved,
        "a fresh run is not solved, so the cadence gate does not short-circuit"
    );
    assert!(
        current.since_reduction >= REDUCTION_INTERVAL,
        "the counter must already be due, or the first attempt runs with no skeleton beside it"
    );
    assert!(
        !current.problem().trim().is_empty(),
        "the reducer works backward from the goal, which must be present at start"
    );
}

/// Two reducers decompose the same goal, so they write the same file, and
/// `write_document` is last-writer-wins: the loser's gaps are gone with no
/// error anywhere. The gate is what makes that impossible rather than
/// unlikely.
#[test]
fn a_second_reduction_is_not_opened_while_one_is_in_flight() {
    let gate = ReductionGate::default();
    assert!(gate.claim(), "the first reduction takes the gate");
    assert!(!gate.claim(), "the second must be refused");
    // Held by the arm rather than by the cycle that opened it, so a reduction
    // outliving its cycle still keeps the gate shut.
    let held = gate.clone();
    assert!(!held.claim());
    gate.release();
    assert!(held.claim(), "the gate reopens once the arm finishes");
}

/// The second bound. The reducer's inputs are what the run has established, so
/// a tick over a workspace that has not moved would rewrite the same skeleton
/// from the same evidence — the pattern team's `results_unchanged` argument
/// applied to the research tree.
#[test]
fn the_cadence_declines_a_workspace_that_has_not_moved() {
    let gate = ReductionGate::default();
    // Nothing has been decomposed yet, so the first tick goes ahead whatever
    // the fingerprint is — including a workspace that happens to hash to zero.
    assert!(gate.moved(0));
    gate.remember(0);
    assert!(!gate.moved(0), "an unchanged tree is not new evidence");
    assert!(gate.moved(1), "a claim landing is");
}

/// An attempt told "Lemmas that would suffice:" with nothing under it
/// reasonably concludes the run decided there were none, which is a different
/// statement from no reduction having run.
#[test]
fn the_gap_briefing_renders_nothing_for_an_empty_mailbox() {
    let skeletons = Mailbox::default();
    assert!(gap_briefing(&skeletons).is_empty());

    skeletons.post("- `G-density` (event-rate): events occur with density >= 1/2".to_string());
    let briefing = gap_briefing(&skeletons);
    assert!(briefing.contains("G-density"));
    assert!(
        briefing.contains("task"),
        "an open gap has to arrive as a target rather than as background: {briefing}"
    );
}

/// The gaps travel in the attempt's prompt, under their own heading rather than
/// folded into the material the reflection gathered.
#[test]
fn the_attempt_is_told_which_lemmas_would_suffice() {
    let current = state();
    let prompt = super::attempt_prompt(
        &current,
        "",
        "",
        "",
        "Lemmas that would suffice to prove the goal:\n- `G-density`: events are dense\n\n",
        "",
    );
    assert!(prompt.contains("G-density"));
}

/// An attempt must be told what the library already entails, before it spends
/// itself proving something the run holds.
#[test]
fn the_attempt_is_told_what_it_already_has() {
    let current = state();
    let prompt = super::attempt_prompt(
        &current,
        "",
        "",
        "",
        "",
        "- `c` (filed as heuristic) follows from `a`, `b`: the combined bound\n",
    );
    assert!(prompt.contains("What the library already gives you"));
    assert!(prompt.contains("the combined bound"));
}

/// The discriminator behind `ensure_skeleton_written`, and the deliberate
/// inversion of `a_rewritten_approach_does_not_count_as_a_proposal`: refining a
/// live skeleton adds no filename and *is* the correct work, so the comparison
/// has to be on what downstream readers consume.
#[test]
fn a_rewritten_skeleton_counts_when_a_gap_moves() -> std::io::Result<()> {
    let root = approaches_workspace("reduction");
    let dir = root.join("research/backward");
    std::fs::create_dir_all(&dir)?;
    let write = |status: &str| -> std::io::Result<()> {
        std::fs::write(
            dir.join("event-rate.md"),
            format!(
                "```skeleton\ngoal: G\nimplies: the density bound gives it\n```\n\n\
                 ```gap\nid: G-density\nlemma: events are dense\nstatus: {status}\n```\n"
            ),
        )
    };
    write("open")?;
    let before = skeleton_fingerprint(Some(&root));
    assert!(!before.is_empty());

    write("open")?;
    assert_eq!(
        skeleton_fingerprint(Some(&root)),
        before,
        "rewriting the same gap is not moving anything a reader consumes"
    );

    write("discharged")?;
    assert_ne!(
        skeleton_fingerprint(Some(&root)),
        before,
        "closing a gap is the work, and it adds no filename"
    );
    Ok(())
}

/// A workspace that has never been decomposed has no `research/backward/` at
/// all, which has to measure as empty rather than as an error.
#[test]
fn skeleton_fingerprint_treats_a_missing_directory_as_empty() {
    let root = approaches_workspace("no-reduction");
    assert!(skeleton_fingerprint(Some(&root)).is_empty());
    assert!(skeleton_fingerprint(None).is_empty());
}

/// The judge must be able to see work the attempt could not report.
///
/// `RunBudget` caps an agent run, and a `goals` run pursuing an open goal does
/// not stop on its own — so the ordinary way an attempt ends is the cap killing
/// it, which destroys its report and leaves every file it wrote. One evening all
/// three live Euler attempts died at exactly 30:00 and every verdict that
/// followed was 1/5 or 2/5 with "progress no", against workspaces holding
/// verified exact values and exhaustive enumerations. The judge was scoring
/// silence.
#[test]
fn the_judge_is_shown_what_the_attempt_wrote_even_when_it_reported_nothing()
-> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-judge-evidence");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::create_dir_all(root.join("research/approaches"))?;
    std::fs::write(root.join("code/out/exact_pn.json"), "{}")?;
    std::fs::write(root.join("code/out/verification_run.txt"), "ALL CHECKS PASS")?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        "```claim\nid: p4-400\nstatement: p(4,400) = 521/1020.\nholds-here: yes\n\
         status: checked\n```\n",
    )?;
    std::fs::write(root.join("research/approaches/dp.md"), "an idea")?;
    std::fs::create_dir_all(root.join("research/backward"))?;
    std::fs::write(
        root.join("research/backward/reduction.md"),
        "```skeleton\ngoal: p(4,400)\nimplies: the two lemmas combine\n```\n\n\
         ```gap\nid: G-open\nlemma: the recurrence terminates\nstatus: open\n```\n\n\
         ```gap\nid: G-done\nlemma: p(4,400) = 521/1020\nstatus: discharged\n\
         discharged-by: p4-400\n```\n",
    )?;

    let brief = evidence_briefing(&root);
    assert!(
        brief.contains("2 file(s) a program produced"),
        "the output count must reach the judge: {brief}"
    );
    assert!(
        brief.contains("1 established here"),
        "a computed claim must count as established: {brief}"
    );
    assert!(brief.contains("approaches proposed: 1"));
    // What separates an investigation closing in on a theorem from one
    // accumulating verified data beside it.
    assert!(
        brief.contains("1 open, 1 discharged"),
        "the judge must see how much of a proof the run now has: {brief}"
    );
    // The instruction matters as much as the counts: a judge given numbers and
    // no reading of them scores the silent report it can see.
    assert!(brief.contains("reported nothing and left work here"));
    Ok(())
}

/// A workspace with nothing in it must not read as evidence of work.
#[test]
fn an_empty_workspace_offers_the_judge_no_comfort() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-judge-evidence-empty");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root)?;
    let brief = evidence_briefing(&root);
    assert!(brief.contains("0 file(s) a program produced"));
    assert!(brief.contains("0 established here"));
    Ok(())
}

/// A fast method nobody checked against the oracle is not a result.
///
/// Project Euler 241's `solution.py` justified its central pruning rule with a
/// claim that is false — no later sigma factor can contribute the cancelling
/// prime, when sigma(13) = 14 — and found 5 of the 9 terms below 1e8.
/// `brute.py` was in the same folder and the two were never compared.
#[test]
fn an_oracle_that_was_never_run_is_reported_to_the_judge() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-oracle-gap");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::write(root.join("code/brute.py"), "# obviously correct\n")?;
    std::fs::write(root.join("code/solution.py"), "# fast and unchecked\n")?;
    assert!(super::oracle_unchecked(&root, &super::captured_outputs(&root)));
    assert!(evidence_briefing(&root).contains("no captured output records the oracle"));

    // Capturing a run of it clears the fault: the check asks whether anything
    // records the oracle, which is a count, not a judgement about agreement.
    std::fs::write(
        root.join("code/out/brute_n8.txt"),
        "brute.py -> 9 terms below 1e8\n",
    )?;
    assert!(!super::oracle_unchecked(&root, &super::captured_outputs(&root)));
    Ok(())
}

/// The fault must not fire where there is nothing to compare.
#[test]
fn an_oracle_with_no_rival_and_a_rival_with_no_oracle_are_both_quiet() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-oracle-alone");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code"))?;

    // Only the oracle: nothing faster exists to be wrong.
    std::fs::write(root.join("code/brute.py"), "# the oracle\n")?;
    assert!(!super::oracle_unchecked(&root, &super::captured_outputs(&root)));

    // Only a fast program: a missing oracle is a different fault, and
    // `oracle_prompt` is what addresses it.
    std::fs::remove_file(root.join("code/brute.py"))?;
    std::fs::write(root.join("code/solution.py"), "# fast\n")?;
    assert!(!super::oracle_unchecked(&root, &super::captured_outputs(&root)));
    Ok(())
}

/// Output captured beside its program must count as output.
///
/// The check read `code/out/` alone, which is where the layout says captured
/// output belongs. Project Euler 761 writes `code/<program>_OUTPUT.txt` instead,
/// and its `code/out/` held one empty file named `Untitled` — so the briefing
/// would have reported a run with a dozen captured outputs as having produced
/// nothing, and then accused it of never running its oracle, on a run whose
/// `brute.py` output reproduces the published circle value to eight digits.
#[test]
fn output_captured_beside_its_program_counts_as_output() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-output-beside-program");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::create_dir_all(root.join("code/__pycache__"))?;
    std::fs::write(root.join("code/brute.py"), "# the oracle\n")?;
    std::fs::write(root.join("code/solution.py"), "# fast\n")?;
    std::fs::write(root.join("code/brute_OUTPUT.txt"), "V = 4.60333885\n")?;
    std::fs::write(root.join("code/solution_OUTPUT.txt"), "V = 4.60333885\n")?;
    // Neither of these is a thing a program produced.
    std::fs::write(root.join("code/__pycache__/brute.pyc"), "bytecode")?;
    std::fs::write(root.join("code/lib.md"), "notes")?;

    let captured = super::captured_outputs(&root);
    assert_eq!(captured.len(), 2, "captured: {captured:?}");
    let brief = evidence_briefing(&root);
    assert!(brief.contains("2 file(s) a program produced"), "{brief}");
    // And the oracle fault must stay quiet: its run is recorded, one level up
    // from where the layout would have put it.
    assert!(!super::oracle_unchecked(&root, &captured));
    assert!(!brief.contains("no captured output records the oracle"), "{brief}");
    Ok(())
}

/// An oracle that ran and disagreed is the failure after the one already
/// caught, and Project Euler 761 is what it costs.
///
/// Its `code/indep_game_encoding_OUTPUT.txt` says `agree? False` on every line —
/// the run's only independent solver returns 4.14159265 for the circle against a
/// published 4.60333885 — and nothing in the runtime read a word of it. The run
/// went on holding an answer supported by one route while the file that would
/// have said so sat unread beside it.
#[test]
fn an_output_that_records_a_failed_check_reaches_the_judge() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-disagreement");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code"))?;
    std::fs::write(root.join("code/indep.py"), "# an independent route\n")?;
    std::fs::write(
        root.join("code/indep_OUTPUT.txt"),
        "CIRCLE  V* = 4.14159265   oracle 4.60333885   agree?  False\n",
    )?;

    let brief = evidence_briefing(&root);
    assert!(brief.contains("1 captured output(s) record a check"), "{brief}");
    assert!(brief.contains("code/indep_OUTPUT.txt"), "{brief}");
    assert!(brief.contains("supported by one route, not two"), "{brief}");
    Ok(())
}

/// A row of an enumeration reading FAIL is a result, not a broken check.
///
/// Project Euler 761's `patseq_deg_phi_extend_OUTPUT.txt` has
/// `20  -  FAIL  -  -  NotAlgebraic` among twenty-three passing rows, because
/// n=20 genuinely is not algebraic there. Reading a bare FAIL as a failed
/// comparison would raise the alarm on every run that enumerates cases
/// honestly, which is the fastest way to have the alarm ignored.
#[test]
fn a_classification_row_reading_fail_is_not_a_disagreement() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-disagreement-quiet");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code"))?;
    std::fs::write(root.join("code/patseq.py"), "# enumerate\n")?;
    std::fs::write(
        root.join("code/patseq_OUTPUT.txt"),
        "19  8  18  18  True   exact\n20  -  FAIL  -  -  NotAlgebraic\n21  9  12  12  True  exact\n",
    )?;
    let brief = evidence_briefing(&root);
    assert!(!brief.contains("record a check that came out wrong"), "{brief}");
    Ok(())
}

/// The verdict the loop did not have. An answer nobody can second-source is a
/// result to report, not a run to keep retrying.
///
/// Project Euler 761 reached `V_hexagon = 5.05505046`, reduced it to
/// `2 + 2*sqrt(21)/3`, reproduced the formula's published anchors at n=3, n=4 and
/// n→∞, and could not close because the value rests on one Math.SE answer while
/// Abel et al. list regular n-gons with n>4 as open. With only SOLVED and
/// UNSOLVED available it was sent back to retry a derivation it had already
/// finished.
#[test]
fn an_answer_with_one_route_and_no_second_available_ends_the_run() {
    let mut current = state();
    current.attempts = 3;
    current.unverified = UNVERIFIED_THRESHOLD;
    // The unproductive count is what an UNVERIFIED run accumulates by
    // construction — it keeps reaching the answer it already had — so the
    // arm has to win against a state that would otherwise diversify.
    current.unproductive = STUCK_THRESHOLD;
    assert_eq!(route(&current, &chisel()), Route::Reported);
    assert!(current.outcome().contains("not independently verified"));
}

/// Said once it is an attempt reporting what it could not find; the run gets
/// another go with that as the lesson before it becomes the finding.
#[test]
fn a_single_unverified_verdict_still_retries() {
    let mut current = state();
    current.attempts = 2;
    current.unverified = UNVERIFIED_THRESHOLD - 1;
    assert_eq!(route(&current, &chisel()), Route::Retry);
}

/// UNVERIFIED carries SOLVED's evidence bar and clears the moment a reflection
/// stops saying it, so one hedged reply in the middle of a run cannot
/// accumulate toward ending it.
#[test]
fn the_unverified_count_needs_a_program_and_resets() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-unverified-evidence");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root)?;

    let mut current = state();
    // No program on disk: an answer nothing computed is not an answer, however
    // it was qualified.
    record_verdict("VERDICT: UNVERIFIED\nPROGRESS: NO", None, Some(&root), &mut current);
    assert_eq!(current.unverified, 0);

    std::fs::write(root.join("solution.py"), "print(5.05505046)\n")?;
    record_verdict("VERDICT: UNVERIFIED\nPROGRESS: NO", None, Some(&root), &mut current);
    assert_eq!(current.unverified, 1);
    assert!(!current.solved, "a qualified close is not a verified one");

    record_verdict("VERDICT: UNSOLVED\nPROGRESS: YES", None, Some(&root), &mut current);
    assert_eq!(current.unverified, 0, "a different verdict clears the count");
    Ok(())
}

/// A reflection that reports SOLVED and PROGRESS: NO contradicts itself, and
/// the loop must not end on it.
///
/// This is not hypothetical. A live Gilbreath run ended here: its `goals` agent
/// timed out, the salvage path re-ran an already-queued script that
/// re-confirmed an already-hand-checked refutation, and the reflection wrote
/// SOLVED over PROGRESS: NO. The evidence bar did not catch it, because the
/// salvage really had run a program — what no file on disk can show is that the
/// program established nothing the run did not already have. The reflection
/// itself knew, and said so in the lesson it wrote for the next attempt, but by
/// then the verdict had routed the run to `done` and the container exited 0.
#[test]
fn solved_needs_the_reflection_to_agree_it_progressed() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-solved-progress-guard");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root)?;
    // The evidence bar is satisfied throughout: this test is about the case
    // where a program exists and ran, which is exactly when the guard matters.
    std::fs::write(root.join("solution.py"), "print(5.05505046)\n")?;

    let mut current = state();
    record_verdict("VERDICT: SOLVED\nPROGRESS: NO", None, Some(&root), &mut current);
    assert!(
        !current.solved,
        "SOLVED beside PROGRESS: NO is self-contradictory and must not end the run"
    );
    assert!(
        current
            .lessons
            .iter()
            .any(|lesson| lesson.contains("PROGRESS: NO")),
        "the rejection must reach the next attempt as a lesson, not vanish"
    );
    assert_eq!(
        current.unproductive, 1,
        "a rejected close still counts as an unproductive attempt"
    );

    // The same verdict with the contradiction removed ends the run, so the
    // guard rejects the incoherent reply rather than SOLVED itself.
    record_verdict("VERDICT: SOLVED\nPROGRESS: YES", None, Some(&root), &mut current);
    assert!(
        current.solved,
        "a coherent SOLVED with a program on disk still closes the loop"
    );
    Ok(())
}

/// The seeded README of an empty folder is not a proposal.
///
/// `workspace/template` seeds `research/approaches/` and `research/threads/` so
/// the inventor finds the directory its prompt names — PE620's spent eight model
/// calls and then hit `research/approaches is not a directory`. Each seeded
/// folder needs a file for git to track it, and counting that file would tell
/// the judge every run had proposed an approach before doing anything.
#[test]
fn seeded_scaffolding_is_not_counted_as_work() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-scaffolding");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/approaches"))?;
    std::fs::create_dir_all(root.join("research/threads"))?;
    std::fs::write(root.join("research/approaches/README.md"), "what goes here")?;
    std::fs::write(root.join("research/threads/README.md"), "what goes here")?;

    let brief = evidence_briefing(&root);
    assert!(brief.contains("approaches proposed: 0"), "{brief}");
    assert!(brief.contains("threads open: 0"), "{brief}");

    // A real proposal counts.
    std::fs::write(root.join("research/approaches/conformal-map.md"), "an idea")?;
    assert!(
        evidence_briefing(&root).contains("approaches proposed: 1"),
        "a written approach must count"
    );
    Ok(())
}

/// Output that established something and reached no claim is reported.
///
/// The claim ledger is what the planning roles read; a result left in a
/// captured file reaches nobody and the next attempt does the work again. The
/// magic-square-of-squares run proved its parametrisation complete by an exact
/// rank computation, verified both literature near-misses digit by digit, and
/// scanned four million grids — and its ledger held three rows, none of them
/// the run's own, through a judge verdict and a reflection.
#[test]
fn results_that_reached_no_claim_are_reported_to_the_judge() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-unclaimed");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::write(root.join("code/scan.py"), "# the scan\n")?;
    std::fs::write(root.join("code/out/scan.txt"), "rank 7, kernel dimension 2\n")?;

    let brief = evidence_briefing(&root);
    assert!(brief.contains("the claim ledger records nothing this run established"), "{brief}");

    // One established claim clears it: the run is using the ledger.
    std::fs::write(
        root.join("code/out/NOTES.md"),
        "```claim\nid: rank-seven\nstatement: The incidence matrix has rank 7.\n\
         holds-here: yes\nstatus: checked\n```\n",
    )?;
    assert!(
        !evidence_briefing(&root).contains("records nothing this run established"),
        "an established claim clears the fault"
    );
    Ok(())
}

/// A run that has computed nothing yet is not accused of hiding results.
#[test]
fn a_run_with_no_output_is_not_told_its_ledger_is_empty() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-unclaimed-empty");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code"))?;
    std::fs::write(root.join("code/scan.py"), "# written, never run\n")?;
    assert!(
        !evidence_briefing(&root).contains("records nothing this run established"),
        "the fault needs captured output to fire"
    );
    Ok(())
}


/// The property the diversify fan-out rests on: arms write disjoint slots, so
/// the order they are folded in cannot change the state they produce.
///
/// The engine now folds them one at a time through `loop_steps::fold_arm`
/// rather than concurrently through a reducer, and the property is what makes
/// that substitution safe rather than merely convenient.
#[test]
fn arm_findings_merge_to_the_same_state_in_any_order() {
    let findings = [
        Finding::new(Slot::Library, "papers"),
        Finding::new(Slot::Digest, "what they say"),
        Finding::new(Slot::Patterns, "a regularity"),
        Finding::new(Slot::Grounding, "already known"),
        Finding::new(Slot::Chosen, "try the other reduction"),
    ];

    let fold = |order: &[usize]| {
        let mut state = SolutionState::new("problem");
        for index in order {
            state.diversify_mut().set(findings[*index].clone());
        }
        state.diversify().sections().map(|(_, body)| body.to_string())
    };

    assert_eq!(fold(&[0, 1, 2, 3, 4]), fold(&[4, 3, 2, 1, 0]));
    assert_eq!(fold(&[0, 1, 2, 3, 4]), fold(&[2, 0, 4, 1, 3]));
}

/// The merge is the only node that reads every slot, and the only one that
/// clears them. A diversify that inherited the last one's findings would merge
/// a stale arm's report into a briefing it has nothing to do with.
#[test]
fn the_merge_folds_the_slots_and_then_empties_them() {
    let mut state = SolutionState::new("problem");
    state.unproductive = 3;
    state.computational = 2;
    state.fresh_context = "already carried".to_string();
    for finding in [
        Finding::new(Slot::Library, "papers"),
        Finding::new(Slot::Patterns, "a regularity"),
    ] {
        state.diversify_mut().set(finding);
    }

    let merged = diversify_merge(state);

    assert!(merged.fresh_context.contains("already carried"));
    assert!(merged.fresh_context.contains("papers"));
    assert!(merged.fresh_context.contains("a regularity"));
    // Both counters that can route to a diversify are cleared, or the very next
    // reflection routes straight back here.
    assert_eq!(merged.unproductive, 0);
    assert_eq!(merged.computational, 0);
    assert!(
        merged
            .diversify()
            .sections()
            .iter()
            .all(|(_, body)| body.is_empty())
    );
}

/// BANKED is checked against the workspace, not against the reply.
///
/// The verdict exists because `solved` was binary: a run that proved a weakened
/// case, established a conditional result, or ruled a method out with a reason
/// had one word available to it, and that word was UNSOLVED. Greenfeld and Tao
/// published two no-go results before the periodic tiling counterexample and
/// the 2021 one is what told them their encoding could not work — scored here,
/// both would have read as failures.
///
/// But it counts as progress, and progress resets `unproductive`, which is the
/// only route into `diversify`. So a verdict a model could assert freely would
/// let a stuck run keep itself out of diversification indefinitely by claiming
/// a small win every time. It is honoured only when the claim ledger grew.
#[test]
fn banked_counts_as_progress_only_when_the_claim_ledger_grew() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-banked");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;

    let mut current = state();
    current.unproductive = 2;

    // Claimed with nothing new in the ledger: not progress, and the run is told
    // exactly what it failed to do rather than being left to guess.
    record_verdict("VERDICT: BANKED\nPROGRESS: NO", None, Some(&root), &mut current);
    assert_eq!(current.banked, 0, "an unbacked BANKED banks nothing");
    assert_eq!(current.unproductive, 3, "and it does not reset the stuck count");
    assert!(
        current
            .lessons
            .iter()
            .any(|lesson| lesson.contains("no new claim reached")),
        "the lesson must say what was missing: {:?}",
        current.lessons
    );

    // The same verdict, with the result actually written down as a claim.
    std::fs::write(
        root.join("code/out/NOTES.md"),
        "# Result\n\n```claim\nid: n-at-most-14\nstatement: The bound holds for n <= 14.\n\
         holds-here: yes\nstatus: checked\n```\n",
    )?;
    record_verdict("VERDICT: BANKED\nPROGRESS: NO", None, Some(&root), &mut current);
    assert_eq!(current.banked, 1);
    assert_eq!(current.unproductive, 0, "banking a result is progress");
    assert!(!current.solved, "and is never the goal");
    Ok(())
}

/// Banking the same result twice is not progress twice.
///
/// The counter is a high-water mark of what the ledger holds, so a second
/// BANKED over an unchanged ledger is the same claim being reported again —
/// which is precisely the shape that would keep a stuck run out of diversify.
#[test]
fn banking_an_unchanged_ledger_a_second_time_is_not_progress() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-banked-twice");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        "# Result\n\n```claim\nid: one-case\nstatement: The case p=2 is settled.\n\
         holds-here: yes\nstatus: checked\n```\n",
    )?;

    let mut current = state();
    record_verdict("VERDICT: BANKED\nPROGRESS: NO", None, Some(&root), &mut current);
    assert_eq!(current.banked, 1);

    record_verdict("VERDICT: BANKED\nPROGRESS: NO", None, Some(&root), &mut current);
    assert_eq!(current.banked, 1, "the same claim is not a second result");
    assert_eq!(current.unproductive, 1, "so the attempt was unproductive");
    Ok(())
}

/// A banked result must never end the run, whatever else the reply says.
#[test]
fn banked_is_not_a_close() {
    let mut current = state();
    record_verdict("VERDICT: BANKED\nPROGRESS: YES", None, None, &mut current);
    assert!(!current.solved);
    assert_eq!(current.unverified, 0, "it is not a qualified close either");
    assert_ne!(route(&current, &chisel()), Route::Solved);
}

/// The control school is today's runtime under a name, and this is what that
/// has to mean numerically.
///
/// Every boundary the ladder has, asserted against the constants themselves
/// rather than against `chisel()`, so the two cannot agree by both being wrong.
/// If `Thresholds::chisel` ever stopped reading the constants — or read one of
/// them into the wrong field, which is the mistake a struct of seven `usize`s
/// invites — the run would keep working and every routing test above would keep
/// passing, because they would all be asking about the same drifted number.
#[test]
fn the_control_school_routes_on_the_constants_themselves() {
    let at = |attempts, blocked, unproductive, computational, unverified| {
        let mut current = state();
        current.attempts = attempts;
        current.blocked = blocked;
        current.unproductive = unproductive;
        current.computational = computational;
        current.unverified = unverified;
        route(&current, &chisel())
    };
    assert_eq!(at(0, BLOCKED_THRESHOLD, 0, 0, 0), Route::Blocked);
    assert_eq!(at(0, BLOCKED_THRESHOLD - 1, 0, 0, 0), Route::Retry);
    assert_eq!(at(MAX_ATTEMPTS, 0, 0, 0, 0), Route::Solved);
    assert_eq!(at(MAX_ATTEMPTS - 1, 0, 0, 0, 0), Route::Retry);
    assert_eq!(at(0, 0, 0, 0, UNVERIFIED_THRESHOLD), Route::Reported);
    assert_eq!(at(0, 0, 0, 0, UNVERIFIED_THRESHOLD - 1), Route::Retry);
    assert_eq!(at(0, 0, STUCK_THRESHOLD, 0, 0), Route::Diversify);
    assert_eq!(at(0, 0, STUCK_THRESHOLD - 1, 0, 0), Route::Retry);
    assert_eq!(at(0, 0, 0, COMPUTATIONAL_THRESHOLD, 0), Route::Diversify);
    assert_eq!(at(0, 0, 0, COMPUTATIONAL_THRESHOLD - 1, 0), Route::Retry);
}

/// The whole reason a school owns its thresholds.
///
/// `research/mathematicians/12-cross-cutting.md` records that the rising sea is
/// *"unaffordable under `MAX_ATTEMPTS = 8` and `STUCK_THRESHOLD = 2`"*, because
/// a method whose goal deliberately does not move for a long time is
/// indistinguishable, to the unproductive counter, from a run that is stuck. So
/// the test is not that a number can be changed; it is that at the exact count
/// where the control gives up on the method, the patient school is still
/// working on it.
#[test]
fn a_patient_school_retries_where_the_control_diversifies() {
    let patient = ALL
        .iter()
        .find(|school| school.slug == "rising-sea")
        .expect("the rising sea school is registered");
    assert!(
        patient.thresholds.stuck > chisel().stuck,
        "the rising sea school has no longer leash than the control"
    );

    let mut current = state();
    current.unproductive = chisel().stuck;
    assert_eq!(route(&current, &chisel()), Route::Diversify);
    assert_eq!(
        route(&current, &patient.thresholds),
        Route::Retry,
        "the patient school abandons its method at the control's count"
    );

    // Still bounded, and by its own number rather than by nothing.
    current.unproductive = patient.thresholds.stuck;
    assert_eq!(route(&current, &patient.thresholds), Route::Diversify);
}

/// What an attempt is required to end with, and in which order.
///
/// The loop asked for an executed program and said nothing about the kernel, so
/// a run's whole output could be programs and prose — evidence, all of it, and
/// none of it the thing itself. The program requirement stays: it is what
/// stopped attempts that ended in notes. What changes is that a statement now
/// comes first and the program is evidence *for* one.
#[test]
fn an_attempt_is_required_to_reach_the_kernel_and_to_execute() {
    use super::attempt_prompt;

    let state = SolutionState::new("find the cycle lengths");
    let prompt = attempt_prompt(&state, "", "", "", "", "");

    let lean = prompt.find("`lean_check`").expect("the kernel is required");
    let program = prompt
        .find("program written to the workspace")
        .expect("an executed program is still required");
    assert!(lean < program, "the statement leads: {prompt}");
    assert!(
        prompt.contains("evidence for"),
        "a program is evidence for a statement rather than a result: {prompt}"
    );
    assert!(
        prompt.contains("lean_prover"),
        "and the attempt is told who writes the Lean: {prompt}"
    );
}

/// The first attempt opens two runs beside itself, and the second is the one
/// nothing else in an early run would produce: `verify` schedules the kernel
/// against a statement graph and `mill` against digested notes, and an early
/// run has neither.
#[test]
fn the_opening_formalisation_asks_for_a_statement_and_not_a_proof() {
    use super::statement_prompt;

    let prompt = statement_prompt("find the cycle lengths");

    assert!(prompt.contains("code/lean/Lib/Statement.lean"), "{prompt}");
    assert!(prompt.contains(":= by sorry"), "{prompt}");
    assert!(prompt.contains("not being asked to prove"), "{prompt}");
    assert!(prompt.contains("lean_check"), "{prompt}");
}
