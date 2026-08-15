//! Unit tests for reading a ledger declaration.
//!
//! Weighted towards what a declaration must be *refused* for. A spec that
//! parses and then renders nothing is the expensive failure here: a run defines
//! a ledger, records into it for an hour, and reads back an empty file with no
//! error anywhere to say why.
#![allow(clippy::expect_used)]

use serde_json::json;

use super::super::budget;
use super::{Check, Role, Source, parse};

fn minimal() -> serde_json::Value {
    json!({
        "slug": "tasks",
        "title": "Tasks",
        "purpose": "What to do next.",
        "source": "queue",
        "path": "config/tasks.jsonl",
        "derived": "TASKS.md",
        "fields": [
            { "name": "id", "role": "id", "required": true },
            { "name": "title", "role": "title", "required": true },
            { "name": "detail", "role": "prose" },
            { "name": "status", "role": "status" }
        ],
        "statuses": [
            { "name": "open" },
            { "name": "done", "closed": true, "needs_reason": true }
        ],
        "sections": [
            { "heading": "Do next", "blurb": "In order.", "statuses": ["open"], "cap": 10 }
        ],
        "checks": ["required-field", "closed-needs-reason"],
        "writers": ["goals", "director"]
    })
}

/// A well-formed declaration round-trips into the shape the engine renders.
#[test]
fn a_declaration_parses() {
    let spec = parse(&minimal(), true).expect("a well-formed declaration parses");
    assert_eq!(spec.slug, "tasks");
    assert_eq!(spec.derived, "TASKS.md");
    assert!(spec.builtin);
    assert_eq!(
        spec.source,
        Source::Queue {
            path: "config/tasks.jsonl".to_string()
        }
    );
    assert_eq!(spec.id_field().expect("an id field").name, "id");
    assert_eq!(spec.title_field().expect("a title field").name, "title");
    assert_eq!(spec.status_field().expect("a status field").role, Role::Status);
    assert!(spec.knows_status("OPEN"), "status matching is case-blind");
    assert!(!spec.knows_status("blocked"));
    assert!(
        spec.status("done").expect("the done status").needs_reason,
        "closing into `done` demands an outcome"
    );
    assert_eq!(spec.checks, vec![Check::RequiredField, Check::ClosedNeedsReason]);
}

/// Only the named writers may write, and an empty list means anyone holding the
/// tool.
#[test]
fn writers_are_checked_per_ledger() {
    let spec = parse(&minimal(), true).expect("parses");
    assert!(spec.writable_by("goals"));
    assert!(!spec.writable_by("reflection"));

    let mut open = minimal();
    open["writers"] = json!([]);
    let spec = parse(&open, true).expect("parses");
    assert!(
        spec.writable_by("reflection"),
        "an empty writer list is not a closed one"
    );
}

/// A section may not ask for more rows than the shared bound allows.
///
/// The whole point of declaring a ledger is that a run can add one, and the
/// whole point of the bounds is that no ledger can dominate a prompt. A `cap`
/// a declaration could raise would be the second of those undone by the first.
#[test]
fn a_section_cap_is_clamped_not_trusted() {
    let mut document = minimal();
    document["sections"][0]["cap"] = json!(1_000_000);
    let spec = parse(&document, false).expect("parses");
    assert_eq!(spec.sections[0].cap, budget::MAX_LISTED);
}

/// A section filtering on an undeclared status is refused rather than rendered
/// empty forever.
#[test]
fn a_section_naming_an_unknown_status_is_refused() {
    let mut document = minimal();
    document["sections"][0]["statuses"] = json!(["blocked"]);
    let error = parse(&document, false).expect_err("an always-empty section is refused");
    assert!(
        error.to_string().contains("blocked"),
        "the message names the offending status: {error}"
    );
}

/// Without an id field nothing can name an entry to close it.
#[test]
fn a_ledger_without_an_id_is_refused() {
    let mut document = minimal();
    document["fields"] = json!([{ "name": "title", "role": "title" }]);
    let error = parse(&document, false).expect_err("an id-less ledger is refused");
    assert!(error.to_string().contains("`id`"), "{error}");
}

/// A slug reaches the filesystem, so it is held to what a filename may carry.
#[test]
fn a_slug_that_could_escape_the_directory_is_refused() {
    for bad in ["../escape", "Tasks", "with space", "with/slash", ""] {
        let mut document = minimal();
        document["slug"] = json!(bad);
        assert!(
            parse(&document, false).is_err(),
            "`{bad}` must not be accepted as a slug"
        );
    }
}

/// The three source kinds are the whole set; anything else is a typo that would
/// otherwise become a silently empty ledger.
#[test]
fn an_unknown_source_kind_is_refused() {
    let mut document = minimal();
    document["source"] = json!("sqlite");
    let error = parse(&document, false).expect_err("an unknown source is refused");
    assert!(error.to_string().contains("queue"), "{error}");

    document["source"] = json!("items");
    let error = parse(&document, false).expect_err("an items ledger needs a dir");
    assert!(error.to_string().contains("dir"), "{error}");

    document["dir"] = json!("research/folds");
    let error = parse(&document, false).expect_err("an items ledger needs a block name");
    assert!(error.to_string().contains("block"), "{error}");

    document["block"] = json!("fold");
    let spec = parse(&document, false).expect("now it parses");
    assert_eq!(
        spec.source,
        Source::Items {
            dir: "research/folds".to_string(),
            block: "fold".to_string()
        }
    );
}

/// A ledger with no statuses cannot say what any of its sections hold.
#[test]
fn a_ledger_needs_a_status_and_a_derived_path() {
    let mut document = minimal();
    document["statuses"] = json!([]);
    assert!(parse(&document, false).is_err());

    let mut document = minimal();
    document.as_object_mut().expect("an object").remove("derived");
    assert!(parse(&document, false).is_err());
}

/// An unrecognised check is dropped rather than refusing the whole ledger.
///
/// The opposite reading of the source and status cases above, and deliberately:
/// a missing source makes the ledger meaningless, while a check nobody
/// implements only means one fault goes unreported. Losing the ledger would
/// cost more than losing the check.
#[test]
fn an_unknown_check_is_dropped_rather_than_fatal() {
    let mut document = minimal();
    document["checks"] = json!(["required-field", "proves-the-goal"]);
    let spec = parse(&document, false).expect("the ledger still parses");
    assert_eq!(spec.checks, vec![Check::RequiredField]);
}
