//! Long-lived teams that run beside the solution loop.
//!
//! The loop is serial by construction: attempt, judge, route, attempt again.
//! That is right for *solving*, because each attempt should be briefed by the
//! last one's lesson. It is wrong for everything around solving. Gathering
//! sources, digesting them, and keeping the workspace navigable have no reason
//! to wait their turn behind a derivation, and when they do the run spends its
//! wall clock queueing: a live run sat 56 minutes unable to start its second
//! attempt because a support agent inside the loop was still working.
//!
//! So the support roles move out of the loop and become *teams*. A team is one
//! long-lived task with its own goal, its own budget, and an inbox. It runs a
//! serial cycle — which may fan out to parallel subagents inside a cycle — then
//! checks for messages and either works again or backs off. Teams run
//! concurrently with the loop and with each other, and the only coupling is
//! what they leave on disk and what they post to one another.
//!
//! Three properties are deliberate:
//!
//! * **Per-team budgets.** `RunBudget` bounds one agent run; it cannot bound a
//!   thing that runs many. A team that exhausts its own budget stops and says
//!   so, and the others keep going. Nothing a team does may consume the
//!   solver's allowance.
//! * **Idle backoff.** A team with nothing to do sleeps rather than spinning a
//!   model call to discover it has nothing to do, which is the expensive way to
//!   find out.
//! * **A wall clock per team.** A team whose work is open-ended — the research
//!   team always has one more source it could fetch — needs a stop that does
//!   not depend on it deciding to stop.

use std::sync::Arc;
use std::sync::atomic::{AtomicU64, Ordering};
use std::time::{Duration, Instant};

use tokio::sync::mpsc;

use crate::agent::trace::RunTracer;

/// How long an idle team waits before looking for work again.
///
/// Long enough that an idle team costs nothing, short enough that a message
/// posted by the solver is picked up while it still matters.
const IDLE_BACKOFF: Duration = Duration::from_secs(20);

/// Messages queued for one team before the sender is made to wait.
///
/// A team that has fallen this far behind is not going to catch up by being
/// handed more; back-pressure onto the sender is the honest signal.
const INBOX_DEPTH: usize = 64;

/// A note passed from one team to another.
#[derive(Clone, Debug)]
pub(super) struct TeamMessage {
    /// The team that sent it, for attribution in the receiving prompt.
    pub(super) from: String,
    /// What the sender wants the receiver to know or do.
    pub(super) body: String,
}

/// What one team may spend before it stops.
///
/// Separate from [`crate::agent::budget::RunBudget`], which bounds a single
/// agent run. A team runs many, so a per-run bound says nothing about what the
/// team as a whole costs.
#[derive(Clone, Copy, Debug)]
pub(super) struct TeamBudget {
    /// Cycles the team may run.
    pub(super) max_cycles: u64,
    /// Wall clock the team may occupy, from its first cycle.
    pub(super) wall_clock: Duration,
}

impl TeamBudget {
    /// A support team's default allowance.
    pub(super) const fn support() -> Self {
        Self {
            max_cycles: 40,
            wall_clock: Duration::from_mins(90),
        }
    }
}

/// Whether a team's goal can ever be complete.
///
/// The distinction is not pedantic; collapsing it cost a live run its whole
/// background team. On a fresh workspace at t=0 there is nothing to tidy, the
/// organiser truthfully said so, and the team treated that as its goal being
/// met and stopped — for the remaining two hours, while files accumulated and
/// nobody indexed them.
///
/// A team whose work is *acquisitive* genuinely finishes: once further sources
/// stop changing the shared brief, fetching more is waste. A team whose work is
/// *custodial* never does, because the thing it maintains keeps changing
/// underneath it. For that team an empty cycle means come back later, not stop.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Completion {
    /// The goal can be reached; "nothing further" ends the team.
    Attainable,
    /// The goal is standing; "nothing further" only means idle for now.
    Standing,
}

impl Completion {
    /// Maps a cycle that reported nothing further to do.
    pub(super) const fn nothing_further(self) -> Cycle {
        match self {
            Self::Attainable => Cycle::Finished,
            Self::Standing => Cycle::Idle,
        }
    }
}

/// The handle a team's owner keeps: somewhere to post, and a way to stop it.
#[derive(Clone, Debug)]
pub(super) struct TeamHandle {
    name: String,
    sender: mpsc::Sender<TeamMessage>,
    cancelled: Arc<std::sync::atomic::AtomicBool>,
    cycles: Arc<AtomicU64>,
}

impl TeamHandle {
    /// Returns the team's name.
    pub(super) fn name(&self) -> &str {
        &self.name
    }

    /// Posts a message without waiting for the team to be free.
    ///
    /// A full inbox drops the message rather than blocking the sender: the
    /// sender is usually the solver, and stalling the solve to deliver a note
    /// to a busy support team inverts the priority this design exists to fix.
    pub(super) fn post(&self, from: &str, body: impl Into<String>) -> bool {
        self.sender
            .try_send(TeamMessage {
                from: from.to_string(),
                body: body.into(),
            })
            .is_ok()
    }

    /// Asks the team to finish its current cycle and stop.
    pub(super) fn cancel(&self) {
        self.cancelled.store(true, Ordering::Relaxed);
    }

    /// Returns how many cycles the team has completed.
    pub(super) fn cycles(&self) -> u64 {
        self.cycles.load(Ordering::Relaxed)
    }
}

/// Why a team stopped, for the closing report.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum TeamExit {
    /// The owner asked it to stop, normally because the solve finished.
    Cancelled,
    /// It used its cycle allowance.
    CyclesSpent,
    /// It ran out of wall clock.
    TimeSpent,
    /// Its own cycle said there was nothing further worth doing.
    Done,
}

impl std::fmt::Display for TeamExit {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter.write_str(match self {
            Self::Cancelled => "cancelled",
            Self::CyclesSpent => "cycle budget spent",
            Self::TimeSpent => "time budget spent",
            Self::Done => "nothing further to do",
        })
    }
}

/// What one cycle of a team decided about its own future.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Cycle {
    /// Work happened; come back promptly.
    Worked,
    /// Nothing to do right now; back off before looking again.
    Idle,
    /// This team has finished its goal and should stop.
    Finished,
}

/// Runs `cycle` as a team until its budget, its own judgement, or its owner
/// stops it.
///
/// The cycle receives every message waiting for it, so a team that was busy
/// sees the whole backlog at once rather than one note per cycle.
pub(super) fn spawn<F, Fut>(
    name: impl Into<String>,
    budget: TeamBudget,
    tracer: Option<Arc<RunTracer>>,
    mut cycle: F,
) -> TeamHandle
where
    F: FnMut(Vec<TeamMessage>) -> Fut + Send + 'static,
    Fut: std::future::Future<Output = Cycle> + Send,
{
    let name = name.into();
    let (sender, mut receiver) = mpsc::channel(INBOX_DEPTH);
    let cancelled = Arc::new(std::sync::atomic::AtomicBool::new(false));
    let cycles = Arc::new(AtomicU64::new(0));
    let handle = TeamHandle {
        name: name.clone(),
        sender,
        cancelled: cancelled.clone(),
        cycles: cycles.clone(),
    };

    tokio::spawn(async move {
        let started = Instant::now();
        let exit = loop {
            if cancelled.load(Ordering::Relaxed) {
                break TeamExit::Cancelled;
            }
            if started.elapsed() >= budget.wall_clock {
                break TeamExit::TimeSpent;
            }
            if cycles.load(Ordering::Relaxed) >= budget.max_cycles {
                break TeamExit::CyclesSpent;
            }
            // Drain rather than take one: a team that spent ten minutes on a
            // cycle should see everything that arrived while it worked, not
            // trickle through the backlog a cycle at a time.
            let mut inbox = Vec::new();
            while let Ok(message) = receiver.try_recv() {
                inbox.push(message);
            }
            let idle = inbox.is_empty();
            // Counted before the cycle runs, not after. Counting after means a
            // team that finishes or is cancelled during its first cycle
            // reports having run none, which reads as a team that never
            // started rather than one that did its job and stopped.
            cycles.fetch_add(1, Ordering::Relaxed);
            match cycle(inbox).await {
                Cycle::Finished => break TeamExit::Done,
                Cycle::Worked => {}
                Cycle::Idle => {
                    // Only sleep when there was genuinely nothing waiting.
                    // Backing off with a full inbox would delay the message
                    // that arrived precisely to be acted on.
                    if idle {
                        tokio::time::sleep(IDLE_BACKOFF).await;
                    }
                }
            }
        };
        if let Some(tracer) = tracer {
            tracer.note(&format!(
                "team {name}: stopped after {} cycle(s), {exit}",
                cycles.load(Ordering::Relaxed)
            ));
        }
    });

    handle
}

#[cfg(test)]
mod test;
