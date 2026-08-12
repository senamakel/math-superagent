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

include!("readable_html.rs");
include!("readable_links.rs");
include!("readable_text.rs");

#[cfg(test)]
#[path = "readable_test.rs"]
mod test;
