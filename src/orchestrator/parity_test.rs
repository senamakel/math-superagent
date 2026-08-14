//! The parity gate: zero decision divergence between the two engines.
#![allow(clippy::expect_used)]

use super::*;
use crate::orchestrator::solutions::route;

/// The gate. Every state in the corpus must route identically on both engines.
///
/// A divergence is reported with the state that caused it and both answers,
/// because the useful question after a failure is which arm disagreed, not how
/// many did.
#[test]
fn both_engines_route_every_state_identically() {
    let mut divergences = Vec::new();
    let cases = corpus();
    for case in &cases {
        let rust = route_port(route(&case.state));
        let flow = workflow_route(&case.json);
        if rust != flow {
            divergences.push(format!("{}: rust={rust} workflow={flow}", case.describe()));
        }
    }
    assert!(
        divergences.is_empty(),
        "{} of {} states diverged:\n{}",
        divergences.len(),
        cases.len(),
        divergences
            .iter()
            .take(20)
            .cloned()
            .collect::<Vec<_>>()
            .join("\n")
    );
}

/// The corpus has to reach past every threshold, or agreement is agreement
/// about nothing. Asserts every arm of the ladder is actually exercised.
#[test]
fn the_corpus_exercises_every_arm() {
    let mut seen: Vec<&str> = corpus()
        .iter()
        .map(|case| route_port(route(&case.state)))
        .collect();
    seen.sort_unstable();
    seen.dedup();
    assert_eq!(
        seen,
        ["blocked", "diversify", "reported", "retry", "solved"],
        "the corpus never reaches some arm of the ladder"
    );
}

/// A guard on the guard: the comparison must be capable of failing. If the jq
/// ever resolved to null for every state, every assertion above would compare
/// `<null>` against itself only if the Rust also said `<null>` — it does not,
/// so this checks the workflow side produces real ports.
#[test]
fn the_workflow_side_produces_real_ports_rather_than_null() {
    for case in corpus().iter().take(64) {
        let port = workflow_route(&case.json);
        assert_ne!(port, "<null>", "{}", case.describe());
    }
}
