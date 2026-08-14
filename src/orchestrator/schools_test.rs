use super::{ALL, School, Thresholds, selected};

/// Every school has a distinct slug, since the slug is its address and its
/// workspace subtree.
#[test]
fn slugs_are_distinct() {
    let mut slugs: Vec<&str> = ALL.iter().map(|school| school.slug).collect();
    slugs.sort_unstable();
    let count = slugs.len();
    slugs.dedup();
    assert_eq!(count, slugs.len(), "two schools share a slug");
}

/// A slug is safe to use as a directory name and as a role suffix.
#[test]
fn slugs_are_safe_as_paths_and_role_suffixes() {
    for school in ALL {
        assert!(
            school
                .slug
                .chars()
                .all(|character| character.is_ascii_lowercase() || character == '-'),
            "slug `{}` must be lowercase ASCII and hyphens",
            school.slug
        );
        assert!(!school.slug.is_empty(), "a slug must not be empty");
        assert!(
            !school.stance.trim().is_empty(),
            "school `{}` must say what it is a bet on",
            school.slug
        );
    }
}

/// The control school is today's runtime, unchanged.
///
/// The empty policy is the load-bearing assertion: it is what makes `chisel`'s
/// assembled prompts byte-identical to the ones sent before schools existed, so
/// a new school is measurable against a control that did not move.
#[test]
fn the_control_school_is_unchanged() {
    let chisel = ALL[0];
    assert_eq!(chisel.slug, "chisel");
    assert!(
        chisel.policy.is_empty(),
        "the control school must add nothing to the shared method policy"
    );
    assert_eq!(
        chisel.thresholds,
        Thresholds::chisel(),
        "the control school must run on the runtime's own thresholds"
    );
}

/// Every school that is not the control actually differs from it.
///
/// A school whose prompt and thresholds both matched `chisel` would cost a full
/// share of the run's budget to reproduce the control's work.
#[test]
fn every_alternative_school_differs_from_the_control() {
    for school in ALL.iter().skip(1) {
        let differs =
            !school.policy.trim().is_empty() || school.thresholds != Thresholds::chisel();
        assert!(
            differs,
            "school `{}` is indistinguishable from the control",
            school.slug
        );
    }
}

/// The patient thresholds are a longer leash, never a shorter one.
#[test]
fn a_patient_school_is_never_given_less_room() {
    let control = Thresholds::chisel();
    for school in ALL {
        assert!(
            school.thresholds.stuck >= control.stuck,
            "school `{}` diversifies sooner than the control",
            school.slug
        );
        assert!(
            school.thresholds.max_attempts >= control.max_attempts,
            "school `{}` has fewer attempts than the control",
            school.slug
        );
        assert!(
            school.thresholds.blocked == control.blocked,
            "a provider failure is not a methodological question; school `{}` moved it",
            school.slug
        );
    }
}

/// A role name is qualified by the school that answers it.
#[test]
fn roles_are_qualified_by_school() {
    let school = ALL[1];
    assert_eq!(school.role("inventor"), format!("inventor@{}", school.slug));
}

/// Selection defaults to the control alone, so an existing run is unchanged.
#[test]
fn selection_defaults_to_the_control() {
    assert_eq!(parse_selection(None), vec!["chisel"]);
    assert_eq!(parse_selection(Some("")), vec!["chisel"]);
    assert_eq!(parse_selection(Some("   ")), vec!["chisel"]);
}

/// A wholly unrecognised selection keeps the default rather than emptying it.
///
/// The rule every override in this runtime follows: a malformed value never
/// silently removes the thing it configures.
#[test]
fn an_unrecognised_selection_keeps_the_default() {
    assert_eq!(parse_selection(Some("bourbaki")), vec!["chisel"]);
    assert_eq!(parse_selection(Some(",,,")), vec!["chisel"]);
}

/// Recognised names are kept in the order written, unknown ones dropped.
#[test]
fn selection_keeps_order_and_drops_the_unknown() {
    assert_eq!(
        parse_selection(Some("rising-sea,bourbaki,chisel")),
        vec!["rising-sea", "chisel"]
    );
}

/// A school named twice runs once.
#[test]
fn selection_collapses_duplicates() {
    assert_eq!(
        parse_selection(Some("chisel,chisel,adversarial")),
        vec!["chisel", "adversarial"]
    );
}

/// All three run when all three are asked for.
#[test]
fn every_school_can_be_selected() {
    assert_eq!(
        parse_selection(Some("chisel,rising-sea,adversarial")),
        vec!["chisel", "rising-sea", "adversarial"]
    );
}

/// `selected` reads the environment, which a test must not mutate globally.
///
/// The parsing is what has the behaviour worth testing, so it is exercised
/// through this pure mirror of [`selected`]'s body and [`selected`] itself is
/// checked only for its default. Sharing the loop rather than restating it
/// would be better still; it is not shared because doing so would put a
/// test-only parameter on a production signature.
fn parse_selection(raw: Option<&str>) -> Vec<&'static str> {
    let Some(raw) = raw else {
        return vec!["chisel"];
    };
    let mut chosen: Vec<School> = Vec::new();
    for name in raw.split(',') {
        let name = name.trim();
        if name.is_empty() || chosen.iter().any(|school| school.slug == name) {
            continue;
        }
        if let Some(school) = ALL.iter().find(|school| school.slug == name) {
            chosen.push(*school);
        }
    }
    if chosen.is_empty() {
        return vec!["chisel"];
    }
    chosen.into_iter().map(|school| school.slug).collect()
}

/// The environment default, checked once and without mutating the environment.
#[test]
fn selected_returns_at_least_one_school() {
    assert!(
        !selected().is_empty(),
        "a run must always have a school to work in"
    );
}
