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
///
/// `declare_length` chooses which of the two bounds is under test. Without it
/// the body is delimited by the close, which is what a real chunked transfer
/// looks like to the caller: no `Content-Length` for the pre-check to read, so
/// the streaming bound is the only one left.
async fn serving(body: Vec<u8>, declare_length: bool) -> Result<String> {
    let listener = tokio::net::TcpListener::bind("127.0.0.1:0")
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to bind test listener: {error}"))
        })?;
    let address = listener.local_addr().map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to read test listener address: {error}"))
    })?;
    tokio::spawn(async move {
        use tokio::io::{AsyncReadExt as _, AsyncWriteExt as _};
        let Ok((mut socket, _)) = listener.accept().await else {
            return;
        };
        // Read the request before answering it. Closing a socket that still
        // holds unread bytes makes the kernel send RST rather than FIN, and an
        // RST discards whatever the peer has not yet read — so a small response
        // arrived intact and a large one came back as a decode error, which
        // looks exactly like the bound under test failing.
        let mut request = [0_u8; 2048];
        let _ = socket.read(&mut request).await;
        let header = if declare_length {
            format!(
                "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {}\r\n\
                 Connection: close\r\n\r\n",
                body.len()
            )
        } else {
            "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nConnection: close\r\n\r\n".to_string()
        };
        if socket.write_all(header.as_bytes()).await.is_err() {
            return;
        }
        // In pieces, so the client genuinely reads a stream rather than one
        // buffer handed over whole.
        for piece in body.chunks(16 * 1024) {
            if socket.write_all(piece).await.is_err() {
                return;
            }
        }
        let _ = socket.flush().await;
        let _ = socket.shutdown().await;
    });
    Ok(format!("http://{address}/source.txt"))
}

#[tokio::test]
async fn a_document_within_the_limit_downloads_whole() -> Result<()> {
    let path = workspace("download-small")?;
    let documents = WorkspaceDocuments::new(path)?;
    let url = serving(b"Theorem 1. The bound is respected.\n".to_vec(), false).await?;
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
async fn an_undeclared_oversized_body_is_refused_without_being_buffered() -> Result<()> {
    // Without a `Content-Length` the pre-check has nothing to read, so the
    // whole body used to reach memory before its size could be compared. The
    // container has a hard `mem_limit` and an OOM kill loses everything in
    // flight, so the bound has to apply as the bytes arrive.
    let path = workspace("download-oversized")?;
    let documents = WorkspaceDocuments::new(path)?;
    let url = serving(vec![b'x'; super::MAX_DOCUMENT_BYTES + 64 * 1024], false).await?;
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
    let url = serving(vec![b'x'; super::MAX_DOCUMENT_BYTES + 1], true).await?;
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

/// The screen has to reach `download_document`, and nothing else here.
///
/// `download_document` fetches an arbitrary URL, it is granted to almost every
/// role, and — unlike the search tools — it is **not** withheld by
/// `MATH_AGENT_RESEARCH`. So on a calibration run it is the second way onto the
/// web and the one most easily left unscreened.
///
/// Asserted behaviourally rather than by inspecting the wrapper, because what
/// matters is that a denied host is actually refused, not that a particular
/// type is present. The refusal happens before any request, so this test makes
/// no network call.
#[tokio::test]
async fn the_screen_reaches_the_download_tool() -> Result<()> {
    let path = workspace("screened-download")?;
    std::fs::write(path.join("screen.json"), SCREEN_POLICY)
        .expect("the fixture policy must be writable");
    let screen = crate::orchestrator::screen::Screen::load(&path.join("screen.json"), &path, None)?;

    let documents = WorkspaceDocuments::new(path.clone())?.with_screen(Some(screen));
    let tools = documents.tools();
    let download = tools
        .iter()
        .find(|tool| tool.name() == "download_document")
        .expect("the download tool must be registered");

    let refused = download
        .call(
            &(),
            crate::agent::ToolCall {
                id: "c1".to_string(),
                name: "download_document".to_string(),
                arguments: serde_json::json!({"url": "https://blocked.example/paper.pdf"}),
                invalid: None,
            },
        )
        .await?;
    assert!(
        refused.content.contains("withheld by the run's evidence policy"),
        "a denied host must be refused before the request, got: {}",
        refused.content
    );

    // The file tools read and write what the run itself produced, so screening
    // them would put the screen in front of the run reading its own notes.
    let write = tools
        .iter()
        .find(|tool| tool.name() == "write_document")
        .expect("the write tool must be registered");
    let stored = write
        .call(
            &(),
            crate::agent::ToolCall {
                id: "c2".to_string(),
                name: "write_document".to_string(),
                arguments: serde_json::json!({
                    "path": "notes.md",
                    "content": "https://blocked.example/paper.pdf"
                }),
                invalid: None,
            },
        )
        .await?;
    assert!(
        stored.error.is_none(),
        "writing a note is not screened, got: {stored:?}"
    );
    Ok(())
}

/// A compiled policy denying one host, in the shape `scripts/compile-screen`
/// emits. `9be49db4…` is that script's digest of the normalised host
/// `blocked example` under the salt below; `block` carries one unreachable
/// digest because a policy withholding nothing is rejected as a compilation
/// mistake.
const SCREEN_POLICY: &str = concat!(
    r#"{"slug":"fixture","salt":"0123456789abcdef0","max_ngram":4,"#,
    r#""block":["0000000000000000000000000000dead"],"#,
    r#""deny_hosts":["9be49db4c8786f44f484383e88a15b23"]}"#
);
/// Concurrent writes to different paths all survive.
///
/// The shape several schools on one workspace make ordinary: a dozen roles
/// writing at once, none of them to the same file. Nothing here contends, so
/// nothing may be lost — a serialisation that dropped a write would be worse
/// than the race it replaced.
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn concurrent_writes_to_different_paths_all_survive() -> Result<()> {
    let path = workspace("write-race")?;
    let documents = WorkspaceDocuments::new(path.clone())?;

    let mut tasks = tokio::task::JoinSet::new();
    for n in 0..16 {
        let documents = documents.clone();
        tasks.spawn(async move {
            documents
                .write_document(&format!("notes/finding{n}.md"), &format!("claim number {n}"))
                .await
        });
    }
    while let Some(joined) = tasks.join_next().await {
        joined.expect("a write task must not panic")?;
    }

    for n in 0..16 {
        let content = documents
            .read_document(&format!("notes/finding{n}.md"))
            .await?;
        assert_eq!(content, format!("claim number {n}"), "write {n} was lost");
    }
    let _ = std::fs::remove_dir_all(path);
    Ok(())
}

/// A reader sees the old bytes or the new ones, never half of each.
///
/// `tokio::fs::write` truncates and then writes, which is two operations: a
/// reader between them sees an empty or partial file. That is not theoretical
/// here — three concurrent writes to the document index left four stranded
/// bytes on the end and invalid JSON behind them on Euler 579. The two
/// contents differ in length deliberately, so a torn read is a value equal to
/// neither rather than one that happens to look plausible.
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn a_reader_never_sees_a_half_written_document() -> Result<()> {
    let root = workspace("write-tearing")?;
    let documents = WorkspaceDocuments::new(root.clone())?;
    let old = "old".repeat(4_000);
    let new = "new-and-rather-longer".repeat(4_000);
    documents.write_document("notes/derivation.md", &old).await?;

    let file = root.join("notes/derivation.md");
    let stop = std::sync::Arc::new(std::sync::atomic::AtomicBool::new(false));
    let reader = {
        let file = file.clone();
        let stop = std::sync::Arc::clone(&stop);
        let (old, new) = (old.clone(), new.clone());
        tokio::spawn(async move {
            let mut reads = 0usize;
            while !stop.load(std::sync::atomic::Ordering::Relaxed) {
                // The destination is replaced by a rename rather than
                // truncated, so it is never absent and never empty.
                let seen = tokio::fs::read_to_string(&file)
                    .await
                    .expect("a document replaced by rename is readable throughout");
                assert!(
                    seen == old || seen == new,
                    "a reader observed {} bytes, which is neither content whole",
                    seen.len()
                );
                reads += 1;
                tokio::task::yield_now().await;
            }
            reads
        })
    };

    for turn in 0..60 {
        let content = if turn % 2 == 0 { &new } else { &old };
        documents.write_document("notes/derivation.md", content).await?;
        tokio::task::yield_now().await;
    }
    stop.store(true, std::sync::atomic::Ordering::Relaxed);
    let reads = reader.await.expect("the reader must not panic");
    assert!(reads > 0, "the reader never got a look in");

    let _ = std::fs::remove_dir_all(root);
    Ok(())
}

/// Concurrent note writes all reach the ledger derived from them.
///
/// A note write does not only write a note: it re-derives up to six ledgers,
/// each by walking the notes on disk and rewriting a whole file. Two of those
/// cascades interleaved leave a ledger rendered from one write and missing the
/// other — and a derived file that disagrees with its sources is worse than no
/// derived file, because the next reader trusts the row instead of opening the
/// note. Driven through the tool rather than through the store, because the
/// lock is taken at the tool-call boundary and this is what that boundary is
/// for.
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn concurrent_note_writes_all_reach_the_derived_ledger() -> Result<()> {
    let root = workspace("ledger-race")?;
    let documents = WorkspaceDocuments::new(root.clone())?;
    let tools = documents.tools();
    let write = tools
        .iter()
        .find(|tool| tool.name() == "write_document")
        .cloned()
        .expect("write_document is registered");

    // Written in rounds rather than as one burst. What is lost is one
    // re-derivation's rendering, overwritten by another that read the notes
    // before it existed, and whether that lands on the *last* write of a burst
    // is chance. Several rounds, each checked, turn a race that shows itself
    // occasionally into one that shows itself.
    // Fifty notes in total, under the sixty rows the rendered ledger carries,
    // so a missing row is a lost write rather than the cap doing its job.
    let (rounds, per_round) = (5, 10);
    let mut expected: Vec<String> = Vec::new();
    for round in 0..rounds {
        let mut tasks = tokio::task::JoinSet::new();
        for n in 0..per_round {
            // Zero-padded, so no identifier is a prefix of another and a
            // `contains` cannot pass on the strength of a longer id.
            let id = format!("finding-{round:02}-{n:03}");
            expected.push(id.clone());
            let write = std::sync::Arc::clone(&write);
            tasks.spawn(async move {
                write
                    .call(
                        &(),
                        crate::agent::ToolCall {
                            id: format!("call-{id}"),
                            name: "write_document".into(),
                            invalid: None,
                            arguments: serde_json::json!({
                                "path": format!("research/L1.0/{id}.md"),
                                // Padded deliberately: the window between a
                                // re-derivation reading the notes off disk and
                                // writing what it rendered from them is
                                // proportional to how much there is to read.
                                "content": format!(
                                    "# {id}\n\n```claim\nid: {id}\nstatement: This bound is \
                                     attained.\nholds-here: yes\nstatus: proved\n```\n\n{}",
                                    "Supporting prose, at the length a real note runs to. "
                                        .repeat(400)
                                ),
                            }),
                        },
                    )
                    .await
            });
        }
        while let Some(joined) = tasks.join_next().await {
            joined.expect("a note write must not panic")?;
        }

        let ledger = documents
            .read_runtime(crate::orchestrator::claims::CLAIMS_PATH)
            .await?;
        for id in &expected {
            assert!(
                ledger.contains(id),
                "round {round} left the ledger without `{id}`; it renders {} rows:\n{ledger}",
                ledger.lines().filter(|line| line.contains("finding-")).count()
            );
        }
    }
    let _ = std::fs::remove_dir_all(root);
    Ok(())
}

/// Calls `read_document` and returns what the model would see.
async fn read_through_tool(
    documents: &WorkspaceDocuments,
    arguments: serde_json::Value,
) -> Result<String> {
    let tools = documents.tools();
    let read = tools
        .iter()
        .find(|tool| tool.name() == "read_document")
        .expect("the read tool must be registered");
    let result = read
        .call(
            &(),
            crate::agent::ToolCall {
                id: "r1".to_string(),
                name: "read_document".to_string(),
                arguments,
                invalid: None,
            },
        )
        .await?;
    Ok(result.content)
}

#[tokio::test]
async fn a_small_document_is_returned_byte_for_byte() -> Result<()> {
    // Most of what a run reads is a note it wrote itself. Wrapping those in
    // coordinates would be noise on every read to serve the handful that are
    // large, so the unselected small read is unchanged.
    let documents = WorkspaceDocuments::new(workspace("read-small")?)?;
    let body = "# Note\n\nA short belief.\n";
    documents.write_document("notes/small.md", body).await?;

    let out = read_through_tool(&documents, serde_json::json!({"path": "notes/small.md"})).await?;

    assert_eq!(out, body);
    Ok(())
}

#[tokio::test]
async fn an_unselected_read_of_a_large_document_answers_with_its_outline() -> Result<()> {
    // The control: no single call may put a hundred thousand tokens into a
    // context window by accident. Nothing is hidden — every byte is still
    // reachable one named range at a time.
    let documents = WorkspaceDocuments::new(workspace("read-large")?)?;
    let body = (1..=400).fold(String::new(), |mut body, n| {
        use std::fmt::Write as _;
        let _ = writeln!(body, "## Section {n}\n{}", "prose ".repeat(20));
        body
    });
    documents.write_document("research/sources/big.md", &body).await?;

    let out =
        read_through_tool(&documents, serde_json::json!({"path": "research/sources/big.md"})).await?;

    assert!(out.contains("too large to read whole"), "{out}");
    assert!(out.contains("outline of research/sources/big.md"), "{out}");
    assert!(out.len() < body.len() / 4, "{} bytes", out.len());
    Ok(())
}

#[tokio::test]
async fn a_selected_read_of_a_large_document_returns_that_part_with_coordinates() -> Result<()> {
    let documents = WorkspaceDocuments::new(workspace("read-selected")?)?;
    let body = (1..=400).fold(String::new(), |mut body, n| {
        use std::fmt::Write as _;
        let _ = writeln!(body, "## Section {n}\nbody of {n}");
        body
    });
    documents.write_document("research/sources/big.md", &body).await?;

    let out = read_through_tool(
        &documents,
        serde_json::json!({"path": "research/sources/big.md", "section": "Section 7"}),
    )
    .await?;

    assert!(out.contains("body of 7"), "{out}");
    assert!(!out.contains("body of 8"), "{out}");
    // Coordinates, so the caller can cite it and ask for what comes next.
    assert!(out.contains("lines 13-14"), "{out}");
    Ok(())
}
