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
pub(in crate::orchestrator) fn render<'a>(
    slug: &str,
    title: &str,
    purpose: &str,
    rows: impl IntoIterator<Item = Row<'a>>,
    headline: usize,
) -> String {
    let mut out = format!("# {title} — index\n\n{purpose}\n\n");
    let (body, dropped) = budget::listed(rows, budget::MAX_LISTED, |body, row| {
        let _ = write!(body, "- `{}`", row.id);
        if !row.status.trim().is_empty() {
            let _ = write!(body, " ({})", row.status.trim());
        }
        if !row.headline.trim().is_empty() {
            let _ = write!(body, " — {}", truncate(row.headline, headline));
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
        "\n**This is the index, not the ledger.** Each line is shortened to its \
         identity. Whatever you actually need — the full statement, the whole reason \
         something closed, the detail of an entry — is one call away and is *not* \
         above:\n\n```\nread_ledger {{ ledger: \"{slug}\", id: \"<one of the ids above>\" }}\n\
         read_ledger {{ ledger: \"{slug}\", status: \"<one of the statuses above>\" }}\n```\n\n\
         Do not conclude from this page that the run holds nothing more on a subject. It \
         holds more on every line of it.\n"
    );
    out
}

#[cfg(test)]
#[path = "index_test.rs"]
mod test;
