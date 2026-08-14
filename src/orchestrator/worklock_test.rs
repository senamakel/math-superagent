//! Unit tests for the workspace write and commit locks.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::atomic::{AtomicUsize, Ordering};

use super::{commits, writes};

/// The write lock admits one holder at a time.
///
/// Written as a peak-concurrency count rather than as an ordering assertion,
/// because ordering between tasks is not what the lock promises and a test that
/// asserted it would be flaky. What it promises is that two writers are never
/// inside at once, which is exactly what a torn ledger requires.
#[tokio::test]
async fn writes_admit_one_holder_at_a_time() {
    let inside = Arc::new(AtomicUsize::new(0));
    let peak = Arc::new(AtomicUsize::new(0));
    let mut tasks = Vec::new();
    for _ in 0..16 {
        let inside = Arc::clone(&inside);
        let peak = Arc::clone(&peak);
        tasks.push(tokio::spawn(async move {
            let _guard = writes().await;
            let now = inside.fetch_add(1, Ordering::SeqCst) + 1;
            peak.fetch_max(now, Ordering::SeqCst);
            tokio::task::yield_now().await;
            inside.fetch_sub(1, Ordering::SeqCst);
        }));
    }
    for task in tasks {
        task.await.expect("a locked task must not panic");
    }
    assert_eq!(
        peak.load(Ordering::SeqCst),
        1,
        "two writers were inside the workspace write lock at once"
    );
}

/// The commit lock is a different lock, so holding one does not hold the other.
///
/// The property that matters: a writer holding [`writes`] must not stop the
/// checkpoint middleware from committing, because the middleware runs on every
/// agent in the run and a stall there stalls everything.
#[tokio::test]
async fn commits_are_independent_of_writes() {
    let held = writes().await;
    let commit = tokio::time::timeout(std::time::Duration::from_secs(5), commits()).await;
    assert!(
        commit.is_ok(),
        "the commit lock must not be blocked by a held write lock"
    );
    drop(held);
}
