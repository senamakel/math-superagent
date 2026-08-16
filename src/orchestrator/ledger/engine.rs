//! Reading, folding and rendering a declared ledger.
//!
//! One engine for both source kinds, because the difference between them is
//! only where an entry's fields come from. After that they are the same thing:
//! a set of entries with ids, statuses and prose, rendered into bounded
//! sections.
//!
//! # Everything is a merge
//!
//! There is one write operation, and adding, closing, dropping, blocking and
//! reprioritising are all it. An event names an entry and carries some fields;
//! the fold applies them in order; absent keys are left alone. Closing a task
//! is `{status: done, outcome: …}` and nothing else.
//!
//! That is not a simplification for its own sake. A vocabulary of operations
//! means a vocabulary of *inverses* to get wrong — what `unblock` does to a
//! task that was never blocked, whether `reopen` restores the old status or the
//! default — and every one of those is a decision the fold would have to make
//! silently. A merge has no inverse to get wrong, and the event log keeps the
//! whole history either way, so nothing is lost by not naming the operations.
//!
//! It also means a run may add a field the spec never declared. That is
//! deliberate: the field is stored, reported as unknown by
//! [`super::spec::Check::RequiredField`]'s sibling checks, and never silently
//! dropped — the rule the claim ledger already follows for a malformed block. A
//! recorded fact that vanishes because a schema did not anticipate it is worse
//! than one that shows up in the wrong place, because only the second is
//! visible.
//!
//! # Why the queue needs no lock
//!
//! [`append`] is one `write_all` of one complete line on a handle opened for
//! append — the construction [`super::super::board`] and [`crate::directives`]
//! both use and both justify. Concurrent writers interleave whole lines and
//! never halves of one. The *render* is what they would collide on, and
//! `worklock` serialises that at the tool-call boundary.

use std::collections::BTreeMap;
use std::fmt::Write as _;
use std::io::Write as _;
use std::path::Path;

use serde_json::{Map, Value, json};

use super::budget;
use super::spec::{Check, LedgerSpec, Role, Source};
use crate::agent::Result;
use crate::orchestrator::text::truncate;

/// One entry, whatever kind of source it came from.
#[derive(Clone, Debug, Default)]
pub(in crate::orchestrator) struct Entry {
    pub(in crate::orchestrator) id: String,
    /// Every field recorded, including ones the spec does not declare.
    pub(in crate::orchestrator) fields: BTreeMap<String, String>,
    /// Who recorded it last. Empty for an items ledger, which has no sender.
    pub(in crate::orchestrator) from: String,
    /// Where this entry's *last* event sits in the queue, if it came from one.
    ///
    /// What [`super::spec::Order::Recent`] sorts on. The line number is the
    /// ordering, not the `at` timestamp: the timestamps are written by whichever
    /// container is running, and the queue's own append order is the only thing
    /// the fold can read that is guaranteed monotone.
    ///
    /// `None` for a [`Source::Items`] ledger, which has no queue and therefore
    /// no touch order. A file's modification time would be the obvious stand-in
    /// and is not usable: the run rewrites items files for reasons that have
    /// nothing to do with priority — a `merge` that changes one field, a
    /// checkpoint restore, a `git` checkout — so mtime would shuffle the section
    /// on events no reader can see. So an items ledger keeps recorded order
    /// under either [`super::spec::Order`], which [`ordered`] gets for free by
    /// sorting stably on a key that is equal for every one of its entries.
    pub(in crate::orchestrator) touched: Option<usize>,
}

impl Entry {
    /// A field's value, or the empty string.
    pub(in crate::orchestrator) fn get(&self, name: &str) -> &str {
        self.fields.get(name).map_or("", String::as_str)
    }

    /// The entry's status under `spec`, lowercased, or the empty string.
    pub(in crate::orchestrator) fn status(&self, spec: &LedgerSpec) -> String {
        spec.status_field()
            .map(|field| self.get(&field.name).trim().to_ascii_lowercase())
            .unwrap_or_default()
    }

    /// The one-line summary a row carries.
    pub(in crate::orchestrator) fn title(&self, spec: &LedgerSpec) -> &str {
        spec.title_field()
            .map_or("", |field| self.get(&field.name))
    }

    /// Every field the entry carries whole, for `read_ledger`.
    pub(in crate::orchestrator) fn full(&self) -> String {
        let mut out = format!("### `{}`\n", self.id);
        if !self.from.is_empty() {
            let _ = writeln!(out, "- recorded by: {}", self.from);
        }
        for (name, value) in &self.fields {
            let _ = writeln!(out, "- {name}: {}", value.trim());
        }
        out
    }
}

/// Every entry a ledger holds, with the faults found reading them.
#[derive(Clone, Debug, Default)]
pub(in crate::orchestrator) struct Entries {
    pub(in crate::orchestrator) entries: Vec<Entry>,
    pub(in crate::orchestrator) faults: Vec<String>,
}

/// Reads every entry `spec` declares a source for.
///
/// A [`Source::Derived`] ledger has no per-entry source this engine
/// understands — it is rendered by its own module — so it reads as empty here
/// and `read_ledger` serves its derived file instead.
pub(in crate::orchestrator) fn collect(workspace: &Path, spec: &LedgerSpec) -> Entries {
    let mut entries = match &spec.source {
        Source::Queue { path } => fold_queue(workspace, path),
        Source::Items { dir, block } => read_items(workspace, dir, block, spec),
        Source::Derived => Entries::default(),
    };
    check(&mut entries, spec);
    entries
}

/// Folds an append-only queue into current state.
///
/// A line that will not parse is skipped rather than failing the read, on the
/// board's reasoning: the append discipline makes a torn line unusual, and one
/// unreadable event must not cost the ledger every other entry on it.
fn fold_queue(workspace: &Path, path: &str) -> Entries {
    let mut out = Entries::default();
    let Ok(raw) = std::fs::read_to_string(workspace.join(path)) else {
        return out;
    };
    // Insertion order is the order ids were first seen, which is the order a
    // reader expects: the task added first is at the top until something moves
    // it. A map keyed by id would sort alphabetically, which is no order at all.
    let mut index: BTreeMap<String, usize> = BTreeMap::new();
    for (line_number, line) in raw.lines().enumerate() {
        if line.trim().is_empty() {
            continue;
        }
        let Ok(event) = serde_json::from_str::<Value>(line) else {
            out.faults.push(format!(
                "line {} of the queue could not be read as JSON and was skipped",
                line_number + 1
            ));
            continue;
        };
        let Some(id) = event.get("id").and_then(Value::as_str).map(str::trim) else {
            out.faults.push(format!(
                "line {} of the queue names no entry and was skipped",
                line_number + 1
            ));
            continue;
        };
        if id.is_empty() {
            continue;
        }
        let position = *index.entry(id.to_string()).or_insert_with(|| {
            out.entries.push(Entry {
                id: id.to_string(),
                ..Entry::default()
            });
            out.entries.len() - 1
        });
        let entry = &mut out.entries[position];
        // Every event, not only the first: the last one to name an id is what
        // `Order::Recent` reads, which is what lets a role re-prioritise an
        // existing task by recording against it.
        entry.touched = Some(line_number);
        if let Some(from) = event.get("from").and_then(Value::as_str) {
            entry.from = from.trim().to_string();
        }
        if let Some(fields) = event.get("fields").and_then(Value::as_object) {
            for (name, value) in fields {
                // A null clears a field, which is the one thing a merge cannot
                // express otherwise. Everything else is a set.
                match value {
                    Value::Null => {
                        entry.fields.remove(name);
                    }
                    Value::String(text) => {
                        entry.fields.insert(name.clone(), text.clone());
                    }
                    other => {
                        entry.fields.insert(name.clone(), other.to_string());
                    }
                }
            }
        }
    }
    out
}

/// Reads one file per entry, each carrying a fenced block.
fn read_items(workspace: &Path, dir: &str, block: &str, spec: &LedgerSpec) -> Entries {
    let mut out = Entries::default();
    let Ok(listing) = std::fs::read_dir(workspace.join(dir)) else {
        return out;
    };
    let mut paths: Vec<std::path::PathBuf> = listing
        .flatten()
        .map(|entry| entry.path())
        .filter(|path| path.is_file())
        .collect();
    paths.sort();
    for path in paths {
        let name = path.file_name().unwrap_or_default().to_string_lossy();
        if !name.ends_with(".md") || name == super::super::folder_index::INDEX_FILE {
            continue;
        }
        let Ok(text) = std::fs::read_to_string(&path) else {
            continue;
        };
        let slug = name.trim_end_matches(".md").to_string();
        let (blocks, unclosed) = super::super::claims::fenced(&text, block);
        if unclosed {
            out.faults
                .push(format!("`{slug}` has a `{block}` block that was never closed"));
        }
        let Some(body) = blocks.first() else {
            out.faults.push(format!(
                "`{slug}` carries no `{block}` block, so nothing on it can be read"
            ));
            continue;
        };
        let fields: BTreeMap<String, String> =
            super::super::claims::fields(body).into_iter().collect();
        // The id field wins when it is filled in; otherwise the filename is the
        // identity, which is what `threads` and `approaches` already do and
        // what makes a hand-written file work without ceremony.
        let id = spec
            .id_field()
            .and_then(|field| fields.get(&field.name))
            .map(|value| value.trim().to_string())
            .filter(|value| !value.is_empty())
            .unwrap_or(slug);
        out.entries.push(Entry {
            id,
            fields,
            from: String::new(),
            // No queue, so no touch order. See [`Entry::touched`] for why the
            // file's modification time is not the fallback.
            touched: None,
        });
    }
    out
}

/// Runs the declared checks, appending what they find to the fault list.
fn check(entries: &mut Entries, spec: &LedgerSpec) {
    let mut faults = Vec::new();
    for entry in &entries.entries {
        for declared in &spec.checks {
            match declared {
                Check::RequiredField => {
                    for field in spec.fields.iter().filter(|field| field.required) {
                        // The id is the entry's identity and lives *beside* the
                        // fields, not inside them: every queue event names it at
                        // the top level and an event without one is dropped
                        // before it reaches here. So looking for it in `fields`
                        // fails for every well-formed entry, and a spec that
                        // declares its id field required — as `tasks` does —
                        // reports each of its own rows unreadable. A live
                        // workspace had all eight of its open tasks under
                        // "Entries that could not be read" while the queue was
                        // perfectly valid, and the run could not see its own
                        // work.
                        let present = if field.role == super::spec::Role::Id {
                            !entry.id.trim().is_empty()
                        } else {
                            !entry.get(&field.name).trim().is_empty()
                        };
                        if !present {
                            faults.push(format!(
                                "`{}` has no `{}`, which this ledger requires",
                                entry.id, field.name
                            ));
                        }
                    }
                }
                Check::KnownStatus => {
                    let status = entry.status(spec);
                    if !status.is_empty() && !spec.knows_status(&status) {
                        faults.push(format!(
                            "`{}` is in status `{status}`, which this ledger does not declare",
                            entry.id
                        ));
                    }
                }
                Check::ClosedNeedsReason => {
                    let status = entry.status(spec);
                    if spec.status(&status).is_some_and(|declared| {
                        declared.needs_reason
                    }) && entry.get(REASON).trim().is_empty()
                    {
                        faults.push(format!(
                            "`{}` was closed as `{status}` with no `{REASON}` — a row that does \
                             not say why is worth nothing to whoever reads it next",
                            entry.id
                        ));
                    }
                }
            }
        }
    }
    entries.faults.extend(faults);
}

/// The field a closing status is expected to fill in.
///
/// One name across every ledger rather than a per-spec choice, because the
/// check above has to know it and a spec that could rename it would make the
/// check unwritable. *Why did this close* is the same question everywhere.
pub(in crate::orchestrator) const REASON: &str = "reason";

/// Renders the derived file every reader opens.
pub(in crate::orchestrator) fn render(spec: &LedgerSpec, entries: &Entries) -> String {
    let mut out = format!("# {}\n\n", spec.title);
    if !spec.purpose.is_empty() {
        let _ = writeln!(out, "{}\n", spec.purpose);
    }
    let _ = writeln!(
        out,
        "Derived from `{}` and rewritten on every write. Do not edit this file — the next write \
         re-derives it, and your edit is gone. Record into it with `record_entry` and close a row \
         with `close_entry`.\n",
        source_label(&spec.source)
    );
    if entries.entries.is_empty() {
        let _ = writeln!(out, "_Nothing recorded yet._");
    }
    for section in &spec.sections {
        append_section(&mut out, spec, entries, section);
    }
    append_faults(&mut out, spec, entries);
    out
}

fn source_label(source: &Source) -> String {
    match source {
        Source::Queue { path } => path.clone(),
        Source::Items { dir, .. } => dir.clone(),
        Source::Derived => "its own module".to_string(),
    }
}

/// Puts entries in the order a section, or a `read_ledger` call, asked for.
///
/// Ordering happens here rather than in [`collect`], so the fold keeps saying
/// one thing — first-seen order — and every reader picks its own view of it.
///
/// The sort is stable and keyed on [`Entry::touched`], which makes the items
/// case fall out rather than needing a branch: every one of its entries has the
/// same key, so a stable sort leaves them exactly as they were read.
pub(in crate::orchestrator) fn ordered<'a>(
    entries: &'a [Entry],
    order: super::spec::Order,
) -> Vec<&'a Entry> {
    let mut out: Vec<&Entry> = entries.iter().collect();
    if order == super::spec::Order::Recent {
        out.sort_by_key(|entry| std::cmp::Reverse(entry.touched.unwrap_or(0)));
    }
    out
}

fn append_section(out: &mut String, spec: &LedgerSpec, entries: &Entries, section: &super::spec::Section) {
    let sorted = ordered(&entries.entries, section.order);
    let matching = sorted.into_iter().filter(|entry| {
        section.statuses.is_empty()
            || section
                .statuses
                .iter()
                .any(|wanted| wanted.eq_ignore_ascii_case(&entry.status(spec)))
    });
    let (rows, dropped) = budget::listed(matching, section.cap, |rows, entry| {
        let title = entry.title(spec);
        if title.trim().is_empty() {
            let _ = writeln!(rows, "- `{}`", entry.id);
        } else {
            let _ = writeln!(
                rows,
                "- `{}` — {}",
                entry.id,
                truncate(title, budget::REASON_CHARS)
            );
        }
        // Every prose field the entry filled in, one indented line each. A row
        // that carried only its title would make `read_ledger` mandatory to
        // learn anything, and the point of the derived file is that a reader
        // can open it and be done.
        for field in spec.fields.iter().filter(|field| field.role == Role::Prose) {
            let value = entry.get(&field.name);
            if value.trim().is_empty() {
                continue;
            }
            let _ = writeln!(
                rows,
                "  - {}: {}",
                field.name,
                truncate(value, budget::REASON_CHARS)
            );
        }
        for field in spec.fields.iter().filter(|field| field.role == Role::Refs) {
            let value = entry.get(&field.name);
            if value.trim().is_empty() {
                continue;
            }
            let _ = writeln!(rows, "  - {}: {}", field.name, value.trim());
        }
    });
    if rows.is_empty() {
        return;
    }
    let _ = write!(out, "\n## {}\n\n", section.heading);
    if !section.blurb.is_empty() {
        let _ = write!(out, "{}\n\n", section.blurb);
    }
    out.push_str(&rows);
    out.push_str(&budget::elided(dropped, &source_label(&spec.source)));
}

fn append_faults(out: &mut String, spec: &LedgerSpec, entries: &Entries) {
    if entries.faults.is_empty() {
        return;
    }
    out.push_str(
        "\n## Entries that could not be read\n\nReported rather than dropped: an entry silently \
         discarded leaves the ledger reading as though it recorded something.\n\n",
    );
    let (rows, dropped) = budget::listed(&entries.faults, budget::MAX_LISTED, |rows, fault| {
        let _ = writeln!(rows, "- {}", truncate(fault, budget::REASON_CHARS));
    });
    out.push_str(&rows);
    out.push_str(&budget::elided(dropped, &source_label(&spec.source)));
}

/// Appends one event to a queue ledger.
///
/// # Errors
///
/// Returns an error when the ledger is not queue-backed, or when the queue
/// cannot be created or written.
pub(in crate::orchestrator) fn append(
    workspace: &Path,
    spec: &LedgerSpec,
    from: &str,
    id: &str,
    fields: &Map<String, Value>,
) -> Result<()> {
    let Source::Queue { path } = &spec.source else {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{}` is not an append-only ledger, so nothing can be appended to it",
            spec.slug
        )));
    };
    let target = workspace.join(path);
    if let Some(parent) = target.parent() {
        std::fs::create_dir_all(parent).map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to create the directory for `{path}`: {error}"
            ))
        })?;
    }
    let line = format!(
        "{}\n",
        json!({ "at": now_ms(), "from": from, "id": id, "fields": Value::Object(fields.clone()) })
    );
    let mut file = std::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(&target)
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to open `{path}`: {error}"))
        })?;
    // One `write_all` of one complete line. See the module documentation for
    // why this is what removes the need for a lock.
    file.write_all(line.as_bytes()).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to write to `{path}`: {error}"))
    })?;
    Ok(())
}

/// Merges `fields` into one entry's fenced block, creating the file if absent.
///
/// A merge rather than a rewrite, and the argument is
/// [`super::super::authoring`]'s: re-emitting a whole document to change one
/// field is token-heavy and the largest source of accidental regressions,
/// because a dropped line looks exactly like the document the author meant. A
/// merge that fails, fails loudly.
///
/// Everything outside the block is preserved — an items file is a note with a
/// block in it, and the prose around the block is the working record.
///
/// # Errors
///
/// Returns an error when the ledger is not items-backed, or when the file
/// cannot be read or written.
pub(in crate::orchestrator) fn merge(
    workspace: &Path,
    spec: &LedgerSpec,
    id: &str,
    fields: &Map<String, Value>,
) -> Result<String> {
    let Source::Items { dir, block } = &spec.source else {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{}` does not keep one file per entry, so there is no block to merge into",
            spec.slug
        )));
    };
    let relative = format!("{dir}/{id}.md");
    let target = workspace.join(&relative);
    if let Some(parent) = target.parent() {
        std::fs::create_dir_all(parent).map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to create the directory for `{relative}`: {error}"
            ))
        })?;
    }
    let existing = std::fs::read_to_string(&target).unwrap_or_default();
    let mut merged: BTreeMap<String, String> = super::super::claims::fenced(&existing, block)
        .0
        .first()
        .map(|body| super::super::claims::fields(body).into_iter().collect())
        .unwrap_or_default();
    for (name, value) in fields {
        match value {
            Value::Null => {
                merged.remove(name);
            }
            Value::String(text) => {
                merged.insert(name.clone(), text.clone());
            }
            other => {
                merged.insert(name.clone(), other.to_string());
            }
        }
    }
    let mut body = String::new();
    for (name, value) in &merged {
        // A newline inside a field would close the block early and silently
        // truncate everything after it, so it is folded to a space. The field
        // is one line by construction in every ledger that has one.
        let _ = writeln!(body, "{name}: {}", value.replace('\n', " ").trim());
    }
    let rendered = format!("```{block}\n{body}```");
    let updated = replace_block(&existing, block, &rendered, id);
    std::fs::write(&target, &updated).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to write `{relative}`: {error}"))
    })?;
    Ok(relative)
}

/// Swaps the first fenced `block` in `text` for `rendered`, or appends it.
fn replace_block(text: &str, block: &str, rendered: &str, id: &str) -> String {
    let opening = format!("```{block}");
    let Some(start) = text.find(&opening) else {
        if text.trim().is_empty() {
            return format!("# {id}\n\n{rendered}\n");
        }
        return format!("{}\n\n{rendered}\n", text.trim_end());
    };
    let after = start + opening.len();
    let end = text[after..]
        .find("\n```")
        .map_or(text.len(), |offset| after + offset + "\n```".len());
    format!("{}{rendered}{}", &text[..start], &text[end..])
}

/// Milliseconds since the epoch, or zero if the clock is before it.
fn now_ms() -> u64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map_or(0, |since| {
            u64::try_from(since.as_millis()).unwrap_or(u64::MAX)
        })
}

#[cfg(test)]
#[path = "engine_test.rs"]
mod test;
