//! Hello-world agent with basic tools and sub-agent delegation.

use std::sync::Arc;

use async_trait::async_trait;
use std::fmt::Write as _;

use serde_json::{Value, json};

use crate::agent::budget::RunBudget;
use crate::agent::{
    AgentHarness, Message, ObservedAgent, Result, Tool, ToolCall, ToolResult, ToolSchema,
    configure_run_budget, provider_model_from_env,
};
use crate::orchestrator::async_subagents::AsyncSubagentManager;

const SYSTEM_PROMPT: &str = "You are a friendly hello-world agent. Use tools when they help. \
    Use add_numbers for arithmetic instead of calculating mentally. Delegate a focused piece of \
    work with spawn_agent when the user asks for checking or a second opinion. Keep its run id \
    and use await_agent to retrieve the response. Use exa_search \
    for current facts or web research. Keep the final answer concise, cite returned URLs when \
    search was used, and mention useful tool results naturally.";

const SUBAGENT_PROMPT: &str = "You are a concise helper sub-agent. Complete only the delegated \
    task, report the useful result clearly, and do not invent tool output.";

/// A small provider-backed agent with deterministic tools and delegation.
#[derive(Debug)]
pub struct HelloAgent {
    inner: ObservedAgent,
}

impl HelloAgent {
    /// Loads the local provider and Langfuse configuration and constructs the
    /// parent and child agent loops.
    ///
    /// # Errors
    ///
    /// Returns an error when the required provider or Langfuse environment
    /// variables are missing or invalid.
    pub fn from_env() -> Result<Self> {
        let model = provider_model_from_env()?;
        let budget = RunBudget::from_env();

        let mut child_harness: AgentHarness<()> = AgentHarness::new();
        child_harness
            .register_model("openrouter", model.clone())
            .set_default_model("openrouter");
        configure_run_budget(&mut child_harness, budget);
        let async_subagents = AsyncSubagentManager::new(budget, None);
        async_subagents.register("helper", Arc::new(child_harness), SUBAGENT_PROMPT)?;

        let mut parent_harness: AgentHarness<()> = AgentHarness::new();
        parent_harness
            .register_model("openrouter", model)
            .set_default_model("openrouter")
            .register_tool(Arc::new(EchoTool))
            .register_tool(Arc::new(AddTool))
            .register_tool(Arc::new(ExaSearchTool::from_env()?));
        for tool in async_subagents.tools(["helper"]) {
            parent_harness.register_tool(tool);
        }

        Ok(Self {
            inner: ObservedAgent::from_harness(parent_harness)?,
        })
    }

    /// Runs one task through the hello-world agent.
    ///
    /// The run and any delegated child work are exported to Langfuse under
    /// `run_id`.
    ///
    /// # Errors
    ///
    /// Returns any provider, tool, policy, or agent-loop error.
    pub async fn run(&self, run_id: impl Into<String>, task: impl Into<String>) -> Result<String> {
        let run = self
            .inner
            .invoke(
                run_id,
                vec![Message::system(SYSTEM_PROMPT), Message::user(task)],
            )
            .await?;
        Ok(run.text().unwrap_or_default())
    }
}

#[derive(Debug)]
struct EchoTool;

#[async_trait]
impl Tool<()> for EchoTool {
    fn name(&self) -> &'static str {
        "echo_text"
    }

    fn description(&self) -> &'static str {
        "Echoes a short text value exactly, useful for checking tool calls."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": { "text": { "type": "string" } },
                "required": ["text"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let text = call
            .arguments
            .get("text")
            .and_then(serde_json::Value::as_str)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation("text is required".into()))?;
        Ok(ToolResult::text(call.id, self.name(), text))
    }
}

#[derive(Debug)]
struct AddTool;

#[async_trait]
impl Tool<()> for AddTool {
    fn name(&self) -> &'static str {
        "add_numbers"
    }

    fn description(&self) -> &'static str {
        "Adds two numbers and returns their sum."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "a": { "type": "number" },
                    "b": { "type": "number" }
                },
                "required": ["a", "b"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let a = number_argument(&call, "a")?;
        let b = number_argument(&call, "b")?;
        Ok(ToolResult::text(call.id, self.name(), (a + b).to_string()))
    }
}

fn number_argument(call: &ToolCall, name: &str) -> Result<f64> {
    call.arguments
        .get(name)
        .and_then(serde_json::Value::as_f64)
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{name} must be a number")))
}

/// Results requested per search.
///
/// Five was too few for the way this runtime searches. A mathematical question
/// rarely has one right source: the run wants the original paper, a survey
/// that places it, and whatever states the identity in the form it needs, and
/// the first five hits for a technical query are routinely three restatements
/// of the problem and two unrelated pages. Ten is enough for the useful source
/// to be present without the result becoming a context bill of its own, which
/// the per-result and total bounds below then hold it to.
const EXA_RESULTS: usize = 10;
/// Characters kept from any one result's text.
const EXA_RESULT_CHARS: usize = 1_200;
/// Characters kept across the whole rendered result.
const EXA_TOTAL_CHARS: usize = 12_000;

fn exa_results() -> usize {
    std::env::var("MATH_AGENT_EXA_RESULTS")
        .ok()
        .and_then(|value| value.trim().parse::<usize>().ok())
        .filter(|count| *count > 0)
        .unwrap_or(EXA_RESULTS)
}

/// Truncates on a character boundary, marking that it did.
fn clip(text: &str, limit: usize) -> String {
    let trimmed = text.trim();
    if trimmed.chars().count() <= limit {
        return trimmed.to_string();
    }
    let kept: String = trimmed.chars().take(limit).collect();
    format!("{kept}…")
}

/// Renders one Exa result: what it is, who wrote it, and why it matched.
fn render_exa_result(index: usize, result: &Value) -> String {
    let title = result
        .get("title")
        .and_then(Value::as_str)
        .unwrap_or("Untitled");
    let url = result
        .get("url")
        .and_then(Value::as_str)
        .unwrap_or("No URL");
    let mut rendered = format!("{}. {title}\n{url}", index + 1);

    // Provenance, so a source can be weighed rather than merely cited. A 1994
    // paper by the author the problem is named after is worth more than a
    // forum post, and nothing else in the result says so.
    let author = result
        .get("author")
        .and_then(Value::as_str)
        .unwrap_or_default()
        .trim();
    let published = result
        .get("publishedDate")
        .and_then(Value::as_str)
        .unwrap_or_default()
        .trim();
    let separator = if author.is_empty() || published.is_empty() {
        ""
    } else {
        ", "
    };
    if !author.is_empty() || !published.is_empty() {
        let _ = write!(rendered, "\n{author}{separator}{published}");
    }

    let summary = result
        .get("summary")
        .and_then(Value::as_str)
        .unwrap_or_default();
    if !summary.trim().is_empty() {
        let _ = write!(rendered, "\n{}", clip(summary, EXA_RESULT_CHARS));
    }
    let highlights = result
        .get("highlights")
        .and_then(Value::as_array)
        .map(|items| {
            items
                .iter()
                .filter_map(Value::as_str)
                .collect::<Vec<_>>()
                .join(" ")
        })
        .unwrap_or_default();
    if !highlights.trim().is_empty() {
        let _ = write!(
            rendered,
            "\nMatching passages: {}",
            clip(&highlights, EXA_RESULT_CHARS)
        );
    }
    rendered
}

#[derive(Debug)]
pub(crate) struct ExaSearchTool {
    client: reqwest::Client,
    api_key: String,
}

impl ExaSearchTool {
    pub(crate) fn from_env() -> Result<Self> {
        let api_key = std::env::var("EXA_API_KEY").map_err(|_| {
            tinyagents::TinyAgentsError::Validation("EXA_API_KEY is required".into())
        })?;
        Ok(Self {
            client: reqwest::Client::new(),
            api_key,
        })
    }
}

#[async_trait]
impl Tool<()> for ExaSearchTool {
    fn name(&self) -> &'static str {
        "exa_search"
    }

    fn description(&self) -> &'static str {
        "Searches the live web with Exa and returns each source's URL, a summary, and the passages \
         matching the query. Set `category` to `research paper` to search the literature rather \
         than the open web — that is usually what a mathematical question wants. Search several \
         distinct phrasings rather than one: the named theory, the objects involved, and the \
         numbers themselves each surface different sources."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A specific natural-language web search query."
                    },
                    "category": {
                        "type": "string",
                        "description": "Narrows the search to one kind of source.",
                        "enum": ["research paper", "pdf", "news", "company", "github"]
                    },
                    "include_domains": {
                        "type": "array",
                        "items": { "type": "string" },
                        "description": "Only return results from these domains, e.g. \
                                        [\"arxiv.org\"]. Use it when a subject's name collides \
                                        with something popular, which is what buries a \
                                        mathematical query under an unrelated field."
                    },
                    "exclude_domains": {
                        "type": "array",
                        "items": { "type": "string" },
                        "description": "Never return results from these domains. Use it to push \
                                        past the encyclopedic retellings once the run holds them."
                    },
                    "start_published_date": {
                        "type": "string",
                        "description": "ISO 8601 date; only results published after it. Use it to \
                                        find what came after a result the run is stuck on."
                    },
                    "end_published_date": {
                        "type": "string",
                        "description": "ISO 8601 date; only results published before it. Use it \
                                        to reach the original treatment rather than its \
                                        retellings."
                    },
                    "num_results": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 25,
                        "description": "How many results to return. Raise it when surveying a \
                                        subject rather than checking one fact."
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = call
            .arguments
            .get("query")
            .and_then(serde_json::Value::as_str)
            .ok_or_else(|| tinyagents::TinyAgentsError::Validation("query is required".into()))?;
        let requested = call
            .arguments
            .get("num_results")
            .and_then(Value::as_u64)
            .map_or_else(exa_results, |count| count.clamp(1, 25) as usize);
        let mut request = json!({
            "query": query,
            "type": "auto",
            "numResults": requested,
            // A summary says what the source is; highlights say why it matched.
            // Asking for both is what makes a result decidable without a
            // download, which is the expensive step this is trying to target.
            "contents": {
                "summary": true,
                "highlights": { "numSentences": 4, "highlightsPerUrl": 3 }
            }
        });
        if let Some(category) = call.arguments.get("category").and_then(Value::as_str)
            && !category.trim().is_empty()
            && let Some(object) = request.as_object_mut()
        {
            object.insert("category".to_string(), json!(category.trim()));
        }
        // A filter is only sent when it carries something. An empty list is not
        // "no filter" to Exa — `includeDomains: []` matches nothing — so a
        // model that names the argument and leaves it blank must not silently
        // get an empty search.
        if let Some(object) = request.as_object_mut() {
            for (argument, field) in [
                ("include_domains", "includeDomains"),
                ("exclude_domains", "excludeDomains"),
            ] {
                let domains: Vec<&str> = call
                    .arguments
                    .get(argument)
                    .and_then(Value::as_array)
                    .into_iter()
                    .flatten()
                    .filter_map(Value::as_str)
                    .map(str::trim)
                    .filter(|domain| !domain.is_empty())
                    .collect();
                if !domains.is_empty() {
                    object.insert(field.to_string(), json!(domains));
                }
            }
            for (argument, field) in [
                ("start_published_date", "startPublishedDate"),
                ("end_published_date", "endPublishedDate"),
            ] {
                if let Some(date) = call
                    .arguments
                    .get(argument)
                    .and_then(Value::as_str)
                    .map(str::trim)
                    .filter(|date| !date.is_empty())
                {
                    object.insert(field.to_string(), json!(date));
                }
            }
        }
        let response = self
            .client
            .post("https://api.exa.ai/search")
            .header("x-api-key", &self.api_key)
            .json(&request)
            .send()
            .await
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("Exa search request failed: {error}"))
            })?;
        let status = response.status();
        let body: serde_json::Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("Exa response was invalid: {error}"))
        })?;
        if !status.is_success() {
            let message = body
                .get("error")
                .and_then(serde_json::Value::as_str)
                .unwrap_or("unknown Exa API error");
            return Err(tinyagents::TinyAgentsError::Tool(format!(
                "Exa search returned {status}: {message}"
            )));
        }

        let results = body
            .get("results")
            .and_then(serde_json::Value::as_array)
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Tool("Exa response contained no results".into())
            })?;
        let rendered = results
            .iter()
            .enumerate()
            .map(|(index, result)| render_exa_result(index, result))
            .collect::<Vec<_>>()
            .join("\n\n");
        // A wider search must not become a context bill. The per-result clip
        // in the renderer bounds a verbose source; this bounds a verbose set
        // of them.
        let rendered = clip(&rendered, EXA_TOTAL_CHARS);

        Ok(ToolResult::text(call.id, self.name(), rendered))
    }
}

#[cfg(test)]
#[path = "hello_agent_test.rs"]
mod test;
