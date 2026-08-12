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
    assert!(!needs_conversion("SCRATCHPAD.md", b"# Working notes"));
    assert!(!needs_conversion("solution.py", b"print(1)"));
    assert!(!needs_conversion("results.tsv", b"1\t2"));
    // A note quoting HTML is still a note.
    assert!(!needs_conversion("notes.md", b"see <html> tags"));
}

#[test]
fn downloads_are_filed_under_the_research_folder() {
    use super::{full_text_path, research_path};
    let root = std::path::Path::new("/nonexistent-workspace");
    // Enforced in code, not asked for in a prompt: a prompt instruction holds
    // only until a model decides otherwise.
    assert_eq!(research_path(root, "pell.md"), "research/summaries/pell.md");
    assert_eq!(
        research_path(root, "papers/lagrange.md"),
        "research/summaries/lagrange.md"
    );
    assert_eq!(
        research_path(root, "research/pell.md"),
        "research/summaries/pell.md"
    );
    assert_eq!(
        research_path(root, "research/summaries/pell.md"),
        "research/summaries/pell.md"
    );
    // Common spellings must not produce research/workspace/...
    assert_eq!(
        research_path(root, "/workspace/pell.md"),
        "research/summaries/pell.md"
    );
    assert_eq!(
        research_path(root, "./pell.md"),
        "research/summaries/pell.md"
    );
    assert_eq!(
        research_path(root, "/pell.md"),
        "research/summaries/pell.md"
    );
    // A blank path still lands somewhere sensible rather than at the root.
    assert_eq!(research_path(root, "   "), "research/summaries/document.md");
    // Naming the full text names the wrong half of the pair: the digest is
    // what a download produces at level 1.
    assert_eq!(
        research_path(root, "confusioninterval.full.md"),
        "research/summaries/confusioninterval.md"
    );
    // A name that already carries the marker does not earn a second one.
    assert_eq!(
        full_text_path(root, "research/sources/paper.full.md"),
        "research/sources/paper.full.md"
    );
    // The untouched original sits one level below the note that digests it.
    assert_eq!(
        full_text_path(root, "research/summaries/pell.md"),
        "research/sources/pell.full.md"
    );
}

#[tokio::test]
async fn a_note_requested_from_the_wrong_research_folder_is_pointed_at_its_real_one() -> Result<()>
{
    let root = std::env::temp_dir().join(format!("math-agent-batch-hint-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/summaries")).expect("workspace is creatable");
    let root = root.canonicalize().expect("workspace resolves");
    std::fs::write(root.join("research/summaries/paper.md"), "note").expect("note is writable");
    let documents = WorkspaceDocuments::new(root.clone())?;

    let error = documents
        .read_document("research/sources/paper.md")
        .await
        .expect_err("the guessed batch does not hold it");
    let message = error.to_string();
    assert!(message.contains("research/summaries/paper.md"), "{message}");

    // A name that is genuinely absent still gets the folder listing rather
    // than a confident wrong answer.
    let missing = documents
        .read_document("research/sources/absent.md")
        .await
        .expect_err("no such note anywhere");
    assert!(!missing.to_string().contains("summaries/absent.md"));
    let _ = std::fs::remove_dir_all(&root);
    Ok(())
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
        // The console stream, the same replay under a different name. A live
        // `context_curator` read 37,609 bytes of one into a model call.
        "config/start.log",
        "start.log",
        "/workspace/config/start.log",
    ] {
        assert!(
            ensure_visible(hidden).is_err(),
            "{hidden} must not be readable"
        );
    }

    // The run's own working files stay reachable.
    for visible in [
        "SCRATCHPAD.md",
        "solution.py",
        "research/pell.md",
        "research/summaries/pell.md",
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
    std::fs::create_dir_all(
        path.join(super::INDEX_PATH)
            .parent()
            .expect("index has a parent"),
    )
    .expect("the config folder is creatable");
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
    std::fs::write(root.join("GOAL.md"), "objective").expect("file is writable");
    std::fs::write(root.join("SCRATCHPAD.md"), "working").expect("file is writable");
    std::fs::write(root.join("trace.jsonl"), "{}").expect("trace is writable");

    let documents = WorkspaceDocuments::new(root.clone())?;
    let error = documents
        .read("solution.md")
        .await
        .expect_err("a missing document must fail");
    let message = error.to_string();
    assert!(message.contains("GOAL.md"), "got: {message}");
    assert!(message.contains("SCRATCHPAD.md"), "got: {message}");
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

/// Serves one response on loopback and returns the URL to fetch it from.
///
/// A real socket rather than a mocked client, because the thing under test is
/// what the HTTP layer does with a body that arrives in pieces — a mock that
/// hands over a `Vec` has already done the buffering the bound exists to
/// prevent. Nothing leaves the machine, so this stays a deterministic unit test
/// rather than the live network tests that belong outside the suite.
async fn serving(body: Vec<u8>, chunked: bool) -> Result<String> {
    let listener = tokio::net::TcpListener::bind("127.0.0.1:0")
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to bind test listener: {error}"))
        })?;
    let address = listener.local_addr().map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to read test listener address: {error}"))
    })?;
    tokio::spawn(async move {
        let Ok((mut socket, _)) = listener.accept().await else {
            return;
        };
        use tokio::io::AsyncWriteExt as _;
        let header = if chunked {
            // No `Content-Length`, so the declared-length check has nothing to
            // look at and the streaming bound is the only one left.
            "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nTransfer-Encoding: chunked\r\n\r\n"
                .to_string()
        } else {
            format!(
                "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {}\r\n\r\n",
                body.len()
            )
        };
        if socket.write_all(header.as_bytes()).await.is_err() {
            return;
        }
        if chunked {
            for piece in body.chunks(16 * 1024) {
                let framed = format!("{:x}\r\n", piece.len());
                if socket.write_all(framed.as_bytes()).await.is_err()
                    || socket.write_all(piece).await.is_err()
                    || socket.write_all(b"\r\n").await.is_err()
                {
                    return;
                }
            }
            let _ = socket.write_all(b"0\r\n\r\n").await;
        } else {
            let _ = socket.write_all(&body).await;
        }
        let _ = socket.flush().await;
    });
    Ok(format!("http://{address}/source.txt"))
}

#[tokio::test]
async fn a_document_within_the_limit_downloads_whole() -> Result<()> {
    let path = workspace("download-small")?;
    let documents = WorkspaceDocuments::new(path)?;
    let url = serving(b"Theorem 1. The bound is respected.\n".to_vec(), true).await?;
    let (bytes, content_type) = super::DocumentTool {
        kind: super::DocumentToolKind::Download,
        documents,
    }
    .fetch(&url)
    .await?;
    assert_eq!(bytes, b"Theorem 1. The bound is respected.\n");
    assert_eq!(content_type.as_deref(), Some("text/plain"));
    Ok(())
}

#[tokio::test]
async fn an_oversized_chunked_body_is_refused_without_being_buffered() -> Result<()> {
    // A chunked response carries no `Content-Length`, so the pre-check has
    // nothing to read and the whole body used to reach memory before its size
    // could be compared. The container has a hard `mem_limit` and an OOM kill
    // loses everything in flight, so the bound has to apply as it arrives.
    let path = workspace("download-oversized")?;
    let documents = WorkspaceDocuments::new(path)?;
    let url = serving(vec![b'x'; super::MAX_DOCUMENT_BYTES + 64 * 1024], true).await?;
    let refused = super::DocumentTool {
        kind: super::DocumentToolKind::Download,
        documents,
    }
    .fetch(&url)
    .await;
    let message = refused
        .err()
        .map(|error| error.to_string())
        .unwrap_or_default();
    assert!(
        message.contains("exceeds") && message.contains("abandoned"),
        "the refusal must say the transfer stopped: {message}"
    );
    Ok(())
}

#[tokio::test]
async fn a_declared_length_over_the_limit_is_refused_before_the_body_arrives() -> Result<()> {
    let path = workspace("download-declared")?;
    let documents = WorkspaceDocuments::new(path)?;
    let url = serving(vec![b'x'; super::MAX_DOCUMENT_BYTES + 1], false).await?;
    let refused = super::DocumentTool {
        kind: super::DocumentToolKind::Download,
        documents,
    }
    .fetch(&url)
    .await;
    assert!(refused.is_err(), "an honest oversized header is enough");
    Ok(())
}

#[tokio::test]
async fn a_non_http_scheme_is_refused() -> Result<()> {
    let path = workspace("download-scheme")?;
    let documents = WorkspaceDocuments::new(path)?;
    let refused = super::DocumentTool {
        kind: super::DocumentToolKind::Download,
        documents,
    }
    .fetch("file:///etc/passwd")
    .await;
    assert!(refused.is_err(), "only HTTP and HTTPS are fetchable");
    Ok(())
}
