//! Unit tests for the lemma index: what is read out of a Lean file, and what
//! the index refuses to claim about it.
//!
//! The parse is a header-level text parse and the tests are shaped by that. Its
//! one unacceptable failure is inventing a declaration — a role that reads a
//! signature here and cannot `exact?` against it has been sent somewhere that
//! does not exist — so the cases below lean on the conservative direction, and
//! several of them assert that something is *not* indexed.
#![allow(clippy::expect_used)]

use std::fmt::Write as _;
use std::path::Path;

use super::{Standing, collect, declarations};

/// A workspace of this test's own, with one Lean file in it.
fn workspace_with(name: &str, file: &str, body: &str) -> std::path::PathBuf {
    let root = std::env::temp_dir().join(format!("lemmas-test-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    let path = root.join(super::LEAN_DIR).join(file);
    std::fs::create_dir_all(path.parent().expect("the lean folder has a parent"))
        .expect("the test workspace is created");
    std::fs::write(&path, body).expect("the lean source is written");
    root
}

/// Files a verdict, as a `lean_check` would.
fn file_verdict(root: &Path, file: &str, axioms: &str) {
    let directory = root.join(super::super::lean::VERDICT_DIR);
    std::fs::create_dir_all(&directory).expect("the verdict folder is created");
    std::fs::write(
        directory.join(format!("{}.json", file.replace('/', "_"))),
        format!(
            r#"{{"file":"{file}","compiled":true,"sorries":[],"axioms":[{axioms}]}}"#
        ),
    )
    .expect("the verdict is written");
}

#[test]
fn a_theorem_is_read_with_its_namespace_and_its_statement() {
    let found = declarations(
        "namespace Riffle\n\
         theorem order_dvd (n s : ℕ) (h : 2 ≤ n) : shuffles n s = id ↔ (n - 1) ∣ 2 ^ s - 1 := by\n\
         \x20 simp\n\
         end Riffle\n",
    );
    assert_eq!(found.len(), 1);
    assert_eq!(found[0].name, "Riffle.order_dvd", "the namespace qualifies it");
    assert_eq!(found[0].kind, "theorem");
    assert!(
        found[0].signature.contains("(n - 1) ∣ 2 ^ s - 1"),
        "the statement is the point of the row: {}",
        found[0].signature
    );
    assert!(
        !found[0].signature.contains("simp"),
        "the proof is not: {}",
        found[0].signature
    );
}

/// The provenance line is the whole compression argument. A paragraph of prose
/// summarising where a result came from becomes one docstring, and it has to
/// survive into the index or the Lean library is only half a replacement.
#[test]
fn the_source_docstring_reaches_the_row() {
    let found = declarations(
        "/-- src: arXiv:2307.05997 §4 Cor 8 -/\n\
         @[simp] theorem bad_prime (p d : ℕ) : True := trivial\n",
    );
    assert_eq!(found.len(), 1);
    assert_eq!(found[0].source, "arXiv:2307.05997 §4 Cor 8");
    assert_eq!(found[0].name, "bad_prime", "the attribute is not part of the name");
}

/// A docstring belongs to the declaration it precedes, and to nothing further
/// down the file.
#[test]
fn a_source_line_does_not_leak_onto_the_next_declaration() {
    let found = declarations(
        "/-- src: Mordell 1967 -/\n\
         theorem first : True := trivial\n\
         \n\
         theorem second : True := trivial\n",
    );
    assert_eq!(found.len(), 2);
    assert_eq!(found[0].source, "Mordell 1967");
    assert_eq!(found[1].source, "", "the second theorem cites nothing");
}

/// Only at the start of a line. `def` inside prose, inside a docstring, or
/// indented under a `where` is not a declaration this index can send anyone to.
#[test]
fn a_keyword_that_is_not_a_declaration_is_not_indexed() {
    let found = declarations(
        "-- we def not want this\n\
         /-- The def of a shuffle. -/\n\
         theorem real : True := trivial\n\
         \x20 where def_helper : Nat := 0\n",
    );
    assert_eq!(
        found.iter().map(|d| d.name.as_str()).collect::<Vec<_>>(),
        vec!["real"],
        "only the declaration at column zero is indexed"
    );
}

/// Modifiers are ordinary Lean and must not hide a declaration from the index.
#[test]
fn modifiers_do_not_hide_a_declaration() {
    let found = declarations(
        "private theorem a : True := trivial\n\
         noncomputable def b : Nat := 0\n\
         protected lemma c : True := trivial\n\
         axiom d : True\n",
    );
    assert_eq!(
        found.iter().map(|d| d.name.as_str()).collect::<Vec<_>>(),
        vec!["a", "b", "c", "d"]
    );
    assert_eq!(found[3].kind, "axiom");
}

/// An `example` is anonymous, so a row for one would be a row nobody can act
/// on.
#[test]
fn an_example_is_not_indexed() {
    assert!(declarations("example : True := trivial\n").is_empty());
}

/// The standing comes off the verdict, and the three outcomes have to reach the
/// index distinctly — a conditional file read as verified would be the index
/// claiming a proof the kernel did not give.
#[test]
fn the_standing_is_read_off_the_filed_verdict() {
    for (name, axioms, expected) in [
        (
            "verified",
            r#""'t' depends on axioms: [propext]""#,
            Standing::Verified,
        ),
        (
            "conditional",
            r#""'t' depends on axioms: [Cited.mordell1967]""#,
            Standing::Conditional,
        ),
        ("failed", r#""'t' depends on axioms: [hole]""#, Standing::Failed),
    ] {
        let root = workspace_with(name, "Lib/T.lean", "theorem t : True := trivial\n");
        file_verdict(&root, "code/lean/Lib/T.lean", axioms);
        let lemmas = collect(&root);
        assert_eq!(lemmas.declarations.len(), 1);
        assert_eq!(lemmas.declarations[0].standing, expected, "for {name}");
        assert!(
            lemmas.unchecked_files.is_empty(),
            "a file with a verdict is not unchecked"
        );
    }
}

/// The state worth making visible: a `.lean` file nobody ran the kernel over
/// reads exactly like one that passed, and the replay of this repository's own
/// history found 54 of 78 files in it.
#[test]
fn a_file_with_no_verdict_is_unchecked_and_is_listed_as_such() {
    let root = workspace_with("never", "Lib/T.lean", "theorem t : True := trivial\n");
    let lemmas = collect(&root);
    assert_eq!(lemmas.declarations[0].standing, Standing::Unchecked);
    assert_eq!(lemmas.unchecked_files, vec!["code/lean/Lib/T.lean"]);
    assert_eq!(lemmas.checked(), 0, "unchecked is not checked");
    let rendered = lemmas.render();
    assert!(rendered.contains("## Never checked"), "{rendered}");
    assert!(rendered.contains("code/lean/Lib/T.lean"));
}

/// The bound is the ledger contract: cap the rows, and say what was left out.
/// A cut list reading as complete is worse than a long one.
#[test]
fn the_table_caps_its_rows_and_says_what_it_dropped() {
    let mut body = String::new();
    for index in 0..(super::MAX_ROWS + 25) {
        let _ = writeln!(body, "theorem t{index} : True := trivial");
    }
    let root = workspace_with("ceiling", "Lib/Many.lean", &body);
    let rendered = collect(&root).render();
    let rows = rendered.matches("| theorem |").count();
    assert_eq!(rows, super::MAX_ROWS, "the table is capped");
    assert!(
        rendered.contains("25 more"),
        "and says how many it left out: {rendered}"
    );
}

/// Past the bound, more declarations must not mean more file.
#[test]
fn past_the_bound_more_declarations_do_not_mean_more_file() {
    let render_with = |count: usize, name: &str| {
        let body = (0..count).fold(String::new(), |mut body, index| {
            let _ = writeln!(body, "theorem t{index} : True := trivial");
            body
        });
        collect(&workspace_with(name, "Lib/Many.lean", &body))
            .render()
            .len()
    };
    let smaller = render_with(super::MAX_ROWS + 10, "bound-a");
    let larger = render_with(super::MAX_ROWS + 400, "bound-b");
    // Not equal — the counts in the prose differ by a few characters — but the
    // difference must be a rounding error rather than 390 more rows.
    assert!(
        larger < smaller + 200,
        "{larger} against {smaller}: the table is not growing with the tree"
    );
}

/// Verified rows sort first, so when the bound bites it drops the rows a reader
/// can least act on.
#[test]
fn verified_declarations_are_rendered_before_unchecked_ones() {
    let root = workspace_with("order", "Lib/A.lean", "theorem checked_one : True := trivial\n");
    std::fs::write(
        root.join(super::LEAN_DIR).join("Lib/B.lean"),
        "theorem unchecked_one : True := trivial\n",
    )
    .expect("the second source is written");
    file_verdict(&root, "code/lean/Lib/A.lean", r#""'t' depends on axioms: [propext]""#);
    let rendered = collect(&root).render();
    let verified_at = rendered.find("checked_one").expect("the verified row is rendered");
    let unchecked_at = rendered
        .find("unchecked_one")
        .expect("the unchecked row is rendered");
    assert!(verified_at < unchecked_at, "verified sorts first");
}

/// A file written and never checked must reach the index on the *write*.
///
/// The other refresh runs on `lean_check`, and that is the wrong event to rely
/// on alone: a file nobody checks never fires it, so the unchecked files — the
/// whole reason the index carries a standing — were the ones least likely to
/// appear in it. A live PE 622 run reached seventeen `.lean` files against two
/// verdicts while the index still described the tree as it had been two checks
/// earlier.
#[test]
fn a_written_file_is_indexed_before_any_check() {
    let root = workspace_with("write-first", "Lib/A.lean", "theorem a : True := trivial\n");
    // A second file arriving after the first would have been invisible until
    // something checked it.
    std::fs::write(
        root.join(super::LEAN_DIR).join("Lib/B.lean"),
        "theorem b : True := trivial\n",
    )
    .expect("the second source is written");

    let lemmas = collect(&root);
    let names: Vec<&str> = lemmas
        .declarations
        .iter()
        .map(|declaration| declaration.name.as_str())
        .collect();
    assert!(names.contains(&"a") && names.contains(&"b"), "{names:?}");
    assert!(
        lemmas
            .declarations
            .iter()
            .all(|declaration| declaration.standing == Standing::Unchecked),
        "a file with no verdict is unchecked, not absent"
    );
    assert_eq!(lemmas.unchecked_files.len(), 2);
}

/// `X = X`: the one wrong statement a kernel check cannot object to.
///
/// The case is real. A live PE 622 run, told the answer was not accepted until
/// a `.lean` file with a passing verdict carried it, wrote
/// `theorem pe622_answer_nat : 3010983666182123972 = 3010983666182123972 := by
/// rfl` under a docstring calling it "the answer stated directly". Every check
/// in `lean.rs` would have passed it as `verified`.
mod tautologies {
    use super::super::tautologies;

    #[test]
    fn a_statement_whose_sides_are_identical_is_caught() {
        let found = tautologies(
            "theorem pe622_answer_nat : 3010983666182123972 = 3010983666182123972 := by rfl\n",
        );
        assert_eq!(found, vec!["pe622_answer_nat"]);
    }

    /// The check must be this narrow. `rfl` on a closed numeral is an ordinary
    /// and useful fact, and a check that refused it would make the runtime
    /// unable to state arithmetic at all.
    #[test]
    fn an_honest_rfl_still_passes() {
        for source in [
            "theorem two : 2 + 2 = 4 := by rfl\n",
            "theorem sig : sigma 1 15 = 24 := by decide\n",
            "theorem answer : 3010983666182119516 + 4456 = 3010983666182123972 := by norm_num\n",
        ] {
            assert!(tautologies(source).is_empty(), "refused: {source}");
        }
    }

    /// A `def` of a proposition is not an assertion of one.
    #[test]
    fn a_definition_is_not_a_claim() {
        assert!(tautologies("def trivially (n : Nat) : Prop := n = n\n").is_empty());
    }

    /// The relations that contain or neighbour `=` must not be mis-split — that
    /// is the only way this check could report a real theorem as empty.
    #[test]
    fn a_neighbouring_relation_is_not_mistaken_for_equality() {
        for source in [
            "theorem ne (n : Nat) : n ≠ n := by simp\n",
            "theorem le (n : Nat) : n ≤ n := le_refl n\n",
            "theorem ge (n : Nat) : n ≥ n := le_refl n\n",
        ] {
            assert!(tautologies(source).is_empty(), "mis-split: {source}");
        }
    }

    /// Binders carry their own `:`, so the proposition is taken after the last.
    #[test]
    fn a_binder_colon_does_not_confuse_the_split() {
        let found = tautologies("theorem t (n : Nat) (h : 0 < n) : n = n := rfl\n");
        assert_eq!(found, vec!["t"]);
    }

    /// The mill's commonest bad output, refused as a statement rather than as an
    /// accident.
    ///
    /// Ten statements milled from Conway-99's research summaries produced six of
    /// exactly this shape: a docstring describing a real theorem, and `True`
    /// underneath it. Without this they fail because the verdict finds no
    /// declaration to report, which tells a reader nothing about why.
    #[test]
    fn a_declaration_that_asserts_true_says_nothing_and_is_refused() {
        let source = "\
    import Mathlib

    namespace Cited

    /-- There exists a strongly regular graph with parameters (9,4,1,2). -/
    axiom srg9_4_1_2_exists : True

    end Cited
    ";
        assert_eq!(
            tautologies(source),
            vec!["Cited.srg9_4_1_2_exists".to_string()],
            "the name carries its namespace, as every other declaration here does"
        );
    }

    /// A theorem is judged the same way an axiom is.
    #[test]
    fn a_theorem_of_true_is_refused_too() {
        let source = "theorem nothing_at_all : True := trivial\n";
        assert_eq!(tautologies(source), vec!["nothing_at_all".to_string()]);
    }

    /// The check must not swallow a real axiom, which is the only way it could harm.
    #[test]
    fn an_axiom_that_states_something_is_left_alone() {
        let source = "\
    namespace Cited

    /-- Bagchi 2006, Theorem 4. -/
    axiom bagchi_mu1_k_bound : ∀ (k lam : ℕ), k ≥ (lam + 1) * (lam + 2)

    end Cited
    ";
        assert!(tautologies(source).is_empty());
    }

    /// A `def` whose body is `True` is a definition, not an assertion, and stays
    /// outside this check for the reason the identical-sides case does.
    #[test]
    fn a_definition_is_not_an_assertion() {
        let source = "def StronglyRegular (_v _k : \u{2115}) : Prop := True\n";
        assert!(tautologies(source).is_empty());
    }
}
