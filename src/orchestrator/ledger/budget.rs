//! Bounds for the list sections a derived ledger renders below its table.
//!
//! See [`super`] for why these are shared rather than per-module.

use std::fmt::Write as _;

/// Rows one list section renders.
///
/// Larger than a table's `MAX_ROWS`, and deliberately: a table is scanned, so a
/// long one is unreadable, while a list of what the run has closed is *read for
/// what is on it* — the inventor's whole obligation is not to re-propose
/// anything named there. Dropping a row costs more here than it does in a
/// table, so the bound is looser and the per-row prose bound is what does the
/// work.
pub(in crate::orchestrator) const MAX_LISTED: usize = 40;

/// Characters one prose field in a list section is held to.
///
/// Sized against [`super::super::board`]'s `BODY_CHARS`, for the same reason:
/// long enough to carry why something closed — *"it needs f to be D-finite and
/// it is not"* — and short enough that forty of them do not become a document.
/// The full text is always one read away, and every caller says where.
pub(in crate::orchestrator) const REASON_CHARS: usize = 600;

/// Renders at most `max` of `items`, and reports how many were left out.
///
/// The count is the point. A section cut to its bound and rendered as though
/// complete tells the reader the run holds nothing more, which is the failure
/// this whole module exists to prevent — so the caller is handed the number and
/// is expected to say it, along with where the rest is. See [`elided`].
pub(in crate::orchestrator) fn listed<T>(
    items: impl IntoIterator<Item = T>,
    max: usize,
    mut render: impl FnMut(&mut String, T),
) -> (String, usize) {
    let mut out = String::new();
    let mut seen = 0_usize;
    for item in items {
        seen += 1;
        if seen > max {
            continue;
        }
        render(&mut out, item);
    }
    (out, seen.saturating_sub(max))
}

/// The line a caller appends when [`listed`] left rows out.
///
/// Empty when it did not, so a caller can append it unconditionally rather than
/// branching — a branch each of five modules would have written separately, and
/// one of them would have got wrong.
pub(in crate::orchestrator) fn elided(dropped: usize, where_the_rest_is: &str) -> String {
    if dropped == 0 {
        return String::new();
    }
    let mut out = String::new();
    let _ = write!(
        out,
        "\n_{dropped} more not shown here; they are in `{where_the_rest_is}`._\n"
    );
    out
}

#[cfg(test)]
#[path = "budget_test.rs"]
mod test;
