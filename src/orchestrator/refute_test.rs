//! Unit tests for the counterexample search: what the model builder's status
//! line means, and what the filed verdict is worth to a later reader.
//!
//! Every test here runs without `vampire` installed, which is deliberate. The
//! engine lives in the container image, so a parser exercised only there is one
//! the deterministic suite never checks — and the parse is where the
//! interesting mistakes are, not the process spawn.
#![allow(clippy::expect_used)]

use super::{FindCounterexample, Finding, VERDICT_DIR, Verdict, parse, verdict};
use crate::agent::{Tool, ToolCall};

/// A workspace of this test's own, so one test's verdicts are not another's.
fn workspace_named(name: &str) -> std::path::PathBuf {
    let path = std::env::temp_dir().join(format!("refute-test-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).expect("the test workspace is created");
    path
}

fn call(problem: &str) -> ToolCall {
    ToolCall {
        id: "1".into(),
        name: "find_counterexample".into(),
        invalid: None,
        arguments: serde_json::json!({ "problem": problem }),
    }
}

/// The interpretation `vampire` prints beside a `CounterSatisfiable`.
const MODEL: &str = "% SZS output start FiniteModel for girth
tff(declare_$i1,type,fmb_$i_1:$i).
tff(finite_domain,axiom,![X:$i]:(X = fmb_$i_1)).
% SZS output end FiniteModel for girth";

#[test]
fn counter_satisfiable_is_a_refutation() {
    let read = parse("code/refute/girth.p", "% SZS status CounterSatisfiable for girth");
    assert_eq!(read.finding, Finding::Refuted);
    assert_eq!(read.status, "CounterSatisfiable");
}

#[test]
fn satisfiable_is_a_refutation_too() {
    // The model builder answers `Satisfiable` when the problem it was handed
    // carries no conjecture of its own, which is the same news: the axioms plus
    // the negated goal have a model.
    let read = parse("code/refute/girth.p", "% SZS status Satisfiable for girth");
    assert_eq!(read.finding, Finding::Refuted);
}

#[test]
fn theorem_from_the_model_builder_is_a_proof() {
    // `fmb` really does return `Theorem` when the conjecture follows, so a
    // parse that recognised only the saturation vocabulary would file the one
    // outcome that ends the search as undecided.
    let read = parse("code/refute/girth.p", "% SZS status Theorem for girth");
    assert_eq!(read.finding, Finding::Proved);
    assert_eq!(read.status, "Theorem");
}

#[test]
fn unsatisfiable_is_a_proof() {
    let read = parse("code/refute/girth.p", "% SZS status Unsatisfiable");
    assert_eq!(read.finding, Finding::Proved);
}

#[test]
fn contradictory_axioms_are_read_as_their_own_finding() {
    // The verdict this module exists for. From contradictory hypotheses
    // everything follows, so a broken axiomatisation *proves the goal* and
    // reads like a triumph; folding `ContradictoryAxioms` into `Proved` would
    // hand the run a result about its own encoding as a result about the
    // mathematics.
    let read = parse(
        "code/refute/girth.p",
        "% SZS status ContradictoryAxioms for girth",
    );
    assert_eq!(read.finding, Finding::Contradictory);
    assert_eq!(read.status, "ContradictoryAxioms");
}

#[test]
fn the_ways_of_not_settling_are_all_undecided() {
    for word in ["Timeout", "GaveUp", "Unknown"] {
        let read = parse("code/refute/girth.p", &format!("% SZS status {word} for x"));
        assert_eq!(read.finding, Finding::Undecided, "`{word}` settles nothing");
        assert_eq!(read.status, word);
    }
}

#[test]
fn output_with_no_recognised_status_is_undecided_rather_than_an_error() {
    // The ordinary outcome of asking a hard question cheaply. An error here
    // would end the refuter's turn on the most common thing that happens, so
    // the fact recorded is "the engine ran and settled nothing".
    let read = parse("code/refute/girth.p", "% Time elapsed: 60.0 s\n% Refutation not found");
    assert_eq!(read.finding, Finding::Undecided);
    assert_eq!(read.status, "none reported");
    assert!(read.model.is_empty());
}

#[test]
fn an_unrecognised_status_word_does_not_overwrite_a_recognised_one() {
    // A portfolio prints vocabulary this parse has no entry for. Letting the
    // later unknown word clear the earlier verdict would lose the answer.
    let read = parse(
        "code/refute/girth.p",
        "% SZS status CounterSatisfiable for girth\n% SZS status WeirdThing for girth",
    );
    assert_eq!(read.finding, Finding::Refuted);
    assert_eq!(read.status, "CounterSatisfiable");
}

#[test]
fn the_last_recognised_status_wins() {
    // A portfolio reports each strategy's conclusion before the run's answer,
    // so the first status line on the page is not the one the engine stands by.
    let read = parse(
        "code/refute/girth.p",
        "% SZS status Timeout for girth\n% SZS status CounterSatisfiable for girth",
    );
    assert_eq!(read.finding, Finding::Refuted);
    assert_eq!(read.status, "CounterSatisfiable");
}

#[test]
fn the_printed_model_is_kept_without_its_markers() {
    let output = format!("% SZS status CounterSatisfiable for girth\n{MODEL}\n% Time elapsed: 0.1 s");
    let read = parse("code/refute/girth.p", &output);
    assert_eq!(read.finding, Finding::Refuted);
    assert_eq!(
        read.model,
        "tff(declare_$i1,type,fmb_$i_1:$i).\ntff(finite_domain,axiom,![X:$i]:(X = fmb_$i_1)).\n"
    );
    assert!(!read.model.contains("SZS output"), "neither marker is kept");
}

#[test]
fn a_refutation_with_no_printed_model_still_refutes() {
    // Inventing a model for it would be worse than saying nothing: the
    // counterexample is the part a person checks by hand.
    let read = parse(
        "code/refute/girth.p",
        "% SZS status CounterSatisfiable for girth\n% Time elapsed: 0.1 s",
    );
    assert_eq!(read.finding, Finding::Refuted);
    assert!(read.model.is_empty());
}

#[test]
fn a_proof_or_a_timeout_carries_no_model_even_when_one_is_printed() {
    // Model-looking text survives in the output of a strategy that was
    // abandoned. Attaching it to a `Proved` verdict would present a discarded
    // interpretation as a counterexample to a statement just proved.
    for word in ["Theorem", "Timeout"] {
        let output = format!("% SZS status {word} for girth\n{MODEL}");
        let read = parse("code/refute/girth.p", &output);
        assert_ne!(read.finding, Finding::Refuted);
        assert!(read.model.is_empty(), "`{word}` carries no counterexample");
    }
}

#[test]
fn a_problem_with_no_verdict_filed_finds_nothing() {
    let workspace = workspace_named("absent-verdict");
    assert!(verdict(&workspace, "code/refute/never-run.p").is_none());
}

#[test]
fn a_verdict_round_trips_through_the_record_a_later_reader_finds() {
    // The verdict is re-read long after the refuter's turn has ended, so what
    // matters is that the file on disk says what the tool did.
    let workspace = workspace_named("roundtrip");
    let output = format!("% SZS status CounterSatisfiable for girth\n{MODEL}");
    let read = parse("code/refute/girth.p", &output);
    let directory = workspace.join(VERDICT_DIR);
    std::fs::create_dir_all(&directory).expect("the verdict folder is created");
    std::fs::write(
        directory.join("code_refute_girth.p.json"),
        serde_json::to_string(&read.record()).expect("the record renders"),
    )
    .expect("the verdict is written");

    let found = verdict(&workspace, "code/refute/girth.p").expect("the verdict is found");
    assert_eq!(found.problem, read.problem);
    assert_eq!(found.finding, Finding::Refuted);
    assert_eq!(found.status, read.status);
    assert_eq!(found.model, read.model);

    // The `/workspace`-prefixed spelling names the same file, as it does
    // everywhere else a model supplies a path.
    let prefixed =
        verdict(&workspace, "/workspace/code/refute/girth.p").expect("the same verdict is found");
    assert_eq!(prefixed.finding, found.finding);
    assert_eq!(prefixed.model, found.model);
}

#[test]
fn every_finding_renders_its_own_guidance() {
    // Three of the four read as something other than what they are, so the
    // sentence that says what to do about one has to reach the model that asked.
    for finding in [
        Finding::Refuted,
        Finding::Proved,
        Finding::Contradictory,
        Finding::Undecided,
    ] {
        let rendered = Verdict {
            problem: "code/refute/girth.p".into(),
            finding,
            status: "Whatever".into(),
            model: String::new(),
        }
        .render();
        assert!(
            rendered.contains(finding.guidance()),
            "{finding:?} must carry its own guidance"
        );
        assert!(rendered.contains(finding.label()));
        assert!(
            !rendered.contains("The counterexample:"),
            "{finding:?} has no model here"
        );
    }
}

#[test]
fn only_a_refutation_shows_the_counterexample() {
    let rendered = Verdict {
        problem: "code/refute/girth.p".into(),
        finding: Finding::Refuted,
        status: "CounterSatisfiable".into(),
        model: "tff(finite_domain,axiom,$true).\n".into(),
    }
    .render();
    assert!(rendered.contains("The counterexample:"));
    assert!(rendered.contains("tff(finite_domain,axiom,$true)."));
}

#[tokio::test]
async fn traversal_and_absolute_paths_are_refused() {
    let workspace = workspace_named("traversal");
    let tool = FindCounterexample::new(workspace);
    for path in ["../escape.p", "/etc/passwd.p", ""] {
        assert!(
            tool.call(&(), call(path)).await.is_err(),
            "`{path}` must be refused"
        );
    }
}

#[tokio::test]
async fn a_file_that_is_not_a_tptp_problem_is_refused_before_anything_runs() {
    let workspace = workspace_named("extension");
    std::fs::write(workspace.join("notes.md"), "not tptp").expect("the file is written");
    let tool = FindCounterexample::new(workspace);
    assert!(
        tool.call(&(), call("notes.md")).await.is_err(),
        "only `.p` problems are searched"
    );
}

#[tokio::test]
async fn a_missing_problem_is_refused_with_its_own_reason() {
    // The distinction matters to the role reading the result: a problem that
    // does not exist is a file to write, where one the engine could not settle
    // is a search to widen. Collapsing them costs a turn.
    let workspace = workspace_named("missing");
    let tool = FindCounterexample::new(workspace);
    let refused = tool
        .call(&(), call("code/refute/absent.p"))
        .await
        .expect_err("a missing problem is refused");
    assert!(
        refused.to_string().contains("does not exist"),
        "the reason names the missing file, not a failed search: {refused}"
    );
}
