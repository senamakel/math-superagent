//! Local similarity search across everything the run has written down.
//!
//! `search_documents` answers a different question: it matches literal terms,
//! and only against documents an agent explicitly called `index_document` on.
//! Downloads get indexed; the run's own thinking does not. So `memory.md`,
//! `reflections/`, `scratchpad.md`, and the toolkit sat unreachable to anything
//! but a path an agent already knew, which meant the inventor re-proposed
//! approaches whose failure was recorded three files away, and the pattern
//! agent rebuilt helpers that already existed.
//!
//! This walks the workspace instead of an index, and ranks by cosine similarity
//! over the same deterministic feature-hashing encoder the Qdrant notes use, so
//! a query matches on shared vocabulary rather than on an exact phrase and the
//! runtime still needs no embedding provider. It is a way back into the run's
//! own record, not a replacement for reading the file it points at.

use std::path::{Path, PathBuf};
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Files a single search will read.
///
/// A bound rather than a budget: a workspace late in a run holds hundreds of
/// files, and reading all of them to answer one question would cost more than
/// the answer is worth.
const MAX_FILES_SCANNED: usize = 400;

/// Bytes read from any one file.
///
/// Enough to carry a derivation or a reflection whole. A converted paper's full
/// text runs far past this, and its summary — the file the scholar is held to —
/// is what should match anyway.
const MAX_FILE_BYTES: usize = 64 * 1024;

/// Matches returned by one search.
const MAX_RESULTS: usize = 8;

/// Characters of surrounding text shown per match.
const SNIPPET_CHARS: usize = 320;

/// Directory depth walked below the workspace root.
const MAX_DEPTH: usize = 4;

/// Extensions worth reading. Anything else is data or a binary.
const TEXT_EXTENSIONS: [&str; 6] = ["md", "py", "txt", "toml", "json", "sh"];

/// Similarity search over the run's own files.
#[derive(Clone, Debug)]
pub(super) struct RecallWorkspaceTool {
    workspace: PathBuf,
}

impl RecallWorkspaceTool {
    pub(super) fn new(workspace: PathBuf) -> Arc<dyn Tool<()>> {
        Arc::new(Self { workspace })
    }

    /// Collects readable text files below the workspace root.
    fn collect(&self, folder: &Path, depth: usize, found: &mut Vec<PathBuf>) {
        if depth > MAX_DEPTH || found.len() >= MAX_FILES_SCANNED {
            return;
        }
        let Ok(entries) = std::fs::read_dir(folder) else {
            return;
        };
        for entry in entries.flatten() {
            if found.len() >= MAX_FILES_SCANNED {
                return;
            }
            let name = entry.file_name().to_string_lossy().to_string();
            // Whatever the workspace listing hides, this hides too: an agent
            // must not reach the event log or the raw downloads through a
            // search when it cannot reach them through a path.
            if name.starts_with('.') || super::documents::is_hidden(&name) {
                continue;
            }
            let path = entry.path();
            if path.is_dir() {
                self.collect(&path, depth + 1, found);
            } else if is_text(&path) {
                found.push(path);
            }
        }
    }

    /// Ranks every readable file against the query.
    fn search(&self, query: &str) -> Vec<Value> {
        let wanted = super::vector::embed(query);
        let mut files = Vec::new();
        self.collect(&self.workspace, 0, &mut files);

        let mut scored: Vec<(f32, Value)> = Vec::new();
        for path in files {
            let Ok(bytes) = std::fs::read(&path) else {
                continue;
            };
            let text = String::from_utf8_lossy(&bytes[..bytes.len().min(MAX_FILE_BYTES)]);
            if text.trim().is_empty() {
                continue;
            }
            let score = similarity(&wanted, &super::vector::embed(&text));
            if score <= 0.0 {
                continue;
            }
            let relative = path
                .strip_prefix(&self.workspace)
                .unwrap_or(&path)
                .to_string_lossy()
                .to_string();
            scored.push((
                score,
                json!({
                    "path": relative,
                    "score": (score * 1000.0).round() / 1000.0,
                    "snippet": snippet(&text, query),
                }),
            ));
        }
        scored.sort_by(|left, right| {
            right
                .0
                .partial_cmp(&left.0)
                .unwrap_or(std::cmp::Ordering::Equal)
        });
        scored
            .into_iter()
            .take(MAX_RESULTS)
            .map(|(_, value)| value)
            .collect()
    }
}

#[async_trait]
impl Tool<()> for RecallWorkspaceTool {
    fn name(&self) -> &str {
        "search_workspace"
    }

    fn description(&self) -> &str {
        "Finds files in this workspace whose wording is closest to a question, across derivations, \
         memory.md, reflections, research summaries, and toolkit helpers. Use it before proposing \
         an approach or building a helper, to see what the run already tried, learned, or wrote. \
         Returns paths with a snippet; read the file for the detail."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(json!({
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "What you are looking for, in words you would expect the file \
                                    to use.",
                    "maxLength": 500
                }
            },
            "required": ["query"],
            "additionalProperties": false
        }))
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = call
            .arguments
            .get("query")
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|query| !query.is_empty())
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation("query must be a non-empty string".into())
            })?;
        let matches = self.search(query);
        // An empty result is reported as one. A bare `[]` reads as a failure,
        // and the useful next move — widen the wording, or accept that the run
        // has not been here before — depends on knowing which it was.
        if matches.is_empty() {
            return Ok(ToolResult::new(
                call.id,
                format!("nothing in this workspace resembles `{query}` yet"),
            ));
        }
        Ok(ToolResult::new(
            call.id,
            serde_json::to_string_pretty(&json!({ "matches": matches }))?,
        ))
    }
}

/// Cosine similarity of two unit vectors from the shared encoder.
fn similarity(left: &[f32], right: &[f32]) -> f32 {
    left.iter()
        .zip(right.iter())
        .map(|(one, other)| one * other)
        .sum()
}

/// Returns whether a path is worth reading as text.
fn is_text(path: &Path) -> bool {
    path.extension()
        .and_then(|extension| extension.to_str())
        .is_some_and(|extension| TEXT_EXTENSIONS.contains(&extension.to_ascii_lowercase().as_str()))
}

/// Returns the passage around the query's strongest literal foothold.
///
/// The ranking is by shared vocabulary, so a file can match without containing
/// the query verbatim. Falling back to the opening is right there: the head of
/// a derivation or a reflection says what it is.
fn snippet(text: &str, query: &str) -> String {
    let lowercase = text.to_lowercase();
    let anchor = query
        .split_whitespace()
        .filter(|term| term.len() > 3)
        .filter_map(|term| lowercase.find(&term.to_lowercase()))
        .min()
        .unwrap_or_default();
    let start = floor_boundary(text, anchor.saturating_sub(80));
    let end = floor_boundary(text, (start + SNIPPET_CHARS).min(text.len()));
    text[start..end].replace('\n', " ").trim().to_string()
}

/// Rounds down to a character boundary so slicing cannot split a code point.
fn floor_boundary(text: &str, mut index: usize) -> usize {
    while index > 0 && !text.is_char_boundary(index) {
        index -= 1;
    }
    index.min(text.len())
}

#[cfg(test)]
mod test;
