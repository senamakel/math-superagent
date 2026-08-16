//! Entailment: what the library already gives the run for free.
//!
//! The claim ledger stores statements and never reasons over them. Every claim
//! stands alone, with its own status, and the only relation between two of them
//! the runtime has ever computed is `contradicts`. That leaves three specific
//! things on the floor, and the Equational Theories Project measured how much
//! they are worth: 597,582 facts closed transitively into answers for all
//! 22,028,942 implications, roughly a thirty-sevenfold return. Most of what a
//! library knows is not what it says.
//!
//! The first is the **free upgrade**. A claim written `follows-from: a, b` is a
//! consequence of `a` and `b`, so the moment both are established it is too —
//! whatever status it happens to carry. Until this file, nothing noticed, and
//! the failure is the expensive direction: a run spends an attempt proving a
//! lemma its own library already hands it. `research/BACKWARD.md` warns about
//! exactly this in prose ("a decomposition into three statements two of which
//! the run has already proved is nearly a proof") and asks a *role* to check.
//! This computes it.
//!
//! The second is **redundancy**, which is the Dalmatian heuristic from
//! Fajtlowicz's Graffiti under its own name. Graffiti generated conjectures
//! mechanically and its hard problem was never generating them; it was that
//! most were uninformative — implied by something already on the board. More
//! than half of that program was the filter rather than the generator. Here the
//! same test applies to a proposal: a statement the library already entails is
//! not a result, however true it is, and the cheapest moment to find that out
//! is before an attempt is spent on it.
//!
//! The third is a **contradiction the direct check cannot see**. The ledger
//! flags `a contradicts b` when a claim says so. It cannot flag that `a` gives
//! `c`, and `c` contradicts `b`, and the run is holding both `a` and `b` — the
//! inconsistency is real, no single block states it, and following the edges is
//! the only way to reach it.
//!
//! Derived from what is already on disk, like every ledger here. No role writes
//! this file and no role was added; the `follows-from` edge is one line in a
//! block roles already write.

use std::collections::{BTreeMap, BTreeSet};
use std::fmt::Write as _;
use std::path::Path;

use super::claims::{Claim, Ledger, Status};
use super::text::truncate;

/// The derived report, filed with the library it is computed from.
pub(super) const CLOSURE_PATH: &str = "derived/ENTAILMENT.md";

/// Rows one section lists.
const MAX_ROWS: usize = 30;

/// Characters one rendered statement is held to.
const FIELD_CHARS: usize = 160;

/// Whether a status means the run may build on the claim without redoing it.
///
/// The same three the ledger counts as established. `Asserted`, `Heuristic` and
/// `Catalogued` are reasons to believe, and a closure that propagated them
/// would manufacture establishment out of a chain of guesses — each step
/// looking sound and the conclusion resting on nothing.
fn is_established(status: Status) -> bool {
    matches!(
        status,
        Status::Proved | Status::Formalised | Status::Checked
    )
}

/// One claim the library establishes without anybody having said so.
#[derive(Clone, Debug)]
pub(super) struct Upgrade {
    /// The claim whose status is lower than its support.
    pub(super) id: String,
    /// What it says.
    statement: String,
    /// The status written in the block.
    stated: &'static str,
    /// The established claims that give it.
    support: Vec<String>,
}

/// One statement the library already entails.
#[derive(Clone, Debug)]
struct Redundant {
    id: String,
    statement: String,
    /// The claim it follows from, which is where a reader should go instead.
    covered_by: Vec<String>,
}

/// Two claims the run holds that cannot both be true.
#[derive(Clone, Debug)]
struct Conflict {
    held: String,
    against: String,
    /// The chain from `held` to the claim that does the contradicting.
    through: Vec<String>,
}

/// What following the entailment edges found.
#[derive(Debug, Default)]
pub(super) struct Closure {
    upgrades: Vec<Upgrade>,
    redundant: Vec<Redundant>,
    conflicts: Vec<Conflict>,
    /// Edges naming a claim that does not exist.
    dangling: Vec<(String, String)>,
    /// Claims that transitively support themselves.
    circular: Vec<String>,
    /// Every claim the library entails, whatever its own block says.
    ///
    /// Separate from `redundant` because the two answer different questions.
    /// The report lists what adds nothing *new*; the graph asks whether a
    /// lemma is settled, and one the library establishes for free is settled
    /// whether or not anybody has updated its status line yet.
    covered: BTreeSet<String>,
}

/// Everything reachable from each claim by following `follows-from` backwards.
///
/// Keyed by claim, valued by the set of claims it is a consequence of, closed
/// transitively. Computed once and shared by all three reports, because each of
/// them is a different question about the same relation.
fn support_sets(claims: &[Claim]) -> BTreeMap<String, BTreeSet<String>> {
    let direct: BTreeMap<&str, &Vec<String>> = claims
        .iter()
        .map(|claim| (claim.id.as_str(), &claim.follows_from))
        .collect();
    let mut closed: BTreeMap<String, BTreeSet<String>> = BTreeMap::new();
    for claim in claims {
        let mut reached: BTreeSet<String> = BTreeSet::new();
        let mut frontier: Vec<String> = claim.follows_from.clone();
        // Breadth-first with a visited set rather than recursion, so a cycle in
        // the edges terminates instead of overflowing the stack. A cycle is a
        // thing roles do write — two lemmas each said to follow from the other
        // — and it is reported below rather than treated as impossible.
        while let Some(next) = frontier.pop() {
            if !reached.insert(next.clone()) {
                continue;
            }
            if let Some(further) = direct.get(next.as_str()) {
                frontier.extend((*further).clone());
            }
        }
        closed.insert(claim.id.clone(), reached);
    }
    closed
}

/// Every claim the library establishes, written status or derived.
///
/// A fixed point rather than one pass over the written statuses, and the
/// difference is the whole of what a transitive closure buys. With `a` proved,
/// `b` a consequence of `a`, and `c` a consequence of `b`, a single pass
/// reports only `b`: it reads `c`'s support and finds the word `asserted` in
/// `b`'s block, because nothing has written the upgrade back yet. The chain of
/// sound steps above the first is exactly what the Equational Theories Project
/// got its thirty-sevenfold return from, so stopping at one hop discards most
/// of the value.
///
/// Bounded by the claim count: each round either settles a claim or is the
/// last. Claims in `circular` are never settled here however their supports
/// stand, which is what stops two claims resting on each other from
/// bootstrapping themselves into an establishment neither has.
fn settled_set(
    claims: &[Claim],
    by_id: &BTreeMap<&str, &Claim>,
    circular: &BTreeSet<String>,
) -> BTreeSet<String> {
    let mut settled: BTreeSet<String> = claims
        .iter()
        .filter(|claim| !claim.id.is_empty() && is_established(claim.status))
        .map(|claim| claim.id.clone())
        .collect();
    for _ in 0..=claims.len() {
        let mut grew = false;
        for claim in claims {
            if claim.id.is_empty()
                || settled.contains(&claim.id)
                || circular.contains(&claim.id)
                || claim.follows_from.is_empty()
            {
                continue;
            }
            let supported = claim.follows_from.iter().all(|id| {
                by_id.contains_key(id.as_str()) && settled.contains(id.as_str())
            });
            if supported {
                settled.insert(claim.id.clone());
                grew = true;
            }
        }
        if !grew {
            break;
        }
    }
    settled
}

/// Follows the entailment edges over one library.
pub(super) fn build(ledger: &Ledger) -> Closure {
    let claims = ledger.all();
    let by_id: BTreeMap<&str, &Claim> = claims
        .iter()
        .filter(|claim| !claim.id.is_empty())
        .map(|claim| (claim.id.as_str(), claim))
        .collect();
    let support = support_sets(claims);
    // Every claim that supports itself, computed before anything reads the
    // relation. A cycle has to be known up front rather than skipped as it is
    // met: a claim outside the cycle resting on one inside it must not inherit
    // an establishment the cycle never had.
    let circular: BTreeSet<String> = claims
        .iter()
        .filter(|claim| {
            support
                .get(&claim.id)
                .is_some_and(|reached| reached.contains(&claim.id))
        })
        .map(|claim| claim.id.clone())
        .collect();
    let settled = settled_set(claims, &by_id, &circular);
    let mut closure = Closure::default();

    for claim in claims {
        if claim.id.is_empty() {
            continue;
        }
        let Some(reached) = support.get(&claim.id) else {
            continue;
        };
        for id in reached {
            if !by_id.contains_key(id.as_str()) {
                closure.dangling.push((claim.id.clone(), id.clone()));
            }
        }
        if circular.contains(&claim.id) {
            closure.circular.push(claim.id.clone());
            // A claim supporting itself supports nothing: every conclusion
            // drawn from it below would be drawn from the claim itself. It is
            // reported and then left out of the other three reports, which is
            // the only reading that does not manufacture an establishment.
            continue;
        }
        // Against the closure's own conclusion rather than the word written in
        // the block, which is the whole transitive half. A support that is
        // itself only a consequence of proved claims is established, and a
        // check that read its `status:` line would stop at the first such link
        // — leaving everything above it unreported however long the chain of
        // sound steps above it ran.
        let established: Vec<String> = claim
            .follows_from
            .iter()
            .filter(|id| settled.contains(id.as_str()))
            .cloned()
            .collect();
        let fully_supported =
            !claim.follows_from.is_empty() && established.len() == claim.follows_from.len();

        if fully_supported && !is_established(claim.status) {
            closure.upgrades.push(Upgrade {
                id: claim.id.clone(),
                statement: claim.statement.clone(),
                stated: claim.status.label(),
                support: established.clone(),
            });
        }
        // Only what the run already calls established. A claim that is
        // entailed *and* filed weaker is one fact, and it belongs under the
        // upgrade — where the line says what to do about it. Listing it here
        // as well printed the same id twice under two headings that read as
        // opposite advice: settle it, and it is not a result.
        if fully_supported {
            closure.covered.insert(claim.id.clone());
        }
        if fully_supported && is_established(claim.status) {
            closure.redundant.push(Redundant {
                id: claim.id.clone(),
                statement: claim.statement.clone(),
                covered_by: established,
            });
        }
        // A conflict the direct check misses: this claim is a consequence of
        // things the run holds, and something it entails contradicts a claim
        // the run also holds.
        for id in reached {
            let Some(support) = by_id.get(id.as_str()) else {
                continue;
            };
            for against in &support.contradicts {
                if by_id.contains_key(against.as_str()) && !claim.contradicts.contains(against) {
                    closure.conflicts.push(Conflict {
                        held: claim.id.clone(),
                        against: against.clone(),
                        through: vec![id.clone()],
                    });
                }
            }
        }
    }
    closure.dangling.sort();
    closure.dangling.dedup();
    closure
}

impl Closure {
    /// Whether a proposed statement is already entailed by the library.
    ///
    /// The Dalmatian test. Matching is by id, because that is the only
    /// comparison this runtime can make soundly — deciding that two English
    /// statements say the same thing is the model's job, and a runtime that
    /// guessed at it would suppress a real result.
    ///
    /// Read by the statement graph as well as by the report, and that is the
    /// join that makes the free upgrade worth anything: a lemma discharged by
    /// a claim the library *entails* is as settled as one discharged by a claim
    /// somebody proved, and a graph that only read written statuses would leave
    /// it blocked and offer the run its own theorem as work.
    pub(super) fn is_covered(&self, id: &str) -> bool {
        self.covered.contains(id)
    }

    /// How many free upgrades and unseen conflicts the closure found.
    pub(super) fn counts(&self) -> (usize, usize) {
        (self.upgrades.len(), self.conflicts.len())
    }

    /// The lines that reach the next attempt, or nothing.
    ///
    /// Only the upgrades and the conflicts. Redundancy is a fact about work
    /// already done and belongs in the file; an upgrade changes what the next
    /// attempt should even try, and a conflict means some of what it would
    /// build on is wrong.
    pub(super) fn briefing(&self) -> String {
        if self.upgrades.is_empty() && self.conflicts.is_empty() {
            return String::new();
        }
        let mut out = String::new();
        if !self.upgrades.is_empty() {
            out.push_str(
                "The library already establishes these, through claims it holds. Do not prove any \
                 of them again — mark the status and move on:\n",
            );
            for upgrade in self.upgrades.iter().take(MAX_ROWS) {
                let _ = writeln!(
                    out,
                    "- `{}` (filed as {}) follows from {}: {}",
                    upgrade.id,
                    upgrade.stated,
                    joined(&upgrade.support),
                    truncate(&upgrade.statement, FIELD_CHARS)
                );
            }
        }
        if !self.conflicts.is_empty() {
            out.push_str(
                "\nThe run is holding claims that cannot all be true. Settle this before building \
                 anything on either side:\n",
            );
            for conflict in self.conflicts.iter().take(MAX_ROWS) {
                let _ = writeln!(
                    out,
                    "- `{}` rests on `{}`, which contradicts `{}`",
                    conflict.held,
                    joined(&conflict.through),
                    conflict.against
                );
            }
        }
        out
    }

    /// Renders the derived file.
    pub(super) fn render(&self) -> String {
        let mut out = String::from(
            "# Entailment — what the library gives without new work\n\n\
             Derived from the `follows-from:` lines in every `claim` block, closed transitively. \
             Do not edit this file; the next note write re-derives it.\n\n\
             A claim written `follows-from: a, b` says `a` and `b` together give it. That single \
             edge is enough to answer three questions the claim ledger cannot: which claims the \
             run has already established without noticing, which proposals would add nothing, and \
             which pair of held beliefs cannot both be true.\n\n",
        );
        self.append_conflicts(&mut out);
        self.append_upgrades(&mut out);
        self.append_redundant(&mut out);
        self.append_circular(&mut out);
        self.append_dangling(&mut out);
        if self.upgrades.is_empty()
            && self.conflicts.is_empty()
            && self.redundant.is_empty()
            && self.circular.is_empty()
            && self.dangling.is_empty()
        {
            out.push_str(
                "_Nothing to derive yet. Add a `follows-from:` line to a `claim` block naming the \
                 claim ids it is a consequence of, and this file fills in._\n",
            );
        }
        out
    }

    /// Contradictions first, because they invalidate what is below them.
    fn append_conflicts(&self, out: &mut String) {
        if self.conflicts.is_empty() {
            return;
        }
        out.push_str(
            "## Cannot all be true — read this first\n\nNo single block states these. Each is a \
             claim the run holds whose support entails something that contradicts another claim \
             the run holds. One of the two is wrong, and everything resting on either is \
             suspect.\n\n",
        );
        for conflict in self.conflicts.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "- `{}` rests on `{}`, which is recorded as contradicting `{}`",
                conflict.held,
                joined(&conflict.through),
                conflict.against
            );
        }
        out.push('\n');
    }

    /// Free establishments, which is the section that saves attempts.
    fn append_upgrades(&self, out: &mut String) {
        if self.upgrades.is_empty() {
            return;
        }
        out.push_str(
            "## Established for free\n\nEvery claim these rest on is established, so these are \
             too, whatever status their block carries. Proving one again spends an attempt on \
             something the run already has — update the status instead.\n\n",
        );
        for upgrade in self.upgrades.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "- `{}` — filed as {}, follows from {}\n  - {}",
                upgrade.id,
                upgrade.stated,
                joined(&upgrade.support),
                cell(&truncate(&upgrade.statement, FIELD_CHARS))
            );
        }
        out.push('\n');
    }

    /// The Dalmatian filter's output.
    fn append_redundant(&self, out: &mut String) {
        if self.redundant.is_empty() {
            return;
        }
        out.push_str(
            "## Already entailed\n\nThese add nothing the library did not have. That is not a \
             criticism of them — a consequence worth naming is worth a block — but a *proposal* \
             that lands in this list is not a result, and the cheapest time to find that out is \
             before an attempt is spent on it.\n\n",
        );
        for entry in self.redundant.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "- `{}` is covered by {}: {}",
                entry.id,
                joined(&entry.covered_by),
                cell(&truncate(&entry.statement, FIELD_CHARS))
            );
        }
        out.push('\n');
    }

    /// Claims that support themselves.
    fn append_circular(&self, out: &mut String) {
        if self.circular.is_empty() {
            return;
        }
        out.push_str(
            "\n## Supporting themselves\n\nEach of these follows, through the edges on disk, from \
             itself. Whatever the statements are worth, this chain establishes none of them, and \
             nothing above counts them as support.\n\n",
        );
        for id in self.circular.iter().take(MAX_ROWS) {
            let _ = writeln!(out, "- `{id}`");
        }
    }

    /// Edges naming a claim nobody wrote.
    fn append_dangling(&self, out: &mut String) {
        if self.dangling.is_empty() {
            return;
        }
        out.push_str(
            "\n## Following from nothing recorded\n\nEach edge below names a claim no block on \
             disk carries. Either the id is misspelled, or the run is deriving something from a \
             belief nobody wrote down.\n\n",
        );
        for (claim, missing) in self.dangling.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "- `{claim}` follows from `{missing}`, which does not exist"
            );
        }
    }
}

/// Renders an id list as backticked names.
fn joined(ids: &[String]) -> String {
    if ids.is_empty() {
        return "nothing".to_string();
    }
    ids.iter()
        .map(|id| format!("`{id}`"))
        .collect::<Vec<_>>()
        .join(", ")
}

fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
}

/// Builds the closure from what is on disk.
pub(super) fn collect(workspace: &Path) -> Closure {
    build(&super::claims::collect(workspace))
}

/// Re-derives the report and rewrites [`CLOSURE_PATH`].
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) {
    let closure = collect(documents.root());
    let _ = documents
        .write_runtime(CLOSURE_PATH, &closure.render())
        .await;
    super::folder_index::record_description(
        documents,
        CLOSURE_PATH,
        "Derived: what the claim library entails without new work — statements already \
         established through their support, proposals it already covers, and pairs of held \
         beliefs that cannot both be true. Rewritten on every note write; do not edit.",
    )
    .await;
}

#[cfg(test)]
#[path = "closure_test.rs"]
mod test;
