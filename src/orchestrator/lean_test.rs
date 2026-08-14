//! Unit tests for the kernel check: what counts as verified, and what the
//! recorded verdict is worth to a later reader.
//!
//! Every test here runs without Lean installed, which is deliberate. The
//! deterministic suite runs on a host with no Mathlib, so a parser exercised
//! only inside the container is one nothing checks — and the parse is where
//! the interesting mistakes are, not the process spawn.
#![allow(clippy::expect_used)]

use std::time::Duration;

use super::{LeanCheck, VERDICT_DIR, Verdict, parse, verdict};
use crate::agent::{Tool, ToolCall};

/// A workspace of this test's own, so one test's verdicts are not another's.
fn workspace_named(name: &str) -> std::path::PathBuf {
    let path = std::env::temp_dir().join(format!("lean-test-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).expect("the test workspace is created");
    path
}

/// The output a clean Mathlib proof produces.
const CLEAN: &str = "'my_lemma' depends on axioms: [propext, Classical.choice, Quot.sound]";

fn call(file: &str) -> ToolCall {
    ToolCall {
        id: "1".into(),
        name: "lean_check".into(),
        invalid: None,
        arguments: serde_json::json!({ "file": file }),
    }
}

#[test]
fn a_clean_proof_with_its_axioms_printed_is_verified() {
    let checked = parse("code/lemma.lean", true, CLEAN);
    assert!(checked.compiled);
    assert!(checked.verified());
    assert_eq!(checked.objection(), None);
    assert_eq!(checked.axioms.len(), 1);
}

#[test]
fn a_sorry_is_caught_even_though_lean_exits_cleanly() {
    // The failure this whole file exists for. `lean` warns and returns zero, so
    // a check reading the exit status alone calls this a proof.
    let output = format!("lemma.lean:4:8: warning: declaration uses 'sorry'\n{CLEAN}");
    let checked = parse("code/lemma.lean", true, &output);
    assert!(checked.compiled, "it did compile; that is the trap");
    assert!(!checked.verified());
    assert!(
        checked
            .objection()
            .expect("a sorry is an objection")
            .contains("`sorry` still in it")
    );
}

#[test]
fn sorry_ax_in_the_axioms_is_caught_when_no_warning_names_it() {
    // A declaration proved elsewhere in the file can carry `sorryAx` through
    // without this file emitting a `sorry` warning of its own, so the axioms
    // are parsed rather than inferred from the warning list.
    let checked = parse(
        "code/lemma.lean",
        true,
        "'my_lemma' depends on axioms: [propext, sorryAx]",
    );
    assert!(checked.sorries.is_empty(), "nothing warned");
    assert!(!checked.verified());
    assert!(
        checked
            .objection()
            .expect("sorryAx is an objection")
            .contains("sorryAx")
    );
}

/// The hole `lean4checker` is usually reached for, closed from output already
/// on hand.
///
/// One `axiom` line is all it takes: the file compiles, warns nothing, prints
/// its axioms exactly as asked, and proves the theorem *given* something nobody
/// established. Every other check here passes it.
#[test]
fn a_proof_resting_on_an_assumed_axiom_does_not_pass() {
    let checked = parse(
        "code/lemma.lean",
        true,
        "'main' depends on axioms: [propext, key_estimate, Quot.sound]",
    );
    assert!(checked.compiled, "it does compile — that is the problem");
    assert!(checked.sorries.is_empty(), "and nothing warned");
    assert!(!checked.verified(), "but it is not a proof");
    let objection = checked.objection().expect("an assumed axiom is an objection");
    assert!(
        objection.contains("key_estimate"),
        "the objection names the axiom, so the role knows what to prove: {objection}"
    );
}

/// `native_decide` trusts the compiler rather than the kernel, and the whole
/// argument for filing a Lean result as the strongest row available is that the
/// kernel checked it.
#[test]
fn a_proof_closed_by_native_decide_does_not_pass() {
    let checked = parse(
        "code/lemma.lean",
        true,
        "'main' depends on axioms: [propext, Lean.ofReduceBool]",
    );
    assert!(!checked.verified());
    assert!(
        checked
            .objection()
            .expect("ofReduceBool is an objection")
            .contains("Lean.ofReduceBool")
    );
}

/// The trusted three, in any order and any subset, are what a Mathlib proof
/// actually rests on — so none of them may be read as untrusted.
#[test]
fn lean_s_own_axioms_are_not_treated_as_assumptions() {
    for listed in [
        "[propext]",
        "[Quot.sound, propext]",
        "[propext, Classical.choice, Quot.sound]",
    ] {
        let checked = parse(
            "code/lemma.lean",
            true,
            &format!("'main' depends on axioms: {listed}"),
        );
        assert!(
            checked.untrusted_axioms().is_empty(),
            "{listed} is Lean's own foundation, not an assumption"
        );
        assert!(checked.verified(), "{listed} should pass");
    }
}

#[test]
fn a_proof_that_never_printed_its_axioms_does_not_pass() {
    let checked = parse("code/lemma.lean", true, "");
    assert!(checked.compiled);
    assert!(!checked.verified(), "silence about axioms is not a clean bill");
    assert!(
        checked
            .objection()
            .expect("unstated axioms are an objection")
            .contains("#print axioms")
    );
}

#[test]
fn an_error_fails_the_check_even_when_the_exit_status_is_zero() {
    let checked = parse(
        "code/lemma.lean",
        true,
        "lemma.lean:2:0: error: unknown identifier 'foo'",
    );
    assert!(!checked.compiled);
    assert!(
        checked
            .objection()
            .expect("a broken file is an objection")
            .contains("does not compile")
    );
}

#[test]
fn a_nonzero_exit_fails_the_check_even_with_axioms_printed() {
    let checked = parse("code/lemma.lean", false, CLEAN);
    assert!(!checked.compiled);
    assert!(!checked.verified());
}

#[tokio::test]
async fn traversal_and_absolute_paths_are_refused() {
    let workspace = workspace_named("traversal");
    let tool = LeanCheck::new(workspace, Duration::from_secs(5));
    for path in ["../escape.lean", "/etc/passwd.lean", ""] {
        assert!(
            tool.call(&(), call(path)).await.is_err(),
            "`{path}` must be refused"
        );
    }
}

#[tokio::test]
async fn a_file_that_is_not_lean_is_refused_before_anything_runs() {
    let workspace = workspace_named("extension");
    std::fs::write(workspace.join("notes.md"), "not lean").expect("the file is written");
    let tool = LeanCheck::new(workspace, Duration::from_secs(5));
    let refused = tool.call(&(), call("notes.md")).await;
    assert!(refused.is_err(), "only .lean sources are checked");
}

#[tokio::test]
async fn a_missing_file_is_refused_rather_than_reported_as_not_compiling() {
    // The distinction matters to the role reading the result: a file that does
    // not compile is a proof to fix, and one that is not there is a file to
    // write. Collapsing them costs a turn.
    let workspace = workspace_named("missing");
    let tool = LeanCheck::new(workspace, Duration::from_secs(5));
    assert!(tool.call(&(), call("code/absent.lean")).await.is_err());
}

#[test]
fn a_verdict_round_trips_through_the_record_a_later_reader_finds() {
    // The ledger is re-derived long after the `lean_prover` run has ended, so
    // what matters is that the file on disk says the same thing the tool did.
    let workspace = workspace_named("roundtrip");
    let checked = parse("code/lemma.lean", true, CLEAN);
    let directory = workspace.join(VERDICT_DIR);
    std::fs::create_dir_all(&directory).expect("the verdict folder is created");
    std::fs::write(
        directory.join("code_lemma.lean.json"),
        serde_json::to_string(&checked.record()).expect("the record renders"),
    )
    .expect("the verdict is written");

    let found = verdict(&workspace, "code/lemma.lean").expect("the verdict is found");
    assert_eq!(found, checked);
    assert!(found.verified());
    // The `/workspace`-prefixed spelling names the same file, as it does
    // everywhere else a model supplies a path.
    assert_eq!(verdict(&workspace, "/workspace/code/lemma.lean"), Some(found));
}

#[test]
fn a_claim_naming_a_file_with_no_verdict_finds_nothing() {
    let workspace = workspace_named("absent-verdict");
    assert_eq!(verdict(&workspace, "code/never-checked.lean"), None);
}

#[test]
fn a_default_verdict_is_not_verified() {
    // The `Default` is what a malformed record degrades toward, so it must not
    // be the shape that passes.
    assert!(!Verdict::default().verified());
}

/// Every string below is verbatim container output, from `lean` 4 with the
/// image's Mathlib, run over four files written to exercise exactly these four
/// outcomes. The parser had only ever been tested against text this file
/// authored, and two of the four disagreed with the real thing.
mod what_lean_actually_prints {
    use super::parse;

    /// The clean case, and the one the earlier parser rejected: Lean says a
    /// proof needs no axioms in words that contain neither `axioms:` nor a
    /// list, so the check read the strictest possible result as *nothing was
    /// reported* and refused it.
    #[test]
    fn a_proof_that_needs_no_axiom_at_all_passes() {
        let checked = parse(
            "code/good.lean",
            true,
            "'two_le_four' does not depend on any axioms\n",
        );
        assert!(checked.compiled);
        assert!(checked.untrusted_axioms().is_empty());
        assert!(
            checked.verified(),
            "an axiom-free kernel-checked proof is the best result available: {:?}",
            checked.objection()
        );
    }

    /// Lean writes the warning with backticks. The straight-quoted form this
    /// parser looked for never appears, so no `sorry` was ever recorded.
    #[test]
    fn a_sorry_warning_is_recorded_in_the_form_lean_emits_it() {
        let checked = parse(
            "code/sorry.lean",
            true,
            "/workspace/Sorry.lean:1:8: warning: declaration uses `sorry`\n\
             'hard' depends on axioms: [sorryAx]\n",
        );
        assert_eq!(checked.sorries.len(), 1, "the warning is the primary signal");
        assert!(!checked.verified());
        assert!(
            checked
                .objection()
                .expect("a sorry is an objection")
                .contains("`sorry`"),
            "the objection should name the sorry, not only the axiom behind it"
        );
    }

    /// The file this control was written for: it compiles, warns nothing, and
    /// proves the theorem from an axiom the run declared itself.
    #[test]
    fn a_self_declared_axiom_is_caught_in_lean_s_own_wording() {
        let checked = parse(
            "code/assumed.lean",
            true,
            "'main' depends on axioms: [key_estimate]\n",
        );
        assert!(checked.compiled && checked.sorries.is_empty());
        assert!(!checked.verified());
        assert_eq!(checked.untrusted_axioms(), vec!["key_estimate".to_string()]);
    }

    /// `native_decide` does not print `Lean.ofReduceBool` on this toolchain; it
    /// prints a generated per-declaration axiom. Naming untrusted axioms by
    /// what is *not* on the trusted list, rather than by a denylist, is why the
    /// check still holds when the toolchain changes the name.
    #[test]
    fn native_decide_is_refused_under_the_name_this_toolchain_gives_it() {
        let checked = parse(
            "code/native.lean",
            true,
            "'big' depends on axioms: [big._native.native_decide.ax_1_1]\n",
        );
        assert!(!checked.verified());
        assert!(
            checked
                .objection()
                .expect("a native_decide axiom is an objection")
                .contains("native_decide"),
            "the objection names the generated axiom, so the role can see where it came from"
        );
    }
}
