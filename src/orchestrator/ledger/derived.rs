//! Reading part of a ledger that only exists as a rendered file.
//!
//! Nine of the eleven ledgers are [`Source::Derived`](super::spec::Source):
//! `claims`, `approaches`, `threads`, `frontier` and the rest are walked and
//! rendered by their own modules, so the engine holds no entries for them and
//! `read_ledger` answered out of the file instead.
//!
//! It answered with the *whole* file, and ignored every argument it advertised.
//! `id`, `status`, `query`, `sort` and `limit` are in the tool's schema and
//! worked only for the two engine-backed ledgers; asking `read_ledger` for one
//! claim by id returned all of them. There was no size bound either — the
//! measured cost is 7,488 tokens for `CLAIMS.md` and 86 KB for a live
//! `APPROACHES.md`, paid on every call, to answer a question about one row.
//!
//! Advertising a filter that silently does nothing is worse than not offering
//! one: a role that asks for one entry and receives four hundred concludes the
//! ledger is unusable, not that the argument was dropped.
//!
//! # What this can and cannot do
//!
//! It works on the rendered Markdown, because that is all there is. The shape
//! every one of these files shares is `## heading`, then entries as list items
//! or table rows, each possibly followed by indented continuation lines. So an
//! *entry* here is a top-level line plus everything indented under it, which is
//! enough to select by id or by text and to say what was left out.
//!
//! It cannot reason about the entry — it does not know a claim's status from
//! its hypotheses. `status` is matched as text like anything else, which is
//! honest about what a rendered file supports and is why the engine-backed path
//! is still the one that filters properly.

use std::fmt::Write as _;

use serde_json::Value;

/// How much of a rendered ledger one unfiltered read may return.
///
/// The per-ledger prompt budget, in characters. A read that hits this is
/// reporting a defect as much as a size: a derived ledger reaching it means a
/// section of it renders unbounded, which `ceiling_test` exists to catch.
fn ceiling() -> usize {
    usize::try_from(super::budget_tokens())
        .unwrap_or(usize::MAX)
        .saturating_mul(super::super::shared_context::CHARS_PER_TOKEN)
}

/// One rendered entry: its own line, and the lines indented under it.
struct Block<'a> {
    heading: &'a str,
    lines: Vec<&'a str>,
}

impl Block<'_> {
    fn text(&self) -> String {
        self.lines.join("\n")
    }

    /// Whether this block mentions `needle`, ignoring case.
    fn mentions(&self, needle: &str) -> bool {
        self.lines
            .iter()
            .any(|line| line.to_ascii_lowercase().contains(needle))
    }
}

/// Splits a rendered ledger into its headings and entry blocks.
///
/// Anything before the first entry — the title, the preamble, a section blurb —
/// is not a block and is not returned. A filtered read is about the entries.
fn blocks(rendered: &str) -> Vec<Block<'_>> {
    let mut found: Vec<Block<'_>> = Vec::new();
    let mut heading = "";
    for line in rendered.lines() {
        if let Some(rest) = line.trim_start().strip_prefix("## ") {
            heading = rest.trim();
            continue;
        }
        let is_entry = line.starts_with("- ") || (line.starts_with('|') && !line.contains("---"));
        if is_entry {
            found.push(Block {
                heading,
                lines: vec![line],
            });
        } else if !line.trim().is_empty()
            && line.starts_with(char::is_whitespace)
            && let Some(last) = found.last_mut()
        {
            // A continuation of the entry above: the engine writes prose fields
            // as indented children, and the hand-written renderers do the same.
            last.lines.push(line);
        }
    }
    found
}

/// Answers one `read_ledger` call against a rendered file.
///
/// With no filter this is the file, bounded. With one it is the matching
/// entries, grouped under their headings, and a count of what did not match.
pub(super) fn select(path: &str, rendered: &str, arguments: &Value) -> String {
    let wanted_id = super::tool::text(arguments, "id").to_ascii_lowercase();
    let query = super::tool::text(arguments, "query").to_ascii_lowercase();
    let status = super::tool::text(arguments, "status").to_ascii_lowercase();
    let limit = arguments
        .get("limit")
        .and_then(Value::as_u64)
        .and_then(|value| usize::try_from(value).ok());

    let filtering = !wanted_id.is_empty() || !query.is_empty() || !status.is_empty();
    if !filtering && limit.is_none() {
        return bounded(path, rendered);
    }

    let all = blocks(rendered);
    let total = all.len();
    let matching: Vec<&Block<'_>> = all
        .iter()
        .filter(|block| {
            (wanted_id.is_empty() || block.mentions(&wanted_id))
                && (query.is_empty() || block.mentions(&query))
                // A rendered file carries the status as text, in the row or in
                // the heading of the section the row is under.
                && (status.is_empty()
                    || block.mentions(&status)
                    || block.heading.to_ascii_lowercase().contains(&status))
        })
        .collect();

    if matching.is_empty() {
        return format!(
            "Nothing in `{path}` matches. It holds {total} entr{}. Read it without a filter to \
             see them.",
            if total == 1 { "y" } else { "ies" }
        );
    }

    let kept = limit.unwrap_or(matching.len()).min(matching.len());
    let mut out = format!(
        "{} of {total} entr{} in `{path}` match:\n",
        matching.len(),
        if total == 1 { "y" } else { "ies" }
    );
    let mut heading = "";
    for block in matching.iter().take(kept) {
        if block.heading != heading {
            heading = block.heading;
            if !heading.is_empty() {
                let _ = write!(out, "\n## {heading}\n\n");
            }
        }
        out.push_str(&block.text());
        out.push('\n');
    }
    if kept < matching.len() {
        let _ = write!(
            out,
            "\n_[{} further match(es) not shown; raise `limit` or narrow the query.]_\n",
            matching.len() - kept
        );
    }
    super::super::capture::clamp(&out, ceiling())
}

/// An unfiltered read, bounded and honest about the bound.
fn bounded(path: &str, rendered: &str) -> String {
    if rendered.len() <= ceiling() {
        return rendered.to_string();
    }
    let mut out = super::super::capture::clamp(rendered, ceiling());
    let _ = write!(
        out,
        "\n\n_[`{path}` is larger than one read may return. Ask again with `id`, `query` or \
         `status` to select what you need. A derived ledger this large also means a section of it \
         renders unbounded, which is a defect in the module that renders it.]_\n"
    );
    out
}

#[cfg(test)]
#[path = "derived_test.rs"]
mod test;
