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

#[derive(Clone, Debug)]
pub(super) struct VectorStore {
    client: reqwest::Client,
    base_url: String,
    project: String,
    session: String,
    session_dataset: String,
    scratch_dataset: String,
}

impl VectorStore {
    /// Runs one search against this project's datasets and renders the hits.
    ///
    /// `search_type` is Cognee's: `CHUNKS` for passages, `INSIGHTS` for the
    /// relationships between entities. Both tools share this because the only
    /// thing that differs between them is that string, and a second copy of the
    /// request would drift from the first the moment either is corrected.
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
        self.search_in(datasets, query, search_type, limit).await
    }

    /// Runs one search against exactly the datasets named.
    ///
    /// Split from [`VectorStore::search`] so the scratch can be read without
    /// being listed among the datasets durable recall reaches. Sharing the
    /// request is what keeps a correction to one from drifting from the other.
    ///
    /// # Errors
    ///
    /// Returns an error when Cognee is unreachable, refuses the request, or
    /// answers with something other than a JSON array.
    async fn search_in(
        &self,
        datasets: Vec<String>,
        query: &str,
        search_type: &str,
        limit: u64,
    ) -> Result<Option<String>> {
        if datasets.is_empty() {
            return Ok(None);
        }
        let response = self
            .client
            .post(format!("{}/api/v1/recall", self.base_url))
            .json(&json!({
                "query": query,
                "datasets": datasets,
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
        Ok(Self {
            client: reqwest::Client::new(),
            base_url,
            project,
            session,
            session_dataset,
            scratch_dataset,
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
        self.ingest(
            document,
            format!("scratch-{}-{id}.md", slug(topic)),
            &self.scratch_dataset,
            &format!("scratch:{}", self.project),
            true,
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
        self.search_in(vec![self.scratch_dataset.clone()], query, "CHUNKS", limit)
            .await
    }

    /// Adds one durable Markdown memory and waits until Cognee has indexed it.
    pub(super) async fn remember(&self, text: &str, source: &str) -> Result<u64> {
        let id = point_id(&format!("{source}\n{text}"));
        let document = format!("# Durable memory\n\n{text}\n\nSource: {source}\n");
        self.ingest(
            document,
            format!("memory-{id}.md"),
            BRAIN_DATASET,
            "math_agent_brain",
            false,
        )
        .await?;
        Ok(id)
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
        tokio::time::timeout(
            Duration::from_secs(30),
            self.ingest(
                document,
                format!("session-{}-{}.md", slug(agent), slug(run_id)),
                &self.session_dataset,
                &format!("project:{}", self.project),
                true,
            ),
        )
        .await
        .map_err(|_| {
            tinyagents::TinyAgentsError::Tool(
                "Cognee session-memory enqueue timed out after 30 seconds".into(),
            )
        })?
    }

    async fn ingest(
        &self,
        document: String,
        filename: String,
        dataset: &str,
        node_set: &str,
        background: bool,
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
                    .text("run_in_background", background.to_string())
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
        let response = self
            .client
            .get(format!("{}/api/v1/datasets", self.base_url))
            .send()
            .await
            .map_err(|error| cognee_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(cognee_response_error("list datasets", response).await);
        }
        let datasets: Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("Cognee returned invalid JSON: {error}"))
        })?;
        Ok(visible_datasets(&datasets, &self.session_dataset))
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
        let rendered = self.store.search(&query, "CHUNKS", limit).await?;
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
        let rendered = self.store.search(&query, "INSIGHTS", limit).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            rendered.unwrap_or_else(|| {
                "the memory holds no connections for that subject yet".to_string()
            }),
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

/// Picks the datasets one run may read: everything shared, plus this project's
/// own session memory and no other project's.
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
fn visible_datasets(datasets: &Value, current_session: &str) -> Vec<String> {
    let owned_prefix = format!("{current_session}__");
    datasets
        .as_array()
        .into_iter()
        .flatten()
        .filter_map(|dataset| dataset.get("name").and_then(Value::as_str))
        .filter(|name| !name.starts_with(SCRATCH_DATASET_PREFIX))
        .filter(|name| {
            !name.starts_with(SESSION_DATASET_PREFIX)
                || *name == current_session
                || name.starts_with(&owned_prefix)
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

    use super::{point_id, render_result, slug, visible_datasets};

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

    #[test]
    fn session_recall_is_limited_to_the_current_project_run() {
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": "project_euler_903_L0"},
            {"name": "math_agent_sessions__project_euler_903__current"},
            {"name": "math_agent_sessions__project_euler_904__other"}
        ]);
        assert_eq!(
            visible_datasets(&datasets, "math_agent_sessions__project_euler_903__current"),
            vec![
                "math_agent_brain",
                "project_euler_903_L0",
                "math_agent_sessions__project_euler_903__current"
            ]
        );
        assert_eq!(slug("project-euler/903"), "project_euler_903");
        assert_eq!(slug("---"), "default");
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
            {"name": "project_euler_185_L0"},
            {"name": "math_agent_sessions__project_euler_185"},
            {"name": "math_agent_sessions__project_euler_185__s18cb030630d9e2be-1"},
            {"name": "math_agent_sessions__project_euler_185__s18cb0306ffffffff-9"},
            {"name": "math_agent_sessions__project_euler_763"}
        ]);
        let visible = visible_datasets(&datasets, ours);
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
    fn a_shorter_project_name_does_not_swallow_a_longer_one() {
        // `euler_18` is a prefix of `euler_185`, so the ownership test has to
        // require the `__` separator or one problem reads another's memory.
        let datasets = json!([
            {"name": "math_agent_sessions__euler_18"},
            {"name": "math_agent_sessions__euler_185"},
            {"name": "math_agent_sessions__euler_18__s1-2"}
        ]);
        let visible = visible_datasets(&datasets, "math_agent_sessions__euler_18");
        assert!(visible.contains(&"math_agent_sessions__euler_18".to_string()));
        assert!(visible.contains(&"math_agent_sessions__euler_18__s1-2".to_string()));
        assert!(
            !visible.contains(&"math_agent_sessions__euler_185".to_string()),
            "euler_18 must not read euler_185's memory"
        );
    }
}
