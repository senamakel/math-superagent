//! Text shortening shared by every module that renders a derived ledger.
//!
//! This was one function copied into six modules — `claims`, `threads`,
//! `requests`, `frontier`, `digest`, and `oeis` — and by the time it was
//! counted, two copies had already drifted: `oeis` had lost the word-boundary
//! cut and shortened mid-word, and `digest` had lost the leading `trim`, so the
//! same sentence rendered differently depending on which ledger it landed in.
//! That is the fault `code_layout::plan` measures in the agent's own programs —
//! a routine defined in three or more places, where a check passing against one
//! copy says nothing about the others — and the runtime was not being held to
//! it.

/// Shortens `text` to at most `limit` characters, cutting at a word boundary.
///
/// The bound is in `char`s rather than bytes because these strings are rendered
/// into Markdown tables that a reader counts by eye, and because slicing a
/// multi-byte character in half would panic.
///
/// Leading and trailing whitespace is removed first, so a field that arrived
/// with a stray newline does not spend its budget on it. When the text is
/// already short enough it is returned as-is, with no ellipsis for a truncation
/// that did not happen.
pub(super) fn truncate(text: &str, limit: usize) -> String {
    let text = text.trim();
    if text.chars().count() <= limit {
        return text.to_string();
    }
    let head: String = text.chars().take(limit).collect();
    // Cutting at the last space keeps the final word whole. A run of text with
    // no whitespace at all — a URL, a long identifier — has no boundary to cut
    // at, so it keeps the character bound instead.
    let head = head
        .rsplit_once(char::is_whitespace)
        .map_or(head.as_str(), |(body, _)| body);
    format!("{}…", head.trim_end())
}

#[cfg(test)]
mod test;
