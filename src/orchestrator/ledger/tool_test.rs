//! Unit tests for the six ledger tools.
#![allow(clippy::expect_used)]

use serde_json::{Value, json};

use super::{Kind, LedgerTool};
use crate::agent::{Tool as _, ToolCall};
use crate::orchestrator::documents::WorkspaceDocuments;

fn tool(root: &std::path::Path, kind: Kind, role: &str) -> LedgerTool {
    LedgerTool {
        kind,
        documents: WorkspaceDocuments::new(root.to_path_buf())
            .expect("a workspace under a temporary directory is accepted"),
        role: role.to_string(),
    }
}

async fn run(root: &std::path::Path, kind: Kind, role: &str, arguments: Value) -> Result<String, String> {
    let tool = tool(root, kind, role);
    let call = ToolCall {
        id: "1".to_string(),
        name: tool.name().to_string(),
        arguments,
        invalid: None,
    };
    match tool.call(&(), call).await {
        Ok(result) => Ok(result.content),
        Err(error) => Err(error.to_string()),
    }
}

/// The end-to-end shape of the thing this was built for: record a task, close
/// it, and read the outcome back.
#[tokio::test]
async fn a_task_is_recorded_closed_and_still_readable() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();

    let recorded = run(
        root,
        Kind::Record,
        "goals",
        json!({
            "ledger": "tasks",
            "id": "fix-the-audit-verdict",
            "fields": {
                "title": "Fix the audit's verdict logic",
                "detail": "A refuted sub-check must not print ALL AUDIT CHECKS PASSED.",
                "status": "open"
            }
        }),
    )
    .await
    .expect("the task is recorded");
    assert!(recorded.contains("derived/TASKS.md"), "the render is reported: {recorded}");

    let rendered = std::fs::read_to_string(root.join("derived/TASKS.md")).expect("TASKS.md exists");
    assert!(rendered.contains("## Do next"));
    assert!(rendered.contains("Fix the audit's verdict logic"));

    let closed = run(
        root,
        Kind::Close,
        "goals",
        json!({
            "ledger": "tasks",
            "id": "fix-the-audit-verdict",
            "status": "done",
            "reason": "the verdict now prints (D) refuted separately; re-captured to .captured2.txt"
        }),
    )
    .await
    .expect("the task closes");
    assert!(closed.contains("stays on the ledger"), "{closed}");

    let rendered = std::fs::read_to_string(root.join("derived/TASKS.md")).expect("TASKS.md exists");
    assert!(rendered.contains("## Recently done"));
    assert!(
        rendered.contains("captured2"),
        "the outcome is on the ledger, which a wholesale rewrite destroyed: {rendered}"
    );

    let read = run(
        root,
        Kind::Read,
        "goals",
        json!({ "ledger": "tasks", "status": "done" }),
    )
    .await
    .expect("the ledger reads");
    assert!(read.contains("fix-the-audit-verdict"));
    assert!(read.contains("re-captured"), "read_ledger returns it in full");
}

/// Closing without a reason, or into a status that does not close, is refused
/// at the call rather than recorded and reported later.
#[tokio::test]
async fn a_close_must_say_what_came_of_it() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();
    run(
        root,
        Kind::Record,
        "goals",
        json!({ "ledger": "tasks", "id": "a-task", "fields": { "title": "A task", "status": "open" } }),
    )
    .await
    .expect("recorded");

    let error = run(
        root,
        Kind::Close,
        "goals",
        json!({ "ledger": "tasks", "id": "a-task", "status": "done", "reason": "  " }),
    )
    .await
    .expect_err("a blank reason is refused");
    assert!(error.contains("needs a reason"), "{error}");

    let error = run(
        root,
        Kind::Close,
        "goals",
        json!({ "ledger": "tasks", "id": "a-task", "status": "open", "reason": "because" }),
    )
    .await
    .expect_err("a non-closing status is refused");
    assert!(error.contains("does not close"), "{error}");
    assert!(error.contains("done"), "and names the ones that do: {error}");
}

/// A role the spec does not name cannot write, even holding the tool.
///
/// This is why write authority lives in the spec rather than in the grant: the
/// registry cannot express it, because a ledger may not exist when the tools
/// are registered.
#[tokio::test]
async fn a_role_outside_the_writer_list_is_refused() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let error = run(
        workspace.path(),
        Kind::Record,
        "judge",
        json!({ "ledger": "tasks", "id": "x", "fields": { "title": "y" } }),
    )
    .await
    .expect_err("the judge does not file tasks");
    assert!(error.contains("judge"), "{error}");
    assert!(!workspace.path().join("derived/TASKS.md").exists(), "and nothing was written");
}

/// An unknown slug comes back with the list of real ones.
///
/// The error is the discovery path: a model that guessed learns the right name
/// in one turn, without having thought to call `list_ledgers` first.
#[tokio::test]
async fn an_unknown_ledger_names_the_real_ones() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let error = run(
        workspace.path(),
        Kind::Read,
        "goals",
        json!({ "ledger": "todos" }),
    )
    .await
    .expect_err("there is no `todos`");
    assert!(error.contains("tasks"), "the real slug is offered: {error}");
    assert!(error.contains("approaches"), "{error}");
}

/// A run defines an axis and records into it in the same session.
///
/// The property the whole design turns on. The tool schema was fixed when the
/// container started, so this only works because `ledger` is a string checked
/// at call time rather than an enum.
#[tokio::test]
async fn a_run_defines_a_ledger_and_uses_it_immediately() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();

    let defined = run(
        root,
        Kind::Define,
        "orchestrator",
        json!({
            "slug": "folds",
            "title": "Folds",
            "purpose": "What the run knows about one subject, gathered across arrival batches.",
            "source": "items",
            "dir": "research/folds",
            "block": "fold",
            "derived": "research/FOLDS.md",
            "fields": [
                { "name": "id", "role": "id" },
                { "name": "subject", "role": "title" },
                { "name": "holds", "role": "prose" },
                { "name": "status", "role": "status" }
            ],
            "statuses": [{ "name": "open" }, { "name": "sealed", "closed": true, "needs_reason": true }],
            "sections": [{ "heading": "Open", "blurb": "Still filling.", "statuses": ["open"] }]
        }),
    )
    .await
    .expect("the ledger is defined");
    assert!(defined.contains("record_entry"), "{defined}");

    let recorded = run(
        root,
        Kind::Record,
        "orchestrator",
        json!({
            "ledger": "folds",
            "id": "the pass rule",
            "fields": { "subject": "The pass rule", "holds": "parity closes it", "status": "open" }
        }),
    )
    .await
    .expect("recording into a ledger defined this session");
    assert!(recorded.contains("the-pass-rule"), "the id is slugified: {recorded}");

    let rendered =
        std::fs::read_to_string(root.join("research/FOLDS.md")).expect("the new ledger renders");
    assert!(rendered.contains("## Open"));
    assert!(rendered.contains("parity closes it"));

    let listed = run(root, Kind::List, "orchestrator", json!({}))
        .await
        .expect("the listing");
    assert!(listed.contains("`folds`"));
    assert!(listed.contains("defined by this run"));
    assert!(listed.contains("`tasks`"), "the built-ins are listed too");
}

/// A ledger rendered by its own module serves its file rather than an empty
/// list.
///
/// An empty list would read as *the run recorded nothing*, which for the claim
/// ledger is the most misleading answer available.
#[tokio::test]
async fn a_runtime_rendered_ledger_reads_its_file() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();
    std::fs::create_dir_all(root.join("derived")).expect("the directory");
    std::fs::write(
        root.join("derived/CLAIMS.md"),
        "# Claims\n\n| Claim | Statement |\n| --- | --- |\n| `a-claim` | something true |\n",
    )
    .expect("the file");

    let read = run(root, Kind::Read, "goals", json!({ "ledger": "claims" }))
        .await
        .expect("it reads");
    assert!(read.contains("something true"));

    let error = run(
        root,
        Kind::Record,
        "goals",
        json!({ "ledger": "claims", "id": "x", "fields": { "a": "b" } }),
    )
    .await
    .expect_err("it is not written through this tool");
    assert!(error.contains("note"), "the message says what to write instead: {error}");
}

/// `read_ledger` is the pull side, so it says how many it did not show.
#[tokio::test]
async fn a_read_says_what_it_did_not_show() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();
    for index in 0..30 {
        run(
            root,
            Kind::Record,
            "goals",
            json!({
                "ledger": "tasks",
                "id": format!("task-{index}"),
                "fields": { "title": format!("Task {index}"), "status": "open" }
            }),
        )
        .await
        .expect("recorded");
    }
    let read = run(root, Kind::Read, "goals", json!({ "ledger": "tasks", "limit": 5 }))
        .await
        .expect("it reads");
    assert!(read.contains("5 of 30"), "{read}");
    assert!(read.contains("25 more match"), "{read}");

    let filtered = run(
        root,
        Kind::Read,
        "goals",
        json!({ "ledger": "tasks", "query": "task 7" }),
    )
    .await
    .expect("it reads");
    assert!(filtered.contains("task-7"));
    assert!(!filtered.contains("task-12"));
}

/// The failure this ordering was built for, end to end on the built-in ledger.
///
/// A live `director` turned a human directive into task rows correctly and then
/// reported that it could not get them read: `TASKS.md` rendered in first-seen
/// order, so the fresh, higher-priority row landed at the *bottom* of a section
/// whose blurb tells the next role to work the first one it can.
#[tokio::test]
async fn a_task_added_last_leads_do_next() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();
    for id in ["gsplit-exhaustive-line-test", "the-directives-task"] {
        run(
            root,
            Kind::Record,
            "director",
            json!({
                "ledger": "tasks",
                "id": id,
                "fields": { "title": format!("Work on {id}"), "status": "open" }
            }),
        )
        .await
        .expect("recorded");
    }

    let rendered = std::fs::read_to_string(root.join("derived/TASKS.md")).expect("TASKS.md exists");
    let new = rendered.find("the-directives-task").expect("it renders");
    let old = rendered
        .find("gsplit-exhaustive-line-test")
        .expect("it renders");
    assert!(
        new < old,
        "the newest task leads `Do next`, which is the section a role works from the top of:\n\
         {rendered}"
    );

    // And an older row is raised by recording against it — the reason the order
    // is by last event rather than by newest created.
    run(
        root,
        Kind::Record,
        "director",
        json!({
            "ledger": "tasks",
            "id": "gsplit-exhaustive-line-test",
            "fields": { "detail": "directive 12 raises this" }
        }),
    )
    .await
    .expect("recorded");
    let rendered = std::fs::read_to_string(root.join("derived/TASKS.md")).expect("TASKS.md exists");
    assert!(
        rendered.find("gsplit-exhaustive-line-test") < rendered.find("the-directives-task"),
        "touching an existing task raises it, using a tool every writing role holds:\n{rendered}"
    );
}

/// The archives keep arrival order: they are read for what is on them.
#[tokio::test]
async fn recently_done_is_not_reordered() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();
    for id in ["first-finished", "second-finished"] {
        run(
            root,
            Kind::Record,
            "goals",
            json!({
                "ledger": "tasks",
                "id": id,
                "fields": { "title": format!("Task {id}"), "status": "open" }
            }),
        )
        .await
        .expect("recorded");
    }
    for id in ["first-finished", "second-finished"] {
        run(
            root,
            Kind::Close,
            "goals",
            json!({
                "ledger": "tasks",
                "id": id,
                "status": "done",
                "reason": "carried out, with the capture beside it"
            }),
        )
        .await
        .expect("closed");
    }
    let rendered = std::fs::read_to_string(root.join("derived/TASKS.md")).expect("TASKS.md exists");
    assert!(
        rendered.find("first-finished") < rendered.find("second-finished"),
        "`Recently done` is an archive and stays in recorded order:\n{rendered}"
    );
}

/// `sort` overrides the ledger's own order, and an unknown one names the real
/// ones rather than failing opaquely.
#[tokio::test]
async fn a_read_can_sort_and_says_what_the_orders_are() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();
    for id in ["oldest-task", "newest-task"] {
        run(
            root,
            Kind::Record,
            "goals",
            json!({
                "ledger": "tasks",
                "id": id,
                "fields": { "title": format!("Task {id}"), "status": "open" }
            }),
        )
        .await
        .expect("recorded");
    }

    let recent = run(root, Kind::Read, "goals", json!({ "ledger": "tasks" }))
        .await
        .expect("it reads");
    assert!(
        recent.find("newest-task") < recent.find("oldest-task"),
        "the task ledger's own order is most-recently-touched first: {recent}"
    );

    let recorded = run(
        root,
        Kind::Read,
        "goals",
        json!({ "ledger": "tasks", "sort": "recorded" }),
    )
    .await
    .expect("it reads");
    assert!(
        recorded.find("oldest-task") < recorded.find("newest-task"),
        "`sort` overrides the spec: {recorded}"
    );

    let error = run(
        root,
        Kind::Read,
        "goals",
        json!({ "ledger": "tasks", "sort": "newest" }),
    )
    .await
    .expect_err("an unknown order is refused");
    assert!(error.contains("recorded"), "the real orders are offered: {error}");
    assert!(error.contains("recent"), "{error}");
}

/// Fields are text. A nested object is refused rather than stored as JSON that
/// renders as JSON.
#[tokio::test]
async fn a_nested_field_is_refused_with_a_reason() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let error = run(
        workspace.path(),
        Kind::Record,
        "goals",
        json!({
            "ledger": "tasks",
            "id": "x",
            "fields": { "title": "A task", "detail": { "nested": true } }
        }),
    )
    .await
    .expect_err("nested fields are refused");
    assert!(error.contains("detail"), "the offending field is named: {error}");

    // A list is the ordinary way a model writes several references, so it is
    // joined rather than refused.
    run(
        workspace.path(),
        Kind::Record,
        "goals",
        json!({
            "ledger": "tasks",
            "id": "y",
            "fields": { "title": "A task", "refs": ["claim-1", "claim-2"], "status": "open" }
        }),
    )
    .await
    .expect("a list of refs is accepted");
    let rendered = std::fs::read_to_string(workspace.path().join("derived/TASKS.md")).expect("rendered");
    assert!(rendered.contains("claim-1, claim-2"), "{rendered}");
}

/// A record that names no fields would write an event saying nothing.
#[tokio::test]
async fn an_empty_record_is_refused() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let error = run(
        workspace.path(),
        Kind::Record,
        "goals",
        json!({ "ledger": "tasks", "id": "x", "fields": {} }),
    )
    .await
    .expect_err("refused");
    assert!(error.contains("record nothing"), "{error}");
}

/// Retiring a run's ledger leaves its entries, and a built-in cannot be
/// retired at all.
#[tokio::test]
async fn retiring_is_bounded_to_what_the_run_defined() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let root = workspace.path();
    let error = run(root, Kind::Retire, "orchestrator", json!({ "ledger": "tasks" }))
        .await
        .expect_err("a built-in cannot be retired");
    assert!(error.contains("built in"), "{error}");
}
