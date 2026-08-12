//! Cognee-backed durable brain, project-scoped session memory, and the run's
//! provisional scratch.
//!
//! Three stores, and the separation between them is the point. The brain holds
//! what survived checking and every project reads it. The session dataset holds
//! this project's completed agent runs. The *scratch* holds the half-finished
//! arithmetic a run produces on the way to a result — what `SCRATCHPAD.md` used
//! to be — and it is deliberately not reachable from `recall_memory` or
//! `relate_memory`: provisional work is not durable knowledge, and a
//! half-finished calculation surfacing as one is how a run comes to believe
//! something nobody verified. It is also not the knowledge graph. The graph
//! answers what the run's entities are connected to; the scratch answers what
//! this run was in the middle of, which no amount of graph traversal recovers.

use async_trait::async_trait;
use serde_json::{Value, json};
use std::time::Duration;

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

const BRAIN_DATASET: &str = "math_agent_brain";
const SESSION_DATASET_PREFIX: &str = "math_agent_sessions__";

/// The prefix of the per-project dataset holding provisional work.
///
/// Scoped to the *project* rather than the run, for the reason recorded on
/// [`VectorStore::from_env`]: `./euler 763` continues from what is on disk, and
/// a scratch that vanished on restart would be worse than the file it replaces.
const SCRATCH_DATASET_PREFIX: &str = "math_agent_scratch__";

/// The prefix of the per-project dataset holding the downloaded library.
///
/// Scoped to the project because a source is fetched to answer *this* problem:
/// another run's library is a different subject, and reading it is how a run
/// meets a paper nobody here asked for. The brain stays shared; the sources do
/// not.
const LIBRARY_DATASET_PREFIX: &str = "math_agent_library__";

/// The node set every durable brain document is ingested under.
const BRAIN_NODE_SET: &str = "math_agent_brain";

/// The prefix of the node set this project's completed sessions carry.
const SESSION_NODE_SET_PREFIX: &str = "project:";

/// The prefix of the node set this project's provisional notes carry.
const SCRATCH_NODE_SET_PREFIX: &str = "scratch:";

/// The prefix of the node set this project's downloaded sources carry.
const LIBRARY_NODE_SET_PREFIX: &str = "library:";

/// Cognee's search type for the passages nearest a phrase.
const CHUNK_SEARCH: &str = "CHUNKS";

/// Cognee's search type for the edges the graph holds around a subject.
///
/// It was `INSIGHTS`, which this server rejects outright — the enum it accepts
/// has no such member, so every `relate_memory` call ever made returned a 422
/// naming the eighteen types it does accept, and the graph half of the memory
/// has never answered anything. `GRAPH_COMPLETION` is the surviving name for
/// the same question: it retrieves the nodes and edges around the query and
/// renders them, and with `only_context` set it returns that context rather
/// than a model's prose about it.
const GRAPH_SEARCH: &str = "GRAPH_COMPLETION";

/// The most of a source that is handed to Cognee.
///
/// A converted reference page reaches 91,190 characters and a paper more, and
/// what recall returns is a chunk either way. The cap bounds one multipart
/// request rather than what the library may hold, and the whole text stays on
/// disk beside the digest, which is where a reader who needs all of it goes.
const MAX_SOURCE_CHARS: usize = 200_000;

/// How long a write may spend enqueueing before the caller is told it failed.
///
/// Every ingest here is backgrounded, so this bounds the *enqueue* and not the
/// indexing. It exists because a hung Cognee must not become a hung agent: a
/// live `remember_memory` ran into the ten-minute tool ceiling and the finding
/// it carried — a falsified conjecture — was lost with it.
const ENQUEUE_TIMEOUT: Duration = Duration::from_secs(30);

#[derive(Clone, Debug)]
pub(super) struct VectorStore {
    client: reqwest::Client,
    base_url: String,
    project: String,
    session: String,
    session_dataset: String,
    scratch_dataset: String,
    library_dataset: String,
}

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
    pub(super) async fn remember_source(&self, path: &str, url: &str, text: &str) -> Result<()> {
        let document = format!(
            "# Source\n\nProject: {}\nPath: {path}\nURL: {url}\n\n{}\n",
            self.project,
            truncate_chars(text, MAX_SOURCE_CHARS)
        );
        self.enqueue(
            document,
            format!("source-{}.md", slug(path)),
            &self.library_dataset,
            &library_node_set(&self.project),
        )
        .await
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
        let response = self
            .client
            .post(format!("{}/api/v1/remember", self.base_url))
            .multipart(
                reqwest::multipart::Form::new()
                    .text("datasetName", dataset.to_string())
                    .text("node_set", node_set.to_string())
                    .text("run_in_background", "true")
                    .part("data", part),
            )
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

impl RememberMemoryTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RememberMemoryTool {
    fn name(&self) -> &'static str {
        "remember_memory"
    }

    fn description(&self) -> &'static str {
        "Stores a concise durable finding, lesson, decision, or failed approach in Cognee."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "A self-contained memory worth reusing across agents and runs."
                    },
                    "source": {
                        "type": "string",
                        "description": "A source URL, agent name, or short provenance label."
                    }
                },
                "required": ["text", "source"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let text = string_argument(&call, "text")?;
        let source = string_argument(&call, "source")?;
        let id = self.store.remember(&text, &source).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("stored research note {id} from {source}"),
        ))
    }
}

#[derive(Debug)]
pub(super) struct RecallMemoryTool {
    store: VectorStore,
}

impl RecallMemoryTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RecallMemoryTool {
    fn name(&self) -> &'static str {
        "recall_memory"
    }

    fn description(&self) -> &'static str {
        "Recalls shared durable findings and research plus session memory from this project/run only."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string" },
                    "limit": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "default": 5
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = string_argument(&call, "query")?;
        let limit = limit_argument(&call);
        let rendered = self.store.search(&query, CHUNK_SEARCH, limit).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            rendered.unwrap_or_else(|| "no related research notes found".to_string()),
        ))
    }
}

/// Asks the memory what its entities are connected to, rather than which
/// passages mention them.
///
/// This is the one thing a graph memory can answer that a vector store cannot.
/// `recall_memory` returns the chunks most similar to a phrase, which is a
/// better index than a filename and no more; `relate_memory` returns the edges
/// the graph actually holds, so "what does this run connect the Moore bound to"
/// has an answer that nobody wrote down in those words. A run that only ever
/// recalls chunks is paying for a graph store and using it as a search box.
#[derive(Debug)]
pub(super) struct RelateMemoryTool {
    store: VectorStore,
}

impl RelateMemoryTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RelateMemoryTool {
    fn name(&self) -> &'static str {
        "relate_memory"
    }

    fn description(&self) -> &'static str {
        "Returns what this project's memory connects a subject to — the relationships between \
         entities rather than the passages mentioning them. Use it to find a link the run \
         established but never stated in one place; use recall_memory when you want the text."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string" },
                    "limit": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "default": 5
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = string_argument(&call, "query")?;
        let limit = limit_argument(&call);
        let rendered = self.store.search(&query, GRAPH_SEARCH, limit).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            rendered.unwrap_or_else(|| {
                "the memory holds no connections for that subject yet".to_string()
            }),
        ))
    }
}

/// Writes one provisional note where `SCRATCHPAD.md` used to be written.
///
/// The file was in three roles' system prompts, so every model call in each of
/// them paid for every number anyone had jotted down, whether or not the turn
/// was about it — and it was re-read whole to add a line. A note is written
/// once and read back by wording, which is the same trade `remember_memory`
/// makes for durable findings.
///
/// It is a separate tool rather than a flag on `remember_memory` because the
/// distinction is the one the method policy rests on. A durable memory is
/// something the run checked; a scratch note is something it has not. Sharing a
/// tool between them would leave which store a statement landed in decided by
/// an argument, mid-derivation, by the role least able to judge it.
#[derive(Debug)]
pub(super) struct NoteScratchTool {
    store: VectorStore,
}

impl NoteScratchTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for NoteScratchTool {
    fn name(&self) -> &'static str {
        "note_scratch"
    }

    fn description(&self) -> &'static str {
        "Records provisional work — a partial derivation, an intermediate number, a hypothesis \
         not yet checked — in this project's scratch. Nothing here is evidence: once a finding \
         survives a check, store it with remember_memory instead."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The provisional work, self-contained enough to be read back later."
                    },
                    "topic": {
                        "type": "string",
                        "description": "A few words naming what the note is about, so it can be recalled."
                    }
                },
                "required": ["text", "topic"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let text = string_argument(&call, "text")?;
        let topic = string_argument(&call, "topic")?;
        let id = self.store.note_scratch(&text, &topic).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("noted provisional work {id} on {topic}"),
        ))
    }
}

/// Reads the run's provisional work back, and nothing else.
#[derive(Debug)]
pub(super) struct RecallScratchTool {
    store: VectorStore,
}

impl RecallScratchTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RecallScratchTool {
    fn name(&self) -> &'static str {
        "recall_scratch"
    }

    fn description(&self) -> &'static str {
        "Returns this project's provisional notes nearest a phrase — unfinished work, not \
         established results. Use recall_memory for what the run has actually checked."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string" },
                    "limit": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "default": 5
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = string_argument(&call, "query")?;
        let limit = limit_argument(&call);
        let rendered = self.store.recall_scratch(&query, limit).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            rendered.unwrap_or_else(|| "no provisional notes on that yet".to_string()),
        ))
    }
}

/// Reads the shared `limit` argument, clamped to what a prompt can afford.
fn limit_argument(call: &ToolCall) -> u64 {
    call.arguments
        .get("limit")
        .and_then(Value::as_u64)
        .unwrap_or(5)
        .clamp(1, 10)
}

fn string_argument(call: &ToolCall, name: &str) -> Result<String> {
    call.arguments
        .get(name)
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .map(ToOwned::to_owned)
        .ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("{name} must be a non-empty string"))
        })
}

fn point_id(text: &str) -> u64 {
    fnv1a(text.as_bytes())
}

fn slug(value: &str) -> String {
    let slug = value
        .chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() {
                character.to_ascii_lowercase()
            } else {
                '_'
            }
        })
        .collect::<String>();
    let slug = slug.trim_matches('_');
    if slug.is_empty() {
        "default".into()
    } else {
        slug.to_string()
    }
}

/// The node set this project's completed agent sessions are written under.
fn session_node_set(project: &str) -> String {
    format!("{SESSION_NODE_SET_PREFIX}{project}")
}

/// The node set this project's provisional notes are written under.
fn scratch_node_set(project: &str) -> String {
    format!("{SCRATCH_NODE_SET_PREFIX}{project}")
}

/// The node set this project's downloaded sources are written under.
fn library_node_set(project: &str) -> String {
    format!("{LIBRARY_NODE_SET_PREFIX}{project}")
}

/// The node sets durable recall may read: the shared brain, plus this
/// project's completed sessions and its library.
///
/// This is the scoping that the server actually applies, so it is the one the
/// separation between the three stores now rests on — see
/// [`VectorStore::search_in`]. Every writer builds its `node_set` through the
/// helpers above and this reader consumes the same ones, because a writer and
/// a reader spelling the same scope apart is a leak nothing would report: the
/// documents would simply be filed where recall never looks.
///
/// The scratch is deliberately absent, for the reason [`visible_datasets`]
/// records: provisional arithmetic returned by durable recall is how a run
/// comes to believe something nobody checked. [`VectorStore::recall_scratch`]
/// is the only way in, and it names [`scratch_node_set`] alone.
fn durable_node_sets(project: &str) -> Vec<String> {
    vec![
        BRAIN_NODE_SET.to_string(),
        session_node_set(project),
        library_node_set(project),
    ]
}

/// Picks the datasets one run may read: the shared brain, plus this project's
/// own session memory and library, and nothing else.
///
/// An allowlist rather than a denylist, and that is the correction of a
/// measured leak. The rule used to be "everything except another project's
/// sessions and any scratch", which passes anything a name does not classify —
/// so a live server carrying `project_euler_903_L0`, thirty-six sources an
/// earlier build had ingested, was searched by every run on the box. For a
/// Project Euler problem that is another problem's literature arriving
/// unasked, and at worst its answer. A dataset this runtime does not recognise
/// belongs to another project or an older build, and neither is this run's.
///
/// A session dataset belongs to this project when it *is* this project's
/// dataset, or when it is one of the per-run datasets an older build created
/// underneath it — `<project>__s<nanos>-<pid>`. Matching those too is what lets
/// a run reach the session memory of every earlier run on the same problem
/// instead of only its own, and it recovers the datasets already stranded by
/// the old naming.
///
/// The `__` in the prefix test is load-bearing: without it, project `euler_18`
/// would read `euler_185`'s memory.
///
/// No scratch dataset is ever visible here, not even this project's own. The
/// scratch holds arithmetic that has not survived anything yet, and durable
/// recall returning it would restate the mistake `role_context` was built to
/// avoid: provisional work read as evidence of progress. `recall_scratch` is
/// the only way in, and only the roles doing provisional work hold it.
fn visible_datasets(datasets: &Value, current_session: &str, library: &str) -> Vec<String> {
    let owned_session = format!("{current_session}__");
    datasets
        .as_array()
        .into_iter()
        .flatten()
        .filter_map(|dataset| dataset.get("name").and_then(Value::as_str))
        .filter(|name| {
            *name == BRAIN_DATASET
                || *name == library
                || *name == current_session
                || name.starts_with(&owned_session)
        })
        .map(ToOwned::to_owned)
        .collect()
}

fn fnv1a(bytes: &[u8]) -> u64 {
    bytes.iter().fold(0xcbf2_9ce4_8422_2325, |hash, byte| {
        (hash ^ u64::from(*byte)).wrapping_mul(0x0000_0100_0000_01b3)
    })
}

/// Renders both Cognee's plain chunk results and richer result objects.
fn render_result(value: &Value) -> String {
    match value {
        Value::String(text) => text.clone(),
        _ => serde_json::to_string_pretty(value).unwrap_or_else(|_| value.to_string()),
    }
}

fn cognee_transport_error(error: &reqwest::Error) -> tinyagents::TinyAgentsError {
    tinyagents::TinyAgentsError::Tool(format!("Cognee request failed: {error}"))
}

async fn cognee_response_error(
    operation: &str,
    response: reqwest::Response,
) -> tinyagents::TinyAgentsError {
    let status = response.status();
    let body = response
        .text()
        .await
        .unwrap_or_else(|_| "unreadable response".into());
    tinyagents::TinyAgentsError::Tool(format!(
        "Cognee {operation} returned {status}: {}",
        truncate_chars(&body, 2_000)
    ))
}

fn truncate_chars(text: &str, limit: usize) -> String {
    let mut chars = text.chars();
    let kept = chars.by_ref().take(limit).collect::<String>();
    if chars.next().is_some() {
        format!("{kept}…")
    } else {
        kept
    }
}

#[cfg(test)]
mod test {
    use serde_json::json;

    use super::{
        durable_node_sets, library_node_set, point_id, render_result, scratch_node_set,
        session_node_set, slug, visible_datasets,
    };

    #[test]
    fn point_ids_are_deterministic() {
        assert_eq!(point_id("same note"), point_id("same note"));
        assert_ne!(point_id("same note"), point_id("different note"));
    }

    #[test]
    fn cognee_results_render_strings_and_structured_context() {
        assert_eq!(render_result(&json!("plain context")), "plain context");
        let rendered = render_result(&json!({"text": "context", "score": 0.9}));
        assert!(rendered.contains("context"));
        assert!(rendered.contains("0.9"));
    }

    /// This project's library, named the way `VectorStore::from_env` names it.
    const LIBRARY: &str = "math_agent_library__project_euler_903";

    #[test]
    fn session_recall_is_limited_to_the_current_project_run() {
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": LIBRARY},
            {"name": "math_agent_sessions__project_euler_903__current"},
            {"name": "math_agent_sessions__project_euler_904__other"}
        ]);
        assert_eq!(
            visible_datasets(
                &datasets,
                "math_agent_sessions__project_euler_903__current",
                LIBRARY
            ),
            vec![
                "math_agent_brain",
                LIBRARY,
                "math_agent_sessions__project_euler_903__current"
            ]
        );
        assert_eq!(slug("project-euler/903"), "project_euler_903");
        assert_eq!(slug("---"), "default");
    }

    #[test]
    fn an_unrecognised_dataset_is_not_this_run_s_to_read() {
        // A live server carried `project_euler_903_L0` — thirty-six sources an
        // earlier build ingested — and the old denylist passed it, so every
        // run on the box searched another problem's literature. Anything this
        // runtime does not name belongs to another project or an older build.
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": "project_euler_903_L0"},
            {"name": "math_agent_library__project_euler_763"},
            {"name": "something_a_person_uploaded"},
            {"name": "math_agent_library__project_euler_185"},
            {"name": "math_agent_sessions__project_euler_185"}
        ]);
        assert_eq!(
            visible_datasets(
                &datasets,
                "math_agent_sessions__project_euler_185",
                "math_agent_library__project_euler_185"
            ),
            vec![
                "math_agent_brain",
                "math_agent_library__project_euler_185",
                "math_agent_sessions__project_euler_185"
            ]
        );
    }

    #[test]
    fn a_rerun_of_the_same_problem_reuses_its_dataset_and_reaches_earlier_runs() {
        // The dataset used to carry the run id — nanoseconds and a pid — so
        // every restart opened a new one and could see only itself. One problem
        // restarted eight times left eight datasets, seven unreachable. The
        // name is now the project, and the per-run datasets an older build
        // stranded underneath it are readable again.
        let ours = "math_agent_sessions__project_euler_185";
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": "math_agent_sessions__project_euler_185"},
            {"name": "math_agent_sessions__project_euler_185__s18cb030630d9e2be-1"},
            {"name": "math_agent_sessions__project_euler_185__s18cb0306ffffffff-9"},
            {"name": "math_agent_sessions__project_euler_763"}
        ]);
        let visible = visible_datasets(&datasets, ours, "math_agent_library__project_euler_185");
        assert!(visible.contains(&ours.to_string()));
        assert!(visible.contains(&"math_agent_brain".to_string()));
        assert!(
            visible.contains(&format!("{ours}__s18cb030630d9e2be-1")),
            "a run must reach the session memory of earlier runs on the same problem"
        );
        assert!(
            !visible.contains(&"math_agent_sessions__project_euler_763".to_string()),
            "another problem's session memory must stay out"
        );
    }

    #[test]
    fn provisional_work_never_reaches_durable_recall() {
        // The scratch replaces SCRATCHPAD.md, and the file was withheld from
        // reflection on purpose: unsettled arithmetic is not evidence of
        // progress, and a loop that reads it as such keeps retrying. Durable
        // recall must therefore not reach the scratch even for this project —
        // `recall_scratch` is the only way in.
        let ours = "math_agent_sessions__project_euler_185";
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": "math_agent_sessions__project_euler_185"},
            {"name": "math_agent_scratch__project_euler_185"},
            {"name": "math_agent_scratch__project_euler_763"}
        ]);
        let visible = visible_datasets(&datasets, ours, "math_agent_library__project_euler_185");
        assert_eq!(
            visible,
            vec!["math_agent_brain", "math_agent_sessions__project_euler_185"]
        );
    }

    #[test]
    fn a_shorter_project_name_does_not_swallow_a_longer_one() {
        // `euler_18` is a prefix of `euler_185`, so the ownership test has to
        // require the `__` separator or one problem reads another's memory.
        let datasets = json!([
            {"name": "math_agent_sessions__euler_18"},
            {"name": "math_agent_sessions__euler_185"},
            {"name": "math_agent_sessions__euler_18__s1-2"}
        ]);
        let visible = visible_datasets(
            &datasets,
            "math_agent_sessions__euler_18",
            "math_agent_library__euler_18",
        );
        assert!(visible.contains(&"math_agent_sessions__euler_18".to_string()));
        assert!(visible.contains(&"math_agent_sessions__euler_18__s1-2".to_string()));
        assert!(
            !visible.contains(&"math_agent_sessions__euler_185".to_string()),
            "euler_18 must not read euler_185's memory"
        );
    }

    #[test]
    fn durable_recall_reads_the_brain_and_this_project_only() {
        let ours = durable_node_sets("project_euler_185");
        assert!(ours.contains(&"math_agent_brain".to_string()));
        assert!(ours.contains(&session_node_set("project_euler_185")));
        assert!(ours.contains(&library_node_set("project_euler_185")));
        assert!(
            !ours.contains(&session_node_set("project_euler_763")),
            "one problem must not read another's sessions"
        );
    }

    #[test]
    fn durable_recall_never_reaches_the_scratch() {
        // The separation the three stores rest on. It used to hold because
        // `visible_datasets` omitted the scratch dataset; the server does not
        // apply the dataset filter, so it holds here or nowhere.
        let project = "project_euler_185";
        assert!(
            !durable_node_sets(project).contains(&scratch_node_set(project)),
            "provisional arithmetic must not come back as durable knowledge"
        );
    }

    #[test]
    fn a_writer_and_a_reader_spell_each_scope_the_same_way() {
        // A leak nothing would report: documents filed under a node set recall
        // never names are simply unreachable, and the store reads as empty.
        let project = "conjectures_erdos_gyarfas";
        assert_eq!(session_node_set(project), format!("project:{project}"));
        assert_eq!(scratch_node_set(project), format!("scratch:{project}"));
        assert_eq!(library_node_set(project), format!("library:{project}"));
    }

    #[test]
    fn a_shorter_project_name_does_not_swallow_a_longer_one_in_node_sets() {
        // The same failure `visible_datasets` guards against, one layer down:
        // node-set matching is exact, so a prefix cannot widen the scope.
        assert_ne!(session_node_set("euler_18"), session_node_set("euler_185"));
        assert!(!durable_node_sets("euler_18").contains(&session_node_set("euler_185")));
    }
}
