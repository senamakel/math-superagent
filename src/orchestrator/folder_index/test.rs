//! Unit tests for the per-folder index.
#![allow(clippy::expect_used)]

use std::collections::BTreeMap;

use super::{INDEX_FILE, index_for, parse, render, split};

fn entries(pairs: &[(&str, &str)]) -> BTreeMap<String, String> {
    pairs
        .iter()
        .map(|(name, purpose)| ((*name).to_string(), (*purpose).to_string()))
        .collect()
}

#[test]
fn a_rendered_index_round_trips_through_the_parser() {
    // Descriptions survive a refresh only if what we write is what we read.
    let original = entries(&[
        ("brute.py", "naive oracle; validates the real method"),
        (
            "solution.py",
            "efficient peel solver; the answer comes from here",
        ),
    ]);

    let parsed = parse(&render("", &original));

    assert_eq!(parsed, original);
}

#[test]
fn a_reformatted_index_does_not_lose_its_descriptions() {
    // An index a human or an agent has rewritten must still yield its rows,
    // because losing them silently is worse than an ugly table.
    let hand_written = "# Notes\n\
        | File | Purpose |\n\
        |------|---------|\n\
        |`brute.py`| naive oracle |\n\
        | solution.py | the real method |\n\
        \nsome prose that is not a row\n";

    let parsed = parse(hand_written);

    assert_eq!(
        parsed.get("brute.py").map(String::as_str),
        Some("naive oracle")
    );
    assert_eq!(
        parsed.get("solution.py").map(String::as_str),
        Some("the real method")
    );
    // The header and separator are not files.
    assert!(!parsed.contains_key("File"));
    assert_eq!(parsed.len(), 2);
}

#[test]
fn an_undescribed_file_is_marked_rather_than_left_blank() {
    let rendered = render("research", &entries(&[("paper.md", "")]));
    assert!(rendered.contains("_(undescribed)_"), "{rendered}");
    assert!(rendered.contains("# Index — research"), "{rendered}");
}

#[test]
fn an_empty_folder_still_renders_a_usable_table() {
    let rendered = render("notes", &BTreeMap::new());
    assert!(rendered.contains("This folder is empty"), "{rendered}");
    // The placeholder must not be a table row: parsed back it would become a
    // file the next refresh carries forward as though it existed.
    assert_eq!(parse(&rendered).len(), 0, "{rendered}");
}

#[test]
fn a_path_resolves_to_the_index_beside_it() {
    assert_eq!(split("research/papers/pell.md").0, "research/papers");
    assert_eq!(split("research/papers/pell.md").1, "pell.md");
    assert_eq!(split("solution.py"), (String::new(), "solution.py".into()));
    assert_eq!(
        split("./solution.py"),
        (String::new(), "solution.py".into())
    );

    assert_eq!(index_for("research"), format!("research/{INDEX_FILE}"));
    assert_eq!(index_for(""), INDEX_FILE);
}
