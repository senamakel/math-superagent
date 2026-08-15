//! Bounded tools for workspace documents and a local searchable index.

use std::cmp::Reverse;
use std::fmt::Write as _;
use std::path::PathBuf;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// The local search index, kept under `config/` with the run's other plumbing.
///
/// It is runtime bookkeeping, not work: nothing in it is worth a row in the
/// listing an agent reads before deciding what to do next.
const INDEX_PATH: &str = "config/.document-index.json";
/// Folder every externally-sourced document is filed under.
///
/// Enforced here rather than asked for in a prompt: downloads are the one kind
/// of file that arrives from outside the run, and keeping them in one place is
/// what lets an agent tell at a glance what it gathered from what it derived.
/// A prompt instruction would hold only until a model chose otherwise.
pub(super) const RESEARCH_DIR: &str = "research";
/// Folder holding the untouched bytes of every download.
///
/// Kept because conversion is lossy and occasionally wrong: when a converted
/// document reads oddly, the only way to tell a bad source from a bad
/// converter is the original. It is hidden from `list_workspace` and excluded
/// from the index so it never competes for an agent's attention or context —
/// it exists for a human debugging a conversion, not for the run.
pub(super) const RAW_DIR: &str = "raw";
const MAX_DOCUMENT_BYTES: usize = 5 * 1024 * 1024;

/// Entries named when a requested path does not exist.
///
/// Enough to recognise the file that was meant, few enough that a large folder
/// cannot turn one failed read into a wall of text.
const NEARBY_ENTRIES: usize = 20;
/// Suffix marking the full converted text of a source.
pub(super) const FULL_TEXT_SUFFIX: &str = ".full.md";

const SOURCE_DIR: &str = "research/sources";
const DIGEST_DIR: &str = "research/summaries";

const MAX_SEARCH_RESULTS: usize = 10;

#[derive(Clone, Debug)]
pub(super) struct WorkspaceDocuments {
    workspace: PathBuf,
    client: reqwest::Client,
    /// Serialises the index's read-modify-write cycle.
    ///
    /// A model routinely issues several `index_document` calls in one turn,
    /// and the harness runs them concurrently. Each reads the index, appends
    /// its own path, and writes the result back, so without this the last
    /// write silently discards the others' entries.
    ///
    /// Worse was observed on Euler 579. `tokio::fs::write` truncates and then
    /// writes, which is two operations, not one: three concurrent calls
    /// interleaved so a 34-byte write landed inside a 38-byte file and left
    /// the previous content's last four bytes stranded on the end. The index
    /// became `[…]f"\n]` — invalid JSON — and every subsequent
    /// `index_document` failed with a serialization error the model had no
    /// way to act on, because the corruption was in runtime bookkeeping it
    /// cannot see or repair.
    index_lock: Arc<tokio::sync::Mutex<()>>,
    /// Where a downloaded source is filed in durable memory, when there is one.
    ///
    /// Optional because a document tool set is useful without a memory server
    /// — the tests build one — and because a library that cannot be filed must
    /// still be downloaded. Filing is best effort at the call site for the same
    /// reason the frontier and the index row are: the bytes are already on
    /// disk, and a memory that refused the document must not turn a stored
    /// source into a failed tool call.
    library: Option<super::vector::VectorStore>,
    /// The evidence screen, on a calibration run.
    ///
    /// Only `download_document` is wrapped with it. That tool fetches an
    /// arbitrary URL, it is granted to almost every role, and — unlike the
    /// search tools — it is **not** withheld by `MATH_AGENT_RESEARCH`, so it is
    /// the second way onto the web and the one most easily overlooked. The
    /// other document tools read and write files the run itself produced,
    /// where there is nothing to withhold.
    screen: Option<super::screen::Screen>,
}

include!("documents_store.rs");
include!("documents_paths.rs");
include!("documents_tool.rs");
include!("documents_arguments.rs");

#[cfg(test)]
#[path = "documents_test.rs"]
mod test;
