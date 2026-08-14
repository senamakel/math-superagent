// How a run reports when more than one school worked the problem.

use super::combined_outcome;

/// One school's outcome is passed through untouched.
///
/// The load-bearing case. `SolutionState::outcome` is written against specific
/// ways a run can end — an answer with one route behind it must not read as
/// solved, a provider failure must not read as a mathematical one — and a
/// single-school run must report exactly that wording, not a summary wrapped
/// around it.
#[test]
fn one_school_reports_exactly_what_it_reached() {
    let reached = vec![("chisel", "Solved: 4938827.\nVerified by a sieve.".to_string())];
    assert_eq!(combined_outcome(&reached), reached[0].1);
}

/// Every school is named and reported when several ran.
#[test]
fn several_schools_are_each_named() {
    let reached = vec![
        ("chisel", "Solved: 4938827.".to_string()),
        ("rising-sea", "Not solved within 8 attempts.".to_string()),
        ("adversarial", "Reported without a second route.".to_string()),
    ];
    let report = combined_outcome(&reached);
    for (slug, outcome) in &reached {
        assert!(
            report.contains(slug),
            "the report must name the {slug} school"
        );
        assert!(
            report.contains(outcome.trim_end_matches('.')),
            "the report must carry what {slug} reached"
        );
    }
}

/// A school whose loop failed is reported rather than quietly dropped.
///
/// A run that lost a school and did not say so reads as a run that chose to
/// pursue fewer approaches, which is the opposite of what happened.
#[test]
fn a_failed_school_still_appears() {
    let reached = vec![
        ("chisel", "Solved: 4938827.".to_string()),
        (
            "rising-sea",
            "the rising-sea loop failed: HTTP 403".to_string(),
        ),
    ];
    let report = combined_outcome(&reached);
    assert!(report.contains("rising-sea"));
    assert!(report.contains("403"));
}

/// No school having finished renders rather than panicking.
#[test]
fn an_empty_report_renders() {
    assert!(!combined_outcome(&[]).is_empty());
}

/// The schools a run works in are resolved once, and there is always one.
#[test]
fn a_run_always_has_a_school() {
    assert!(
        !super::schools::selected().is_empty(),
        "a run with no school has no roles registered and cannot attempt anything"
    );
}
