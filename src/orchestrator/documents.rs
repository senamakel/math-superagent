//! Bounded tools for workspace documents and a local searchable index.

use std::cmp::Reverse;
use std::fmt::Write as _;
use std::path::PathBuf;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

const INDEX_PATH: &str = ".document-index.json";
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
/// Suffix marking the full converted text beside its summary.
pub(super) const FULL_TEXT_SUFFIX: &str = ".full.md";

/// Characters of a downloaded document kept in the summary file before it has
/// been digested.
///
/// A converted document is not small: one downloaded reference page came to
/// 91,190 characters, roughly 23,000 tokens, and three of them would fill a
/// specialist's context before it had done any work. Filing the whole thing
/// where agents read it means the run pays that cost every time anyone opens
/// it, to re-read prose it has already been through.
///
/// So a download lands as two files side by side: `<name>.md` carries a
/// bounded excerpt that the scholar replaces with a real summary, and
/// `<name>.full.md` carries the whole converted text. Both stay in `research/`
/// where an agent can reach them, because a source whose detail is genuinely
/// needed must be readable without leaving the workspace. What the split buys
/// is that reading the short one is the default and reading the long one is a
/// decision.
///
/// Four thousand characters is about a thousand tokens — enough to carry a
/// paper's abstract and the opening of its first section, which is usually
/// enough to tell whether the full text is worth opening.
const RESEARCH_EXCERPT_CHARS: usize = 4_000;
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
}

impl WorkspaceDocuments {
    pub(super) fn new(workspace: PathBuf) -> Result<Self> {
        // Several reference sites, Wikipedia among them, answer an unidentified
        // client with `403 Forbidden`. Sending a real User-Agent is what their
        // policies ask for and turns a hard failure into a usable source.
        let client = reqwest::Client::builder()
            .timeout(std::time::Duration::from_mins(10))
            .user_agent(concat!(
                "math-agent/",
                env!("CARGO_PKG_VERSION"),
                " (+https://github.com/senamakel/riemann)"
            ))
            .build()
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!(
                    "failed to build document HTTP client: {error}"
                ))
            })?;
        Ok(Self {
            workspace,
            client,
            index_lock: Arc::new(tokio::sync::Mutex::new(())),
        })
    }

    pub(super) fn tools(&self) -> Vec<Arc<dyn Tool<()>>> {
        DocumentToolKind::ALL
            .into_iter()
            .map(|kind| {
                Arc::new(DocumentTool {
                    kind,
                    documents: self.clone(),
                }) as Arc<dyn Tool<()>>
            })
            // Every agent that can create a file can describe it, so the
            // index tools travel with the document tools rather than being
            // granted to a role that then becomes the only one able to keep
            // the index honest.
            .chain(super::folder_index::FolderIndexTool::all(self))
            .collect()
    }

    fn path(&self, relative: &str) -> Result<PathBuf> {
        super::checked_workspace_path(&self.workspace, relative)
    }

    fn readable_path(&self, relative: &str) -> Result<PathBuf> {
        ensure_visible(relative)?;
        let path = self.path(relative)?;
        let canonical = path.canonicalize().map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to resolve workspace document `{relative}`: {error}"
            ))
        })?;
        if !canonical.starts_with(&self.workspace) || !canonical.is_file() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "document must resolve to a file inside /workspace".into(),
            ));
        }
        Ok(canonical)
    }

    async fn read(&self, relative: &str) -> Result<String> {
        let path = self.readable_path(relative)?;
        let bytes = tokio::fs::read(&path).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to read workspace document `{relative}`: {error}"
            ))
        })?;
        if bytes.len() > MAX_DOCUMENT_BYTES {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "document `{relative}` exceeds {MAX_DOCUMENT_BYTES} bytes"
            )));
        }
        // Markup and PDFs on disk are converted on the way out, not only on
        // download. Files arrive here by other routes too: the Project Euler
        // wrapper fetches `problem.html` with curl, and that statement is the
        // single most-read document in a run.
        if needs_conversion(relative, &bytes) {
            return super::readable::to_markdown(&bytes, None, relative);
        }
        String::from_utf8(bytes).map_err(|error| {
            tinyagents::TinyAgentsError::Validation(format!(
                "document `{relative}` is not UTF-8: {error}"
            ))
        })
    }

    /// Lists the visible file names directly inside `relative`.
    ///
    /// Hidden runtime bookkeeping is excluded, so an index built from this can
    /// never advertise a file the tools refuse to open.
    ///
    /// # Errors
    ///
    /// Returns an error when the folder escapes the workspace or cannot be
    /// read.
    pub(super) async fn file_names(&self, relative: &str) -> Result<Vec<String>> {
        let folder = if relative.is_empty() { "." } else { relative };
        ensure_visible(folder)?;
        let path = self.path(folder)?;
        let mut entries = tokio::fs::read_dir(&path).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to read workspace folder `{relative}`: {error}"
            ))
        })?;
        let mut names = Vec::new();
        while let Ok(Some(entry)) = entries.next_entry().await {
            let name = entry.file_name().to_string_lossy().into_owned();
            if HIDDEN_ENTRIES.contains(&name.as_str()) || name.starts_with('.') {
                continue;
            }
            if entry.file_type().await.is_ok_and(|kind| kind.is_file()) {
                names.push(name);
            }
        }
        names.sort();
        Ok(names)
    }

    /// Reports whether a visible workspace document exists.
    pub(super) fn exists(&self, relative: &str) -> bool {
        self.readable_path(relative).is_ok()
    }

    /// Reads a visible workspace document.
    ///
    /// # Errors
    ///
    /// Returns an error when the path is hidden, escapes the workspace, is
    /// missing, oversized, or is not UTF-8.
    pub(super) async fn read_document(&self, relative: &str) -> Result<String> {
        self.read(relative).await
    }

    /// Writes a visible workspace document on an agent's behalf.
    ///
    /// # Errors
    ///
    /// Returns an error when the path is hidden, escapes the workspace, or the
    /// content exceeds the per-document limit.
    pub(super) async fn write_document(&self, relative: &str, content: &str) -> Result<()> {
        self.write(relative, content).await
    }

    /// Deletes a visible workspace document.
    ///
    /// # Errors
    ///
    /// Returns an error when the path is hidden, escapes the workspace, or the
    /// file cannot be removed.
    pub(super) async fn remove(&self, relative: &str) -> Result<()> {
        let path = self.readable_path(relative)?;
        tokio::fs::remove_file(&path).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to delete workspace document `{relative}`: {error}"
            ))
        })
    }

    /// Writes raw bytes, used for the untouched copy of a download.
    async fn write_bytes(&self, relative: &str, bytes: &[u8]) -> Result<()> {
        if bytes.len() > MAX_DOCUMENT_BYTES {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "document content exceeds {MAX_DOCUMENT_BYTES} bytes"
            )));
        }
        let path = self.path(relative)?;
        let parent = path.parent().ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation("document path has no parent".into())
        })?;
        tokio::fs::create_dir_all(parent).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to create document directory: {error}"
            ))
        })?;
        tokio::fs::write(path, bytes).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to write workspace document `{relative}`: {error}"
            ))
        })
    }

    /// Writes a document on an agent's behalf.
    ///
    /// Refuses the runtime's own bookkeeping. The index writes through
    /// [`Self::write_internal`] instead, because the runtime maintaining its
    /// own index is not an agent reaching for it.
    async fn write(&self, relative: &str, content: &str) -> Result<()> {
        ensure_visible(relative)?;
        self.write_internal(relative, content).await
    }

    async fn write_internal(&self, relative: &str, content: &str) -> Result<()> {
        if content.len() > MAX_DOCUMENT_BYTES {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "document content exceeds {MAX_DOCUMENT_BYTES} bytes"
            )));
        }
        let path = self.path(relative)?;
        let parent = path.parent().ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation("document path has no parent".into())
        })?;
        tokio::fs::create_dir_all(parent).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to create document directory: {error}"
            ))
        })?;
        let canonical_parent = parent.canonicalize().map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to resolve document directory: {error}"
            ))
        })?;
        if !canonical_parent.starts_with(&self.workspace) {
            return Err(tinyagents::TinyAgentsError::Validation(
                "document path resolves outside /workspace".into(),
            ));
        }
        tokio::fs::write(path, content).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to write workspace document `{relative}`: {error}"
            ))
        })
    }

    /// Renders a bounded directory tree under `relative`.
    ///
    /// Agents were previously told file names in their prompts and had to
    /// guess anything else, so work already on disk went unread. Sizes are
    /// included because they are what distinguishes a finished derivation from
    /// an empty placeholder.
    async fn list(&self, relative: &str, depth: usize) -> Result<String> {
        let root = if relative == "." || relative.is_empty() {
            self.workspace.clone()
        } else {
            self.path(relative)?
        };
        if !root.is_dir() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{relative}` is not a directory in the workspace"
            )));
        }
        let mut lines = Vec::new();
        let mut truncated = false;
        walk(&root, &root, depth, &mut lines, &mut truncated).await?;
        lines.sort();
        let mut out = format!("{} (depth {depth})\n", display_root(relative));
        if lines.is_empty() {
            out.push_str("  (empty)\n");
        }
        for line in &lines {
            out.push_str(line);
            out.push('\n');
        }
        if truncated {
            let _ = write!(
                out,
                "  [listing truncated at {MAX_LISTING_ENTRIES} entries; narrow the path or depth]"
            );
        }
        Ok(out)
    }

    async fn indexed_paths(&self) -> Result<Vec<String>> {
        let path = self.workspace.join(INDEX_PATH);
        let bytes = match tokio::fs::read(path).await {
            Ok(bytes) => bytes,
            Err(error) if error.kind() == std::io::ErrorKind::NotFound => return Ok(Vec::new()),
            Err(error) => {
                return Err(tinyagents::TinyAgentsError::Tool(format!(
                    "failed to read document index: {error}"
                )));
            }
        };
        // A damaged index is rebuilt, not reported. It is runtime bookkeeping
        // the model never sees and cannot repair, so handing it a parse error
        // only converts a self-healing condition into a dead end — which is
        // exactly what happened on Euler 579, where three `index_document`
        // calls in a row failed against a corrupt file. The cost of starting
        // over is that `search_documents` misses whatever had been indexed
        // until those documents are indexed again; the cost of the error was
        // that indexing could never succeed again for the rest of the run.
        Ok(serde_json::from_slice(&bytes).unwrap_or_default())
    }

    async fn index(&self, relative: &str) -> Result<usize> {
        let content = self.read(relative).await?;
        let _guard = self.index_lock.lock().await;
        let mut paths = self.indexed_paths().await?;
        if !paths.iter().any(|path| path == relative) {
            paths.push(relative.to_string());
            paths.sort();
        }
        self.write_index(&serde_json::to_string_pretty(&paths)?)
            .await?;
        Ok(content.split_whitespace().count())
    }

    /// Replaces the index in one step that cannot be observed half-written.
    ///
    /// The lock above orders writers inside this process; the rename is what
    /// makes each write atomic on disk, so a crash or an unexpected second
    /// writer leaves the previous index intact rather than a truncated one.
    async fn write_index(&self, content: &str) -> Result<()> {
        let final_path = self.workspace.join(INDEX_PATH);
        let temporary = self.workspace.join(format!("{INDEX_PATH}.tmp"));
        tokio::fs::write(&temporary, content)
            .await
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("failed to stage document index: {error}"))
            })?;
        tokio::fs::rename(&temporary, &final_path)
            .await
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("failed to replace document index: {error}"))
            })
    }

    async fn search(&self, query: &str) -> Result<Vec<Value>> {
        let terms = query
            .split(|character: char| !character.is_alphanumeric())
            .filter(|term| !term.is_empty())
            .map(str::to_ascii_lowercase)
            .collect::<Vec<_>>();
        if terms.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "search query must contain a word".into(),
            ));
        }
        let mut results = Vec::new();
        for path in self.indexed_paths().await? {
            let Ok(content) = self.read(&path).await else {
                continue;
            };
            let lowercase = content.to_ascii_lowercase();
            let score = terms
                .iter()
                .map(|term| lowercase.match_indices(term).count())
                .sum::<usize>();
            if score == 0 {
                continue;
            }
            let first = terms
                .iter()
                .filter_map(|term| lowercase.find(term))
                .min()
                .unwrap_or_default();
            let start = floor_char_boundary(&content, first.saturating_sub(160));
            let end = ceil_char_boundary(&content, (first + 320).min(content.len()));
            results.push((
                score,
                json!({
                    "path": path,
                    "score": score,
                    "snippet": content[start..end].replace('\n', " ")
                }),
            ));
        }
        results.sort_by_key(|result| Reverse(result.0));
        Ok(results
            .into_iter()
            .take(MAX_SEARCH_RESULTS)
            .map(|(_, value)| value)
            .collect())
    }
}

/// Returns whether a stored document should be rendered to Markdown on read.
///
/// Keyed on the extension, plus the PDF magic bytes for a file saved without
/// one. Deliberately narrow: content sniffing every read would eventually
/// mangle a Markdown note that happens to quote some HTML.
fn needs_conversion(relative: &str, bytes: &[u8]) -> bool {
    if bytes.starts_with(b"%PDF-") {
        return true;
    }
    let lowered = relative.to_ascii_lowercase();
    [".html", ".htm", ".xhtml", ".pdf"]
        .iter()
        .any(|extension| lowered.ends_with(extension))
}

/// Recursively lists `directory`, appending one formatted line per entry.
fn walk<'a>(
    root: &'a std::path::Path,
    directory: &'a std::path::Path,
    depth: usize,
    lines: &'a mut Vec<String>,
    truncated: &'a mut bool,
) -> std::pin::Pin<Box<dyn Future<Output = Result<()>> + Send + 'a>> {
    Box::pin(async move {
        if depth == 0 || *truncated {
            return Ok(());
        }
        // An unreadable directory is skipped rather than failing the whole
        // listing: one bad permission should not hide the rest of the tree.
        let Ok(mut entries) = tokio::fs::read_dir(directory).await else {
            return Ok(());
        };
        while let Ok(Some(entry)) = entries.next_entry().await {
            if lines.len() >= MAX_LISTING_ENTRIES {
                *truncated = true;
                return Ok(());
            }
            let name = entry.file_name().to_string_lossy().into_owned();
            if HIDDEN_ENTRIES.contains(&name.as_str()) {
                continue;
            }
            let path = entry.path();
            let Ok(relative) = path.strip_prefix(root) else {
                continue;
            };
            let shown = relative.to_string_lossy();
            let Ok(metadata) = entry.metadata().await else {
                continue;
            };
            if metadata.is_dir() {
                lines.push(format!("  {shown}/"));
                walk(root, &path, depth - 1, lines, truncated).await?;
            } else {
                lines.push(format!("  {shown} ({} bytes)", metadata.len()));
            }
        }
        Ok(())
    })
}

/// Files a downloaded document under the research folder.
///
/// A path already inside the folder is left alone; anything else is moved into
/// it, and a leading `/workspace` or `./` is trimmed first so the common
/// spellings do not produce `research/workspace/...`.
pub(super) fn research_path(requested: &str) -> String {
    let trimmed = requested
        .trim()
        .trim_start_matches("/workspace/")
        .trim_start_matches("./")
        .trim_start_matches('/');
    if trimmed.is_empty() {
        return format!("{RESEARCH_DIR}/document.md");
    }
    if trimmed == RESEARCH_DIR || trimmed.starts_with(&format!("{RESEARCH_DIR}/")) {
        return trimmed.to_string();
    }
    format!("{RESEARCH_DIR}/{trimmed}")
}

/// Renames a stored document to `.md`, because that is what it now contains.
///
/// Everything filed under `research/` has been through `to_markdown`, so a
/// stored file called `paper.pdf` is a lie: it holds Markdown. The wrong
/// extension misleads every later reader — an agent deciding whether it can
/// read a file, a human opening the workspace, and any tool that dispatches on
/// suffix. The original bytes keep their true extension under `raw/`, which is
/// where a genuine PDF still lives.
pub(super) fn markdown_path(relative: &str) -> String {
    // No extension at all: give it the one it has earned.
    let Some((stem, extension)) = relative.rsplit_once('.') else {
        return format!("{relative}.md");
    };
    // A dot in a directory name is not an extension, and neither is a version
    // number in `zeta.2.1` — only rewrite when the tail looks like a suffix.
    if stem.is_empty()
        || extension.contains('/')
        || extension.is_empty()
        || !extension.chars().all(|c| c.is_ascii_alphanumeric())
    {
        return format!("{relative}.md");
    }
    if extension.eq_ignore_ascii_case("md") {
        return relative.to_string();
    }
    format!("{stem}.md")
}

/// Returns where a converted document's original bytes are archived.
///
/// Mirrors the research layout under [`RAW_DIR`] so the two stay in
/// correspondence: `research/papers/pell.md` archives to `raw/papers/pell.md`.
pub(super) fn raw_path(research_relative: &str) -> String {
    let tail = research_relative
        .strip_prefix(&format!("{RESEARCH_DIR}/"))
        .unwrap_or(research_relative);
    format!("{RAW_DIR}/{tail}")
}

/// Builds the bounded stand-in filed under `research/` for a fresh download.
///
/// Returns the whole text unchanged when it is already short enough, so a
/// small source is not decorated with a notice about truncation that did not
/// happen.
pub(super) fn research_excerpt(full: &str, full_relative: &str) -> String {
    if full.chars().count() <= RESEARCH_EXCERPT_CHARS {
        return full.to_string();
    }
    let head: String = full.chars().take(RESEARCH_EXCERPT_CHARS).collect();
    // Cut at a line boundary so the excerpt does not end mid-sentence.
    let head = head
        .rsplit_once('\n')
        .map_or(head.as_str(), |(body, _)| body);
    format!(
        "> **Excerpt only — read this first.** The complete text is beside it at \
         `{full_relative}`; open that only when this file does not answer the question, because \
         it is large. Replace this excerpt with a summary of what the source establishes and what \
         it implies for this problem — under 1000 tokens, and specific enough that nobody needs \
         the full text.\n\n{head}\n\n\
         *[excerpt ends; {} characters not shown — see `{full_relative}`]*\n",
        full.chars().count().saturating_sub(head.chars().count())
    )
}

/// Returns where a document's complete converted text sits beside its summary.
pub(super) fn full_text_path(summary_relative: &str) -> String {
    let stem = summary_relative
        .strip_suffix(".md")
        .unwrap_or(summary_relative);
    format!("{stem}{FULL_TEXT_SUFFIX}")
}

/// Renders the heading for a listing root.
fn display_root(relative: &str) -> String {
    if relative == "." || relative.is_empty() {
        "/workspace".to_string()
    } else {
        format!("/workspace/{}", relative.trim_start_matches('/'))
    }
}

#[derive(Clone, Copy, Debug)]
enum DocumentToolKind {
    Download,
    Read,
    Write,
    Edit,
    Index,
    Search,
    List,
}

impl DocumentToolKind {
    const ALL: [Self; 7] = [
        Self::Download,
        Self::Read,
        Self::Write,
        Self::Edit,
        Self::Index,
        Self::Search,
        Self::List,
    ];
}

/// Entries never worth showing an agent: its own bookkeeping, installed
/// packages, and the multi-megabyte event log.
const HIDDEN_ENTRIES: [&str; 6] = [
    ".workspace-history",
    ".python-packages",
    "__pycache__",
    ".document-index.json",
    "trace.jsonl",
    RAW_DIR,
];

/// Largest number of entries one listing returns.
const MAX_LISTING_ENTRIES: usize = 400;

/// Rejects a path that names one of the runtime's own hidden entries.
///
/// Hiding these from `list_workspace` was never enough, because an agent can
/// name a path the listing did not offer it. A reflection run did exactly
/// that: it read `/workspace/trace.jsonl` — 1,124,798 bytes of the run's own
/// event log — straight into its context, producing a single 339,652-token
/// model call, pushing the run past the 300,000-token compression trigger and
/// collapsing the prompt-cache hit rate from 71% to 26% in one turn.
///
/// The content is the worst possible thing to feed back in. The trace is a
/// verbatim record of every prompt and tool result the run has already seen,
/// so re-reading it tells the agent nothing new while costing more than any
/// real document could. Worse, the reader is the judge: reflection consuming a
/// replay of the attempt it is meant to assess is not evidence, it is an echo.
///
/// Enforced here rather than by asking the model to avoid the file, because a
/// prompt instruction is not a control — and the workspace policy previously
/// told agents to read this very file.
fn ensure_visible(relative: &str) -> Result<()> {
    let hidden = std::path::Path::new(relative)
        .components()
        .filter_map(|component| component.as_os_str().to_str())
        .find(|name| HIDDEN_ENTRIES.contains(name));
    if let Some(hidden) = hidden {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{hidden}` is runtime bookkeeping, not a workspace document; it is \
             already in your context or irrelevant to the problem"
        )));
    }
    Ok(())
}

#[derive(Debug)]
struct DocumentTool {
    kind: DocumentToolKind,
    documents: WorkspaceDocuments,
}

impl DocumentTool {
    /// Fetches a URL and stores it as Markdown.
    ///
    /// Split out of the tool dispatch because it is the only branch that does
    /// network work, size checks, and format conversion.
    async fn download(&self, call: &ToolCall) -> Result<String> {
        let output = {
            let url = required_string(&call.arguments, "url")?;
            let parsed = reqwest::Url::parse(&url).map_err(|error| {
                tinyagents::TinyAgentsError::Validation(format!("invalid document URL: {error}"))
            })?;
            if !matches!(parsed.scheme(), "http" | "https") {
                return Err(tinyagents::TinyAgentsError::Validation(
                    "document URL must use HTTP or HTTPS".into(),
                ));
            }
            let response = self
                .documents
                .client
                .get(parsed)
                .send()
                .await
                .map_err(|error| {
                    tinyagents::TinyAgentsError::Tool(format!("document download failed: {error}"))
                })?
                .error_for_status()
                .map_err(|error| {
                    tinyagents::TinyAgentsError::Tool(format!("document download failed: {error}"))
                })?;
            if response
                .content_length()
                .is_some_and(|length| length > MAX_DOCUMENT_BYTES as u64)
            {
                return Err(tinyagents::TinyAgentsError::Validation(
                    "downloaded document is too large".into(),
                ));
            }
            let content_type = response
                .headers()
                .get(reqwest::header::CONTENT_TYPE)
                .and_then(|value| value.to_str().ok())
                .map(ToOwned::to_owned);
            let bytes = response.bytes().await.map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!(
                    "failed to read downloaded document: {error}"
                ))
            })?;
            if bytes.len() > MAX_DOCUMENT_BYTES {
                return Err(tinyagents::TinyAgentsError::Validation(
                    "downloaded document is too large".into(),
                ));
            }
            // Convert to Markdown rather than storing raw bytes. A PDF or
            // a markup-heavy page is unreadable otherwise, and the old
            // UTF-8 check turned a PDF into an error that ended the run.
            let content = super::readable::to_markdown(&bytes, content_type.as_deref(), &url)?;
            let requested = research_path(&required_string(&call.arguments, "path")?);
            // The stored document is Markdown, so it is named `.md`. The
            // archive keeps the requested name, and so keeps the true
            // extension of the bytes it holds.
            let path = markdown_path(&requested);
            // Two archives, both best effort: the original bytes, and the full
            // converted text. Neither failing may fail a download that
            // otherwise succeeded.
            // The original bytes are archived out of sight; a failure there
            // must not fail a download that otherwise succeeded.
            let raw_original = raw_path(&requested);
            let archived = self
                .documents
                .write_bytes(&raw_original, &bytes)
                .await
                .is_ok();
            // The complete converted text sits beside the summary, reachable
            // when the summary is not enough.
            let full = full_text_path(&path);
            let excerpt = research_excerpt(&content, &full);
            let split = excerpt.len() < content.len();
            if split {
                self.documents.write(&full, &content).await?;
            }
            self.documents.write(&path, &excerpt).await?;
            format!(
                "downloaded {} bytes from {url}, converted to {} bytes of Markdown{}. {}",
                bytes.len(),
                content.len(),
                if archived {
                    ""
                } else {
                    " (original bytes not archived)"
                },
                if split {
                    format!(
                        "{path} holds a {} byte excerpt to read first; the complete text is at \
                         {full}. Have the scholar replace the excerpt with a summary.",
                        excerpt.len()
                    )
                } else {
                    format!("{path} holds the whole document ({} bytes)", excerpt.len())
                }
            )
        };
        Ok(output)
    }
}

#[async_trait]
impl Tool<()> for DocumentTool {
    fn name(&self) -> &'static str {
        match self.kind {
            DocumentToolKind::Download => "download_document",
            DocumentToolKind::Read => "read_document",
            DocumentToolKind::Write => "write_document",
            DocumentToolKind::Edit => "edit_document",
            DocumentToolKind::Index => "index_document",
            DocumentToolKind::Search => "search_documents",
            DocumentToolKind::List => "list_workspace",
        }
    }

    fn description(&self) -> &'static str {
        match self.kind {
            DocumentToolKind::Download => {
                "Downloads an HTTP or HTTPS document into /workspace, converting HTML and PDF to                  Markdown."
            }
            DocumentToolKind::Read => {
                "Reads a document from /workspace, rendering HTML and PDF to Markdown."
            }
            DocumentToolKind::Write => "Stores a UTF-8 document in /workspace.",
            DocumentToolKind::Edit => "Replaces one exact text occurrence in a workspace document.",
            DocumentToolKind::Index => "Adds a workspace document to the local searchable index.",
            DocumentToolKind::List => {
                "Lists the files and directories under a workspace path, with sizes, so relevant \
                 files can be found without guessing their names."
            }
            DocumentToolKind::Search => {
                "Searches indexed workspace documents and returns ranked snippets."
            }
        }
    }

    fn schema(&self) -> ToolSchema {
        let path = json!({ "type": "string", "description": "Relative path below /workspace." });
        let schema = match self.kind {
            DocumentToolKind::Download => json!({
                "type": "object",
                "properties": { "url": { "type": "string" }, "path": path },
                "required": ["url", "path"], "additionalProperties": false
            }),
            DocumentToolKind::Read | DocumentToolKind::Index => json!({
                "type": "object", "properties": { "path": path },
                "required": ["path"], "additionalProperties": false
            }),
            DocumentToolKind::Write => json!({
                "type": "object",
                "properties": { "path": path, "content": { "type": "string" } },
                "required": ["path", "content"], "additionalProperties": false
            }),
            DocumentToolKind::Edit => json!({
                "type": "object",
                "properties": {
                    "path": path,
                    "old_text": { "type": "string" },
                    "new_text": { "type": "string" }
                },
                "required": ["path", "old_text", "new_text"], "additionalProperties": false
            }),
            DocumentToolKind::Search => json!({
                "type": "object", "properties": { "query": { "type": "string" } },
                "required": ["query"], "additionalProperties": false
            }),
            DocumentToolKind::List => json!({
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative directory below /workspace. Defaults to the root."
                    },
                    "depth": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 6,
                        "description": "How many directory levels to descend. Defaults to 3."
                    }
                },
                "additionalProperties": false
            }),
        };
        ToolSchema::new(self.name(), self.description(), schema)
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let output = match self.kind {
            DocumentToolKind::Download => self.download(&call).await?,
            DocumentToolKind::Read => {
                self.documents
                    .read(&required_string(&call.arguments, "path")?)
                    .await?
            }
            DocumentToolKind::Write => {
                let path = required_string(&call.arguments, "path")?;
                let content = string_value(&call.arguments, "content")?;
                self.documents.write(&path, &content).await?;
                format!("wrote {} bytes to {path}", content.len())
            }
            DocumentToolKind::Edit => {
                let path = required_string(&call.arguments, "path")?;
                let old_text = required_string(&call.arguments, "old_text")?;
                let new_text = string_value(&call.arguments, "new_text")?;
                let content = self.documents.read(&path).await?;
                if !content.contains(&old_text) {
                    return Err(tinyagents::TinyAgentsError::Validation(
                        "old_text was not found in the document".into(),
                    ));
                }
                self.documents
                    .write(&path, &content.replacen(&old_text, &new_text, 1))
                    .await?;
                format!("edited {path}")
            }
            DocumentToolKind::Index => {
                let path = required_string(&call.arguments, "path")?;
                let words = self.documents.index(&path).await?;
                format!("indexed {path} ({words} words)")
            }
            DocumentToolKind::List => {
                let path = call
                    .arguments
                    .get("path")
                    .and_then(Value::as_str)
                    .unwrap_or(".")
                    .to_string();
                let depth = call
                    .arguments
                    .get("depth")
                    .and_then(Value::as_u64)
                    .and_then(|value| usize::try_from(value).ok())
                    .unwrap_or(3)
                    .clamp(1, 6);
                self.documents.list(&path, depth).await?
            }
            DocumentToolKind::Search => {
                let results = self
                    .documents
                    .search(&required_string(&call.arguments, "query")?)
                    .await?;
                serde_json::to_string(&results)?
            }
        };
        Ok(ToolResult::text(call.id, self.name(), output))
    }
}

fn required_string(arguments: &Value, name: &str) -> Result<String> {
    string_value(arguments, name).and_then(|value| {
        if value.trim().is_empty() {
            Err(tinyagents::TinyAgentsError::Validation(format!(
                "{name} must be a non-empty string"
            )))
        } else {
            Ok(value)
        }
    })
}

fn string_value(arguments: &Value, name: &str) -> Result<String> {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .map(ToOwned::to_owned)
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{name} must be a string")))
}

fn floor_char_boundary(text: &str, mut index: usize) -> usize {
    while index > 0 && !text.is_char_boundary(index) {
        index -= 1;
    }
    index
}

fn ceil_char_boundary(text: &str, mut index: usize) -> usize {
    while index < text.len() && !text.is_char_boundary(index) {
        index += 1;
    }
    index
}

#[cfg(test)]
mod test;
