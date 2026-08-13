//! Backward reasoning: what would *suffice* to prove the goal, beside what the
//! run has been trying to compute.
//!
//! Every reasoning role in this runtime pushes forward. The solver attempts the
//! problem from what it holds, the inventor proposes a different route when the
//! attempts stall, the pattern agent extrapolates from numbers already
//! computed. None of them ever states the proposition the run is actually
//! trying to reach and asks what would be enough to get there.
//!
//! The cost of that is on disk. A live Gilbreath workspace contains exactly
//! this reasoning — the conjecture reduced to whether (2,4)-events arrive fast
//! enough that a sum never falls behind — and it took sixteen operator
//! directives to produce, because nothing in the runtime would have produced it
//! alone. The opposite failure is the one the loop walks into by itself: an
//! investigation reports genuine progress every attempt, verifies more and more
//! data, and spends its whole budget having never written down what a proof
//! would consist of.
//!
//! A skeleton is that missing statement. It carries the goal, the lemmas that
//! would imply it, and the inference that combines them — and then one gap per
//! lemma nobody has proved yet, each with a first move somebody could make
//! today. A gap is the unit that matters: it is what the forward loop attacks,
//! and it is why this file holds two kinds of block rather than one. A `gaps:`
//! list inside a single block cannot carry per-gap status, cannot say which
//! claim discharged which lemma, and gives the control that stops a role
//! restating a closed gap nothing to compare.
//!
//! `BACKWARD.md` is derived from the skeleton files exactly as `APPROACHES.md`
//! is derived from the approach files, and for the same reason — a table an
//! agent edits is a table that disagrees with its sources.
//!
//! This is not the approach ledger under another name. An approach is a *route*
//! — a reformulation that might get the run there. A skeleton is a
//! *decomposition* — the goal itself, broken into propositions that are
//! individually attackable. The inventor asks what else could get us there; the
//! reducer asks what would be enough. A run that is going well needs the second
//! question as much as a stuck one does, which is why nothing here is gated on
//! being stuck.

use std::collections::BTreeSet;
use std::fmt::Write as _;
use std::path::Path;

use super::claims::{Ledger, fenced, fields, identifiers};
use super::text::truncate;

/// Folder holding one file per proof skeleton.
pub(super) const BACKWARD_DIR: &str = "research/backward";

/// The derived table, filed with the library it describes.
pub(super) const BACKWARD_PATH: &str = "research/BACKWARD.md";

/// Skeletons one table lists.
const MAX_ROWS: usize = 24;

/// Characters one rendered field is held to.
const FIELD_CHARS: usize = 160;

/// Where a proof skeleton currently stands.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, PartialOrd, Ord)]
pub(super) enum Stance {
    /// Written down, and nothing is attacking any of its gaps.
    #[default]
    Sketched,
    /// At least one gap has a thread; the forward loop is on it.
    Live,
    /// Every gap is discharged, so the goal follows.
    ///
    /// Deliberately not closed. A discharged reduction is the most valuable
    /// thing in this file and the one a later reader most wants to find, which
    /// is the opposite of an approach that was spent.
    Discharged,
    /// The inference is wrong: the lemmas do not imply the goal, or one of them
    /// is false. `killed-by` says which.
    Broken,
    /// The gaps were attacked and it did not arrive.
    Spent,
}

impl Stance {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("broken") || lowered.starts_with("wrong") {
            Self::Broken
        } else if lowered.starts_with("spent") || lowered.starts_with("exhaust") {
            Self::Spent
        } else if lowered.starts_with("discharg") || lowered.starts_with("complete") {
            Self::Discharged
        } else if lowered.starts_with("live") || lowered.starts_with("active") {
            Self::Live
        } else {
            Self::Sketched
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Sketched => "sketched",
            Self::Live => "live",
            Self::Discharged => "**discharged**",
            Self::Broken => "broken",
            Self::Spent => "spent",
        }
    }

    /// Whether this stance closes the skeleton.
    ///
    /// A closed skeleton is what the reducer must not sketch again, so the
    /// dossier and the table both need to pick them out.
    pub(super) fn is_closed(self) -> bool {
        matches!(self, Self::Broken | Self::Spent)
    }
}

/// Where one lemma stands.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, PartialOrd, Ord)]
pub(super) enum GapStance {
    /// Nobody has proved it.
    #[default]
    Open,
    /// Proved, or already established, with `discharged-by` saying where.
    Discharged,
    /// False. The skeleton resting on it is `broken`, not merely stalled.
    Refuted,
}

impl GapStance {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("discharg") || lowered.starts_with("closed") {
            Self::Discharged
        } else if lowered.starts_with("refut") || lowered.starts_with("false") {
            Self::Refuted
        } else {
            Self::Open
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Open => "open",
            Self::Discharged => "discharged",
            Self::Refuted => "refuted",
        }
    }
}

/// One lemma the skeleton needs and does not have.
#[derive(Clone, Debug, Default)]
pub(super) struct Gap {
    /// The skeleton this gap belongs to, so a briefing can name its source.
    pub(super) skeleton: String,
    /// A stable name, which is what makes "already discharged" computable.
    pub(super) id: String,
    /// The statement that has to be proved, in mathematics.
    pub(super) lemma: String,
    /// Where it stands.
    pub(super) stance: GapStance,
    /// The claim id or note path that closed it.
    discharged_by: String,
    /// The thread attacking it, when the run has opened one.
    thread: String,
    /// The first concrete move a forward attempt could make today.
    pub(super) next: String,
}

/// One proof skeleton: a goal, the lemmas that would imply it, and the gaps.
#[derive(Clone, Debug, Default)]
pub(super) struct Skeleton {
    /// The file's stem, which is how a reader names the skeleton.
    pub(super) slug: String,
    /// The proposition this file is a proof skeleton of.
    goal: String,
    /// How the lemmas combine to give the goal — the inference itself.
    ///
    /// The load-bearing field. The failure mode of any decomposition is three
    /// attractive lemmas that do not recombine into the goal, and a file
    /// without this reads like progress while being none.
    implies: String,
    /// Where it stands.
    pub(super) stance: Stance,
    /// Claim ids the reduction takes as already established.
    rests_on: Vec<String>,
    /// Why it is broken or spent.
    killed_by: String,
    /// The lemmas, open and closed alike.
    gaps: Vec<Gap>,
}

impl Skeleton {
    /// The gaps nobody has closed.
    fn open(&self) -> impl Iterator<Item = &Gap> {
        self.gaps
            .iter()
            .filter(|gap| gap.stance == GapStance::Open)
    }
}

/// Every skeleton on disk, with the faults found reading them.
#[derive(Debug, Default)]
pub(super) struct Skeletons {
    skeletons: Vec<Skeleton>,
    faults: Vec<String>,
}

impl Skeletons {
    /// The skeletons that are closed, for the dossier.
    pub(super) fn closed(&self) -> impl Iterator<Item = &Skeleton> {
        self.skeletons
            .iter()
            .filter(|skeleton| skeleton.stance.is_closed())
    }

    /// Every gap still open, across every skeleton that is not closed.
    ///
    /// A closed skeleton's gaps are excluded: the reduction they belonged to is
    /// broken or spent, so proving one of them buys the run nothing, and
    /// putting it in front of the next attempt as a target would be the
    /// expensive kind of wrong.
    pub(super) fn open_gaps(&self) -> Vec<&Gap> {
        self.skeletons
            .iter()
            .filter(|skeleton| !skeleton.stance.is_closed())
            .flat_map(Skeleton::open)
            .collect()
    }

    /// Every gap id anything on disk records as discharged.
    pub(super) fn discharged_ids(&self) -> BTreeSet<String> {
        self.skeletons
            .iter()
            .flat_map(|skeleton| skeleton.gaps.iter())
            .filter(|gap| gap.stance == GapStance::Discharged)
            .map(|gap| gap.id.clone())
            .filter(|id| !id.is_empty())
            .collect()
    }

    /// What a turn has to move for it to have done anything.
    ///
    /// Slug, gap id, and gap stance — the three things every downstream reader
    /// of this ledger actually consumes. Compared before and after a
    /// delegation, an unchanged fingerprint means the turn changed nothing
    /// anybody reads, whatever it did to the bytes.
    pub(super) fn fingerprint(&self) -> BTreeSet<(String, String, GapStance)> {
        self.skeletons
            .iter()
            .flat_map(|skeleton| {
                skeleton.gaps.iter().map(move |gap| {
                    (skeleton.slug.clone(), gap.id.clone(), gap.stance)
                })
            })
            .collect()
    }
}

/// Reads one `skeleton` block into a skeleton, or records why it could not.
///
/// Split from [`collect`] so the loop over the directory stays readable; the
/// two halves of parsing a file are a header and a list of gaps, and they have
/// nothing to say to each other.
fn read_skeleton(slug: &str, block: &str, out: &mut Skeletons) -> Skeleton {
    let mut skeleton = Skeleton {
        slug: slug.to_string(),
        ..Skeleton::default()
    };
    for (key, value) in fields(block) {
        match key.as_str() {
            "goal" | "target" => skeleton.goal = value,
            "implies" | "sufficient-because" => skeleton.implies = value,
            "status" | "stance" => skeleton.stance = Stance::parse(&value),
            "rests-on" | "claims" => skeleton.rests_on = identifiers(&value),
            "killed-by" | "broken-by" => skeleton.killed_by = value,
            _ => {}
        }
    }
    if skeleton.goal.is_empty() {
        out.faults.push(format!(
            "`{slug}` names no goal, so it is a note, not a skeleton"
        ));
    }
    if skeleton.implies.is_empty() {
        out.faults.push(format!(
            "`{slug}` does not say how its lemmas imply the goal, so nothing can check that they \
             do"
        ));
    }
    skeleton
}

/// Reads one `gap` block, or records why it could not be used.
fn read_gap(slug: &str, block: &str, out: &mut Skeletons) -> Option<Gap> {
    let mut gap = Gap {
        skeleton: slug.to_string(),
        ..Gap::default()
    };
    for (key, value) in fields(block) {
        match key.as_str() {
            "id" | "gap" => gap.id = value,
            "lemma" | "statement" => gap.lemma = value,
            "status" | "stance" => gap.stance = GapStance::parse(&value),
            "discharged-by" | "closed-by" => gap.discharged_by = value,
            "thread" => gap.thread = value,
            "next" | "next-step" => gap.next = value,
            _ => {}
        }
    }
    // An id is the precondition for everything downstream: whether a gap is
    // already discharged, whether the fingerprint moved, whether a turn
    // restated something closed. A gap without one cannot be tracked between
    // two writes, so it is a fault rather than an anonymous row.
    if gap.id.is_empty() {
        out.faults.push(format!(
            "`{slug}` has a gap with no id, so nothing can say later whether it was closed"
        ));
        return None;
    }
    if gap.lemma.is_empty() {
        out.faults.push(format!(
            "`{slug}` gap `{}` states no lemma, so there is nothing to prove",
            gap.id
        ));
        return None;
    }
    Some(gap)
}

/// Reads every skeleton file under [`BACKWARD_DIR`].
pub(super) fn collect(workspace: &Path) -> Skeletons {
    let mut out = Skeletons::default();
    let Ok(entries) = std::fs::read_dir(workspace.join(BACKWARD_DIR)) else {
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
        let (blocks, unclosed) = fenced(&text, "skeleton");
        if unclosed {
            out.faults.push(format!(
                "`{slug}` has a skeleton block that was never closed"
            ));
        }
        let Some(block) = blocks.first() else {
            out.faults.push(format!(
                "`{slug}` has no skeleton block, so nothing can say what it reduces or whether the \
                 reduction is sound"
            ));
            continue;
        };
        let mut skeleton = read_skeleton(&slug, block, &mut out);
        let (gap_blocks, gaps_unclosed) = fenced(&text, "gap");
        if gaps_unclosed {
            out.faults
                .push(format!("`{slug}` has a gap block that was never closed"));
        }
        for gap_block in gap_blocks {
            if let Some(gap) = read_gap(&slug, gap_block, &mut out) {
                skeleton.gaps.push(gap);
            }
        }
        if skeleton.gaps.is_empty() && !skeleton.stance.is_closed() {
            out.faults.push(format!(
                "`{slug}` has no gaps, so it either claims the goal outright or nobody wrote down \
                 what is missing"
            ));
        }
        out.skeletons.push(skeleton);
    }
    out
}

impl Skeletons {
    /// Renders the table routed into the roles that pick what to attack.
    ///
    /// `ledger` is passed for the same reason [`super::threads::Threads::render`]
    /// takes one, and for two more: a reduction resting on a claim nobody wrote
    /// down cannot be checked by the next reader, and a gap whose id names a
    /// claim already in the library is a lemma the run has proved without
    /// noticing.
    pub(super) fn render(&self, ledger: &Ledger) -> String {
        let known: BTreeSet<String> = ledger.ids();
        let mut out = String::from(
            "# Backward — what would suffice to prove the goal\n\n\
             Derived from the files under `research/backward/`, and rewritten whenever one of them \
             is written. Do not edit this file; the next write re-derives it. One skeleton is one \
             decomposition of the goal: open `research/backward/<name>.md` to work on it.\n\n\
             This is not the approach ledger. An approach is a *route* — a reformulation that \
             might get there. A skeleton is a *decomposition* — the goal itself, broken into \
             propositions that can each be attacked on their own. `research/APPROACHES.md` \
             answers what else could get us there; this file answers what would be enough.\n\n\
             Every open gap below is a task. A gap with a `next` a tool_builder or a \
             theorem_prover could start on today is worth more than three lemmas nobody can \
             begin.\n\n",
        );
        if self.skeletons.is_empty() {
            out.push_str(
                "_No skeletons yet. Write one as soon as the goal can be decomposed: \
                 `research/backward/<name>.md`, with a fenced `skeleton` block carrying `goal`, \
                 `implies`, `status`, `rests-on`, and `killed-by` lines, then one fenced `gap` \
                 block per missing lemma carrying `id`, `lemma`, `status`, `discharged-by`, \
                 `thread`, and `next`._\n",
            );
            self.append_faults(&mut out);
            return out;
        }
        out.push_str(
            "| Skeleton | Goal | Reduces to | Status | Open gaps |\n\
             | --- | --- | --- | --- | --- |\n",
        );
        for skeleton in self.skeletons.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "| [[{}]] | {} | {} | {} | {} |",
                skeleton.slug,
                cell(&truncate(&skeleton.goal, FIELD_CHARS)),
                cell(&truncate(&skeleton.implies, FIELD_CHARS)),
                skeleton.stance.label(),
                skeleton.open().count()
            );
        }
        if self.skeletons.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further skeletons not shown._",
                self.skeletons.len() - MAX_ROWS
            );
        }
        self.append_open(&mut out);
        self.append_discharged(&mut out);
        self.append_broken(&mut out);
        self.append_reopened(&mut out);
        self.append_unsupported(&mut out, &known);
        self.append_faults(&mut out);
        out
    }

    /// Lists every open gap, which is the section the forward roles read.
    ///
    /// A gap with no thread is called out rather than left to look the same as
    /// one being worked: the difference between a lemma somebody is attacking
    /// and a lemma nobody has touched is the whole value of writing them down
    /// separately.
    fn append_open(&self, out: &mut String) {
        let mut rows = String::new();
        for gap in self.open_gaps() {
            let _ = writeln!(
                rows,
                "- [[{}]] `{}` — {}",
                gap.skeleton, gap.id, gap.lemma
            );
            let next = if gap.next.trim().is_empty() {
                "_no first step — a gap nobody can begin is a research request, not a task_"
            } else {
                gap.next.trim()
            };
            let _ = writeln!(rows, "  - next: {next}");
            if gap.thread.trim().is_empty() {
                let _ = writeln!(rows, "  - _no thread — nothing is attacking this_");
            } else {
                let _ = writeln!(rows, "  - thread: {}", gap.thread.trim());
            }
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## The open gaps — each one is a task\n\nProve any of these and the skeleton it \
             belongs to moves. Pick the one with a first step.\n\n",
        );
        out.push_str(&rows);
    }

    /// Lists the gaps already closed, and what closed each.
    ///
    /// Kept for the reason the approach ledger keeps its refuted rows: the
    /// single failure this ledger exists to prevent is a role restating a lemma
    /// the run already has, and the id with the claim beside it is what
    /// prevents it.
    fn append_discharged(&self, out: &mut String) {
        let mut rows = String::new();
        for gap in self
            .skeletons
            .iter()
            .flat_map(|skeleton| skeleton.gaps.iter())
            .filter(|gap| gap.stance == GapStance::Discharged)
        {
            let by = if gap.discharged_by.trim().is_empty() {
                "_nothing named — say which claim closed it, or the next reducer will restate it_"
            } else {
                gap.discharged_by.trim()
            };
            let _ = writeln!(
                rows,
                "- [[{}]] `{}` — {} (closed by {by})",
                gap.skeleton, gap.id, gap.lemma
            );
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Gaps already discharged\n\nDo not state these again. Each one is a lemma this \
             run has, and the claim beside it is where to read it.\n\n",
        );
        out.push_str(&rows);
    }

    /// Spells out why each broken or spent reduction closed.
    fn append_broken(&self, out: &mut String) {
        let mut rows = String::new();
        for skeleton in self.closed() {
            let reason = if skeleton.killed_by.trim().is_empty() {
                "_no reason recorded — say what broke it, or the next reducer will sketch it again_"
            } else {
                skeleton.killed_by.trim()
            };
            let _ = writeln!(
                rows,
                "- [[{}]] ({}): {reason}",
                skeleton.slug,
                skeleton.stance.label()
            );
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Reductions that broke, and why\n\nA decomposition that does not recombine into \
             the goal is the failure this file exists to make visible. The reason is the useful \
             half; one left blank makes the row worthless.\n\n",
        );
        out.push_str(&rows);
    }

    /// Lists open gaps whose id something else already discharged.
    ///
    /// Computed rather than asked for. A role that restates a closed lemma has
    /// spent a turn establishing what the run already had, and a prompt telling
    /// it not to is not a control — this row is what makes it visible for as
    /// long as the file exists.
    fn append_reopened(&self, out: &mut String) {
        let discharged = self.discharged_ids();
        let mut rows = String::new();
        for gap in self.open_gaps() {
            if !discharged.contains(&gap.id) {
                continue;
            }
            let _ = writeln!(
                rows,
                "- [[{}]] states `{}` as open, and it is discharged elsewhere in this ledger",
                gap.skeleton, gap.id
            );
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Re-opened after being discharged\n\nEither the lemma was closed and somebody \
             asked for it again, or two skeletons are using one id for two different \
             statements.\n\n",
        );
        out.push_str(&rows);
    }

    /// Lists reductions resting on claims that are not in the ledger.
    fn append_unsupported(&self, out: &mut String, known: &BTreeSet<String>) {
        let mut rows = String::new();
        for skeleton in &self.skeletons {
            let missing: Vec<&String> = skeleton
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
                skeleton.slug,
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
            "\n## Resting on nothing recorded\n\nA reduction taking an unrecorded belief as input \
             proves the goal from something nobody downstream can check. Either write the claim, \
             or the id is misspelled.\n\n",
        );
        out.push_str(&rows);
    }

    fn append_faults(&self, out: &mut String) {
        if self.faults.is_empty() {
            return;
        }
        out.push_str("\n## Skeletons that could not be read\n\n");
        for fault in &self.faults {
            let _ = writeln!(out, "- {fault}");
        }
    }
}

impl Skeleton {
    /// Renders one skeleton for the dossier, in full rather than as a row.
    ///
    /// The table truncates every field and scatters the gaps into sections
    /// below. That is right for a file somebody scans, and wrong for the
    /// dossier, where a role is handed the closed skeletons precisely so it
    /// does not sketch one again: there the inference and the reason it broke
    /// have to arrive whole, together.
    pub(super) fn full(&self) -> String {
        let mut out = format!("### {} ({})\n", self.slug, self.stance.label());
        for (label, value) in [
            ("Goal", self.goal.as_str()),
            ("Reduces to", self.implies.as_str()),
            ("Broken by", self.killed_by.as_str()),
        ] {
            if !value.trim().is_empty() {
                let _ = writeln!(out, "- {label}: {}", value.trim());
            }
        }
        if !self.rests_on.is_empty() {
            let _ = writeln!(out, "- Rests on: {}", self.rests_on.join(", "));
        }
        for gap in &self.gaps {
            let _ = writeln!(
                out,
                "- Gap `{}` ({}): {}",
                gap.id,
                gap.stance.label(),
                gap.lemma.trim()
            );
        }
        out
    }
}

impl Gap {
    /// Renders one open gap for the next attempt's prompt.
    ///
    /// Read from disk rather than taken from the reducer's reply, which is the
    /// same argument the dossier makes: what is on disk is the record, and a
    /// summary of itself is not it.
    pub(super) fn briefing(&self) -> String {
        let mut out = format!("- `{}` ({}): {}", self.id, self.skeleton, self.lemma.trim());
        if !self.next.trim().is_empty() {
            let _ = write!(out, "\n  first step: {}", self.next.trim());
        }
        out
    }
}

/// Re-derives the skeleton table and rewrites [`BACKWARD_PATH`].
///
/// Best effort, like the claim ledger and the thread table: a failed refresh
/// must not fail the write that succeeded.
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) {
    let skeletons = collect(documents.root());
    let ledger = super::claims::collect(documents.root());
    let _ = documents
        .write_runtime(BACKWARD_PATH, &skeletons.render(&ledger))
        .await;
    super::folder_index::record_description(
        documents,
        BACKWARD_PATH,
        "Derived: what would suffice to prove the goal — every decomposition under \
         research/backward/, the lemmas still missing, and which ones are already closed. \
         Rewritten on every skeleton and note write; do not edit.",
    )
    .await;
}

/// Whether a written path is a skeleton file the table is derived from.
///
/// The derived table itself must never match. It lives one directory up, so on
/// a case-sensitive filesystem it cannot — but this ledger is written into an
/// agent-authored tree, and a refresh that triggered a refresh would be a loop
/// nothing bounds, so the exclusion is asserted rather than assumed.
pub(super) fn is_backward(relative: &str) -> bool {
    relative != BACKWARD_PATH
        && relative.starts_with(&format!("{BACKWARD_DIR}/"))
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
#[path = "backward_test.rs"]
mod test;
