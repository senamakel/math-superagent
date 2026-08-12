//! Diff-shaped multi-file edits, in the `apply_patch` envelope Codex uses.
//!
//! The existing tools each rewrite or replace one thing at a time, and both
//! costs show up in a live run. `write_tool_file` re-emits an entire file to
//! change one line: a 3.5 KB script costs roughly a thousand output tokens per
//! revision, generation time is linear in output length, and a turn that runs
//! past the output cap is truncated and retried at double the budget. And a
//! change that spans files — a helper in `lib/rle.py` plus its row in
//! `lib/INDEX.md` — takes several calls, any of which can be the last one before
//! the model changes course, leaving the catalogue describing a function that
//! does something else.
//!
//! This applies one envelope containing many operations, so a coordinated edit
//! is one call that either lands completely or not at all.
//!
//! The format is Codex's, deliberately: it is documented, models have seen it,
//! and inventing a private diff dialect for a small model to emit would be a
//! worse bet than borrowing one it may already know.
//!
//! ```text
//! *** Begin Patch
//! *** Update File: solution.py
//! @@ def peel(p, q):
//!  bits = []
//! -    while a != b:
//! +    while a != b and steps < limit:
//! *** Add File: lib/rle.py
//! +def sbe(n): ...
//! *** Delete File: scratch.py
//! *** End Patch
//! ```
//!
//! Two deviations from Codex are deliberate. Context must match **exactly**:
//! upstream falls back to fuzzy matching, which is right for an interactive
//! tool with a human watching and wrong here, where a patch quietly landing in
//! the wrong place produces a plausible program that computes something else.
//! And application is **atomic**: every operation is parsed, resolved, and
//! checked against the current file contents before a single byte is written,
//! so a bad hunk in the third file cannot leave the first two rewritten.

use std::collections::HashSet;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::documents::WorkspaceDocuments;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

const BEGIN: &str = "*** Begin Patch";
const END: &str = "*** End Patch";
const ADD: &str = "*** Add File: ";
const DELETE: &str = "*** Delete File: ";
const UPDATE: &str = "*** Update File: ";
const MOVE: &str = "*** Move to: ";
const END_OF_FILE: &str = "*** End of File";

/// One file operation inside a patch envelope.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) enum FileOp {
    /// Create a new file with the given contents.
    Add { path: String, contents: String },
    /// Remove an existing file.
    Delete { path: String },
    /// Rewrite an existing file in place, optionally renaming it.
    Update {
        path: String,
        move_to: Option<String>,
        hunks: Vec<Hunk>,
    },
}

impl FileOp {
    fn path(&self) -> &str {
        match self {
            Self::Add { path, .. } | Self::Delete { path } | Self::Update { path, .. } => path,
        }
    }
}

/// A contiguous change within one file.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct Hunk {
    /// Optional `@@ <header>` text used to narrow where the hunk may match.
    header: Option<String>,
    /// Lines to find: the context and removal lines, in order.
    expected: Vec<String>,
    /// Lines to write in their place: the context and addition lines.
    replacement: Vec<String>,
}

/// Parses a patch envelope into its file operations.
///
/// # Errors
///
/// Returns an error when the envelope markers are missing, a header is
/// unrecognised, a path is absolute or empty, or a hunk line lacks one of the
/// ` `, `-`, `+` prefixes.
pub(super) fn parse(patch: &str) -> Result<Vec<FileOp>> {
    let body = envelope(patch)?;
    let mut lines = body.iter().peekable();
    let mut ops: Vec<FileOp> = Vec::new();
    let mut seen: HashSet<String> = HashSet::new();

    // The path an `Add` asked for, when placement moved it. Both spellings
    // have to collide with a later operation: a patch adding `a.py` and then
    // deleting `a.py` is malformed whichever folder the add landed in.
    let mut requested: Option<String> = None;
    while let Some(line) = lines.next() {
        let op = if let Some(path) = line.strip_prefix(ADD) {
            let mut contents = String::new();
            while let Some(next) = lines.peek() {
                let Some(added) = next.strip_prefix('+') else {
                    break;
                };
                contents.push_str(added);
                contents.push('\n');
                lines.next();
            }
            // A new file is placed by the same rule as a written one: adding
            // through a patch must not be the way around the layout. An
            // update or a delete names a file that already exists, so both
            // are left exactly as addressed.
            let asked = checked_path(path)?;
            let filed = super::layout::placed(&asked);
            if filed != asked {
                requested = Some(asked);
            }
            FileOp::Add {
                path: filed,
                contents,
            }
        } else if let Some(path) = line.strip_prefix(DELETE) {
            FileOp::Delete {
                path: checked_path(path)?,
            }
        } else if let Some(raw) = line.strip_prefix(UPDATE) {
            let target = checked_path(raw)?;
            let move_to = match lines.peek().and_then(|next| next.strip_prefix(MOVE)) {
                Some(renamed) => {
                    lines.next();
                    Some(checked_path(renamed)?)
                }
                None => None,
            };
            let mut hunks = Vec::new();
            while let Some(next) = lines.peek() {
                if !next.starts_with("@@") {
                    break;
                }
                let header = next.trim_start_matches('@').trim().to_string();
                lines.next();
                hunks.push(read_hunk(
                    (!header.is_empty()).then_some(header),
                    &mut lines,
                )?);
            }
            if hunks.is_empty() {
                return Err(invalid(format!(
                    "`{UPDATE}{target}` has no `@@` hunk; an update must say what to change"
                )));
            }
            FileOp::Update {
                path: target,
                move_to,
                hunks,
            }
        } else if line.trim().is_empty() {
            continue;
        } else {
            return Err(invalid(format!(
                "expected a file header (`{ADD}`, `{UPDATE}`, or `{DELETE}`), found `{line}`"
            )));
        };

        let collided = !seen.insert(op.path().to_string())
            || requested.take().is_some_and(|asked| !seen.insert(asked));
        if collided {
            return Err(invalid(format!(
                "`{}` appears twice in one patch; combine the changes into a single operation",
                op.path()
            )));
        }
        ops.push(op);
    }

    if ops.is_empty() {
        return Err(invalid("patch contains no file operations".to_string()));
    }
    Ok(ops)
}

/// Strips the envelope markers and returns the lines between them.
fn envelope(patch: &str) -> Result<Vec<String>> {
    let trimmed = patch.trim_matches(['\n', '\r']);
    let mut lines: Vec<String> = trimmed.lines().map(str::to_string).collect();
    if lines.first().map(String::as_str) != Some(BEGIN) {
        return Err(invalid(format!("patch must start with `{BEGIN}`")));
    }
    if lines.last().map(String::as_str) != Some(END) {
        return Err(invalid(format!("patch must end with `{END}`")));
    }
    lines.pop();
    lines.remove(0);
    Ok(lines)
}

/// Reads one hunk's ` `/`-`/`+` lines.
fn read_hunk<'a>(
    header: Option<String>,
    lines: &mut std::iter::Peekable<impl Iterator<Item = &'a String>>,
) -> Result<Hunk> {
    let mut expected = Vec::new();
    let mut replacement = Vec::new();
    while let Some(next) = lines.peek() {
        if next.starts_with("@@") || next.starts_with("*** ") {
            // `*** End of File` closes the hunk and is otherwise informational:
            // the exact-match applier already knows where the file ends.
            if next.as_str() == END_OF_FILE {
                lines.next();
            }
            break;
        }
        let line = lines.next().unwrap_or(&String::new()).clone();
        match line.chars().next() {
            Some('+') => replacement.push(line[1..].to_string()),
            Some('-') => expected.push(line[1..].to_string()),
            Some(' ') => {
                expected.push(line[1..].to_string());
                replacement.push(line[1..].to_string());
            }
            // A completely empty line is a context line whose trailing space
            // an editor or the model trimmed. Treating it as an error would
            // reject otherwise-correct patches over invisible whitespace.
            None => {
                expected.push(String::new());
                replacement.push(String::new());
            }
            // An unprefixed line is a context line whose leading space the
            // model dropped — the single most common way a small model
            // malforms this envelope. The reading is unambiguous (only ' ',
            // '-' and '+' carry meaning, and the other two are present), and
            // rejecting it would spend a whole turn on punctuation. Strictness
            // that matters lives in the matching, not here.
            Some(_) => {
                expected.push(line.clone());
                replacement.push(line);
            }
        }
    }
    if expected.is_empty() && replacement.is_empty() {
        return Err(invalid("hunk is empty".to_string()));
    }
    Ok(Hunk {
        header,
        expected,
        replacement,
    })
}

/// Rejects absolute and empty paths, tolerating the `/workspace/` prefix.
///
/// The grammar says references are always relative. Models write the absolute
/// form anyway, having just been told the working directory is `/workspace`,
/// so the common spelling is trimmed rather than refused.
fn checked_path(path: &str) -> Result<String> {
    let path = super::strip_workspace_prefix(path.trim());
    if path.is_empty() {
        return Err(invalid("file header has an empty path".to_string()));
    }
    if path.starts_with('/') {
        return Err(invalid(format!(
            "`{path}` is absolute; patch paths are relative to /workspace"
        )));
    }
    Ok(path.to_string())
}

/// Applies one hunk to `content`, returning the rewritten text.
///
/// Matching is exact and unambiguous: the hunk's context and removal lines
/// must appear verbatim, and exactly once within the region the `@@` header
/// selects. A patch that could land in two places is refused rather than
/// guessed at, because the wrong guess yields a program that runs and computes
/// the wrong thing.
fn apply_hunk(path: &str, content: &str, hunk: &Hunk) -> Result<String> {
    let lines: Vec<&str> = content.split('\n').collect();
    let from = match hunk.header.as_deref() {
        Some(header) => lines
            .iter()
            .position(|line| line.contains(header))
            .ok_or_else(|| {
                invalid(format!(
                    "`{path}`: no line matches the hunk header `@@ {header}`"
                ))
            })?,
        None => 0,
    };

    let matches: Vec<usize> = (from..=lines.len().saturating_sub(hunk.expected.len()))
        .filter(|start| {
            lines[*start..*start + hunk.expected.len()]
                .iter()
                .zip(&hunk.expected)
                .all(|(actual, wanted)| *actual == wanted.as_str())
        })
        .collect();

    match matches.as_slice() {
        [] => Err(invalid(format!(
            "`{path}`: the hunk's context was not found. The file must contain these lines \
             exactly, in order:\n{}",
            hunk.expected.join("\n")
        ))),
        [start] => {
            let mut rewritten: Vec<&str> = lines[..*start].to_vec();
            rewritten.extend(hunk.replacement.iter().map(String::as_str));
            rewritten.extend_from_slice(&lines[start + hunk.expected.len()..]);
            Ok(rewritten.join("\n"))
        }
        many => Err(invalid(format!(
            "`{path}`: the hunk's context matches {} places. Add surrounding context lines, or \
             an `@@ <enclosing function>` header, so it identifies exactly one.",
            many.len()
        ))),
    }
}

fn invalid(message: String) -> tinyagents::TinyAgentsError {
    tinyagents::TinyAgentsError::Validation(message)
}

/// The `apply_patch` tool.
#[derive(Debug)]
pub(super) struct ApplyPatchTool {
    documents: WorkspaceDocuments,
}

impl ApplyPatchTool {
    pub(super) fn new(documents: WorkspaceDocuments) -> Self {
        Self { documents }
    }

    /// Resolves every operation against the current workspace without writing.
    ///
    /// Returning the full planned contents before anything is written is what
    /// makes the patch atomic.
    async fn plan(&self, ops: &[FileOp]) -> Result<Vec<Planned>> {
        let mut planned = Vec::new();
        for op in ops {
            match op {
                FileOp::Add { path, contents } => {
                    if self.documents.exists(path) {
                        return Err(invalid(format!(
                            "`{path}` already exists; use `{UPDATE}{path}` to change it"
                        )));
                    }
                    planned.push(Planned::Write {
                        path: path.clone(),
                        contents: contents.clone(),
                    });
                }
                FileOp::Delete { path } => {
                    if !self.documents.exists(path) {
                        return Err(invalid(format!("`{path}` does not exist")));
                    }
                    planned.push(Planned::Remove { path: path.clone() });
                }
                FileOp::Update {
                    path,
                    move_to,
                    hunks,
                } => {
                    let mut contents = self.documents.read_document(path).await?;
                    for hunk in hunks {
                        contents = apply_hunk(path, &contents, hunk)?;
                    }
                    let target = move_to.clone().unwrap_or_else(|| path.clone());
                    if move_to.is_some() {
                        planned.push(Planned::Remove { path: path.clone() });
                    }
                    planned.push(Planned::Write {
                        path: target,
                        contents,
                    });
                }
            }
        }
        Ok(planned)
    }
}

/// A resolved change, ready to write.
enum Planned {
    Write { path: String, contents: String },
    Remove { path: String },
}

#[async_trait]
impl Tool<()> for ApplyPatchTool {
    fn name(&self) -> &'static str {
        "apply_patch"
    }

    fn description(&self) -> &'static str {
        "Applies a multi-file patch envelope atomically. Cheaper than rewriting a whole file to \
         change a few lines, and the way to keep a change and its documentation in step. Format: \
         `*** Begin Patch` / one or more of `*** Add File: <path>` (every following line prefixed \
         `+`), `*** Delete File: <path>`, or `*** Update File: <path>` (optionally followed by \
         `*** Move to: <path>`, then `@@` hunks whose lines start with ' ' for context, '-' to \
         remove, '+' to add) / `*** End Patch`. Paths are relative to /workspace. Context must \
         match exactly and identify one location; nothing is written unless every operation \
         succeeds."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": { "patch": { "type": "string" } },
                "required": ["patch"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let patch = call
            .arguments
            .get("patch")
            .and_then(Value::as_str)
            .ok_or_else(|| invalid("`patch` is required and must be a string".to_string()))?;

        let ops = parse(patch)?;
        let planned = self.plan(&ops).await?;

        let mut touched = Vec::new();
        for change in planned {
            match change {
                Planned::Write { path, contents } => {
                    self.documents.write_document(&path, &contents).await?;
                    touched.push(path);
                }
                Planned::Remove { path } => {
                    self.documents.remove(&path).await?;
                    touched.push(path);
                }
            }
        }

        Ok(ToolResult::text(
            call.id,
            self.name().to_string(),
            format!("applied patch to {}", touched.join(", ")),
        ))
    }
}

/// Builds the tool, boxed for registration.
pub(super) fn tool(documents: WorkspaceDocuments) -> Arc<dyn Tool<()>> {
    Arc::new(ApplyPatchTool::new(documents))
}

#[cfg(test)]
#[path = "patch_test.rs"]
mod test;
