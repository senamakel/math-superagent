//! Durable workflow state, kept in the workspace.
//!
//! `TinyFlows` asks a host for a key/value store so a stateful workflow — a
//! `dedup` node's commit ledger, anything a graph wants to survive a restart —
//! has somewhere to live. This crate already has exactly one durable place, and
//! it is the same one everything else writes to: the workspace directory
//! mounted at `/workspace`.
//!
//! # Keys are hashed, not used as paths
//!
//! A key is author-supplied, and an author is a workflow document that may have
//! been written by a model. Using one as a path component is how `../../.env`
//! becomes a file read, so a key never reaches the filesystem: it is hashed,
//! and the hash is the filename. That also removes every other question a
//! path-shaped key raises — length limits, case-insensitive collisions,
//! characters a filesystem refuses — without a validation rule per platform.
//!
//! The original key is stored *inside* the file beside its value, so the store
//! stays readable by a person: the directory is opaque, but any single file
//! says what it is.

use std::path::{Path, PathBuf};

use async_trait::async_trait;
use serde_json::{Value, json};
use tinyflows::caps::StateStore;
use tinyflows::error::{EngineError, Result as EngineResult};

/// Where the store keeps its files, below the workspace root.
///
/// Hidden, because it is runtime bookkeeping rather than the record of an
/// investigation — the same reason `config/.*.json` is git-ignored. A reader
/// opening a workspace should find the mathematics, not a key/value directory.
const STATE_DIR: &str = "config/.workflow-state";

/// Workflow state, one JSON file per key, under the workspace.
#[derive(Clone, Debug)]
pub(crate) struct WorkspaceState {
    root: PathBuf,
}

impl WorkspaceState {
    /// Builds a store rooted at `workspace`.
    pub(crate) fn new(workspace: impl Into<PathBuf>) -> Self {
        Self {
            root: workspace.into(),
        }
    }

    /// The file a key lives in.
    ///
    /// The hash is `DefaultHasher`, which is neither stable across Rust
    /// releases nor cryptographic — and both are fine here, because nothing
    /// outside this process reads the mapping and a collision loses a cache
    /// entry rather than corrupting a result. What it must be is total over
    /// arbitrary key strings, which it is.
    fn path_for(&self, key: &str) -> PathBuf {
        use std::hash::{Hash as _, Hasher as _};
        let mut hasher = std::collections::hash_map::DefaultHasher::new();
        key.hash(&mut hasher);
        self.root
            .join(STATE_DIR)
            .join(format!("{:016x}.json", hasher.finish()))
    }

    /// Reads the entry at `path`, if it holds one for `key`.
    ///
    /// The key is compared as well as the path, so a hash collision reads as a
    /// miss rather than as another key's value. A miss is recoverable; the
    /// wrong value silently is not.
    fn read_entry(path: &Path, key: &str) -> Option<Value> {
        let text = std::fs::read_to_string(path).ok()?;
        let entry: Value = serde_json::from_str(&text).ok()?;
        if entry.get("key").and_then(Value::as_str) != Some(key) {
            return None;
        }
        entry.get("value").cloned()
    }
}

#[async_trait]
impl StateStore for WorkspaceState {
    /// Loads `key`, or `None` when nothing is stored under it.
    ///
    /// An unreadable or malformed file is a miss rather than an error: this
    /// store's callers treat absence as "not done yet", which is the safe
    /// reading of a file this process cannot make sense of.
    ///
    /// # Errors
    ///
    /// Does not fail; the signature is the trait's.
    async fn load(&self, key: &str) -> EngineResult<Option<Value>> {
        Ok(Self::read_entry(&self.path_for(key), key))
    }

    /// Stores `value` under `key`.
    ///
    /// # Errors
    ///
    /// Returns a capability error when the directory cannot be created or the
    /// file cannot be written — a store that silently dropped a write would let
    /// a `dedup` node run the same work twice and report it as new.
    async fn store(&self, key: &str, value: Value) -> EngineResult<()> {
        let path = self.path_for(key);
        if let Some(parent) = path.parent() {
            std::fs::create_dir_all(parent).map_err(|error| {
                EngineError::Capability(format!(
                    "workflow state directory {} is unusable: {error}",
                    parent.display()
                ))
            })?;
        }
        let entry = json!({ "key": key, "value": value });
        std::fs::write(&path, entry.to_string()).map_err(|error| {
            EngineError::Capability(format!(
                "workflow state for `{key}` could not be written: {error}"
            ))
        })
    }
}

#[cfg(test)]
#[path = "state_test.rs"]
mod test;
