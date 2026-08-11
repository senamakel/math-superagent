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
    if leading.starts_with("<!doctype html") || leading.starts_with("<html") || leading.contains("<head") {
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
    let format = detect(bytes, content_type);
    let body = match format {
        Format::Html => html_to_markdown(&String::from_utf8_lossy(bytes)),
        Format::Pdf => pdf_to_text(bytes)?,
        Format::Text => String::from_utf8_lossy(bytes).into_owned(),
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
    Ok(format!(
        "<!-- source: {source} | converted from {} -->\n\n{body}\n",
        format.label()
    ))
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
fn html_to_markdown(html: &str) -> String {
    let mut out = String::with_capacity(html.len() / 2);
    let mut chars = html.char_indices().peekable();
    let mut list_stack: Vec<Option<usize>> = Vec::new();
    let mut in_pre = false;
    let mut pending_text = String::new();

    while let Some((index, character)) = chars.next() {
        if character != '<' {
            pending_text.push(character);
            continue;
        }
        // Flush the text accumulated before this tag.
        flush_text(&mut out, &mut pending_text, in_pre);

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

        match (name.as_str(), closing) {
            ("br", _) => out.push('\n'),
            ("hr", _) => out.push_str("\n\n---\n\n"),
            ("p" | "div" | "section" | "article" | "tr" | "blockquote", _) => {
                ensure_blank_line(&mut out);
            }
            ("h1" | "h2" | "h3" | "h4" | "h5" | "h6", false) => {
                ensure_blank_line(&mut out);
                let level = name[1..].parse::<usize>().unwrap_or(1);
                let _ = write!(out, "{} ", "#".repeat(level.clamp(1, 6)));
            }
            ("h1" | "h2" | "h3" | "h4" | "h5" | "h6", true) => ensure_blank_line(&mut out),
            ("ul", false) => {
                ensure_blank_line(&mut out);
                list_stack.push(None);
            }
            ("ol", false) => {
                ensure_blank_line(&mut out);
                list_stack.push(Some(1));
            }
            ("ul" | "ol", true) => {
                list_stack.pop();
                ensure_blank_line(&mut out);
            }
            ("li", false) => {
                trim_trailing_spaces(&mut out);
                if !out.ends_with('\n') {
                    out.push('\n');
                }
                let depth = list_stack.len().saturating_sub(1);
                out.push_str(&"  ".repeat(depth));
                match list_stack.last_mut() {
                    Some(Some(counter)) => {
                        let _ = write!(out, "{counter}. ");
                        *counter += 1;
                    }
                    _ => out.push_str("- "),
                }
            }
            ("pre", false) => {
                ensure_blank_line(&mut out);
                out.push_str("```\n");
                in_pre = true;
            }
            ("pre", true) => {
                in_pre = false;
                if !out.ends_with('\n') {
                    out.push('\n');
                }
                out.push_str("```\n\n");
            }
            ("code", _) if !in_pre => out.push('`'),
            ("strong" | "b", _) => out.push_str("**"),
            ("em" | "i", _) => out.push('*'),
            ("td" | "th", true) => out.push_str(" | "),
            ("table", _) => ensure_blank_line(&mut out),
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
                {
                    out.push('[');
                    // Remember the target for the closing tag.
                    pending_text.clear();
                    out.push_str("\u{0}");
                    out.push_str(&href);
                    out.push_str("\u{0}");
                }
            }
            _ => {}
        }
    }
    flush_text(&mut out, &mut pending_text, in_pre);
    finish_links(&out)
}

/// Rewrites the link placeholders left by the anchor handling.
///
/// Anchors are emitted as `[` plus a delimited href, because the link text is
/// only known once the closing tag arrives. This pass turns each pair into
/// `[text](href)`, and drops any placeholder whose anchor never closed.
fn finish_links(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut rest = text;
    while let Some(start) = rest.find('\u{0}') {
        let (before, tail) = rest.split_at(start);
        out.push_str(before);
        let tail = &tail[1..];
        let Some(end) = tail.find('\u{0}') else {
            // Unterminated placeholder: drop the stray `[` we emitted.
            if out.ends_with('[') {
                out.pop();
            }
            out.push_str(tail);
            return out;
        };
        let href = &tail[..end];
        let after = &tail[end + 1..];
        // The link text runs to the end of this anchor's content.
        match after.find("</a") {
            Some(_) => {
                let label_end = after.find('\u{0}').unwrap_or(after.len());
                let label = &after[..label_end];
                let label = label.split('<').next().unwrap_or(label).trim();
                if label.is_empty() {
                    if out.ends_with('[') {
                        out.pop();
                    }
                    let _ = write!(out, "<{href}>");
                } else {
                    let _ = write!(out, "{label}]({href})");
                }
                rest = &after[label_end.min(after.len())..];
            }
            None => {
                if out.ends_with('[') {
                    out.pop();
                }
                rest = after;
            }
        }
    }
    out.push_str(rest);
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
        match decoded {
            Some(value) => {
                out.push_str(&value);
                rest = &tail[end + 1..];
            }
            None => {
                out.push('&');
                rest = &tail[1..];
            }
        }
    }
    out.push_str(rest);
    out
}

#[cfg(test)]
mod test;
