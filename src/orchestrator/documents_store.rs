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
            library: None,
            screen: None,
            reader: None,
        })
    }

    /// Gives the run the recursive read: `map_document` answers a question
    /// about a document by reading it in chunks with this model.
    ///
    /// `model` must already carry accounting; see the field's documentation.
    #[must_use]
    pub(super) fn with_reader(
        mut self,
        model: Arc<dyn tinyagents::harness::model::ChatModel<()>>,
    ) -> Self {
        self.reader = Some(model);
        self
    }

    /// Screens what `download_document` brings back, on a calibration run.
    ///
    /// `None` is every ordinary run and leaves the tool untouched.
    #[must_use]
    pub(super) fn with_screen(mut self, screen: Option<super::screen::Screen>) -> Self {
        self.screen = screen;
        self
    }

    /// Files every later download in durable memory as well as on disk.
    ///
    /// Downloading and remembering used to be unrelated: the library lived in
    /// `research/` and in a local literal-term index, so nothing a run gathered
    /// was reachable through `recall_memory` — while every role's prompt said
    /// Cognee was the durable catalogue. The hook belongs here rather than in a
    /// separate tool because the moment the text is in hand is the only moment
    /// it is free to file.
    #[must_use]
    pub(super) fn with_library(mut self, library: super::vector::VectorStore) -> Self {
        self.library = Some(library);
        self
    }

    pub(super) fn tools(&self) -> Vec<Arc<dyn Tool<()>>> {
        DocumentToolKind::ALL
            .into_iter()
            .map(|kind| {
                let tool = Arc::new(DocumentTool {
                    kind,
                    documents: self.clone(),
                }) as Arc<dyn Tool<()>>;
                // Only the download reaches outside the workspace, so only the
                // download is screened. Wrapping the file tools too would put
                // an adjudicator in front of the run reading its own notes.
                match kind {
                    DocumentToolKind::Download => {
                        super::screen::wrap_one(self.screen.as_ref(), tool)
                    }
                    _ => tool,
                }
            })
            // Every agent that can create a file can describe it, so the
            // index tools travel with the document tools rather than being
            // granted to a role that then becomes the only one able to keep
            // the index honest.
            .chain(super::folder_index::FolderIndexTool::all(self))
            // What the library establishes is a question every reader of it
            // has, not only the role that writes the notes.
            .chain(super::claims::ClaimsTool::all(self))
            // The role that finds a gap is whichever one walked into it, so
            // stating one is available to every role rather than only to the
            // ones that go looking.
            .chain(super::requests::RequestTool::all(self))
            // The three ways to read something too large to read. They travel
            // with the document tools because they are not a specialism: every
            // role that can open a file can open one that does not fit, and a
            // role holding `read_document` without them has only the option
            // this runtime is trying to remove.
            .chain(super::outline::OutlineTool::all(self))
            .chain(super::grep::GrepTool::all(self))
            .chain(super::recursive::MapTool::all(self, self.reader.as_ref()))
            .collect()
    }

    /// The workspace this tool set is rooted at.
    pub(super) fn root(&self) -> &std::path::Path {
        &self.workspace
    }

    /// Reads the run's objective, or an empty string when it has none.
    ///
    /// Used to rank mechanically — how well a citation's prose matches what
    /// the run is trying to do. A run without a goal file simply ranks on the
    /// other signals, so a missing file is an empty string rather than an
    /// error.
    pub(super) async fn goal(&self) -> String {
        self.read_runtime("GOAL.md").await.unwrap_or_default()
    }

    fn path(&self, relative: &str) -> Result<PathBuf> {
        super::checked_workspace_path(&self.workspace, relative)
    }

    /// Resolves a folder, treating an empty path and `.` as the workspace root.
    ///
    /// The path checker refuses both — one is empty, the other is a `CurDir`
    /// component it cannot distinguish from traversal — and it is right to for
    /// a *file*. A folder argument is different: `.` is the obvious way to name
    /// the directory an agent is already standing in, and callers that
    /// normalise it to `""` on the way in would otherwise have it converted
    /// back to `.` here and refused. That cost a live agent its
    /// `refresh_index` on the workspace root.
    fn folder_path(&self, relative: &str) -> Result<PathBuf> {
        if relative.is_empty() || relative == "." {
            return Ok(self.workspace.clone());
        }
        self.path(relative)
    }

    /// Finds a file of the same name elsewhere under the requested root.
    pub(super) fn same_name_elsewhere(&self, relative: &str) -> Option<String> {
        let (root, name) = relative.split_once('/')?;
        let name = std::path::Path::new(name).file_name()?;
        [SOURCE_DIR, DIGEST_DIR].into_iter().find_map(|folder| {
            if !folder.starts_with(root) {
                return None;
            }
            let candidate = std::path::Path::new(folder).join(name);
            self.workspace
                .join(&candidate)
                .is_file()
                .then(|| candidate.to_string_lossy().into_owned())
        })
    }

    /// Names what does exist beside a path that does not.
    ///
    /// A model that guessed `research/DIGEST.md` or `research/raw` learns only
    /// that it guessed wrong, and its cheapest next move is to guess again —
    /// each attempt costing a full model turn. Listing the folder's real
    /// entries turns the failure into the answer, so the correction happens on
    /// the next call rather than the next few. Returns an empty string when
    /// there is nothing useful to add, so the caller can always append it.
    fn nearby(&self, relative: &str) -> String {
        // A note's batch number is the one thing an agent cannot infer: it
        // knows the name, and which of `L1.0`, `L1.1`, `L1.2` holds it is an
        // accident of when it arrived. Seven of one live run's twenty-three
        // tool failures were exactly this guess. Naming the file's real home
        // answers the question the failed read was asking.
        if let Some(found) = self.same_name_elsewhere(relative) {
            return format!("; it is at `{found}`");
        }
        let requested = std::path::Path::new(relative);
        let folder = match requested.parent() {
            Some(parent) if !parent.as_os_str().is_empty() => parent.to_path_buf(),
            _ => std::path::PathBuf::new(),
        };
        // Resolved as a folder, not a file: a name at the workspace root has an
        // empty parent, and the file checker refuses that. Routing it through
        // `path` made this whole helper silently do nothing for exactly the
        // paths agents get wrong most — the ones at the root.
        let Ok(directory) = self.folder_path(folder.to_string_lossy().as_ref()) else {
            return String::new();
        };
        // A missing parent is left unreported rather than walked upwards: the
        // useful answer is what sits beside the requested name, and naming a
        // grandparent's contents invites a second wrong guess.
        let Ok(entries) = std::fs::read_dir(&directory) else {
            return String::new();
        };
        let mut names: Vec<String> = entries
            .flatten()
            .map(|entry| {
                let name = entry.file_name().to_string_lossy().to_string();
                if entry.file_type().is_ok_and(|kind| kind.is_dir()) {
                    format!("{name}/")
                } else {
                    name
                }
            })
            // Whatever the listing hides, this hides too. Naming the raw
            // download folder here would advertise the one directory the run is
            // deliberately kept out of.
            .filter(|name| {
                !name.starts_with('.')
                    && name != &format!("{RAW_DIR}/")
                    && name != "__pycache__/"
                    && name != "trace.jsonl"
            })
            .collect();
        if names.is_empty() {
            return String::new();
        }
        names.sort();
        names.truncate(NEARBY_ENTRIES);
        format!("; the folder holds {}", names.join(", "))
    }

    fn readable_path(&self, relative: &str) -> Result<PathBuf> {
        ensure_visible(relative)?;
        let path = self.path(relative)?;
        let canonical = path.canonicalize().map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to resolve workspace document `{relative}`: {error}{}",
                self.nearby(relative)
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
        ensure_visible(relative)?;
        let path = self.folder_path(relative)?;
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
            let Ok(kind) = entry.file_type().await else {
                continue;
            };
            if kind.is_file() {
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

    /// Lists every visible file under `relative`, recursively.
    ///
    /// Unlike [`Self::file_names`] this descends, because the question
    /// [`super::grep`] asks is "where in the workspace", and a search that
    /// stopped at one directory would answer it wrongly rather than
    /// incompletely — `research/sources/` is two levels below the root a caller
    /// naturally names.
    ///
    /// Ordered, so a search returns the same result twice running, and bounded
    /// by `limit` so a tree that has grown an enumeration pool cannot turn one
    /// call into an unbounded walk.
    ///
    /// # Errors
    ///
    /// Returns an error when the path is hidden or escapes the workspace.
    pub(super) async fn walk_files(&self, relative: &str, limit: usize) -> Result<Vec<String>> {
        ensure_visible(relative)?;
        let root = self.folder_path(relative)?;
        // A caller may name a single file; searching it is a reasonable thing
        // to ask for and refusing would be pedantry.
        if root.is_file() {
            return Ok(vec![super::strip_workspace_prefix(relative).to_string()]);
        }
        let mut found = Vec::new();
        let mut pending = vec![root];
        while let Some(directory) = pending.pop() {
            if found.len() >= limit {
                break;
            }
            let Ok(mut entries) = tokio::fs::read_dir(&directory).await else {
                continue;
            };
            while let Ok(Some(entry)) = entries.next_entry().await {
                let name = entry.file_name().to_string_lossy().into_owned();
                if HIDDEN_ENTRIES.contains(&name.as_str()) || name.starts_with('.') {
                    continue;
                }
                let path = entry.path();
                let Ok(kind) = entry.file_type().await else {
                    continue;
                };
                if kind.is_dir() {
                    pending.push(path);
                } else if kind.is_file()
                    && let Ok(relative) = path.strip_prefix(&self.workspace)
                {
                    found.push(relative.to_string_lossy().into_owned());
                }
            }
        }
        found.sort();
        found.truncate(limit);
        Ok(found)
    }

    /// Reads a document's bytes as text, refusing anything over `limit`.
    ///
    /// Separate from [`Self::read`] because the caller is scanning rather than
    /// reading: it wants the file skipped, not the call failed, when the file
    /// is enormous or is not text at all. Nothing is converted — a scan of a
    /// PDF's raw bytes finds nothing and costs nothing, where converting every
    /// PDF in a library to Markdown to grep it would cost minutes.
    ///
    /// # Errors
    ///
    /// Returns an error when the path is hidden, escapes the workspace, is
    /// missing, exceeds `limit`, or is not UTF-8.
    pub(super) async fn read_bounded(&self, relative: &str, limit: u64) -> Result<String> {
        let path = self.readable_path(relative)?;
        let metadata = tokio::fs::metadata(&path).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to stat `{relative}`: {error}"))
        })?;
        if metadata.len() > limit {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{relative}` is {} bytes, over the {limit} byte scan limit",
                metadata.len()
            )));
        }
        let bytes = tokio::fs::read(&path).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to read `{relative}`: {error}"))
        })?;
        String::from_utf8(bytes)
            .map_err(|_| tinyagents::TinyAgentsError::Validation(format!("`{relative}` is not UTF-8")))
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
        replace_atomically(&path, bytes, &format!("workspace document `{relative}`")).await
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

    /// Writes a file the runtime maintains rather than an agent.
    ///
    /// The frontier's ledger and its rendered table are written by code on
    /// every download, the way the reflection log is written by the loop. Both
    /// go through here rather than through [`Self::write`] because the visible
    /// check exists to stop an *agent* reaching for the runtime's bookkeeping,
    /// and the runtime keeping its own books is not that.
    pub(super) async fn write_runtime(&self, relative: &str, content: &str) -> Result<()> {
        self.write_internal(relative, content).await
    }

    /// Fetches a URL and returns its body as text.
    ///
    /// For the structured endpoints a source adapter talks to, where the reply
    /// is JSON to be read rather than a document to be filed. Bounded by the
    /// same limit and served by the same client, so an adapter cannot become a
    /// way around either.
    ///
    /// # Errors
    ///
    /// Returns an error when the URL is not HTTP, the request fails, the reply
    /// exceeds the document limit, or it is not UTF-8.
    pub(super) async fn fetch_text(&self, url: &str) -> Result<String> {
        let parsed = reqwest::Url::parse(url).map_err(|error| {
            tinyagents::TinyAgentsError::Validation(format!("invalid URL: {error}"))
        })?;
        if !matches!(parsed.scheme(), "http" | "https") {
            return Err(tinyagents::TinyAgentsError::Validation(
                "URL must use HTTP or HTTPS".into(),
            ));
        }
        let response = self
            .client
            .get(parsed)
            .send()
            .await
            .map_err(|error| tinyagents::TinyAgentsError::Tool(format!("request failed: {error}")))?
            .error_for_status()
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("request failed: {error}"))
            })?;
        let bytes = response.bytes().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to read the reply: {error}"))
        })?;
        if bytes.len() > MAX_DOCUMENT_BYTES {
            return Err(tinyagents::TinyAgentsError::Validation(
                "the reply is too large".into(),
            ));
        }
        String::from_utf8(bytes.to_vec()).map_err(|error| {
            tinyagents::TinyAgentsError::Validation(format!("reply is not UTF-8: {error}"))
        })
    }

    /// Reads a file the runtime maintains, bypassing the visibility check.
    ///
    /// # Errors
    ///
    /// Returns an error when the file is absent, oversized, or not UTF-8.
    pub(super) async fn read_runtime(&self, relative: &str) -> Result<String> {
        let path = self.path(relative)?;
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
        String::from_utf8(bytes).map_err(|error| {
            tinyagents::TinyAgentsError::Validation(format!(
                "document `{relative}` is not UTF-8: {error}"
            ))
        })
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
        replace_atomically(
            &path,
            content.as_bytes(),
            &format!("workspace document `{relative}`"),
        )
        .await
    }

    /// Renders a bounded directory tree under `relative`.
    ///
    /// Agents were previously told file names in their prompts and had to
    /// guess anything else, so work already on disk went unread. Sizes are
    /// included because they are what distinguishes a finished derivation from
    /// an empty placeholder.
    async fn list(&self, relative: &str, depth: usize) -> Result<String> {
        let root = self.folder_path(relative)?;
        if !root.is_dir() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{relative}` is not a directory in the workspace{}",
                self.nearby(relative)
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
        // The index lives under `config/`, which a fresh workspace does not
        // have until something writes there first.
        if let Some(parent) = final_path.parent() {
            let _ = tokio::fs::create_dir_all(parent).await;
        }
        replace_atomically(&final_path, content.as_bytes(), "document index").await
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

/// Replaces a file in one step that cannot be observed half-written.
///
/// A bare `tokio::fs::write` truncates and then writes, which is two operations
/// rather than one: a reader between them sees an empty or partial file, and
/// two writers interleave into a file that is neither's. That was already
/// measured on the document index, where three concurrent writes left four
/// stranded bytes on the end and invalid JSON behind them. Staging beside the
/// destination and renaming over it is atomic within a directory, so a reader
/// sees the old bytes or the new ones and never half of each.
///
/// The staged name carries the process id and a per-process ticket, so two
/// writers racing for one destination do not also collide on the file they
/// stage it through. It starts with a dot, which is what keeps a listing from
/// advertising a file that exists for microseconds.
///
/// This is per-file atomicity only. Ordering a write against the ledgers
/// derived from it is [`super::worklock::writes`]'s job, and is taken at the
/// tool-call boundary rather than here.
async fn replace_atomically(final_path: &std::path::Path, bytes: &[u8], what: &str) -> Result<()> {
    static STAGED: std::sync::atomic::AtomicU64 = std::sync::atomic::AtomicU64::new(0);
    let name = final_path
        .file_name()
        .map(|name| name.to_string_lossy().into_owned())
        .unwrap_or_default();
    let ticket = STAGED.fetch_add(1, std::sync::atomic::Ordering::Relaxed);
    let staged = final_path.with_file_name(format!(".{name}.{}.{ticket}.tmp", std::process::id()));
    tokio::fs::write(&staged, bytes).await.map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to stage {what}: {error}"))
    })?;
    if let Err(error) = tokio::fs::rename(&staged, final_path).await {
        // The staged copy is nobody's document. Left behind it would be a file
        // in the workspace that no index explains and no later write replaces.
        let _ = tokio::fs::remove_file(&staged).await;
        return Err(tinyagents::TinyAgentsError::Tool(format!(
            "failed to replace {what}: {error}"
        )));
    }
    Ok(())
}
