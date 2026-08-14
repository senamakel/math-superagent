#[derive(Debug)]
struct DocumentTool {
    kind: DocumentToolKind,
    documents: WorkspaceDocuments,
}

impl DocumentTool {
    /// Retrieves a URL's bytes and its declared content type.
    ///
    /// Bounded twice — once on the declared length and once on what actually
    /// arrives — because a server may understate the first and the second is
    /// the only one that has to be true.
    ///
    /// The second bound is applied *as the body streams*, which is the part
    /// that was missing. `Response::bytes` reads the whole response into memory
    /// and only then can its length be compared, so the limit described a
    /// document the runtime had already paid for: a chunked response carries no
    /// `Content-Length` to check beforehand, and one that lies is exactly the
    /// case the second check exists for. The container has a hard `mem_limit`
    /// and an OOM kill loses everything in flight, so a 5 MiB ceiling that
    /// requires buffering an arbitrary body to enforce is not a ceiling.
    ///
    /// The transfer is abandoned at the limit rather than truncated. A half a
    /// paper is not a shorter paper — its text layer will not parse, its
    /// reference list is gone, and the digest built from it would misrepresent
    /// what the source says. Refusing names the size so the caller can look for
    /// another copy.
    async fn fetch(&self, url: &str) -> Result<(Vec<u8>, Option<String>)> {
        let parsed = reqwest::Url::parse(url).map_err(|error| {
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
        let mut response = response;
        let mut bytes: Vec<u8> = Vec::new();
        while let Some(chunk) = response.chunk().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!(
                "failed to read downloaded document: {error}"
            ))
        })? {
            if bytes.len() + chunk.len() > MAX_DOCUMENT_BYTES {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "downloaded document exceeds {MAX_DOCUMENT_BYTES} bytes and the transfer was \
                     abandoned; find a smaller source, or one page of this one"
                )));
            }
            bytes.extend_from_slice(&chunk);
        }
        Ok((bytes, content_type))
    }

    /// Re-derives the claim ledger when the written file is a research note.
    ///
    /// Done in the write path rather than asked for in a prompt, on the same
    /// argument as placement: a derived file that disagrees with its sources
    /// is worse than no derived file, because the next reader trusts the row
    /// instead of opening the note. Returns the sentence to append to the tool
    /// result — a model not told the ledger moved has no reason to read it.
    async fn reledger(&self, path: &str) -> String {
        if super::threads::is_thread(path) {
            super::threads::refresh(&self.documents).await;
            return format!(" and re-derived {}", super::threads::THREADS_PATH);
        }
        // An approach carries no claim ids, so unlike a thread it cannot be
        // stranded by a note that changes what the library establishes. Its
        // table is therefore re-derived only when an approach itself is
        // written.
        if super::approaches::is_approach(path) {
            super::approaches::refresh(&self.documents).await;
            return format!(" and re-derived {}", super::approaches::APPROACHES_PATH);
        }
        if super::backward::is_backward(path) {
            super::backward::refresh(&self.documents).await;
            return format!(" and re-derived {}", super::backward::BACKWARD_PATH);
        }
        if super::weakened::is_weakened(path) {
            super::weakened::refresh(&self.documents).await;
            return format!(" and re-derived {}", super::weakened::WEAKENED_PATH);
        }
        if !super::claims::is_note(path) {
            return String::new();
        }
        super::claims::refresh(&self.documents).await;
        // A thread rests on claim ids, so a note that changes what the library
        // establishes can strand a thread on a claim that is no longer there.
        super::threads::refresh(&self.documents).await;
        // A gap is discharged *by* a claim, so the same note can close a gap or
        // strand one — which is why the skeleton ledger follows a note write
        // and the approach ledger does not.
        super::backward::refresh(&self.documents).await;
        // And the ladder, for the same reason one step weaker: a rung is
        // settled by a claim, so a note can turn the current rung into a
        // settled one. A ladder still pointing at a rung the run has already
        // proved is how the next attempt spends itself re-proving it.
        super::weakened::refresh(&self.documents).await;
        format!(
            " and re-derived {}, {}, {} and {}",
            super::claims::CLAIMS_PATH,
            super::threads::THREADS_PATH,
            super::backward::BACKWARD_PATH,
            super::weakened::WEAKENED_PATH
        )
    }

    /// Fetches a URL and stores it as Markdown.
    ///
    /// Split out of the tool dispatch because it is the only branch that does
    /// network work, size checks, and format conversion.
    async fn download(&self, call: &ToolCall) -> Result<String> {
        let output = {
            let url = required_string(&call.arguments, "url")?;
            // A source already in the library is not downloaded twice. The
            // refusal names the file, so the model's next move is to read what
            // the run already has rather than to guess at another spelling of
            // the same URL.
            if let Some(existing) = super::frontier::already_fetched(&self.documents, &url).await {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "{url} is already in this library at `{existing}` — read that instead of \
                     downloading it again"
                )));
            }
            let (bytes, content_type) = self.fetch(&url).await?;
            // Convert to Markdown rather than storing raw bytes. A PDF or
            // a markup-heavy page is unreadable otherwise, and the old
            // UTF-8 check turned a PDF into an error that ended the run.
            let converted = super::readable::convert(&bytes, content_type.as_deref(), &url)?;
            let content = converted.markdown;
            let requested = research_path(
                self.documents.root(),
                &required_string(&call.arguments, "path")?,
            );
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
            let full = full_text_path(self.documents.root(), &path);
            let excerpt = super::digest::digest(&content, &full);
            let split = excerpt.len() < content.len();
            if split {
                self.documents.write(&full, &content).await?;
            }
            self.documents.write(&path, &excerpt).await?;
            // What this source cites becomes the run's next set of leads, and
            // this is the only moment the citations are in hand. Best effort:
            // the download has already succeeded, and a lost lead must not
            // turn a stored document into a failed tool call.
            super::frontier::record(
                &self.documents,
                &url,
                &path,
                &converted.links,
                &self.documents.goal().await,
            )
            .await;
            // File the source in durable memory too, so `recall_memory`
            // reaches what the run gathered and not only what it concluded.
            // Best effort and reported: a memory that refused the document
            // must not fail a download that succeeded, but a library the run
            // believes is searchable and is not is worse than one it knows is
            // not.
            let remembered = match self.documents.library.as_ref() {
                None => String::new(),
                Some(library) => match library
                    .remember_source(&path, &url, &bytes, content_type.as_deref())
                    .await
                {
                    Ok(()) => " and filed in durable memory".to_string(),
                    Err(error) => format!(" (not filed in durable memory: {error})"),
                },
            };
            // Say what this is while the answer is still known. The scholar
            // replaces this with what the source establishes; until it does,
            // the row names the origin and the title rather than nothing.
            super::folder_index::record_description(
                &self.documents,
                &path,
                &provisional_description(&content, &url),
            )
            .await;
            format!(
                "downloaded {} bytes from {url}, converted to {} bytes of Markdown{}{remembered}. {}",
                bytes.len(),
                content.len(),
                if archived {
                    ""
                } else {
                    " (original bytes not archived)"
                },
                if split {
                    format!(
                        "{path} holds a {} byte structural digest to read first — its outline, \
                         what it claims, and the statements it makes; the complete text is at \
                         {full}. Have the scholar replace the digest with a summary. {} of its \
                         citations were added to {}.",
                        excerpt.len(),
                        converted.links.len(),
                        super::frontier::FRONTIER_PATH
                    )
                } else {
                    format!(
                        "{path} holds the whole document ({} bytes); {} of its citations were \
                         added to {}.",
                        excerpt.len(),
                        converted.links.len(),
                        super::frontier::FRONTIER_PATH
                    )
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
                let requested = required_string(&call.arguments, "path")?;
                let content = string_value(&call.arguments, "content")?;
                // Placement is decided here rather than asked for in a prompt.
                // A run that writes its thirty-first program to the root has
                // buried the two files carrying its derivation.
                let path = super::layout::placed(&requested);
                self.documents.write(&path, &content).await?;
                format!(
                    "wrote {} bytes to {path}{}{}",
                    content.len(),
                    super::layout::note(&requested, &path),
                    self.reledger(&path).await
                )
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
                format!("edited {path}{}", self.reledger(&path).await)
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
