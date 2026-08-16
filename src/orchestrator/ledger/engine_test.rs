//! Unit tests for the ledger engine: the fold, the merge, and the render.
#![allow(clippy::expect_used)]

use serde_json::{Map, Value, json};

use super::super::spec::{LedgerSpec, Order, parse};
use super::{append, collect, merge, ordered, render};

fn tasks_spec() -> LedgerSpec {
    parse(
        &json!({
            "slug": "tasks",
            "title": "Tasks",
            "purpose": "What to do next, and what was already done.",
            "source": "queue",
            "path": "config/tasks.jsonl",
            "derived": "TASKS.md",
            "fields": [
                { "name": "id", "role": "id", "required": true },
                { "name": "title", "role": "title", "required": true },
                { "name": "detail", "role": "prose" },
                { "name": "reason", "role": "prose" },
                { "name": "refs", "role": "refs" },
                { "name": "status", "role": "status" }
            ],
            "statuses": [
                { "name": "open" },
                { "name": "done", "closed": true, "needs_reason": true },
                { "name": "dropped", "closed": true, "needs_reason": true }
            ],
            "sections": [
                { "heading": "Do next", "blurb": "In order.", "statuses": ["open"] },
                { "heading": "Do not do", "blurb": "With reasons.", "statuses": ["dropped"] },
                { "heading": "Recently done", "statuses": ["done"] }
            ],
            "checks": ["required-field", "known-status", "closed-needs-reason"]
        }),
        true,
    )
    .expect("the task spec parses")
}

/// The shape the built-in `tasks` now has: a work queue ordered by what was
/// touched last, above an archive that keeps arrival order.
fn recent_tasks_spec() -> LedgerSpec {
    parse(
        &json!({
            "slug": "tasks",
            "title": "Tasks",
            "source": "queue",
            "path": "config/tasks.jsonl",
            "derived": "TASKS.md",
            "fields": [
                { "name": "id", "role": "id" },
                { "name": "title", "role": "title" },
                { "name": "reason", "role": "prose" },
                { "name": "status", "role": "status" }
            ],
            "statuses": [
                { "name": "open" },
                { "name": "done", "closed": true }
            ],
            "sections": [
                {
                    "heading": "Do next",
                    "blurb": "Most recently added first.",
                    "statuses": ["open"],
                    "order": "recent"
                },
                { "heading": "Recently done", "statuses": ["done"] }
            ]
        }),
        true,
    )
    .expect("the recent task spec parses")
}

fn folds_spec() -> LedgerSpec {
    parse(
        &json!({
            "slug": "folds",
            "title": "Folds",
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
            "statuses": [{ "name": "open" }, { "name": "sealed", "closed": true }],
            "sections": [{ "heading": "Open", "statuses": ["open"] }]
        }),
        false,
    )
    .expect("the fold spec parses")
}

fn fields(pairs: &[(&str, &str)]) -> Map<String, Value> {
    pairs
        .iter()
        .map(|(name, value)| ((*name).to_string(), json!(value)))
        .collect()
}

/// The whole point of an event log: closing a task keeps the record of it.
///
/// A wholesale rewrite of `TASKS.md` deleted the finished rows, so nothing on
/// disk said what the run had done or why anything was ruled out. Here the
/// close is another event, the fold applies it, and the row moves section
/// instead of disappearing.
#[test]
fn closing_an_entry_keeps_it_and_moves_it() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();

    append(
        workspace.path(),
        &spec,
        "goals",
        "fix-the-audit-verdict",
        &fields(&[
            ("title", "Fix the audit's verdict logic"),
            ("detail", "A refuted sub-check must not print ALL CHECKS PASSED."),
            ("status", "open"),
        ]),
    )
    .expect("the task is recorded");

    let entries = collect(workspace.path(), &spec);
    assert_eq!(entries.entries.len(), 1);
    assert_eq!(entries.entries[0].status(&spec), "open");

    append(
        workspace.path(),
        &spec,
        "coder",
        "fix-the-audit-verdict",
        &fields(&[
            ("status", "done"),
            ("reason", "verdict now prints (D) refuted separately; re-captured."),
        ]),
    )
    .expect("the close is recorded");

    let entries = collect(workspace.path(), &spec);
    assert_eq!(entries.entries.len(), 1, "closing does not add a second row");
    let entry = &entries.entries[0];
    assert_eq!(entry.status(&spec), "done");
    assert_eq!(
        entry.title(&spec),
        "Fix the audit's verdict logic",
        "the merge left the title alone rather than blanking it"
    );
    assert!(
        entry.get("reason").contains("re-captured"),
        "the outcome survives, which is what a rewrite destroyed"
    );
    assert_eq!(entry.from, "coder", "the last writer is recorded");

    let rendered = render(&spec, &entries);
    assert!(rendered.contains("## Recently done"));
    assert!(!rendered.contains("## Do next"), "the open section is empty");
    assert!(rendered.contains("re-captured"));
}

/// A dropped task keeps its reason, which is the `Do not do` list the live
/// workspace was maintaining by hand.
#[test]
fn a_dropped_entry_renders_with_its_reason() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    append(
        workspace.path(),
        &spec,
        "director",
        "queue-a-4e9-sieve",
        &fields(&[
            ("title", "Queue a 4e9 sieve run"),
            ("status", "dropped"),
            ("reason", "Directive 36 stands: the empirical route is at its ceiling."),
        ]),
    )
    .expect("recorded");
    let rendered = render(&spec, &collect(workspace.path(), &spec));
    assert!(rendered.contains("## Do not do"));
    assert!(rendered.contains("Directive 36 stands"));
}

/// Closing into a status that demands a reason, without one, is reported.
#[test]
fn closing_without_a_reason_is_a_reported_fault() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    append(
        workspace.path(),
        &spec,
        "goals",
        "silent-close",
        &fields(&[("title", "Something"), ("status", "done")]),
    )
    .expect("recorded");
    let entries = collect(workspace.path(), &spec);
    assert!(
        entries.faults.iter().any(|fault| fault.contains("silent-close")),
        "a close with no reason is reported: {:?}",
        entries.faults
    );
    assert!(render(&spec, &entries).contains("## Entries that could not be read"));
}

/// An unknown status and a missing required field are both reported rather than
/// guessed at.
#[test]
fn the_declared_checks_report_what_they_find() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    append(
        workspace.path(),
        &spec,
        "goals",
        "odd-one",
        &fields(&[("status", "marinating")]),
    )
    .expect("recorded");
    let entries = collect(workspace.path(), &spec);
    let faults = entries.faults.join("\n");
    assert!(faults.contains("marinating"), "unknown status reported: {faults}");
    assert!(faults.contains("`title`"), "missing required field reported: {faults}");
}

/// A null clears a field. It is the one thing a merge cannot otherwise say.
#[test]
fn a_null_clears_a_field() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    append(
        workspace.path(),
        &spec,
        "goals",
        "task",
        &fields(&[("title", "A task"), ("detail", "some detail"), ("status", "open")]),
    )
    .expect("recorded");
    let mut clearing = Map::new();
    clearing.insert("detail".to_string(), Value::Null);
    append(workspace.path(), &spec, "goals", "task", &clearing).expect("recorded");
    let entries = collect(workspace.path(), &spec);
    assert_eq!(entries.entries[0].get("detail"), "");
    assert_eq!(entries.entries[0].get("title"), "A task");
}

/// A torn or malformed line costs that one event, not the whole ledger.
#[test]
fn an_unreadable_line_does_not_cost_the_other_entries() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    let queue = workspace.path().join("config/tasks.jsonl");
    std::fs::create_dir_all(queue.parent().expect("a parent")).expect("the directory");
    std::fs::write(
        &queue,
        "{\"id\":\"first\",\"fields\":{\"title\":\"First\",\"status\":\"open\"}}\n\
         {\"id\":\"torn\",\"fields\":{\"tit\n\
         {\"id\":\"second\",\"fields\":{\"title\":\"Second\",\"status\":\"open\"}}\n",
    )
    .expect("the queue");
    let entries = collect(workspace.path(), &spec);
    let ids: Vec<&str> = entries.entries.iter().map(|entry| entry.id.as_str()).collect();
    assert_eq!(ids, vec!["first", "second"]);
    assert!(
        entries.faults.iter().any(|fault| fault.contains("line 2")),
        "the skipped line is named: {:?}",
        entries.faults
    );
}

/// Entries render in the order their ids were first seen.
///
/// A map keyed by id would sort alphabetically, which for a task list is no
/// order at all — the thing to do next would move whenever somebody named a
/// task with an earlier letter.
#[test]
fn entries_keep_the_order_they_arrived_in() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    for id in ["zebra", "alpha", "mango"] {
        append(
            workspace.path(),
            &spec,
            "goals",
            id,
            &fields(&[("title", id), ("status", "open")]),
        )
        .expect("recorded");
    }
    // Touching the first one again must not move it to the end.
    append(
        workspace.path(),
        &spec,
        "goals",
        "zebra",
        &fields(&[("detail", "still first")]),
    )
    .expect("recorded");
    let entries = collect(workspace.path(), &spec);
    let ids: Vec<&str> = entries.entries.iter().map(|entry| entry.id.as_str()).collect();
    assert_eq!(ids, vec!["zebra", "alpha", "mango"]);
}

/// The two orders on one queue, on a fixture where they cannot agree.
///
/// Three tasks arrive, then the *first* is touched again. That separates all
/// three candidate answers: recorded order is the arrival order, recent order
/// puts the re-touched one first and the rest newest-first behind it, and
/// newest-*created*-first — the ordering this deliberately is not — would put
/// the re-touched one last.
#[test]
fn recent_order_is_by_last_event_and_recorded_order_is_by_first() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    for id in ["alpha", "beta", "gamma"] {
        append(
            workspace.path(),
            &spec,
            "goals",
            id,
            &fields(&[("title", id), ("status", "open")]),
        )
        .expect("recorded");
    }
    append(
        workspace.path(),
        &spec,
        "director",
        "alpha",
        &fields(&[("detail", "raised by a directive")]),
    )
    .expect("recorded");

    let entries = collect(workspace.path(), &spec);
    let ids = |order| {
        ordered(&entries.entries, order)
            .into_iter()
            .map(|entry| entry.id.clone())
            .collect::<Vec<String>>()
    };
    assert_eq!(
        ids(Order::Recorded),
        vec!["alpha", "beta", "gamma"],
        "recorded order is the order the ids were first seen"
    );
    assert_eq!(
        ids(Order::Recent),
        vec!["alpha", "gamma", "beta"],
        "recent order is by last event: alpha was touched after gamma arrived"
    );
}

/// The motivating case, at the level the render decides it: a task recorded
/// last is the first row of `Do next`.
#[test]
fn a_task_recorded_last_renders_first_under_a_recent_section() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = recent_tasks_spec();
    for id in ["stale-exhaustive-line-test", "the-directives-task"] {
        append(
            workspace.path(),
            &spec,
            "director",
            id,
            &fields(&[("title", id), ("status", "open")]),
        )
        .expect("recorded");
    }
    let rendered = render(&spec, &collect(workspace.path(), &spec));
    let new = rendered
        .find("the-directives-task")
        .expect("the new task renders");
    let old = rendered
        .find("stale-exhaustive-line-test")
        .expect("the old task renders");
    assert!(
        new < old,
        "the newest task leads the section a role is told to work from the top of:\n{rendered}"
    );
}

/// A section that does not declare an order keeps the one every ledger had
/// before ordering existed.
#[test]
fn a_section_without_an_order_is_unaffected() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = recent_tasks_spec();
    for id in ["first-done", "second-done"] {
        append(
            workspace.path(),
            &spec,
            "goals",
            id,
            &fields(&[("title", id), ("status", "done"), ("reason", "it finished")]),
        )
        .expect("recorded");
    }
    assert_eq!(
        spec.sections[1].order,
        Order::Recorded,
        "`Recently done` is an archive, not a queue"
    );
    let rendered = render(&spec, &collect(workspace.path(), &spec));
    let first = rendered.find("first-done").expect("it renders");
    let second = rendered.find("second-done").expect("it renders");
    assert!(
        first < second,
        "a recorded section still lists in arrival order:\n{rendered}"
    );
}

/// An items ledger has no queue, so `recent` leaves it in recorded order rather
/// than inventing one out of the filesystem.
#[test]
fn an_items_ledger_keeps_recorded_order_under_either_order() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = folds_spec();
    for id in ["aaa", "bbb", "ccc"] {
        merge(
            workspace.path(),
            &spec,
            id,
            &fields(&[("subject", id), ("status", "open")]),
        )
        .expect("the block is written");
    }
    let entries = collect(workspace.path(), &spec);
    let ids = |order| {
        ordered(&entries.entries, order)
            .into_iter()
            .map(|entry| entry.id.clone())
            .collect::<Vec<String>>()
    };
    assert_eq!(ids(Order::Recorded), vec!["aaa", "bbb", "ccc"]);
    assert_eq!(
        ids(Order::Recent),
        vec!["aaa", "bbb", "ccc"],
        "no queue means no touch order, and mtime is not a stand-in for one"
    );
}

/// Merging into an items file changes the named fields and nothing else.
#[test]
fn a_merge_leaves_the_rest_of_the_file_alone() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = folds_spec();

    let path = merge(
        workspace.path(),
        &spec,
        "passes",
        &fields(&[("subject", "The pass rule"), ("status", "open")]),
    )
    .expect("the block is written");
    assert_eq!(path, "research/folds/passes.md");

    // A working note grows around the block, which is the whole shape of an
    // items ledger: a file somebody writes in, with a block the engine reads.
    let file = workspace.path().join(&path);
    let text = std::fs::read_to_string(&file).expect("the file");
    std::fs::write(&file, format!("{text}\n## Working notes\n\nSomething handwritten.\n"))
        .expect("the note");

    merge(
        workspace.path(),
        &spec,
        "passes",
        &fields(&[("holds", "the parity argument closes it")]),
    )
    .expect("the merge");

    let text = std::fs::read_to_string(&file).expect("the file");
    assert!(
        text.contains("Something handwritten."),
        "the prose around the block survives a merge: {text}"
    );
    assert!(text.contains("subject: The pass rule"), "untouched fields survive");
    assert!(text.contains("holds: the parity argument closes it"));
    assert_eq!(
        text.matches("```fold").count(),
        1,
        "the block is replaced, not duplicated: {text}"
    );

    let entries = collect(workspace.path(), &spec);
    assert_eq!(entries.entries.len(), 1);
    assert_eq!(entries.entries[0].id, "passes");
}

/// A newline in a field would close the block early and truncate everything
/// after it, so it is folded to a space rather than written through.
#[test]
fn a_newline_in_a_field_cannot_break_the_block() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = folds_spec();
    merge(
        workspace.path(),
        &spec,
        "multi",
        &fields(&[
            ("subject", "one\nlong\nsubject"),
            ("holds", "still here"),
            ("status", "open"),
        ]),
    )
    .expect("the merge");
    let entries = collect(workspace.path(), &spec);
    assert_eq!(entries.entries.len(), 1);
    assert_eq!(entries.entries[0].get("subject"), "one long subject");
    assert_eq!(
        entries.entries[0].get("holds"),
        "still here",
        "the field after the folded one is not lost"
    );
}

/// An items file whose id field is filled in wins over its filename.
#[test]
fn an_explicit_id_beats_the_filename() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = folds_spec();
    let dir = workspace.path().join("research/folds");
    std::fs::create_dir_all(&dir).expect("the directory");
    std::fs::write(
        dir.join("whatever.md"),
        "# a note\n\n```fold\nid: the-real-id\nsubject: A subject\nstatus: open\n```\n",
    )
    .expect("the file");
    let entries = collect(workspace.path(), &spec);
    assert_eq!(entries.entries[0].id, "the-real-id");
}

/// Appending to a ledger that keeps files, or merging into one that keeps a
/// queue, is refused rather than half-done.
#[test]
fn the_two_source_kinds_refuse_each_other_s_writes() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    assert!(
        merge(workspace.path(), &tasks_spec(), "x", &fields(&[("a", "b")])).is_err(),
        "a queue ledger has no block to merge into"
    );
    assert!(
        append(
            workspace.path(),
            &folds_spec(),
            "goals",
            "x",
            &fields(&[("a", "b")])
        )
        .is_err(),
        "an items ledger has no queue to append to"
    );
}

/// A ledger with no entries says so rather than rendering an empty shell.
#[test]
fn an_empty_ledger_says_it_is_empty() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    let rendered = render(&spec, &collect(workspace.path(), &spec));
    assert!(rendered.contains("Nothing recorded yet"));
    assert!(rendered.contains("Do not edit this file"));
}

/// A required id field is satisfied by the entry's identity, not by a field.
///
/// The id lives at the top level of every queue event; nothing writes it into
/// `fields`, and the parser drops an event without one. So a spec that declares
/// its id field required — as `tasks` does — used to report every one of its own
/// well-formed rows as unreadable. A live workspace had all eight of its open
/// tasks under "Entries that could not be read", and the run could not see its
/// own queue while the file on disk was perfectly valid.
#[test]
fn a_required_id_is_met_by_the_entrys_own_identity() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();

    append(
        workspace.path(),
        &spec,
        "goals",
        "f2-matrix-covering-bound",
        &fields(&[
            ("title", "Prove wt(M_n h) >= (2/3) wt(h)"),
            ("status", "open"),
        ]),
    )
    .expect("the task is recorded");

    let entries = collect(workspace.path(), &spec);
    assert_eq!(entries.entries.len(), 1, "the entry is read back");
    assert!(
        entries.faults.is_empty(),
        "an entry whose id is its identity is not a fault: {:?}",
        entries.faults
    );
}

/// The index keeps every id and status, and drops the prose behind them.
///
/// This is the trade the whole module makes, measured on the ledger that made
/// it worth making: `TASKS.md` was 8,539 tokens in each of thirteen prompts,
/// and most of that was `detail` and `reason` fields on rows nobody was going
/// to work again. The obligation a closed row discharges is *do not re-propose
/// this*, and an id beside the word `dropped` discharges it.
#[test]
fn the_index_keeps_identities_and_drops_the_prose() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();

    append(
        workspace.path(),
        &spec,
        "goals",
        "enumerate-the-ball",
        &fields(&[
            ("title", "Enumerate the radius-2 ball"),
            ("detail", &"a paragraph nobody needs up front. ".repeat(80)),
            ("status", "open"),
        ]),
    )
    .expect("the open task is recorded");
    append(
        workspace.path(),
        &spec,
        "goals",
        "search-the-answer-space",
        &fields(&[
            ("title", "Search the answer space"),
            ("status", "dropped"),
            ("reason", &"the reason it was ruled out, at length. ".repeat(80)),
        ]),
    )
    .expect("the dropped task is recorded");

    let entries = collect(workspace.path(), &spec);
    let index = super::index(&spec, &entries);

    for expected in [
        "enumerate-the-ball",
        "search-the-answer-space",
        "(open)",
        "(dropped)",
        "Enumerate the radius-2 ball",
    ] {
        assert!(index.contains(expected), "`{expected}` survives: {index}");
    }
    assert!(
        !index.contains("a paragraph nobody needs up front."),
        "the detail is dropped: {index}"
    );
    assert!(
        !index.contains("the reason it was ruled out, at length."),
        "the reason is dropped: {index}"
    );
    assert!(
        index.len() < render(&spec, &entries).len(),
        "an index is smaller than the file it replaces"
    );
}

/// An index that shortens a ledger has to say so, and say how to reach the rest.
///
/// A role that reads a shortened list and never calls `read_ledger` is cheaper
/// *and dumber* — it concludes the run holds nothing more and re-proposes what
/// was cut, which is strictly worse than sending the whole file.
#[test]
fn the_index_names_the_call_that_fetches_what_it_dropped() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = tasks_spec();
    append(
        workspace.path(),
        &spec,
        "goals",
        "one-task",
        &fields(&[("title", "One task"), ("status", "open")]),
    )
    .expect("the task is recorded");

    let entries = collect(workspace.path(), &spec);
    let index = super::index(&spec, &entries);

    assert!(
        index.contains("This is the index, not the ledger."),
        "the copy says it is shortened: {index}"
    );
    assert!(
        index.contains(r#"read_ledger { ledger: "tasks""#),
        "the index names the call and the slug: {index}"
    );
}

/// The archive is capped and the work queue is not.
///
/// An index is read top-down for what to do next, and on a long-lived workspace
/// the archive is most of the file: every open row still has to be there, and
/// the twentieth finished one does not. What it leaves out it says, by status,
/// so the reader knows to call rather than concluding the run did nothing else.
#[test]
fn the_index_keeps_every_open_row_and_the_last_few_closed_ones() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = recent_tasks_spec();

    for index in 0..8 {
        append(
            workspace.path(),
            &spec,
            "goals",
            &format!("open-{index}"),
            &fields(&[("title", "still to do"), ("status", "open")]),
        )
        .expect("the open task is recorded");
    }
    for index in 0..9 {
        append(
            workspace.path(),
            &spec,
            "goals",
            &format!("closed-{index}"),
            &fields(&[
                ("title", "already finished"),
                ("status", "done"),
                ("reason", "it was carried out"),
            ]),
        )
        .expect("the finished task is recorded");
    }

    let entries = collect(workspace.path(), &spec);
    let index = super::index(&spec, &entries);

    for open in 0..8 {
        assert!(
            index.contains(&format!("`open-{open}`")),
            "every open row is carried: {index}"
        );
    }
    // The five most recent of the nine, and the four oldest reported as absent.
    for kept in 4..9 {
        assert!(
            index.contains(&format!("`closed-{kept}`")),
            "the recent archive is carried: {index}"
        );
    }
    for cut in 0..4 {
        assert!(
            !index.contains(&format!("`closed-{cut}`")),
            "the old archive is cut: {index}"
        );
    }
    assert!(
        index.contains("4 more `done`"),
        "the index says what it left out, by status: {index}"
    );
}

/// A ledger with no closed status is untouched by the archive cap.
#[test]
fn a_ledger_that_closes_nothing_keeps_every_row_in_its_index() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let spec = parse(
        &json!({
            "slug": "notes",
            "title": "Notes",
            "source": "queue",
            "path": "config/notes.jsonl",
            "derived": "NOTES.md",
            "fields": [
                { "name": "id", "role": "id" },
                { "name": "title", "role": "title" }
            ],
            "statuses": []
        }),
        false,
    )
    .expect("the note spec parses");

    for index in 0..9 {
        append(
            workspace.path(),
            &spec,
            "goals",
            &format!("note-{index}"),
            &fields(&[("title", "a note")]),
        )
        .expect("the note is recorded");
    }

    let entries = collect(workspace.path(), &spec);
    let index = super::index(&spec, &entries);
    for note in 0..9 {
        assert!(index.contains(&format!("`note-{note}`")), "{index}");
    }
    assert!(!index.contains("most recent of each kind"), "{index}");
}
