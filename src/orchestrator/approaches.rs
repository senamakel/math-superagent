//! Approaches: the run's record of what it has tried to *think* of, beside
//! what it has tried to compute.
//!
//! A thread is a direction already anchored to the library: it has a question
//! and it rests on claim ids. An approach is what comes before that — a
//! candidate reformulation somebody proposed, which may turn out to be a known
//! theory, a dead end, or the thing that works. The distinction matters because
//! the interesting failure is the one that leaves no trace: the inventor
//! proposed a generating-function reformulation at attempt three, nothing wrote
//! it down, and at attempt six it proposed the same thing in different words.
//!
//! Before this module the inventor's output went into one prose field on the
//! solution state and was gone by the next attempt. Nothing on disk said what
//! had been considered, nothing said why a candidate died, and the only guard
//! against re-proposing a dead idea was whether a similarity search happened to
//! surface it. A refuted approach with its reason attached is the cheapest
//! thing the run owns: it costs one file and it saves a whole diversify.
//!
//! `APPROACHES.md` is derived from the approach files exactly as `THREADS.md`
//! is derived from the thread files, and for the same reason — a table an agent
//! edits is a table that disagrees with its sources.
//!
//! The stances form a life cycle rather than a status flag. `proposed` is an
//! idea nobody has checked; `grounded` is one the literature backs, with the
//! sources named; `refuted` is one the literature or the mathematics closed;
//! `adopted` is the one the run is now pursuing; `spent` is one that was
//! adopted, was carried out, and did not arrive. Keeping `refuted` and `spent`
//! visible is the point of the file.

use std::fmt::Write as _;
use std::path::Path;

use super::claims::{fenced, fields, references};
use super::text::truncate;

/// Folder holding one file per candidate line of attack.
pub(super) const APPROACHES_DIR: &str = "research/approaches";

/// The derived table, filed with the library it describes.
pub(super) const APPROACHES_PATH: &str = "research/APPROACHES.md";

/// Approaches one table lists.
const MAX_ROWS: usize = 24;

/// Characters one rendered field is held to.
const FIELD_CHARS: usize = 160;

/// Where a candidate line of attack currently stands.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub(super) enum Stance {
    /// Named, and nobody has checked it against the literature yet.
    #[default]
    Proposed,
    /// The literature backs it, and `precedent` says where.
    Grounded,
    /// Closed, with the reason in `killed-by`.
    ///
    /// Retained and rendered for the same reason a dead thread is: a closed
    /// line of attack is a result, and the reason it closed is the only thing
    /// that stops the next inventor paying for it again.
    Refuted,
    /// The line of attack the run is pursuing now.
    Adopted,
    /// Adopted, carried out, and it did not arrive.
    Spent,
}

impl Stance {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("refut")
            || lowered.starts_with("dead")
            || lowered.starts_with("ruled")
        {
            Self::Refuted
        } else if lowered.starts_with("adopt") || lowered.starts_with("chosen") {
            Self::Adopted
        } else if lowered.starts_with("spent") || lowered.starts_with("exhaust") {
            Self::Spent
        } else if lowered.starts_with("ground") || lowered.starts_with("known") {
            Self::Grounded
        } else {
            Self::Proposed
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Proposed => "proposed",
            Self::Grounded => "grounded",
            Self::Refuted => "refuted",
            Self::Adopted => "**adopted**",
            Self::Spent => "spent",
        }
    }

    /// Whether this stance closes the approach.
    ///
    /// A closed approach is what the inventor must not re-propose, so the
    /// dossier and the table both need to pick them out.
    pub(super) fn is_closed(self) -> bool {
        matches!(self, Self::Refuted | Self::Spent)
    }
}

/// One candidate line of attack.
#[derive(Clone, Debug, Default)]
pub(super) struct Approach {
    /// The file's stem, which is how a reader names the approach.
    pub(super) slug: String,
    /// The reformulation, named in mathematics rather than described.
    idea: String,
    /// Why this problem's structure suits it.
    mechanism: String,
    /// Where it stands.
    pub(super) stance: Stance,
    /// Source URLs and claim ids the literature check turned up.
    ///
    /// Empty means nobody has checked, which is a different statement from
    /// "nothing was found" — and keeping the two distinguishable is most of
    /// why this field exists.
    precedent: Vec<String>,
    /// The concrete first move.
    first_step: String,
    /// Why it is refuted or spent.
    killed_by: String,
}

/// Every approach on disk, with the faults found reading them.
#[derive(Debug, Default)]
pub(super) struct Approaches {
    approaches: Vec<Approach>,
    faults: Vec<String>,
}

impl Approaches {
    /// The approaches that are closed, newest last, for the dossier.
    pub(super) fn closed(&self) -> impl Iterator<Item = &Approach> {
        self.approaches
            .iter()
            .filter(|approach| approach.stance.is_closed())
    }
}

/// Reads every approach file under [`APPROACHES_DIR`].
pub(super) fn collect(workspace: &Path) -> Approaches {
    let mut out = Approaches::default();
    let Ok(entries) = std::fs::read_dir(workspace.join(APPROACHES_DIR)) else {
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
        let (blocks, unclosed) = fenced(&text, "approach");
        if unclosed {
            out.faults.push(format!(
                "`{slug}` has an approach block that was never closed"
            ));
        }
        let Some(block) = blocks.first() else {
            out.faults.push(format!(
                "`{slug}` has no approach block, so nothing can say what the idea is or whether \
                 anyone has checked it"
            ));
            continue;
        };
        let mut approach = Approach {
            slug: slug.clone(),
            ..Approach::default()
        };
        for (key, value) in fields(block) {
            match key.as_str() {
                "idea" | "reformulation" => approach.idea = value,
                "mechanism" | "why" => approach.mechanism = value,
                "status" | "stance" => approach.stance = Stance::parse(&value),
                "precedent" | "sources" => approach.precedent = references(&value),
                "first-step" | "next" => approach.first_step = value,
                "killed-by" | "refuted-by" => approach.killed_by = value,
                _ => {}
            }
        }
        if approach.idea.is_empty() {
            out.faults.push(format!(
                "`{slug}` names no idea, so it is a note, not an approach"
            ));
        }
        out.approaches.push(approach);
    }
    out
}

impl Approaches {
    /// Renders the table routed into the roles that choose a formulation.
    pub(super) fn render(&self) -> String {
        let mut out = String::from(
            "# Approaches — the lines of attack this run has considered\n\n\
             Derived from the files under `research/approaches/`, and rewritten whenever one of \
             them is written. Do not edit this file; the next write re-derives it. One approach is \
             one candidate reformulation: open `research/approaches/<name>.md` to work on it.\n\n\
             An approach is what comes *before* a thread. A thread already has a question and \
             rests on claims; an approach is the idea that might become one, and it carries \
             whether anybody has checked it against the literature yet. `precedent` empty means \
             unchecked, which is not the same as nothing having been found.\n\n\
             Refuted and spent approaches are kept deliberately. Proposing again what this run \
             already closed is the one failure the inventor exists to avoid, and the reason it \
             closed is the only thing that prevents it.\n\n",
        );
        if self.approaches.is_empty() {
            out.push_str(
                "_No approaches yet. Record one as soon as a line of attack is named: \
                 `research/approaches/<name>.md`, with a fenced `approach` block carrying `idea`, \
                 `mechanism`, `status`, `precedent`, `first-step`, and `killed-by` lines._\n",
            );
            self.append_faults(&mut out);
            return out;
        }
        out.push_str(
            "| Approach | Idea | Status | Precedent | First step |\n\
             | --- | --- | --- | --- | --- |\n",
        );
        for approach in self.approaches.iter().take(MAX_ROWS) {
            let precedent = if approach.precedent.is_empty() {
                "_unchecked_".to_string()
            } else {
                approach.precedent.join(", ")
            };
            let _ = writeln!(
                out,
                "| [[{}]] | {} | {} | {} | {} |",
                approach.slug,
                cell(&truncate(&approach.idea, FIELD_CHARS)),
                approach.stance.label(),
                cell(&truncate(&precedent, FIELD_CHARS)),
                cell(&truncate(&approach.first_step, FIELD_CHARS))
            );
        }
        if self.approaches.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further approaches not shown._",
                self.approaches.len() - MAX_ROWS
            );
        }
        self.append_closed(&mut out);
        self.append_unchecked(&mut out);
        self.append_faults(&mut out);
        out
    }

    /// Spells out why each closed approach closed.
    ///
    /// The reason is the useful half. A row saying an idea is refuted stops it
    /// being picked; the sentence saying *what* refuted it is what stops the
    /// same idea arriving next time under a different name.
    fn append_closed(&self, out: &mut String) {
        let mut rows = String::new();
        for approach in self.closed() {
            let reason = if approach.killed_by.is_empty() {
                "_no reason recorded — say what closed it, or the next inventor will propose it \
                 again_"
            } else {
                approach.killed_by.as_str()
            };
            let _ = writeln!(
                rows,
                "- [[{}]] ({}): {reason}",
                approach.slug,
                approach.stance.label()
            );
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## What closed, and why\n\nDo not propose these again. A reason stated precisely is \
             what makes that possible; one left blank makes this row worthless.\n\n",
        );
        out.push_str(&rows);
    }

    /// Lists approaches nobody has taken to the literature.
    ///
    /// An unchecked idea is not a criticism — every approach starts there — but
    /// a table full of them says the run is inventing without grounding, which
    /// is the failure mode opposite to the one it usually has.
    fn append_unchecked(&self, out: &mut String) {
        let mut rows = String::new();
        for approach in self
            .approaches
            .iter()
            .filter(|approach| approach.precedent.is_empty() && !approach.stance.is_closed())
        {
            let mechanism = if approach.mechanism.is_empty() {
                "_no mechanism stated — say why this problem's structure suits it_"
            } else {
                approach.mechanism.as_str()
            };
            let _ = writeln!(rows, "- [[{}]]: {mechanism}", approach.slug);
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Not yet taken to the literature\n\nNobody has checked whether these are known \
             theory. Grounding one is cheaper than pursuing it: a named theorem arrives with its \
             hypotheses, and a reformulation somebody already tried arrives with the reason it \
             failed.\n\n",
        );
        out.push_str(&rows);
    }

    fn append_faults(&self, out: &mut String) {
        if self.faults.is_empty() {
            return;
        }
        out.push_str("\n## Approaches that could not be read\n\n");
        for fault in &self.faults {
            let _ = writeln!(out, "- {fault}");
        }
    }
}

impl Approach {
    /// Renders one approach for the dossier, in full rather than as a row.
    ///
    /// The table scatters an approach across a row and up to two sections
    /// below it, and truncates every field in the row. That is right for a
    /// file somebody scans. It is wrong for the dossier, where a role is being
    /// handed the closed approaches precisely so it does not repeat one: there
    /// the idea and the reason it died need to arrive whole, together.
    pub(super) fn full(&self) -> String {
        let mut out = format!("### {} ({})\n", self.slug, self.stance.label());
        for (label, value) in [
            ("Idea", self.idea.as_str()),
            ("Mechanism", self.mechanism.as_str()),
            ("First step", self.first_step.as_str()),
            ("Closed by", self.killed_by.as_str()),
        ] {
            if !value.trim().is_empty() {
                let _ = writeln!(out, "- {label}: {}", value.trim());
            }
        }
        if !self.precedent.is_empty() {
            let _ = writeln!(out, "- Precedent: {}", self.precedent.join(", "));
        }
        out
    }
}

/// Re-derives the approach table and rewrites [`APPROACHES_PATH`].
///
/// Best effort, like the claim ledger and the thread table: a failed refresh
/// must not fail the write that succeeded.
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) {
    let approaches = collect(documents.root());
    let _ = documents
        .write_runtime(APPROACHES_PATH, &approaches.render())
        .await;
    super::folder_index::record_description(
        documents,
        APPROACHES_PATH,
        "Derived: every line of attack this run has considered, whether the literature backs it, \
         and why the closed ones closed. Rewritten on every approach write; do not edit.",
    )
    .await;
}

/// Whether a written path is an approach file the table is derived from.
pub(super) fn is_approach(relative: &str) -> bool {
    relative.starts_with(&format!("{APPROACHES_DIR}/"))
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
#[path = "approaches_test.rs"]
mod test;
