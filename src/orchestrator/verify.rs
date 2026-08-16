//! Which statement the kernel is handed next, and what to ask for when the
//! last attempt on it failed.
//!
//! [`super::lean`] made a kernel check something the runtime *reads* rather
//! than something a role reports. It left the harder half open: `lean_check` is
//! granted to `lean_prover`, and `lean_prover` is delegated to when some other
//! role decides to ask. So what gets formalised is whatever a model found
//! interesting, and across three live calibration runs the answer was nothing
//! at all. Every proof engine in this image has the same shape — four ways to
//! prove something, none of them scheduled — and `refute.rs` records what
//! closing that gap for one of them was worth.
//!
//! This file closes it for the kernel, and the two decisions it makes are the
//! whole of it.
//!
//! # What to check
//!
//! Not everything. Mathlib elaboration is the most expensive thing this image
//! runs, the container has a fixed memory ceiling, and a run buys a handful of
//! checks. [`super::blueprint::Blueprint::targets`] ranks the graph by
//! Scholze's criterion — how much rests on a node, with what the run is already
//! building on ahead of what it has yet to prove — and this file takes the
//! first entry that is still worth attempting.
//!
//! That ranking is the answer to the resource question rather than a
//! concession to it. A fleet of provers is one way to cover a blueprint;
//! choosing the three nodes whose failure would cost the most is another, and
//! it is the one that fits in eight gigabytes. What it gives up is coverage of
//! the tail, and the queue is rendered into `research/BLUEPRINT.md` so the tail
//! is visible rather than silently dropped.
//!
//! # What to ask for when it fails
//!
//! The first attempt on a node asks for a proof. A second asks for something
//! different: split the statement into sub-lemmas, state each one, and leave
//! `sorry` in the ones that are not proved yet. That is Seed-Prover's recursive
//! sketch — a lemma too hard to prove is decomposed and the pieces are proved
//! separately — expressed in the ledgers this runtime already has. The
//! sub-lemmas are written as gaps under `research/backward/`, so they become
//! blueprint nodes, and a leaf whose dependencies are settled comes back
//! through this same ranking as `ready` on a later pass. The recursion is the
//! loop, not a call stack.
//!
//! There is no third stage. A node that survived a proof attempt and a
//! decomposition is one this run does not know how to break down, and the
//! honest thing is to leave it recorded and spend the next check on a different
//! node — which is exactly what skipping it does, since the ranking will offer
//! the next one down. `MAX_ATTEMPTS` is what makes that a rule rather than a
//! hope: without it a node the prover cannot close is the highest-ranked target
//! forever, and the arm re-attempts it every pass for the rest of the run.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};

use serde_json::json;

use super::blueprint::Target;
use super::lean::{self, Verdict};

/// Where a formalisation's Lean source goes.
///
/// A directory of its own under `code/`, so the sources sit beside the
/// programs rather than among them: both are things this run wrote and had
/// checked, and a reader looking for the proof of a lemma should not have to
/// tell a `.lean` file from an enumeration script by name.
pub(super) const SOURCE_DIR: &str = "code/lean";

/// Where the attempt record for one node is filed.
///
/// Beside the kernel verdicts and the refutation verdicts, and committed for
/// the same reason: it is what a reader opens to find out why a lemma the
/// blueprint ranked first was never checked. The Lean verdict says what
/// happened to a *file*; this says what happened to a *statement*, which is a
/// different thing once a decomposition has replaced one file with four.
pub(super) const LEDGER_DIR: &str = "code/out/verify";

/// How many times one node is handed to the kernel.
///
/// Two, because there are two things to ask and no third. See the module
/// header: a proof attempt, then a decomposition, then the budget is better
/// spent on the next node down the ranking.
pub(super) const MAX_ATTEMPTS: usize = 2;

/// What the prover is being asked for this time.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Stage {
    /// State it in Lean and prove it.
    Prove,
    /// Break it into sub-lemmas, and leave the ones not proved as gaps.
    Decompose,
}

impl Stage {
    /// The stage after `attempts` have already been made on a node.
    ///
    /// The ceiling is tested before the match rather than expressed as its last
    /// arm, so lowering [`MAX_ATTEMPTS`] to one narrows the ladder instead of
    /// leaving a stage the bound no longer reaches.
    fn after(attempts: usize) -> Option<Self> {
        if attempts >= MAX_ATTEMPTS {
            return None;
        }
        match attempts {
            0 => Some(Self::Prove),
            _ => Some(Self::Decompose),
        }
    }

    /// What the stage is called on disk.
    fn label(self) -> &'static str {
        match self {
            Self::Prove => "prove",
            Self::Decompose => "decompose",
        }
    }
}

/// One node, the file it is proved in, and what to ask for.
#[derive(Clone, Debug)]
pub(super) struct Assignment {
    /// The node the ranking chose.
    pub(super) target: Target,
    /// What to ask for, given what has already been tried.
    pub(super) stage: Stage,
    /// The workspace-relative Lean source this node's proof lives in.
    pub(super) source: String,
    /// What the kernel said last time, when there was a last time.
    pub(super) previous: Option<Verdict>,
}

/// The Lean source one node's proof is written in.
///
/// Derived from the id rather than chosen by the prover, and that is what makes
/// the loop close: the arm has to find the verdict again next pass, and a file
/// the model named is a file the model has to name identically a pass later.
/// Every character outside the Lean-safe set folds to `_`, so a gap key like
/// `main-bound/step-2` and a claim id are both addressable.
pub(super) fn source_for(id: &str) -> String {
    let name: String = id
        .chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() {
                character
            } else {
                '_'
            }
        })
        .collect();
    format!("{SOURCE_DIR}/{name}.lean")
}

/// The attempt record's path for one node.
fn record_path(workspace: &Path, id: &str) -> PathBuf {
    let name: String = id.replace(['/', '\\'], "_");
    workspace.join(LEDGER_DIR).join(format!("{name}.json"))
}

/// How many times this node has been handed to the kernel.
///
/// A missing or unreadable record reads as zero. That is the permissive
/// direction and it is the right one here: the failure it allows is one extra
/// proof attempt, and the failure the strict direction would allow is a node
/// the run never checks because a JSON file was truncated.
pub(super) fn attempts(workspace: &Path, id: &str) -> usize {
    let Ok(text) = std::fs::read_to_string(record_path(workspace, id)) else {
        return 0;
    };
    let counted = serde_json::from_str::<serde_json::Value>(&text)
        .ok()
        .and_then(|value| value.get("attempts").and_then(serde_json::Value::as_u64))
        .unwrap_or_default();
    // A count too large for this target's `usize` is past the bound whatever
    // the bound is, so saturating is the same answer the arithmetic would give
    // and the truncating cast is not.
    usize::try_from(counted).unwrap_or(usize::MAX)
}

/// Records that this node is being handed to the kernel, and what for.
///
/// Written *before* the prover is delegated to, never after. An attempt that
/// ends in the run cap — the ordinary way a turn ends here — would otherwise
/// leave no record, and the same node would rank first on the next pass and be
/// attempted again until the run ended. Counting the attempt when it starts
/// costs a re-attempt that a crash made pointless; counting it when it finishes
/// costs the bound.
///
/// # Errors
///
/// Returns an error when the directory or the record cannot be written. The
/// caller must not delegate on an error: an uncounted attempt is an unbounded
/// one.
pub(super) async fn note_attempt(workspace: &Path, id: &str, stage: Stage) -> std::io::Result<()> {
    let directory = workspace.join(LEDGER_DIR);
    tokio::fs::create_dir_all(&directory).await?;
    let body = serde_json::to_string_pretty(&json!({
        "node": id,
        "attempts": attempts(workspace, id) + 1,
        "stage": stage.label(),
        "source": source_for(id),
    }))
    .map_err(std::io::Error::other)?;
    tokio::fs::write(record_path(workspace, id), body + "\n").await
}

/// The next node to hand to the kernel, or nothing when there is none.
///
/// Walks the ranking and takes the first node that is still worth a check:
/// not already verified, and not past [`MAX_ATTEMPTS`]. Returning `None` is an
/// ordinary outcome rather than a failure — a run with no skeleton on disk has
/// no graph, and an arm that delegated anyway would spend a child run asking a
/// prover to formalise a problem statement nobody has decomposed.
pub(super) fn next(workspace: &Path) -> Option<Assignment> {
    for target in super::blueprint::collect(workspace).targets() {
        let source = source_for(&target.id);
        let previous = lean::verdict(workspace, &source);
        if previous.as_ref().is_some_and(Verdict::verified) {
            continue;
        }
        let Some(stage) = Stage::after(attempts(workspace, &target.id)) else {
            continue;
        };
        return Some(Assignment {
            target,
            stage,
            source,
            previous,
        });
    }
    None
}

impl Assignment {
    /// What this assignment asks for, rendered for the prover's prompt.
    ///
    /// The statement, the file, and — when there was a previous attempt — the
    /// kernel's objection to it verbatim. The objection is the part that earns
    /// its length: a prover told only "decompose this" will decompose the
    /// statement it would have written anyway, where one told "`code/lean/x.lean`
    /// rests on `key_estimate`, which nothing proved" knows which line the
    /// decomposition has to attack.
    pub(super) fn briefing(&self) -> String {
        let mut out = format!(
            "Node `{}`, from `{}`.\n\nStatement: {}\n\nWrite the proof in `{}`.\n",
            self.target.id, self.target.home, self.target.statement, self.source
        );
        let _ = writeln!(
            out,
            "\n{} node(s) in the statement graph rest directly on this one, and the run {}.",
            self.target.load,
            if self.target.established {
                "is already building on it — which is why it is first in the queue, since a \
                 mistake here is a mistake nothing above it can catch"
            } else {
                "has not established it yet, so it has to be proved before the kernel can check it"
            }
        );
        if let Some(objection) = self.previous.as_ref().and_then(Verdict::objection) {
            let _ = writeln!(out, "\nThe last attempt on this node did not pass: {objection}.");
        }
        out
    }
}

#[cfg(test)]
#[path = "verify_test.rs"]
mod test;
