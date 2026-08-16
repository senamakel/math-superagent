#![allow(clippy::expect_used)]

use std::fmt::Write as _;

use serde_json::json;

use super::select;

/// A rendered ledger of the shape the hand-written modules produce: a preamble,
/// section headings, list entries, and indented prose under each.
fn rendered() -> String {
    "# Claims\n\nWhat the library establishes.\n\n\
     ## Established\n\n\
     - `claim-alpha` — every even number above two is a sum of two primes\n  \
     - hypotheses: none stated\n  \
     - status: asserted\n\
     - `claim-beta` — the sieve is exact below ten million\n  \
     - hypotheses: exact integer arithmetic\n  \
     - status: verified\n\n\
     ## Contradicted\n\n\
     - `claim-gamma` — the bound is tight\n  \
     - killed-by: a counterexample at n=12\n"
        .to_string()
}

#[test]
fn an_unfiltered_read_returns_the_file() {
    let out = select("derived/CLAIMS.md", &rendered(), &json!({}));
    assert_eq!(out, rendered());
}

#[test]
fn an_id_selects_one_entry_and_its_prose() {
    let out = select("derived/CLAIMS.md", &rendered(), &json!({ "id": "claim-beta" }));
    assert!(out.contains("claim-beta"), "{out}");
    assert!(
        out.contains("exact integer arithmetic"),
        "the entry's own prose must come with it: {out}"
    );
    assert!(
        !out.contains("claim-alpha") && !out.contains("claim-gamma"),
        "an id must not return the whole ledger: {out}"
    );
    assert!(out.contains("1 of 3"), "it must say what it selected: {out}");
}

#[test]
fn a_query_matches_the_prose_as_well_as_the_title() {
    let out = select(
        "derived/CLAIMS.md",
        &rendered(),
        &json!({ "query": "counterexample" }),
    );
    assert!(out.contains("claim-gamma"), "{out}");
    assert!(!out.contains("claim-alpha"), "{out}");
}

#[test]
fn a_status_matches_the_section_it_is_under() {
    // A rendered file carries status in the heading as often as in the row, and
    // a filter that only looked at the row would silently return nothing.
    let out = select(
        "derived/CLAIMS.md",
        &rendered(),
        &json!({ "status": "contradicted" }),
    );
    assert!(out.contains("claim-gamma"), "{out}");
    assert!(!out.contains("claim-beta"), "{out}");
}

#[test]
fn the_matching_entries_keep_the_heading_they_were_under() {
    let out = select("derived/CLAIMS.md", &rendered(), &json!({ "query": "claim" }));
    assert!(out.contains("## Established"), "{out}");
    assert!(out.contains("## Contradicted"), "{out}");
}

#[test]
fn a_limit_bounds_the_matches_and_says_what_it_dropped() {
    let out = select(
        "derived/CLAIMS.md",
        &rendered(),
        &json!({ "query": "claim", "limit": 1 }),
    );
    assert!(out.contains("further match"), "{out}");
    assert!(out.contains("3 of 3"), "the true total must survive: {out}");
}

#[test]
fn nothing_matching_says_so_and_says_how_many_there_are() {
    let out = select(
        "derived/CLAIMS.md",
        &rendered(),
        &json!({ "id": "claim-omega" }),
    );
    assert!(out.contains("Nothing"), "{out}");
    assert!(
        out.contains("3 entries"),
        "an empty result must say what the ledger does hold: {out}"
    );
}

#[test]
fn an_oversized_ledger_is_bounded_and_names_the_way_to_narrow_it() {
    // The measured failure: 86 KB returned to answer a question about one row,
    // with no bound and no suggestion of a better call.
    let mut huge = String::from("# Approaches\n\n## What closed, and why\n\n");
    for index in 0..4_000 {
        let _ = write!(
            huge,
            "- `approach-{index}` — an idea\n  - killed-by: {}\n",
            "the reason it died ".repeat(40)
        );
    }
    let out = select("derived/APPROACHES.md", &huge, &json!({}));
    assert!(out.len() < huge.len(), "an oversized ledger must be cut");
    assert!(
        out.contains("truncated from the middle"),
        "the cut must be visible: {out:.300}"
    );
    assert!(
        out.contains("`id`, `query` or `status`"),
        "it must name the cheaper call: {}",
        &out[out.len().saturating_sub(400)..]
    );
}

#[test]
fn a_filtered_read_of_an_oversized_ledger_stays_bounded() {
    let mut huge = String::from("# Approaches\n\n## Open\n\n");
    for index in 0..4_000 {
        let _ = write!(
            huge,
            "- `approach-{index}` — sieve\n  - detail: {}\n",
            "words ".repeat(60)
        );
    }
    let out = select("derived/APPROACHES.md", &huge, &json!({ "query": "sieve" }));
    assert!(
        out.len() < huge.len(),
        "a filter that matches everything must still be bounded"
    );
}

#[test]
fn a_table_row_is_an_entry_too() {
    // `frontier` and `blueprint` render tables rather than lists.
    let table = "# Frontier\n\n## Rows\n\n| id | what |\n| --- | --- |\n| f-1 | the first |\n| f-2 | the second |\n";
    let out = select("derived/FRONTIER.md", table, &json!({ "id": "f-2" }));
    assert!(out.contains("the second"), "{out}");
    assert!(!out.contains("the first"), "{out}");
    assert!(
        !out.contains("---"),
        "the separator row must not count as an entry: {out}"
    );
}
