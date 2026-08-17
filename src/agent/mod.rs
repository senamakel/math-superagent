//! Embedded `TinyAgents` runtime.
//!
//! This facade exposes the vendored, provider-neutral `tinyagents` engine with
//! its optional `SQLite`, REPL, and RLM features disabled.

pub mod accounting;
pub mod budget;
pub mod fallback;
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
use tinyagents::harness::providers::{ProviderKind, ProviderSpec};
use tinyagents::harness::tool::ToolTimeoutSettings;

use budget::RunBudget;
use fallback::ProviderFallbackModel;
use trace::RunTracer;

const DEFAULT_SURPLUS_MODEL: &str = "deepseek-v4-flash-0731";
const DEFAULT_OPENROUTER_MODEL: &str = "deepseek/deepseek-v4-flash-0731";
const SURPLUS_BASE_URL: &str = "https://api.surplusintelligence.ai/v1";
const OPENROUTER_BASE_URL: &str = "https://openrouter.ai/api/v1";
/// Preferred `OpenRouter` provider slug, verified to route to `DeepInfra`.
///
/// Overridable with `MATH_AGENT_PROVIDER` when a route is degraded.
const PREFERRED_PROVIDER: &str = "deepinfra";

/// Public URL used to attribute this application's `OpenRouter` requests.
const OPENROUTER_APP_URL: &str = "https://opencompany.tinyhumans.ai/";

/// Display name used to attribute this application's `OpenRouter` requests.
const OPENROUTER_APP_TITLE: &str = "OpenCompany";

/// Marketplace category used to classify this application's `OpenRouter` requests.
const OPENROUTER_APP_CATEGORY: &str = "personal-agent";

/// The model the Lean scribe runs on, on Mistral's own endpoint.
///
/// A 119B mixture-of-experts trained for Lean 4 proof engineering, free while
/// it is in public preview. Measured against this repository's own kernel it
/// answers a routine Mathlib lemma in one to four seconds where the run's
/// default spends three minutes reasoning and still misses — so what it buys
/// is volume, not depth. Overridable with `MATH_AGENT_SCRIBE_MODEL`.
const SCRIBE_MODEL: &str = "labs-leanstral-1-5";

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
///
/// **It is the flash model today**, which is to say the split is switched off
/// at its default while every part of the mechanism stays: `REASONING_ROLES`
/// still selects the four roles, `MATH_AGENT_REASONING_MODEL` still moves them,
/// and turning the split back on is one variable rather than a rewrite. The
/// reason is price — `deepseek-v4-pro` cost $0.43/$0.87 per million when the
/// paragraph above was written and $0.66/$1.98 on 2026-08-17, against
/// $0.08/$0.18 for flash, so a judgement now costs roughly ten times a working
/// turn rather than five. What that buys is unmeasured here, and a cost this
/// repository has not measured a benefit for is one the default should not
/// carry.
const REASONING_MODEL: &str = "deepseek-v4-flash-0731";

/// Preferred `OpenRouter` fallback route for [`REASONING_MODEL`].
///
/// `DeepInfra`, which is the fallback route for the flash model too, so both
/// fallback models leave through one provider.
///
/// It was `DeepSeek`'s own endpoint, on an argument that has since expired:
/// $0.43/$0.87 per million against `DeepInfra`'s $1.30/$2.60, unquantized
/// against fp4. `DeepSeek` has raised its prices — the same endpoint reads
/// $0.66/$1.98 on 2026-08-17, a completion rate more than doubled — and
/// `DeepInfra` now serves this model at fp8 rather than fp4, so the precision
/// half of that argument is gone as well.
///
/// What the pin does *not* buy is a cheaper route. `DeepInfra` is still the
/// dearer of the two per token, and `StreamLake` ($0.40/$0.79, fp8) and `Baidu`
/// ($0.41/$0.81, fp8) are cheaper than either — `MATH_AGENT_REASONING_PROVIDER`
/// moves it in one variable, and the endpoint list is worth re-reading before
/// leaving it where it is.
///
/// The usual argument for one pinned provider — prompt caching across a large
/// fixed prefix — is weak for these roles: the inventor's prompt carries a
/// dossier rebuilt from disk on every call, and the judge and reflection are
/// handed a different attempt report each time.
const REASONING_PROVIDER: &str = "deepinfra";

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
    /// `MATH_AGENT_MODEL` optionally overrides the default `DeepSeek` V4 Flash
    /// model, and `MATH_AGENT_API_BASE_URL` replaces the Surplus primary.
    ///
    /// # Errors
    ///
    /// Returns an error when no provider API key or any required
    /// `LANGFUSE_*` variable is missing, or when the Langfuse URL is invalid.
    pub fn from_env() -> Result<Self> {
        let model = provider_model_from_env()?;
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

pub(crate) fn provider_model_from_env() -> Result<Arc<dyn ChatModel<()>>> {
    let model = provider_model(
        DEFAULT_SURPLUS_MODEL,
        DEFAULT_OPENROUTER_MODEL,
        PREFERRED_PROVIDER,
    )?;
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
/// Returns an error when neither supported provider API key is configured.
pub(crate) fn provider_reasoning_model() -> Result<Arc<dyn ChatModel<()>>> {
    let model =
        env_override("MATH_AGENT_REASONING_MODEL").unwrap_or_else(|| REASONING_MODEL.to_string());
    let provider = env_override("MATH_AGENT_REASONING_PROVIDER")
        .unwrap_or_else(|| REASONING_PROVIDER.to_string());
    let fallback_model = env_override("MATH_AGENT_REASONING_OPENROUTER_MODEL")
        .unwrap_or_else(|| openrouter_model_name(&model));
    provider_model(&model, &fallback_model, &provider)
}

/// Builds the model the Lean scribe runs on, or `None` when it is unavailable.
///
/// Mistral's own endpoint rather than `OpenRouter`, because the Leanstral tier
/// is free there and answers a routine Mathlib lemma in seconds where the run's
/// default takes minutes. The base URL and the key's name are read off the
/// vendored [`ProviderSpec`] rather than restated here, so a vendor bump moves
/// them in one place.
///
/// `None` is the ordinary outcome of an unset `MISTRAL_API_KEY`, not a failure:
/// this tier is optional, and a run that never asked for it must start exactly
/// as before. That is also why [`OpenAiModel::from_spec`] is used rather than
/// `from_spec_env`, which returns an error for a missing key.
///
/// `MATH_AGENT_SCRIBE_MODEL` overrides the model under the usual rule. The
/// `OpenRouter`-only overrides deliberately do not reach here: `provider.order`
/// is not a concept this endpoint has.
pub(crate) fn scribe_model() -> Option<Arc<dyn ChatModel<()>>> {
    let _ = dotenvy::dotenv();
    let mut spec = ProviderSpec::for_kind(ProviderKind::Mistral);
    spec.model =
        env_override("MATH_AGENT_SCRIBE_MODEL").unwrap_or_else(|| SCRIBE_MODEL.to_string());
    let api_key = env_override(spec.api_key_env.as_deref()?)?;
    let model = OpenAiModel::from_spec(spec, api_key).ok()?;
    // Both wrappers go inside the returned handle so no call site can forget
    // either: the sampling pair is what makes a greedy request legal here at
    // all, and the pacing is what keeps a fan-out under the account's ceiling.
    // Pacing outermost, so a call waits for its slot before anything else.
    let model: Arc<dyn ChatModel<()>> =
        Arc::new(sampling::GreedySamplingModel::new(Arc::new(model)));
    Some(Arc::new(pace::PacedModel::scribe_from_env(model)))
}

/// Reads a non-blank environment override, or `None`.
fn env_override(name: &str) -> Option<String> {
    std::env::var(name)
        .ok()
        .map(|value| value.trim().to_string())
        .filter(|value| !value.is_empty())
}

/// Builds the configured OpenAI-compatible model on `model_name`.
///
/// Surplus is the default. `OpenRouter` is used when the primary fails, or by
/// itself when no primary key is configured. `MATH_AGENT_API_BASE_URL`,
/// `MATH_AGENT_API_KEY`, and `MATH_AGENT_MODEL` replace the primary endpoint;
/// `OPENROUTER_API_KEY` and `OPENROUTER_MODEL` configure the fallback.
fn provider_model(
    model_name: &str,
    fallback_model_name: &str,
    provider: &str,
) -> Result<Arc<dyn ChatModel<()>>> {
    let _ = dotenvy::dotenv();
    let base_url = configured_api_base_url();
    let model_name = env_override("MATH_AGENT_MODEL").unwrap_or_else(|| model_name.to_string());
    let fallback_model_name =
        env_override("OPENROUTER_MODEL").unwrap_or_else(|| fallback_model_name.to_string());

    if is_openrouter_base_url(&base_url) {
        let api_key = primary_api_key(&base_url)
            .or_else(|| env_override("OPENROUTER_API_KEY"))
            .ok_or_else(missing_provider_key)?;
        return Ok(openrouter_model(api_key, &model_name, provider));
    }

    let primary_name = if is_surplus_base_url(&base_url) {
        "surplus"
    } else {
        "primary"
    };
    let primary = primary_api_key(&base_url).map(|api_key| {
        let profile_provider = if is_surplus_base_url(&base_url) {
            "surplus"
        } else {
            "openai-compatible"
        };
        Arc::new(
            OpenAiModel::new(api_key)
                .with_provider(profile_provider)
                .with_base_url(base_url.clone())
                .with_model(model_name.clone()),
        ) as Arc<dyn ChatModel<()>>
    });
    let fallback = env_override("OPENROUTER_API_KEY")
        .map(|api_key| openrouter_model(api_key, &fallback_model_name, provider));

    match (primary, fallback) {
        (Some(primary), Some(fallback)) => Ok(Arc::new(ProviderFallbackModel::new(
            primary,
            primary_name,
            fallback,
            "openrouter",
        ))),
        (Some(primary), None) => Ok(primary),
        (None, Some(fallback)) => Ok(fallback),
        (None, None) => Err(missing_provider_key()),
    }
}

fn openrouter_model(api_key: String, model_name: &str, provider: &str) -> Arc<dyn ChatModel<()>> {
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
    let mut model = openrouter_client(api_key)
        .with_model(model_name)
        .with_default_provider_options(serde_json::json!({
            "provider": { "order": [provider], "allow_fallbacks": true }
        }));
    if let Some(provider) = env_override("MATH_AGENT_PROVIDER") {
        model = model.with_default_provider_options(serde_json::json!({
            "provider": { "order": [provider], "allow_fallbacks": true }
        }));
    }
    Arc::new(model)
}

fn missing_provider_key() -> TinyAgentsError {
    TinyAgentsError::Validation(
        "SURPLUS_API_KEY, MATH_AGENT_API_KEY, or OPENROUTER_API_KEY is required".to_string(),
    )
}

fn primary_api_key(base_url: &str) -> Option<String> {
    env_override("MATH_AGENT_API_KEY").or_else(|| {
        is_surplus_base_url(base_url)
            .then(|| env_override("SURPLUS_API_KEY"))
            .flatten()
    })
}

fn openrouter_model_name(model: &str) -> String {
    if model.contains('/') {
        return model.to_string();
    }
    if model.starts_with("deepseek-") {
        return format!("deepseek/{model}");
    }
    model.to_string()
}

/// Returns whether the configured endpoint speaks `OpenRouter`'s routing dialect.
///
/// Direct OpenAI-compatible endpoints must not receive `OpenRouter`'s nested
/// `provider` object or its affinity/rerouting wrappers.
pub(crate) fn configured_endpoint_is_openrouter() -> bool {
    let _ = dotenvy::dotenv();
    let base_url = configured_api_base_url();
    is_openrouter_base_url(&base_url)
        || (primary_api_key(&base_url).is_none() && env_override("OPENROUTER_API_KEY").is_some())
}

fn configured_api_base_url() -> String {
    env_override("MATH_AGENT_API_BASE_URL").unwrap_or_else(|| SURPLUS_BASE_URL.to_string())
}

fn is_surplus_base_url(base_url: &str) -> bool {
    base_url.trim_end_matches('/') == SURPLUS_BASE_URL
}

fn is_openrouter_base_url(base_url: &str) -> bool {
    base_url.trim_end_matches('/') == OPENROUTER_BASE_URL
}

/// Builds the shared `OpenRouter` transport, including application attribution.
fn openrouter_client(api_key: impl Into<String>) -> OpenAiModel {
    OpenAiModel::openrouter(api_key)
        .with_header("HTTP-Referer", OPENROUTER_APP_URL)
        .with_header("X-OpenRouter-Title", OPENROUTER_APP_TITLE)
        .with_header("X-OpenRouter-Categories", OPENROUTER_APP_CATEGORY)
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
