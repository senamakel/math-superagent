impl VectorStore {
    /// Runs one search against this project's datasets and renders the hits.
    ///
    /// `search_type` is Cognee's: [`CHUNK_SEARCH`] for passages,
    /// [`GRAPH_SEARCH`] for the relationships between entities. Both tools
    /// share this because the only thing that differs between them is that
    /// string, and a second copy of the request would drift from the first the
    /// moment either is corrected.
    ///
    /// Returns `Ok(None)` when the memory has nothing, so each caller can say
    /// so in its own words rather than returning an empty result the model has
    /// to interpret.
    ///
    /// # Errors
    ///
    /// Returns an error when Cognee is unreachable, refuses the request, or
    /// answers with something other than a JSON array.
    pub(super) async fn search(
        &self,
        query: &str,
        search_type: &str,
        limit: u64,
    ) -> Result<Option<String>> {
        let datasets = self.recall_datasets().await?;
        self.search_in(
            datasets,
            durable_node_sets(&self.project),
            query,
            search_type,
            limit,
        )
        .await
    }

    /// Runs one search against exactly the datasets and node sets named.
    ///
    /// Split from [`VectorStore::search`] so the scratch can be read without
    /// being listed among the datasets durable recall reaches. Sharing the
    /// request is what keeps a correction to one from drifting from the other.
    ///
    /// `node_sets` is the scoping that actually holds, and that is the
    /// correction of a measured leak rather than a belt-and-braces addition.
    /// `datasets` is the boundary this runtime was built around — the
    /// allowlist in [`visible_datasets`] exists to compute it — and the server
    /// does not apply it: a live probe asking for one project's session
    /// dataset, then another's, then a third's by UUID, returned the *same*
    /// chunk from a fourth project every time, while a name that matched no
    /// dataset was the only request that changed the answer, to an error. So
    /// every run on the box was reading every other project's memory, and the
    /// allowlist was scoping a field nothing downstream honoured. `node_name`
    /// filters on the `node_set` each document was ingested under, which the
    /// same probe showed is applied exactly: asking for `project:<a>` returned
    /// only `<a>`'s documents and asking for `project:<b>` only `<b>`'s. Both
    /// are sent — the dataset list still bounds what a working server would
    /// search, and it costs nothing to keep asking for the narrower thing.
    ///
    /// # Errors
    ///
    /// Returns an error when Cognee is unreachable, refuses the request, or
    /// answers with something other than a JSON array.
    async fn search_in(
        &self,
        datasets: Vec<String>,
        node_sets: Vec<String>,
        query: &str,
        search_type: &str,
        limit: u64,
    ) -> Result<Option<String>> {
        if datasets.is_empty() || node_sets.is_empty() {
            return Ok(None);
        }
        // The one place every recall passes through, so the one place worth
        // checking that what is being asked for can be scoped at all. See
        // [`SCOPE_SAFE_SEARCH_TYPES`]: a retriever that ignores `node_name`
        // searches every project on the server, and this runtime has already
        // shipped that leak once through the dataset field.
        if !SCOPE_SAFE_SEARCH_TYPES.contains(&search_type) {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{search_type}` cannot be scoped to one project on this server and must not be \
                 used"
            )));
        }
        let response = self
            .client
            .post(format!("{}/api/v1/recall", self.base_url))
            .json(&json!({
                "query": query,
                "datasets": datasets,
                "node_name": node_sets,
                "search_type": search_type,
                "only_context": true,
                "include_references": true,
                "top_k": limit
            }))
            .send()
            .await
            .map_err(|error| cognee_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(cognee_response_error("recall", response).await);
        }
        let body: Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("Cognee returned invalid JSON: {error}"))
        })?;
        let results = body.as_array().ok_or_else(|| {
            tinyagents::TinyAgentsError::Tool("Cognee recall response was not an array".into())
        })?;
        if results.is_empty() {
            return Ok(None);
        }
        Ok(Some(
            results
                .iter()
                .enumerate()
                .map(|(index, result)| {
                    format!(
                        "{}. {}",
                        index + 1,
                        truncate_chars(&render_result(result), 4_000)
                    )
                })
                .collect::<Vec<_>>()
                .join("\n\n"),
        ))
    }

    /// Runs two searches at once and returns both answers under one heading
    /// each.
    ///
    /// The two retrievers answer different questions about the same memory and
    /// miss in opposite directions. `CHUNKS` returns the passages nearest a
    /// phrase, so it finds what a source said and is blind to anything nobody
    /// wrote in one place. `TRIPLET_COMPLETION` returns the graph's own
    /// subject–predicate–object edges, so it finds what the run connected
    /// across sources and is blind to the wording. A run that only ever asks
    /// for chunks is paying for a graph store and using it as a search box —
    /// which is what this runtime did for as long as recall meant one search.
    ///
    /// Concurrent because they are independent and the slower one is what the
    /// caller waits for either way; sequential would make the richer answer
    /// cost twice the latency, which is how a richer answer stops being asked
    /// for.
    ///
    /// One side failing is not a failed recall. A graph half that errors while
    /// the passage half answers still leaves the caller better off than the
    /// error would, so a failure becomes a line in the result saying which half
    /// is missing. Both failing propagates the passage side's error, because
    /// then there is nothing to return and silence would read as "nothing
    /// known".
    ///
    /// # Errors
    ///
    /// Returns an error when both searches fail.
    pub(super) async fn search_fused(&self, query: &str, limit: u64) -> Result<Option<String>> {
        // Split between the two, with the passage side favoured: it is the one
        // that returns readable text, and a triple is worth less per row.
        let graph_limit = (limit / 3).max(1);
        let chunk_limit = limit.saturating_sub(graph_limit).max(1);
        let (passages, triples) = tokio::join!(
            self.search(query, CHUNK_SEARCH, chunk_limit),
            self.search(query, TRIPLET_SEARCH, graph_limit)
        );
        let passages = match passages {
            Ok(found) => found,
            Err(error) => {
                let Ok(triples) = triples else {
                    return Err(error);
                };
                return Ok(triples.map(|triples| {
                    format!(
                        "## What this memory connects\n\n{triples}\n\n(The passage search failed: \
                         {error}. Only the graph half of this recall answered.)"
                    )
                }));
            }
        };
        let mut sections: Vec<String> = Vec::new();
        if let Some(passages) = passages {
            sections.push(format!("## Passages\n\n{passages}"));
        }
        match triples {
            Ok(Some(triples)) => sections.push(format!("## What this memory connects\n\n{triples}")),
            Ok(None) => {}
            Err(error) => sections.push(format!(
                "(The graph half of this recall failed: {error}. What is above is the passage \
                 search alone.)"
            )),
        }
        Ok((!sections.is_empty()).then(|| sections.join("\n\n")))
    }

    pub(super) fn from_env() -> Result<Self> {
        let base_url = std::env::var("COGNEE_API_URL").map_err(|_| {
            tinyagents::TinyAgentsError::Validation("COGNEE_API_URL is required".into())
        })?;
        let base_url = base_url.trim_end_matches('/').to_string();
        if base_url.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "COGNEE_API_URL cannot be empty".into(),
            ));
        }
        let project =
            slug(&std::env::var("MATH_AGENT_WORKSPACE_LABEL").unwrap_or_else(|_| "default".into()));
        let nanos = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap_or_default()
            .as_nanos();
        // The run id identifies a run, and it belongs *inside* the document —
        // `remember_session` writes it as a `Session:` line. It used to be part
        // of the dataset name as well, which made the name unique per process:
        // `math_agent_sessions__project_euler_185__s18cb030630d9e2be-1`. Every
        // restart therefore opened a fresh dataset, and because `recall` shows
        // a run only its own session dataset, every restart also *lost* the
        // session memory of every earlier run on that problem. One problem
        // restarted eight times in a day left eight datasets, seven of them
        // unreachable. The dataset is the project; the run is a field.
        let session = format!("s{nanos:x}-{}", std::process::id());
        let session_dataset = format!("{SESSION_DATASET_PREFIX}{project}");
        let scratch_dataset = format!("{SCRATCH_DATASET_PREFIX}{project}");
        let library_dataset = format!("{LIBRARY_DATASET_PREFIX}{project}");
        Ok(Self {
            client: reqwest::Client::new(),
            base_url,
            project,
            session,
            session_dataset,
            scratch_dataset,
            library_dataset,
        })
    }

    /// Records one provisional note in this project's scratch.
    ///
    /// Ingested in the background: a scratch note is written mid-derivation and
    /// waiting on an index would put the memory on the critical path of the
    /// arithmetic it is describing, which is exactly what a file did not do.
    pub(super) async fn note_scratch(&self, text: &str, topic: &str) -> Result<u64> {
        let id = point_id(&format!("{topic}\n{text}"));
        let document = format!(
            "# Provisional note\n\nProject: {}\nSession: {}\nTopic: {topic}\n\n{text}\n",
            self.project, self.session
        );
        self.enqueue(
            document,
            format!("scratch-{}-{id}.md", slug(topic)),
            &self.scratch_dataset,
            &scratch_node_set(&self.project),
        )
        .await?;
        Ok(id)
    }

    /// Returns the provisional notes nearest a phrase, and nothing durable.
    ///
    /// # Errors
    ///
    /// Returns an error when Cognee is unreachable or refuses the request.
    pub(super) async fn recall_scratch(&self, query: &str, limit: u64) -> Result<Option<String>> {
        // A project that has not written a scratch note yet has no scratch
        // dataset, and naming one Cognee does not hold is the single request
        // shape it refuses outright — "No datasets found". Nothing recorded is
        // an answer rather than a failure, so it is answered here.
        if !self.dataset_exists(&self.scratch_dataset).await? {
            return Ok(None);
        }
        self.search_in(
            vec![self.scratch_dataset.clone()],
            vec![scratch_node_set(&self.project)],
            query,
            CHUNK_SEARCH,
            limit,
        )
        .await
    }

    /// Queues one durable Markdown memory in the shared brain.
    ///
    /// Queued rather than awaited, and that is the correction of a measured
    /// failure. Waiting for Cognee to finish indexing meant waiting on its
    /// entity extraction: four live `remember_memory` calls took 66, 114 and
    /// 177 seconds, and the fourth hit the ten-minute tool ceiling and was
    /// killed, losing the falsified conjecture it was storing. A store the
    /// run is charged minutes to write is a store the run stops writing to,
    /// which is the opposite of what a durable memory is for.
    ///
    /// # Errors
    ///
    /// Returns an error when Cognee is unreachable, refuses the document, or
    /// does not accept it within [`ENQUEUE_TIMEOUT`].
    pub(super) async fn remember(&self, text: &str, source: &str) -> Result<u64> {
        let id = point_id(&format!("{source}\n{text}"));
        let document = format!("# Durable memory\n\n{text}\n\nSource: {source}\n");
        self.enqueue(
            document,
            format!("memory-{id}.md"),
            BRAIN_DATASET,
            "math_agent_brain",
        )
        .await?;
        Ok(id)
    }

    /// Files one downloaded source in this project's library dataset.
    ///
    /// The library was on disk and nowhere else: `download_document` wrote
    /// `research/…` and `index_document` wrote a local literal-term index, so
    /// nothing a run gathered was reachable through `recall_memory` at all —
    /// while the prompts told every role that Cognee was the durable catalogue.
    /// A source is stored under the path it was written to and the URL it came
    /// from, so a hit names a file the reader can open.
    ///
    /// # Errors
    ///
    /// Returns an error when Cognee is unreachable, refuses the document, or
    /// does not accept it within [`ENQUEUE_TIMEOUT`].
    /// Files one downloaded source in this project's library as the bytes that
    /// arrived, not as the runtime's rendering of them.
    ///
    /// This used to send `readable::convert`'s Markdown, capped at 200,000
    /// characters. That made the library a copy of one converter's opinion:
    /// a PDF whose text layer would not extract reached Cognee as an error
    /// rather than as a paper, a long reference page arrived with its tail
    /// missing, and every structural cue the original carried — headings,
    /// tables, the reference list — was already flattened before the graph saw
    /// it. Cognee does its own extraction, so handing it the original bytes
    /// gives it more to work with than the runtime can, and costs the runtime
    /// nothing: the bytes are already in hand from the download.
    ///
    /// Two files go in one request. The source keeps its real name and content
    /// type; the card beside it carries the project, the workspace path, and
    /// the URL, because a chunk recalled from the graph has to be traceable to
    /// a file on disk. Without the card a recalled passage names no source, and
    /// a claim nobody can trace is worth less than no claim.
    ///
    /// # Errors
    ///
    /// Returns an error when Cognee is unreachable or refuses the upload.
    pub(super) async fn remember_source(
        &self,
        path: &str,
        url: &str,
        bytes: &[u8],
        content_type: Option<&str>,
    ) -> Result<()> {
        let card = format!(
            "# Source\n\nProject: {}\nPath: {path}\nURL: {url}\n\nThe document itself was \
             filed alongside this card as `{}`. Read `{path}` in the workspace for the \
             converted text.\n",
            self.project,
            source_file_name(path, content_type)
        );
        let card_part = reqwest::multipart::Part::bytes(card.into_bytes())
            .file_name(format!("source-{}.md", slug(path)))
            .mime_str("text/markdown")
            .map_err(|error| tinyagents::TinyAgentsError::Tool(error.to_string()))?;
        // The declared type is passed through when it is one Cognee can act
        // on, and sniffed otherwise. Servers mislabel routinely — the download
        // path already prefers magic bytes over the header for that reason —
        // so a mislabelled PDF must still arrive as a PDF.
        let mime = source_mime(bytes, content_type);
        let source_part = reqwest::multipart::Part::bytes(bytes.to_vec())
            .file_name(source_file_name(path, content_type))
            .mime_str(&mime)
            .map_err(|error| tinyagents::TinyAgentsError::Tool(error.to_string()))?;
        tokio::time::timeout(
            ENQUEUE_TIMEOUT,
            self.post_parts(
                vec![source_part, card_part],
                &self.library_dataset,
                &library_node_set(&self.project),
            ),
        )
        .await
        .map_err(|_| {
            tinyagents::TinyAgentsError::Tool(format!(
                "Cognee did not accept the source for `{}` within {} seconds",
                self.library_dataset,
                ENQUEUE_TIMEOUT.as_secs()
            ))
        })?
    }

    /// Queues one completed agent session in the current project/run dataset.
    pub(super) async fn remember_session(
        &self,
        agent: &str,
        run_id: &str,
        input: &str,
        output: &str,
    ) -> Result<()> {
        let document = format!(
            "# Agent session\n\nProject: {}\nSession: {}\nAgent: {agent}\nRun: {run_id}\n\n## Input\n\n{input}\n\n## Final output\n\n{output}\n",
            self.project, self.session
        );
        self.enqueue(
            document,
            format!("session-{}-{}.md", slug(agent), slug(run_id)),
            &self.session_dataset,
            &session_node_set(&self.project),
        )
        .await
    }

    /// Hands one document to Cognee for background indexing.
    ///
    /// Every store here goes through this, so the bound on how long a write may
    /// block is one number rather than one per caller. Indexing continues after
    /// this returns; what is bounded is the enqueue.
    async fn enqueue(
        &self,
        document: String,
        filename: String,
        dataset: &str,
        node_set: &str,
    ) -> Result<()> {
        tokio::time::timeout(
            ENQUEUE_TIMEOUT,
            self.ingest(document, filename, dataset, node_set),
        )
        .await
        .map_err(|_| {
            tinyagents::TinyAgentsError::Tool(format!(
                "Cognee did not accept the document for `{dataset}` within {} seconds",
                ENQUEUE_TIMEOUT.as_secs()
            ))
        })?
    }

    async fn ingest(
        &self,
        document: String,
        filename: String,
        dataset: &str,
        node_set: &str,
    ) -> Result<()> {
        let part = reqwest::multipart::Part::bytes(document.into_bytes())
            .file_name(filename)
            .mime_str("text/markdown")
            .map_err(|error| tinyagents::TinyAgentsError::Tool(error.to_string()))?;
        self.post_parts(vec![part], dataset, node_set).await
    }

    /// Posts one or more files to Cognee under one dataset and node set.
    ///
    /// `data` is a list on Cognee's side, and a source uses both slots: the
    /// original bytes, and a small card naming where they came from. Sending
    /// them in one request is what keeps the two from arriving separately —
    /// a card whose companion failed to upload would describe a document the
    /// library does not hold.
    async fn post_parts(
        &self,
        parts: Vec<reqwest::multipart::Part>,
        dataset: &str,
        node_set: &str,
    ) -> Result<()> {
        let mut form = reqwest::multipart::Form::new()
            .text("datasetName", dataset.to_string())
            .text("node_set", node_set.to_string())
            .text("run_in_background", "true");
        for part in parts {
            form = form.part("data", part);
        }
        let response = self
            .client
            .post(format!("{}/api/v1/remember", self.base_url))
            .multipart(form)
            .send()
            .await
            .map_err(|error| cognee_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(cognee_response_error("remember", response).await);
        }
        Ok(())
    }

    /// Returns shared brain/research datasets plus this project's session
    /// dataset, excluding every other project's.
    async fn recall_datasets(&self) -> Result<Vec<String>> {
        let datasets = self.list_datasets().await?;
        Ok(visible_datasets(
            &datasets,
            &self.session_dataset,
            &self.library_dataset,
        ))
    }

    /// Says whether Cognee holds a dataset under this name.
    async fn dataset_exists(&self, dataset: &str) -> Result<bool> {
        let datasets = self.list_datasets().await?;
        Ok(datasets
            .as_array()
            .into_iter()
            .flatten()
            .filter_map(|entry| entry.get("name").and_then(Value::as_str))
            .any(|name| name == dataset))
    }

    /// Returns Cognee's dataset listing verbatim.
    async fn list_datasets(&self) -> Result<Value> {
        let response = self
            .client
            .get(format!("{}/api/v1/datasets", self.base_url))
            .send()
            .await
            .map_err(|error| cognee_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(cognee_response_error("list datasets", response).await);
        }
        response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("Cognee returned invalid JSON: {error}"))
        })
    }
}

#[derive(Debug)]
pub(super) struct RememberMemoryTool {
    store: VectorStore,
}
