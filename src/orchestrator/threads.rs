//! Threads: the library's topic axis, beside its arrival axis.
//!
//! `research/` folds by arrival. Ten originals fill `L0.0`, one note seals
//! them, and the seal is named for the batch. That is exactly right for
//! provenance — it is one-time, it never drifts, and every claim stays
//! traceable — and exactly wrong for retrieval. A reader asking *what do we
//! know about the pass rule* gets a seal covering whichever ten things arrived
//! together, and the answer is spread across three of them.
//!
//! One live workspace built the missing axis by hand. Under `research/` it
//! grew a `folds/` folder nobody designed, holding `game-core.md`,
//! `passes.md`, `counting-arithmetic.md`, and `deadends.md` — a run needing
//! topic-shaped notes badly enough to invent them outside the schema. This
//! module is that shape, made part of it.
//!
//! A thread is a direction of attack: the question it is chasing, the claims
//! it rests on, what is blocking it, and what to do next. Unlike a seal it is
//! live and may be rewritten as often as the direction changes; unlike the
//! arrival tree it is organised by what a reader wants rather than by when a
//! download happened. The two are complementary, and neither replaces the
//! other: the thread says what the run believes about a direction, and the
//! links in it reach the notes that establish it.
//!
//! `THREADS.md` is derived from the thread files the way `CLAIMS.md` is
//! derived from the notes, and for the same reason. It is what gets routed
//! into a prompt: a table of every direction the run is pursuing, what each
//! rests on, and which ones are dead — a dead end being a result the method
//! policy asks to be recorded, and the one thing a planner most needs so it
//! does not re-open it.

use std::collections::BTreeSet;
use std::fmt::Write as _;
use std::path::Path;

use super::claims::{Ledger, fenced, fields, identifiers};
use super::text::truncate;

/// Folder holding one file per direction of attack.
pub(super) const THREADS_DIR: &str = "research/threads";

/// The derived table, filed with the library it describes.
pub(super) const THREADS_PATH: &str = "research/THREADS.md";

/// Threads one table lists.
const MAX_ROWS: usize = 24;

/// Characters one rendered question is held to.
const QUESTION_CHARS: usize = 160;

/// Where a direction of attack currently stands.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
enum Stance {
    /// Being pursued now.
    #[default]
    Open,
    /// Waiting on something named in `blocked-by`.
    Blocked,
    /// Ruled out, with the reason recorded.
    ///
    /// A known dead end is a result, and a table that dropped these would let
    /// the next planner re-open a direction the run has already paid to close.
    Dead,
    /// Carried to its conclusion.
    Settled,
}

impl Stance {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("dead") || lowered.starts_with("ruled") {
            Self::Dead
        } else if lowered.starts_with("block") || lowered.starts_with("stuck") {
            Self::Blocked
        } else if lowered.starts_with("settled") || lowered.starts_with("done") {
            Self::Settled
        } else {
            Self::Open
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Open => "open",
            Self::Blocked => "**blocked**",
            Self::Dead => "dead",
            Self::Settled => "settled",
        }
    }
}

/// One direction of attack.
#[derive(Clone, Debug, Default)]
struct Thread {
    /// The file's stem, which is how a reader names the thread.
    slug: String,
    /// What this direction is trying to answer.
    question: String,
    /// Where it stands.
    stance: Stance,
    /// Claim ids it rests on.
    rests_on: Vec<String>,
    /// What is in the way, when it is blocked or dead.
    blocked_by: String,
    /// The next concrete step.
    next: String,
}

/// Every thread on disk, with the faults found reading them.
#[derive(Debug, Default)]
pub(super) struct Threads {
    threads: Vec<Thread>,
    faults: Vec<String>,
}

/// Reads every thread file under [`THREADS_DIR`].
pub(super) fn collect(workspace: &Path) -> Threads {
    let mut out = Threads::default();
    let Ok(entries) = std::fs::read_dir(workspace.join(THREADS_DIR)) else {
        return out;
    };
    let mut paths: Vec<std::path::PathBuf> = entries
        .flatten()
        .map(|entry| entry.path())
        .filter(|path| path.is_file())
        .collect();
    paths.sort();
    for path in paths {
        let name = path.file_name().unwrap_or_default().to_string_lossy();
        if !name.ends_with(".md") || name == super::folder_index::INDEX_FILE {
            continue;
        }
        let Ok(text) = std::fs::read_to_string(&path) else {
            continue;
        };
        let slug = name.trim_end_matches(".md").to_string();
        let (blocks, unclosed) = fenced(&text, "thread");
        if unclosed {
            out.faults
                .push(format!("`{slug}` has a thread block that was never closed"));
        }
        let Some(block) = blocks.first() else {
            out.faults.push(format!(
                "`{slug}` has no thread block, so nothing can say what it is chasing or what it \
                 rests on"
            ));
            continue;
        };
        let mut thread = Thread {
            slug: slug.clone(),
            ..Thread::default()
        };
        for (key, value) in fields(block) {
            match key.as_str() {
                "question" | "chasing" => thread.question = value,
                "status" | "stance" => thread.stance = Stance::parse(&value),
                "rests-on" | "claims" => thread.rests_on = identifiers(&value),
                "blocked-by" | "blocker" => thread.blocked_by = value,
                "next" | "next-step" => thread.next = value,
                _ => {}
            }
        }
        if thread.question.is_empty() {
            out.faults.push(format!(
                "`{slug}` names no question, so it is a note, not a thread"
            ));
        }
        out.threads.push(thread);
    }
    out
}

impl Threads {
    /// Renders the table routed into the roles that choose a direction.
    ///
    /// `ledger` is passed so a thread resting on a claim nobody wrote down is
    /// visible. A direction built on a belief that is not in the library is
    /// either resting on something unrecorded — which the next reader cannot
    /// check — or on a claim id that was misspelled, and both are worth one
    /// line here rather than a wrong turn later.
    pub(super) fn render(&self, ledger: &Ledger) -> String {
        let known: BTreeSet<String> = ledger.ids();
        let mut out = String::from(
            "# Threads — the directions this run is pursuing\n\n\
             Derived from the files under `research/threads/`, and rewritten whenever one of them \
             is written. Do not edit this file; the next write re-derives it. A thread is one \
             direction of attack: open `research/threads/<name>.md` to work inside it.\n\n\
             This is the library's topic axis. `research/L0…L2` folds by *arrival* and is sealed \
             once, which keeps provenance honest but scatters a subject across batches; a thread \
             gathers one subject and stays live. Dead threads are kept deliberately — a known \
             dead end is a result, and the reason it died is what stops the next attempt paying \
             for it again.\n\n",
        );
        if self.threads.is_empty() {
            out.push_str(
                "_No threads yet. Open one as soon as a direction has a question and a claim \
                 under it: `research/threads/<name>.md`, with a fenced `thread` block carrying \
                 `question`, `status`, `rests-on`, `blocked-by`, and `next` lines._\n",
            );
            self.append_faults(&mut out);
            return out;
        }
        out.push_str(
            "| Thread | Question | Status | Rests on | Next |\n| --- | --- | --- | --- | --- |\n",
        );
        for thread in self.threads.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "| [[{}]] | {} | {} | {} | {} |",
                thread.slug,
                cell(&truncate(&thread.question, QUESTION_CHARS)),
                thread.stance.label(),
                cell(&thread.rests_on.join(", ")),
                cell(&truncate(&thread.next, QUESTION_CHARS))
            );
        }
        if self.threads.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further threads not shown._",
                self.threads.len() - MAX_ROWS
            );
        }
        self.append_blocked(&mut out);
        self.append_unsupported(&mut out, &known);
        self.append_faults(&mut out);
        out
    }

    /// Spells out what each blocked or dead thread is waiting on.
    ///
    /// The blocker is the useful half. A row saying a direction is stuck tells
    /// a planner not to pick it; the sentence saying *what* would unstick it
    /// is what turns the same row into the next research request.
    fn append_blocked(&self, out: &mut String) {
        let mut rows = String::new();
        for thread in self
            .threads
            .iter()
            .filter(|thread| matches!(thread.stance, Stance::Blocked | Stance::Dead))
        {
            let reason = if thread.blocked_by.is_empty() {
                "_no blocker recorded — say what would unstick it, or the row is only a mood_"
            } else {
                thread.blocked_by.as_str()
            };
            let _ = writeln!(
                rows,
                "- [[{}]] ({}): {reason}",
                thread.slug,
                thread.stance.label()
            );
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## What is in the way\n\nEach blocked or dead thread and what would move it. A \
             blocker stated precisely is the next research request; one left blank is a mood.\n\n",
        );
        out.push_str(&rows);
    }

    /// Lists threads resting on claims that are not in the ledger.
    fn append_unsupported(&self, out: &mut String, known: &BTreeSet<String>) {
        let mut rows = String::new();
        for thread in &self.threads {
            let missing: Vec<&String> = thread
                .rests_on
                .iter()
                .filter(|id| !known.contains(*id))
                .collect();
            if missing.is_empty() {
                continue;
            }
            let _ = writeln!(
                rows,
                "- [[{}]] rests on {}, which no claim block on disk establishes",
                thread.slug,
                missing
                    .iter()
                    .map(|id| format!("`{id}`"))
                    .collect::<Vec<_>>()
                    .join(", ")
            );
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Resting on nothing recorded\n\nEither the belief was never written down as a \
             claim — in which case nobody downstream can check it — or the id is misspelled.\n\n",
        );
        out.push_str(&rows);
    }

    fn append_faults(&self, out: &mut String) {
        if self.faults.is_empty() {
            return;
        }
        out.push_str("\n## Threads that could not be read\n\n");
        for fault in &self.faults {
            let _ = writeln!(out, "- {fault}");
        }
    }
}

/// Re-derives the thread table and rewrites [`THREADS_PATH`].
///
/// Best effort, like the claim ledger: a failed refresh must not fail the
/// write that succeeded.
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) {
    let threads = collect(documents.root());
    let ledger = super::claims::collect(documents.root());
    let _ = documents
        .write_runtime(THREADS_PATH, &threads.render(&ledger))
        .await;
    super::folder_index::record_description(
        documents,
        THREADS_PATH,
        "Derived: every direction of attack under research/threads/, what each rests on, and why \
         the dead ones died. Rewritten on every research write; do not edit.",
    )
    .await;
}

/// Whether a written path is a thread file the table is derived from.
pub(super) fn is_thread(relative: &str) -> bool {
    relative.starts_with(&format!("{THREADS_DIR}/"))
        && super::claims::is_markdown(relative)
        && !relative.ends_with(super::folder_index::INDEX_FILE)
}

fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
}

#[cfg(test)]
#[path = "threads_test.rs"]
mod test;
