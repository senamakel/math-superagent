//! The parity gate: zero decision divergence between the two engines.
#![allow(clippy::expect_used)]

use super::*;
use crate::orchestrator::solutions::route;

/// The gate. Every state in every school's corpus must route identically on
/// both engines.
///
/// Run per school rather than once, because each school builds its own graph
/// from its own [`Thresholds`] and the jq in it is therefore a different
/// translation. A divergence is reported with the school and the state that
/// caused it and both answers, because the useful question after a failure is
/// whose ladder disagreed and where, not how many did.
#[test]
fn both_engines_route_every_state_identically() {
    let mut divergences = Vec::new();
    let mut swept = 0;
    for (slug, thresholds) in schools_under_test() {
        let cases = corpus(&thresholds);
        swept += cases.len();
        for case in &cases {
            let rust = route_port(route(&case.state, &thresholds));
            let flow = workflow_route(&case.json, &thresholds);
            if rust != flow {
                divergences.push(format!(
                    "{slug}: {}: rust={rust} workflow={flow}",
                    case.describe()
                ));
            }
        }
    }
    assert!(
        divergences.is_empty(),
        "{} of {swept} states diverged:\n{}",
        divergences.len(),
        divergences
            .iter()
            .take(20)
            .cloned()
            .collect::<Vec<_>>()
            .join("\n")
    );
}

/// The corpus has to reach past every threshold, or agreement is agreement
/// about nothing. Asserts every arm of the ladder is actually exercised, for
/// every school — a range derived from the wrong school's numbers would show up
/// here as an arm nothing reaches.
#[test]
fn the_corpus_exercises_every_arm() {
    for (slug, thresholds) in schools_under_test() {
        let mut seen: Vec<&str> = corpus(&thresholds)
            .iter()
            .map(|case| route_port(route(&case.state, &thresholds)))
            .collect();
        seen.sort_unstable();
        seen.dedup();
        assert_eq!(
            seen,
            ["blocked", "diversify", "reported", "retry", "solved"],
            "{slug}: the corpus never reaches some arm of the ladder"
        );
    }
}

/// A guard on the guard: the comparison must be capable of failing. If the jq
/// ever resolved to null for every state, every assertion above would compare
/// `<null>` against itself only if the Rust also said `<null>` — it does not,
/// so this checks the workflow side produces real ports.
#[test]
fn the_workflow_side_produces_real_ports_rather_than_null() {
    for (slug, thresholds) in schools_under_test() {
        for case in corpus(&thresholds).iter().take(64) {
            let port = workflow_route(&case.json, &thresholds);
            assert_ne!(port, "<null>", "{slug}: {}", case.describe());
        }
    }
}

/// The control school is today's runtime under a name, so its sweep must be the
/// one this file has always run: every threshold at two, the ceiling at eight,
/// and therefore ranges of `0..=3` and `0..=9`.
///
/// Asserted on the corpus's size rather than on the constants, because what
/// broke would be the derivation — a range that stopped one short would leave
/// every arm still reachable and every state still agreeing, and nothing else
/// here would notice.
#[test]
fn the_control_school_sweeps_exactly_the_corpus_it_always_did() {
    let chisel = Thresholds::chisel();
    assert_eq!(
        corpus(&chisel).len(),
        10 * 2 * 4 * 4 * 4 * 4,
        "the control school's sweep is no longer the one this gate was written on"
    );
}

/// A school with a longer leash must be swept further than the control's range
/// reaches, or the extra room it bought is exactly the part nothing tested.
#[test]
fn a_patient_school_is_swept_past_the_controls_range() {
    let chisel = Thresholds::chisel();
    let patient = Thresholds {
        stuck: chisel.stuck + 2,
        max_attempts: chisel.max_attempts + 4,
        ..chisel
    };
    let reached = |thresholds: &Thresholds| {
        corpus(thresholds).iter().fold((0, 0), |(a, u), case| {
            (a.max(case.state.attempts), u.max(case.state.unproductive))
        })
    };
    let (attempts, unproductive) = reached(&patient);
    let (control_attempts, control_unproductive) = reached(&chisel);
    assert!(
        attempts > control_attempts && attempts > patient.max_attempts,
        "the sweep stops short of the patient school's ceiling"
    );
    assert!(
        unproductive > control_unproductive && unproductive > patient.stuck,
        "the sweep stops short of the patient school's stuck threshold"
    );
}
