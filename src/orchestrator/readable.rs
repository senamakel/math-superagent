//! Converts downloaded bytes into Markdown an agent can actually read.
//!
//! Before this, a document was written to the workspace verbatim. That meant a
//! model reading a reference page spent its context on `<div class="wrap">`
//! and navigation chrome rather than on the mathematics, and a PDF was not
//! merely unhelpful but fatal: the bytes failed a UTF-8 check, the tool
//! returned an error, and the error ended the run. Detecting the format and
//! rendering it to Markdown fixes both the noise and the failure.
//!
//! The HTML converter is written here rather than taken from a crate because
//! the documents that matter most carry TeX in them — Project Euler statements
//! and most mathematical references delimit maths with `\(…\)` — and a
//! general-purpose converter escapes the backslashes and destroys it.

use std::fmt::Write as _;

/// What a downloaded document turned out to be.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Format {
    /// Markup rendered to Markdown.
    Html,
    /// A PDF whose text layer is extracted.
    Pdf,
    /// Already text; passed through unchanged.
    Text,
    /// Recognisably not text, and not a format we can render.
    Binary,
}

impl Format {
    /// A short label for the conversion note added to the document.
    fn label(self) -> &'static str {
        match self {
            Self::Html => "HTML",
            Self::Pdf => "PDF",
            Self::Text => "plain text",
            Self::Binary => "binary",
        }
    }
}

/// Identifies a document from its declared content type and leading bytes.
///
/// The bytes win over the header: servers mislabel content routinely, and a
/// PDF served as `text/html` is still a PDF.
pub(super) fn detect(bytes: &[u8], content_type: Option<&str>) -> Format {
    if bytes.starts_with(b"%PDF-") {
        return Format::Pdf;
    }
    let leading = String::from_utf8_lossy(&bytes[..bytes.len().min(1024)])
        .trim_start()
        .to_ascii_lowercase();
    if leading.starts_with("<!doctype html")
        || leading.starts_with("<html")
        || leading.contains("<head")
    {
        return Format::Html;
    }
    let declared = content_type.unwrap_or_default().to_ascii_lowercase();
    if declared.contains("pdf") {
        return Format::Pdf;
    }
    if declared.contains("html") || declared.contains("xml") {
        return Format::Html;
    }
    if std::str::from_utf8(bytes).is_ok() {
        return Format::Text;
    }
    Format::Binary
}

/// A converted document and the citations it carries.
///
/// The links travel beside the Markdown rather than only inside it because
/// they are evidence in their own right: a URL three of the run's sources all
/// cite is the standard reference for the subject, and nothing else in the
/// runtime is in a position to notice that.
#[derive(Debug)]
pub(super) struct Converted {
    /// The document rendered as Markdown.
    pub(super) markdown: String,
    /// One record per distinct URL the document cites.
    pub(super) links: Vec<LinkRecord>,
}

/// One outbound citation, with enough context to judge it without fetching it.
///
/// The context is the point. An anchor's URL says a document exists; the
/// sentence it was cited in says why this source thought it mattered, which is
/// the difference between a reading list and a list of URLs.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct LinkRecord {
    /// The cited URL, with tracking parameters stripped.
    pub(super) url: String,
    /// The anchor text, empty when the citation was a bare URL.
    pub(super) label: String,
    /// A one-line window of the prose surrounding the citation.
    pub(super) context: String,
}

/// Renders `bytes` to Markdown, or explains why it cannot be read.
///
/// # Errors
///
/// Returns an error only for content with no text at all — an image or an
/// archive. The message names the format and says what to do instead, because
/// this result reaches a model that has to choose a different source.
pub(super) fn to_markdown(
    bytes: &[u8],
    content_type: Option<&str>,
    source: &str,
) -> crate::agent::Result<String> {
    convert(bytes, content_type, source).map(|converted| converted.markdown)
}

/// Renders `bytes` to Markdown and collects the citations it carries.
///
/// # Errors
///
/// As [`to_markdown`]: only content with no text at all fails.
pub(super) fn convert(
    bytes: &[u8],
    content_type: Option<&str>,
    source: &str,
) -> crate::agent::Result<Converted> {
    let format = detect(bytes, content_type);
    let mut links = LinkTable::default();
    let (body, records) = match format {
        Format::Html => {
            let rendered = html_to_markdown(&String::from_utf8_lossy(bytes), &mut links);
            // Context is read off the pre-trim buffer, where the recorded
            // offsets still point at the reference markers that produced them.
            let records = links.records(&rendered);
            (rendered, records)
        }
        Format::Pdf => {
            let text = pdf_to_text(bytes)?;
            let records = bare_links(&text);
            (text, records)
        }
        Format::Text => {
            let text = String::from_utf8_lossy(bytes).into_owned();
            let records = bare_links(&text);
            (text, records)
        }
        Format::Binary => {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{source}` is binary content with no readable text, so it cannot be turned into \
                 Markdown. Find an HTML or PDF version of the same material, or a different \
                 source."
            )));
        }
    };
    let body = collapse_blank_lines(body.trim());
    if body.is_empty() {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{source}` parsed as {} but contained no extractable text. If it is a scanned PDF \
             there is no text layer to read; find another source.",
            format.label()
        )));
    }
    let cited = clean_url(source);
    Ok(Converted {
        markdown: format!(
            "<!-- source: {cited} | converted from {} -->\n\n{body}\n{}",
            format.label(),
            links.render()
        ),
        // A document citing itself is not a lead, and a reference page's link
        // back to its own canonical URL is the commonest citation there is.
        links: records
            .into_iter()
            .filter(|record| record.url != cited)
            .collect(),
    })
}

/// Extracts a PDF's text layer.
///
/// The extractor is run inside `catch_unwind` because it panics on malformed
/// input, and a panic here would take down work that has nothing to do with
/// this document.
fn pdf_to_text(bytes: &[u8]) -> crate::agent::Result<String> {
    let owned = bytes.to_vec();
    let extracted = std::panic::catch_unwind(move || pdf_extract::extract_text_from_mem(&owned));
    match extracted {
        Ok(Ok(text)) => Ok(text),
        Ok(Err(error)) => Err(tinyagents::TinyAgentsError::Validation(format!(
            "this PDF could not be parsed: {error}. Try the publisher's HTML version, or an \
             abstract or preprint page instead."
        ))),
        Err(_) => Err(tinyagents::TinyAgentsError::Validation(
            "this PDF is malformed enough to crash the text extractor. Use a different source or \
             format."
                .into(),
        )),
    }
}

/// Elements whose entire contents are dropped.
const DROPPED: [&str; 8] = [
    "script", "style", "noscript", "nav", "header", "footer", "aside", "form",
];

/// Converts HTML to Markdown, preserving TeX delimiters and code verbatim.
fn html_to_markdown(html: &str, table: &mut LinkTable) -> String {
    let mut out = String::with_capacity(html.len() / 2);
    let mut chars = html.char_indices().peekable();
    let mut list_stack: Vec<Option<usize>> = Vec::new();
    let mut in_pre = false;
    let mut pending_text = String::new();
    // While inside an anchor, text is buffered here instead of being written
    // out, because the reference number is only emitted once the label is
    // known at the closing tag.
    let mut link_target: Option<String> = None;
    let mut link_text = String::new();

    while let Some((index, character)) = chars.next() {
        if character != '<' {
            pending_text.push(character);
            continue;
        }
        // Flush the text accumulated before this tag into whichever buffer is
        // currently collecting.
        if link_target.is_some() {
            flush_text(&mut link_text, &mut pending_text, in_pre);
        } else {
            flush_text(&mut out, &mut pending_text, in_pre);
        }

        let Some(close) = html[index..].find('>') else {
            break;
        };
        let raw = &html[index + 1..index + close];
        // Advance past the tag body.
        while let Some(&(next, _)) = chars.peek() {
            if next >= index + close {
                chars.next();
                break;
            }
            chars.next();
        }

        if raw.starts_with('!') {
            continue;
        }
        let closing = raw.starts_with('/');
        let name = raw
            .trim_start_matches('/')
            .split(|c: char| c.is_whitespace() || c == '/')
            .next()
            .unwrap_or("")
            .to_ascii_lowercase();

        if DROPPED.contains(&name.as_str()) {
            if !closing && let Some(end) = find_close(html, index, &name) {
                while let Some(&(next, _)) = chars.peek() {
                    if next >= end {
                        break;
                    }
                    chars.next();
                }
            }
            continue;
        }

        apply_tag(
            &mut TagContext {
                out: &mut out,
                list_stack: &mut list_stack,
                in_pre: &mut in_pre,
                link_target: &mut link_target,
                link_text: &mut link_text,
                table,
            },
            &name,
            closing,
            raw,
        );
    }
    if link_target.is_some() {
        // An anchor that never closed: keep its text rather than losing it.
        flush_text(&mut link_text, &mut pending_text, in_pre);
        out.push_str(link_text.trim());
    } else {
        flush_text(&mut out, &mut pending_text, in_pre);
    }
    out
}

/// The mutable state a tag handler acts on.
struct TagContext<'a> {
    out: &'a mut String,
    list_stack: &'a mut Vec<Option<usize>>,
    in_pre: &'a mut bool,
    link_target: &'a mut Option<String>,
    link_text: &'a mut String,
    table: &'a mut LinkTable,
}

/// Emits the Markdown for one opening or closing tag.
fn apply_tag(ctx: &mut TagContext<'_>, name: &str, closing: bool, raw: &str) {
    let out = &mut *ctx.out;
    match (name, closing) {
        ("br", _) => out.push('\n'),
        ("hr", _) => out.push_str("\n\n---\n\n"),
        ("p" | "div" | "section" | "article" | "tr" | "blockquote" | "table", _)
        | ("h1" | "h2" | "h3" | "h4" | "h5" | "h6", true) => ensure_blank_line(out),
        ("h1" | "h2" | "h3" | "h4" | "h5" | "h6", false) => {
            ensure_blank_line(out);
            let level = name[1..].parse::<usize>().unwrap_or(1);
            let _ = write!(out, "{} ", "#".repeat(level.clamp(1, 6)));
        }

        ("ul", false) => {
            ensure_blank_line(out);
            ctx.list_stack.push(None);
        }
        ("ol", false) => {
            ensure_blank_line(out);
            ctx.list_stack.push(Some(1));
        }
        ("ul" | "ol", true) => {
            ctx.list_stack.pop();
            ensure_blank_line(out);
        }
        ("li", false) => {
            trim_trailing_spaces(out);
            if !out.ends_with('\n') {
                out.push('\n');
            }
            let depth = ctx.list_stack.len().saturating_sub(1);
            out.push_str(&"  ".repeat(depth));
            match ctx.list_stack.last_mut() {
                Some(Some(counter)) => {
                    let _ = write!(out, "{counter}. ");
                    *counter += 1;
                }
                _ => out.push_str("- "),
            }
        }
        ("pre", false) => {
            ensure_blank_line(out);
            out.push_str("```\n");
            *ctx.in_pre = true;
        }
        ("pre", true) => {
            *ctx.in_pre = false;
            if !out.ends_with('\n') {
                out.push('\n');
            }
            out.push_str("```\n\n");
        }
        ("code", _) if !*ctx.in_pre => out.push('`'),
        ("strong" | "b", _) => out.push_str("**"),
        ("em" | "i", _) => out.push('*'),
        ("td" | "th", true) => out.push_str(" | "),

        ("img", false) => {
            if let Some(alt) = attribute(raw, "alt")
                && !alt.trim().is_empty()
            {
                let _ = write!(out, "[image: {}]", decode_entities(&alt));
            }
        }
        ("a", false) => {
            if let Some(href) = attribute(raw, "href")
                && !href.starts_with('#')
                && !href.starts_with("javascript:")
            {
                *ctx.link_target = Some(href);
                ctx.link_text.clear();
            }
        }
        ("a", true) => {
            if let Some(href) = ctx.link_target.take() {
                let label = ctx.link_text.trim().to_string();
                let reference = ctx.table.reference(&href);
                if needs_space(out, "[") {
                    out.push(' ');
                }
                ctx.table.cited(reference, &label, out.len());
                if label.is_empty() {
                    let _ = write!(out, "[{reference}]");
                } else {
                    let _ = write!(out, "[{label}][{reference}]");
                }
                ctx.link_text.clear();
            }
        }
        _ => {}
    }
}

/// Query parameters that carry no meaning and cost tokens.
const TRACKING_PARAMS: [&str; 9] = [
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
    "mc_cid",
    "ref_src",
];

/// Collects links so each distinct URL is written once.
///
/// A reference page can carry the same long URL a dozen times, and an inline
/// `[text](https://…)` pays for the whole thing at every occurrence. Numbering
/// them and listing each once at the end costs a couple of characters per use
/// instead, which on a real page is the difference between a readable document
/// and one that fills the context with navigation targets.
#[derive(Debug, Default)]
pub(super) struct LinkTable {
    urls: Vec<String>,
    /// Where each distinct URL was first cited, and under what anchor text.
    ///
    /// Only the first occurrence is kept. A page that links the same reference
    /// a dozen times cites it once for a reason and eleven times from a
    /// navigation bar, and the first is the one that came with prose.
    first: Vec<(String, usize)>,
}

impl LinkTable {
    /// Returns the one-based reference number for `url`, adding it if new.
    fn reference(&mut self, url: &str) -> usize {
        let cleaned = clean_url(url);
        if let Some(position) = self.urls.iter().position(|existing| *existing == cleaned) {
            return position + 1;
        }
        self.urls.push(cleaned);
        self.first.push((String::new(), 0));
        self.urls.len()
    }

    /// Records the anchor text and position of a URL's first citation.
    fn cited(&mut self, reference: usize, label: &str, at: usize) {
        if let Some(entry) = self.first.get_mut(reference.saturating_sub(1))
            && entry.1 == 0
        {
            *entry = (label.to_string(), at);
        }
    }

    /// Builds one record per distinct URL, reading context out of `rendered`.
    ///
    /// `rendered` must be the buffer the offsets were taken against — the
    /// conversion output before it is trimmed and its blank lines collapsed —
    /// or the windows land in the wrong place.
    fn records(&self, rendered: &str) -> Vec<LinkRecord> {
        self.urls
            .iter()
            .zip(&self.first)
            .map(|(url, (label, at))| LinkRecord {
                url: url.clone(),
                label: label.clone(),
                context: window(rendered, *at),
            })
            .collect()
    }

    /// Renders the reference list appended below the document.
    fn render(&self) -> String {
        if self.urls.is_empty() {
            return String::new();
        }
        let mut out = String::from("\n\n## Links\n\n");
        for (index, url) in self.urls.iter().enumerate() {
            let _ = writeln!(out, "[{}]: {url}", index + 1);
        }
        out
    }
}

/// Characters of prose kept either side of a citation.
const CONTEXT_BEFORE: usize = 140;

/// Characters of prose kept after a citation.
const CONTEXT_AFTER: usize = 160;

/// Reads a one-line window of prose around byte offset `at`.
///
/// Collapsed to a single line because the window is destined for a table row.
/// An empty result is normal and means the citation carried no prose — a
/// navigation link, or a bare URL on a line of its own.
fn window(text: &str, at: usize) -> String {
    if at == 0 || at > text.len() {
        return String::new();
    }
    let start = floor_boundary(text, at.saturating_sub(CONTEXT_BEFORE));
    let end = ceil_boundary(text, (at + CONTEXT_AFTER).min(text.len()));
    let mut out = collapse_spaces(&text[start..end].replace('\n', " "));
    // Both ends are cut mid-word by construction, so drop the partial words
    // rather than presenting them as text the source wrote.
    if start > 0 && let Some((_, rest)) = out.split_once(' ') {
        out = rest.to_string();
    }
    if end < text.len() && let Some((body, _)) = out.rsplit_once(' ') {
        out = body.to_string();
    }
    out.trim().to_string()
}

/// Markers introducing a citation in text that has no anchors.
///
/// A converted PDF is the case that matters: a mathematical paper's reference
/// list is where the primary literature on its subject is named, and it names
/// it as arXiv identifiers and DOIs far more often than as URLs. Reading them
/// is the difference between a library that grows by search and one that grows
/// by following what its own sources cite.
const BARE_MARKERS: [&str; 4] = ["http://", "https://", "arxiv:", "doi:"];

/// Extracts citations from text with no markup to read them from.
fn bare_links(text: &str) -> Vec<LinkRecord> {
    let lowered = text.to_ascii_lowercase();
    let mut records: Vec<LinkRecord> = Vec::new();
    let mut cursor = 0;
    while cursor < lowered.len() {
        let Some((at, marker)) = BARE_MARKERS
            .iter()
            .filter_map(|marker| lowered[cursor..].find(marker).map(|at| (cursor + at, *marker)))
            .min_by_key(|(at, _)| *at)
        else {
            break;
        };
        let rest = &text[at + marker.len()..];
        let body: String = rest
            .chars()
            .take_while(|c| !c.is_whitespace() && !matches!(c, '<' | '>' | '"' | '\\' | '|'))
            .collect();
        let body = body.trim_end_matches(['.', ',', ';', ':', ')', ']', '}', '\'']);
        cursor = at + marker.len() + body.len().max(1);
        if body.is_empty() {
            continue;
        }
        let url = match marker {
            "arxiv:" => format!("https://arxiv.org/abs/{body}"),
            "doi:" => format!("https://doi.org/{body}"),
            _ => format!("{marker}{body}"),
        };
        let url = clean_url(&url);
        if records.iter().any(|record| record.url == url) {
            continue;
        }
        records.push(LinkRecord {
            label: String::new(),
            context: window(text, at),
            url,
        });
    }
    records
}

fn floor_boundary(text: &str, mut index: usize) -> usize {
    while index > 0 && !text.is_char_boundary(index) {
        index -= 1;
    }
    index
}

fn ceil_boundary(text: &str, mut index: usize) -> usize {
    while index < text.len() && !text.is_char_boundary(index) {
        index += 1;
    }
    index
}

/// Removes tracking parameters and a redundant trailing slash from a URL.
pub(super) fn clean_url(url: &str) -> String {
    let (base, query) = match url.split_once('?') {
        Some((base, query)) => (base, Some(query)),
        None => (url, None),
    };
    let (query, fragment) = match query {
        Some(query) => match query.split_once('#') {
            Some((query, fragment)) => (Some(query), Some(fragment)),
            None => (Some(query), None),
        },
        None => (None, None),
    };
    let kept: Vec<&str> = query
        .map(|query| {
            query
                .split('&')
                .filter(|pair| {
                    let key = pair.split('=').next().unwrap_or(pair);
                    !TRACKING_PARAMS.contains(&key) && !pair.is_empty()
                })
                .collect()
        })
        .unwrap_or_default();
    let mut out = base.to_string();
    if !kept.is_empty() {
        out.push('?');
        out.push_str(&kept.join("&"));
    }
    if let Some(fragment) = fragment
        && !fragment.is_empty()
    {
        out.push('#');
        out.push_str(fragment);
    }
    out
}

/// Returns the byte offset just past the matching closing tag.
fn find_close(html: &str, from: usize, name: &str) -> Option<usize> {
    let needle = format!("</{name}");
    html[from..]
        .to_ascii_lowercase()
        .find(&needle)
        .map(|offset| from + offset)
}

/// Reads a tag attribute's value.
fn attribute(tag: &str, name: &str) -> Option<String> {
    let lowered = tag.to_ascii_lowercase();
    let position = lowered.find(&format!("{name}="))?;
    let rest = &tag[position + name.len() + 1..];
    let mut characters = rest.chars();
    match characters.next()? {
        quote @ ('"' | '\'') => rest[1..].find(quote).map(|end| rest[1..=end].to_string()),
        _ => Some(
            rest.split(|c: char| c.is_whitespace() || c == '>')
                .next()
                .unwrap_or("")
                .to_string(),
        ),
    }
}

fn flush_text(out: &mut String, pending: &mut String, in_pre: bool) {
    if pending.is_empty() {
        return;
    }
    let decoded = decode_entities(pending);
    if in_pre {
        out.push_str(&decoded);
    } else {
        let collapsed = collapse_spaces(&decoded);
        if !collapsed.is_empty() {
            if needs_space(out, &collapsed) {
                out.push(' ');
            }
            out.push_str(&collapsed);
        }
    }
    pending.clear();
}

fn needs_space(out: &str, next: &str) -> bool {
    match out.chars().last() {
        None | Some('\n' | ' ' | '[' | '`' | '*' | '#' | '\u{0}') => false,
        Some(_) => !next.starts_with([',', '.', ';', ':', ')', ']', '!', '?']),
    }
}

fn collapse_spaces(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut in_space = false;
    for character in text.chars() {
        if character.is_whitespace() {
            in_space = true;
        } else {
            if in_space && !out.is_empty() {
                out.push(' ');
            }
            in_space = false;
            out.push(character);
        }
    }
    if in_space && !out.is_empty() {
        out.push(' ');
    }
    out
}

fn ensure_blank_line(out: &mut String) {
    trim_trailing_spaces(out);
    if out.is_empty() {
        return;
    }
    while !out.ends_with("\n\n") {
        out.push('\n');
        if out.len() > 2 && out.ends_with("\n\n") {
            break;
        }
        if out.ends_with("\n\n") {
            break;
        }
        if out.chars().rev().take_while(|c| *c == '\n').count() >= 2 {
            break;
        }
    }
}

fn trim_trailing_spaces(out: &mut String) {
    while out.ends_with(' ') || out.ends_with('\t') {
        out.pop();
    }
}

fn collapse_blank_lines(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut blanks = 0;
    for line in text.lines() {
        let trimmed = line.trim_end();
        if trimmed.is_empty() {
            blanks += 1;
            if blanks > 1 {
                continue;
            }
        } else {
            blanks = 0;
        }
        out.push_str(trimmed);
        out.push('\n');
    }
    out.trim().to_string()
}

/// Decodes the HTML entities that appear in mathematical prose.
fn decode_entities(text: &str) -> String {
    if !text.contains('&') {
        return text.to_string();
    }
    let mut out = String::with_capacity(text.len());
    let mut rest = text;
    while let Some(start) = rest.find('&') {
        out.push_str(&rest[..start]);
        let tail = &rest[start..];
        let Some(end) = tail[..tail.len().min(12)].find(';') else {
            out.push('&');
            rest = &tail[1..];
            continue;
        };
        let entity = &tail[1..end];
        let decoded = match entity {
            "amp" => Some("&".to_string()),
            "lt" => Some("<".to_string()),
            "gt" => Some(">".to_string()),
            "quot" => Some("\"".to_string()),
            "apos" | "#39" => Some("'".to_string()),
            "nbsp" | "#160" => Some(" ".to_string()),
            "mdash" => Some("—".to_string()),
            "ndash" => Some("–".to_string()),
            "hellip" => Some("…".to_string()),
            "times" => Some("×".to_string()),
            "minus" => Some("−".to_string()),
            "le" => Some("≤".to_string()),
            "ge" => Some("≥".to_string()),
            other => other
                .strip_prefix('#')
                .and_then(|digits| {
                    digits.strip_prefix('x').map_or_else(
                        || digits.parse::<u32>().ok(),
                        |hex| u32::from_str_radix(hex, 16).ok(),
                    )
                })
                .and_then(char::from_u32)
                .map(|c| c.to_string()),
        };
        if let Some(value) = decoded {
            out.push_str(&value);
            rest = &tail[end + 1..];
        } else {
            out.push('&');
            rest = &tail[1..];
        }
    }
    out.push_str(rest);
    out
}

#[cfg(test)]
mod test;
