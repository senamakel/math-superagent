//! Unit tests for workspace document storage and search.
#![allow(clippy::expect_used)]

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
    use super::{full_text_path, research_path};
    // Enforced in code, not asked for in a prompt: a prompt instruction holds
    // only until a model decides otherwise.
    assert_eq!(research_path("pell.md"), "research/L1/pell.md");
    // A source arriving from outside is a level-1 note whatever folder the
    // caller invented for it.
    assert_eq!(
        research_path("papers/lagrange.md"),
        "research/L1/lagrange.md"
    );
    assert_eq!(research_path("research/pell.md"), "research/L1/pell.md");
    // A path that already names a level knows where it belongs.
    assert_eq!(research_path("research/L2/pell.md"), "research/L2/pell.md");
    // Common spellings must not produce research/workspace/...
    assert_eq!(research_path("/workspace/pell.md"), "research/L1/pell.md");
    assert_eq!(research_path("./pell.md"), "research/L1/pell.md");
    assert_eq!(research_path("/pell.md"), "research/L1/pell.md");
    // A blank path still lands somewhere sensible rather than at the root.
    assert_eq!(research_path("   "), "research/L1/document.md");
    // The untouched original sits one level below the note that digests it.
    assert_eq!(
        full_text_path("research/L1/pell.md"),
        "research/L0/pell.full.md"
    );
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

#[test]
fn runtime_bookkeeping_cannot_be_read_into_an_agents_context() {
    use super::ensure_visible;

    // A reflection run read `/workspace/trace.jsonl` — 1.1 MB of the run's own
    // event log — into one 339,652-token model call. Hiding these from
    // `list_workspace` was not enough: an agent can name a path the listing
    // never offered it.
    for hidden in [
        "trace.jsonl",
        "/workspace/trace.jsonl",
        "./trace.jsonl",
        ".document-index.json",
        "raw/papers/lagrange.md",
        ".workspace-history/HEAD",
    ] {
        assert!(
            ensure_visible(hidden).is_err(),
            "{hidden} must not be readable"
        );
    }

    // The run's own working files stay reachable.
    for visible in [
        "memory.md",
        "solution.py",
        "research/pell.md",
        "reflections/1_01_learnings.md",
    ] {
        assert!(
            ensure_visible(visible).is_ok(),
            "{visible} must be readable"
        );
    }
}

#[test]
fn a_converted_document_is_named_for_what_it_now_contains() {
    use super::{markdown_path, raw_path};

    // Everything under research/ has been through `to_markdown`, so a stored
    // `paper.pdf` holds Markdown and the suffix misleads every later reader.
    assert_eq!(
        markdown_path("research/recounting_rationals.pdf"),
        "research/recounting_rationals.md"
    );
    assert_eq!(
        markdown_path("research/oeis_A002487.html"),
        "research/oeis_A002487.md"
    );
    // Already Markdown, or no extension at all.
    assert_eq!(markdown_path("research/pell.md"), "research/pell.md");
    assert_eq!(markdown_path("research/PELL.MD"), "research/PELL.MD");
    assert_eq!(markdown_path("research/notes"), "research/notes.md");
    // A dot that is not a suffix must not eat part of the name.
    assert_eq!(markdown_path("research/v1.2/zeta"), "research/v1.2/zeta.md");

    // The archive keeps the requested name, so the original bytes keep the
    // extension that actually describes them.
    assert_eq!(
        raw_path("research/recounting_rationals.pdf"),
        "raw/recounting_rationals.pdf"
    );
}

#[test]
fn a_downloaded_document_is_excerpted_where_agents_read_it() {
    use super::{RESEARCH_EXCERPT_CHARS, research_excerpt};

    // One real downloaded page converted to 91,190 characters — roughly 23,000
    // tokens. Three of those fill a specialist's context before it has done
    // any work, so only a bounded stand-in is filed under research/.
    let full = (0..4_000)
        .map(|line| format!("line {line} of a long converted paper"))
        .collect::<Vec<_>>()
        .join("\n");
    assert!(full.chars().count() > RESEARCH_EXCERPT_CHARS);

    let excerpt = research_excerpt(&full, "raw/paper.md");

    assert!(excerpt.chars().count() < full.chars().count() / 4);
    assert!(
        excerpt.contains("raw/paper.md"),
        "it must say where the rest is"
    );
    assert!(
        excerpt.contains("1000 tokens"),
        "and what to replace it with"
    );
    assert!(excerpt.contains("line 0 of a long"), "the opening survives");
    // Cut at a line boundary rather than mid-sentence.
    assert!(!excerpt.contains("*[excerpt ends; 0 characters"));
}

#[test]
fn a_short_document_is_stored_whole_without_a_truncation_notice() {
    use super::research_excerpt;

    let full = "# Pell's equation\n\nThe fundamental solution is minimal.\n";
    assert_eq!(research_excerpt(full, "raw/pell.md"), full);
}

#[tokio::test]
async fn concurrent_indexing_keeps_every_entry() -> Result<()> {
    let path = workspace("index-race")?;
    let documents = WorkspaceDocuments::new(path.clone())?;
    let names: Vec<String> = (0..12).map(|n| format!("notes/source{n}.md")).collect();
    for name in &names {
        documents
            .write(name, "a lattice cube has eight vertices")
            .await?;
    }

    // The shape that corrupted a live run: one turn's worth of index calls,
    // all in flight at once against the same file.
    let mut tasks = tokio::task::JoinSet::new();
    for name in names.clone() {
        let documents = documents.clone();
        tasks.spawn(async move { documents.index(&name).await });
    }
    while let Some(joined) = tasks.join_next().await {
        joined.expect("index task panicked")?;
    }

    let indexed = documents.indexed_paths().await?;
    assert_eq!(indexed.len(), names.len(), "lost entries: {indexed:?}");
    // Readable as JSON, not merely non-empty: the failure being guarded
    // against left a file that parsed as far as column 2 of line 3.
    let raw = std::fs::read(path.join(super::INDEX_PATH)).expect("index is on disk");
    let parsed: Vec<String> = serde_json::from_slice(&raw).expect("index is valid JSON");
    assert_eq!(parsed.len(), names.len());
    let _ = std::fs::remove_dir_all(path);
    Ok(())
}

#[tokio::test]
async fn a_corrupt_index_rebuilds_instead_of_failing_forever() -> Result<()> {
    let path = workspace("index-corrupt")?;
    let documents = WorkspaceDocuments::new(path.clone())?;
    documents.write("notes/proof.md", "a bijection").await?;
    // Byte-for-byte the wreckage Euler 579 produced.
    std::fs::write(
        path.join(super::INDEX_PATH),
        "[\n  \"research/ehrhart_cubes.pdf\"\n]f\"\n]",
    )
    .expect("seed a corrupt index");

    // Indexing must still succeed; the model cannot repair bookkeeping it
    // never sees.
    documents.index("notes/proof.md").await?;
    let indexed = documents.indexed_paths().await?;
    assert_eq!(indexed, vec!["notes/proof.md".to_string()]);
    let _ = std::fs::remove_dir_all(path);
    Ok(())
}

#[tokio::test]
async fn a_missing_document_names_what_the_folder_actually_holds() -> Result<()> {
    // A model that guessed `research/DIGEST.md` otherwise learns only that it
    // guessed wrong, and guesses again — a full model turn per attempt.
    let root = workspace("missing-document")?;
    let research = root.join("research");
    std::fs::create_dir_all(&research).expect("research folder is creatable");
    std::fs::write(research.join("INDEX.md"), "index").expect("index is writable");
    std::fs::write(research.join("kiss_kutas.md"), "source").expect("source is writable");
    std::fs::create_dir_all(research.join("raw")).expect("raw folder is creatable");

    let documents = WorkspaceDocuments::new(root.clone())?;
    let error = documents
        .read("research/DIGEST.md")
        .await
        .expect_err("a missing document must fail");
    let message = error.to_string();
    assert!(message.contains("INDEX.md"), "got: {message}");
    assert!(message.contains("kiss_kutas.md"), "got: {message}");
    assert!(
        !message.contains("raw/"),
        "the raw folder is hidden from agents and must stay hidden: {message}"
    );
    Ok(())
}

#[tokio::test]
async fn a_missing_file_at_the_workspace_root_names_its_neighbours() -> Result<()> {
    // The root is where an agent guesses most — `solution.md` was the first
    // thing a live run reached for — and an empty parent is what the file path
    // checker refuses, so this is the case the helper must not miss.
    let root = workspace("missing-at-root")?;
    std::fs::write(root.join("memory.md"), "beliefs").expect("file is writable");
    std::fs::write(root.join("scratchpad.md"), "working").expect("file is writable");
    std::fs::write(root.join("trace.jsonl"), "{}").expect("trace is writable");

    let documents = WorkspaceDocuments::new(root.clone())?;
    let error = documents
        .read("solution.md")
        .await
        .expect_err("a missing document must fail");
    let message = error.to_string();
    assert!(message.contains("memory.md"), "got: {message}");
    assert!(message.contains("scratchpad.md"), "got: {message}");
    assert!(
        !message.contains("trace.jsonl"),
        "the event log stays hidden: {message}"
    );
    Ok(())
}

#[tokio::test]
async fn listing_a_folder_that_is_not_there_names_the_ones_that_are() -> Result<()> {
    let root = workspace("missing-folder")?;
    let research = root.join("research");
    std::fs::create_dir_all(&research).expect("research folder is creatable");
    std::fs::write(research.join("INDEX.md"), "index").expect("index is writable");

    let documents = WorkspaceDocuments::new(root.clone())?;
    let error = documents
        .list("research/raw", 2)
        .await
        .expect_err("a missing directory must fail");
    assert!(error.to_string().contains("INDEX.md"), "got: {error}");
    Ok(())
}
