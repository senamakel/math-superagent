//! Unit tests for workspace document storage and search.

use std::path::PathBuf;

use super::WorkspaceDocuments;
use crate::agent::Result;

fn workspace(name: &str) -> Result<PathBuf> {
    let path = std::env::temp_dir().join(format!("math-agent-documents-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to create test workspace: {error}"))
    })?;
    path.canonicalize().map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to resolve test workspace: {error}"))
    })
}

#[tokio::test]
async fn stores_edits_indexes_and_searches_documents() -> Result<()> {
    let path = workspace("search")?;
    let documents = WorkspaceDocuments::new(path.clone())?;
    documents
        .write(
            "notes/proof.md",
            "A bijection proves the finite sets are equinumerous.",
        )
        .await?;
    let original = documents.read("notes/proof.md").await?;
    documents
        .write("notes/proof.md", &original.replace("finite", "two finite"))
        .await?;
    documents.index("notes/proof.md").await?;

    let results = documents.search("bijection finite").await?;
    assert_eq!(results.len(), 1);
    assert_eq!(results[0]["path"], "notes/proof.md");
    assert!(
        results[0]["snippet"]
            .as_str()
            .is_some_and(|text| text.contains("two finite"))
    );
    let _ = std::fs::remove_dir_all(path);
    Ok(())
}

#[tokio::test]
async fn rejects_paths_outside_the_workspace() -> Result<()> {
    let path = workspace("boundary")?;
    let documents = WorkspaceDocuments::new(path.clone())?;
    assert!(documents.write("../outside.md", "no").await.is_err());
    let _ = std::fs::remove_dir_all(path);
    Ok(())
}

#[test]
fn html_and_pdf_are_converted_on_read_but_notes_are_not() {
    use super::needs_conversion;
    // The Euler wrapper curls `problem.html` straight in; it never passes
    // through download_document, so conversion has to happen on read too.
    assert!(needs_conversion("problem.html", b"<p>x</p>"));
    assert!(needs_conversion("reference/paper.PDF", b"anything"));
    assert!(needs_conversion("saved-without-extension", b"%PDF-1.4 ..."));
    // Working notes and source must come back byte-for-byte.
    assert!(!needs_conversion("memory.md", b"# Working memory"));
    assert!(!needs_conversion("solution.py", b"print(1)"));
    assert!(!needs_conversion("results.tsv", b"1\t2"));
    // A note quoting HTML is still a note.
    assert!(!needs_conversion("notes.md", b"see <html> tags"));
}

#[test]
fn downloads_are_filed_under_the_research_folder() {
    use super::research_path;
    // Enforced in code, not asked for in a prompt: a prompt instruction holds
    // only until a model decides otherwise.
    assert_eq!(research_path("pell.md"), "research/pell.md");
    assert_eq!(
        research_path("papers/lagrange.md"),
        "research/papers/lagrange.md"
    );
    // Already in place: left exactly as given.
    assert_eq!(research_path("research/pell.md"), "research/pell.md");
    // Common spellings must not produce research/workspace/...
    assert_eq!(research_path("/workspace/pell.md"), "research/pell.md");
    assert_eq!(research_path("./pell.md"), "research/pell.md");
    assert_eq!(research_path("/pell.md"), "research/pell.md");
    // A blank path still lands somewhere sensible rather than at the root.
    assert_eq!(research_path("   "), "research/document.md");
}

#[test]
fn raw_originals_mirror_the_research_layout_and_stay_hidden() {
    use super::{HIDDEN_ENTRIES, RAW_DIR, raw_path};
    // Conversion is lossy; the original is what distinguishes a bad source
    // from a bad converter when a document reads oddly.
    assert_eq!(raw_path("research/pell.md"), "raw/pell.md");
    assert_eq!(
        raw_path("research/papers/lagrange.md"),
        "raw/papers/lagrange.md"
    );
    // Never surfaced to an agent: it would only compete for context.
    assert!(HIDDEN_ENTRIES.contains(&RAW_DIR));
}
