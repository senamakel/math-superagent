//! Unit tests for the shared run budget.

use tinyagents::harness::limits::LimitBehavior;

use super::{RunBudget, capture_for, telemetry_from};

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
fn a_delegating_role_outlasts_the_children_it_waits_on() {
    // `goals` runs its children inside its own clock, so sharing their ceiling
    // meant one child spending its allowance exhausted the parent's. This is
    // the same ordering `run_timeout > tool_timeout` already asserts, one
    // level up. On the fleet that produced it, 52 of 57 `goals` runs died on
    // the wall clock with the call caps nowhere near binding.
    let base = RunBudget::default();
    let orchestration = base.for_orchestration();
    assert!(orchestration.run_timeout > base.run_timeout);
    // The tool clock stays the inner bound, so a slow tool still returns its
    // output instead of failing the run.
    assert!(orchestration.run_timeout > orchestration.tool_timeout);
}

#[test]
fn orchestration_widens_only_the_run_clock() {
    // The call caps stay the graceful trip, and widening authority was never
    // the point: a failing wall clock discards the work, a call cap does not.
    let base = RunBudget::default();
    let orchestration = base.for_orchestration();
    assert_eq!(orchestration.max_model_calls, base.max_model_calls);
    assert_eq!(orchestration.max_tool_calls, base.max_tool_calls);
    assert_eq!(orchestration.tool_timeout, base.tool_timeout);
    assert_eq!(
        orchestration.max_turn_output_tokens,
        base.max_turn_output_tokens
    );
}

#[test]
fn orchestration_keeps_an_operators_larger_run_clock() {
    // `max`, not assignment: an operator who raised MATH_AGENT_RUN_MINUTES
    // past this ceiling meant it.
    let base = RunBudget {
        run_timeout: std::time::Duration::from_hours(10),
        ..RunBudget::default()
    };
    assert_eq!(base.for_orchestration().run_timeout, base.run_timeout);
}

#[test]
fn policy_stops_with_partial_results_rather_than_erroring() {
    // Capture is deliberately not asserted here: it follows the telemetry
    // switch rather than the budget, and reads the environment. What it does
    // for a given posture is `nothing_is_retained_for_a_reader_that_does_not_exist`.
    let policy = RunBudget::default().run_policy();
    assert_eq!(policy.limits.behavior, LimitBehavior::StopWithPartial);
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
    // Above what a turn actually needs, where "needs" counts the hidden
    // reasoning channel and not just the visible answer. Across 4,180 accounted
    // calls on a live run, 77.8% of output tokens were reasoning, and every
    // turn that hit the old ceiling read `out=24000` with
    // `reasoning_tokens=23999` — one visible token. A cap that trips on
    // ordinary work truncates mid-thought and costs more than the long turn it
    // was meant to prevent.
    assert!(
        budget.max_turn_output_tokens >= 40_000,
        "a cap that trips routinely causes truncation retries"
    );
    // ...but still a ceiling, not unlimited. Generation is linear in length, so
    // this is the wall clock for one turn.
    assert!(budget.max_turn_output_tokens <= 50_000);
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
    // The wall clock must NOT be narrowed. It fails a run outright rather than
    // stopping with partial results: a ten-minute housekeeping ceiling killed
    // two live organizer runs after 20 and 13 model calls and threw away every
    // row they had written. The graceful cap has to be the one that trips.
    assert_eq!(filing.run_timeout, full.run_timeout);
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

#[test]
fn an_invention_budget_is_a_floor_not_a_widening() {
    // It was a widening when the default was 12,000. Measuring the reasoning
    // channel raised the default past it, so on a default run this is inert —
    // and that is correct, not dead code. It is a floor: an operator who
    // narrows `MATH_AGENT_TURN_OUTPUT_TOKENS` for a cheap run narrows every
    // role, and the inventor is the one whose product is the long turn.
    let full = RunBudget::default();
    let invention = full.for_invention();

    assert_eq!(
        invention.max_turn_output_tokens, full.max_turn_output_tokens,
        "the default already exceeds the invention floor"
    );
    // Authority is untouched either way. A turn cap says a long answer is
    // legitimate, not that the inventor may wander further than any other role.
    assert_eq!(invention.max_model_calls, full.max_model_calls);
    assert_eq!(invention.max_tool_calls, full.max_tool_calls);
    assert_eq!(invention.run_timeout, full.run_timeout);
    assert_eq!(invention.tool_timeout, full.tool_timeout);

    // The floor bites when an operator narrows below it, which is the whole
    // reason it is kept.
    let narrowed = RunBudget {
        max_turn_output_tokens: 8_000,
        ..full
    };
    assert!(narrowed.for_invention().max_turn_output_tokens > 12_000);
}

#[test]
fn an_operator_who_raised_the_turn_cap_keeps_their_value() {
    // `max`, not assignment: unlike the narrowing budgets, an override above
    // this one is not a mistake to be corrected.
    let generous = RunBudget {
        max_turn_output_tokens: 64_000,
        ..RunBudget::default()
    };
    assert_eq!(generous.for_invention().max_turn_output_tokens, 64_000);
}

#[test]
fn nothing_is_retained_for_a_reader_that_does_not_exist() {
    // Captured payloads go into the in-memory event journal, which is read
    // once when the run *ends*, so nothing trims it while the run is going.
    // Each `ModelCompleted` carries the whole request — the whole conversation
    // so far — so call n retains a copy of what calls 1..n-1 already retained,
    // and retention is quadratic in the number of model calls. Measured on a
    // live `conjectures/hilbert-16` run: 337 calls, 1.8 GiB of anonymous
    // memory, ~1.9 MiB/s and monotonic. With telemetry off nobody ever reads
    // those bytes, so keeping them is pure cost.
    assert!(capture_for(false).is_disabled());
    assert!(!capture_for(true).is_disabled());
}

#[test]
fn telemetry_is_off_unless_it_is_switched_on_and_configured() {
    // Off by default while the retention above is unfixed. Both halves are
    // required: a switch with no credentials would capture payloads for an
    // exporter that cannot be built, which is the worst of both.
    assert!(telemetry_from(Some("on"), false, true));
    assert!(telemetry_from(Some("on"), true, false));
    assert!(!telemetry_from(Some("on"), false, false));
    assert!(!telemetry_from(None, true, true));
    assert!(!telemetry_from(Some("off"), true, true));
    // Neither an empty value nor a typo is an opt-in: the cost is paid by the
    // run, not by whoever set the variable.
    assert!(!telemetry_from(Some(""), true, true));
    assert!(!telemetry_from(Some("yes"), true, true));
    // Spelling and spacing a person would reasonably use still work.
    assert!(telemetry_from(Some(" ON "), true, true));
    assert!(telemetry_from(Some("true"), true, true));
}
