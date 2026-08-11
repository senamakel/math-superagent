//! Qdrant-backed research notes with deterministic local embeddings.

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

const COLLECTION: &str = "math_agent_research";
const VECTOR_SIZE: usize = 256;

#[derive(Clone, Debug)]
pub(super) struct VectorStore {
    client: reqwest::Client,
    base_url: String,
}

impl VectorStore {
    pub(super) fn from_env() -> Result<Self> {
        let base_url = std::env::var("QDRANT_URL").map_err(|_| {
            tinyagents::TinyAgentsError::Validation("QDRANT_URL is required".into())
        })?;
        let base_url = base_url.trim_end_matches('/').to_string();
        if base_url.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "QDRANT_URL cannot be empty".into(),
            ));
        }
        Ok(Self {
            client: reqwest::Client::new(),
            base_url,
        })
    }

    async fn ensure_collection(&self) -> Result<()> {
        let url = format!("{}/collections/{COLLECTION}", self.base_url);
        let status = self
            .client
            .get(&url)
            .send()
            .await
            .map_err(|error| qdrant_transport_error(&error))?
            .status();
        if status.is_success() {
            return Ok(());
        }
        if status != reqwest::StatusCode::NOT_FOUND {
            return Err(tinyagents::TinyAgentsError::Tool(format!(
                "Qdrant collection check returned {status}"
            )));
        }

        let response = self
            .client
            .put(url)
            .json(&json!({
                "vectors": {
                    "size": VECTOR_SIZE,
                    "distance": "Cosine"
                }
            }))
            .send()
            .await
            .map_err(|error| qdrant_transport_error(&error))?;
        if collection_now_exists(response.status()) {
            return Ok(());
        }
        Err(qdrant_response_error("collection creation", response).await)
    }
}

#[derive(Debug)]
pub(super) struct RememberResearchTool {
    store: VectorStore,
}

impl RememberResearchTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RememberResearchTool {
    fn name(&self) -> &'static str {
        "remember_research"
    }

    fn description(&self) -> &'static str {
        "Stores a concise research finding and its source URL in the local vector database."
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
                        "description": "A self-contained finding worth reusing."
                    },
                    "source": {
                        "type": "string",
                        "description": "The source URL or a short provenance label."
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
        self.store.ensure_collection().await?;
        let id = point_id(&format!("{source}\n{text}"));
        let response = self
            .store
            .client
            .put(format!(
                "{}/collections/{COLLECTION}/points?wait=true",
                self.store.base_url
            ))
            .json(&json!({
                "points": [{
                    "id": id,
                    "vector": embed(&text),
                    "payload": {
                        "text": text,
                        "source": source
                    }
                }]
            }))
            .send()
            .await
            .map_err(|error| qdrant_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(qdrant_response_error("point upsert", response).await);
        }
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("stored research note {id} from {source}"),
        ))
    }
}

#[derive(Debug)]
pub(super) struct RecallResearchTool {
    store: VectorStore,
}

impl RecallResearchTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RecallResearchTool {
    fn name(&self) -> &'static str {
        "recall_research"
    }

    fn description(&self) -> &'static str {
        "Finds related prior research notes in the local vector database."
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
        let limit = call
            .arguments
            .get("limit")
            .and_then(Value::as_u64)
            .unwrap_or(5)
            .clamp(1, 10);
        self.store.ensure_collection().await?;
        let response = self
            .store
            .client
            .post(format!(
                "{}/collections/{COLLECTION}/points/query",
                self.store.base_url
            ))
            .json(&json!({
                "query": embed(&query),
                "limit": limit,
                "with_payload": true
            }))
            .send()
            .await
            .map_err(|error| qdrant_transport_error(&error))?;
        if !response.status().is_success() {
            return Err(qdrant_response_error("vector query", response).await);
        }
        let body: Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("Qdrant returned invalid JSON: {error}"))
        })?;
        let points = body
            .pointer("/result/points")
            .and_then(Value::as_array)
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Tool(
                    "Qdrant query response contained no points array".into(),
                )
            })?;
        if points.is_empty() {
            return Ok(ToolResult::text(
                call.id,
                self.name(),
                "no related research notes found",
            ));
        }
        let rendered = points
            .iter()
            .enumerate()
            .map(|(index, point)| {
                let score = point.get("score").and_then(Value::as_f64).unwrap_or(0.0);
                let text = point
                    .pointer("/payload/text")
                    .and_then(Value::as_str)
                    .unwrap_or("missing text");
                let source = point
                    .pointer("/payload/source")
                    .and_then(Value::as_str)
                    .unwrap_or("missing source");
                format!("{}. score {score:.3}\n{text}\nsource: {source}", index + 1)
            })
            .collect::<Vec<_>>()
            .join("\n\n");
        Ok(ToolResult::text(call.id, self.name(), rendered))
    }
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

pub(super) fn embed(text: &str) -> Vec<f32> {
    let mut vector = vec![0.0_f32; VECTOR_SIZE];
    for token in text
        .split(|character: char| !character.is_alphanumeric())
        .filter(|token| !token.is_empty())
    {
        let hash = fnv1a(token.to_ascii_lowercase().as_bytes());
        let index = usize::from(hash.to_le_bytes()[0]);
        let sign = if hash & (1 << 63) == 0 { 1.0 } else { -1.0 };
        vector[index] += sign;
    }
    let magnitude = vector.iter().map(|value| value * value).sum::<f32>().sqrt();
    if magnitude > 0.0 {
        for value in &mut vector {
            *value /= magnitude;
        }
    }
    vector
}

fn point_id(text: &str) -> u64 {
    fnv1a(text.as_bytes())
}

fn fnv1a(bytes: &[u8]) -> u64 {
    bytes.iter().fold(0xcbf2_9ce4_8422_2325, |hash, byte| {
        (hash ^ u64::from(*byte)).wrapping_mul(0x0000_0100_0000_01b3)
    })
}

/// Returns whether a collection-creation response leaves the collection in
/// place.
///
/// A 409 means another caller created it between our existence check and our
/// `PUT`. The postcondition is "the collection exists", and it does, so that is
/// success rather than a conflict. Check-then-create is inherently racy and
/// specialists run in parallel, so losing the race is routine: treating it as an
/// error fails `recall_research` for whichever agent arrives second.
fn collection_now_exists(status: reqwest::StatusCode) -> bool {
    status.is_success() || status == reqwest::StatusCode::CONFLICT
}

fn qdrant_transport_error(error: &reqwest::Error) -> tinyagents::TinyAgentsError {
    tinyagents::TinyAgentsError::Tool(format!("Qdrant request failed: {error}"))
}

async fn qdrant_response_error(
    operation: &str,
    response: reqwest::Response,
) -> tinyagents::TinyAgentsError {
    let status = response.status();
    let body = response
        .text()
        .await
        .unwrap_or_else(|_| "unreadable response".into());
    tinyagents::TinyAgentsError::Tool(format!(
        "Qdrant {operation} returned {status}: {}",
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
    use super::{VECTOR_SIZE, collection_now_exists, embed, point_id};

    #[test]
    fn local_embedding_has_fixed_size_and_unit_length() {
        let vector = embed("prime number theorem asymptotic primes");
        let magnitude = vector.iter().map(|value| value * value).sum::<f32>().sqrt();
        assert_eq!(vector.len(), VECTOR_SIZE);
        assert!((magnitude - 1.0).abs() < 0.000_01);
    }

    #[test]
    fn point_ids_are_deterministic() {
        assert_eq!(point_id("same note"), point_id("same note"));
        assert_ne!(point_id("same note"), point_id("different note"));
    }

    #[test]
    fn losing_the_collection_creation_race_counts_as_success() {
        assert!(collection_now_exists(reqwest::StatusCode::OK));
        assert!(collection_now_exists(reqwest::StatusCode::CONFLICT));
        assert!(!collection_now_exists(
            reqwest::StatusCode::INTERNAL_SERVER_ERROR
        ));
        assert!(!collection_now_exists(reqwest::StatusCode::UNAUTHORIZED));
    }
}
