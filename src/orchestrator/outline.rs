//! The structure map a large document is read through, and the slicing that
//! makes a targeted read possible.
//!
//! `read_document` returned whole files. That is correct for a note and ruinous
//! for a library: the Gilbreath workspace holds 404 Markdown files totalling
//! 4.7 MB, and **37 of them hold 60% of those bytes**. The largest is a 427,889
//! byte annotated bibliography — roughly 107,000 tokens, more than a third of
//! the compression trigger — and a role with no way to ask for part of it had
//! exactly two options: spend a third of its window on one source, or never
//! open it. Both were taken. The same shape already cost this runtime a
//! 339,652-token model call from `trace.jsonl`, which is why
//! [`super::documents::ensure_visible`] exists; a research source is the same
//! failure wearing a legitimate name, and cannot be answered by hiding the file.
//!
//! So a document is read in two steps. First its *outline* — the heading tree
//! with a line range and a byte count against each section, which turns that
//! 427 KB bibliography into about 2 KB of navigation. Then the one or two
//! sections that answer the question, named by heading or by line range.
//!
//! # The ceiling is a control, not advice
//!
//! An unselected read over [`super::reading::unselected_ceiling`] does not return the
//! document. It returns this outline and says how to select. That is deliberate
//! and it is the whole point of the module: `CLAUDE.md` is explicit that a
//! prompt instruction is not a control, and "please read large files in
//! sections" is a prompt instruction. Nothing is hidden and nothing is lost —
//! every byte is still reachable, one named range at a time — but no single
//! call can put a hundred thousand tokens into a context window by accident.
//!
//! # Why the outline is derived and never stored
//!
//! A written index has to be maintained, and [`super::folder_index`] already
//! carries the judgement half of that job — what a file is *for*, which only
//! the agent that wrote it knows. What a file *contains* needs no judgement:
//! it is in the file. Deriving it on every read costs a single pass over bytes
//! already in memory and cannot go stale, which a stored table of contents
//! would do at the next edit.

use std::fmt::Write as _;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::json;

use super::documents::WorkspaceDocuments;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Lines one block of a structureless document covers.
///
/// A file with no headings still has to be navigable, or the ceiling above
/// becomes a wall. Blocks give it coordinates to ask for.
const BLOCK_LINES: usize = 200;

/// Sections one outline lists before it is summarised rather than printed.
///
/// An outline that runs to four hundred rows has reproduced the problem it
/// exists to solve.
const MAX_ROWS: usize = 120;

/// Characters one heading is shown to.
const TITLE_CHARS: usize = 96;

/// One addressable region of a document.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct Section {
    /// Heading depth: 1 for `#`, 2 for `##`. Zero for a derived block.
    pub(super) level: usize,
    /// The heading text, or a derived label for a block.
    pub(super) title: String,
    /// First line of the section, 1-based and inclusive of the heading itself.
    pub(super) first_line: usize,
    /// Last line of the section, 1-based and inclusive.
    pub(super) last_line: usize,
    /// How many bytes the section occupies.
    pub(super) bytes: usize,
}

/// A resolved region of a document.
///
/// Carries however much text the selection named. It is *not* bounded, because
/// its two callers want opposite things from it: [`select`] is on its way to a
/// context window and applies [`super::reading::slice_ceiling`], while
/// [`super::recursive`] is on its way to a chunker and wants every byte. A
/// bound here would silently truncate the recursive read, which is the one
/// path in this module whose whole purpose is to cover a document completely.
#[derive(Clone, Debug)]
pub(super) struct Region {
    /// How the selection is described back to the caller.
    pub(super) label: String,
    /// First line of the region, 1-based.
    pub(super) first_line: usize,
    /// Last line of the region, 1-based.
    pub(super) last_line: usize,
    /// The text itself.
    pub(super) text: String,
}

/// A region cut to what one tool result may carry.
#[derive(Clone, Debug)]
pub(super) struct Slice {
    /// How the selection is described back to the caller.
    pub(super) label: String,
    /// First line of the returned text, 1-based.
    pub(super) first_line: usize,
    /// Last line of the returned text, 1-based, after any truncation.
    pub(super) last_line: usize,
    /// Whether the region was cut short at [`super::reading::slice_ceiling`].
    pub(super) truncated: bool,
    /// The text itself.
    pub(super) text: String,
}

/// Reads a Markdown ATX heading out of a line, returning its level and title.
///
/// Fenced code is the reason this is not a bare `starts_with('#')`: a Python
/// comment inside a fence begins with `#` and is not a section of the document.
/// The caller tracks fences and only asks about lines outside them.
fn heading(line: &str) -> Option<(usize, String)> {
    let trimmed = line.trim_start();
    let hashes = trimmed.chars().take_while(|c| *c == '#').count();
    if hashes == 0 || hashes > 6 {
        return None;
    }
    let rest = trimmed[hashes..].trim();
    // `#hashtag` is not a heading; ATX requires the space.
    if rest.is_empty() || !trimmed[hashes..].starts_with(char::is_whitespace) {
        return None;
    }
    Some((hashes, rest.trim_end_matches('#').trim().to_string()))
}

/// Reads a top-level Python definition out of a line.
///
/// Only column zero, so a method keeps its class as the section it belongs to.
/// The run writes a great deal of Python and a 900-line verification script is
/// no more readable in one gulp than a paper is.
fn definition(line: &str) -> Option<String> {
    let name = line
        .strip_prefix("def ")
        .or_else(|| line.strip_prefix("class "))
        .or_else(|| line.strip_prefix("async def "))?;
    let name = name.split(['(', ':']).next().unwrap_or(name).trim();
    if name.is_empty() {
        return None;
    }
    let kind = if line.starts_with("class ") {
        "class"
    } else {
        "def"
    };
    Some(format!("{kind} {name}"))
}

/// Splits `content` into the sections an outline lists.
///
/// Markdown headings when there are any, top-level Python definitions for a
/// `.py` file, and fixed line blocks otherwise — so every document has
/// coordinates, including the ones with no structure of their own.
pub(super) fn sections(relative: &str, content: &str) -> Vec<Section> {
    let lines: Vec<&str> = content.lines().collect();
    let python = relative.to_ascii_lowercase().ends_with(".py");
    let mut starts: Vec<(usize, usize, String)> = Vec::new();
    let mut fenced = false;
    for (index, line) in lines.iter().enumerate() {
        let trimmed = line.trim_start();
        if trimmed.starts_with("```") || trimmed.starts_with("~~~") {
            fenced = !fenced;
            continue;
        }
        if fenced {
            continue;
        }
        if python {
            if let Some(title) = definition(line) {
                starts.push((1, index, title));
            }
        } else if let Some((level, title)) = heading(line) {
            starts.push((level, index, title));
        }
    }
    if starts.is_empty() {
        return blocks(&lines);
    }
    // A document whose first heading is not its first line has a preamble, and
    // a preamble nothing addresses is a hole in the map.
    if starts.first().is_some_and(|(_, index, _)| *index > 0) {
        starts.insert(0, (0, 0, "(preamble)".to_string()));
    }
    let mut out = Vec::with_capacity(starts.len());
    for (position, (level, first, title)) in starts.iter().enumerate() {
        let last = starts
            .get(position + 1)
            .map_or(lines.len(), |(_, next, _)| *next);
        out.push(Section {
            level: *level,
            title: super::text::truncate(title, TITLE_CHARS),
            first_line: first + 1,
            last_line: last.max(first + 1),
            bytes: byte_span(&lines, *first, last),
        });
    }
    out
}

/// Divides a structureless document into fixed line blocks.
fn blocks(lines: &[&str]) -> Vec<Section> {
    let mut out = Vec::new();
    let mut first = 0;
    while first < lines.len() {
        let last = (first + BLOCK_LINES).min(lines.len());
        // The first line with anything on it labels the block. It is a guess,
        // and a guess is what the caller needs to decide whether to look.
        let label = lines[first..last]
            .iter()
            .map(|line| line.trim())
            .find(|line| !line.is_empty())
            .unwrap_or("(blank)");
        out.push(Section {
            level: 0,
            title: super::text::truncate(label, TITLE_CHARS),
            first_line: first + 1,
            last_line: last,
            bytes: byte_span(lines, first, last),
        });
        first = last;
    }
    if out.is_empty() {
        out.push(Section {
            level: 0,
            title: "(empty)".to_string(),
            first_line: 1,
            last_line: 1,
            bytes: 0,
        });
    }
    out
}

/// Bytes covered by `lines[first..last]`, counting the newline each line lost
/// when the content was split.
fn byte_span(lines: &[&str], first: usize, last: usize) -> usize {
    lines[first..last.min(lines.len())]
        .iter()
        .map(|line| line.len() + 1)
        .sum()
}

/// Renders the navigation a caller reads before asking for anything.
pub(super) fn render(relative: &str, content: &str) -> String {
    let sections = sections(relative, content);
    let lines = content.lines().count();
    let mut out = format!(
        "outline of {relative} — {} bytes, {lines} lines, {} sections\n\n",
        content.len(),
        sections.len()
    );
    let shown = sections.len().min(MAX_ROWS);
    let mut oversized = false;
    for section in sections.iter().take(shown) {
        let indent = "  ".repeat(section.level.saturating_sub(1).min(4));
        // A derived ledger is one heading over a thousand-line table, so
        // "read this section" is not always a thing one call can do. Saying
        // which sections those are is the difference between a map and a map
        // with the impassable parts left unmarked.
        let note = if section.bytes > super::reading::slice_ceiling() {
            oversized = true;
            "  [over one read]"
        } else {
            ""
        };
        let _ = writeln!(
            out,
            "  {:>11}  {:>8}  {indent}{}{note}",
            format!("{}-{}", section.first_line, section.last_line),
            section.bytes,
            section.title
        );
    }
    if sections.len() > shown {
        let _ = writeln!(
            out,
            "  … {} further sections; narrow with grep_workspace, or read by line range",
            sections.len() - shown
        );
    }
    out.push_str(
        "\nRead one region: read_document with `section` (a heading, matched by substring) \
         or `lines` (\"120-260\").\n",
    );
    if oversized {
        out.push_str(
            "A section marked [over one read] does not fit in one call — reach it by line range, \
             find the rows you want with grep_workspace, or ask map_document a question about it \
             instead.\n",
        );
    }
    out
}

/// Parses a `"120-260"`, `"120-"` or `"120"` line specification.
fn parse_lines(spec: &str) -> Result<(usize, Option<usize>)> {
    let spec = spec.trim();
    let (first, last) = match spec.split_once(['-', ':']) {
        Some((first, last)) => (first.trim(), last.trim()),
        None => (spec, ""),
    };
    let first: usize = first.parse().map_err(|_| {
        tinyagents::TinyAgentsError::Validation(format!(
            "`lines` must look like \"120-260\", \"120-\" or \"120\"; got `{spec}`"
        ))
    })?;
    if first == 0 {
        return Err(tinyagents::TinyAgentsError::Validation(
            "`lines` is 1-based; the first line is 1".into(),
        ));
    }
    if last.is_empty() {
        return Ok((first, None));
    }
    let last: usize = last.parse().map_err(|_| {
        tinyagents::TinyAgentsError::Validation(format!(
            "`lines` must look like \"120-260\", \"120-\" or \"120\"; got `{spec}`"
        ))
    })?;
    if last < first {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`lines` ends before it starts: `{spec}`"
        )));
    }
    Ok((first, Some(last)))
}

/// Finds the section a `section` argument names.
///
/// Matched case-insensitively: exact heading first, then unique substring. An
/// ambiguous name is an error listing the candidates rather than a guess,
/// because reading the wrong section is indistinguishable from reading the
/// right one until the conclusion is already drawn from it.
fn find(sections: &[Section], wanted: &str) -> Result<Section> {
    let wanted = wanted.trim().trim_start_matches('#').trim();
    let lowered = wanted.to_ascii_lowercase();
    if let Some(section) = sections
        .iter()
        .find(|section| section.title.eq_ignore_ascii_case(wanted))
    {
        return Ok(section.clone());
    }
    let matches: Vec<&Section> = sections
        .iter()
        .filter(|section| section.title.to_ascii_lowercase().contains(&lowered))
        .collect();
    match matches.as_slice() {
        [only] => Ok((*only).clone()),
        [] => Err(tinyagents::TinyAgentsError::Validation(format!(
            "no section matches `{wanted}`; call outline_document to see the headings"
        ))),
        many => {
            let names: Vec<String> = many
                .iter()
                .take(8)
                .map(|section| format!("`{}`", section.title))
                .collect();
            Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{wanted}` matches {} sections ({}); name one exactly, or use `lines`",
                many.len(),
                names.join(", ")
            )))
        }
    }
}

/// Resolves a selection into the region it names, unbounded.
///
/// `section` wins when both are given: it is the more specific statement of
/// intent, and a caller that has an exact range has no reason to send a
/// heading too. No selection at all is the whole document.
///
/// # Errors
///
/// Returns a validation error when the specification is malformed, names a
/// heading that does not exist or is ambiguous, or starts past the last line.
pub(super) fn region(
    relative: &str,
    content: &str,
    section: Option<&str>,
    lines: Option<&str>,
) -> Result<Region> {
    let all: Vec<&str> = content.lines().collect();
    let (label, first, last) = if let Some(section) = section {
        let found = find(&sections(relative, content), section)?;
        (
            format!("section `{}`", found.title),
            found.first_line,
            Some(found.last_line),
        )
    } else if let Some(spec) = lines {
        let (first, last) = parse_lines(spec)?;
        (format!("lines {spec}"), first, last)
    } else {
        ("the whole document".to_string(), 1, None)
    };
    if first > all.len().max(1) {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "{relative} has {} lines; `{first}` is past its end",
            all.len()
        )));
    }
    let last = last.unwrap_or(all.len()).min(all.len());
    let body = all.get(first - 1..last).unwrap_or_default();
    let mut text = String::with_capacity(body.iter().map(|line| line.len() + 1).sum());
    for line in body {
        text.push_str(line);
        text.push('\n');
    }
    Ok(Region {
        label,
        first_line: first,
        last_line: last.max(first),
        text,
    })
}

/// Resolves a selection and cuts it to [`super::reading::slice_ceiling`] at a line boundary.
///
/// # Errors
///
/// Returns whatever [`region`] returns.
pub(super) fn select(
    relative: &str,
    content: &str,
    section: Option<&str>,
    lines: Option<&str>,
) -> Result<Slice> {
    let region = region(relative, content, section, lines)?;
    let mut text = String::new();
    let mut end = region.first_line;
    let mut truncated = false;
    for (offset, line) in region.text.lines().enumerate() {
        if text.len() + line.len() + 1 > super::reading::slice_ceiling() && !text.is_empty() {
            truncated = true;
            break;
        }
        text.push_str(line);
        text.push('\n');
        end = region.first_line + offset;
    }
    Ok(Slice {
        label: region.label,
        first_line: region.first_line,
        last_line: end,
        truncated,
        text,
    })
}

/// Renders a resolved slice with the coordinates needed to continue from it.
///
/// The header is not decoration. A model handed 48 KB of prose with no line
/// numbers cannot cite it, cannot ask for the next part, and cannot tell
/// whether it is holding the beginning or the middle.
pub(super) fn render_slice(relative: &str, total_lines: usize, slice: &Slice) -> String {
    let mut out = format!(
        "{relative} — {}, lines {}-{} of {total_lines}\n\n{}",
        slice.label, slice.first_line, slice.last_line, slice.text
    );
    if slice.truncated || slice.last_line < total_lines {
        let _ = write!(
            out,
            "\n[stopped at line {}{}; continue with lines \"{}-\"]\n",
            slice.last_line,
            if slice.truncated {
                format!(" — the {} byte slice limit", super::reading::slice_ceiling())
            } else {
                String::new()
            },
            slice.last_line + 1
        );
    }
    out
}

/// The refusal an oversized unselected read is answered with.
///
/// It is phrased as an answer rather than as a failure because it *is* one: the
/// caller asked what is in the document, and this says what is in it and how to
/// get any part of it. A bare error would cost a turn and teach nothing.
pub(super) fn too_large(relative: &str, content: &str) -> String {
    format!(
        "{relative} is {} bytes — too large to read whole, and reading it whole is almost never \
         what is wanted. Its structure is below; ask for the part you need.\n\n{}",
        content.len(),
        render(relative, content)
    )
}

/// The `outline_document` tool.
#[derive(Debug)]
pub(super) struct OutlineTool {
    documents: WorkspaceDocuments,
}

impl OutlineTool {
    /// Builds the tool over a workspace.
    pub(super) fn all(documents: &WorkspaceDocuments) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            documents: documents.clone(),
        })]
    }
}

#[async_trait]
impl Tool<()> for OutlineTool {
    fn name(&self) -> &'static str {
        "outline_document"
    }

    fn description(&self) -> &'static str {
        "Maps a document's sections with their line ranges and sizes, so a large file can be read \
         one part at a time instead of whole."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative path below /workspace."
                    }
                },
                "required": ["path"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let path = super::string_argument(&call, "path")?;
        let content = self.documents.read_document(&path).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            render(&path, &content),
        ))
    }
}

#[cfg(test)]
#[path = "outline_test.rs"]
mod test;
