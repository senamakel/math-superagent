//! Finding the lines worth reading, without reading the files they are in.
//!
//! [`super::outline`] answers "what is in this document"; this answers "which
//! document, and where in it". They are the two halves of one motion, and the
//! second is the one a run reaches for far more often: a role does not want
//! `research/sources/martin-annotated-bibliography.full.md`, it wants the four
//! places anywhere in the library that mention a Chebyshev bias, with enough
//! line numbers to go and read them.
//!
//! # Why this is not `search_documents`
//!
//! `search_documents` ranks whole documents by word overlap against a manually
//! maintained index, and returns snippets from the ones it liked. That is a
//! different question with a different failure: a source nobody ran
//! `index_document` over is invisible to it, and what it returns is a document
//! name rather than a position. This is exact, needs no index, covers every
//! visible file the moment it is written, and returns coordinates
//! [`super::outline::select`] can be handed directly.
//!
//! # Why it is bounded everywhere
//!
//! A pattern like `the` across a 4.7 MB library matches tens of thousands of
//! times, and a tool that answered honestly would be a worse context spend than
//! the file it was avoiding. Every dimension is capped — matches per file,
//! matches overall, bytes per line, files visited — and the caps are *reported*
//! rather than silently applied, because a truncated result a caller believes
//! is complete is how a run concludes that something does not appear anywhere.

use std::fmt::Write as _;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::documents::WorkspaceDocuments;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Matches one call may return in total.
const MAX_MATCHES: usize = 60;

/// Matches one file may contribute.
///
/// A term that is the subject of one document matches on nearly every line of
/// it, and that document would otherwise fill the whole answer while the other
/// six files that mention it never appear. Spreading the budget is what makes
/// the result a map of *where* something is discussed.
const MAX_PER_FILE: usize = 8;

/// Files one call will open.
const MAX_FILES: usize = 600;

/// Bytes of a matching line that are shown.
const MAX_LINE_BYTES: usize = 400;

/// Bytes of a file this will scan.
///
/// Well above the largest source in a live workspace; it exists so a stray
/// binary or a runaway log cannot be pulled into memory line by line.
const MAX_SCAN_BYTES: u64 = 8 * 1024 * 1024;

/// One matching line.
#[derive(Clone, Debug)]
struct Hit {
    path: String,
    line: usize,
    text: String,
}

/// Whether `name` is worth opening: text this run wrote or downloaded.
///
/// An allowlist rather than a blocklist. The workspace accumulates
/// enumeration pools, captured output and converted PDFs, and a grep that
/// scans everything spends its budget proving that a 326 KB column of integers
/// does not contain the word "Chebyshev".
fn searchable(name: &str) -> bool {
    let lowered = name.to_ascii_lowercase();
    [".md", ".txt", ".py", ".json", ".jsonl", ".tex", ".lean", ".toml", ".rs"]
        .iter()
        .any(|suffix| lowered.ends_with(suffix))
}

/// Renders the report a search returns.
fn render(pattern: &str, hits: &[Hit], scanned: usize, capped: bool) -> String {
    if hits.is_empty() {
        return format!(
            "no line matches `{pattern}` in {scanned} searched files.\nThe pattern is a regular \
             expression: check for an unintended `.` or `|`, or search for a shorter stem."
        );
    }
    let files = {
        let mut names: Vec<&str> = hits.iter().map(|hit| hit.path.as_str()).collect();
        names.dedup();
        names.len()
    };
    let mut out = format!(
        "{} matching lines in {files} of {scanned} searched files, for `{pattern}`\n\n",
        hits.len()
    );
    let mut current = "";
    for hit in hits {
        if hit.path != current {
            current = &hit.path;
            let _ = writeln!(out, "{current}");
        }
        let _ = writeln!(out, "  {:>6}: {}", hit.line, hit.text);
    }
    if capped {
        let _ = writeln!(
            out,
            "\n[the result was capped at {MAX_MATCHES} matches, {MAX_PER_FILE} per file; narrow \
             the pattern or the path to see the rest]"
        );
    }
    out.push_str(
        "\nRead around a hit with read_document and a `lines` range, or map the file first with \
         outline_document.\n",
    );
    out
}

/// The `grep_workspace` tool.
#[derive(Debug)]
pub(super) struct GrepTool {
    documents: WorkspaceDocuments,
}

impl GrepTool {
    /// Builds the tool over a workspace.
    pub(super) fn all(documents: &WorkspaceDocuments) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            documents: documents.clone(),
        })]
    }

    /// Walks `root`, collecting matching lines under every cap.
    ///
    /// Errors on individual files are skipped rather than propagated: a search
    /// that fails because one file in a tree is not UTF-8 has answered a
    /// question nobody asked.
    async fn search(&self, root: &str, matcher: &regex::Regex) -> Result<(Vec<Hit>, usize, bool)> {
        let paths = self.documents.walk_files(root, MAX_FILES).await?;
        let mut hits = Vec::new();
        let mut scanned = 0;
        let mut capped = false;
        for path in paths {
            if !searchable(&path) {
                continue;
            }
            if hits.len() >= MAX_MATCHES {
                capped = true;
                break;
            }
            let Ok(content) = self.documents.read_bounded(&path, MAX_SCAN_BYTES).await else {
                continue;
            };
            scanned += 1;
            let mut in_file = 0;
            for (index, line) in content.lines().enumerate() {
                if !matcher.is_match(line) {
                    continue;
                }
                if in_file >= MAX_PER_FILE || hits.len() >= MAX_MATCHES {
                    capped = true;
                    break;
                }
                in_file += 1;
                hits.push(Hit {
                    path: path.clone(),
                    line: index + 1,
                    text: super::text::truncate(line, MAX_LINE_BYTES),
                });
            }
        }
        Ok((hits, scanned, capped))
    }
}

#[async_trait]
impl Tool<()> for GrepTool {
    fn name(&self) -> &'static str {
        "grep_workspace"
    }

    fn description(&self) -> &'static str {
        "Finds the lines matching a regular expression across workspace files, with their paths \
         and line numbers, so the right part of the right file can be read without opening any of \
         them."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string",
                        "description": "Regular expression matched against each line."
                    },
                    "path": {
                        "type": "string",
                        "description": "Relative directory or file to search. Defaults to the \
                                        whole workspace."
                    },
                    "ignore_case": {
                        "type": "boolean",
                        "description": "Match without regard to case. Defaults to true."
                    }
                },
                "required": ["pattern"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let pattern = super::string_argument(&call, "pattern")?;
        let root = call
            .arguments
            .get("path")
            .and_then(Value::as_str)
            .unwrap_or(".")
            .to_string();
        let ignore_case = call
            .arguments
            .get("ignore_case")
            .and_then(Value::as_bool)
            .unwrap_or(true);
        // Compiled with a size bound, because the pattern comes from a model
        // and a pathological one is a way to spend the container's memory.
        let matcher = regex::RegexBuilder::new(&pattern)
            .case_insensitive(ignore_case)
            .size_limit(1 << 20)
            .build()
            .map_err(|error| {
                tinyagents::TinyAgentsError::Validation(format!(
                    "`{pattern}` is not a usable regular expression: {error}"
                ))
            })?;
        let (hits, scanned, capped) = self.search(&root, &matcher).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            render(&pattern, &hits, scanned, capped),
        ))
    }
}

#[cfg(test)]
#[path = "grep_test.rs"]
mod test;
