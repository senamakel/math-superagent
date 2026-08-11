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
