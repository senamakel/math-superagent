//! Unit tests for the shared run budget.

use tinyagents::harness::limits::LimitBehavior;

use super::RunBudget;

#[test]
fn default_budget_is_far_above_the_tinyagents_defaults() {
    let budget = RunBudget::default();
    assert!(budget.max_model_calls > 25);
    assert!(budget.max_tool_calls > 50);
    assert!(budget.run_timeout > budget.tool_timeout);
}

#[test]
fn tool_cap_stays_out_of_reach_of_the_model_cap() {
    // Only the model-call cap stops gracefully in the vendored agent loop, so
    // the tool cap must not be reachable by parallel tool calling first.
    let budget = RunBudget::default();
    assert!(budget.max_tool_calls >= budget.max_model_calls * 8);
}

#[test]
fn policy_stops_with_partial_results_and_captures_payloads() {
    let policy = RunBudget::default().run_policy();
    assert_eq!(policy.limits.behavior, LimitBehavior::StopWithPartial);
    assert!(policy.capture.model_io);
    assert!(policy.capture.tool_io);
    assert_eq!(
        policy.limits.max_wall_clock_ms,
        Some(RunBudget::default().run_timeout_ms())
    );
}

#[test]
fn the_retry_ladder_is_longer_and_slower_than_the_vendored_default() {
    let policy = RunBudget::default().run_policy();
    // A transport failure that drops a stream mid-body needs more than the
    // vendored four attempts backing off from 200ms.
    assert!(policy.retry.max_attempts >= 6);
    assert!(policy.retry.initial_backoff_ms >= 1_000);
    assert!(
        policy.retry.jitter,
        "concurrent runs must not retry in lockstep"
    );
    // The loop takes the stricter cap, so this one has to be raised too or the
    // longer ladder is silently ignored.
    assert!(policy.limits.max_retries_per_call >= policy.retry.max_attempts - 1);
}

#[test]
fn millisecond_conversions_match_the_configured_durations() {
    let budget = RunBudget::default();
    assert_eq!(
        budget.tool_timeout_ms(),
        budget.tool_timeout.as_secs() * 1_000
    );
    assert_eq!(
        budget.run_timeout_ms(),
        budget.run_timeout.as_secs() * 1_000
    );
}

#[test]
fn a_turn_is_bounded_so_wall_clock_is_bounded() {
    // Generation time is linear in output length, so an uncapped turn is an
    // uncapped wall clock. A live turn reached 9,361 tokens and 2.9 minutes.
    let budget = RunBudget::default();
    assert!(budget.max_turn_output_tokens > 0);
    // Above the largest observed real turn (9,361). A cap that trips on
    // ordinary work truncates the model mid-answer and forces a retry, which
    // costs more than the long turn it was meant to prevent.
    assert!(
        budget.max_turn_output_tokens > 9_361,
        "a cap that trips routinely causes truncation retries"
    );
    // ...but still a ceiling, not unlimited.
    assert!(budget.max_turn_output_tokens <= 32_000);
}

#[test]
fn a_judging_budget_is_narrowed_but_never_widened() {
    // The judge sits on the critical path of every attempt, and its job is to
    // read a report and answer in four lines. A live judge given an
    // investigation's budget spent four minutes and fifteen model calls
    // reading the programs the attempt had written.
    let full = RunBudget::default();
    let judging = full.for_judging();

    assert!(judging.max_model_calls < full.max_model_calls);
    assert!(judging.run_timeout < full.run_timeout);
    assert!(
        judging.max_tool_calls > judging.max_model_calls,
        "one turn can request several reads, so the graceful cap stays the model one"
    );

    // A run already tighter than the judging bounds keeps its own: this
    // narrows a budget and must never hand one more room than it was given.
    let tight = RunBudget {
        max_model_calls: 3,
        max_tool_calls: 4,
        run_timeout: std::time::Duration::from_secs(30),
        ..full
    };
    let narrowed = tight.for_judging();
    assert_eq!(narrowed.max_model_calls, 3);
    assert_eq!(narrowed.max_tool_calls, 4);
    assert_eq!(narrowed.run_timeout, std::time::Duration::from_secs(30));
}

#[test]
fn a_housekeeping_budget_is_narrowed_but_never_widened() {
    // Filing is bounded work — read a listing, write a row per file — and the
    // default budget is sized for an investigation. Two live runs spent 60%
    // and 64% of every model call inside the organizer, not because it ran
    // often (nine and ten times) but because one run spent 62 model calls
    // tidying while the solve had spent 14 on the mathematics.
    let full = RunBudget::default();
    let filing = full.for_housekeeping();

    assert!(filing.max_model_calls < full.max_model_calls);
    assert!(filing.run_timeout < full.run_timeout);
    // The observed 62-call run must not fit inside the new cap, or the cap
    // does not bind the behaviour it was written for.
    assert!(filing.max_model_calls < 62);
    assert!(
        filing.max_tool_calls > filing.max_model_calls,
        "one turn can request several reads, so the graceful cap stays the model one"
    );
    // A judge is tighter still: it answers in four lines, where filing walks
    // several folders.
    assert!(filing.max_model_calls > full.for_judging().max_model_calls);

    // Narrows only. An environment override already below these keeps its own.
    let tight = RunBudget {
        max_model_calls: 3,
        max_tool_calls: 4,
        run_timeout: std::time::Duration::from_secs(30),
        ..full
    };
    let narrowed = tight.for_housekeeping();
    assert_eq!(narrowed.max_model_calls, 3);
    assert_eq!(narrowed.max_tool_calls, 4);
    assert_eq!(narrowed.run_timeout, std::time::Duration::from_secs(30));
}
