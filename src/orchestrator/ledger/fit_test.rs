//! The per-ledger prompt budget.
//!
//! This guard should never fire — [`super::budget`] and the per-module section
//! bounds are what keep these files small, and the ceilings in
//! `ceiling_test.rs` are what keep those honest. An untested guard that never
//! fires is indistinguishable from one that does not work, so it is exercised
//! here directly.
#![allow(clippy::expect_used)]

use super::{DEFAULT_LEDGER_TOKENS, fit, is_routed};
use crate::orchestrator::approaches::APPROACHES_PATH;
use crate::orchestrator::shared_context::CHARS_PER_TOKEN;

/// Characters the default budget allows, as a `usize` the fixtures can repeat.
fn budget_chars() -> usize {
    usize::try_from(DEFAULT_LEDGER_TOKENS).unwrap_or(usize::MAX) * CHARS_PER_TOKEN
}

/// A ledger inside its budget is passed through untouched.
///
/// `None` rather than a copy, so the caller keeps its own string in the
/// ordinary case and nothing allocates on the common path.
#[test]
fn a_ledger_within_budget_is_left_alone() {
    assert!(fit(APPROACHES_PATH, "a short ledger").is_none());
}

/// A file that is not a routed ledger is never touched, whatever its size.
///
/// The bound is about what a *derived* file may cost a prompt. A note, a
/// program, or the problem statement is not derived and is not this module's
/// business — cutting one here would be a silent edit to something an agent
/// wrote.
#[test]
fn a_file_that_is_not_a_routed_ledger_is_left_alone() {
    let huge = "x".repeat(budget_chars() * 4);
    assert!(fit("research/notes/some-note.md", &huge).is_none());
    assert!(fit("GOAL.md", &huge).is_none());
    assert!(!is_routed("GOAL.md"));
    assert!(is_routed(APPROACHES_PATH));
}

/// An oversized ledger is cut, and says so in a way that reaches the model.
#[test]
fn an_oversized_ledger_is_cut_and_says_so() {
    let huge = "the reason it died. ".repeat(budget_chars());
    let cut = fit(APPROACHES_PATH, &huge).expect("a ledger four times its budget is cut");

    assert!(
        cut.chars().count() < huge.chars().count(),
        "the cut copy is shorter than the file"
    );
    assert!(
        cut.contains(APPROACHES_PATH),
        "the notice names the file so the model knows what to read: {cut}"
    );
    assert!(
        cut.contains("cut here"),
        "and says plainly that it was cut, so the model does not read the fragment as the whole \
         ledger: {cut}"
    );
    // The kept portion is the head, because every derived ledger puts its table
    // first. A tail-preserving cut would hand the model the fault list and
    // nothing else.
    assert!(cut.starts_with("the reason it died."));
}

/// The cut lands on a character boundary rather than panicking.
///
/// Every one of these files carries mathematics, so multi-byte characters are
/// the norm and not an edge case: `δ`, `≤`, `→` and `ν₂` all appear in the
/// workspace this module was written against. Slicing one in half would panic
/// inside prompt assembly, which happens at container start — so the run would
/// fail before doing any work.
#[test]
fn a_multibyte_ledger_is_cut_on_a_boundary() {
    let huge = "δ_k(q_n) ≤ ν₂ → ".repeat(budget_chars());
    let cut = fit(APPROACHES_PATH, &huge).expect("an oversized ledger is cut");
    assert!(cut.contains('δ'), "the mathematics survives the cut");
}


/// The nine rendered ledgers move into `derived/` once, on a workspace that
/// predates the folder — which is every workspace on disk.
#[test]
fn a_workspace_written_before_the_derived_folder_is_migrated_once() {
    let root = std::env::temp_dir().join("ledger-migrate-once");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research")).expect("created");
    std::fs::write(root.join("research/CLAIMS.md"), "old claims\n").expect("written");
    std::fs::write(root.join("research/APPROACHES.md"), "old approaches\n").expect("written");
    // An ordinary note beside them, which is not derived and must not move.
    std::fs::write(root.join("research/pell.md"), "a note\n").expect("written");

    let moved = super::migrate_derived(&root);
    assert_eq!(moved.len(), 2, "both ledgers move: {moved:?}");
    assert_eq!(
        std::fs::read_to_string(root.join("derived/CLAIMS.md")).expect("moved"),
        "old claims\n"
    );
    assert!(
        !root.join("research/CLAIMS.md").exists(),
        "the old copy must not be left behind to go stale"
    );
    assert!(
        root.join("research/pell.md").is_file(),
        "a note that is not a derived ledger must stay where it is"
    );

    // Idempotent: a second start moves nothing.
    assert!(super::migrate_derived(&root).is_empty());
}

/// A destination that already exists wins, and the source is left alone.
///
/// `docs/workspace.md` forbids overwriting a file carrying a result, and one of
/// these may be mid-write.
#[test]
fn migration_never_overwrites_what_is_already_there() {
    let root = std::env::temp_dir().join("ledger-migrate-clobber");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research")).expect("created");
    std::fs::create_dir_all(root.join("derived")).expect("created");
    std::fs::write(root.join("research/CLAIMS.md"), "the old one\n").expect("written");
    std::fs::write(root.join("derived/CLAIMS.md"), "the current one\n").expect("written");

    assert!(super::migrate_derived(&root).is_empty());
    assert_eq!(
        std::fs::read_to_string(root.join("derived/CLAIMS.md")).expect("kept"),
        "the current one\n",
        "the newer file was clobbered by the older one"
    );
}
