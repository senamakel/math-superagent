//! The solution loop: a graph that attempts, reflects, and diversifies.
//!
//! A single agent asked to "solve this" retries the approach it already has.
//! When that approach is wrong, more turns of it produce more of the same
//! failure, and the run ends having learned nothing it can act on. This graph
//! makes the control flow explicit instead of leaving it to the model's
//! judgement:
//!
//! ```text
//!   attempt ──> judge ──┬─ restart ─────────────────────────> pass ──┐
//!      ▲                └─ reflect ──> goals ──> route ──┬─ solved ──┤
//!      │                                (child)          ├─ retry ───┤
//!      │                                                 └─ stuck ─> diversify ──┐
//!      │                                                              (3 arms) ──┘
//!      └───────────────────────── the loop head, which folds ────────────────────┘
//! ```
//!
//! Every path back to the head goes through one node, and every step reads the
//! step before it rather than the head's accumulator — the head folds at the top
//! of a pass, so during a pass the accumulator is what the *last* one ended
//! with. `goals` is a child workflow that decides, on a cadence, whether to open
//! a decomposition of the goal beside the loop; see `super::workflow_goals`.
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
//! `diversify` is what breaks a loop the reflection alone cannot: it gathers
//! reference material, looks for structure in the results already computed, and
//! asks for a genuinely different approach, in parallel, before trying again.

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
include!("solutions_routing.rs");
include!("solutions_state.rs");

#[cfg(test)]
#[path = "solutions_test.rs"]
mod test;
