//! Builds the bounded stand-in filed under `research/` for a fresh download.
//!
//! The first version of this took the leading four thousand characters. For a
//! reference page that is the navigation and the lede; for a paper — the
//! source that matters most — it is the title, the abstract, and half the
//! introduction. That is precisely the part the scholar is told to throw away:
//! "compress by dropping what the source says about itself — motivation,
//! history, related work — and keeping the statements and their consequences".
//! So the run paid for a thousand tokens of exactly the wrong thousand tokens,
//! and whether the full text was worth opening still had to be decided by
//! opening it.
//!
//! A mathematical source carries its payload in labelled statements —
//! `Theorem`, `Lemma`, `Definition`, `Proposition`, `Corollary`, `Algorithm` —
//! and those labels are mechanically locatable. So is the heading outline, and
//! so is the abstract. This module assembles a digest out of those three under
//! the same budget: the outline says what is in the document and where, the
//! abstract says what it claims, and the statements are what the run would
//! have gone looking for.
//!
//! It is a fallback-first design. A document with no headings and no labelled
//! statements — a plain-text table, a short note — digests to the leading
//! characters exactly as before, because for that shape the leading characters
//! genuinely are the document.

/// Characters the whole digest is held to.
///
/// About a thousand tokens: enough to tell whether the full text is worth
/// opening, which is the only decision this file exists to support.
pub(super) const DIGEST_CHARS: usize = 4_000;

/// Characters the heading outline may take.
///
/// Small on purpose. The outline is navigation, not content: it says a section
/// on the pass rule exists at §4, and the reader who needs §4 opens the full
/// text. Letting it grow would spend the statement budget on a table of
/// contents.
const OUTLINE_CHARS: usize = 700;

/// Headings the outline may list.
const OUTLINE_ROWS: usize = 30;

/// Characters the abstract may take.
const ABSTRACT_CHARS: usize = 1_100;

/// Characters one heading row is truncated to.
const HEADING_CHARS: usize = 90;

/// Longest a single statement may run before it is cut.
///
/// A proof that runs for two pages is not a statement, and one of them would
/// eat the whole budget. The statement is the part before the proof.
const STATEMENT_CHARS: usize = 700;

/// Words that begin a labelled mathematical statement.
///
/// Everything a paper marks out as a result the reader is meant to take away.
/// `Proof` is deliberately absent: it is the argument for a statement already
/// captured, it is the longest block on the page, and a run that needs it
/// needs the full text anyway.
const STATEMENT_LABELS: [&str; 10] = [
    "theorem",
    "lemma",
    "proposition",
    "corollary",
    "definition",
    "algorithm",
    "conjecture",
    "claim",
    "fact",
    "axiom",
];

/// Section heading marking the reference list appended by the converter.
const LINKS_HEADING: &str = "## Links";

/// Builds the digest filed at level 1 for a source whose full text is at
/// `full_relative`.
///
/// Returns `full` unchanged when it is already inside the budget, so a small
/// source is not decorated with a notice about truncation that did not happen.
pub(super) fn digest(full: &str, full_relative: &str) -> String {
    if full.chars().count() <= DIGEST_CHARS {
        return full.to_string();
    }
    let (body, _) = split_links(full);
    let provenance = provenance(full);
    let blocks = blocks(body);

    let outline = outline(&blocks);
    let abstract_text = abstract_text(&blocks);
    // The statements get whatever the other two did not use, and never less
    // than half the budget: they are the reason this file exists.
    let spent = outline.chars().count() + abstract_text.chars().count();
    let statements = statements(&blocks, DIGEST_CHARS.saturating_sub(spent).max(DIGEST_CHARS / 2));

    if outline.is_empty() && statements.is_empty() {
        return leading(full, full_relative);
    }

    let mut out = String::with_capacity(DIGEST_CHARS + 512);
    out.push_str(&header(full_relative));
    if !provenance.is_empty() {
        out.push_str(&provenance);
        out.push_str("\n\n");
    }
    for (heading, section) in [
        ("## What is in it", &outline),
        ("## What it claims", &abstract_text),
        ("## Statements it makes", &statements),
    ] {
        if section.is_empty() {
            continue;
        }
        out.push_str(heading);
        out.push_str("\n\n");
        out.push_str(section);
        out.push_str("\n\n");
    }
    out.push_str(&footer(full, full_relative));
    out
}

/// The instruction the digest carries above its content.
///
/// The digest is a placeholder with a job: it is what the scholar replaces,
/// and a file that does not say so gets left as it was found.
fn header(full_relative: &str) -> String {
    format!(
        "> **Digest only — read this first.** This is a structural digest of the source: its \
         outline, what it claims, and the statements it makes. The complete text is at \
         `{full_relative}`; open that only when this file does not answer the question, because it \
         is large. Replace this digest with a summary of what the source establishes and what it \
         implies for this problem — under 1000 tokens, specific enough that nobody needs the full \
         text, and wikilinking it so they can still reach it.\n\n"
    )
}

/// The note closing the digest, saying what was left out and where it is.
fn footer(full: &str, full_relative: &str) -> String {
    format!(
        "*[digest of a {} character source; every section, statement, and proof in full at \
         `{full_relative}`]*\n",
        full.chars().count()
    )
}

/// Truncation to the leading characters, for a source with no structure to
/// read.
///
/// A plain-text table or a short note has no headings and no labelled
/// statements, and for that shape the leading characters genuinely are the
/// document rather than its preamble.
fn leading(full: &str, full_relative: &str) -> String {
    let head: String = full.chars().take(DIGEST_CHARS).collect();
    let head = head
        .rsplit_once('\n')
        .map_or(head.as_str(), |(body, _)| body);
    format!(
        "{}{head}\n\n*[excerpt ends; {} characters not shown — see `{full_relative}`]*\n",
        header(full_relative),
        full.chars().count().saturating_sub(head.chars().count())
    )
}

/// Splits the converted text from the reference list the converter appended.
///
/// The links are not dropped so much as relocated: they are the run's citation
/// frontier and are carried by `research/FRONTIER.md`, so repeating them here
/// would spend the digest budget on URLs nobody is going to read in this file.
pub(super) fn split_links(full: &str) -> (&str, &str) {
    match full.find(&format!("\n{LINKS_HEADING}\n")) {
        Some(at) => (&full[..at], &full[at..]),
        None => (full, ""),
    }
}

/// Returns the converter's provenance comment, if the document carries one.
fn provenance(full: &str) -> String {
    full.lines()
        .take(3)
        .find(|line| line.trim_start().starts_with("<!-- source:"))
        .unwrap_or_default()
        .to_string()
}

/// Splits a document into paragraph blocks.
///
/// The converter collapses runs of blank lines to one, so a blank line is a
/// reliable block separator. Headings are single lines and therefore already
/// their own blocks.
fn blocks(body: &str) -> Vec<&str> {
    body.split("\n\n")
        .map(str::trim)
        .filter(|block| !block.is_empty() && !block.starts_with("<!--"))
        .collect()
}

/// Whether a block is a Markdown heading.
fn is_heading(block: &str) -> bool {
    block.starts_with('#')
}

/// Renders the heading outline, bounded in both rows and characters.
fn outline(blocks: &[&str]) -> String {
    let mut out = String::new();
    let mut rows = 0;
    for block in blocks.iter().filter(|block| is_heading(block)) {
        if rows >= OUTLINE_ROWS || out.chars().count() >= OUTLINE_CHARS {
            out.push_str("- …\n");
            break;
        }
        let level = block.chars().take_while(|c| *c == '#').count();
        let text = truncate(block.trim_start_matches('#').trim(), HEADING_CHARS);
        if text.is_empty() {
            continue;
        }
        // Two spaces per level below the top, so the outline reads as the
        // document's shape rather than a flat list of names.
        let indent = "  ".repeat(level.saturating_sub(1).min(4));
        out.push_str(&format!("{indent}- {text}\n"));
        rows += 1;
    }
    out
}

/// Extracts the abstract, or the opening prose when there is no abstract.
///
/// A paper labels it; a reference page does not, and for that shape the
/// opening paragraphs answer the same question — what is this about.
fn abstract_text(blocks: &[&str]) -> String {
    let labelled = blocks
        .iter()
        .position(|block| {
            let stripped = strip_emphasis(block.trim_start_matches('#').trim());
            stripped.len() < 40 && stripped.to_ascii_lowercase().starts_with("abstract")
        })
        .map(|at| at + 1);
    let start = match labelled {
        Some(start) => start,
        // No label: the first non-heading block that is prose rather than a
        // one-line byline is as close to an abstract as this document has.
        None => blocks
            .iter()
            .position(|block| !is_heading(block) && block.chars().count() > 200)
            .map_or(blocks.len(), |at| at),
    };
    let mut out = String::new();
    for block in blocks.iter().skip(start) {
        if is_heading(block) || out.chars().count() >= ABSTRACT_CHARS {
            break;
        }
        out.push_str(&truncate(
            block,
            ABSTRACT_CHARS.saturating_sub(out.chars().count()),
        ));
        out.push_str("\n\n");
    }
    out.trim().to_string()
}

/// Collects the labelled statements, in document order, up to `budget`.
fn statements(blocks: &[&str], budget: usize) -> String {
    let mut out = String::new();
    for block in blocks {
        if out.chars().count() >= budget {
            out.push_str("\n*[further statements in the full text]*\n");
            break;
        }
        if !is_statement(block) {
            continue;
        }
        let remaining = budget.saturating_sub(out.chars().count());
        out.push_str(&truncate(block, STATEMENT_CHARS.min(remaining)));
        out.push_str("\n\n");
    }
    out.trim().to_string()
}

/// Whether a block opens with a labelled mathematical statement.
///
/// Matched on the first word after any heading, emphasis, or quote marker,
/// because a paper writes the label a dozen ways — `Theorem 3.1.`,
/// `**Lemma 2 (Li).**`, `### Definition`, `THEOREM A` — and they all mean the
/// same thing. Requiring the label to *start* the block is what keeps this
/// from matching every sentence that mentions a theorem.
fn is_statement(block: &str) -> bool {
    let stripped = strip_emphasis(block.trim_start_matches('#').trim_start_matches('>').trim());
    let first: String = stripped
        .chars()
        .take_while(|c| c.is_alphabetic())
        .collect::<String>()
        .to_ascii_lowercase();
    if !STATEMENT_LABELS.contains(&first.as_str()) {
        return false;
    }
    // `Theorems of this kind are…` is prose about theorems, not a theorem. A
    // real label is followed by a number, a bracket, or a full stop.
    stripped[first.len()..]
        .chars()
        .find(|c| !c.is_whitespace())
        .is_none_or(|next| !next.is_alphabetic())
}

/// Removes the emphasis and quote markers a label is commonly wrapped in.
fn strip_emphasis(text: &str) -> &str {
    text.trim_start_matches(['*', '_', '`', '"', '\'', ' '])
}

/// Cuts `text` to `limit` characters at a word boundary where it can.
fn truncate(text: &str, limit: usize) -> String {
    if text.chars().count() <= limit {
        return text.to_string();
    }
    let head: String = text.chars().take(limit).collect();
    let cut = head
        .rsplit_once(char::is_whitespace)
        .map_or(head.as_str(), |(body, _)| body);
    format!("{}…", cut.trim_end())
}

#[cfg(test)]
mod test;
