//! Unit tests for the team runtime.
#![allow(clippy::expect_used)]

use std::sync::Arc;
use std::sync::atomic::{AtomicU64, Ordering};
use std::time::Duration;

use super::{Cycle, TeamBudget, spawn};

fn budget(max_cycles: u64, wall_clock: Duration) -> TeamBudget {
    TeamBudget {
        max_cycles,
        wall_clock,
    }
}

/// Waits until `check` holds or the deadline passes, without sleeping the
/// whole interval on the common case.
async fn settle(check: impl Fn() -> bool) -> bool {
    for _ in 0..200 {
        if check() {
            return true;
        }
        tokio::time::sleep(Duration::from_millis(10)).await;
    }
    check()
}

#[tokio::test]
async fn a_team_stops_at_its_cycle_budget_rather_than_running_forever() {
    // A team's work is open-ended — the research team always has one more
    // source it could fetch — so the stop cannot depend on the team choosing
    // to stop.
    let ran = Arc::new(AtomicU64::new(0));
    let counter = ran.clone();
    let team = spawn(
        "research",
        budget(3, Duration::from_secs(60)),
        None,
        move |_inbox| {
            let counter = counter.clone();
            async move {
                counter.fetch_add(1, Ordering::Relaxed);
                Cycle::Worked
            }
        },
    );

    assert!(
        settle(|| ran.load(Ordering::Relaxed) >= 3).await,
        "the team should have run its three cycles"
    );
    assert!(
        settle(|| team.cycles() == 3).await,
        "got {} cycles",
        team.cycles()
    );
    // And no more: give it room to overrun if it were going to.
    tokio::time::sleep(Duration::from_millis(80)).await;
    assert_eq!(ran.load(Ordering::Relaxed), 3, "the budget is a ceiling");
}

#[tokio::test]
async fn a_cancelled_team_stops_without_finishing_its_budget() {
    // The normal ending: the solve finished, so the support teams stop even
    // though they had cycles left.
    let ran = Arc::new(AtomicU64::new(0));
    let counter = ran.clone();
    let team = spawn(
        "background",
        budget(1_000, Duration::from_secs(60)),
        None,
        move |_inbox| {
            let counter = counter.clone();
            async move {
                counter.fetch_add(1, Ordering::Relaxed);
                Cycle::Worked
            }
        },
    );

    assert!(settle(|| ran.load(Ordering::Relaxed) >= 1).await);
    team.cancel();
    let stopped_at = ran.load(Ordering::Relaxed);
    tokio::time::sleep(Duration::from_millis(120)).await;
    assert!(
        ran.load(Ordering::Relaxed) <= stopped_at + 1,
        "a cancelled team finishes at most the cycle it was in"
    );
}

#[tokio::test]
async fn a_team_that_says_it_is_finished_is_not_asked_again() {
    let ran = Arc::new(AtomicU64::new(0));
    let counter = ran.clone();
    let _team = spawn(
        "background",
        budget(1_000, Duration::from_secs(60)),
        None,
        move |_inbox| {
            let counter = counter.clone();
            async move {
                counter.fetch_add(1, Ordering::Relaxed);
                Cycle::Finished
            }
        },
    );

    assert!(settle(|| ran.load(Ordering::Relaxed) >= 1).await);
    tokio::time::sleep(Duration::from_millis(120)).await;
    assert_eq!(ran.load(Ordering::Relaxed), 1, "Finished means finished");
}

#[tokio::test]
async fn a_busy_team_sees_its_whole_backlog_in_one_cycle() {
    // A cycle can take minutes. Trickling the backlog through one message per
    // cycle would deliver the solver's third request long after it mattered.
    let seen = Arc::new(std::sync::Mutex::new(Vec::<usize>::new()));
    let record = seen.clone();
    let team = spawn(
        "research",
        budget(1_000, Duration::from_secs(60)),
        None,
        move |inbox| {
            let record = record.clone();
            async move {
                if !inbox.is_empty() {
                    record
                        .lock()
                        .expect("recorded batches are not poisoned")
                        .push(inbox.len());
                }
                Cycle::Idle
            }
        },
    );

    for index in 0..3 {
        assert!(team.post("solver", format!("request {index}")));
    }

    assert!(
        settle(|| !seen
            .lock()
            .expect("recorded batches are not poisoned")
            .is_empty())
        .await
    );
    let batches = seen.lock().expect("recorded batches are not poisoned");
    assert_eq!(
        batches.first().copied(),
        Some(3),
        "all three messages should arrive in one cycle: {batches:?}"
    );
}

#[tokio::test]
async fn posting_to_a_team_never_blocks_the_sender() {
    // The sender is usually the solver. Stalling a solve to hand a note to a
    // busy support team inverts the priority this design exists to fix, so a
    // full inbox drops rather than waits.
    let team = spawn(
        "research",
        budget(1, Duration::from_secs(60)),
        None,
        move |_inbox| async move {
            tokio::time::sleep(Duration::from_secs(30)).await;
            Cycle::Worked
        },
    );

    let started = std::time::Instant::now();
    for index in 0..(super::INBOX_DEPTH + 8) {
        let _ = team.post("solver", format!("note {index}"));
    }
    assert!(
        started.elapsed() < Duration::from_secs(2),
        "posting took {:?}; it must not wait on the team",
        started.elapsed()
    );
}
