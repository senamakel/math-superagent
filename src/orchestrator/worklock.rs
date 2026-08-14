//! The two locks that order concurrent writers to one workspace.
//!
//! Nothing in this runtime locked the workspace, and for a single solution loop
//! that was very nearly true enough: one loop writes from one place at a time,
//! and the standing teams were few and slow. It was never *quite* true — fifty
//! sub-agents may run at once ([`super::async_subagents`]) and every one of them
//! carries the checkpoint middleware — and the evidence that it was not is on
//! disk. A live Erdős–Gyárfás workspace holds a stranded zero-byte
//! `.workspace-history/index.lock`, which is what two concurrent `git add` on
//! one index leaves behind. The commit that lost is not reported anywhere,
//! because [`super::checkpoint`] deliberately swallows its own failures rather
//! than failing the tool whose work succeeded.
//!
//! Running several schools on one workspace turns that from a rare loss into
//! the normal case, so the locks come first.
//!
//! # Two locks, and the rule that keeps them from deadlocking
//!
//! [`tokio::sync::Mutex`] is not reentrant, and the write path is a cascade: a
//! note write re-derives six ledgers, each of which reads a directory and
//! writes a file through the same store. A lock taken at the leaf would be
//! taken again by everything above it and the run would stop.
//!
//! So the rule is: **a lock is taken at a tool-call boundary and never below
//! one.** [`writes`] is held across a whole write-and-re-derive, so another
//! writer cannot interleave with the cascade; nothing the cascade calls may
//! take it again. Per-file atomicity is not this lock's job and does not
//! depend on it — [`super::documents`] writes through a temporary file and
//! renames it, so a reader sees the old bytes or the new ones and never half of
//! each.
//!
//! [`commits`] is separate rather than the same lock reused, because the git
//! checkpoint runs as middleware *after* a tool returns. The two critical
//! sections never nest today, and keeping them distinct means a future one that
//! did would block rather than deadlock.

use std::sync::OnceLock;

use tokio::sync::{Mutex, MutexGuard};

/// Orders writes to the workspace and the ledger re-derivations that follow.
static WRITES: OnceLock<Mutex<()>> = OnceLock::new();

/// Orders commits into the workspace's own git history.
static COMMITS: OnceLock<Mutex<()>> = OnceLock::new();

/// Holds the write lock until the returned guard is dropped.
///
/// Take it at a tool-call boundary, around the write *and* everything derived
/// from it. Never take it from anything reachable below one; see the module
/// documentation for why that deadlocks rather than merely contending.
pub(super) async fn writes() -> MutexGuard<'static, ()> {
    WRITES.get_or_init(|| Mutex::new(())).lock().await
}

/// Holds the commit lock until the returned guard is dropped.
///
/// One git index cannot serve two `git add --all` at once. The loser leaves an
/// `index.lock` behind and its commit is lost silently.
pub(super) async fn commits() -> MutexGuard<'static, ()> {
    COMMITS.get_or_init(|| Mutex::new(())).lock().await
}

#[cfg(test)]
#[path = "worklock_test.rs"]
mod test;
