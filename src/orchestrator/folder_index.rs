//! A per-folder `INDEX.md` saying what each file is for.
//!
//! `list_workspace` answers what exists; it cannot answer what anything is
//! for. After a long run a workspace holds `brute.py`, `solution.py`,
//! `pointcount.py`, `verify_matrix.py`, `scratchpad_verify2.py`, and a dozen
//! sources, and nothing on disk distinguishes the oracle from the answer, or a
//! superseded experiment from the file the result actually came out of. A
//! later agent — or a later run — has to open each one to find out, which is
//! exactly the context spend the rest of this module works to avoid.
//!
//! So each folder carries an `INDEX.md`: one row per file, saying what it is
//! and why it is there.
//!
//! The index is maintained through explicit tools rather than silently on
//! every write, because a description is a judgement about purpose and only
//! the agent that wrote the file holds it. What is *not* left to judgement is
//! whether the index matches the directory: [`refresh_index`] re-derives the
//! file list from disk, keeps the descriptions already written, marks new
//! files undescribed, and drops rows for files that no longer exist. A
//! forgotten description therefore shows up as a visible gap, and never as an
//! index that quietly disagrees with the folder it describes.

use std::collections::BTreeMap;
use std::fmt::Write as _;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::documents::WorkspaceDocuments;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// The per-folder index file.
pub(super) const INDEX_FILE: &str = "INDEX.md";

/// Placeholder for a file nobody has described yet.
const UNDESCRIBED: &str = "_(undescribed)_";

/// Normalises a folder a model named, to the form the rest of this module uses.
///
/// The mount point is stripped here rather than left to the path checker
/// downstream, because a folder is allowed to be the empty string — the
/// workspace root — and the checker rejects that as naming no file. So
/// `workspace` has to become `""` before it gets there, not after.
///
/// `.` is the root for the same reason. It is the obvious way to ask for the
/// current folder, and the path checker refuses it as traversal — a true
/// answer to a question nobody asked, since the model wanted the folder it is
/// already standing in.
fn folder_name(requested: &str) -> String {
    let normalised = super::strip_workspace_prefix(requested)
        .trim_start_matches("./")
        .trim_matches('/');
    if normalised == "." {
        return String::new();
    }
    normalised.to_string()
}

/// Splits a path into its folder and file name.
fn split(relative: &str) -> (String, String) {
    let trimmed = folder_name(relative);
    match trimmed.rsplit_once('/') {
        Some((folder, name)) => (folder.to_string(), name.to_string()),
        None => (String::new(), trimmed),
    }
}

/// Returns the index path for the folder holding `relative`.
fn index_for(folder: &str) -> String {
    if folder.is_empty() {
        INDEX_FILE.to_string()
    } else {
        format!("{folder}/{INDEX_FILE}")
    }
}

/// Reads the descriptions already recorded in an index.
///
/// Tolerant by design: an index a human or an agent has reformatted must not
/// lose its descriptions, so anything shaped like a table row is accepted and
/// everything else ignored.
pub(super) fn parse(existing: &str) -> BTreeMap<String, String> {
    let mut entries = BTreeMap::new();
    for line in existing.lines() {
        let line = line.trim();
        let Some(body) = line.strip_prefix('|') else {
            continue;
        };
        let mut columns = body.split('|').map(str::trim);
        let (Some(name), Some(description)) = (columns.next(), columns.next()) else {
            continue;
        };
        // Skip the header and its separator row.
        let name = name.trim_matches('`').trim();
        if name.is_empty() || name.eq_ignore_ascii_case("file") || name.starts_with("---") {
            continue;
        }
        entries.insert(name.to_string(), description.to_string());
    }
    entries
}

/// Renders an index for `folder` from its entries.
pub(super) fn render(folder: &str, entries: &BTreeMap<String, String>) -> String {
    let title = if folder.is_empty() {
        "workspace"
    } else {
        folder
    };
    let mut out = format!(
        "# Index — {title}\n\n\
         What each file in this folder is for. Keep it current: describe a file when you create \
         it, and refresh this index after adding, renaming, or deleting files.\n\n\
         | File | Purpose |\n| --- | --- |\n"
    );
    for (name, description) in entries {
        let description = if description.trim().is_empty() {
            UNDESCRIBED
        } else {
            description.trim()
        };
        let _ = writeln!(out, "| `{name}` | {description} |");
    }
    if entries.is_empty() {
        // Deliberately not a table row. A placeholder row parses back as a
        // file called `_(empty)_`, which the next refresh would then carry
        // forward as though the folder contained it.
        out.push_str("\n_This folder is empty._\n");
    }
    out
}

/// The two index tools.
#[derive(Clone, Copy, Debug)]
enum IndexToolKind {
    Describe,
    Refresh,
}

impl IndexToolKind {
    const ALL: [Self; 2] = [Self::Describe, Self::Refresh];
}

/// A tool that maintains `INDEX.md` for a folder.
#[derive(Debug)]
pub(super) struct FolderIndexTool {
    kind: IndexToolKind,
    documents: WorkspaceDocuments,
}

impl FolderIndexTool {
    /// Builds both index tools.
    pub(super) fn all(documents: &WorkspaceDocuments) -> Vec<Arc<dyn Tool<()>>> {
        IndexToolKind::ALL
            .into_iter()
            .map(|kind| {
                Arc::new(Self {
                    kind,
                    documents: documents.clone(),
                }) as Arc<dyn Tool<()>>
            })
            .collect()
    }

    /// Reads a folder's current index entries, if it has one.
    async fn entries(&self, folder: &str) -> BTreeMap<String, String> {
        match self.documents.read_document(&index_for(folder)).await {
            Ok(existing) => parse(&existing),
            Err(_) => BTreeMap::new(),
        }
    }

    async fn write(&self, folder: &str, entries: &BTreeMap<String, String>) -> Result<()> {
        self.documents
            .write_document(&index_for(folder), &render(folder, entries))
            .await
    }

    async fn describe(&self, call: &ToolCall) -> Result<String> {
        let path = required(&call.arguments, "path")?;
        let purpose = required(&call.arguments, "purpose")?;
        let (folder, name) = split(&path);
        if name.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "`path` must name a file, not a folder".into(),
            ));
        }
        if name == INDEX_FILE {
            return Err(tinyagents::TinyAgentsError::Validation(
                "the index does not describe itself".into(),
            ));
        }
        let mut entries = self.entries(&folder).await;
        entries.insert(name.clone(), purpose.trim().replace('\n', " "));
        self.write(&folder, &entries).await?;
        Ok(format!("described {name} in {}", index_for(&folder)))
    }

    async fn refresh(&self, call: &ToolCall) -> Result<String> {
        let folder = folder_name(
            call.arguments
                .get("path")
                .and_then(Value::as_str)
                .unwrap_or_default(),
        );
        let described = self.entries(&folder).await;
        let present = self.documents.file_names(&folder).await?;

        let mut entries = BTreeMap::new();
        for name in &present {
            if name == INDEX_FILE {
                continue;
            }
            let description = described.get(name).cloned().unwrap_or_default();
            entries.insert(name.clone(), description);
        }
        let added = entries
            .iter()
            .filter(|(name, _)| !described.contains_key(*name))
            .count();
        let removed = described
            .keys()
            .filter(|name| !entries.contains_key(*name))
            .count();
        self.write(&folder, &entries).await?;
        Ok(format!(
            "refreshed {} — {} files, {added} newly listed and needing a purpose, {removed} stale \
             rows dropped",
            index_for(&folder),
            entries.len()
        ))
    }
}

fn required(arguments: &Value, name: &str) -> Result<String> {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .map(str::to_string)
        .ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!(
                "`{name}` is required and must be a non-empty string"
            ))
        })
}

#[async_trait]
impl Tool<()> for FolderIndexTool {
    fn name(&self) -> &'static str {
        match self.kind {
            IndexToolKind::Describe => "describe_file",
            IndexToolKind::Refresh => "refresh_index",
        }
    }

    fn description(&self) -> &'static str {
        match self.kind {
            IndexToolKind::Describe => {
                "Records what a file is for in its folder's INDEX.md, creating the index if \
                 needed. Call it whenever you create a file, or when a file's purpose changes. \
                 Say what the file is and why it exists — `solution.py` is less useful than \
                 \"efficient peel solver; the answer comes from here\"."
            }
            IndexToolKind::Refresh => {
                "Rebuilds a folder's INDEX.md from what is actually on disk, keeping the \
                 descriptions already written, listing new files as undescribed, and dropping \
                 rows for files that no longer exist. Call it after adding, renaming, or deleting \
                 files so the index never disagrees with the folder."
            }
        }
    }

    fn schema(&self) -> ToolSchema {
        let schema = match self.kind {
            IndexToolKind::Describe => json!({
                "type": "object",
                "properties": {
                    "path": { "type": "string" },
                    "purpose": { "type": "string" }
                },
                "required": ["path", "purpose"],
                "additionalProperties": false
            }),
            IndexToolKind::Refresh => json!({
                "type": "object",
                "properties": { "path": { "type": "string" } },
                "additionalProperties": false
            }),
        };
        ToolSchema::new(self.name(), self.description(), schema)
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let message = match self.kind {
            IndexToolKind::Describe => self.describe(&call).await?,
            IndexToolKind::Refresh => self.refresh(&call).await?,
        };
        Ok(ToolResult::text(call.id, self.name().to_string(), message))
    }
}

#[cfg(test)]
mod test;
