//! Unit tests for the workspace line search.
#![allow(clippy::expect_used)]

use std::path::PathBuf;
use std::sync::Arc;

use serde_json::json;

use super::{GrepTool, MAX_PER_FILE, searchable};
use crate::agent::{Result, Tool, ToolCall};
use crate::orchestrator::documents::WorkspaceDocuments;

fn workspace(name: &str) -> Result<PathBuf> {
    let path = std::env::temp_dir().join(format!("math-agent-grep-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to create test workspace: {error}"))
    })?;
    path.canonicalize().map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to resolve test workspace: {error}"))
    })
}

/// Runs the tool and returns what a model would see.
async fn run(documents: &WorkspaceDocuments, arguments: serde_json::Value) -> Result<String> {
    let tool: Arc<dyn Tool<()>> = GrepTool::all(documents)
        .into_iter()
        .next()
        .ok_or_else(|| tinyagents::TinyAgentsError::Tool("no grep tool".into()))?;
    let result = tool
        .call(
            &(),
            ToolCall {
                id: "1".to_string(),
                name: tool.name().to_string(),
                arguments,
                invalid: None,
            },
        )
        .await?;
    Ok(result.content)
}

#[tokio::test]
async fn a_match_is_reported_with_its_path_and_line() -> Result<()> {
    let documents = WorkspaceDocuments::new(workspace("hit")?)?;
    documents
        .write_document("research/notes/a.md", "one\ntwo\nthe Chebyshev bias\nfour\n")
        .await?;

    let out = run(&documents, json!({ "pattern": "chebyshev" })).await?;

    assert!(out.contains("research/notes/a.md"), "{out}");
    // The line number is the whole point: it is what a `lines` read needs.
    assert!(out.contains("3: the Chebyshev bias"), "{out}");
    Ok(())
}

#[tokio::test]
async fn the_search_descends_into_subdirectories() -> Result<()> {
    // `research/sources/` is two levels below the root a caller names, so a
    // search that did not descend would answer "nowhere" rather than "not here".
    let documents = WorkspaceDocuments::new(workspace("deep")?)?;
    documents
        .write_document("research/sources/deep/paper.md", "a Gilbreath row\n")
        .await?;

    let out = run(&documents, json!({ "pattern": "gilbreath" })).await?;

    assert!(out.contains("research/sources/deep/paper.md"), "{out}");
    Ok(())
}

#[tokio::test]
async fn the_pattern_is_a_regular_expression() -> Result<()> {
    let documents = WorkspaceDocuments::new(workspace("regex")?)?;
    documents
        .write_document("n.md", "Lemma 4.2 holds\nLemma B is prose\nTheorem 1.1\n")
        .await?;

    let out = run(&documents, json!({ "pattern": r"Lemma \d+\.\d+" })).await?;

    assert!(out.contains("Lemma 4.2"), "{out}");
    assert!(!out.contains("Lemma B"), "{out}");
    Ok(())
}

#[tokio::test]
async fn an_unusable_pattern_says_so_rather_than_matching_nothing() -> Result<()> {
    // Reported as a bad pattern, not as an empty result: "no matches" would
    // send the caller looking for the term somewhere else.
    let documents = WorkspaceDocuments::new(workspace("bad")?)?;
    documents.write_document("n.md", "text\n").await?;

    let error = run(&documents, json!({ "pattern": "(unclosed" }))
        .await
        .expect_err("the pattern does not compile");

    assert!(
        error.to_string().contains("not a usable regular expression"),
        "{error}"
    );
    Ok(())
}

#[tokio::test]
async fn one_file_cannot_take_the_whole_budget() -> Result<()> {
    // A term that is the subject of one document matches on every line of it,
    // and would otherwise hide the six other files that mention it.
    let documents = WorkspaceDocuments::new(workspace("share")?)?;
    documents
        .write_document("loud.md", &"gilbreath\n".repeat(200))
        .await?;
    documents.write_document("quiet.md", "one gilbreath line\n").await?;

    let out = run(&documents, json!({ "pattern": "gilbreath" })).await?;

    assert!(out.contains("quiet.md"), "{out}");
    assert_eq!(out.matches("loud.md").count(), 1, "{out}");
    // Every reported hit is a line of the form `  <n>: <text>`, so counting
    // those counts hits rather than mentions of the pattern in the prose.
    let hits = out
        .lines()
        .filter(|line| {
            let trimmed = line.trim_start();
            line.starts_with(' ')
                && trimmed.split_once(": ").is_some_and(|(number, _)| {
                    !number.is_empty() && number.chars().all(|c| c.is_ascii_digit())
                })
        })
        .count();
    assert_eq!(hits, MAX_PER_FILE + 1, "{out}");
    assert!(out.contains("capped"), "{out}");
    Ok(())
}

#[tokio::test]
async fn no_match_says_the_pattern_is_a_regular_expression() -> Result<()> {
    let documents = WorkspaceDocuments::new(workspace("empty")?)?;
    documents.write_document("n.md", "nothing of interest\n").await?;

    let out = run(&documents, json!({ "pattern": "zeta" })).await?;

    assert!(out.contains("no line matches"), "{out}");
    assert!(out.contains("regular expression"), "{out}");
    Ok(())
}

#[tokio::test]
async fn the_search_can_be_narrowed_to_one_folder() -> Result<()> {
    let documents = WorkspaceDocuments::new(workspace("narrow")?)?;
    documents.write_document("research/a.md", "zeta here\n").await?;
    documents.write_document("code/b.md", "zeta there\n").await?;

    let out = run(&documents, json!({ "pattern": "zeta", "path": "code" })).await?;

    assert!(out.contains("code/b.md"), "{out}");
    assert!(!out.contains("research/a.md"), "{out}");
    Ok(())
}

#[test]
fn only_text_this_run_could_have_written_is_scanned() {
    // The workspace accumulates enumeration pools and converted PDFs; scanning
    // them spends the budget proving a column of integers has no prose in it.
    assert!(searchable("research/notes/a.md"));
    assert!(searchable("code/solve.py"));
    assert!(!searchable("raw/paper.pdf"));
    assert!(!searchable("code/out/pool.bin"));
}
