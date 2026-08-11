//! Embedded `TinyAgents` runtime.
//!
//! This facade exposes the vendored, provider-neutral `tinyagents` engine with
//! its optional `SQLite`, REPL, and RLM features disabled.

pub mod budget;
pub mod reflection;
pub mod resilient;
pub mod trace;

use std::sync::Arc;

use tinyagents::harness::context::{RunConfig, RunContext};
use tinyagents::harness::events::EventSink;
use tinyagents::harness::ids::RunId;
use tinyagents::harness::middleware::AgentRun;
use tinyagents::harness::model::ChatModel;
use tinyagents::harness::observability::{
    HarnessEventJournal, InMemoryEventJournal, JournalSink, LangfuseClient, LangfuseTraceConfig,
};
use tinyagents::harness::providers::openai::OpenAiModel;
use tinyagents::harness::tool::ToolTimeoutSettings;

use budget::RunBudget;
use trace::RunTracer;

const DEFAULT_OPENROUTER_MODEL: &str = "deepseek/deepseek-v4-flash-0731";
/// Preferred `OpenRouter` provider slug, verified to route to `DeepInfra`.
///
/// Overridable with `MATH_AGENT_PROVIDER` when a route is degraded.
const PREFERRED_PROVIDER: &str = "deepinfra";

pub use tinyagents::harness::message::Message;
pub use tinyagents::harness::model::ModelResponse;
pub use tinyagents::harness::providers::MockModel;
pub use tinyagents::harness::runtime::AgentHarness;
pub use tinyagents::harness::tool::{Tool, ToolCall, ToolResult, ToolSchema};
pub use tinyagents::{Result, TinyAgentsError};

/// The default slim harness state, which has no application-owned memory or
/// channel context.
pub type SlimAgent = AgentHarness<()>;

/// A `TinyAgents` loop backed by `OpenRouter` and observed through Langfuse.
pub struct ObservedAgent {
    harness: SlimAgent,
    langfuse: LangfuseClient,
    tracer: Option<Arc<RunTracer>>,
}

impl std::fmt::Debug for ObservedAgent {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("ObservedAgent")
            .field("model", &"openrouter")
            .field("langfuse_endpoint", &self.langfuse.endpoint())
            .finish_non_exhaustive()
    }
}

impl ObservedAgent {
    /// Loads `.env`, configures the `OpenRouter` model, and creates the direct
    /// Langfuse ingestion client.
    ///
    /// `OPENROUTER_MODEL` optionally overrides the default `DeepSeek` V4 Flash
    /// model. Requests are routed through `StreamLake`.
    ///
    /// # Errors
    ///
    /// Returns an error when `OPENROUTER_API_KEY` or any required
    /// `LANGFUSE_*` variable is missing, or when the Langfuse URL is invalid.
    pub fn from_env() -> Result<Self> {
        let model = openrouter_model_from_env()?;
        let mut harness = SlimAgent::new();
        harness
            .register_model("openrouter", model)
            .set_default_model("openrouter");
        Self::from_harness(harness)
    }

    /// Runs one `TinyAgents` turn and exports its model, tool, usage, and
    /// lifecycle observations to Langfuse.
    ///
    /// Langfuse delivery is best-effort: an unavailable telemetry endpoint
    /// does not turn a successful agent response into a failure.
    ///
    /// # Errors
    ///
    /// Returns any model, tool, policy, or loop error produced by `TinyAgents`.
    pub async fn invoke(&self, run_id: impl Into<String>, input: Vec<Message>) -> Result<AgentRun> {
        let run_id = run_id.into();
        let journal = Arc::new(InMemoryEventJournal::new());
        let durable_journal: Arc<dyn HarnessEventJournal> = journal.clone();
        let journal_sink = Arc::new(JournalSink::new(
            durable_journal,
            RunId::new(run_id.clone()),
        ));
        let events = EventSink::with_stream_id(&run_id);
        events.subscribe(journal_sink.clone());
        if let Some(tracer) = self.tracer.clone() {
            events.subscribe(tracer);
        }
        let config = RunConfig::new(&run_id)
            .with_max_turn_output_tokens(RunBudget::from_env().max_turn_output_tokens);
        let context = RunContext::new(config, ()).with_events(events);

        let result = self.harness.invoke_in_context(&(), context, input).await;
        journal_sink.flush();
        if let Ok(observations) = journal.read_from(&run_id, 0).await
            && !observations.is_empty()
        {
            let _ = self
                .langfuse
                .send_observations(LangfuseTraceConfig::default(), &observations)
                .await;
        }
        result
    }

    pub(crate) fn from_harness(mut harness: SlimAgent) -> Result<Self> {
        let _ = dotenvy::dotenv();
        configure_run_budget(&mut harness, RunBudget::from_env());
        Ok(Self {
            harness,
            langfuse: LangfuseClient::from_env()?,
            tracer: None,
        })
    }

    /// Attaches a tracer so this run's model and tool activity is streamed to
    /// the console and the workspace journal as it happens.
    #[must_use]
    pub(crate) fn with_tracer(mut self, tracer: Arc<RunTracer>) -> Self {
        self.tracer = Some(tracer);
        self
    }
}

/// Applies the run budget to a harness: per-tool deadline, per-run call and
/// wall-clock caps, partial-result stopping, and payload capture.
pub(crate) fn configure_run_budget(harness: &mut SlimAgent, budget: RunBudget) {
    let tool_timeout_ms = budget.tool_timeout_ms();
    harness
        .with_tool_timeout_settings(ToolTimeoutSettings::new(
            tool_timeout_ms,
            1,
            tool_timeout_ms,
            0,
        ))
        .with_policy(budget.run_policy());
}

pub(crate) fn openrouter_model_from_env() -> Result<Arc<dyn ChatModel<()>>> {
    let _ = dotenvy::dotenv();
    let api_key = std::env::var("OPENROUTER_API_KEY")
        .map_err(|_| TinyAgentsError::Validation("OPENROUTER_API_KEY is required".to_string()))?;
    // One preferred provider, with fallbacks. Both halves matter.
    //
    // Preferring a single route is what makes prompt caching pay: the cache is
    // per-provider, so a run that bounces between providers re-sends its whole
    // system prompt and transcript at full price every turn. These agents carry
    // a large fixed prefix, so the cached reads are most of the saving.
    //
    // Allowing fallbacks is what keeps a busy provider from stopping the
    // runtime. An exclusive `only` pin previously left requests hanging for
    // minutes and exhausting their retries while other providers serving the
    // same model sat idle.
    //
    // Verify any slug you put here actually routes: `streamlake` sat in this
    // list and silently matched nothing, so the documented preference had no
    // effect at all.
    let mut model = OpenAiModel::openrouter(api_key)
        .with_model(DEFAULT_OPENROUTER_MODEL)
        .with_default_provider_options(serde_json::json!({
            "provider": { "order": [PREFERRED_PROVIDER], "allow_fallbacks": true }
        }));
    if let Ok(provider) = std::env::var("MATH_AGENT_PROVIDER")
        && !provider.trim().is_empty()
    {
        model = model.with_default_provider_options(serde_json::json!({
            "provider": { "order": [provider.trim()], "allow_fallbacks": true }
        }));
    }
    if let Ok(model_name) = std::env::var("OPENROUTER_MODEL")
        && !model_name.trim().is_empty()
    {
        model = model.with_model(model_name);
    }
    Ok(Arc::new(model))
}

/// Creates an offline harness suitable for deterministic development and tests.
#[must_use]
pub fn mock(text: impl Into<String>) -> SlimAgent {
    let mut harness = SlimAgent::new();
    harness
        .register_model("mock", std::sync::Arc::new(MockModel::constant(text)))
        .set_default_model("mock");
    harness
}

#[cfg(test)]
mod test;
