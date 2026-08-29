impl CortexStore {
    /// Builds the store from the environment the container was started with.
    ///
    /// # Errors
    ///
    /// Returns an error when `CORTEX_API_URL` or `CORTEX_API_KEY` is missing or
    /// empty, when the key cannot be sent as a header, or when the configured
    /// scope root is not a valid scope segment.
    pub(super) fn from_env() -> Result<Self> {
        let base_url = std::env::var("CORTEX_API_URL").map_err(|_| {
            tinyagents::TinyAgentsError::Validation("CORTEX_API_URL is required".into())
        })?;
        let base_url = base_url.trim_end_matches('/').to_string();
        if base_url.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "CORTEX_API_URL cannot be empty".into(),
            ));
        }
        let project =
            slug(&std::env::var("MATH_AGENT_WORKSPACE_LABEL").unwrap_or_else(|_| "default".into()));
        let client = authenticated_client(
            &std::env::var("CORTEX_API_KEY").map_err(|_| {
                tinyagents::TinyAgentsError::Validation(
                    "CORTEX_API_KEY is required: the memory server is shared and an unkeyed \
                     request is a `401` on every memory call"
                        .into(),
                )
            })?,
            &project,
        )?;
        let root = std::env::var("CORTEX_SCOPE_ROOT").unwrap_or_else(|_| DEFAULT_SCOPE_ROOT.into());
        let root = root.trim().trim_matches('/').to_string();
        if !root.contains(':') {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "CORTEX_SCOPE_ROOT=`{root}` is not a scope: a segment is `type:id`, so the root \
                 looks like `{DEFAULT_SCOPE_ROOT}`"
            )));
        }
        let nanos = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap_or_default()
            .as_nanos();
        // The run id identifies a run and belongs *inside* the document, the
        // same way it does for Cognee and for the same measured reason: when it
        // was part of the store's name instead, every restart opened a fresh
        // store and lost the session memory of every earlier run on the problem.
        // The scope is the project; the run is a field.
        let session = format!("s{nanos:x}-{}", std::process::id());
        Ok(Self {
            client,
            base_url,
            project,
            session,
            root,
            readiness: Arc::new(tokio::sync::Mutex::new(None)),
        })
    }

    /// The scope this project's three durable stores hang below.
    ///
    /// Nothing is ever written to it and no recall addresses it: reads name the
    /// child stores one at a time, for the reason [`CortexStore::search`]
    /// records. It exists to give the three a common parent, and to keep the
    /// scratch outside that parent. Built from [`CortexStore::project`] and
    /// nothing else, which is the whole of the cross-problem boundary — see
    /// this module's header for what that is and is not worth.
    fn durable_scope(&self) -> String {
        format!("{}/{PROJECT_SEGMENT}:{}", self.root, self.project)
    }

    /// The scope one durable store within this project occupies.
    fn store_scope(&self, store: &str) -> String {
        format!("{}/{store}", self.durable_scope())
    }

    /// The scope holding this project's provisional notes.
    ///
    /// A sibling of [`CortexStore::durable_scope`] rather than a child of it.
    /// What actually keeps it out of durable recall is that it is not in
    /// [`DURABLE_STORES`], which is the list every durable read is built from;
    /// the placement is the second line of defence, and stops a future reader
    /// who reaches for a subtree traversal from picking it up by accident.
    fn scratch_scope(&self) -> String {
        format!("{}/{SCRATCH_SEGMENT}:{}", self.root, self.project)
    }

    /// Runs one lookup against each of this project's durable stores and
    /// renders the hits under a heading each.
    ///
    /// **Three requests against three named leaf scopes, not one `descend`
    /// against their parent**, and that is a correction rather than a
    /// preference. `descend` is the server's own traversal of a scope's
    /// descendants, and it was the first thing tried here — it worked on the
    /// scope it was developed against and then, on a live run's workspace,
    /// returned **nothing at all** while the brain it should have reached held
    /// nineteen events that a `granular` recall addressed straight at it
    /// returned every time. The registry listed the brain as a registered
    /// scope throughout. Worse, the same `descend` returned three events for a
    /// *stranger's* actor and zero for the scope's own owner, so the result
    /// was not merely incomplete but incoherent.
    ///
    /// A durable recall that silently misses the brain is the failure this
    /// whole engine was chosen to end, so it must not rest on a traversal this
    /// runtime cannot predict. Naming the three scopes costs two extra
    /// requests, which run concurrently, and buys three things:
    ///
    /// - **The set of stores durable recall reads is a literal here**, so it
    ///   can be read, tested and audited rather than inferred from a server
    ///   policy — and [`DURABLE_STORES`] is that list.
    /// - **The scratch is excluded by never being named**, which is stronger
    ///   than being excluded by a traversal rule. Its sibling placement stays
    ///   as the second line of defence rather than the only one.
    /// - **No `scope.read.descend` capability is needed**, so this works on a
    ///   deployment whose policy stack does not grant it.
    ///
    /// One store failing is not a failed recall: a store that errors becomes a
    /// line saying so, and the others still answer. All three failing
    /// propagates the first error, because then there is nothing to return and
    /// silence would read as "nothing known".
    ///
    /// Returns `Ok(None)` when every store is empty, so each caller can say so
    /// in its own words rather than returning an empty result the model has to
    /// interpret.
    ///
    /// # Errors
    ///
    /// Returns an error when every store's lookup fails.
    pub(super) async fn search(
        &self,
        query: &str,
        lookup: Lookup,
        limit: u64,
    ) -> Result<Option<String>> {
        let budgets = store_budgets(limit);
        // Bound to locals: `join!` borrows each future for the whole await, and
        // a scope built inline is a temporary that would not outlive it.
        let scopes = DURABLE_STORES.map(|store| self.store_scope(store));
        let (brain, library, session) = tokio::join!(
            self.recall(&scopes[0], "granular", query, lookup, budgets[0]),
            self.recall(&scopes[1], "granular", query, lookup, budgets[1]),
            self.recall(&scopes[2], "granular", query, lookup, budgets[2]),
        );
        let found = [brain, library, session];
        let mut sections: Vec<String> = Vec::new();
        let mut failure: Option<tinyagents::TinyAgentsError> = None;
        for (store, outcome) in DURABLE_STORES.iter().zip(found) {
            match outcome {
                Ok(Some(rendered)) => {
                    sections.push(format!("## {}\n\n{rendered}", store_heading(store)));
                }
                Ok(None) => {}
                Err(error) => {
                    sections.push(format!(
                        "(The {} could not be read: {error}.)",
                        store_heading(store).to_lowercase()
                    ));
                    failure.get_or_insert(error);
                }
            }
        }
        // Every section a failure notice means nothing was actually recalled,
        // and a list of apologies reads as an answer. Propagate instead.
        if sections.len() == DURABLE_STORES.len()
            && let Some(error) = failure
            && sections.iter().all(|section| section.starts_with('('))
        {
            return Err(error);
        }
        Ok((!sections.is_empty()).then(|| sections.join("\n\n")))
    }

    /// Returns the provisional notes nearest a phrase, and nothing durable.
    ///
    /// `granular` rather than `descend`: the scratch is a leaf and has no
    /// children, and asking to descend from it would be asking for a traversal
    /// with nothing to traverse.
    ///
    /// # Errors
    ///
    /// Returns an error when `CortexDB` is unreachable or refuses the request.
    pub(super) async fn recall_scratch(&self, query: &str, limit: u64) -> Result<Option<String>> {
        self.recall(
            &self.scratch_scope(),
            "granular",
            query,
            Lookup::Passages,
            limit,
        )
        .await
    }

    /// Asks the server for one stratified pack and renders it.
    async fn recall(
        &self,
        scope: &str,
        view: &str,
        query: &str,
        lookup: Lookup,
        limit: u64,
    ) -> Result<Option<String>> {
        let include = layers(lookup);
        let per_layer = include
            .iter()
            .map(|layer| (singular(layer).to_string(), json!(limit)))
            .collect::<serde_json::Map<_, _>>();
        let body = json!({
            "scope": scope,
            "view": view,
            "query": query,
            "include": include,
            "budgets": { "per_layer_limits": per_layer },
            "citation_mode": "none",
        });
        let request = self
            .client
            .post(format!("{}/v1/recall", self.base_url))
            .json(&body)
            .send();
        let response = tokio::time::timeout(RECALL_TIMEOUT, request)
            .await
            .map_err(|_| {
                tinyagents::TinyAgentsError::Tool(format!(
                    "CortexDB did not answer a recall within {} seconds",
                    RECALL_TIMEOUT.as_secs()
                ))
            })?
            .map_err(|error| cortex_transport_error(&error))?;
        // A scope nothing has ever been written to is not an error. The server
        // reports it as an empty pack, but a deployment that answered `404`
        // would otherwise turn "this run has stored nothing yet" into a failed
        // tool call, which is the shape Cognee's missing-dataset `404` took.
        if response.status() == reqwest::StatusCode::NOT_FOUND {
            return Ok(None);
        }
        if !response.status().is_success() {
            return Err(cortex_response_error("recall", response).await);
        }
        let pack: Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("CortexDB returned invalid JSON: {error}"))
        })?;
        Ok(render_pack(&pack, lookup))
    }

    /// Stores one durable memory in this project's brain.
    ///
    /// Awaited to [`DURABLE_BARRIER`], so the call answers whether the finding
    /// is recallable rather than whether the server accepted the bytes. That is
    /// the correction of the failure that cost one workspace 193 findings, and
    /// it costs about five seconds a write.
    ///
    /// # Errors
    ///
    /// Returns an error when `CortexDB` is unreachable, cannot index, refuses the
    /// document, or does not store it within [`WRITE_TIMEOUT`].
    pub(super) async fn remember(&self, text: &str, source: &str) -> Result<u64> {
        let id = point_id(&format!("{source}\n{text}"));
        let document = format!("# Durable memory\n\n{text}\n\nSource: {source}\n");
        self.capture(
            &self.store_scope(BRAIN_STORE),
            "observation",
            json!({ "kind": "text", "text": document }),
            &["brain", &slug(source)],
            &format!("brain-{id:x}"),
            DURABLE_BARRIER,
        )
        .await?;
        Ok(id)
    }

    /// Records one provisional note in this project's scratch.
    ///
    /// Awaited only to [`SCRATCH_BARRIER`]; see that constant for the trade.
    ///
    /// # Errors
    ///
    /// Returns an error when `CortexDB` is unreachable, cannot index, or refuses
    /// the note.
    pub(super) async fn note_scratch(&self, text: &str, topic: &str) -> Result<u64> {
        let id = point_id(&format!("{topic}\n{text}"));
        let document = format!(
            "# Provisional note\n\nProject: {}\nSession: {}\nTopic: {topic}\n\n{text}\n",
            self.project, self.session
        );
        self.capture(
            &self.scratch_scope(),
            "observation",
            json!({ "kind": "text", "text": document }),
            &["scratch", &slug(topic)],
            &format!("scratch-{id:x}"),
            SCRATCH_BARRIER,
        )
        .await?;
        Ok(id)
    }

    /// Stores one completed agent session in this project's sessions.
    ///
    /// # Errors
    ///
    /// Returns an error when `CortexDB` is unreachable, cannot index, or refuses
    /// the document.
    pub(super) async fn remember_session(
        &self,
        agent: &str,
        run_id: &str,
        input: &str,
        output: &str,
    ) -> Result<()> {
        let document = format!(
            "# Agent session\n\nProject: {}\nSession: {}\nAgent: {agent}\nRun: {run_id}\n\n## \
             Input\n\n{input}\n\n## Final output\n\n{output}\n",
            self.project, self.session
        );
        self.capture(
            &self.store_scope(SESSION_STORE),
            "conversation",
            json!({ "kind": "text", "text": document }),
            &["session", &slug(agent)],
            &format!("session-{}-{}", slug(agent), slug(run_id)),
            DURABLE_BARRIER,
        )
        .await
        .map(|_| ())
    }

    /// Files one downloaded source in this project's library as the bytes that
    /// arrived.
    ///
    /// Two writes, and the order carries the guarantee. The blob goes first and
    /// carries the document itself: uploaded raw to `/v1/blobs`, then referenced
    /// from an envelope as `blob_ref`, which is what routes it through the
    /// server's own content processors rather than through this runtime's
    /// opinion of what the bytes say. The card goes second and names the
    /// workspace path and the URL, because a passage recalled out of a document
    /// has to be traceable to a file the reader can open.
    ///
    /// Cognee sent both in one multipart request, so neither could arrive
    /// alone. Here they cannot be atomic, so they are ordered instead: a failed
    /// blob writes no card, and a failed card leaves a source that is
    /// recallable but harder to trace. The degraded outcome is the recoverable
    /// one, which is why it is the one placed second.
    ///
    /// # Errors
    ///
    /// Returns an error when `CortexDB` is unreachable, cannot index, or refuses
    /// either write.
    pub(super) async fn remember_source(
        &self,
        path: &str,
        url: &str,
        bytes: &[u8],
        content_type: Option<&str>,
    ) -> Result<()> {
        let scope = self.store_scope(LIBRARY_STORE);
        let name = source_file_name(path, content_type);
        let blob = self.upload_blob(bytes, &source_mime(bytes, content_type)).await?;
        self.capture(
            &scope,
            "document",
            json!({ "kind": "blob_ref", "blob_id": blob }),
            &["library", &slug(path)],
            &format!("library-{}", slug(path)),
            DURABLE_BARRIER,
        )
        .await?;
        let card = format!(
            "# Source\n\nProject: {}\nPath: {path}\nURL: {url}\n\nThe document itself was filed \
             alongside this card as `{name}`. Read `{path}` in the workspace for the converted \
             text.\n",
            self.project
        );
        self.capture(
            &scope,
            "document",
            json!({ "kind": "text", "text": card }),
            &["library", "card", &slug(path)],
            &format!("library-card-{}", slug(path)),
            DURABLE_BARRIER,
        )
        .await
        .map(|_| ())
    }

    /// Uploads one source's bytes and returns the id an envelope references it
    /// by.
    ///
    /// The body *is* the file, with `Content-Type` declaring what it is:
    /// multipart is refused `415` rather than stored as boundary noise, which
    /// is worth knowing because multipart is exactly what the Cognee path sent.
    async fn upload_blob(&self, bytes: &[u8], mime: &str) -> Result<String> {
        self.refuse_if_degraded().await?;
        let request = self
            .client
            .post(format!("{}/v1/blobs", self.base_url))
            .header(reqwest::header::CONTENT_TYPE, mime)
            .body(bytes.to_vec())
            .send();
        let response = tokio::time::timeout(WRITE_TIMEOUT, request)
            .await
            .map_err(|_| {
                tinyagents::TinyAgentsError::Tool(format!(
                    "CortexDB did not accept the source within {} seconds",
                    WRITE_TIMEOUT.as_secs()
                ))
            })?
            .map_err(|error| cortex_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(cortex_response_error("blob upload", response).await);
        }
        let body: Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("CortexDB returned invalid JSON: {error}"))
        })?;
        body.get("blob_id")
            .and_then(Value::as_str)
            .map(ToOwned::to_owned)
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Tool(
                    "CortexDB stored the source but named no blob_id for it".into(),
                )
            })
    }

    /// Writes one experience and waits for the barrier named.
    ///
    /// Every store's write passes through here, so the bound on how long a
    /// write may block, the readiness refusal, and the reading of the server's
    /// per-stage answer are each in one place rather than four.
    async fn capture(
        &self,
        scope: &str,
        modality: &str,
        content: Value,
        labels: &[&str],
        idempotency_key: &str,
        barrier: &str,
    ) -> Result<String> {
        self.refuse_if_degraded().await?;
        let body = json!({
            "scope": scope,
            "modality": modality,
            "content": content,
            // No `observed_at`. It is optional and the server defaults it to
            // its own clock, which is the clock every bi-temporal query is
            // asked against — so supplying one from this container would be
            // introducing a second clock to disagree with, for nothing. Probed:
            // an envelope with labels and no `observed_at` is stored with both
            // `observed_at` and `recorded_at` set by the server.
            "context": { "labels": labels },
            // Bounded at 64 characters by the server, and a key reused with a
            // different body is a `409` rather than an overwrite. Every caller
            // derives it from the content, so a genuine rewrite gets a new key
            // and a genuine repeat is deduplicated.
            "idempotency_key": truncate_chars(idempotency_key, 64),
        });
        let request = self
            .client
            .post(format!("{}/v1/experience?wait={barrier}", self.base_url))
            .json(&body)
            .send();
        let response = tokio::time::timeout(WRITE_TIMEOUT, request)
            .await
            .map_err(|_| {
                tinyagents::TinyAgentsError::Tool(format!(
                    "CortexDB did not store the document for `{scope}` within {} seconds; write it \
                     to the workspace instead and store it once the memory recovers",
                    WRITE_TIMEOUT.as_secs()
                ))
            })?
            .map_err(|error| cortex_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(cortex_response_error("experience", response).await);
        }
        let body: Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("CortexDB returned invalid JSON: {error}"))
        })?;
        // The stage list is the point of waiting at all. A `200` naming stages
        // short of the barrier asked for is the server saying it stored
        // something it has not indexed, which is the one outcome this engine
        // exists to stop reporting as a success.
        reached_barrier(&body, barrier)?;
        Ok(body
            .get("event_id")
            .and_then(Value::as_str)
            .unwrap_or("unknown")
            .to_string())
    }

    /// Refuses a write the server would store and make unrecallable.
    ///
    /// A verdict stands for [`READY_TTL`] and the probe is bounded by
    /// [`READY_TIMEOUT`]. Unlike Cognee's equivalent this does *not* treat a
    /// slow probe as a refusal: the failure it guards is a configuration one
    /// the server reports instantly in a flag, not a hanging model check, so
    /// silence here carries no information and refusing on it would stop a
    /// memory that works.
    ///
    /// # Errors
    ///
    /// Returns an error when the server reports it is not ready, or is pinned
    /// to mock embeddings.
    async fn refuse_if_degraded(&self) -> Result<()> {
        let mut cached = self.readiness.lock().await;
        let fresh = match cached.as_ref() {
            Some((taken, verdict)) if taken.elapsed() < READY_TTL => verdict.clone(),
            _ => {
                let verdict = self.probe_readiness().await;
                *cached = Some((Instant::now(), verdict.clone()));
                verdict
            }
        };
        match fresh {
            Readiness::Ready => Ok(()),
            Readiness::Refusing(detail) => Err(tinyagents::TinyAgentsError::Tool(format!(
                "the memory server cannot store anything recallable right now, so this document \
                 would be kept and never found again: {detail}. Write it to the workspace instead \
                 and store it once the memory recovers"
            ))),
        }
    }

    /// Asks the server whether it is ready, and reads the answer as a verdict.
    ///
    /// Never fails: an unreachable server is already reported by the write that
    /// follows, and turning a probe's transport error into a refusal would stop
    /// writes for a reason the write itself has not met yet.
    async fn probe_readiness(&self) -> Readiness {
        let request = self
            .client
            .get(format!("{}/v1/admin/ready", self.base_url))
            .send();
        let Ok(Ok(response)) = tokio::time::timeout(READY_TIMEOUT, request).await else {
            return Readiness::Ready;
        };
        // A `503` carries the same body shape as a `200` and is the readiness
        // answer rather than a failed request, so the body is read either way.
        let Ok(body) = response.json::<Value>().await else {
            return Readiness::Ready;
        };
        readiness(&body)
    }
}
