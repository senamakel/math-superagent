//! The index: what a role carries in its prompt, instead of the whole ledger.
//!
//! Bounding the sections took the nine derived ledgers from 404,873 tokens
//! across the twenty-two assembled prompts to 259,175. That is a real saving and
//! it is not the end of the argument, because most of what is left is still
//! being re-sent on every model call to answer a question nobody is asking yet.
//!
//! # Why a description is not enough
//!
//! The obvious move is to replace each ledger with a sentence saying it exists
//! and how to read it. That fails, and the reason is worth stating precisely:
//! the obligation these files discharge is *specific*. It is not "be aware there
//! are approaches", it is **do not re-propose this one**. It is not "claims
//! exist", it is **do not re-prove this statement**. A description cannot
//! discharge either, because neither is about the ledger — both are about the
//! entries.
//!
//! So an index keeps every entry's *identity* and drops the *reasoning*: one
//! line per entry, its id, its status, and a headline. Measured against one live
//! workspace, per prompt that carries the file:
//!
//! | ledger | bounded | indexed |
//! | --- | ---: | ---: |
//! | `APPROACHES` | 8,822 | ~2,100 |
//! | `WEAKENED` | 7,630 | ~1,300 |
//! | `CLAIMS` | 7,488 | ~3,700 |
//! | `BACKWARD` | 5,186 | ~800 |
//!
//! # Three things that table settles
//!
//! **The win is per-ledger, not uniform.** `APPROACHES` collapses furthest
//! because its payload is refutation prose nobody needs until they are actually
//! considering that approach — the id and a one-line reason discharge the
//! obligation, and the rest is elaboration. `CLAIMS` only halves, because a
//! claim's *statement* is the payload and cannot be indexed away. So
//! [`HEADLINE`] is a per-caller argument rather than one constant: the claim
//! ledger keeps more of each line than the approach ledger does.
//!
//! **Indexing a small ledger costs more than it saves.** `research/ENTAILMENT.md`
//! is 266 tokens; an index of it, with a header explaining what it is and how to
//! read the rest, comes to about 440. [`worth_indexing`] is that finding made
//! mechanical, and a uniform rule would have made two files worse.
//!
//! **The saving is only real if the pull happens.** A role that never calls
//! `read_ledger` is cheaper and dumber, which is strictly worse than before the
//! bound: it reads a shortened list, concludes the run holds nothing more, and
//! re-proposes what was cut. So every index ends with the exact call that
//! fetches the rest, and a test asserts every role reading one is told the copy
//! is shortened.

use std::fmt::Write as _;

use super::budget;
use crate::orchestrator::text::truncate;

/// Characters of headline one index line carries by default.
///
/// Enough for the shape of a reason — *"needs f to be D-finite and it is not"* —
/// and not enough for the argument behind it. A caller whose headline *is* the
/// payload passes its own; see the module documentation on `CLAIMS`.
pub(in crate::orchestrator) const HEADLINE: usize = 110;

/// Tokens below which a ledger is routed whole rather than indexed.
///
/// An index is not free: it carries a header saying what the file is and how to
/// read the rest of it. Under this, that header costs more than the entries it
/// replaces, and the honest thing is to send the file.
const WORTH_INDEXING: usize = 600;

/// Whether `rendered` is large enough that an index of it saves anything.
pub(in crate::orchestrator) fn worth_indexing(rendered: &str) -> bool {
    rendered.chars().count() / super::CHARS_PER_TOKEN > WORTH_INDEXING
}

/// Cleans a headline, or returns nothing when it says nothing.
///
/// Two things, both from reading what the real ledgers actually produce.
///
/// A field written into a Markdown table cell arrives with the cell's own
/// punctuation on the front — `| The exact telescoping identity…` or
/// `> Refuted on three grounds` — and an index line spends its first two
/// characters on a pipe. The headline is the scarcest space in the whole
/// prompt, and that is the least useful thing that could be in it.
///
/// And a field the writer left empty falls back, in several of these ledgers,
/// to the entry's own slug. Rendering that gives `` `ducci-potential-max-decrease`
/// (proposed) — ducci-potential-max-decrease``, which is not a summary of
/// anything: it reads as though the run recorded something and says less than
/// the bare id would. Better to render the id alone and let the emptiness show.
fn headline_of(headline: &str, id: &str) -> String {
    let cleaned = headline
        .trim()
        .trim_start_matches(['|', '>', '-', '*', '#', ' '])
        .trim();
    if cleaned.eq_ignore_ascii_case(id) {
        return String::new();
    }
    cleaned.to_string()
}

/// One entry, reduced to what a prompt has to carry.
pub(in crate::orchestrator) struct Row<'a> {
    /// How the entry is named in `read_ledger` and in every other ledger.
    pub(in crate::orchestrator) id: &'a str,
    /// Where it stands. Empty when the ledger has no statuses.
    pub(in crate::orchestrator) status: &'a str,
    /// The one thing about it a reader has to know without pulling it.
    pub(in crate::orchestrator) headline: &'a str,
}

/// Renders an index over `rows`.
///
/// `slug` is what `read_ledger` is called with, and it is in the closing line
/// rather than left implicit: an index that says *there is more* without saying
/// how to get it is the failure this whole module has to avoid.
///
/// Two things are hoisted out of the rows because repeating them per row is
/// paying for a constant. A status every row shares is stated once — a claims
/// index whose seventy lines all read `(asserted, yes)` spent six hundred
/// characters saying nothing that varies. And the closing instruction is one
/// line rather than a paragraph, because the same instruction is in the ledger
/// brief above it in every prompt that carries an index. What the line cannot
/// drop is the call itself: the searcher holds the claim index and is
/// deliberately *not* sent the brief, so the way to the full entry has to be on
/// the page.
pub(in crate::orchestrator) fn render<'a>(
    slug: &str,
    title: &str,
    purpose: &str,
    rows: impl IntoIterator<Item = Row<'a>>,
    headline: usize,
) -> String {
    let rows: Vec<Row<'a>> = rows.into_iter().collect();
    let shared = shared_status(&rows);
    let mut out = format!("# {title} — index\n\n{purpose}\n\n");
    if let Some(status) = &shared {
        let _ = write!(out, "Every row below is `{status}`.\n\n");
    }
    let (body, dropped) = budget::listed(rows, budget::MAX_LISTED, |body, row| {
        let _ = write!(body, "- `{}`", row.id);
        if shared.is_none() && !row.status.trim().is_empty() {
            let _ = write!(body, " ({})", row.status.trim());
        }
        let summary = headline_of(row.headline, row.id);
        if !summary.is_empty() {
            let _ = write!(body, " — {}", truncate(&summary, headline));
        }
        body.push('\n');
    });
    if body.is_empty() {
        out.push_str("_Nothing recorded yet._\n");
        return out;
    }
    out.push_str(&body);
    if dropped > 0 {
        let _ = write!(out, "\n_{dropped} more, reachable the same way._\n");
    }
    let _ = write!(
        out,
        "\n_Index only — every line above is shortened, and the run holds more on each of them. \
         `read_ledger {{ ledger: \"{slug}\", id: \"…\" }}` returns one in full; `status`, `query` \
         and `limit` narrow it._\n"
    );
    out
}

/// The status every row shares, when they share one.
///
/// `None` for a ledger with no statuses, for a single row — one row does not
/// establish that a value is constant, and hoisting it costs more than it saves
/// — and for the ordinary case where the status is the thing worth reading.
fn shared_status(rows: &[Row<'_>]) -> Option<String> {
    if rows.len() < 2 {
        return None;
    }
    let first = rows.first()?.status.trim();
    if first.is_empty() {
        return None;
    }
    rows.iter()
        .all(|row| row.status.trim() == first)
        .then(|| first.to_string())
}

#[cfg(test)]
#[path = "index_test.rs"]
mod test;
