//! Bounded tools for workspace documents and a local searchable index.

use std::cmp::Reverse;
use std::path::PathBuf;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

const INDEX_PATH: &str = ".document-index.json";
const MAX_DOCUMENT_BYTES: usize = 5 * 1024 * 1024;
const MAX_SEARCH_RESULTS: usize = 10;

#[derive(Clone, Debug)]
pub(super) struct WorkspaceDocuments {
    workspace: PathBuf,
    client: reqwest::Client,
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
        Ok(Self { workspace, client })
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
            .collect()
    }

    fn path(&self, relative: &str) -> Result<PathBuf> {
        super::checked_workspace_path(&self.workspace, relative)
    }

    fn readable_path(&self, relative: &str) -> Result<PathBuf> {
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

    async fn write(&self, relative: &str, content: &str) -> Result<()> {
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
        serde_json::from_slice(&bytes).map_err(Into::into)
    }

    async fn index(&self, relative: &str) -> Result<usize> {
        let content = self.read(relative).await?;
        let mut paths = self.indexed_paths().await?;
        if !paths.iter().any(|path| path == relative) {
            paths.push(relative.to_string());
            paths.sort();
        }
        self.write(INDEX_PATH, &serde_json::to_string_pretty(&paths)?)
            .await?;
        Ok(content.split_whitespace().count())
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
const HIDDEN_ENTRIES: [&str; 5] = [
    ".workspace-history",
    ".python-packages",
    "__pycache__",
    ".document-index.json",
    "trace.jsonl",
];

/// Largest number of entries one listing returns.
const MAX_LISTING_ENTRIES: usize = 400;

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
            let path = required_string(&call.arguments, "path")?;
            self.documents.write(&path, &content).await?;
            format!(
                "downloaded {} bytes from {url}, converted to {} bytes of Markdown at {path}",
                bytes.len(),
                content.len()
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
                "Lists the files and directories under a workspace path, with sizes, so relevant \
                 files can be found without guessing their names."
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
