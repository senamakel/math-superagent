//! Weakening: the goal with most of its difficulties switched off, and the
//! ladder back up to the one that was asked for.
//!
//! The runtime already reasons backward and sideways. The reducer asks what
//! lemmas would *suffice* to prove the goal; the inventor asks what other
//! *route* could reach it. Both of them keep the target fixed. Nothing in the
//! runtime is allowed to lower it, and lowering it is the move a working
//! mathematician makes first: if ten things make the problem hard, solve the
//! version with nine of them turned off, then turn them back on a few at a
//! time and find out which one was actually carrying the difficulty.
//!
//! The failure this prevents is the one a fixed target produces by itself. An
//! attempt against the full-strength statement either lands or does not, and a
//! run that cannot land it has no smaller thing to have proved instead — so it
//! spends its budget re-attacking the same statement and banks nothing. A
//! ladder replaces that with a sequence of statements the run can actually
//! settle, each one a real theorem about a real special case, and each one
//! evidence about which difficulty is the obstruction.
//!
//! A rung is the unit that matters, which is why a file holds two kinds of
//! block rather than one. The header names the full-strength goal and the
//! difficulties in play; each rung names which of them are switched *off*, what
//! the weakened statement then is, and what re-enabling the next difficulty
//! would take. A `rungs:` list inside a single block could carry none of that
//! per rung — not whether this one was settled, not what it cost, not why one
//! of them failed — and the whole point of the ladder is the per-rung record.
//!
//! The `off` list is checked against the header's declared difficulties rather
//! than taken on trust. A rung switching off something the ladder never
//! declared means the two halves of the file disagree about what makes the
//! problem hard, and a ladder built on that disagreement climbs to a goal
//! nobody stated: the rungs no longer compose back into the header's target.
//!
//! `WEAKENED.md` is derived from the files under `research/weakened/`, exactly
//! as `BACKWARD.md` is derived from the skeleton files and for the same reason
//! — a table an agent edits is a table that disagrees with its sources.

use std::collections::BTreeSet;
use std::fmt::Write as _;
use std::path::Path;

use super::claims::{fenced, fields};
use super::ledger::budget;
use super::text::truncate;

/// Folder holding one file per difficulty ladder.
pub(super) const WEAKENED_DIR: &str = "research/weakened";

/// The derived table, filed with the library it describes.
pub(super) const WEAKENED_PATH: &str = "derived/WEAKENED.md";

/// Rungs one table lists.
const MAX_ROWS: usize = 24;

/// Characters one rendered field is held to.
const FIELD_CHARS: usize = 160;

/// Where a whole ladder stands.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, PartialOrd, Ord)]
pub(super) enum LadderStance {
    /// Rungs remain: something below the full-strength goal is still unproved.
    #[default]
    Open,
    /// Every rung is settled and merged back, so the full problem is reached.
    ///
    /// Deliberately not treated as closed. A ladder climbed to the top is the
    /// most valuable thing this file can hold and the one a later reader most
    /// wants to find, which is the opposite of one that was given up on.
    Exhausted,
    /// Given up on: the weakened versions did not lead anywhere.
    Abandoned,
}

impl LadderStance {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("abandon") || lowered.starts_with("dead") {
            Self::Abandoned
        } else if lowered.starts_with("exhaust")
            || lowered.starts_with("complete")
            || lowered.starts_with("reached")
        {
            Self::Exhausted
        } else {
            Self::Open
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Open => "open",
            Self::Exhausted => "**exhausted**",
            Self::Abandoned => "abandoned",
        }
    }

    /// Whether this stance stops the ladder being offered as work.
    ///
    /// Only abandonment does. An exhausted ladder has no open rung left to
    /// offer anyway, so excluding it here would hide the one contradiction
    /// worth seeing: a ladder that calls itself finished while a rung is still
    /// open has either mislabelled itself or forgotten a rung.
    pub(super) fn is_closed(self) -> bool {
        matches!(self, Self::Abandoned)
    }
}

/// Where one rung stands.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, PartialOrd, Ord)]
pub(super) enum RungStance {
    /// Stated, not yet established.
    #[default]
    Open,
    /// Actually proved. This is a theorem the run owns, weaker than the goal.
    Settled,
    /// Attacked and it did not work.
    ///
    /// Kept rather than deleted, with the reason beside it, because a rung
    /// removed from the file is a rung the next weakener proposes again.
    Failed,
    /// Its difficulty has been switched back on and folded into a higher rung.
    Merged,
}

impl RungStance {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("settl")
            || lowered.starts_with("establish")
            || lowered.starts_with("proved")
            || lowered.starts_with("done")
        {
            Self::Settled
        } else if lowered.starts_with("fail")
            || lowered.starts_with("stuck")
            || lowered.starts_with("dead")
        {
            Self::Failed
        } else if lowered.starts_with("merg") || lowered.starts_with("folded") {
            Self::Merged
        } else {
            Self::Open
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Open => "open",
            Self::Settled => "**settled**",
            Self::Failed => "failed",
            Self::Merged => "merged",
        }
    }
}

/// One weakened version of the goal.
#[derive(Clone, Debug, Default)]
pub(super) struct Rung {
    /// The ladder this rung belongs to, so a briefing can name its source.
    pub(super) ladder: String,
    /// A stable name, which is what makes "already settled" computable.
    pub(super) id: String,
    /// The weakened target itself, in mathematics.
    pub(super) statement: String,
    /// The difficulties switched *off* here.
    ///
    /// The rung's position on the ladder is this list's length: everything off
    /// is a hypothesis the weakened statement gets for free.
    pub(super) off: Vec<String>,
    /// Where it stands.
    pub(super) stance: RungStance,
    /// What turning the next difficulty back on would take — the first
    /// concrete move toward the rung above.
    ///
    /// The load-bearing field. A ladder whose rungs do not say how to climb is
    /// a list of easier problems, which is not the same thing at all: the
    /// value of solving a weakened version is entirely in what it teaches
    /// about the version above it.
    pub(super) merge: String,
    /// The claim or note that established it.
    settled_by: String,
    /// Why it failed, so nobody attacks it the same way twice.
    failed_by: String,
}

/// One difficulty ladder: a full-strength goal, what makes it hard, and the
/// weakened versions between the run and it.
#[derive(Clone, Debug, Default)]
pub(super) struct Ladder {
    /// The file's stem, which is how a reader names the ladder.
    pub(super) slug: String,
    /// The full-strength target every rung is a weakening of.
    goal: String,
    /// The things that make the goal hard, named so a rung can switch them off.
    difficulties: Vec<String>,
    /// Where it stands.
    pub(super) stance: LadderStance,
    /// The rungs, in the order the file wrote them.
    rungs: Vec<Rung>,
}

impl Ladder {
    /// The rungs weakest first — most difficulties off to fewest.
    ///
    /// That is the order they are meant to be climbed, so it is the order they
    /// are rendered in. File order is preserved between rungs turning off the
    /// same number of difficulties, because the sort is stable and the author's
    /// order is the only signal available there.
    fn ordered(&self) -> Vec<&Rung> {
        let mut rungs: Vec<&Rung> = self.rungs.iter().collect();
        rungs.sort_by_key(|rung| std::cmp::Reverse(rung.off.len()));
        rungs
    }

    /// The weakest rung nobody has settled — the one the next attempt wants.
    ///
    /// Weakest rather than nearest the goal: climbing from below is the whole
    /// method, and an attempt aimed three rungs up fails for the same reason
    /// the full-strength goal does.
    pub(super) fn current(&self) -> Option<&Rung> {
        self.ordered()
            .into_iter()
            .find(|rung| rung.stance == RungStance::Open)
    }

    /// Whether this ladder declared `label` as one of its difficulties.
    fn declares(&self, label: &str) -> bool {
        let wanted = normalize(label);
        self.difficulties
            .iter()
            .any(|declared| normalize(declared) == wanted)
    }
}

/// Every ladder on disk, with the faults found reading them.
#[derive(Debug, Default)]
pub(super) struct Ladders {
    ladders: Vec<Ladder>,
    faults: Vec<String>,
}

impl Ladders {
    /// Every rung still open, across every ladder that was not abandoned.
    ///
    /// An abandoned ladder's rungs are excluded: proving one buys the run
    /// nothing, because the ladder they belonged to leads nowhere, and putting
    /// one in front of the next attempt as a target would be the expensive
    /// kind of wrong.
    pub(super) fn open_rungs(&self) -> Vec<&Rung> {
        self.ladders
            .iter()
            .filter(|ladder| !ladder.stance.is_closed())
            .flat_map(|ladder| {
                ladder
                    .ordered()
                    .into_iter()
                    .filter(|rung| rung.stance == RungStance::Open)
            })
            .collect()
    }

    /// Every rung the run actually established.
    ///
    /// These are theorems, weaker than the goal and true. A run that ends
    /// without reaching the goal has these as its result, so they are what a
    /// final write-up is built from.
    pub(super) fn settled(&self) -> impl Iterator<Item = &Rung> {
        self.rungs().filter(|rung| rung.stance == RungStance::Settled)
    }

    /// The rungs that were attacked and did not work.
    fn failed(&self) -> impl Iterator<Item = &Rung> {
        self.rungs().filter(|rung| rung.stance == RungStance::Failed)
    }

    /// Every rung on disk, whatever its ladder's stance.
    fn rungs(&self) -> impl Iterator<Item = &Rung> {
        self.ladders.iter().flat_map(|ladder| ladder.rungs.iter())
    }

    /// The rungs of every ladder, weakest first across the whole ledger.
    fn ordered(&self) -> Vec<&Rung> {
        let mut rungs: Vec<&Rung> = self.rungs().collect();
        rungs.sort_by_key(|rung| std::cmp::Reverse(rung.off.len()));
        rungs
    }

    /// What a turn has to move for it to have done anything.
    ///
    /// Ladder slug, rung id, and rung stance — the three things every
    /// downstream reader of this ledger consumes. Compared before and after a
    /// delegation, an unchanged fingerprint means the turn changed nothing
    /// anybody reads, whatever it did to the bytes. Comparing filenames would
    /// not do: refining a ladder that already exists — adding a rung, settling
    /// one, recording why one failed — adds no new file, and is exactly the
    /// work this ledger most wants to reward.
    pub(super) fn fingerprint(&self) -> BTreeSet<(String, String, RungStance)> {
        self.ladders
            .iter()
            .flat_map(|ladder| {
                ladder
                    .rungs
                    .iter()
                    .map(move |rung| (ladder.slug.clone(), rung.id.clone(), rung.stance))
            })
            .collect()
    }

    /// The short form that travels to the next attempt: one current rung per
    /// ladder, with the move that climbs off it.
    ///
    /// Read from disk rather than taken from the weakener's reply, which is the
    /// same argument the dossier makes: what is on disk is the record, and a
    /// summary of itself is not it.
    pub(super) fn briefing(&self) -> String {
        let mut out = String::new();
        for ladder in &self.ladders {
            if ladder.stance.is_closed() {
                continue;
            }
            if let Some(rung) = ladder.current() {
                out.push_str(&rung.briefing());
                out.push('\n');
            }
        }
        out
    }
}

/// Splits a comma or semicolon separated list into its entries.
///
/// Not [`super::claims::identifiers`], which also splits on whitespace: a
/// difficulty is a phrase a person wrote — "unbounded number of primes" — and
/// splitting it on spaces would turn one difficulty into four that no rung can
/// ever match.
fn list(value: &str) -> Vec<String> {
    value
        .split([',', ';'])
        .map(|entry| entry.trim().trim_matches('`').trim().to_string())
        .filter(|entry| !entry.is_empty())
        .collect()
}

/// The comparable form of a difficulty name.
fn normalize(label: &str) -> String {
    label.trim().to_ascii_lowercase()
}

/// Reads one `ladder` block into a header, or records why it could not.
///
/// Split from [`collect`] so the loop over the directory stays readable; the
/// two halves of parsing a file are a header and a list of rungs, and they have
/// nothing to say to each other.
fn read_ladder(slug: &str, block: &str, out: &mut Ladders) -> Ladder {
    let mut ladder = Ladder {
        slug: slug.to_string(),
        ..Ladder::default()
    };
    for (key, value) in fields(block) {
        match key.as_str() {
            "goal" | "target" | "full-strength" => ladder.goal = value,
            "difficulties" | "difficulty" | "hard-because" => ladder.difficulties = list(&value),
            "status" | "stance" => ladder.stance = LadderStance::parse(&value),
            _ => {}
        }
    }
    if ladder.goal.is_empty() {
        out.faults.push(format!(
            "`{slug}` names no full-strength goal, so nothing says what its rungs are weakenings of"
        ));
    }
    if ladder.difficulties.is_empty() {
        out.faults.push(format!(
            "`{slug}` names no difficulties, so no rung can say what it switched off and nothing \
             can check that the rungs climb back to the goal"
        ));
    }
    ladder
}

/// Reads one `rung` block, or records why it could not be used.
fn read_rung(slug: &str, block: &str, out: &mut Ladders) -> Option<Rung> {
    let mut rung = Rung {
        ladder: slug.to_string(),
        ..Rung::default()
    };
    for (key, value) in fields(block) {
        match key.as_str() {
            "id" | "rung" => rung.id = value,
            "statement" | "weakened" | "target" => rung.statement = value,
            "off" | "switched-off" | "drops" => rung.off = list(&value),
            "status" | "stance" => rung.stance = RungStance::parse(&value),
            "merge" | "merge-next" | "next" => rung.merge = value,
            "settled-by" | "established-by" => rung.settled_by = value,
            "failed-by" | "because" => rung.failed_by = value,
            _ => {}
        }
    }
    // An id is the precondition for everything downstream: whether a rung is
    // already settled, whether the fingerprint moved, whether a turn proposed
    // something that already failed. A rung without one cannot be tracked
    // between two writes, so it is a fault rather than an anonymous row.
    if rung.id.is_empty() {
        out.faults.push(format!(
            "`{slug}` has a rung with no id, so nothing can say later whether it was settled"
        ));
        return None;
    }
    if rung.statement.is_empty() {
        out.faults.push(format!(
            "`{slug}` rung `{}` states no weakened target, so there is nothing to prove",
            rung.id
        ));
        return None;
    }
    Some(rung)
}

/// Records every rung switching off a difficulty its ladder never declared.
///
/// The two halves of the file disagreeing about what makes the problem hard is
/// the failure that makes a ladder worthless: the rungs stop being weakenings
/// of the stated goal, so climbing them arrives somewhere nobody asked for.
fn check_difficulties(ladder: &Ladder, out: &mut Ladders) {
    for rung in &ladder.rungs {
        for label in &rung.off {
            if ladder.declares(label) {
                continue;
            }
            out.faults.push(format!(
                "`{}` rung `{}` switches off `{label}`, which the ladder never declared as a \
                 difficulty — the rung and the header disagree about what makes the goal hard",
                ladder.slug, rung.id
            ));
        }
    }
}

/// Reads every ladder file under [`WEAKENED_DIR`].
pub(super) fn collect(workspace: &Path) -> Ladders {
    let mut out = Ladders::default();
    let Ok(entries) = std::fs::read_dir(workspace.join(WEAKENED_DIR)) else {
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
        let (blocks, unclosed) = fenced(&text, "ladder");
        if unclosed {
            out.faults
                .push(format!("`{slug}` has a ladder block that was never closed"));
        }
        let Some(block) = blocks.first() else {
            out.faults.push(format!(
                "`{slug}` has no ladder block, so nothing can say what goal its rungs weaken"
            ));
            continue;
        };
        let mut ladder = read_ladder(&slug, block, &mut out);
        let (rung_blocks, rungs_unclosed) = fenced(&text, "rung");
        if rungs_unclosed {
            out.faults
                .push(format!("`{slug}` has a rung block that was never closed"));
        }
        for rung_block in rung_blocks {
            if let Some(rung) = read_rung(&slug, rung_block, &mut out) {
                ladder.rungs.push(rung);
            }
        }
        if ladder.rungs.is_empty() && !ladder.stance.is_closed() {
            out.faults.push(format!(
                "`{slug}` has no rungs, so it names a hard goal and no easier version of it"
            ));
        }
        check_difficulties(&ladder, &mut out);
        out.ladders.push(ladder);
    }
    out
}

impl Ladders {
    /// Renders the table routed into the roles that pick what to attack.
    ///
    /// The rungs come first and weakest first, because that is the order they
    /// are meant to be climbed and a reader scanning for what to do next should
    /// find the easiest unproved thing at the top rather than have to sort the
    /// table themselves.
    pub(super) fn render(&self) -> String {
        let mut out = String::from(
            "# Weakened — the goal with its difficulties switched off\n\n\
             Derived from the files under `research/weakened/`, and rewritten whenever one of them \
             is written. Do not edit this file; the next write re-derives it. One ladder is one \
             full-strength goal plus the weakened versions between the run and it: open \
             `research/weakened/<name>.md` to work on it.\n\n\
             This is neither the approach ledger nor the backward ledger. An approach is a *route* \
             to the same goal; a skeleton is a *decomposition* of the same goal. A ladder lowers \
             the goal itself — it turns difficulties off, proves the easier statement, and turns \
             them back on a few at a time. A settled rung is a real theorem this run owns, and it \
             is evidence about which difficulty was carrying the weight.\n\n\
             Rungs are listed weakest first, which is the order to climb them. Attack the current \
             rung, not the one three above it.\n\n",
        );
        if self.ladders.is_empty() {
            out.push_str(
                "_No ladders yet. Write one as soon as the goal has more than one source of \
                 difficulty: `research/weakened/<name>.md`, with a fenced `ladder` block carrying \
                 `goal`, `difficulties` (comma separated), and `status` lines, then one fenced \
                 `rung` block per weakened version carrying `id`, `statement`, `off`, `status`, \
                 `merge`, and — once it is closed — `settled-by` or `failed-by`._\n",
            );
            self.append_faults(&mut out);
            return out;
        }
        self.append_ladders(&mut out);
        self.append_rungs(&mut out);
        self.append_current(&mut out);
        self.append_settled(&mut out);
        self.append_failed(&mut out);
        self.append_contradictions(&mut out);
        self.append_faults(&mut out);
        out
    }

    /// One row per ladder: the goal it lowers and what it says makes it hard.
    fn append_ladders(&self, out: &mut String) {
        out.push_str(
            "## The ladders\n\n| Ladder | Full-strength goal | Difficulties | Status |\n\
             | --- | --- | --- | --- |\n",
        );
        for ladder in self.ladders.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "| [[{}]] | {} | {} | {} |",
                ladder.slug,
                cell(&truncate(&ladder.goal, FIELD_CHARS)),
                cell(&truncate(&ladder.difficulties.join(", "), FIELD_CHARS)),
                ladder.stance.label()
            );
        }
        if self.ladders.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further ladders not shown._",
                self.ladders.len() - MAX_ROWS
            );
        }
    }

    /// Every rung, weakest first — the order they are meant to be climbed.
    fn append_rungs(&self, out: &mut String) {
        let ordered = self.ordered();
        if ordered.is_empty() {
            return;
        }
        out.push_str(
            "\n## The rungs, weakest first\n\nEach row is a statement weaker than the goal. The \
             more difficulties are off, the easier it is, so the top of this table is where a \
             stuck run should be working.\n\n\
             | Rung | Ladder | Weakened target | Off | Status |\n| --- | --- | --- | --- | --- |\n",
        );
        for rung in ordered.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "| `{}` | [[{}]] | {} | {} | {} |",
                rung.id,
                rung.ladder,
                cell(&truncate(&rung.statement, FIELD_CHARS)),
                cell(&truncate(&rung.off.join(", "), FIELD_CHARS)),
                rung.stance.label()
            );
        }
        if ordered.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further rungs not shown._",
                ordered.len() - MAX_ROWS
            );
        }
    }

    /// States the current rung outright, per ladder.
    ///
    /// The single fact the next attempt needs, and the one a table makes a
    /// reader compute. A run that has to work out for itself which row is the
    /// weakest open one will sometimes get it wrong, and getting it wrong means
    /// attacking something too hard — which is the failure the whole ledger
    /// exists to prevent.
    fn append_current(&self, out: &mut String) {
        let live = self
            .ladders
            .iter()
            .filter(|ladder| !ladder.stance.is_closed());
        let (rows, dropped) = budget::listed(live, budget::MAX_LISTED, |rows, ladder| {
            match ladder.current() {
                Some(rung) => {
                    let _ = writeln!(
                        rows,
                        "- [[{}]] → `{}`: {}",
                        ladder.slug,
                        rung.id,
                        truncate(&rung.statement, budget::REASON_CHARS)
                    );
                    let off = if rung.off.is_empty() {
                        "_nothing — this is the full-strength goal_".to_string()
                    } else {
                        rung.off.join(", ")
                    };
                    let _ = writeln!(rows, "  - switched off: {off}");
                    let merge = if rung.merge.trim().is_empty() {
                        "_not stated — a rung that does not say how to climb off it teaches the \
                         run nothing about the goal_"
                            .to_string()
                    } else {
                        truncate(&rung.merge, budget::REASON_CHARS)
                    };
                    let _ = writeln!(rows, "  - to merge the next difficulty back: {merge}");
                }
                None => {
                    let _ = writeln!(
                        rows,
                        "- [[{}]] has no open rung and is not marked exhausted — either the \
                         ladder reached the goal and nobody said so, or the next rung up has not \
                         been written",
                        ladder.slug
                    );
                }
            }
        });
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## The current rung — attack this one\n\nThe weakest statement nobody has settled \
             yet. Aiming higher is how a run spends a budget proving nothing.\n\n",
        );
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, WEAKENED_DIR));
    }

    /// Lists what the run has actually banked, and under which hypotheses.
    ///
    /// The difficulties that were off are half the result. A settled rung
    /// quoted without them reads as a proof of the goal, which it is not, and
    /// that is the misreading most likely to end up in a final write-up.
    fn append_settled(&self, out: &mut String) {
        let (rows, dropped) = budget::listed(self.settled(), budget::MAX_LISTED, |rows, rung| {
            let off = if rung.off.is_empty() {
                "nothing switched off".to_string()
            } else {
                format!("off: {}", rung.off.join(", "))
            };
            let by = if rung.settled_by.trim().is_empty() {
                "_nothing named — say which claim established it, or a reader cannot check it_"
                    .to_string()
            } else {
                format!("established by {}", rung.settled_by.trim())
            };
            let _ = writeln!(
                rows,
                "- [[{}]] `{}`: {} ({off}; {by})",
                rung.ladder,
                rung.id,
                truncate(&rung.statement, budget::REASON_CHARS)
            );
        });
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Settled — what this run owns\n\nEach one is a theorem, weaker than the goal and \
             true. Quote it with the difficulties that were switched off; without them it reads as \
             a proof of something it did not prove.\n\n",
        );
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, WEAKENED_DIR));
    }

    /// Lists the rungs that failed, so none of them is proposed again.
    fn append_failed(&self, out: &mut String) {
        let (rows, dropped) = budget::listed(self.failed(), budget::MAX_LISTED, |rows, rung| {
            let reason = if rung.failed_by.trim().is_empty() {
                "_no reason recorded — say what went wrong, or the next weakener will propose it \
                 again_"
                    .to_string()
            } else {
                truncate(&rung.failed_by, budget::REASON_CHARS)
            };
            let _ = writeln!(
                rows,
                "- [[{}]] `{}`: {} — {reason}",
                rung.ladder,
                rung.id,
                truncate(&rung.statement, budget::REASON_CHARS)
            );
        });
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Rungs that failed, and why\n\nDo not propose these again. A weakened version \
             that did not work is information about the difficulty it left on, and the reason is \
             the useful half; one left blank makes the row worthless.\n\n",
        );
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, WEAKENED_DIR));
    }

    /// Lists ladders calling themselves finished while a rung is still open.
    ///
    /// Computed rather than asked for. A ladder marked exhausted stops being
    /// worked, so one marked exhausted by mistake silently retires every rung
    /// under it — including the ones nobody proved.
    fn append_contradictions(&self, out: &mut String) {
        let contradictory = self.ladders.iter().filter_map(|ladder| {
            if ladder.stance != LadderStance::Exhausted {
                return None;
            }
            let open = ladder
                .rungs
                .iter()
                .filter(|rung| rung.stance == RungStance::Open)
                .count();
            (open > 0).then_some((ladder, open))
        });
        let (rows, dropped) =
            budget::listed(contradictory, budget::MAX_LISTED, |rows, (ladder, open)| {
                let _ = writeln!(
                    rows,
                    "- [[{}]] is marked exhausted while {open} of its rungs are still open",
                    ladder.slug
                );
            });
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Exhausted while a rung is open\n\nEither the ladder reached the goal and a rung \
             was never updated, or it did not reach the goal and calling it exhausted retires work \
             nobody did.\n\n",
        );
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, WEAKENED_DIR));
    }

    fn append_faults(&self, out: &mut String) {
        if self.faults.is_empty() {
            return;
        }
        out.push_str("\n## Ladders that could not be read\n\n");
        let (rows, dropped) = budget::listed(&self.faults, budget::MAX_LISTED, |rows, fault| {
            let _ = writeln!(rows, "- {}", truncate(fault, budget::REASON_CHARS));
        });
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, WEAKENED_DIR));
    }
}

impl Rung {
    /// Renders one rung for the next attempt's prompt.
    ///
    /// The statement, what it is allowed to assume, and the move that climbs
    /// off it. An attempt handed the statement alone would prove it and stop,
    /// which banks a theorem and learns nothing about the goal above it.
    pub(super) fn briefing(&self) -> String {
        let mut out = format!(
            "- `{}` ({}): {}",
            self.id,
            self.ladder,
            self.statement.trim()
        );
        if !self.off.is_empty() {
            let _ = write!(out, "\n  switched off: {}", self.off.join(", "));
        }
        if !self.merge.trim().is_empty() {
            let _ = write!(out, "\n  then merge back: {}", self.merge.trim());
        }
        out
    }
}

/// One line per rung: its id, where it stands, and the weakened statement.
///
/// The rungs rather than the ladders, for the reason the backward ledger
/// indexes gaps: a rung is the thing somebody attacks, and the ladder is what
/// it hangs off. Weakest first, which is the order they are meant to be climbed
/// and therefore the order a reader wants them.
pub(super) fn index(workspace: &Path) -> String {
    let ladders = collect(workspace);
    let rows: Vec<(String, String, String)> = ladders
        .ordered()
        .iter()
        .map(|rung| {
            (
                format!("{}/{}", rung.ladder, rung.id),
                rung.stance.label().to_string(),
                rung.statement.clone(),
            )
        })
        .collect();
    super::ledger::index::render(
        "weakened",
        "Weakened targets",
        "The goal with its difficulties switched off, weakest first. The first open rung is the \
         one to attack; a settled one is a theorem this run owns, under the difficulties it \
         switched off.",
        rows.iter().map(|(id, status, headline)| super::ledger::index::Row {
            id,
            status,
            headline,
        }),
        super::ledger::index::HEADLINE,
    )
}

/// Re-derives the ladder table and rewrites [`WEAKENED_PATH`].
///
/// Best effort, like the claim ledger and the backward table: a failed refresh
/// must not fail the write that succeeded.
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) {
    let ladders = collect(documents.root());
    let _ = documents
        .write_runtime(WEAKENED_PATH, &ladders.render())
        .await;
    super::folder_index::record_description(
        documents,
        WEAKENED_PATH,
        "Derived: the goal with its difficulties switched off — every ladder under \
         research/weakened/, which weakened version is current, what the run has settled, and \
         which rungs failed. Rewritten on every ladder write; do not edit.",
    )
    .await;
}

/// Whether a written path is a ladder file the table is derived from.
///
/// The derived table itself must never match. It lives one directory up, so on
/// a case-sensitive filesystem it cannot — but this ledger is written into an
/// agent-authored tree, and a refresh that triggered a refresh would be a loop
/// nothing bounds, so the exclusion is asserted rather than assumed.
pub(super) fn is_weakened(relative: &str) -> bool {
    relative != WEAKENED_PATH
        && relative.starts_with(&format!("{WEAKENED_DIR}/"))
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
#[path = "weakened_test.rs"]
mod test;
