//! Deterministic tests for the child-run registry.
#![allow(clippy::expect_used)]

use super::*;

fn task(id: &str) -> TaskId {
    TaskId::new(id)
}

#[test]
fn a_new_run_starts_pending_and_is_neither_live_nor_terminal() {
    let store = RunStore::new();
    store
        .insert(task("agent-run-1"), "research")
        .expect("a fresh id is accepted");

    let record = store.get(&task("agent-run-1")).expect("the run is present");
    assert_eq!(record.status, RunStatus::Pending);
    assert_eq!(record.agent, "research");
    // Queued is not steerable — nothing is reading the handle yet — and not
    // finished, so an await loop keeps waiting.
    assert!(!record.status.is_live());
    assert!(!record.status.is_terminal());
}

#[test]
fn a_completed_run_carries_its_text_and_ends_an_await() {
    let store = RunStore::new();
    store.insert(task("agent-run-1"), "research").expect("insert");
    store.mark_running(&task("agent-run-1"));
    assert!(
        store
            .get(&task("agent-run-1"))
            .expect("present")
            .status
            .is_live()
    );

    store.complete(&task("agent-run-1"), RunOutcome::text("found it"));
    let record = store.get(&task("agent-run-1")).expect("present");
    assert_eq!(record.status, RunStatus::Completed);
    assert!(record.status.is_terminal());
    assert_eq!(
        record.result.and_then(|result| result.text).as_deref(),
        Some("found it")
    );
    assert!(record.error.is_none());
}

#[test]
fn a_failed_run_is_terminal_so_a_waiter_is_not_left_blocking() {
    let store = RunStore::new();
    store.insert(task("agent-run-1"), "research").expect("insert");
    store.fail(&task("agent-run-1"), "provider refused");

    let record = store.get(&task("agent-run-1")).expect("present");
    assert_eq!(record.status, RunStatus::Failed);
    // The point of the assertion: a waiter that only recognised success would
    // block until its deadline on every failed run.
    assert!(record.status.is_terminal());
    assert_eq!(record.error.as_deref(), Some("provider refused"));
}

#[test]
fn a_duplicate_id_is_refused_rather_than_overwriting_a_live_run() {
    let store = RunStore::new();
    store.insert(task("agent-run-1"), "research").expect("insert");
    store.mark_running(&task("agent-run-1"));

    let refused = store.insert(task("agent-run-1"), "prover");
    assert!(refused.is_err());
    // The first run's record survived the refusal.
    let record = store.get(&task("agent-run-1")).expect("present");
    assert_eq!(record.status, RunStatus::Running);
    assert_eq!(record.agent, "research");
}

#[test]
fn listing_is_stable_so_an_argumentless_await_repeats() {
    let store = RunStore::new();
    for id in ["agent-run-2", "agent-run-1", "agent-run-3"] {
        store.insert(task(id), "research").expect("insert");
    }
    let ids: Vec<String> = store
        .list()
        .iter()
        .map(|record| record.task_id().to_string())
        .collect();
    assert_eq!(ids, ["agent-run-1", "agent-run-2", "agent-run-3"]);
    assert_eq!(ids, {
        let again: Vec<String> = store
            .list()
            .iter()
            .map(|record| record.task_id().to_string())
            .collect();
        again
    });
}

#[test]
fn an_unknown_run_reads_as_absent_rather_than_failing_a_reporter() {
    let store = RunStore::new();
    // Every mutator is a detached task reporting on itself; there is nobody
    // left to return an error to, so an unknown id is a no-op.
    store.mark_running(&task("agent-run-9"));
    store.complete(&task("agent-run-9"), RunOutcome::text("ignored"));
    store.fail(&task("agent-run-9"), "ignored");
    assert!(store.get(&task("agent-run-9")).is_none());
}

#[test]
fn a_handle_is_reachable_until_the_run_is_deregistered() {
    let registry = SteeringRegistry::new();
    registry.register(&task("agent-run-1"), SteeringHandle::allow_all());
    assert!(registry.get(&task("agent-run-1")).is_some());

    registry.deregister(&task("agent-run-1"));
    // A handle held past the run's end would accept a redirect nothing reads.
    assert!(registry.get(&task("agent-run-1")).is_none());
}
