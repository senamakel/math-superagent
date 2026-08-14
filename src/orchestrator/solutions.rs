//! The solution loop: a graph that attempts, reflects, and diversifies.
//!
//! A single agent asked to "solve this" retries the approach it already has.
//! When that approach is wrong, more turns of it produce more of the same
//! failure, and the run ends having learned nothing it can act on. This graph
//! makes the control flow explicit instead of leaving it to the model's
//! judgement:
//!
//! ```text
//!   research ──> seed goals ──> solve ─── done ──> report
//!                                 │
//!                                 └─ body ─> attempt ──┬─> judge ──────────┐
//!                                    ▲                 ├─> reflect ────────┤
//!                                    │                 ├─> patterns ───────┤
//!                                    │                 ├─> invention ──────┼─> merge
//!                                    │                 ├─> library (opens) ┤     │
//!                                    │                 └─> goals ─> cadence┘     │
//!                                    │                                        route
//!                                    │                                           │
//!                                    └───── pass <── escalate <── diversify ─────┤
//!                                    └───── pass <───── solved/retry/... ────────┘
//! ```
//!
//! Three stages. **Research** runs once: establish what the workspace already
//! has, then go looking for what it does not. **Attempt** is one attempt.
//! **Evaluation** asks five questions about that attempt *at the same time* —
//! how it was conducted, what it established, what structure is in its numbers,
//! what a different line of attack would be, and what would suffice to prove the
//! goal — and merges their answers before anything routes.
//!
//! The fan-out is the point. Those five used to run in a line, and three of them
//! were not nodes at all: they were `tokio::spawn`s hidden inside the
//! reflection's body, invisible to the graph, unbounded by its policy, and
//! impossible to checkpoint between. A pass now costs the slowest arm rather
//! than the sum of all of them.
//!
//! Every path back to the head goes through one node, and every arm reads the
//! attempt rather than the head's accumulator — the head folds at the top of a
//! pass, so during a pass the accumulator is what the *last* one ended with.
//!
//! One arm is deliberately not awaited. `library` starts a literature sweep and
//! returns immediately, because a paper is no less relevant for being found a
//! cycle later, while a report about *this attempt* arriving next cycle is a
//! report about the wrong attempt. Its findings reach the next attempt through
//! a mailbox. The escalation on the `diversify` port is the same sweep, awaited:
//! a run that has stopped making progress should read what it gathered before
//! attempting again.
//!
//! The two judgements are separate on purpose. `reflect` asks whether the
//! answer is right and what the run learned, and it alone can end the loop.
//! `judge` asks the narrower question of whether the attempt was *conducted*
//! in a way the next one should inherit, scores it, and may throw the current
//! direction away — bounded by `MAX_RESTARTS`, and never on an unreadable
//! reply. It runs first so a restart costs a judge call rather than a judge
//! call plus a reflection about to be discarded.
//!
//! `reflect` runs after *every* attempt, not only after a failure, because the
//! lesson from a partial success is what stops the next attempt repeating it.

use std::collections::BTreeSet;
use std::ffi::OsString;
use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use super::vector::VectorStore;
use crate::agent::trace::RunTracer;

use super::async_subagents::AsyncSubagentManager;
use super::teams::TeamHandle;

include!("solutions_attempt.rs");
include!("solutions_parallel.rs");
include!("solutions_judging.rs");
include!("solutions_evaluation.rs");
include!("solutions_routing.rs");
include!("solutions_state.rs");

#[cfg(test)]
#[path = "solutions_test.rs"]
mod test;
