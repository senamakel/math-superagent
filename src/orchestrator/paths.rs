//! Resolving and guarding the paths a model asks the runtime to write to.
//!
//! A prompt instruction is not a security control, so every model-supplied path
//! is resolved here rather than trusted. The one tool that writes program
//! source lives beside the checks it depends on, because it was the hole in
//! them once already: `write_tool_file` wrote wherever it was asked while every
//! other write path was guarded.

use std::fmt::Write as _;
use std::path::{Component, Path, PathBuf};

use async_trait::async_trait;
use serde_json::json;

use super::{layout, string_argument};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Resolves a model-supplied path against the workspace root.
///
/// Accepts either a relative path or one written against the `/workspace` mount
/// point, because every prompt, and the problem statement handed to the agents,
/// names files as `/workspace/solution.md`. Rejecting that spelling as
/// "traversal" fails a tool call that asked for exactly the right file, and an
/// in-tool validation error aborts the whole specialist run rather than being
/// handed back for the model to correct.
///
/// Stripping the prefix is not a relaxation: `/workspace/x` and `x` denote the
/// same file, and every other absolute path, traversal component, and empty
/// path is still refused here, with callers that write also re-checking the
/// canonical parent.
pub(super) fn checked_workspace_path(workspace: &Path, requested: &str) -> Result<PathBuf> {
    let relative = Path::new(strip_workspace_prefix(requested));
    if relative.as_os_str().is_empty()
        || relative.is_absolute()
        || relative
            .components()
            .any(|part| !matches!(part, Component::Normal(_)))
    {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "path `{requested}` must name a file below /workspace, written relative to it or as \
             an absolute /workspace path, with no traversal"
        )));
    }
    Ok(workspace.join(relative))
}

/// Removes a leading `workspace` mount-point prefix from a requested path.
///
/// Only an exact path component match is stripped, so a sibling directory such
/// as `/workspace-other/secret` keeps its absolute form and is refused by the
/// caller.
///
/// The relative spellings — `workspace/toolkits`, or bare `workspace` — are
/// stripped too. Every agent's working directory *is* `/workspace`, so a path
/// beginning with that component is always the same mistake: naming the mount
/// point from inside it. It cost a live run three consecutive `refresh_index`
/// failures on `workspace`, `workspace/toolkits`, and `workspace/research`,
/// none of which the model could tell apart from the folder genuinely being
/// absent. Nothing is lost by refusing the literal reading: a folder actually
/// named `workspace` inside the workspace would be `/workspace/workspace`,
/// which no part of the runtime or template creates.
pub(super) fn strip_workspace_prefix(requested: &str) -> &str {
    let trimmed = requested.trim();
    for prefix in ["/workspace/", "/workspace", "workspace/", "workspace"] {
        if let Some(rest) = trimmed.strip_prefix(prefix)
            && (prefix.ends_with('/') || rest.is_empty() || rest.starts_with('/'))
        {
            return rest.trim_start_matches('/');
        }
    }
    trimmed
}

#[derive(Debug)]
pub(super) struct WriteToolFile {
    workspace: PathBuf,
    /// The write path, held so writing a `.lean` file re-derives the lemma
    /// index. Optional because two of the three registration sites have no
    /// documents handle and neither writes Lean.
    documents: Option<super::documents::WorkspaceDocuments>,
}

impl WriteToolFile {
    pub(super) fn new(workspace: PathBuf) -> Self {
        Self {
            workspace,
            documents: None,
        }
    }

    /// Gives the writer the write path, so a `.lean` file reaches the index.
    pub(super) fn deriving(mut self, documents: super::documents::WorkspaceDocuments) -> Self {
        self.documents = Some(documents);
        self
    }
}

#[async_trait]
impl Tool<()> for WriteToolFile {
    fn name(&self) -> &'static str {
        "write_tool_file"
    }

    fn description(&self) -> &'static str {
        "Writes a UTF-8 tool source or support file beneath /workspace."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "path": { "type": "string", "description": "Relative path under /workspace." },
                    "content": { "type": "string", "description": "Complete UTF-8 file contents." }
                },
                "required": ["path", "content"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let requested = string_argument(&call, "path")?;
        let content = string_argument(&call, "content")?;
        // Placement is decided here, as it is for `write_document` and an
        // `apply_patch` addition. This tool was the hole in that: it wrote
        // wherever it was asked, so `write_tool_file` with `path: "brute.py"`
        // put a program at the workspace root while the layout was enforced on
        // every other write path. A live run did exactly that within four
        // minutes of starting, and left two different `brute.py` files — one
        // filed, one loose — with nothing to say which was current.
        let relative = layout::placed(&requested);
        let path = checked_workspace_path(&self.workspace, &relative)?;
        let parent = path.parent().ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation("file path has no parent".into())
        })?;
        tokio::fs::create_dir_all(parent).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to create parent directory: {error}"))
        })?;
        let canonical_parent = parent.canonicalize().map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to resolve parent directory: {error}"
            ))
        })?;
        if !canonical_parent.starts_with(&self.workspace) {
            return Err(tinyagents::TinyAgentsError::Validation(
                "file path resolves outside /workspace".into(),
            ));
        }
        tokio::fs::write(&path, &content).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to write tool file: {error}"))
        })?;
        // A written `.lean` file reaches the lemma index here, and this is the
        // refresh that matters most. The other one runs on `lean_check` — but a
        // file nobody checks never fires it, so the *unchecked* files, which are
        // the whole reason the index carries a standing, were the ones least
        // likely to appear in it. A replay of this repository's own history
        // found 54 of 78 files in that state, and a live run reached 17 files
        // against 2 verdicts while the index still described the tree as it had
        // been two checks earlier.
        let mut derived = String::new();
        // By extension on the path Lean itself is given, matching how
        // `lean_check` decides what it will read.
        if std::path::Path::new(&relative)
            .extension()
            .is_some_and(|extension| extension == "lean")
            && let Some(documents) = &self.documents
        {
            super::lemmas::refresh(documents).await;
            let _ = write!(
                derived,
                "\n\nThis is a Lean source and no kernel verdict covers it, so \
                 `{}` lists it under **Never checked** and nothing may rest on it. \
                 Run `lean_check` on it: checking with the shell leaves no verdict, and a \
                 proof the run cannot distinguish from a sentence is worth what a sentence \
                 is worth.",
                super::lemmas::LEMMAS_PATH
            );
        }
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!(
                "wrote {} bytes to {relative}{}{derived}",
                content.len(),
                layout::note(&requested, &relative)
            ),
        ))
    }
}

#[cfg(test)]
#[path = "paths_test.rs"]
mod test;
