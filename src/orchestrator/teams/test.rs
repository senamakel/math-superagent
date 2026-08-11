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
        min_interval: Duration::ZERO,
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
        budget(3, Duration::from_mins(1)),
        None,
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
        budget(1_000, Duration::from_mins(1)),
        None,
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
        budget(1_000, Duration::from_mins(1)),
        None,
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
        budget(1_000, Duration::from_mins(1)),
        None,
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
        budget(1, Duration::from_mins(1)),
        None,
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

#[tokio::test]
async fn a_team_that_finishes_on_its_first_cycle_reports_having_run_one() {
    // A live background team replied "nothing further" immediately and the
    // console said it "stopped after 0 cycle(s)", which reads as a team that
    // never started rather than one that did its job at once.
    let team = spawn(
        "background",
        budget(1_000, Duration::from_mins(1)),
        None,
        None,
        move |_inbox| async move { Cycle::Finished },
    );

    assert!(settle(|| team.cycles() == 1).await, "got {}", team.cycles());
}

#[test]
fn a_standing_goal_treats_nothing_further_as_idle_rather_than_done() {
    // The failure this exists to stop: on a fresh workspace there is nothing
    // to tidy, the organiser truthfully said "nothing further", and the
    // background team ended for the whole run — while files accumulated for
    // two hours with nobody to index them.
    assert_eq!(
        super::Completion::Standing.nothing_further(),
        Cycle::Idle,
        "a custodial team comes back when the workspace has changed"
    );
    // Acquiring is different: once more sources stop changing the shared
    // brief, fetching more of them is waste.
    assert_eq!(
        super::Completion::Attainable.nothing_further(),
        Cycle::Finished
    );
}

#[tokio::test]
async fn a_cycle_that_changed_nothing_backs_off_however_productive_it_claims_to_be() {
    // The live failure: a background team ran seven cycles in six minutes —
    // 26 reads, 16 listings, seven index refreshes, zero descriptions —
    // reporting work every time, so it never backed off and was on course to
    // spend its whole allowance re-reading a workspace it was not changing.
    let root = std::env::temp_dir().join(format!("math-agent-team-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("temporary workspace is creatable");
    std::fs::write(root.join("goal.md"), "solve it").expect("a file is writable");

    let ran = Arc::new(AtomicU64::new(0));
    let counter = ran.clone();
    let _team = spawn(
        "background",
        budget(1_000, Duration::from_mins(1)),
        None,
        Some(root.clone()),
        move |_inbox| {
            let counter = counter.clone();
            // Claims to have worked, touches nothing.
            async move {
                counter.fetch_add(1, Ordering::Relaxed);
                Cycle::Worked
            }
        },
    );

    assert!(settle(|| ran.load(Ordering::Relaxed) >= 1).await);
    // With the claim believed, this would spin through many cycles. Backed
    // off, it manages one and then waits out the idle interval.
    tokio::time::sleep(Duration::from_millis(400)).await;
    assert!(
        ran.load(Ordering::Relaxed) <= 2,
        "spun {} cycles without changing anything",
        ran.load(Ordering::Relaxed)
    );
    let _ = std::fs::remove_dir_all(&root);
}

#[tokio::test]
async fn a_cycle_that_actually_changed_the_workspace_is_believed() {
    // The check must not punish a team that is working: a cycle that wrote a
    // file goes straight round again.
    let root = std::env::temp_dir().join(format!("math-agent-team-busy-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("temporary workspace is creatable");

    let ran = Arc::new(AtomicU64::new(0));
    let counter = ran.clone();
    let folder = root.clone();
    let _team = spawn(
        "background",
        budget(4, Duration::from_mins(1)),
        None,
        Some(root.clone()),
        move |_inbox| {
            let counter = counter.clone();
            let folder = folder.clone();
            async move {
                let index = counter.fetch_add(1, Ordering::Relaxed);
                let _ = std::fs::write(folder.join(format!("note-{index}.md")), "written");
                Cycle::Worked
            }
        },
    );

    assert!(
        settle(|| ran.load(Ordering::Relaxed) >= 4).await,
        "a productive team ran only {} cycles",
        ran.load(Ordering::Relaxed)
    );
    let _ = std::fs::remove_dir_all(&root);
}

#[tokio::test]
async fn a_custodial_team_is_paced_even_when_it_reports_work() {
    // The fingerprint check alone could not do this. Teams run concurrently
    // with the solver, so somebody has usually written a file while a cycle
    // was running, and every empty cycle was believed: a measured 1.35 cycles
    // a minute producing 20 reads, 12 listings, four refreshes and no
    // descriptions. Rate is the honest bound for work that never finishes.
    let ran = Arc::new(AtomicU64::new(0));
    let counter = ran.clone();
    let _team = spawn(
        "background",
        TeamBudget {
            max_cycles: 1_000,
            wall_clock: Duration::from_mins(1),
            min_interval: Duration::from_millis(400),
        },
        None,
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
    tokio::time::sleep(Duration::from_millis(500)).await;
    assert!(
        ran.load(Ordering::Relaxed) <= 3,
        "ran {} cycles; the floor should hold it near one per interval",
        ran.load(Ordering::Relaxed)
    );
}

#[tokio::test]
async fn a_waiting_message_skips_the_pacing_floor() {
    // Pacing exists to stop idle churn, not to delay a request that has
    // already arrived.
    let seen = Arc::new(AtomicU64::new(0));
    let counter = seen.clone();
    let team = spawn(
        "background",
        TeamBudget {
            max_cycles: 1_000,
            wall_clock: Duration::from_mins(1),
            min_interval: Duration::from_secs(30),
        },
        None,
        None,
        move |inbox| {
            let counter = counter.clone();
            async move {
                if !inbox.is_empty() {
                    counter.fetch_add(1, Ordering::Relaxed);
                }
                Cycle::Worked
            }
        },
    );

    // First cycle runs immediately and starts the floor; post during it.
    for index in 0..2 {
        team.post("solver", format!("attempt {index} learned something"));
    }
    assert!(
        settle(|| seen.load(Ordering::Relaxed) >= 1).await,
        "a queued message must not wait out a 30s pacing floor"
    );
}

#[tokio::test]
async fn an_idle_custodial_cycle_is_paced_like_a_working_one() {
    // Pacing the worked branch alone was measured and was not enough: a
    // custodial team reporting "nothing to tidy" takes the idle branch, so the
    // case most in need of a floor was the one escaping it. Two live teams ran
    // a cycle every 66 and 108 seconds against a three-minute floor.
    let ran = Arc::new(AtomicU64::new(0));
    let counter = ran.clone();
    let _team = spawn(
        "background",
        TeamBudget {
            max_cycles: 1_000,
            wall_clock: Duration::from_mins(1),
            min_interval: Duration::from_millis(600),
        },
        None,
        None,
        move |_inbox| {
            let counter = counter.clone();
            async move {
                counter.fetch_add(1, Ordering::Relaxed);
                Cycle::Idle
            }
        },
    );

    assert!(settle(|| ran.load(Ordering::Relaxed) >= 1).await);
    tokio::time::sleep(Duration::from_millis(700)).await;
    assert!(
        ran.load(Ordering::Relaxed) <= 3,
        "an idle team ran {} cycles; the floor must apply to idle too",
        ran.load(Ordering::Relaxed)
    );
}
