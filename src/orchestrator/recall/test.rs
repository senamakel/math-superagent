//! Unit tests for workspace similarity search.
#![allow(clippy::expect_used)]

use crate::agent::{Result, ToolCall};

fn workspace(name: &str) -> std::path::PathBuf {
    let path =
        std::env::temp_dir().join(format!("math-agent-recall-{name}-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).expect("temporary workspace is creatable");
    path.canonicalize().expect("workspace resolves")
}

async fn search(root: &std::path::Path, query: &str) -> Result<String> {
    let tool = super::RecallWorkspaceTool::registered(root.to_path_buf());
    Ok(tool
        .call(
            &(),
            ToolCall {
                id: "call-1".into(),
                name: "search_workspace".into(),
                invalid: None,
                arguments: serde_json::json!({ "query": query }),
            },
        )
        .await?
        .content)
}

#[tokio::test]
async fn a_lesson_recorded_in_reflections_is_reachable_without_its_path() -> Result<()> {
    // The reason this tool exists: the inventor re-proposed approaches whose
    // failure was already written down, because nothing let it look.
    let root = workspace("reflections");
    std::fs::create_dir_all(root.join("reflections")).expect("folder is creatable");
    std::fs::write(
        root.join("reflections/1786_01_learnings.md"),
        "Attempt 3 judged unsolved. The sieve over primitive quaternion frames \
         does not terminate for even edge lengths and was abandoned.",
    )
    .expect("reflection is writable");
    std::fs::write(root.join("solution.py"), "print('unrelated arithmetic')")
        .expect("file is writable");

    let found = search(&root, "primitive quaternion frames even edge lengths").await?;
    assert!(
        found.contains("reflections/1786_01_learnings.md"),
        "got: {found}"
    );
    let _ = std::fs::remove_dir_all(&root);
    Ok(())
}

#[tokio::test]
async fn runtime_bookkeeping_stays_unreachable_through_search() -> Result<()> {
    // The event log is kept out of an agent's context deliberately. A search
    // that could reach it would be a way around that rule, not a feature.
    let root = workspace("hidden");
    std::fs::write(
        root.join("trace.jsonl"),
        "{\"event\":\"quaternion frames sieve terminated\"}",
    )
    .expect("trace is writable");
    std::fs::create_dir_all(root.join("research/raw")).expect("folder is creatable");
    std::fs::write(
        root.join("research/raw/original.md"),
        "quaternion frames sieve terminated",
    )
    .expect("raw is writable");

    let found = search(&root, "quaternion frames sieve terminated").await?;
    assert!(!found.contains("trace.jsonl"), "got: {found}");
    assert!(!found.contains("raw/"), "got: {found}");
    let _ = std::fs::remove_dir_all(&root);
    Ok(())
}

#[tokio::test]
async fn a_query_matching_nothing_says_so_rather_than_returning_a_bare_list() -> Result<()> {
    let root = workspace("empty");
    std::fs::write(root.join("notes.md"), "unrelated").expect("file is writable");
    let found = search(&root, "zzzz").await?;
    assert!(found.contains("nothing in this workspace"), "got: {found}");
    let _ = std::fs::remove_dir_all(&root);
    Ok(())
}
