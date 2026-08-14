#![allow(clippy::expect_used)]

//! What following the entailment edges has to get right.
//!
//! The dangerous direction throughout is the permissive one. Every test that
//! asserts something is *not* established is guarding against a closure that
//! manufactures a proof out of a chain of assertions, which would be worse than
//! having no closure at all: the run would stop looking.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};

use super::*;

/// Writes one note carrying the given claim blocks.
fn library(root: &Path, blocks: &[&str]) {
    let directory = root.join("research/notes");
    std::fs::create_dir_all(&directory).expect("the notes directory is creatable");
    let mut text = String::from("# library\n");
    for block in blocks {
        let _ = write!(text, "\n```claim\n{block}\n```\n");
    }
    std::fs::write(directory.join("library.md"), text).expect("the note is writable");
}

fn workspace(name: &str) -> PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-closure-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the workspace is creatable");
    root
}

/// The result this file exists to produce.
///
/// Both supports are proved, so the consequence is proved, whatever word its
/// own block carries. A run that proves this again has spent an attempt on
/// something it already had.
#[test]
fn a_consequence_of_established_claims_is_established_for_free() {
    let root = workspace("upgrade");
    library(
        &root,
        &[
            "id: a\nstatement: the first bound\nstatus: proved\n",
            "id: b\nstatement: the second bound\nstatus: checked\n",
            "id: c\nstatement: the combined bound\nstatus: heuristic\nfollows-from: a, b\n",
        ],
    );

    let closure = collect(&root);
    let upgraded: Vec<&str> = closure
        .upgrades
        .iter()
        .map(|upgrade| upgrade.id.as_str())
        .collect();

    assert_eq!(
        upgraded,
        vec!["c"],
        "c follows from two established claims, so it is established"
    );
    assert!(
        closure.briefing().contains("Do not prove any of them again"),
        "and the next attempt is told so: {}",
        closure.briefing()
    );
}

/// The failure that would make this worse than nothing.
///
/// One support is a sentence somebody typed. A closure that propagated it would
/// report an establishment the run does not have.
#[test]
fn a_consequence_of_an_asserted_claim_is_not_established() {
    let root = workspace("asserted");
    library(
        &root,
        &[
            "id: a\nstatement: the proved part\nstatus: proved\n",
            "id: b\nstatement: somebody's guess\nstatus: asserted\n",
            "id: c\nstatement: the conclusion\nstatus: heuristic\nfollows-from: a, b\n",
        ],
    );

    assert!(
        collect(&root).upgrades.is_empty(),
        "one unestablished support is enough to block the upgrade"
    );
}

/// Establishment has to travel the whole chain, not one hop.
///
/// This is the transitive half, and it is where the thirty-sevenfold return in
/// the Equational Theories Project came from: almost none of what a library
/// knows is one edge away from what it says.
#[test]
fn establishment_travels_the_whole_chain() {
    let root = workspace("chain");
    library(
        &root,
        &[
            "id: a\nstatement: the base\nstatus: proved\n",
            "id: b\nstatement: the middle\nstatus: asserted\nfollows-from: a\n",
            "id: c\nstatement: the top\nstatus: asserted\nfollows-from: b\n",
        ],
    );

    let closure = collect(&root);
    let upgraded: Vec<&str> = closure
        .upgrades
        .iter()
        .map(|upgrade| upgrade.id.as_str())
        .collect();

    assert!(
        upgraded.contains(&"b"),
        "b follows directly from a proved claim, got {upgraded:?}"
    );
    assert!(
        closure.is_covered("c"),
        "and c is covered through b, which is what the transitive closure buys"
    );
}

/// The Dalmatian test: a proposal the library already entails is not a result.
#[test]
fn a_statement_the_library_entails_is_reported_as_redundant() {
    let root = workspace("redundant");
    library(
        &root,
        &[
            "id: a\nstatement: the strong bound\nstatus: proved\n",
            "id: weaker\nstatement: the weaker bound\nstatus: proved\nfollows-from: a\n",
        ],
    );

    let closure = collect(&root);

    assert!(closure.is_covered("weaker"), "it follows from a proved claim");
    assert!(
        !closure.is_covered("a"),
        "and the claim it follows from is not itself covered"
    );
    assert!(
        closure.render().contains("Already entailed"),
        "the section is rendered:\n{}",
        closure.render()
    );
}

/// The contradiction no single block states.
///
/// `c` rests on `a`, and `a` is recorded as contradicting `b`. Nothing says
/// `c` contradicts `b`, and the direct check the ledger already runs cannot
/// reach it.
#[test]
fn a_contradiction_reachable_only_through_the_edges_is_found() {
    let root = workspace("conflict");
    library(
        &root,
        &[
            "id: a\nstatement: the first\nstatus: proved\ncontradicts: b\n",
            "id: b\nstatement: the second\nstatus: proved\n",
            "id: c\nstatement: built on the first\nstatus: asserted\nfollows-from: a\n",
        ],
    );

    let closure = collect(&root);
    let (_, conflicts) = closure.counts();

    assert!(conflicts >= 1, "the conflict is found through the edge");
    assert!(
        closure.render().contains("Cannot all be true"),
        "and reported above everything else:\n{}",
        closure.render()
    );
}

/// A claim that supports itself establishes nothing.
///
/// The permissive reading here would be catastrophic: two claims each said to
/// follow from the other would upgrade each other to established out of
/// nothing at all.
#[test]
fn a_claim_supporting_itself_establishes_nothing() {
    let root = workspace("circular");
    library(
        &root,
        &[
            "id: a\nstatement: the first\nstatus: asserted\nfollows-from: b\n",
            "id: b\nstatement: the second\nstatus: asserted\nfollows-from: a\n",
        ],
    );

    let closure = collect(&root);
    let rendered = closure.render();

    assert!(
        closure.upgrades.is_empty(),
        "two claims resting on each other establish neither:\n{rendered}"
    );
    assert!(
        rendered.contains("Supporting themselves"),
        "and the cycle is reported:\n{rendered}"
    );
}

/// An edge naming nothing is a fault worth printing.
#[test]
fn an_edge_to_a_claim_that_does_not_exist_is_reported() {
    let root = workspace("dangling");
    library(
        &root,
        &["id: a\nstatement: the claim\nstatus: asserted\nfollows-from: never-written\n"],
    );

    let rendered = collect(&root).render();

    assert!(
        rendered.contains("`never-written`"),
        "the missing support is named:\n{rendered}"
    );
}

/// A library with no edges must not spend prompt saying so.
#[test]
fn a_library_with_no_edges_briefs_nothing() {
    let root = workspace("quiet");
    library(
        &root,
        &["id: a\nstatement: a lone claim\nstatus: proved\n"],
    );

    let closure = collect(&root);

    assert!(closure.briefing().is_empty(), "nothing derived, nothing said");
    assert!(
        closure.render().contains("Nothing to derive yet"),
        "and the file says what to write instead:\n{}",
        closure.render()
    );
}

/// A claim already established stays out of the upgrade list.
///
/// Otherwise the briefing would tell the next attempt not to prove things it
/// had already proved, which is true and useless, and would bury the entries
/// that matter.
#[test]
fn an_already_established_claim_is_not_offered_as_an_upgrade() {
    let root = workspace("settled");
    library(
        &root,
        &[
            "id: a\nstatement: the base\nstatus: proved\n",
            "id: b\nstatement: the consequence\nstatus: proved\nfollows-from: a\n",
        ],
    );

    assert!(
        collect(&root).upgrades.is_empty(),
        "b is already proved, so there is no upgrade to report"
    );
}
