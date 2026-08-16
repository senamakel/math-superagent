//! Unit tests for the scored program search: what the verifier's output is
//! allowed to mean, what the ledger survives, and what a proposal is shown.
//!
//! The parsing tests need nothing installed, because the verifier boundary is
//! where the interesting mistakes are — an `inf` read as a score puts a program
//! that exploited the scorer on top of the board permanently, and no amount of
//! process-spawn coverage would notice. The tool tests do run `python3`, and
//! skip themselves when it is absent rather than failing a host that has no
//! reason to have it.
#![allow(clippy::expect_used)]

use std::path::{Path, PathBuf};

use super::{
    BOARD, CANDIDATE_DIR, LEDGER, Outcome, Population, SCORER, SEARCH_DIR, SearchBrief,
    SubmitCandidate, parse_outcome,
};
use crate::agent::{Tool, ToolCall};

/// A workspace of this test's own, so one test's ledger is not another's.
fn workspace_named(name: &str) -> PathBuf {
    let path = std::env::temp_dir().join(format!("search-test-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).expect("the test workspace is created");
    path
}

/// The directory one search's files live in.
fn search_root(workspace: &Path, slug: &str) -> PathBuf {
    let root = workspace.join(SEARCH_DIR).join(slug);
    std::fs::create_dir_all(&root).expect("the search directory is created");
    root
}

/// Writes a ledger verbatim, so a test can hand the loader a torn line.
fn write_ledger(workspace: &Path, slug: &str, text: &str) {
    let root = search_root(workspace, slug);
    std::fs::write(root.join(LEDGER), text).expect("the ledger is written");
}

/// Writes a scorer that ignores the candidate and prints one fixed line.
///
/// Fixed on purpose: importing the candidate would make these tests depend on
/// what a candidate happens to contain, and the tool contract under test is
/// "run the scorer, read its verdict", not "run mathematics".
fn write_scorer(workspace: &Path, slug: &str, verdict: &str) {
    let root = search_root(workspace, slug);
    std::fs::write(
        root.join(SCORER),
        format!("import sys\n_ = sys.argv[1]\nprint({verdict:?})\n"),
    )
    .expect("the scorer is written");
}

/// Whether the host can run a scorer at all.
fn has_python() -> bool {
    std::process::Command::new("python3")
        .arg("--version")
        .output()
        .is_ok()
}

fn call(name: &str, arguments: serde_json::Value) -> ToolCall {
    ToolCall {
        id: "1".into(),
        name: name.into(),
        invalid: None,
        arguments,
    }
}

/// The value a scored outcome carries; `None` when the scorer rejected it.
fn score_of(outcome: &Outcome) -> Option<(&str, f64)> {
    match outcome {
        Outcome::Scored { shown, value } => Some((shown.as_str(), *value)),
        Outcome::Invalid(_) => None,
    }
}

/// The reason a rejection carries; `None` when it was scored.
fn reason_of(outcome: &Outcome) -> Option<&str> {
    match outcome {
        Outcome::Scored { .. } => None,
        Outcome::Invalid(reason) => Some(reason.as_str()),
    }
}

/// One row of a ledger, as the tool writes it.
fn scored_row(id: &str, island: usize, score: &str) -> String {
    format!("{{\"id\":\"{id}\",\"island\":{island},\"score\":\"{score}\"}}\n")
}

/// One rejected row of a ledger.
fn discarded_row(id: &str, island: usize, reason: &str) -> String {
    format!("{{\"id\":\"{id}\",\"island\":{island},\"reason\":\"{reason}\"}}\n")
}

#[test]
fn a_plain_decimal_score_is_read_as_a_value() {
    let outcome = parse_outcome("SCORE: 12.5\n");
    let (shown, value) = score_of(&outcome).expect("a decimal score is scored");
    assert_eq!(shown, "12.5");
    assert!((value - 12.5).abs() < f64::EPSILON);
}

/// The exact-arithmetic path. A scorer told to avoid floating point prints a
/// fraction, so a search that could not order `355/113` would silently discard
/// every exact score — precisely the candidates the rule exists to protect.
#[test]
fn an_exact_fraction_is_ordered_without_losing_how_it_was_printed() {
    let outcome = parse_outcome("SCORE: 355/113");
    let (shown, value) = score_of(&outcome).expect("a fraction is scored");
    assert_eq!(shown, "355/113", "the board shows what the scorer printed");
    assert!((value - 355.0 / 113.0).abs() < 1e-12);
}

/// A scorer that reports progress before its verdict must not be misread as
/// having scored the progress line.
#[test]
fn the_last_score_line_wins_over_earlier_ones() {
    let outcome = parse_outcome("SCORE: 1\nsearching deeper\nSCORE: 7.5\n");
    let (shown, value) = score_of(&outcome).expect("the verdict is scored");
    assert_eq!(shown, "7.5");
    assert!((value - 7.5).abs() < f64::EPSILON);
}

#[test]
fn an_invalid_line_is_a_rejection_carrying_its_reason() {
    let outcome = parse_outcome("INVALID: the points are not distinct\n");
    let reason = reason_of(&outcome).expect("an INVALID line is a rejection");
    assert!(reason.contains("the points are not distinct"));
}

/// A verifier that rejects a candidate and then reports a number for it has
/// contradicted itself. The rejection has to win: one discarded candidate out
/// of thousands costs nothing, and the other reading puts an unverified program
/// on the board.
#[test]
fn a_rejection_beats_a_score_printed_beside_it() {
    let outcome = parse_outcome("SCORE: 99999\nINVALID: constraint violated\n");
    let reason = reason_of(&outcome).expect("the rejection wins");
    assert!(reason.contains("constraint violated"));
}

/// Silence is not zero. A scorer that printed nothing recognisable approved
/// nothing, and defaulting to a number would enter an unverified candidate.
#[test]
fn output_with_no_marker_at_all_is_invalid_rather_than_zero() {
    let outcome = parse_outcome("Traceback (most recent call last):\n  ImportError\n");
    let reason = reason_of(&outcome).expect("no marker is a rejection");
    assert!(reason.contains("nothing was verified"));
    assert_eq!(score_of(&outcome), None);
}

/// An unparseable run must carry the scorer's own words back, or the searcher
/// cannot tell a broken scorer from a broken candidate.
///
/// Taken verbatim from the first scored search that ever ran on this harness.
/// The Frankl scorer wanted five floats while `submit_candidate` calls it with
/// one module path, so every candidate exited on the `usage:` line. Seven were
/// written against a contract the harness never speaks, each told only that
/// "nothing was verified" — true, unactionable, and indistinguishable from a
/// fault in the candidate itself.
#[test]
fn a_scorer_that_scored_nothing_says_what_it_printed() {
    let outcome = parse_outcome("usage: python score.py alpha a1 a2 b1 b2 [N] [REF_T]\n");
    let reason = reason_of(&outcome).expect("no marker is a rejection");
    assert!(
        reason.contains("usage: python score.py alpha a1 a2 b1 b2"),
        "the searcher must be told what the scorer said, but got: {reason}"
    );
    assert_eq!(score_of(&outcome), None);
}

/// The tail, not the head: a traceback's last line names the exception, and a
/// head would spend the whole budget on stack frames and cut off before it.
#[test]
fn a_long_traceback_is_carried_back_by_its_informative_end() {
    let frames = (0..200)
        .map(|at| format!("  File \"deep{at}.py\", line {at}, in nested_call_number_{at}"))
        .collect::<Vec<_>>()
        .join("\n");
    let outcome = parse_outcome(&format!(
        "Traceback (most recent call last):\n{frames}\nTypeError: points() takes 1 argument\n"
    ));
    let reason = reason_of(&outcome).expect("no marker is a rejection");
    assert!(
        reason.contains("TypeError: points() takes 1 argument"),
        "the exception must survive, but got: {reason}"
    );
    assert!(
        !reason.contains("Traceback (most recent call last)"),
        "the head is what gets dropped, but got: {reason}"
    );
    assert!(
        reason.chars().count() < 400,
        "a rejection must stay cheap, but is {} characters",
        reason.chars().count()
    );
}

/// A scorer that printed nothing at all has no words to carry, and the reason
/// must say *that* rather than trail off after a colon.
#[test]
fn a_silent_scorer_is_reported_as_silent() {
    let outcome = parse_outcome("   \n\t\n");
    let reason = reason_of(&outcome).expect("no marker is a rejection");
    assert!(
        reason.contains("no output at all"),
        "silence must be named, but got: {reason}"
    );
    assert!(
        !reason.ends_with(": "),
        "the reason must not trail off: {reason}"
    );
}

/// The verifier-exploit shape. A candidate that divides by the constraint it
/// was meant to satisfy scores `inf`, and an `inf` accepted once tops the board
/// for the rest of the run — no later candidate can beat it.
#[test]
fn an_infinite_or_nan_score_is_refused_as_a_verifier_exploit() {
    for printed in ["SCORE: inf", "SCORE: -inf", "SCORE: nan", "SCORE: NaN"] {
        let outcome = parse_outcome(printed);
        let reason = reason_of(&outcome).expect("an unusable value must not reach the board");
        assert!(
            reason.contains("unusable value"),
            "`{printed}` must say why: {reason}"
        );
    }
}

/// A fraction over zero is the same exploit wearing the exact-arithmetic
/// clothes, so it is refused at the same place.
#[test]
fn a_fraction_over_zero_is_not_a_score() {
    let outcome = parse_outcome("SCORE: 1/0");
    let reason = reason_of(&outcome).expect("a division by zero is not a score");
    assert!(reason.contains("unusable value"));
}

#[test]
fn a_search_with_no_ledger_loads_as_an_empty_population() {
    let workspace = workspace_named("no-ledger");
    let population = Population::load(&workspace, "never-started");
    assert!(population.candidates.is_empty());
    assert_eq!(population.best().map(|c| c.id.clone()), None);
    assert_eq!(population.discarded(), 0);
}

/// The ledger is append-only and its writer can be killed by the run cap
/// mid-line, so a torn final row is an ordinary event. Failing the load over one
/// would discard every hour of scoring that came before it.
#[test]
fn a_torn_final_line_is_skipped_and_the_earlier_rows_survive() {
    let workspace = workspace_named("torn");
    let mut text = scored_row("c0000", 0, "1.5");
    text.push_str(&scored_row("c0001", 1, "2.5"));
    text.push_str("{\"id\":\"c0002\",\"isl");
    write_ledger(&workspace, "cap", &text);

    let population = Population::load(&workspace, "cap");
    assert_eq!(population.candidates.len(), 2);
    assert_eq!(
        population.best().map(|c| c.id.clone()),
        Some("c0001".to_string())
    );
}

#[test]
fn the_best_is_the_highest_score_and_everything_else_is_counted_as_discarded() {
    let workspace = workspace_named("best");
    let mut text = scored_row("c0000", 0, "1");
    text.push_str(&scored_row("c0001", 0, "40"));
    text.push_str(&discarded_row("c0002", 0, "too slow"));
    text.push_str(&scored_row("c0003", 0, "12"));
    text.push_str(&discarded_row("c0004", 0, "too slow"));
    write_ledger(&workspace, "board", &text);

    let population = Population::load(&workspace, "board");
    assert_eq!(
        population.best().map(|c| c.id.clone()),
        Some("c0001".to_string())
    );
    assert_eq!(population.discarded(), 2);
}

#[test]
fn islands_are_handed_out_round_robin_over_the_recorded_count() {
    let workspace = workspace_named("round-robin");
    let mut text = String::new();
    let mut seen = Vec::new();
    for index in 0_usize..6 {
        seen.push(Population::load(&workspace, "rr").next_island());
        text.push_str(&scored_row(&format!("c{index:04}"), index % 4, "1"));
        write_ledger(&workspace, "rr", &text);
    }
    assert_eq!(seen, vec![0, 1, 2, 3, 0, 1]);
}

/// `FunSearch`'s ordering, and the reason the brief reads as "improve on the last
/// one": the last program in the prompt is the one the model builds on, so the
/// best has to be last. Reversing this would ask every proposal to improve on
/// the worst program the island has.
#[test]
fn a_best_shot_carries_two_programs_worst_first() {
    let workspace = workspace_named("best-shot-order");
    let mut text = scored_row("c0000", 0, "5");
    text.push_str(&scored_row("c0001", 0, "9"));
    text.push_str(&scored_row("c0002", 0, "7"));
    write_ledger(&workspace, "order", &text);

    let population = Population::load(&workspace, "order");
    let sample = population.best_shot(0);
    let ids: Vec<&str> = sample.iter().map(|c| c.id.as_str()).collect();
    assert_eq!(ids, vec!["c0002", "c0001"], "worst first, best last");
}

/// A young island has to be able to propose from one program, and a discarded
/// candidate is never one of them — it is on the ledger to be counted, not to be
/// imitated.
#[test]
fn a_thin_island_shows_what_it_has_and_never_a_discarded_program() {
    let workspace = workspace_named("thin-island");
    let mut text = scored_row("c0000", 0, "3");
    text.push_str(&discarded_row("c0001", 0, "did not run"));
    write_ledger(&workspace, "thin", &text);

    let population = Population::load(&workspace, "thin");
    let sample = population.best_shot(0);
    assert_eq!(sample.len(), 1);
    assert_eq!(sample[0].id, "c0000");
    assert!(population.best_shot(2).is_empty(), "an empty island has none");
}

/// The reset. An island that has recorded twelve candidates without a gain is
/// proposing variations on a local optimum, so its next brief is drawn from the
/// whole population's best instead of its own — which is what makes a reset
/// explore rather than forget, since nothing on the ledger is deleted.
#[test]
fn a_stale_island_is_reseeded_from_the_whole_populations_best() {
    let workspace = workspace_named("stale");
    let mut text = scored_row("c0000", 0, "1");
    for index in 1_usize..=12 {
        text.push_str(&scored_row(&format!("c{index:04}"), 0, "0.5"));
    }
    text.push_str(&scored_row("c0013", 1, "99"));
    write_ledger(&workspace, "stale", &text);

    let population = Population::load(&workspace, "stale");
    let sample = population.best_shot(0);
    let ids: Vec<&str> = sample.iter().map(|c| c.id.as_str()).collect();
    assert_eq!(ids, vec!["c0000", "c0013"], "worst first, the import last");
    assert_eq!(
        sample[1].island, 1,
        "a stale island draws from another island's best"
    );

    // The island that is not stale still sees only its own.
    let fresh = population.best_shot(1);
    assert_eq!(fresh.len(), 1);
    assert_eq!(fresh[0].id, "c0013");
}

/// An empty board is the one that has to say what to do next: nothing can score
/// until the scorer exists, and the searcher is not the role that writes it.
#[test]
fn an_empty_board_asks_for_the_scorer_first() {
    let rendered = Population::default().render("capset");
    assert!(rendered.contains("capset"));
    assert!(rendered.contains("Nothing scored yet"));
    assert!(rendered.contains(SCORER), "it names the file to write");
    assert!(rendered.contains("exact arithmetic"));
}

/// The counts rather than the rows: a search whose rejections are all one
/// reason has found either a scorer too slow to search with or the constraint
/// that actually binds, and neither is visible from a list of winners.
#[test]
fn a_populated_board_ranks_the_scored_and_counts_why_the_rest_went() {
    let workspace = workspace_named("render");
    let mut text = scored_row("c0000", 0, "1.5");
    text.push_str(&scored_row("c0001", 1, "9.5"));
    text.push_str(&discarded_row("c0002", 2, "too slow"));
    text.push_str(&discarded_row("c0003", 3, "too slow"));
    text.push_str(&discarded_row("c0004", 0, "constraint violated"));
    write_ledger(&workspace, "render", &text);

    let rendered = Population::load(&workspace, "render").render("render");
    assert!(rendered.contains("2 candidates scored, 3 discarded"));
    let best_at = rendered
        .find("c0001")
        .expect("the best candidate is on the board");
    let worse_at = rendered
        .find("c0000")
        .expect("the other candidate is on the board");
    assert!(best_at < worse_at, "rows are best first: {rendered}");
    assert!(rendered.contains("## Why candidates were discarded"));
    assert!(rendered.contains("2× too slow"));
    assert!(rendered.contains("1× constraint violated"));
    // A discarded candidate is counted, not ranked.
    assert!(!rendered.contains("c0002"), "no row for a rejection");
}

#[tokio::test]
async fn a_candidate_cannot_be_submitted_before_a_scorer_exists() {
    // Nothing can score it, so nothing may record it: a candidate on the board
    // that was never executed is the failure the one-call design prevents.
    let workspace = workspace_named("no-scorer");
    search_root(&workspace, "unscored");
    let tool = SubmitCandidate::new(workspace.clone());
    let refused = tool
        .call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "unscored", "program": "x = 1\n" }),
            ),
        )
        .await;
    assert!(refused.is_err(), "there is nothing to score against");
    assert!(
        !workspace
            .join(SEARCH_DIR)
            .join("unscored")
            .join(LEDGER)
            .exists(),
        "and nothing was recorded"
    );
}

#[tokio::test]
async fn a_scored_submission_writes_the_program_one_ledger_line_and_the_board() {
    if !has_python() {
        // The scorer is a Python process; without an interpreter there is
        // nothing under test here that is not already covered by parse_outcome.
        return;
    }
    let workspace = workspace_named("submit");
    write_scorer(&workspace, "capset", "SCORE: 12.5");
    let tool = SubmitCandidate::new(workspace.clone());
    let result = tool
        .call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "capset", "program": "def solve():\n    return 1\n" }),
            ),
        )
        .await
        .expect("a scored candidate is recorded");

    let root = workspace.join(SEARCH_DIR).join("capset");
    let program = std::fs::read_to_string(root.join(CANDIDATE_DIR).join("c0000.py"))
        .expect("the candidate is on disk under its derived id");
    assert!(program.contains("def solve()"));
    let ledger = std::fs::read_to_string(root.join(LEDGER)).expect("the ledger is written");
    assert_eq!(ledger.lines().count(), 1, "exactly one row: {ledger}");
    assert!(ledger.contains("\"score\":\"12.5\""));
    let board = std::fs::read_to_string(root.join(BOARD)).expect("the board is rewritten");
    assert!(board.contains("c0000"));
    assert!(result.content.contains("12.5"));
}

/// The id is derived from the ledger's length rather than supplied, so a second
/// proposal cannot overwrite the first — by collision or by choosing to.
#[tokio::test]
async fn candidate_ids_increment_so_a_submission_cannot_overwrite_an_earlier_one() {
    if !has_python() {
        return;
    }
    let workspace = workspace_named("ids");
    write_scorer(&workspace, "ids", "SCORE: 1");
    let tool = SubmitCandidate::new(workspace.clone());
    for program in ["first = 1\n", "second = 2\n"] {
        tool.call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "ids", "program": program }),
            ),
        )
        .await
        .expect("each candidate is recorded");
    }

    let root = workspace.join(SEARCH_DIR).join("ids");
    let first = std::fs::read_to_string(root.join(CANDIDATE_DIR).join("c0000.py"))
        .expect("the first candidate survives");
    let second = std::fs::read_to_string(root.join(CANDIDATE_DIR).join("c0001.py"))
        .expect("the second lands beside it");
    assert!(first.contains("first"));
    assert!(second.contains("second"));
    assert_eq!(
        std::fs::read_to_string(root.join(LEDGER))
            .expect("the ledger is written")
            .lines()
            .count(),
        2
    );
}

/// A search is wrong thousands of times, so a rejection must cost as close to
/// nothing as possible: one short line, no advice, and no reflection. A
/// paragraph of guidance here would be re-read on every discarded candidate.
#[tokio::test]
async fn a_rejected_candidate_is_recorded_and_answered_in_one_short_line() {
    if !has_python() {
        return;
    }
    let workspace = workspace_named("rejected");
    write_scorer(&workspace, "reject", "INVALID: the points coincide");
    let tool = SubmitCandidate::new(workspace.clone());
    let result = tool
        .call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "reject", "program": "x = 1\n" }),
            ),
        )
        .await
        .expect("a rejection is an ordinary result, not a tool failure");

    assert!(result.content.contains("discarded"));
    assert!(
        !result.content.trim().contains('\n'),
        "one line: {}",
        result.content
    );
    assert!(
        result.content.len() < 160,
        "a rejection must be cheap: {}",
        result.content
    );

    let root = workspace.join(SEARCH_DIR).join("reject");
    let ledger = std::fs::read_to_string(root.join(LEDGER)).expect("it is still recorded");
    assert_eq!(ledger.lines().count(), 1);
    assert!(ledger.contains("the points coincide"));
    let population = Population::load(&workspace, "reject");
    assert_eq!(population.discarded(), 1);
    assert!(population.best().is_none());
}

/// A slug is one directory name. Traversal is not the only way to misuse one —
/// a separator would scatter a search's programs across a tree its own board
/// could not then find.
#[tokio::test]
async fn a_slug_that_is_not_a_single_directory_name_is_refused() {
    let workspace = workspace_named("slug");
    let submit = SubmitCandidate::new(workspace.clone());
    let brief = SearchBrief::new(workspace);
    for slug in ["../escape", "nested/search", "..", ""] {
        assert!(
            submit
                .call(
                    &(),
                    call(
                        "submit_candidate",
                        serde_json::json!({ "slug": slug, "program": "x = 1\n" })
                    )
                )
                .await
                .is_err(),
            "`{slug}` must be refused by submit"
        );
        assert!(
            brief
                .call(&(), call("search_brief", serde_json::json!({ "slug": slug })))
                .await
                .is_err(),
            "`{slug}` must be refused by the brief"
        );
    }
}

#[tokio::test]
async fn a_brief_without_a_scorer_says_the_scorer_is_not_the_searchers_to_write() {
    let workspace = workspace_named("brief-no-scorer");
    search_root(&workspace, "unscored");
    let tool = SearchBrief::new(workspace);
    let refused = tool
        .call(
            &(),
            call("search_brief", serde_json::json!({ "slug": "unscored" })),
        )
        .await;
    let message = refused.expect_err("a search with no scorer is refused");
    assert!(format!("{message}").contains(SCORER));
}

/// The brief is a tool rather than prompt context because it changes on every
/// candidate: it has to carry the verifier the program will face and the
/// programs it is meant to improve on.
#[tokio::test]
async fn a_brief_carries_the_scorer_source_and_the_previous_programs() {
    let workspace = workspace_named("brief");
    write_scorer(&workspace, "capset", "SCORE: 1");
    let root = workspace.join(SEARCH_DIR).join("capset");
    std::fs::write(root.join("PROBLEM.md"), "Maximise the cap set.\n")
        .expect("the problem is written");
    std::fs::create_dir_all(root.join(CANDIDATE_DIR)).expect("the candidate folder is created");
    std::fs::write(
        root.join(CANDIDATE_DIR).join("c0000.py"),
        "def priority():\n    return 41\n",
    )
    .expect("the previous program is written");
    // Island 1, because with one candidate recorded the next proposal is that
    // island's — a brief that sampled another island's would show nothing.
    write_ledger(&workspace, "capset", &scored_row("c0000", 1, "3"));

    let tool = SearchBrief::new(workspace);
    let result = tool
        .call(
            &(),
            call("search_brief", serde_json::json!({ "slug": "capset" })),
        )
        .await
        .expect("the brief is produced");

    assert!(result.content.contains("Maximise the cap set"));
    assert!(
        result.content.contains("_ = sys.argv[1]"),
        "the scorer source is shown: {}",
        result.content
    );
    assert!(result.content.contains("you cannot edit it"));
    assert!(
        result.content.contains("return 41"),
        "the previous program is shown: {}",
        result.content
    );
    assert!(result.content.contains("worst first"));
}

/// Two searchers submitting at once must not be handed the same id.
///
/// The id used to be the count of *parsed* ledger rows, so both callers read
/// the same length, both wrote `candidates/c0000.py`, and one program was
/// destroyed while both rows landed in the ledger pointing at the survivor.
/// Sharing one population across concurrent searchers is the reason to run more
/// than one, so this is the ordinary case rather than a rare one.
#[tokio::test]
async fn two_submissions_racing_on_one_ledger_get_different_ids_and_both_programs_survive() {
    if !has_python() {
        return;
    }
    let workspace = workspace_named("race");
    write_scorer(&workspace, "capset", "SCORE: 1");
    let tool = SubmitCandidate::new(workspace.clone());

    let (left, right) = tokio::join!(
        tool.call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "capset", "program": "# left\n" }),
            ),
        ),
        tool.call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "capset", "program": "# right\n" }),
            ),
        ),
    );
    left.expect("the first submission succeeds");
    right.expect("the second submission succeeds");

    let candidates = search_root(&workspace, "capset").join(CANDIDATE_DIR);
    let mut written: Vec<String> = std::fs::read_dir(&candidates)
        .expect("the candidate directory exists")
        .filter_map(|entry| Some(entry.ok()?.file_name().to_string_lossy().into_owned()))
        .collect();
    written.sort();
    assert_eq!(
        written.len(),
        2,
        "each submission must own a file, but found {written:?}"
    );

    // Both programs, not one twice: an overwrite loses a body while keeping
    // both ledger rows, which is invisible from the row count alone.
    let bodies: std::collections::BTreeSet<String> = written
        .iter()
        .map(|name| std::fs::read_to_string(candidates.join(name)).unwrap_or_default())
        .collect();
    assert_eq!(bodies.len(), 2, "one program was overwritten: {bodies:?}");

    let population = Population::load(&workspace, "capset");
    assert_eq!(population.candidates.len(), 2);
    let ids: std::collections::BTreeSet<&str> = population
        .candidates
        .iter()
        .map(|candidate| candidate.id.as_str())
        .collect();
    assert_eq!(ids.len(), 2, "the ledger recorded one id twice: {ids:?}");
}

/// A torn line must not make the next candidate overwrite an existing program.
///
/// `Population::load` skips an unparseable row on purpose, which also lowers
/// the count the id was derived from — so the very next submission reused a
/// live id. The reservation scans past what is on disk instead of trusting the
/// count, so a torn ledger costs one row and no program.
#[tokio::test]
async fn a_torn_ledger_line_does_not_make_the_next_candidate_overwrite_an_earlier_one() {
    if !has_python() {
        return;
    }
    let workspace = workspace_named("torn-reserve");
    write_scorer(&workspace, "capset", "SCORE: 1");
    let root = search_root(&workspace, "capset");
    std::fs::create_dir_all(root.join(CANDIDATE_DIR)).expect("candidates directory is creatable");
    // Two candidates on disk, but the second row is torn, so the population
    // parses one and would previously have handed out `c0001` again.
    for id in ["c0000", "c0001"] {
        std::fs::write(
            root.join(CANDIDATE_DIR).join(format!("{id}.py")),
            format!("# {id}\n"),
        )
        .expect("write is possible");
    }
    write_ledger(
        &workspace,
        "capset",
        &format!("{}\n{{\"id\": \"c0001\", \"isla", scored_row("c0000", 0, "1")),
    );
    assert_eq!(Population::load(&workspace, "capset").candidates.len(), 1);

    SubmitCandidate::new(workspace.clone())
        .call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "capset", "program": "# fresh\n" }),
            ),
        )
        .await
        .expect("the submission succeeds");

    assert_eq!(
        std::fs::read_to_string(root.join(CANDIDATE_DIR).join("c0001.py"))
            .expect("the earlier candidate still exists"),
        "# c0001\n",
        "the torn row's program was overwritten"
    );
}

/// A board cut to its bound must say so, and say where the rest is.
///
/// `render` took `MAX_ROWS` on both its sections and appended nothing, so a
/// search with four hundred scored candidates produced a file that read as the
/// complete list of twenty. That is the failure the whole ledger budget exists
/// to prevent — a cut list reading as complete is worse than a long one,
/// because the reader concludes the run holds nothing more.
#[test]
fn the_board_says_how_many_rows_it_left_out_and_where_the_rest_is() {
    let workspace = workspace_named("elision");
    let mut text = String::new();
    for index in 0..60 {
        text.push_str(&scored_row(&format!("c{index:04}"), index % 4, "1.5"));
    }
    // More distinct discard reasons than the section can show, so both bounds
    // are exercised by one fixture.
    for index in 60..100 {
        text.push_str(&discarded_row(
            &format!("c{index:04}"),
            index % 4,
            &format!("reason number {index}"),
        ));
    }
    write_ledger(&workspace, "elision", &text);

    let rendered = Population::load(&workspace, "elision").render("elision");
    assert!(
        rendered.contains("60 candidates scored, 40 discarded"),
        "the counts are always exact, whatever the sections show: {rendered}"
    );
    assert!(
        rendered.contains("40 more not shown here"),
        "the leaderboard must say what it dropped: {rendered}"
    );
    assert!(
        rendered.contains(LEDGER),
        "an elision must name where the rest is: {rendered}"
    );
}

/// Past the bound, more candidates must not mean more file.
///
/// A ceiling alone cannot catch a section that grows slowly, and this is the
/// property that actually matters for a search — the one ledger whose entry
/// count is unbounded by design, since being wrong thousands of times cheaply
/// is the method.
#[test]
fn past_the_bound_more_candidates_do_not_grow_the_board() {
    let render_with = |count: usize, name: &str| {
        let workspace = workspace_named(name);
        let mut text = String::new();
        for index in 0..count {
            text.push_str(&scored_row(&format!("c{index:04}"), index % 4, "1.5"));
            // Distinct reasons, each absurdly long. Identical ones would fold
            // into a single counted row and the rejection section would be
            // flat whatever the renderer did — a fixture that cannot fail.
            text.push_str(&discarded_row(
                &format!("d{index:04}"),
                index % 4,
                &format!("reason {index} {}", "x".repeat(6_000)),
            ));
        }
        write_ledger(&workspace, name, &text);
        Population::load(&workspace, name).render(name).len()
    };

    let small = render_with(300, "ceiling-small");
    let large = render_with(900, "ceiling-large");
    assert!(
        large.saturating_sub(small) < 200,
        "the board grew by {} characters between 300 and 900 candidates",
        large - small
    );
    assert!(
        large < 20_000,
        "the board is {large} characters against a 20,000 ceiling"
    );
}

/// A scorer that allocates without bound must lose the candidate, not the run.
///
/// The container's cap is 8 GiB and kills the whole investigation, leaving an
/// OOM to be reconstructed from `docker events`. `SCORER_MEMORY` is far below
/// it so the scorer dies first and the search carries on with an ordinary
/// rejection.
#[tokio::test]
async fn a_scorer_that_allocates_without_bound_is_rejected_rather_than_killing_the_run() {
    if !has_python() {
        return;
    }
    let workspace = workspace_named("memory");
    let root = search_root(&workspace, "capset");
    std::fs::create_dir_all(&root).expect("the search directory is creatable");
    // Well past SCORER_MEMORY, and touched so it cannot be a lazy reservation.
    std::fs::write(
        root.join(SCORER),
        "import sys\nb = bytearray(6 * 1024 * 1024 * 1024)\nb[-1] = 1\nprint('SCORE: 999')\n",
    )
    .expect("write is possible");

    let result = SubmitCandidate::new(workspace.clone())
        .call(
            &(),
            call(
                "submit_candidate",
                serde_json::json!({ "slug": "capset", "program": "# hungry\n" }),
            ),
        )
        .await
        .expect("a rejected candidate is an ordinary result, never a tool error");
    assert!(
        result.content.contains("discarded"),
        "the candidate must be discarded, not scored 999: {}",
        result.content
    );

    let population = Population::load(&workspace, "capset");
    assert_eq!(population.candidates.len(), 1, "the attempt is still recorded");
    assert!(
        population.best().is_none(),
        "a scorer that never printed a verdict must put nothing on the board"
    );
}
