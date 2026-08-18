//! Embedded `TinyAgents` runtime.
//!
//! This facade exposes the vendored, provider-neutral `tinyagents` engine with
//! its optional `SQLite`, REPL, and RLM features disabled.

pub mod accounting;
pub mod budget;
mod context_window;
pub mod flow;
pub mod pace;
pub mod reflection;
pub mod reroute;
pub mod resilient;
pub mod sampling;
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
use context_window::ContextWindowModel;
use trace::RunTracer;

const LOCAL_ROUTER_BASE_URL: &str = "http://localhost:6969/v1";
const DEFAULT_MODEL: &str = "flash";
/// Stable tier id the router resolves to its current reasoning ladder.
const REASONING_MODEL: &str = "reasoning";
/// Stable tier id the router resolves to its deepest ladder.
///
/// A separate ladder rather than a parameter on the reasoning one, because
/// *how hard to think* is a property of the model that ends up serving: the
/// router injects the effort word each rung's model family accepts, and a
/// runtime asking for one directly would be guessing on behalf of a rung it
/// cannot see. See the router's `max-reasoning` ladder.
const MAX_REASONING_MODEL: &str = "max-reasoning";
const ROUTER_CONTEXT_WINDOW: u64 = 1_000_000;

/// Stable tier id the router resolves to its Lean ladder.
///
/// Behind it is Leanstral: a 119B mixture-of-experts trained for Lean 4 proof
/// engineering, free while it is in public preview. Measured against this
/// repository's own kernel it answers a routine Mathlib lemma in one to four
/// seconds where the run's default spends three minutes reasoning and still
/// misses — so what it buys is volume, not depth.
///
/// No marketplace resells it, so the router reaches Mistral directly and the
/// ladder is one rung: this model or nothing, which for a role whose output is
/// checked by a kernel is the right answer. Overridable with
/// `MATH_AGENT_SCRIBE_MODEL`; pointing it at `flash` is how a run opts the tier
/// out without a rebuild.
const SCRIBE_MODEL: &str = "scribe";

pub use tinyagents::harness::message::Message;
pub use tinyagents::harness::model::ModelResponse;
pub use tinyagents::harness::providers::MockModel;
pub use tinyagents::harness::runtime::AgentHarness;
pub use tinyagents::harness::tool::{Tool, ToolCall, ToolResult, ToolSchema};
pub use tinyagents::{Result, TinyAgentsError};

/// The default slim harness state, which has no application-owned memory or
/// channel context.
pub type SlimAgent = AgentHarness<()>;

/// A provider-backed `TinyAgents` loop observed through Langfuse.
pub struct ObservedAgent {
    harness: SlimAgent,
    langfuse: LangfuseClient,
    tracer: Option<Arc<RunTracer>>,
}

impl std::fmt::Debug for ObservedAgent {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("ObservedAgent")
            .field("model", &"configured-provider")
            .field("langfuse_endpoint", &self.langfuse.endpoint())
            .finish_non_exhaustive()
    }
}

impl ObservedAgent {
    /// Loads `.env`, configures the model provider, and creates the direct
    /// Langfuse ingestion client.
    ///
    /// `MATH_AGENT_MODEL` optionally overrides the `flash` tier id, and
    /// `MATH_AGENT_API_BASE_URL` replaces the local router endpoint.
    ///
    /// # Errors
    ///
    /// Returns an error when no provider API key or any required
    /// `LANGFUSE_*` variable is missing, or when the Langfuse URL is invalid.
    pub fn from_env() -> Result<Self> {
        let model = provider_model_from_env()?;
        let mut harness = SlimAgent::new();
        harness
            .register_model("router", model)
            .set_default_model("router");
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

pub(crate) fn provider_model_from_env() -> Result<Arc<dyn ChatModel<()>>> {
    router_model_from_env("MATH_AGENT_MODEL", DEFAULT_MODEL)
}

/// Builds the reasoning model one role runs on, when that role is not on the
/// run's default.
///
/// `MATH_AGENT_REASONING_MODEL` overrides the tier id under the same rule as
/// every other override here: blank or missing keeps the default.
///
/// # Errors
///
/// Returns an error when `MATH_AGENT_API_KEY` is not configured.
pub(crate) fn provider_reasoning_model() -> Result<Arc<dyn ChatModel<()>>> {
    router_model_from_env("MATH_AGENT_REASONING_MODEL", REASONING_MODEL)
}

/// Builds the deepest-thinking model, for the handful of roles whose whole
/// output is a judgement nothing mechanical can check.
///
/// `MATH_AGENT_MAX_REASONING_MODEL` overrides the tier id under the same rule
/// as every other override here: blank or missing keeps the default. Pointing
/// it at `reasoning` is how a run opts the whole tier back out without a
/// rebuild.
///
/// # Errors
///
/// Returns an error when `MATH_AGENT_API_KEY` is not configured.
pub(crate) fn provider_max_reasoning_model() -> Result<Arc<dyn ChatModel<()>>> {
    router_model_from_env("MATH_AGENT_MAX_REASONING_MODEL", MAX_REASONING_MODEL)
}

/// Builds the model the Lean scribe runs on.
///
/// Through the router, like every other tier. It used to hold Mistral's own
/// endpoint and its own key, which made it the one tier outside the router's
/// pacing, session pinning and rate-limit cooldowns — and the one whose
/// credential had to be in the container rather than beside the ladder. The
/// router now carries a one-rung `scribe` ladder reaching the same model, so
/// this is a tier id again and the endpoint is a routing decision.
///
/// The two wrappers stay, and neither is redundant with what the router does.
/// The sampling pair is what makes a greedy request legal at the model behind
/// the ladder at all. The pacing is a *queue*: the router answers a rate limit
/// by parking the rung, and a one-rung ladder with its rung parked has nothing
/// to fall to, so the cheap way to stay under the ceiling is not to cross it.
/// Pacing outermost, so a call waits for its slot before anything else.
///
/// # Errors
///
/// Returns an error when `MATH_AGENT_API_KEY` is not configured.
pub(crate) fn scribe_model() -> Result<Arc<dyn ChatModel<()>>> {
    let model = router_model_from_env("MATH_AGENT_SCRIBE_MODEL", SCRIBE_MODEL)?;
    let model: Arc<dyn ChatModel<()>> = Arc::new(sampling::GreedySamplingModel::new(model));
    Ok(Arc::new(pace::PacedModel::scribe_from_env(model)))
}

/// Reads a non-blank environment override, or `None`.
fn env_override(name: &str) -> Option<String> {
    std::env::var(name)
        .ok()
        .map(|value| value.trim().to_string())
        .filter(|value| !value.is_empty())
}

/// Builds one authenticated tier on the OpenAI-compatible local router.
fn router_model_from_env(model_env: &str, default_model: &str) -> Result<Arc<dyn ChatModel<()>>> {
    let _ = dotenvy::dotenv();
    let base_url = configured_api_base_url();
    let model = env_override(model_env).unwrap_or_else(|| default_model.to_string());
    let api_key = env_override("MATH_AGENT_API_KEY").ok_or_else(missing_provider_key)?;
    Ok(router_model(api_key, &base_url, &model))
}

fn router_model(api_key: String, base_url: &str, model_name: &str) -> Arc<dyn ChatModel<()>> {
    let model: Arc<dyn ChatModel<()>> = Arc::new(
        OpenAiModel::new(api_key)
            .with_provider("local-router")
            .with_base_url(base_url)
            .with_model(model_name),
    );
    Arc::new(ContextWindowModel::new(model, ROUTER_CONTEXT_WINDOW))
}

fn missing_provider_key() -> TinyAgentsError {
    TinyAgentsError::Validation("MATH_AGENT_API_KEY is required".to_string())
}

fn configured_api_base_url() -> String {
    env_override("MATH_AGENT_API_BASE_URL").unwrap_or_else(|| LOCAL_ROUTER_BASE_URL.to_string())
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
#[path = "agent_test.rs"]
mod test;
