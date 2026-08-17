//! Unit tests for the kernel check: what counts as verified, and what the
//! recorded verdict is worth to a later reader.
//!
//! Every test here runs without Lean installed, which is deliberate. The
//! deterministic suite runs on a host with no Mathlib, so a parser exercised
//! only inside the container is one nothing checks — and the parse is where
//! the interesting mistakes are, not the process spawn.
#![allow(clippy::expect_used)]

use std::time::Duration;

use super::{LeanCheck, Outcome, VERDICT_DIR, Verdict, briefing_for, parse, verdict};
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
    let checked = parse("code/lemma.lean", "", true, CLEAN);
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
    let checked = parse("code/lemma.lean", "", true, &output);
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
        "code/lemma.lean", "",
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
        "code/lemma.lean", "",
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
        "code/lemma.lean", "",
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

/// A generated data module that states its own theorem does not pass.
///
/// The certificate boundary, enforced at the verdict rather than asked for in a
/// prompt. This is the failure that looks most like success: the file compiles,
/// carries no `sorry`, rests on Lean's three axioms, and the theorem the kernel
/// checked was chosen by the same generator that wrote the data it is about.
#[test]
fn a_generated_module_stating_its_own_theorem_does_not_pass() {
    let checked = parse(
        "code/lean/Lib/Certificate/Generated/Data499.lean",
        "def rows499 : List Nat := [5]\ntheorem rows499_ok : check rows499 = true := by decide\n",
        true,
        "'rows499_ok' depends on axioms: [propext, Classical.choice, Quot.sound]",
    );
    assert!(
        !checked.verified(),
        "the kernel accepted it, and it still may not carry a claim"
    );
    assert!(
        !checked.states_something(),
        "nor may it be kept as a partial statement to build on"
    );
    let objection = checked
        .objection()
        .expect("a conclusion in generated data is an objection");
    assert!(
        objection.contains("rows499_ok") && objection.contains("generated data"),
        "the objection names the declaration and what to do instead: {objection}"
    );
}

/// The same module holding only data is fine, and the checker beside it passes.
#[test]
fn generated_data_alone_is_not_an_objection() {
    let checked = parse(
        "code/lean/Lib/Certificate/Generated/Data499.lean",
        "def rows499 : List Nat := [5, 6]\n",
        true,
        "'rows499' does not depend on any axioms",
    );
    assert!(
        checked.generated_conclusions.is_empty(),
        "data is what a generated module is for"
    );
}

/// An unguarded denominator is reported and never refused.
///
/// Advisory on purpose: it cannot be made exact, and a wrong refusal on a
/// correct file would cost more than a note a reader can dismiss.
#[test]
fn an_uncleared_division_is_reported_without_failing_the_check() {
    let checked = parse(
        "code/lean/Lib/Mean.lean",
        "theorem mean_bound (m q : \u{211d}) : q / m \u{2264} 1 := by sorry\n",
        true,
        "'mean_bound' depends on axioms: [propext, Classical.choice, Quot.sound]",
    );
    assert_eq!(checked.uncleared, vec!["mean_bound".to_string()]);
    assert!(
        checked.objection().is_none_or(|objection| !objection.contains("denominator")),
        "the advisory never becomes the reason a verdict failed"
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
            "code/lemma.lean", "",
            true,
            &format!("'main' depends on axioms: {listed}"),
        );
        assert!(
            checked.unproved_axioms().is_empty(),
            "{listed} is Lean's own foundation, not an assumption"
        );
        assert!(checked.verified(), "{listed} should pass");
    }
}

#[test]
fn a_proof_that_never_printed_its_axioms_does_not_pass() {
    let checked = parse("code/lemma.lean", "", true, "");
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
        "code/lemma.lean", "",
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
    let checked = parse("code/lemma.lean", "", false, CLEAN);
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

/// The collector stamp survives the record, and a file edited after the check
/// is detected by comparing what the kernel was given against what is there now.
#[test]
fn a_collected_verdict_carries_its_provenance_and_notices_a_changed_file() {
    let workspace = workspace_named("collected");
    std::fs::create_dir_all(workspace.join("code")).expect("the code folder is created");
    let source = "theorem t : 2 + 2 = 4 := by norm_num\n";
    std::fs::write(workspace.join("code/lemma.lean"), source).expect("the source is written");

    let mut checked = parse("code/lemma.lean", source, true, CLEAN);
    assert!(!checked.is_collected(), "parsing text is not collecting it");
    checked.collected(&workspace, source, std::time::Duration::from_millis(1_234));
    assert!(checked.is_collected());

    let directory = workspace.join(VERDICT_DIR);
    std::fs::create_dir_all(&directory).expect("the verdict folder is created");
    std::fs::write(
        directory.join("code_lemma.lean.json"),
        serde_json::to_string(&checked.record()).expect("the record renders"),
    )
    .expect("the verdict is written");
    let found = verdict(&workspace, "code/lemma.lean").expect("the verdict is found");
    assert_eq!(found, checked, "the stamp survives the round trip");
    assert_eq!(
        found.record()["collector"]["elapsed_ms"],
        1_234,
        "the elapsed time is recorded, because a zero is the shape of a check nobody ran"
    );
    // Unchanged file: nothing to object to.
    assert_eq!(found.staleness(&workspace), None);

    // The statement is edited after the kernel saw it.
    std::fs::write(
        workspace.join("code/lemma.lean"),
        "theorem t : 2 + 2 = 5 := by sorry\n",
    )
    .expect("the source is rewritten");
    let objection = found
        .staleness(&workspace)
        .expect("a file edited after its check is stale");
    assert!(objection.contains("has changed since the kernel checked it"));
}

#[test]
fn a_verdict_round_trips_through_the_record_a_later_reader_finds() {
    // The ledger is re-derived long after the `lean_prover` run has ended, so
    // what matters is that the file on disk says the same thing the tool did.
    let workspace = workspace_named("roundtrip");
    let checked = parse("code/lemma.lean", "", true, CLEAN);
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
            "code/good.lean", "",
            true,
            "'two_le_four' does not depend on any axioms\n",
        );
        assert!(checked.compiled);
        assert!(checked.unproved_axioms().is_empty());
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
            "code/sorry.lean", "",
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
            "code/assumed.lean", "",
            true,
            "'main' depends on axioms: [key_estimate]\n",
        );
        assert!(checked.compiled && checked.sorries.is_empty());
        assert!(!checked.verified());
        assert_eq!(checked.unproved_axioms(), vec!["key_estimate".to_string()]);
    }

    /// `native_decide` does not print `Lean.ofReduceBool` on this toolchain; it
    /// prints a generated per-declaration axiom. Naming untrusted axioms by
    /// what is *not* on the trusted list, rather than by a denylist, is why the
    /// check still holds when the toolchain changes the name.
    #[test]
    fn native_decide_is_refused_under_the_name_this_toolchain_gives_it() {
        let checked = parse(
            "code/native.lean", "",
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

/// The live case this field exists for, verbatim.
///
/// `f-lower-bound-ceil-sqrt-n` passed on Lean's three axioms with no `sorry`,
/// and what the kernel had accepted was a fact about an arbitrary `f : ℕ → ℕ`
/// with the hard half taken as a hypothesis. Nothing in the verdict said so.
#[test]
fn the_signature_of_a_checked_theorem_is_recorded() {
    let source = r"import Mathlib.Analysis.Real.Sqrt

/-- The rounding step. -/
theorem f_lower_bound_ceil_sqrt_n
    (f : ℕ → ℕ)
    (hspectral : ∀ (n : ℕ), 1 ≤ n → Real.sqrt (n : ℝ) ≤ (f n : ℝ)) :
    ∀ (n : ℕ), 1 ≤ n → Nat.ceil (Real.sqrt (n : ℝ)) ≤ f n := by
  intro n hn
  exact (Nat.ceil_le).mpr (hspectral n hn)

#print axioms f_lower_bound_ceil_sqrt_n
";
    let checked = parse("code/lean/f.lean", source, true, CLEAN);

    let signature = checked
        .declarations
        .first()
        .expect("the theorem's signature is recorded");
    assert!(
        signature.contains("hspectral"),
        "the assumed hypothesis is what a reader has to see: {signature}"
    );
    assert!(
        signature.contains("f : ℕ → ℕ"),
        "so is the fact that f is arbitrary: {signature}"
    );
    assert!(
        !signature.contains("intro n hn"),
        "the proof is not the statement: {signature}"
    );
}

/// A `theorem` inside a docstring does not open a signature.
///
/// The parse is anchored at the line start for this reason: a comment that
/// discusses a theorem would otherwise swallow the rest of the file into one
/// unterminated signature.
#[test]
fn prose_about_a_theorem_is_not_read_as_one() {
    let source = "/-! We restate the theorem of Huang here. -/\nlemma small : 1 = 1 := rfl\n";

    let checked = parse("code/lean/f.lean", source, true, CLEAN);

    assert_eq!(checked.declarations, vec!["lemma small : 1 = 1".to_string()]);
}

/// A probe file declares nothing, and says nothing.
#[test]
fn a_check_probe_records_no_signature() {
    let source = "import Mathlib.Data.Real.Sqrt\n#check Nat.ceil_le\n#check Nat.ceil_of_int\n";

    let checked = parse("code/lean/ceil_test.lean", source, false, "error: unknown identifier");

    assert!(checked.declarations.is_empty());
    assert!(!checked.verified());
}

/// A commissioned file nobody checked is a fact worth reporting.
#[test]
fn a_source_with_no_verdict_says_so() {
    let workspace = workspace_named("no-verdict");

    let briefed = briefing_for(&workspace, "code/lean/assigned.lean");

    assert!(
        briefed.contains("no `lean_check` verdict"),
        "the caller has to learn the prover never checked what it was asked to: {briefed}"
    );
}

/// The `Cited` namespace, and what it is worth.
///
/// This is the seam that lets a research library be written in Lean at all. A
/// paper's theorem restated as a bare `axiom` is indistinguishable from a hole
/// somebody left, so the check refuses it — correctly, and at the cost of
/// making the honest thing unrecordable. The namespace separates the two, and
/// buys strictly less than it might look like: a conditional result is not a
/// verified one, and every test below says so.
mod cited {
    use super::{Outcome, parse};

    /// A result read from the literature, proved nowhere here.
    const CITED: &str =
        "'catalan' depends on axioms: [propext, Cited.mihailescu2004, Quot.sound]\n";

    #[test]
    fn a_proof_resting_only_on_cited_results_is_conditional() {
        let checked = parse("code/lean/Lib/Catalan.lean", "", true, CITED);
        assert_eq!(checked.outcome(), Outcome::Conditional);
        assert!(
            !checked.verified(),
            "conditional is not verified — the kernel checked the implication and not the \
             hypothesis, and rounding it up is exactly what this file exists to stop"
        );
        assert_eq!(checked.cited_axioms(), vec!["Cited.mihailescu2004"]);
        assert!(checked.unproved_axioms().is_empty());
    }

    /// The objection is what reaches the ledger, so it has to say which status
    /// the file *does* support rather than only which one it does not.
    #[test]
    fn the_objection_points_at_the_conditional_status() {
        let checked = parse("code/lean/Lib/Catalan.lean", "", true, CITED);
        let objection = checked
            .objection()
            .expect("a cited axiom still blocks `formalised`");
        assert!(objection.contains("Cited.mihailescu2004"), "{objection}");
        assert!(
            objection.contains("conditional"),
            "the role is told what it may file instead: {objection}"
        );
    }

    /// One attributed axiom does not launder the one beside it.
    #[test]
    fn an_unproved_axiom_beside_a_cited_one_still_fails() {
        let checked = parse(
            "code/lean/Lib/Catalan.lean", "",
            true,
            "'main' depends on axioms: [Cited.mihailescu2004, key_estimate]\n",
        );
        assert_eq!(checked.outcome(), Outcome::Failed);
        assert_eq!(checked.unproved_axioms(), vec!["key_estimate"]);
        assert!(
            checked
                .objection()
                .expect("an assumed axiom is an objection")
                .contains("key_estimate"),
            "the objection names the hole and not the citation"
        );
    }

    /// A citation says where a hypothesis came from. It says nothing about a
    /// gap in the proof, so it must not rescue a file that has one.
    #[test]
    fn a_cited_axiom_does_not_excuse_a_sorry() {
        let checked = parse(
            "code/lean/Lib/Catalan.lean", "",
            true,
            "code/lean/Lib/Catalan.lean:4:0: warning: declaration uses `sorry`\n\
             'main' depends on axioms: [Cited.mihailescu2004, sorryAx]\n",
        );
        assert_eq!(checked.outcome(), Outcome::Failed);
        assert_eq!(checked.sorries.len(), 1);
    }

    /// The trusted three alone are still the strongest result, and the
    /// namespace must not have moved that line.
    #[test]
    fn a_clean_proof_is_still_verified() {
        let checked = parse(
            "code/lean/Lib/Catalan.lean", "",
            true,
            "'main' depends on axioms: [propext, Classical.choice, Quot.sound]\n",
        );
        assert_eq!(checked.outcome(), Outcome::Verified);
        assert!(checked.cited_axioms().is_empty());
    }

    /// A name that merely mentions the namespace is not in it. Prefix-matched
    /// rather than searched for, so `NotCited.foo` and `myCited.bar` stay
    /// holes.
    #[test]
    fn the_namespace_is_a_prefix_and_not_a_substring() {
        let checked = parse(
            "code/lean/Lib/Catalan.lean", "",
            true,
            "'main' depends on axioms: [NotCited.sneaky]\n",
        );
        assert_eq!(checked.outcome(), Outcome::Failed);
        assert_eq!(checked.unproved_axioms(), vec!["NotCited.sneaky"]);
    }

    /// The record carries the outcome as a word, and keeps the boolean beside
    /// it: thirty-two verdicts already on disk have the old shape, and a reader
    /// that learned it should not start seeing nothing where it saw `false`.
    #[test]
    fn the_record_carries_both_the_outcome_and_the_boolean() {
        let record = parse("code/lean/Lib/Catalan.lean", "", true, CITED).record();
        assert_eq!(record["outcome"], "conditional");
        assert_eq!(record["verified"], false);
        assert_eq!(record["cited"][0], "Cited.mihailescu2004");
    }
}

/// A hallucinated import, which the first bench run found twice in nine files.
///
/// Lean reports it as a missing `.olean` object file — a message that reads
/// like a broken toolchain and is nothing of the kind. Both files it hit were
/// otherwise correct, so a verdict that only said "does not compile" sent the
/// role to debug its mathematics instead of its import line.
mod missing_modules {
    use super::parse;

    const MISSING: &str = "/workspace/code/a.lean:1:0: error: object file \
        '/opt/mathlib4/.lake/build/lib/lean/Mathlib/Data/Nat/Parity.olean' of module \
        Mathlib.Data.Nat.Parity does not exist\n";

    #[test]
    fn the_module_is_named_rather_than_the_object_file() {
        let checked = parse("code/a.lean", "", false, MISSING);
        assert!(!checked.compiled);
        assert_eq!(checked.missing_modules, vec!["Mathlib.Data.Nat.Parity"]);
        let objection = checked.objection().expect("it does not compile");
        assert!(objection.contains("Mathlib.Data.Nat.Parity"), "{objection}");
        assert!(
            objection.contains("/opt/mathlib4/Mathlib"),
            "the objection says how to find the real module: {objection}"
        );
    }

    /// Every other compile failure keeps the plain message, so the specific one
    /// stays a signal.
    #[test]
    fn an_ordinary_compile_failure_is_unchanged() {
        let checked = parse("code/a.lean", "", false, "code/a.lean:3:0: error: unsolved goals\n");
        assert!(checked.missing_modules.is_empty());
        assert_eq!(
            checked.objection(),
            Some("`code/a.lean` does not compile".to_string())
        );
    }

    /// The same module named on two lines is one problem, not two.
    #[test]
    fn a_repeated_module_is_listed_once() {
        let checked = parse("code/a.lean", "", false, &format!("{MISSING}{MISSING}"));
        assert_eq!(checked.missing_modules.len(), 1);
    }

    /// The record carries it, so a replay can count this failure mode without
    /// re-parsing Lean's prose.
    #[test]
    fn the_record_carries_the_missing_module() {
        let record = parse("code/a.lean", "", false, MISSING).record();
        assert_eq!(record["missing_modules"][0], "Mathlib.Data.Nat.Parity");
    }
}

/// A tautology fails the verdict, whatever else is right about the file.
///
/// It is checked before the axioms and before the `sorry` list because a file
/// containing one is typically flawless in every other respect — that is what
/// makes it dangerous. `X = X` compiles, needs no axiom, and would otherwise be
/// `verified`, the strongest status this runtime has.
#[test]
fn a_file_stating_a_tautology_cannot_back_a_claim() {
    let mut checked = parse("code/lean/Lib/Answer.lean", "", true, CLEAN);
    assert!(checked.verified(), "clean before the tautology is added");
    checked.tautologies = vec!["pe622_answer_nat".to_string()];
    assert_eq!(checked.outcome(), Outcome::Failed);
    let objection = checked
        .objection()
        .expect("a tautology is an objection");
    assert!(objection.contains("pe622_answer_nat"), "{objection}");
    assert!(
        objection.contains("identical"),
        "the objection says what is wrong with it: {objection}"
    );
    assert_eq!(checked.record()["tautologies"][0], "pe622_answer_nat");
}

/// The two failures that are about Mathlib's packaging rather than about
/// mathematics, and that between them accounted for most of the first bench
/// run's losses.
mod stale_mathlib {
    use super::CLEAN;
    use super::super::{parse, unresolvable_imports};

    /// The pre-flight must not fire where there is no Mathlib to check against.
    /// The deterministic suite runs on such a host, and a check that reported
    /// every import as missing would fail every file on it.
    #[test]
    fn no_search_path_means_no_opinion() {
        // Neither `LEAN_PATH` nor the image's file exists in the test
        // environment, so the pre-flight declines rather than guesses.
        assert!(
            unresolvable_imports("import Mathlib.Data.Nat.Basic\n").is_empty(),
            "a host with no Mathlib must not report an import as missing"
        );
    }

    /// The retired binder is read off the compiler's objection, never off the
    /// source alone: `for x in`, `open … in` and `let … in` are ordinary Lean.
    #[test]
    fn the_retired_binder_is_diagnosed_from_the_error() {
        let checked = parse(
            "code/a.lean",
            "theorem t (n : Nat) : (∑ i in Finset.range n, i) = 0 := by simp\n",
            false,
            "code/a.lean:1:32: error: unexpected token 'in'; expected ','\n",
        );
        assert!(checked.retired_binder);
        let objection = checked.objection().expect("it does not compile");
        assert!(objection.contains('∈'), "the fix is named: {objection}");
        assert!(objection.contains("retired"), "{objection}");
    }

    /// A file that compiles is not accused of anything, whatever it contains.
    #[test]
    fn a_compiling_file_is_not_accused() {
        // The statement says something on purpose. `True` would be refused as
        // vacuous by `lemmas::tautologies`, which is a different check from the
        // one under test here — this is about a comment containing `in` not
        // being mistaken for the retired big-operator binder.
        let checked = parse(
            "code/a.lean",
            "theorem t : 2 + 2 = 4 := by norm_num -- for x in xs\n",
            true,
            CLEAN,
        );
        assert!(!checked.retired_binder);
        assert!(checked.verified());
    }

    /// An unrelated syntax error keeps the plain message, so the specific one
    /// stays a signal rather than becoming the default advice.
    #[test]
    fn an_unrelated_syntax_error_is_not_blamed_on_the_binder() {
        let checked = parse(
            "code/a.lean",
            "theorem t : True := by trivial\n",
            false,
            "code/a.lean:1:0: error: unexpected token '<'; expected command\n",
        );
        assert!(!checked.retired_binder);
        assert_eq!(
            checked.objection(),
            Some("`code/a.lean` does not compile".to_string())
        );
    }

    /// The record carries it, so a replay can count this failure mode without
    /// re-reading Lean's prose.
    #[test]
    fn the_record_carries_the_binder_finding() {
        let record = parse(
            "code/a.lean",
            "theorem t (n : Nat) : (∑ i in Finset.range n, i) = 0 := by simp\n",
            false,
            "error: unexpected token 'in'; expected ','\n",
        )
        .record();
        assert_eq!(record["retired_binder"], true);
    }
}

/// A statement with a hole is kept apart from a statement that is empty.
///
/// The distinction the mill turns on. A live Casas-Alvero run produced a
/// faithful statement of the conjecture over `ℂ`, compiling, in Mathlib's own
/// vocabulary, whose only defect was a `sorry` nobody can currently remove —
/// and the mill deleted it because it was not `verified`. It is still not
/// verified and must never be filed as such; it is worth keeping.
#[cfg(test)]
mod states_something {
    use super::*;

    #[test]
    fn a_compiling_statement_with_a_sorry_states_something() {
        let checked = parse(
            "code/a.lean",
            "theorem t (n : Nat) : n + 0 = n := by sorry\n",
            true,
            "code/a.lean:1:8: warning: declaration uses `sorry`\n",
        );
        assert!(!checked.verified(), "a hole is still a hole");
        assert!(
            checked.states_something(),
            "but the statement is there and is worth keeping"
        );
    }

    #[test]
    fn a_file_that_does_not_compile_states_nothing() {
        let checked = parse(
            "code/a.lean",
            "theorem t : Nonsense := by rfl\n",
            false,
            "code/a.lean:1:12: error: unknown identifier 'Nonsense'\n",
        );
        assert!(!checked.states_something());
    }

    #[test]
    fn a_file_of_only_probes_states_nothing() {
        let checked = parse(
            "code/a.lean",
            "import Mathlib\n#check Polynomial.derivative\n",
            true,
            CLEAN,
        );
        assert!(
            !checked.states_something(),
            "a file with no declaration is a probe, not a statement"
        );
    }

    #[test]
    fn a_vacuous_statement_states_nothing() {
        let checked = parse("code/a.lean", "axiom t : True\n", true, CLEAN);
        assert!(
            !checked.states_something(),
            "`True` is refused here as it is everywhere else"
        );
    }
}
