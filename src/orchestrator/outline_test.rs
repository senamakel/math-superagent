//! Unit tests for the document outline and the selected read.
#![allow(clippy::expect_used)]

use super::{MAX_SLICE_BYTES, MAX_UNSELECTED_BYTES, region, render, sections, select, too_large};

const PAPER: &str = "\
preamble line
another preamble line
# Title
opening
## Method
the method is this
and this
## Results
a result
### Detail
fine print
";

#[test]
fn a_headed_document_becomes_a_section_per_heading() {
    let found = sections("paper.md", PAPER);

    let titles: Vec<&str> = found.iter().map(|s| s.title.as_str()).collect();
    assert_eq!(
        titles,
        vec![
            "(preamble)",
            "Title",
            "Method",
            "Results",
            "Detail"
        ]
    );
    // Ranges must abut and cover: a hole in the map is a part of the document
    // nothing can address, which is the failure the ceiling would turn fatal.
    for pair in found.windows(2) {
        assert_eq!(pair[0].last_line + 1, pair[1].first_line);
    }
    assert_eq!(found[0].first_line, 1);
    assert_eq!(
        found.last().map(|s| s.last_line),
        Some(PAPER.lines().count())
    );
}

#[test]
fn a_hash_inside_a_fence_is_not_a_heading() {
    // Python written into a Markdown note would otherwise shatter it into a
    // section per comment.
    let note = "# Note\ntext\n```python\n# not a heading\nx = 1\n```\n## Real\nmore\n";

    let titles: Vec<String> = sections("note.md", note)
        .into_iter()
        .map(|s| s.title)
        .collect();

    assert_eq!(titles, vec!["Note".to_string(), "Real".to_string()]);
}

#[test]
fn a_hashtag_without_a_space_is_not_a_heading() {
    let titles: Vec<String> = sections("note.md", "#nothashtag\n# Real\n")
        .into_iter()
        .map(|s| s.title)
        .collect();

    assert_eq!(titles, vec!["(preamble)".to_string(), "Real".to_string()]);
}

#[test]
fn a_python_file_is_mapped_by_its_top_level_definitions() {
    let code = "import sys\n\n\ndef first(n):\n    return n\n\n\nclass Second:\n    def method(self):\n        return 1\n";

    let titles: Vec<String> = sections("code/thing.py", code)
        .into_iter()
        .map(|s| s.title)
        .collect();

    // `method` is indented, so it belongs to its class rather than splitting it.
    assert_eq!(
        titles,
        vec![
            "(preamble)".to_string(),
            "def first".to_string(),
            "class Second".to_string()
        ]
    );
}

#[test]
fn a_document_with_no_structure_still_gets_coordinates() {
    // Otherwise the ceiling is a wall: a 300 KB column of integers would be
    // unreadable rather than readable in parts.
    let flat = "1\n".repeat(500);

    let found = sections("out/data.txt", &flat);

    assert!(found.len() > 1, "expected blocks, got {found:?}");
    assert_eq!(found[0].first_line, 1);
    assert_eq!(found.last().map(|s| s.last_line), Some(500));
}

#[test]
fn an_empty_document_still_has_one_addressable_block() {
    let found = sections("empty.md", "");

    assert_eq!(found.len(), 1);
    assert_eq!(found[0].first_line, 1);
}

#[test]
fn a_section_is_selected_by_a_substring_of_its_heading() {
    let slice = select("paper.md", PAPER, Some("meth"), None).expect("the section exists");

    assert!(slice.text.contains("the method is this"));
    assert!(!slice.text.contains("a result"));
    assert_eq!(slice.first_line, 5);
}

#[test]
fn an_ambiguous_section_names_the_candidates_instead_of_guessing() {
    // Reading the wrong section is indistinguishable from reading the right one
    // until a conclusion has already been drawn from it.
    let doc = "## Bound A\none\n## Bound B\ntwo\n";

    let error = select("d.md", doc, Some("bound"), None).expect_err("two sections match");

    let message = error.to_string();
    assert!(message.contains("Bound A"), "{message}");
    assert!(message.contains("Bound B"), "{message}");
}

#[test]
fn an_exact_heading_wins_over_the_substring_it_is_contained_in() {
    let doc = "## Gap\none\n## Gap Lemma\ntwo\n";

    let slice = select("d.md", doc, Some("Gap"), None).expect("the exact heading resolves");

    assert!(slice.text.contains("one"));
    assert!(!slice.text.contains("two"));
}

#[test]
fn a_missing_section_says_how_to_find_the_real_ones() {
    let error = select("paper.md", PAPER, Some("appendix"), None).expect_err("no such section");

    assert!(error.to_string().contains("outline_document"));
}

#[test]
fn a_line_range_is_returned_inclusive_of_both_ends() {
    let slice = select("paper.md", PAPER, None, Some("3-4")).expect("a valid range");

    assert_eq!(slice.text, "# Title\nopening\n");
    assert_eq!((slice.first_line, slice.last_line), (3, 4));
}

#[test]
fn an_open_ended_range_runs_to_the_end() {
    let slice = select("paper.md", PAPER, None, Some("9-")).expect("a valid range");

    assert!(slice.text.contains("fine print"));
    assert_eq!(slice.last_line, PAPER.lines().count());
}

#[test]
fn a_malformed_range_says_what_a_range_looks_like() {
    let error = select("paper.md", PAPER, None, Some("the middle")).expect_err("not a range");

    assert!(error.to_string().contains("120-260"));
}

#[test]
fn a_backwards_range_is_refused() {
    let error = select("paper.md", PAPER, None, Some("9-2")).expect_err("ends before it starts");

    assert!(error.to_string().contains("ends before it starts"));
}

#[test]
fn a_range_past_the_end_says_how_long_the_document_is() {
    let error = select("paper.md", PAPER, None, Some("900-")).expect_err("past the end");

    assert!(error.to_string().contains("11 lines"), "{error}");
}

#[test]
fn a_section_wins_when_both_selectors_are_given() {
    let slice = select("paper.md", PAPER, Some("Results"), Some("1-2")).expect("the section wins");

    assert!(slice.text.contains("a result"));
}

#[test]
fn an_oversized_selection_is_cut_at_a_line_and_says_where_to_resume() {
    let huge = "x".repeat(200) + "\n";
    let doc = huge.repeat(500);

    let slice = select("big.md", &doc, None, Some("1-")).expect("a valid range");

    assert!(slice.truncated);
    assert!(slice.text.len() <= MAX_SLICE_BYTES);
    // Cut at a line, so the last line is whole and the next range is exact.
    assert!(slice.text.ends_with('\n'));
    let rendered = super::render_slice("big.md", doc.lines().count(), &slice);
    assert!(
        rendered.contains(&format!("lines \"{}-\"", slice.last_line + 1)),
        "{rendered}"
    );
}

#[test]
fn a_region_is_not_cut_where_a_slice_would_be() {
    // The recursive read depends on this: a bounded region would silently
    // truncate the one path whose purpose is to cover a document completely.
    let doc = ("x".repeat(200) + "\n").repeat(500);

    let region = region("big.md", &doc, None, None).expect("the whole document");

    assert_eq!(region.text.len(), doc.len());
    assert!(region.text.len() > MAX_SLICE_BYTES);
}

#[test]
fn an_oversized_unselected_read_is_answered_with_navigation() {
    let doc = "# One\n".to_string() + &"filler\n".repeat(MAX_UNSELECTED_BYTES / 7 + 10);

    let answer = too_large("big.md", &doc);

    assert!(answer.contains("too large to read whole"));
    assert!(answer.contains("outline of big.md"));
    // The refusal must carry the way forward, or it has cost a turn to say no.
    assert!(answer.contains("read_document"));
    // And it must be far smaller than what it withheld.
    assert!(answer.len() < doc.len() / 4, "{} bytes", answer.len());
}

#[test]
fn an_outline_of_a_very_long_document_is_itself_bounded() {
    let doc = (1..=400)
        .map(|n| format!("## Section {n}\nbody\n"))
        .collect::<String>();

    let rendered = render("many.md", &doc);

    assert!(rendered.contains("further sections"), "{rendered}");
    assert!(rendered.len() < 20_000, "{} bytes", rendered.len());
}
