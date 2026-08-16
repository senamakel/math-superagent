//! Unit tests for the index render.
#![allow(clippy::expect_used)]

use super::{HEADLINE, Row, render, worth_indexing};
use crate::orchestrator::ledger::budget;

fn rows(count: usize) -> Vec<(String, String, String)> {
    (0..count)
        .map(|index| {
            (
                format!("approach-{index}"),
                "refuted".to_string(),
                format!("reason {index} ").repeat(400),
            )
        })
        .collect()
}

fn index_of(count: usize) -> String {
    let owned = rows(count);
    render(
        "approaches",
        "Approaches",
        "Candidate reformulations.",
        owned.iter().map(|(id, status, headline)| Row {
            id,
            status,
            headline,
        }),
        HEADLINE,
    )
}

/// Every entry keeps its identity, and none keeps its argument.
///
/// This is the whole trade. The id and the status are what discharge *do not
/// re-propose this one*; the five kilobytes behind it are what a role pulls only
/// when it is actually considering that entry.
#[test]
fn an_index_keeps_identities_and_drops_arguments() {
    let index = index_of(10);
    for expected in ["approach-0", "approach-9", "refuted"] {
        assert!(index.contains(expected), "`{expected}` survives: {index}");
    }
    let longest = index
        .lines()
        .filter(|line| line.starts_with("- `"))
        .map(|line| line.chars().count())
        .max()
        .unwrap_or_default();
    assert!(
        longest <= HEADLINE + 64,
        "no line carries the argument: longest is {longest} characters"
    );
}

/// The index says how to get what it left out, naming the ledger.
///
/// An index that says *there is more* without saying how to reach it is worse
/// than the full file: the role reads a shortened list, concludes the run holds
/// nothing more, and re-proposes what was cut. Cheaper and dumber is not the
/// trade being made.
#[test]
fn an_index_says_how_to_reach_what_it_dropped() {
    let index = index_of(10);
    assert!(index.contains("read_ledger"), "the call is spelled out: {index}");
    assert!(
        index.contains("\"approaches\""),
        "with the slug filled in, not left as a placeholder: {index}"
    );
    // One line rather than the paragraph it was: the ledger brief above it in
    // every prompt says the rest, and the searcher — the one role that reads an
    // index without the brief — needs the call, which is still here.
    assert!(index.contains("Index only"));
    assert!(index.contains("the run holds more on each of them"));
}

/// Past the row bound the index still says what it did not show.
#[test]
fn an_index_is_bounded_and_reports_the_remainder() {
    let index = index_of(budget::MAX_LISTED + 17);
    assert!(index.contains("17 more"), "{index}");
    assert!(
        index.chars().count() < 12_000,
        "an index of any size stays small: {} characters",
        index.chars().count()
    );
}

/// A ledger too small to index is left alone.
///
/// `research/ENTAILMENT.md` is 266 tokens and an index of it, with the header
/// explaining how to read the rest, comes to more. A uniform rule would have
/// made that file worse.
#[test]
fn a_small_ledger_is_not_worth_indexing() {
    assert!(!worth_indexing("a short ledger"));
    assert!(!worth_indexing(&"x".repeat(600 * 4)));
    assert!(worth_indexing(&"x".repeat(600 * 4 + 8)));
}

/// An empty ledger says so rather than rendering a bare header.
#[test]
fn an_empty_index_says_it_is_empty() {
    let index = index_of(0);
    assert!(index.contains("Nothing recorded yet"));
    assert!(
        !index.contains("read_ledger"),
        "and does not send anybody to pull nothing: {index}"
    );
}

/// A caller whose headline is the payload may keep more of it.
///
/// `CLAIMS` is the case: a claim's statement is not elaboration around the
/// identity, it *is* what the reader needs, so that ledger indexes at a wider
/// headline than the approach ledger does.
#[test]
fn the_headline_width_is_the_callers_choice() {
    let owned = rows(3);
    let build = |width| {
        render(
            "claims",
            "Claims",
            "What the library establishes.",
            owned.iter().map(|(id, status, headline)| Row {
                id,
                status,
                headline,
            }),
            width,
        )
    };
    assert!(build(240).chars().count() > build(110).chars().count());
}

/// A headline arriving with a table cell's punctuation on the front does not
/// spend the line's scarcest characters on a pipe.
#[test]
fn markup_is_stripped_off_a_headline() {
    let owned = [(
        "an-approach".to_string(),
        "refuted".to_string(),
        "| The exact telescoping identity is correct, but the approach hunts a functional".to_string(),
    )];
    let index = render(
        "approaches",
        "Approaches",
        "…",
        owned.iter().map(|(id, status, headline)| Row {
            id,
            status,
            headline,
        }),
        HEADLINE,
    );
    assert!(
        index.contains("— The exact telescoping"),
        "the cell punctuation is gone: {index}"
    );
    assert!(!index.contains("— |"), "{index}");
}

/// A headline that is only the entry's own name is dropped.
///
/// Several of these ledgers fall back to the slug when a field is empty, and
/// rendering that gives `` `ducci-potential` (proposed) — ducci-potential`` —
/// which reads as though something was recorded and says less than the bare id.
#[test]
fn a_headline_that_repeats_the_id_is_dropped() {
    let owned = [(
        "ducci-potential-max-decrease".to_string(),
        "proposed".to_string(),
        "ducci-potential-max-decrease".to_string(),
    )];
    let index = render(
        "approaches",
        "Approaches",
        "…",
        owned.iter().map(|(id, status, headline)| Row {
            id,
            status,
            headline,
        }),
        HEADLINE,
    );
    assert!(index.contains("- `ducci-potential-max-decrease` (proposed)\n"), "{index}");
    assert!(
        !index.contains("— ducci"),
        "the id is not repeated as its own summary: {index}"
    );
}

/// A status every row shares is stated once, not on every line.
///
/// The claims index on a live workspace read `(asserted, yes)` on all seventy
/// of its lines: six hundred characters, in twenty prompts, on every model call,
/// spent on a value that never varied. A constant is a header, not a column.
#[test]
fn a_status_every_row_shares_is_hoisted_out_of_the_rows() {
    let index = index_of(10);
    assert!(
        index.contains("Every row below is `refuted`."),
        "the constant is stated once: {index}"
    );
    assert!(
        !index.contains("` (refuted)"),
        "and not on any row: {index}"
    );
}

/// When the status varies it stays on the row, because then it is the payload.
#[test]
fn a_status_that_varies_stays_on_the_row() {
    let owned = [
        ("open-one".to_string(), "open".to_string(), "still to do".to_string()),
        ("done-one".to_string(), "done".to_string(), "carried out".to_string()),
    ];
    let index = render(
        "tasks",
        "Tasks",
        "…",
        owned.iter().map(|(id, status, headline)| Row {
            id,
            status,
            headline,
        }),
        HEADLINE,
    );
    assert!(index.contains("- `open-one` (open)"), "{index}");
    assert!(index.contains("- `done-one` (done)"), "{index}");
    assert!(!index.contains("Every row below"), "{index}");
}

/// One row does not establish that a value is constant.
#[test]
fn a_single_row_keeps_its_status_where_it_is() {
    let owned = [(
        "only-one".to_string(),
        "proposed".to_string(),
        "the only entry".to_string(),
    )];
    let index = render(
        "approaches",
        "Approaches",
        "…",
        owned.iter().map(|(id, status, headline)| Row {
            id,
            status,
            headline,
        }),
        HEADLINE,
    );
    assert!(index.contains("- `only-one` (proposed)"), "{index}");
    assert!(!index.contains("Every row below"), "{index}");
}
