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
        "reductions",
        "thesis",
    ] {
        assert!(slugs.contains(&expected), "`{expected}` is registered: {slugs:?}");
    }
    assert!(specs.iter().all(|spec| spec.builtin));
    // The one the prompts instruct roles to write to.
    let tasks = find(workspace.path(), "tasks").expect("the task ledger");
    assert_eq!(tasks.derived, "derived/TASKS.md");
    assert!(tasks.writable_by("goals"));
    assert!(
        !tasks.writable_by("judge"),
        "a role that scores an attempt does not file tasks"
    );
}

/// The reduction ledger can hold a chain link that is not yet a result.
///
/// The whole reason it exists. An identity established on the way to a target
/// earns no verdict anywhere else in this runtime, so a turn that produced one
/// filed nothing and the loop scored it as a pass with no progress.
#[test]
fn a_reduction_target_banks_a_link_that_is_not_yet_a_result() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = find(workspace.path(), "reductions").expect("the reduction ledger");

    assert_eq!(spec.derived, "derived/REDUCTIONS.md");
    let statuses: Vec<&str> = spec.statuses.iter().map(|s| s.name.as_str()).collect();
    assert!(
        statuses.contains(&"identity"),
        "a link with no consequence yet is recordable: {statuses:?}"
    );
    assert!(
        !spec
            .statuses
            .iter()
            .any(|status| status.name == "identity" && status.closed),
        "banking a link does not close the target it belongs to"
    );

    // Both bounds are separate fields: a run holding one of them is halfway,
    // and a single `gap` field could not say which half.
    let fields: Vec<&str> = spec.fields.iter().map(|f| f.name.as_str()).collect();
    for expected in ["parameter", "lower", "upper", "gap"] {
        assert!(fields.contains(&expected), "`{expected}` is a field: {fields:?}");
    }

    assert!(spec.writable_by("reducer"), "the reducer owns the target");
    assert!(
        spec.writable_by("lean_prover"),
        "the prover banks the links it establishes"
    );
    assert!(
        !spec.writable_by("inventor"),
        "a route recorded as a reduction target is a wish with a parameter in it"
    );
}

/// A thesis cannot be filed without stating what would refute it.
///
/// A belief with no stated way to lose survives every run that should have
/// killed it, which is the failure the ledger is against rather than a
/// tidiness rule.
#[test]
fn a_thesis_must_say_what_would_refute_it() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = find(workspace.path(), "thesis").expect("the thesis ledger");

    assert_eq!(spec.derived, "derived/THESIS.md");
    let required: Vec<&str> = spec
        .fields
        .iter()
        .filter(|field| field.required)
        .map(|field| field.name.as_str())
        .collect();
    assert!(
        required.contains(&"refuted-by"),
        "a thesis states its own refutation: {required:?}"
    );
    assert!(required.contains(&"because"), "and why it is believed: {required:?}");

    assert!(spec.writable_by("reflection"), "reflection revises it against a round");
    assert!(
        !spec.writable_by("research"),
        "a role that reads papers does not set what the run believes"
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
    document["derived"] = json!("derived/CLAIMS.md");
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
        owns_derived(workspace.path(), "derived/TASKS.md").map(|(slug, _)| slug),
        Some("tasks".to_string())
    );
    assert_eq!(
        owns_derived(workspace.path(), "derived/CLAIMS.md").map(|(slug, _)| slug),
        Some("claims".to_string())
    );
    assert!(
        owns_derived(workspace.path(), "GOAL.md").is_none(),
        "a file an agent writes is not owned by any ledger"
    );
    assert!(owns_derived(workspace.path(), "research/notes/a-note.md").is_none());
}

/// Every ledger's refusal names a route that actually works for that ledger.
///
/// This is the test the live run needed and did not have. The write guard
/// correctly refused the librarian's write to `teams/BOARD.md` and then told it
/// to use `record_entry` with `ledger: "board"` — which the board *also*
/// refuses, because it is rendered by its own module and is written with
/// `post_board`. The guard was tested for refusing; nothing tested that what it
/// recommended could be followed. A role that believed the message would have
/// spent two calls to arrive nowhere.
///
/// So: a queue or items ledger may say `record_entry`, and a runtime-rendered
/// one may not.
#[test]
fn a_refusal_never_points_at_a_tool_that_would_also_refuse() {
    use crate::orchestrator::ledger::spec::Source;

    let workspace = tempfile::tempdir().expect("a temporary workspace");
    define(workspace.path(), &folds()).expect("a run-defined ledger too");

    for spec in all(workspace.path()).0 {
        assert!(
            !spec.written_by.trim().is_empty(),
            "`{}` refuses a write without saying what to do instead",
            spec.slug
        );
        let names_record_entry = spec.written_by.contains("record_entry");
        match spec.source {
            // The engine writes these, so `record_entry` is the honest answer
            // and the message has to give it rather than leaving the caller to
            // guess which of six tools applies.
            Source::Queue { .. } | Source::Items { .. } => assert!(
                names_record_entry,
                "`{}` is engine-written but its refusal does not name `record_entry`: {}",
                spec.slug, spec.written_by
            ),
            // These are rendered in Rust from something else, and `record_entry`
            // on one is refused a second time. This is the assertion that would
            // have caught the board.
            Source::Derived => assert!(
                !names_record_entry,
                "`{}` is rendered by its own module, so `record_entry` on it is refused — its \
                 message must not send anybody there: {}",
                spec.slug, spec.written_by
            ),
        }
    }
}

/// The board in particular sends the caller to `post_board`.
///
/// Named rather than left to the loop above, because this is the exact path a
/// live run walked into and the one a regression would be cheapest to
/// reintroduce.
#[test]
fn the_board_refusal_names_post_board() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let (slug, written_by) = owns_derived(workspace.path(), "teams/BOARD.md")
        .expect("the board owns its rendered file");
    assert_eq!(slug, "board");
    assert!(
        written_by.contains("post_board"),
        "the board's refusal names the tool that actually writes it: {written_by}"
    );
    assert!(!written_by.contains("record_entry"), "{written_by}");
}
