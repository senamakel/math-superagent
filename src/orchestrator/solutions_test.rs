//! Unit tests for the solution loop's routing policy and lesson extraction.
#![allow(clippy::expect_used)]

use super::{
    BLOCKED_THRESHOLD, COMPUTATIONAL_THRESHOLD, MAX_ATTEMPTS, Mailbox, Progress, Route,
    STUCK_THRESHOLD, SolutionState, approach_slugs, evidence_briefing, extract_lesson, kind_of,
    provider_blocked, route,
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
    assert_eq!(route(&current), Route::Diversify);
}

/// One scale-up is what an attempt looks like, not a pattern. The loop only
/// intervenes on the second.
#[test]
fn a_single_scale_up_still_retries() {
    let mut current = state();
    current.attempts = 2;
    current.computational = COMPUTATIONAL_THRESHOLD - 1;
    assert_eq!(route(&current), Route::Retry);
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
    assert_eq!(route(&current), Route::Retry);
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
    assert_eq!(route(&current), Route::Blocked);
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
    assert_eq!(route(&retry), Route::Retry, "the cycle that opens one");

    // Diversify runs the same arm one step later and awaits it; opening one
    // here too would spend two inventor runs on a single cycle.
    let mut stuck = state();
    stuck.attempts = 3;
    stuck.unproductive = STUCK_THRESHOLD;
    assert_eq!(route(&stuck), Route::Diversify);

    // A run that has stopped has nobody to hand a new line of attack to.
    let mut solved = state();
    solved.solved = true;
    assert_eq!(route(&solved), Route::Solved);

    let mut blocked = state();
    blocked.attempts = 2;
    blocked.blocked = BLOCKED_THRESHOLD;
    assert_eq!(route(&blocked), Route::Blocked);
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
    let prompt = attempt_prompt(&state, "", &observations, "");

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
    let prompt = attempt_prompt(&state, "", &observations, "");
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
    let prompt = attempt_prompt(&state, "", "", &direction);

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
    let prompt = attempt_prompt(&state, "", "", &direction);
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
