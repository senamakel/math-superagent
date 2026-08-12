//! Embedded `TinyAgents` runtime.
//!
//! This facade exposes the vendored, provider-neutral `tinyagents` engine with
//! its optional `SQLite`, REPL, and RLM features disabled.

pub mod accounting;
pub mod budget;
pub mod reflection;
pub mod reroute;
pub mod resilient;
pub mod sticky;
pub mod trace;
pub mod untruncated;

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

/// The model for roles whose work is judging rather than doing.
///
/// The run's default is a flash model, chosen for speed because most roles
/// spend their turns writing programs, reading files, and reporting what
/// happened — work where the model's job is to be quick and to not confabulate,
/// and where the method policy's mechanical checks catch it when it does. A
/// handful of roles produce something no tool can check: whether a
/// reformulation is genuinely different, whether an attempt was conducted well,
/// whether what an attempt established is a new fact or the same method at a
/// larger size. That is what a stronger model buys, and it is wasted everywhere
/// else. `orchestrator::REASONING_ROLES` is the list, and carries the test for
/// membership.
///
/// It is also what makes the inventor's dossier worth assembling. Sixteen
/// thousand tokens of record only pays off if the model reading it can hold the
/// whole thing against a new idea.
const REASONING_MODEL: &str = "deepseek/deepseek-v4-pro";

/// Preferred route for [`REASONING_MODEL`], verified against the endpoint list.
///
/// `DeepSeek`'s own endpoint rather than the run's usual `deepinfra`, and the
/// choice is not a trade: at the time of writing it is both the cheapest route
/// for this model — $0.43/$0.87 per million against `DeepInfra`'s $1.30/$2.60 —
/// and the only one of the two that is not quantized, `DeepInfra` serving it at
/// fp4. Paying three times as much for a lower-precision copy of a model chosen
/// for its judgement would defeat the point of choosing it.
///
/// The usual argument for one pinned provider — prompt caching across a large
/// fixed prefix — is weak for these roles: the inventor's prompt carries a
/// dossier rebuilt from disk on every call, and the judge and reflection are
/// handed a different attempt report each time.
const REASONING_PROVIDER: &str = "deepseek";

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
    let model = openrouter_model(DEFAULT_OPENROUTER_MODEL, PREFERRED_PROVIDER)?;
    Ok(model)
}

/// Builds the reasoning model one role runs on, when that role is not on the
/// run's default.
///
/// `MATH_AGENT_REASONING_MODEL` overrides the model and
/// `MATH_AGENT_REASONING_PROVIDER` the route, under the same rule as every
/// other override here: blank or missing keeps the default.
///
/// # Errors
///
/// Returns an error when `OPENROUTER_API_KEY` is missing.
pub(crate) fn openrouter_reasoning_model() -> Result<Arc<dyn ChatModel<()>>> {
    let model =
        env_override("MATH_AGENT_REASONING_MODEL").unwrap_or_else(|| REASONING_MODEL.to_string());
    let provider = env_override("MATH_AGENT_REASONING_PROVIDER")
        .unwrap_or_else(|| REASONING_PROVIDER.to_string());
    openrouter_model(&model, &provider)
}

/// Reads a non-blank environment override, or `None`.
fn env_override(name: &str) -> Option<String> {
    std::env::var(name)
        .ok()
        .map(|value| value.trim().to_string())
        .filter(|value| !value.is_empty())
}

/// Builds an `OpenRouter`-backed model on `model_name`, preferring `provider`.
///
/// `OPENROUTER_MODEL` and `MATH_AGENT_PROVIDER` still override both, so the
/// operator's global escape hatch keeps working for every role.
fn openrouter_model(model_name: &str, provider: &str) -> Result<Arc<dyn ChatModel<()>>> {
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
        .with_model(model_name)
        .with_default_provider_options(serde_json::json!({
            "provider": { "order": [provider], "allow_fallbacks": true }
        }));
    if let Some(provider) = env_override("MATH_AGENT_PROVIDER") {
        model = model.with_default_provider_options(serde_json::json!({
            "provider": { "order": [provider], "allow_fallbacks": true }
        }));
    }
    if let Some(model_name) = env_override("OPENROUTER_MODEL") {
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
