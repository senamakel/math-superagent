//! Deterministic tests for workflow state kept in the workspace.
#![allow(clippy::expect_used)]

use super::*;

/// A workspace that cleans up after itself, so these tests leave no files.
struct Scratch {
    root: PathBuf,
}

impl Scratch {
    fn new(name: &str) -> Self {
        let root = std::env::temp_dir().join(format!("riemann-state-{name}-{}", std::process::id()));
        let _ = std::fs::remove_dir_all(&root);
        std::fs::create_dir_all(&root).expect("a scratch workspace can be created");
        Self { root }
    }

    fn store(&self) -> WorkspaceState {
        WorkspaceState::new(&self.root)
    }
}

impl Drop for Scratch {
    fn drop(&mut self) {
        let _ = std::fs::remove_dir_all(&self.root);
    }
}

#[tokio::test]
async fn a_stored_value_reads_back() {
    let scratch = Scratch::new("roundtrip");
    let store = scratch.store();

    assert_eq!(store.load("seen/abc").await.expect("load"), None);
    store
        .store("seen/abc", json!({ "committed": true }))
        .await
        .expect("store");
    assert_eq!(
        store.load("seen/abc").await.expect("load"),
        Some(json!({ "committed": true }))
    );
}

/// A key is author-supplied and an author may be a model, so it must never
/// reach the filesystem as a path.
#[tokio::test]
async fn a_traversing_key_cannot_escape_the_workspace() {
    let scratch = Scratch::new("traversal");
    let store = scratch.store();

    store
        .store("../../../etc/passwd", json!("nope"))
        .await
        .expect("a hostile key is stored like any other");

    // It round-trips as an ordinary key...
    assert_eq!(
        store.load("../../../etc/passwd").await.expect("load"),
        Some(json!("nope"))
    );
    // ...and every file it produced is inside the workspace.
    let written: Vec<_> = std::fs::read_dir(scratch.root.join(STATE_DIR))
        .expect("the state directory exists")
        .filter_map(std::result::Result::ok)
        .collect();
    assert_eq!(written.len(), 1);
    assert!(
        written[0]
            .path()
            .starts_with(scratch.root.join(STATE_DIR)),
        "{:?} escaped the workspace",
        written[0].path()
    );
}

/// The file names itself, so an opaque directory is still diagnosable.
#[tokio::test]
async fn a_stored_file_records_the_key_it_answers_for() {
    let scratch = Scratch::new("selfdescribing");
    scratch
        .store()
        .store("dedup/lemma-5.4", json!(1))
        .await
        .expect("store");

    let entry = std::fs::read_dir(scratch.root.join(STATE_DIR))
        .expect("the state directory exists")
        .filter_map(std::result::Result::ok)
        .next()
        .expect("one file was written");
    let text = std::fs::read_to_string(entry.path()).expect("the file is readable");
    assert!(text.contains("dedup/lemma-5.4"), "{text}");
}

/// A collision must read as a miss. A miss is recoverable; another key's value
/// silently returned in its place is not.
#[tokio::test]
async fn an_entry_written_for_another_key_reads_as_absent() {
    let scratch = Scratch::new("collision");
    let store = scratch.store();
    store.store("real", json!("value")).await.expect("store");

    // Forge the collision the hash makes unlikely but not impossible.
    let path = store.path_for("real");
    std::fs::write(&path, json!({ "key": "other", "value": "value" }).to_string())
        .expect("the entry can be rewritten");

    assert_eq!(store.load("real").await.expect("load"), None);
}

#[tokio::test]
async fn an_unreadable_entry_reads_as_absent_rather_than_failing() {
    let scratch = Scratch::new("garbage");
    let store = scratch.store();
    store.store("key", json!(1)).await.expect("store");
    std::fs::write(store.path_for("key"), "{ not json").expect("the entry can be rewritten");

    // Callers read absence as "not done yet", which is the safe reading of a
    // file this process cannot make sense of.
    assert_eq!(store.load("key").await.expect("load"), None);
}

#[tokio::test]
async fn a_second_write_replaces_the_first() {
    let scratch = Scratch::new("overwrite");
    let store = scratch.store();
    store.store("key", json!(1)).await.expect("store");
    store.store("key", json!(2)).await.expect("store");
    assert_eq!(store.load("key").await.expect("load"), Some(json!(2)));
}
