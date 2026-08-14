//! Unit tests for the shared brief's budget.
//!
//! Nothing here sets an environment variable. Reading one is safe from a test;
//! writing one is process-global, and these run in parallel with every other
//! test in the crate, so a test that overrode the budget would be changing what
//! its neighbours measure. The assertions are therefore written against
//! [`budget_tokens`] rather than against the literal default, and the default
//! itself is checked as a constant.
#![allow(clippy::expect_used)]

use std::path::PathBuf;

use super::{
    CONTEXT_FILE, DEFAULT_CONTEXT_TOKENS, Standing, briefing, budget_tokens, fit, standing,
};

/// Creates an empty workspace under the temporary directory.
fn workspace(name: &str) -> PathBuf {
    let root =
        std::env::temp_dir().join(format!("math-agent-context-{name}-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the workspace is creatable");
    root
}

#[test]
fn the_brief_starts_with_a_ten_thousand_token_allowance() {
    // The number is the product decision this module exists to carry: a
    // thousand tokens buys a catalogue, which `research/INDEX.md` already is.
    assert_eq!(DEFAULT_CONTEXT_TOKENS, 10_000);
}

#[test]
fn a_missing_brief_measures_as_empty_rather_than_as_an_error() {
    // A fresh workspace has no brief, and the caller is a background team
    // deciding what to say to an agent rather than one that can handle an
    // error.
    let root = workspace("missing");
    assert_eq!(
        standing(&root),
        Standing {
            tokens: 0,
            budget: budget_tokens(),
        }
    );
    assert_eq!(standing(&root).headroom(), budget_tokens());
    assert_eq!(standing(&root).excess(), 0);
}

#[test]
fn a_brief_within_budget_is_passed_through_untouched() {
    assert!(fit("## Established\n\nNothing yet.").is_none());
}

#[test]
fn a_brief_over_budget_is_cut_and_says_so() {
    let oversized = "believed: the pass rule is idempotent. "
        .repeat(usize::try_from(budget_tokens()).expect("the budget fits in a usize"));
    let fitted = fit(&oversized).expect("an oversized brief is cut");
    assert!(fitted.len() < oversized.len());
    // Silence is the failure mode: an agent not told the brief was cut
    // believes it has the whole thing and stops reading the file.
    assert!(fitted.contains(CONTEXT_FILE));
    assert!(fitted.contains("compress it"));
    // The leading portion survives, because the brief is written
    // most-established-first.
    assert!(fitted.starts_with("believed: the pass rule is idempotent."));
}

#[test]
fn the_cut_lands_on_a_character_boundary() {
    // A multi-byte brief must not panic the slice. The budget is large, so the
    // string has to be too.
    let oversized = "π approximates the pass density. "
        .repeat(usize::try_from(budget_tokens()).expect("the budget fits in a usize"));
    let fitted = fit(&oversized).expect("an oversized brief is cut");
    assert!(!fitted.is_empty());
}

#[test]
fn an_over_budget_brief_is_briefed_to_compress_rather_than_to_add() {
    let root = workspace("over");
    let oversized = "the run believes the recurrence closes. "
        .repeat(usize::try_from(budget_tokens()).expect("the budget fits in a usize"));
    std::fs::write(root.join(CONTEXT_FILE), oversized).expect("the brief is writable");
    let brief = briefing(&root);
    assert!(brief.contains("compression, not an addition"));
    assert!(brief.contains("Add nothing"));
}

#[test]
fn a_brief_with_headroom_is_told_what_the_headroom_is_for() {
    let root = workspace("under");
    std::fs::write(root.join(CONTEXT_FILE), "## Established\n\nNothing yet.\n")
        .expect("the brief is writable");
    let brief = briefing(&root);
    assert!(brief.contains("remain"));
    // Headroom is not a target. A curator told only that it has room fills it.
    assert!(brief.contains("rather than filling it"));
}
