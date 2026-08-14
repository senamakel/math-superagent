use super::*;

fn workspace(name: &str) -> std::path::PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-screen-env-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the fixture workspace must be creatable");
    root
}

/// Writes a workspace holding a statement and a valid compiled policy.
fn seeded(name: &str, policy: &str) -> (std::path::PathBuf, std::path::PathBuf) {
    let root = workspace(name);
    std::fs::write(root.join("problem.md"), "# A de-named statement\n")
        .expect("the statement must be writable");
    let policy_path = root.join("screen.json");
    std::fs::write(&policy_path, policy).expect("the policy must be writable");
    (root, policy_path)
}

const VALID: &str =
    r#"{"slug":"a-problem","salt":"0123456789abcdef0","max_ngram":4,"block":["aa"]}"#;

#[test]
fn a_valid_policy_arms_the_screen_and_reads_the_statement() {
    let (root, policy_path) = seeded("valid", VALID);
    let screen = Screen::load(&policy_path, &root, None).expect("a valid policy must load");
    assert_eq!(screen.slug(), "a-problem");
    assert!(
        screen.problem.contains("de-named statement"),
        "the adjudicator is asked about the statement, so it must be loaded"
    );
}

#[test]
fn a_named_but_missing_policy_stops_the_run() {
    // Degrading to "no screening" here is the one outcome that must not happen:
    // it produces a calibration run that looks normal, spends hours of provider
    // credit, and measures nothing, with no visible symptom.
    let root = workspace("missing");
    let outcome = Screen::load(
        std::path::Path::new("/nonexistent/screen.json"),
        &root,
        None,
    );
    assert!(
        outcome.is_err(),
        "a named policy that cannot be read must fail the run, not disable the screen"
    );
}

#[test]
fn a_missing_statement_does_not_stop_the_run() {
    // The statement only feeds the adjudicator, which is the supplement rather
    // than the control. Losing it must not take the deterministic stage down
    // with it.
    let root = workspace("no-statement");
    let policy_path = root.join("screen.json");
    std::fs::write(&policy_path, VALID).expect("the policy must be writable");
    let screen = Screen::load(&policy_path, &root, None).expect("a valid policy must load");
    assert!(screen.problem.is_empty());
}

#[test]
fn the_adjudicator_is_disarmed_when_the_policy_disables_it() {
    let (root, policy_path) = seeded(
        "disabled",
        r#"{"slug":"p","salt":"0123456789abcdef0","max_ngram":4,"block":["aa"],
            "adjudicator":{"enabled":false}}"#,
    );
    let screen = Screen::load(&policy_path, &root, None).expect("a valid policy must load");
    assert!(screen.model.is_none());
}

#[test]
fn wrapping_without_a_screen_changes_nothing() {
    assert!(wrap_all(None, Vec::new()).is_empty());
}

#[test]
fn a_debug_line_names_the_problem_but_never_a_term() {
    // `Debug` output reaches logs the run can read.
    let (root, policy_path) = seeded("debug", VALID);
    let screen = Screen::load(&policy_path, &root, None).expect("a valid policy must load");
    let rendered = format!("{screen:?}");
    assert!(rendered.contains("a-problem"));
    assert!(!rendered.contains("0123456789abcdef0"), "{rendered}");
}
