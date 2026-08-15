//! Turns a hand-written `TASKS.md` into the task ledger's queue.
//!
//! `TASKS.md` used to be free-form Markdown that two roles rewrote whole. It is
//! derived now, which means the first write to the ledger would overwrite
//! whatever a live workspace already has there — so the existing file has to be
//! read into the queue first, and this is what does it.
//!
//! It is a one-shot host-side migration rather than a runtime step. A workspace
//! is migrated once, by somebody who can look at the result, and a conversion
//! that ran automatically at container start would be a silent rewrite of the
//! file it was converting.
//!
//! ```sh
//! cargo run --example import_tasks -- workspace/conjectures/gilbreath
//! cargo run --example import_tasks -- workspace/conjectures/gilbreath --write
//! ```
//!
//! Without `--write` it prints what it would record and touches nothing, which
//! is the only safe default for something that reads prose and guesses.
//!
//! # What it keeps, and what it deliberately does not
//!
//! Checklist items become tasks: `- [ ]` open, `- [x]` done. A `## Do not do`
//! section becomes dropped entries carrying their reason, because that section
//! is the ledger's `Do not do` list written by hand — the agents built it
//! themselves once the rewrites started deleting their finished rows.
//!
//! Everything else — `## Background`, the thread summaries, the prose between
//! sections — is **not** imported and not deleted. It is not tasks. It belongs
//! in `CONTEXT.md` and the ledgers that already carry it, and moving it is a
//! judgement about the mathematics that a parser has no business making. The
//! run's own `TASKS.md` is left on disk under a new name so nothing is lost.

use std::collections::BTreeSet;
use std::fmt::Write as _;
use std::path::Path;

/// One bullet as it was read off the page: whether it was ticked, its text,
/// and whether it was a `- [ ]` checklist item rather than a plain bullet.
///
/// The third field is what separates a task from prose. `## Background` and
/// `### Threads` are plain lists of established results and open directions,
/// and importing either as an open task would fill the ledger with rows nobody
/// can finish.
type Bullet = (bool, String, bool);

/// A `## heading` and the bullets under it.
type Block = (Option<String>, Vec<Bullet>);

/// One task read out of the old file.
struct Task {
    id: String,
    title: String,
    detail: String,
    status: &'static str,
    reason: String,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut arguments = std::env::args().skip(1);
    let workspace = arguments
        .next()
        .ok_or("usage: import_tasks <workspace> [--write]")?;
    let write = arguments.any(|flag| flag == "--write");
    let root = Path::new(&workspace);
    if !root.is_dir() {
        return Err(format!("workspace `{workspace}` is not a directory").into());
    }

    let source = root.join("TASKS.md");
    let text = std::fs::read_to_string(&source)
        .map_err(|error| format!("could not read {}: {error}", source.display()))?;
    let tasks = parse(&text);
    if tasks.is_empty() {
        println!("nothing that looks like a task in {}", source.display());
        return Ok(());
    }

    let mut queue = String::new();
    for task in &tasks {
        let mut fields = serde_json::Map::new();
        // The id lives inside `fields`, not beside it. The tasks ledger declares
        // a field named `id` with role `id` and requires it, so an entry that
        // carries the id only at the top level parses as an entry with no id at
        // all — and the engine reports every such row under "Entries that could
        // not be read" rather than dropping it. A live migrated workspace put
        // all eight of its open tasks there, so the run could not see its own
        // queue while the file looked perfectly well-formed.
        fields.insert("id".into(), task.id.clone().into());
        fields.insert("title".into(), task.title.clone().into());
        if !task.detail.is_empty() {
            fields.insert("detail".into(), task.detail.clone().into());
        }
        if !task.reason.is_empty() {
            fields.insert("reason".into(), task.reason.clone().into());
        }
        fields.insert("status".into(), task.status.into());
        let _ = writeln!(
            queue,
            "{}",
            serde_json::json!({
                // Zero rather than a clock reading: these did not happen now,
                // and stamping them with the migration's time would make the
                // ledger claim a history it does not have.
                "at": 0,
                "from": "import_tasks",
                "id": task.id,
                "fields": serde_json::Value::Object(fields),
            })
        );
    }

    let (open, done, dropped) = counts(&tasks);
    println!(
        "{} task(s) read from {}: {open} open, {done} done, {dropped} dropped",
        tasks.len(),
        source.display()
    );
    for task in &tasks {
        println!("  [{}] {} — {}", task.status, task.id, task.title);
    }

    if !write {
        println!(
            "\nnothing written. Re-run with --write to record these into \
             config/tasks.jsonl and move the old file aside."
        );
        return Ok(());
    }

    let target = root.join("config/tasks.jsonl");
    if target.exists() {
        return Err(format!(
            "{} already exists. This migration runs once; importing again would duplicate \
             every row.",
            target.display()
        )
        .into());
    }
    if let Some(parent) = target.parent() {
        std::fs::create_dir_all(parent)?;
    }
    std::fs::write(&target, queue)?;

    // Moved rather than deleted. The prose this did not import — the
    // background, the thread summaries — is still in it, and somebody has to
    // decide where that belongs.
    let kept = root.join("TASKS.imported.md");
    std::fs::rename(&source, &kept)?;

    // Rendered *after* the rename, and the order is the whole of it: the
    // ledger derives into `TASKS.md`, which is the same path the old file is
    // being moved off. Rendering first wrote the derived file and then the
    // rename carried it away, leaving the workspace with no task list at all —
    // and no error, because both operations succeeded.
    //
    // The render reads the queue rather than the old file, so nothing is lost
    // by doing it second.
    match math_agent::render_ledger(root, "tasks") {
        Ok((derived, rendered)) => std::fs::write(root.join(&derived), rendered)
            .map_err(|error| format!("could not write {derived}: {error}"))?,
        Err(error) => return Err(format!("could not render the task ledger: {error}").into()),
    }
    println!(
        "\nwrote {}, re-derived TASKS.md from it, and moved the old file to {}.\nWhat was not \
         imported — background, threads, prose — is still in it and belongs in CONTEXT.md or a \
         ledger of its own.",
        target.display(),
        kept.display()
    );
    Ok(())
}

fn counts(tasks: &[Task]) -> (usize, usize, usize) {
    let count = |wanted: &str| tasks.iter().filter(|task| task.status == wanted).count();
    (count("open"), count("done"), count("dropped"))
}

/// Reads checklist items and the `Do not do` section out of a `TASKS.md`.
fn parse(text: &str) -> Vec<Task> {
    let mut tasks: Vec<Task> = Vec::new();
    let mut seen: BTreeSet<String> = BTreeSet::new();
    let mut in_prohibitions = false;

    for block in blocks(text) {
        let heading = block.0;
        if let Some(heading) = heading {
            let lowered = heading.to_ascii_lowercase();
            in_prohibitions = lowered.contains("do not do") || lowered.contains("don't do");
        }
        for (marker, body, checklist) in block.1 {
            // Outside a prohibitions section, only a checklist item is a task.
            if !checklist && !in_prohibitions {
                continue;
            }
            let (status, title, detail, reason) = if in_prohibitions {
                // A prohibition's whole text is its reason: "do not queue a 4e9
                // sieve run (Directive 36 stands — empirical route at ceiling)"
                // is a dropped task and the parenthesis is why.
                (
                    "dropped",
                    first_sentence(&clean(&body)),
                    String::new(),
                    body.clone(),
                )
            } else if marker {
                (
                    "done",
                    first_sentence(&clean(&body)),
                    body.clone(),
                    String::from(
                        "imported from a hand-written TASKS.md, which recorded it as finished but not \
                     what came of it",
                    ),
                )
            } else {
                (
                    "open",
                    first_sentence(&clean(&body)),
                    body.clone(),
                    String::new(),
                )
            };
            let title = strip_enumeration(&strip_markup(&title));
            if title.is_empty() {
                continue;
            }
            let mut id = slug(&title);
            // Two prohibitions can open with the same words; a duplicate id
            // would silently merge them into one row.
            let mut suffix = 2;
            while !seen.insert(id.clone()) {
                id = format!("{}-{suffix}", slug(&title));
                suffix += 1;
            }
            tasks.push(Task {
                id,
                title,
                detail: strip_markup(&detail),
                status,
                reason: strip_markup(&reason),
            });
        }
    }
    tasks
}

/// Splits the file into `(heading, items)`, where an item is
/// `(done, text, was_a_checklist_item)`.
///
/// Continuation lines are folded into the item above them, because a checklist
/// entry in these files routinely runs to a paragraph and the first line alone
/// is usually half a sentence.
fn blocks(text: &str) -> Vec<Block> {
    let mut out: Vec<Block> = vec![(None, Vec::new())];
    for line in text.lines() {
        let trimmed = line.trim();
        if trimmed.starts_with('#') {
            out.push((
                Some(trimmed.trim_start_matches('#').trim().to_string()),
                Vec::new(),
            ));
            continue;
        }
        let item = trimmed
            .strip_prefix("- [ ]")
            .map(|rest| (false, rest))
            .or_else(|| trimmed.strip_prefix("- [x]").map(|rest| (true, rest)))
            .or_else(|| trimmed.strip_prefix("- [X]").map(|rest| (true, rest)))
            // A plain bullet is only a task inside a prohibitions section,
            // which is written as a list rather than a checklist. Everywhere
            // else a plain bullet is prose — `## Background` is a list of
            // established results and `### Threads` a list of directions, and
            // importing either as an open task would fill the ledger with
            // things nobody can finish. Marked here and filtered in `parse`,
            // which is the pass that knows what section it is in.
            .or_else(|| trimmed.strip_prefix("- ").map(|rest| (false, rest)))
            .map(|(done, rest)| (done, rest, trimmed.starts_with("- [")));
        if let Some((done, rest, checklist)) = item {
            let Some(block) = out.last_mut() else {
                continue;
            };
            block.1.push((done, rest.trim().to_string(), checklist));
            continue;
        }
        // A continuation: indented, or simply the next line of a paragraph.
        if trimmed.is_empty() {
            continue;
        }
        if let Some(block) = out.last_mut()
            && let Some(previous) = block.1.last_mut()
            && (line.starts_with(' ') || line.starts_with('\t'))
        {
            previous.1.push(' ');
            previous.1.push_str(trimmed);
        }
    }
    out
}

/// Markup and enumeration removed, ready for a sentence to be cut out of it.
fn clean(text: &str) -> String {
    strip_enumeration(&strip_markup(text))
}

/// Removes a leading `1.` / `**3.**` enumeration from a title.
///
/// These files number their checklist items inside the bullet, so the first
/// "sentence" of `**1. Write the proof.** …` is `**1`, and every item in a
/// section would end up titled by its own ordinal — and sharing an id with the
/// item of the same number in the section above it.
fn strip_enumeration(title: &str) -> String {
    let trimmed = title.trim_start();
    let digits: String = trimmed.chars().take_while(char::is_ascii_digit).collect();
    if digits.is_empty() {
        return trimmed.to_string();
    }
    let rest = trimmed[digits.len()..].trim_start();
    rest.strip_prefix('.')
        .or_else(|| rest.strip_prefix(')'))
        .map_or_else(|| trimmed.to_string(), |rest| rest.trim_start().to_string())
}

/// The leading sentence, which is what a one-line title wants.
fn first_sentence(text: &str) -> String {
    let cut = text
        .find(". ")
        .map_or(text.len(), |offset| offset + 1)
        .min(160);
    let mut head: String = text.chars().take(cut).collect();
    if head.len() < text.len() {
        head = head.trim_end_matches(['.', ' ']).to_string();
    }
    head
}

/// Removes the Markdown a title should not carry into a table cell.
fn strip_markup(text: &str) -> String {
    text.replace("**", "")
        .replace('`', "")
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")
}

/// A stable id from a title: lowercase words joined by hyphens.
fn slug(title: &str) -> String {
    let mut out = String::new();
    let mut hyphen = true;
    for character in title.chars() {
        if character.is_ascii_alphanumeric() {
            out.push(character.to_ascii_lowercase());
            hyphen = false;
        } else if !hyphen {
            out.push('-');
            hyphen = true;
        }
        if out.len() >= 48 {
            break;
        }
    }
    out.trim_matches('-').to_string()
}
