//! Unit tests for the ledger registry: the built-in set, and the rules a
//! run-defined ledger has to satisfy to join it.
#![allow(clippy::expect_used)]

use serde_json::{Value, json};

use super::{MAX_DEFINED, SPEC_DIR, all, define, find, owns_derived, retire};

fn folds() -> Value {
    json!({
        "slug": "folds",
        "title": "Folds",
        "purpose": "What the run knows about one subject, gathered across batches.",
        "source": "items",
        "dir": "research/folds",
        "block": "fold",
        "derived": "research/FOLDS.md",
        "fields": [
            { "name": "id", "role": "id" },
            { "name": "subject", "role": "title" },
            { "name": "status", "role": "status" }
        ],
        "statuses": [{ "name": "open" }, { "name": "sealed", "closed": true }],
        "sections": [{ "heading": "Open", "statuses": ["open"] }]
    })
}

/// Every built-in parses, and the ones that matter are there under the names
/// the prompts use.
#[test]
fn the_builtin_set_is_available_in_a_bare_workspace() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let (specs, faults) = all(workspace.path());
    assert!(faults.is_empty(), "no built-in is malformed: {faults:?}");

    let slugs: Vec<&str> = specs.iter().map(|spec| spec.slug.as_str()).collect();
    for expected in [
        "tasks",
        "goals",
        "board",
        "claims",
        "threads",
        "approaches",
        "weakened",
        "blueprint",
        "entailment",
        "frontier",
        "requests",
    ] {
        assert!(slugs.contains(&expected), "`{expected}` is registered: {slugs:?}");
    }
    assert!(specs.iter().all(|spec| spec.builtin));
    // The one the prompts instruct roles to write to.
    let tasks = find(workspace.path(), "tasks").expect("the task ledger");
    assert_eq!(tasks.derived, "TASKS.md");
    assert!(tasks.writable_by("goals"));
    assert!(
        !tasks.writable_by("judge"),
        "a role that scores an attempt does not file tasks"
    );
}

/// A run-defined ledger joins the registry and is readable straight away.
///
/// The `research/folds/` case from `docs/ledgers.md`, which a live run built by
/// hand because no such ledger existed. This is that, without a release.
#[test]
fn a_run_can_define_a_ledger() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = define(workspace.path(), &folds()).expect("the declaration is accepted");
    assert!(!spec.builtin);
    assert!(
        workspace.path().join(SPEC_DIR).join("folds.json").exists(),
        "the declaration is on disk, so it survives a restart"
    );
    let found = find(workspace.path(), "folds").expect("it is in the registry");
    assert_eq!(found.derived, "research/FOLDS.md");
}

/// A run may not redefine a built-in slug.
///
/// Every prompt that names `tasks` is written against what `tasks` holds. A run
/// that could rebind the name would make all of them wrong at once, silently.
#[test]
fn a_builtin_slug_cannot_be_shadowed() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let mut document = folds();
    document["slug"] = json!("tasks");
    let error = define(workspace.path(), &document).expect_err("shadowing is refused");
    assert!(error.to_string().contains("already a ledger"), "{error}");
}

/// Two ledgers may not write the same derived file.
#[test]
fn two_ledgers_cannot_own_one_derived_file() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let mut document = folds();
    document["derived"] = json!("research/CLAIMS.md");
    let error = define(workspace.path(), &document).expect_err("the collision is refused");
    assert!(error.to_string().contains("claims"), "{error}");
}

/// A run-defined ledger must have a source the engine can actually read.
#[test]
fn a_run_defined_ledger_cannot_claim_to_be_rendered_in_rust() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let mut document = folds();
    document["source"] = json!("derived");
    let error = define(workspace.path(), &document).expect_err("refused");
    assert!(error.to_string().contains("queue"), "{error}");
}

/// Past the cap, further declarations are refused with a reason.
#[test]
fn the_number_of_defined_ledgers_is_capped() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    for index in 0..MAX_DEFINED {
        let mut document = folds();
        document["slug"] = json!(format!("fold-{index}"));
        document["derived"] = json!(format!("research/FOLD{index}.md"));
        document["dir"] = json!(format!("research/fold{index}"));
        define(workspace.path(), &document).expect("within the cap");
    }
    let error = define(workspace.path(), &folds()).expect_err("past the cap");
    assert!(error.to_string().contains("cap"), "{error}");
    assert!(
        error.to_string().contains("retire_ledger"),
        "the message says what to do about it: {error}"
    );
}

/// Retiring a declaration leaves the entries alone.
///
/// A ledger nobody reads is worth retiring. The work recorded in it is not, and
/// deleting a queue to tidy a registry is the loss this whole design exists to
/// prevent.
#[test]
fn retiring_a_ledger_keeps_its_entries() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    define(workspace.path(), &folds()).expect("defined");
    let entries = workspace.path().join("research/folds");
    std::fs::create_dir_all(&entries).expect("the directory");
    std::fs::write(entries.join("passes.md"), "```fold\nid: passes\n```\n").expect("an entry");

    let left = retire(workspace.path(), "folds").expect("retired");
    assert_eq!(left, "research/folds");
    assert!(find(workspace.path(), "folds").is_none());
    assert!(
        entries.join("passes.md").exists(),
        "the entries survive the retirement"
    );
}

/// A built-in cannot be retired.
#[test]
fn a_builtin_cannot_be_retired() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let error = retire(workspace.path(), "tasks").expect_err("refused");
    assert!(error.to_string().contains("built in"), "{error}");
    assert!(retire(workspace.path(), "nothing-of-that-name").is_err());
}

/// A malformed declaration costs that ledger and nothing else.
///
/// A run that wrote one bad spec must still reach its tasks. Failing the whole
/// registry would turn a typo into a dead run.
#[test]
fn a_malformed_declaration_does_not_cost_the_registry() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    define(workspace.path(), &folds()).expect("a good one");
    std::fs::write(
        workspace.path().join(SPEC_DIR).join("broken.json"),
        "{ not json at all",
    )
    .expect("a bad one");

    let (specs, faults) = all(workspace.path());
    assert!(
        specs.iter().any(|spec| spec.slug == "folds"),
        "the good ledger is still there"
    );
    assert!(specs.iter().any(|spec| spec.slug == "tasks"));
    assert!(
        faults.iter().any(|fault| fault.contains("broken.json")),
        "and the bad one is reported by name: {faults:?}"
    );
}

/// Every derived path is owned, which is what the write guard consults.
#[test]
fn derived_paths_are_owned_and_reported() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    assert_eq!(
        owns_derived(workspace.path(), "TASKS.md").as_deref(),
        Some("tasks")
    );
    assert_eq!(
        owns_derived(workspace.path(), "research/CLAIMS.md").as_deref(),
        Some("claims")
    );
    assert!(
        owns_derived(workspace.path(), "GOAL.md").is_none(),
        "a file an agent writes is not owned by any ledger"
    );
    assert!(owns_derived(workspace.path(), "research/notes/a-note.md").is_none());
}
