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

use std::hash::{Hash as _, Hasher as _};
use std::path::{Path, PathBuf};
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

/// Files a workspace fingerprint will look at.
///
/// A bound, not a budget: the fingerprint runs between every pair of cycles,
/// and walking an unbounded tree to decide whether to sleep would cost more
/// than the sleep saves.
const FINGERPRINT_FILES: usize = 600;

/// Directory depth the fingerprint walks.
const FINGERPRINT_DEPTH: usize = 4;

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
    /// Shortest time between the starts of two cycles.
    ///
    /// The floor exists because the workspace fingerprint below cannot carry
    /// the whole job. It detects a cycle that changed nothing, but only when
    /// nothing else changed either — and teams run concurrently with the
    /// solver, so somebody has usually written a file while a cycle was
    /// running. A custodial team measured at 1.35 cycles a minute produced 20
    /// reads, 12 listings, four index refreshes and no descriptions, and the
    /// fingerprint believed every one of them because the solver was busy
    /// underneath.
    ///
    /// Rate is the honest bound for work that is never finished: filing does
    /// not need doing every forty-five seconds, and a floor costs nothing when
    /// there is genuinely something to file.
    pub(super) min_interval: Duration,
}

impl TeamBudget {
    /// An acquisitive team's allowance: it terminates, so it may go flat out.
    pub(super) const fn acquiring() -> Self {
        Self {
            max_cycles: 40,
            wall_clock: Duration::from_mins(90),
            min_interval: Duration::ZERO,
        }
    }

    /// A custodial team's allowance, paced because its work never ends.
    pub(super) const fn custodial() -> Self {
        Self {
            max_cycles: 40,
            wall_clock: Duration::from_mins(90),
            min_interval: Duration::from_mins(3),
        }
    }

    /// An allowance for a team that mostly waits.
    ///
    /// The director exists to notice that a person has said something, so its
    /// cost profile is the opposite of every other team's: a cycle with an
    /// empty queue costs one file read and returns before any model call, and
    /// what bounds its spending is how often a human types rather than how
    /// often it wakes. The custodial allowance is wrong for it twice over — a
    /// three-minute floor makes a directive wait three minutes to be noticed,
    /// and forty cycles at the twenty-second idle backoff would retire the team
    /// after thirteen minutes of an eight-hour run, with nothing to show that
    /// direction was no longer being read.
    ///
    /// So the cycle count is raised until it is the wall clock that stops the
    /// team, and the rate floor is dropped. Neither is a licence to spend: the
    /// queue check in front of the model call is the real bound, and it is
    /// enforced before the agent runs rather than asked for in its brief.
    pub(super) const fn attentive() -> Self {
        Self {
            max_cycles: 4000,
            wall_clock: Duration::from_hours(24),
            min_interval: Duration::ZERO,
        }
    }

    /// A custodial allowance whose rate the operator sets.
    ///
    /// The curator's cadence is the one pacing decision with a visible effect
    /// on the solve — it decides how stale the brief every role reads may be —
    /// so it is configuration rather than a constant. Everything else about
    /// the allowance is the custodial one: the file it maintains keeps
    /// changing underneath it, so it never finishes.
    pub(super) fn paced(min_interval: Duration) -> Self {
        Self {
            min_interval,
            ..Self::custodial()
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

/// Summarises the workspace as it stands, for detecting a cycle that changed
/// nothing.
///
/// Path, length and modification time of every file, hashed. It does not read
/// contents: a cycle that rewrote a file with identical bytes did no useful
/// work either, and reading the whole workspace twice per cycle to prove that
/// would cost more than the finding is worth.
///
/// `trace.jsonl` is excluded deliberately. It grows on every model call in the
/// run, so including it would make every fingerprint differ and the check
/// would never fire — it would report change from the solver's activity rather
/// than the team's.
pub(super) fn fingerprint(workspace: &Path) -> u64 {
    fingerprint_excluding(workspace, &[])
}

/// The same, ignoring files with any of the given names.
///
/// A team that writes into the folders it watches would otherwise wake itself
/// forever on its own output — the reason the pattern team's `SCRATCHPAD.md` is
/// kept out of its fingerprint. Filing has the same problem one folder
/// wider: it rewrites `INDEX.md`, so an unfiltered fingerprint of the tree it
/// files changes every time it files, and every cycle looks like fresh work.
pub(super) fn fingerprint_excluding(workspace: &Path, excluded: &[&str]) -> u64 {
    let mut hasher = std::collections::hash_map::DefaultHasher::new();
    let mut seen = 0usize;
    let mut stack = vec![(workspace.to_path_buf(), 0usize)];
    let mut entries: Vec<(PathBuf, u64, Option<std::time::SystemTime>)> = Vec::new();
    while let Some((folder, depth)) = stack.pop() {
        if depth > FINGERPRINT_DEPTH || seen >= FINGERPRINT_FILES {
            continue;
        }
        let Ok(listing) = std::fs::read_dir(&folder) else {
            continue;
        };
        for entry in listing.flatten() {
            let name = entry.file_name().to_string_lossy().to_string();
            if name.starts_with('.')
                || name == "trace.jsonl"
                || name == "__pycache__"
                || excluded.contains(&name.as_str())
            {
                continue;
            }
            let path = entry.path();
            if path.is_dir() {
                stack.push((path, depth + 1));
                continue;
            }
            let Ok(meta) = entry.metadata() else { continue };
            entries.push((path, meta.len(), meta.modified().ok()));
            seen += 1;
            if seen >= FINGERPRINT_FILES {
                break;
            }
        }
    }
    // Directory order is not stable across reads, so sort before hashing or
    // the fingerprint changes when nothing has.
    entries.sort();
    for (path, len, modified) in entries {
        path.hash(&mut hasher);
        len.hash(&mut hasher);
        if let Some(modified) = modified
            && let Ok(since) = modified.duration_since(std::time::UNIX_EPOCH)
        {
            since.as_millis().hash(&mut hasher);
        }
    }
    hasher.finish()
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
    workspace: Option<PathBuf>,
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
            let cycle_started = Instant::now();
            // Counted before the cycle runs, not after. Counting after means a
            // team that finishes or is cancelled during its first cycle
            // reports having run none, which reads as a team that never
            // started rather than one that did its job and stopped.
            cycles.fetch_add(1, Ordering::Relaxed);
            let before = workspace.as_deref().map(fingerprint);
            let mut outcome = cycle(inbox).await;
            // A cycle that reports work but left the workspace exactly as it
            // found it did not work. A live background team ran seven cycles
            // in six minutes — 26 reads, 16 listings, seven index refreshes,
            // and not one description — reporting progress each time, so it
            // never backed off and was on course to spend its whole allowance
            // re-reading a workspace it was not changing. What a team claims
            // about its own productivity cannot be the thing that decides
            // whether to believe it.
            if outcome == Cycle::Worked
                && let Some(before) = before
                && workspace.as_deref().map(fingerprint) == Some(before)
            {
                outcome = Cycle::Idle;
            }
            match outcome {
                Cycle::Finished => break TeamExit::Done,
                // Both outcomes wait, and for the same reason: a team with
                // nothing waiting for it should not come straight back.
                //
                // Pacing the worked branch alone was measured and was not
                // enough. A custodial team that reports "nothing to tidy"
                // takes the *idle* branch, so the one case most in need of a
                // floor was the one case escaping it: two live teams ran a
                // cycle every 66 and 108 seconds against a three-minute floor,
                // while a third — which happened to be reporting work — was
                // paced correctly.
                //
                // A message waiting skips the wait entirely. The point is to
                // stop idle churn, not to delay a request that has already
                // arrived.
                // Both outcomes can wait, but not for the same reason, and
                // conflating them is a regression: a team that worked has more
                // to do, so only the rate floor applies to it. A team that
                // found nothing has nothing to come back to yet, so it waits
                // at least the idle interval.
                //
                // Pacing the worked branch alone was measured and was not
                // enough. A custodial team reporting "nothing to tidy" takes
                // the *idle* branch, so the one case most in need of a floor
                // was the one escaping it: two live teams ran a cycle every 66
                // and 108 seconds against a three-minute floor, while a third
                // — which happened to be reporting work — was paced correctly.
                //
                // A message waiting skips the wait entirely either way. The
                // point is to stop idle churn, not to delay a request that has
                // already arrived.
                outcome => {
                    if idle {
                        let floor = if outcome == Cycle::Idle {
                            IDLE_BACKOFF.max(budget.min_interval)
                        } else {
                            budget.min_interval
                        };
                        if let Some(remaining) = floor.checked_sub(cycle_started.elapsed()) {
                            tokio::time::sleep(remaining).await;
                        }
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
