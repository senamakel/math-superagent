//! Unit tests for the formalisation mill.
#![allow(clippy::expect_used)]

use std::path::{Path, PathBuf};

use super::{Candidate, LIB_DIR, Source, gather, parse_candidates, safe_name};

fn candidate(name: &str, cited: bool) -> Candidate {
    Candidate {
        name: name.to_string(),
        statement: "every monic polynomial of degree n has n roots".to_string(),
        provenance: "Berger 2019, Theorem 2".to_string(),
        cited,
    }
}

#[test]
fn a_bare_arxiv_id_and_a_prefixed_one_are_the_same_source() {
    assert_eq!(
        Source::parse("2401.00001"),
        Some(Source::Arxiv("2401.00001".to_string()))
    );
    assert_eq!(
        Source::parse("arxiv:2401.00001"),
        Some(Source::Arxiv("2401.00001".to_string()))
    );
    assert_eq!(
        Source::parse("2401.00001v2"),
        Some(Source::Arxiv("2401.00001v2".to_string()))
    );
}

#[test]
fn a_url_is_a_url_and_a_path_is_a_path() {
    assert_eq!(
        Source::parse("https://example.org/paper.pdf"),
        Some(Source::Url("https://example.org/paper.pdf".to_string()))
    );
    assert_eq!(
        Source::parse("research/summaries"),
        Some(Source::Workspace(PathBuf::from("research/summaries")))
    );
    assert_eq!(Source::parse("   "), None);
}

/// A version suffix is part of the id; a section number is not an id at all.
#[test]
fn something_that_merely_contains_a_dot_is_not_an_arxiv_id() {
    for raw in ["notes/thm.md", "1.2", "20240.0001", "abcd.0001"] {
        assert!(
            !matches!(Source::parse(raw), Some(Source::Arxiv(_))),
            "`{raw}` is not an arXiv id"
        );
    }
}

#[test]
fn a_name_is_folded_into_something_lean_will_accept() {
    assert_eq!(safe_name("Cauchy Bound"), Some("cauchy_bound".to_string()));
    assert_eq!(safe_name("main-bound/step 2"), Some("main_bound_step_2".to_string()));
    assert_eq!(safe_name("  "), None);
    assert_eq!(safe_name("!!!"), None);
}

/// A leading digit is prefixed rather than trimmed away.
///
/// Trimming would turn `2_adic_bound` into `adic_bound`, which is a different
/// lemma's name and would overwrite that lemma's file.
#[test]
fn a_name_starting_with_a_digit_keeps_its_digits() {
    assert_eq!(safe_name("2-adic bound"), Some("lemma_2_adic_bound".to_string()));
}

#[test]
fn candidates_are_read_out_of_a_fenced_reply() {
    let reply = r#"Here are the statements I found:

```json
[
  {"name": "Cauchy bound", "statement": "every root is bounded by 1 + max|a_i|", "source": "Berger 2019 Thm 2", "cited": false},
  {"name": "Marden", "statement": "the critical points lie in the Steiner inellipse", "source": "Marden 1945", "cited": true}
]
```

That is all."#;

    let candidates = parse_candidates(reply);

    assert_eq!(candidates.len(), 2);
    assert_eq!(candidates[0].name, "cauchy_bound");
    assert!(!candidates[0].cited);
    assert_eq!(candidates[1].name, "marden");
    assert!(candidates[1].cited, "a quoted result must stay quoted");
    assert_eq!(candidates[1].provenance, "Marden 1945");
}

/// One malformed row must not cost the run the rows around it.
#[test]
fn a_malformed_row_is_skipped_rather_than_failing_the_batch() {
    let reply = r#"[
      {"name": "good_one", "statement": "a true thing"},
      {"name": "no statement"},
      {"statement": "no name"},
      {"name": "   ", "statement": "unnameable"},
      {"name": "second_good", "statement": "another true thing"}
    ]"#;

    let candidates = parse_candidates(reply);

    let names: Vec<&str> = candidates.iter().map(|c| c.name.as_str()).collect();
    assert_eq!(names, ["good_one", "second_good"]);
}

/// Two candidates with one name would write one file and both report success.
#[test]
fn candidates_are_deduplicated_by_the_file_they_would_write() {
    let reply = r#"[
      {"name": "Cauchy bound", "statement": "first wording"},
      {"name": "cauchy_bound", "statement": "second wording of the same lemma"}
    ]"#;

    let candidates = parse_candidates(reply);

    assert_eq!(candidates.len(), 1);
    assert_eq!(candidates[0].statement, "first wording");
}

#[test]
fn a_reply_with_no_array_yields_nothing_rather_than_panicking() {
    for reply in ["I could not find any statements.", "", "[", "[{]"] {
        assert!(parse_candidates(reply).is_empty(), "`{reply}`");
    }
}

/// A bracket inside a string must not close the array early.
#[test]
fn a_bracket_inside_a_statement_does_not_truncate_the_list() {
    let reply = r#"[
      {"name": "interval", "statement": "the set [0, 1] is compact"},
      {"name": "second", "statement": "and another"}
    ]"#;

    let candidates = parse_candidates(reply);

    assert_eq!(candidates.len(), 2);
    assert!(candidates[0].statement.contains("[0, 1]"));
}

#[test]
fn a_candidate_writes_into_the_library_rather_than_the_working_directory() {
    assert_eq!(
        candidate("cauchy_bound", false).source_path(),
        format!("{LIB_DIR}/cauchy_bound.lean")
    );
}

/// The whole of the `Cited` rule, at the point it is decided.
#[test]
fn a_quoted_result_is_briefed_as_an_axiom_and_a_proved_one_as_a_theorem() {
    let quoted = candidate("marden", true).briefing();
    assert!(quoted.contains("axiom"));
    assert!(quoted.contains("namespace Cited"));
    assert!(
        quoted.contains("Do not write a proof"),
        "a cited axiom is asserted, not proved"
    );

    let proved = candidate("cauchy_bound", false).briefing();
    assert!(proved.contains("theorem"));
    assert!(proved.contains("#print axioms"));
    assert!(!proved.contains("namespace Cited"));

    // Both carry provenance, because an assumption whose source is lost is not
    // a citation.
    for briefing in [quoted, proved] {
        assert!(briefing.contains("Berger 2019, Theorem 2"));
    }
}

#[test]
fn a_directory_is_read_in_name_order_and_bounded() {
    let root = tempfile::tempdir().expect("a temporary workspace");
    let notes = root.path().join("research/notes");
    std::fs::create_dir_all(&notes).expect("the notes directory");
    for (name, body) in [("b.md", "second"), ("a.md", "first"), ("c.txt", "ignored")] {
        std::fs::write(notes.join(name), body).expect("a note");
    }

    let (gathered, unread) = gather(root.path(), Path::new("research/notes"), 1_000);
    assert_eq!(unread, 0);

    let labels: Vec<&str> = gathered.iter().map(|(label, _)| label.as_str()).collect();
    assert_eq!(labels.len(), 2, "only Markdown is read");
    assert!(labels[0].ends_with("a.md"), "read in name order");
    assert!(labels[1].ends_with("b.md"));
}

#[test]
fn the_byte_bound_stops_a_directory_becoming_one_prompt() {
    let root = tempfile::tempdir().expect("a temporary workspace");
    let notes = root.path().join("notes");
    std::fs::create_dir_all(&notes).expect("the notes directory");
    for name in ["a.md", "b.md", "c.md"] {
        std::fs::write(notes.join(name), "x".repeat(100)).expect("a note");
    }

    let (gathered, unread) = gather(root.path(), Path::new("notes"), 250);

    assert_eq!(gathered.len(), 2, "the third note does not fit");
    assert_eq!(
        unread, 1,
        "a file that did not fit must be counted, or the run reads as complete"
    );
}

#[test]
fn a_single_file_is_read_as_itself() {
    let root = tempfile::tempdir().expect("a temporary workspace");
    std::fs::create_dir_all(root.path().join("research")).expect("the directory");
    std::fs::write(root.path().join("research/one.md"), "a statement").expect("the note");

    let (gathered, unread) = gather(root.path(), Path::new("research/one.md"), 1_000);

    assert_eq!(gathered.len(), 1);
    assert_eq!(unread, 0);
    assert_eq!(gathered[0].1, "a statement");
}

#[test]
fn a_missing_path_yields_nothing_rather_than_failing() {
    let root = tempfile::tempdir().expect("a temporary workspace");
    assert!(gather(root.path(), Path::new("nowhere"), 1_000).0.is_empty());
}
