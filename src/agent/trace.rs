//! Live console and JSONL tracing for orchestrator and specialist runs.
//!
//! Without this the operator sees nothing between launching `./agent` and the
//! final answer, and Langfuse only receives the orchestrator's own events
//! because specialist runs are executed on a bare context. A `RunTracer` is
//! attached to every run in the tree. Each one carries a fixed label so
//! concurrent specialists stay distinguishable, and all of them share one
//! start time, one counter pair, and one journal file, so the console shows a
//! single ordered stream of the whole investigation.

use std::fmt::Write as _;
use std::io::Write as _;
use std::path::{Path, PathBuf};
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::{Arc, Mutex};
use std::time::Instant;

use tinyagents::harness::events::{AgentEvent, EventListener, EventRecord};

/// Maximum characters of a tool argument echoed to the console.
const CONSOLE_PREVIEW_CHARS: usize = 240;

/// What one model call used and cost.
///
/// Assembled from the provider's response body, which is the only place that
/// carries the route and the price.
#[derive(Clone, Debug, Default, PartialEq)]
pub struct ModelAccounting {
    /// The agent whose call this was.
    pub agent: String,
    /// The provider that served it, when the body names one.
    pub provider: Option<String>,
    /// The model that served it, when the body names one.
    pub model: Option<String>,
    /// Prompt tokens sent.
    pub input_tokens: u64,
    /// The portion of those prompt tokens served from the provider's cache.
    pub cached_tokens: u64,
    /// Tokens generated.
    pub output_tokens: u64,
    /// The portion of generated tokens spent on a hidden reasoning channel.
    ///
    /// Worth separating: a turn that spends its whole budget here returns no
    /// usable content and is retried at double the cap, so this is what makes
    /// that failure legible instead of mysterious.
    pub reasoning_tokens: u64,
    /// What the provider charged, in USD.
    pub usd: f64,
}

impl ModelAccounting {
    /// Returns the cost in micro-USD for atomic accumulation.
    #[must_use]
    pub fn micro_usd(&self) -> u64 {
        // Negative or non-finite costs are provider noise, not credits.
        if !self.usd.is_finite() || self.usd <= 0.0 {
            return 0;
        }
        // Guarded above: finite and positive, so the cast cannot lose a sign,
        // and a run would have to cost eighteen trillion dollars to saturate.
        #[expect(
            clippy::cast_possible_truncation,
            clippy::cast_sign_loss,
            reason = "value is checked finite and positive immediately above"
        )]
        let micros = (self.usd * 1_000_000.0).round() as u64;
        micros
    }
}

/// State shared by every tracer in one investigation.
#[derive(Debug)]
struct TraceState {
    started: Instant,
    journal: Option<Mutex<std::fs::File>>,
    model_calls: AtomicU64,
    tool_calls: AtomicU64,
    /// Milliseconds spent inside provider calls, summed across every agent.
    model_ms: AtomicU64,
    /// Milliseconds spent inside tool calls, summed across every agent.
    tool_ms: AtomicU64,
    /// Prompt tokens sent, and the portion served from the provider cache.
    input_tokens: AtomicU64,
    cached_tokens: AtomicU64,
    /// Output tokens generated, summed across every agent.
    output_tokens: AtomicU64,
    /// Run cost in micro-USD, summed across every agent.
    ///
    /// Held as an integer because it is accumulated from several threads and a
    /// float has no atomic. Micro-USD keeps a full cent to four decimal places,
    /// far finer than any single call is priced.
    micro_usd: AtomicU64,
    /// Middleware hooks that have started and not yet completed, keyed by the
    /// agent label and the middleware name.
    ///
    /// Keyed by both because children share this state: two specialists running
    /// concurrently pass through the same middleware names, and a key of name
    /// alone would let one agent's completion consume another's start time.
    /// Within a single agent the hooks are sequential, so the pair is unique.
    middleware_started: Mutex<HashMap<(String, String), Instant>>,
    /// How many times each middleware ran and how long it spent, in
    /// microseconds, so the summary can report what the suppressed lines would
    /// have said.
    middleware_totals: Mutex<HashMap<String, (u64, u64)>>,
}

/// How long a middleware hook must take before it earns a journal line.
///
/// The middleware events carry only a name — no duration, no outcome, nothing
/// the surrounding model and tool events do not already imply — and both hooks
/// fire on both sides of every model call and every tool call. On one measured
/// run they were 5,108 of 6,406 events, four fifths of a 24 MB journal, and the
/// same volume reached Langfuse, where it is what makes a broad query fail.
///
/// A hook that returns in under a millisecond did nothing: the reflection
/// middleware short-circuits when no tool has failed, and compression
/// short-circuits below its token trigger. Recording that thousands of times
/// buries the events that matter. So the fast ones are counted and summarised
/// at the end of the run, and only a hook slow enough to have actually worked
/// is written where it happened.
const MIDDLEWARE_JOURNAL_THRESHOLD: std::time::Duration = std::time::Duration::from_millis(1);

/// An event listener that prints a compact live trace for one run and appends
/// full event records to a shared JSONL file inside the workspace.
#[derive(Debug)]
pub struct RunTracer {
    label: String,
    state: Arc<TraceState>,
}

impl RunTracer {
    /// Creates the root tracer, printing to stderr and, when `journal_path` is
    /// writable, appending every event as one JSON object per line.
    ///
    /// A journal that cannot be opened is dropped rather than reported:
    /// tracing is an aid, and an unwritable workspace must not fail the run.
    #[must_use]
    pub fn new(label: impl Into<String>, journal_path: Option<&Path>) -> Arc<Self> {
        let journal = journal_path
            .and_then(|path| {
                std::fs::OpenOptions::new()
                    .create(true)
                    .append(true)
                    .open(path)
                    .ok()
            })
            .map(Mutex::new);
        Arc::new(Self {
            label: label.into(),
            state: Arc::new(TraceState {
                started: Instant::now(),
                journal,
                model_calls: AtomicU64::new(0),
                tool_calls: AtomicU64::new(0),
                model_ms: AtomicU64::new(0),
                tool_ms: AtomicU64::new(0),
                input_tokens: AtomicU64::new(0),
                cached_tokens: AtomicU64::new(0),
                output_tokens: AtomicU64::new(0),
                micro_usd: AtomicU64::new(0),
            }),
        })
    }

    /// Returns a tracer for a nested run that shares this tracer's clock,
    /// counters, and journal but reports under its own label.
    #[must_use]
    pub fn child(&self, label: impl Into<String>) -> Arc<Self> {
        Arc::new(Self {
            label: label.into(),
            state: self.state.clone(),
        })
    }

    /// Returns the conventional journal path for a workspace.
    #[must_use]
    pub fn journal_path(workspace: &Path) -> PathBuf {
        workspace.join("trace.jsonl")
    }

    /// Records what one model call actually cost and who served it.
    ///
    /// The event stream cannot answer this. `ModelCompleted` carries token
    /// counts but names neither the provider that served the call nor the
    /// price, and with `allow_fallbacks` on, the provider varies per call —
    /// so "which route did this run actually use, and what did it cost" was
    /// unanswerable from the trace. The figures come from the response body,
    /// which is why this is reported by a model wrapper rather than derived
    /// from an event.
    pub fn record_model_cost(&self, accounting: &ModelAccounting) {
        self.state
            .output_tokens
            .fetch_add(accounting.output_tokens, Ordering::Relaxed);
        self.state
            .micro_usd
            .fetch_add(accounting.micro_usd(), Ordering::Relaxed);
        self.write_line(&serde_json::json!({
            "type": "model_accounting",
            "agent": accounting.agent,
            "provider": accounting.provider,
            "model": accounting.model,
            "input_tokens": accounting.input_tokens,
            "cached_tokens": accounting.cached_tokens,
            "output_tokens": accounting.output_tokens,
            "reasoning_tokens": accounting.reasoning_tokens,
            "usd": accounting.usd,
            "elapsed_ms": u64::try_from(self.state.started.elapsed().as_millis())
                .unwrap_or(u64::MAX),
        }));
    }

    /// Returns the run's accumulated cost in USD.
    #[must_use]
    pub fn spent_usd(&self) -> f64 {
        // Precision is lost only above 2^53 micro-USD, or nine billion dollars.
        #[expect(
            clippy::cast_precision_loss,
            reason = "a run would have to cost nine billion dollars to lose a cent"
        )]
        let usd = self.state.micro_usd.load(Ordering::Relaxed) as f64 / 1_000_000.0;
        usd
    }

    /// Prints one operator-facing progress line outside the event stream.
    pub fn note(&self, message: &str) {
        self.emit_line(message);
    }

    /// Returns how many model and tool calls every tracer in this tree has
    /// observed so far.
    #[must_use]
    pub fn counts(&self) -> (u64, u64) {
        (
            self.state.model_calls.load(Ordering::Relaxed),
            self.state.tool_calls.load(Ordering::Relaxed),
        )
    }

    /// Renders the cumulative time and cache profile for the whole run tree.
    ///
    /// Printed on every model completion because that is the moment the
    /// numbers change and the moment an operator is asking "why is this
    /// slow". `idle` is wall clock attributable to neither the provider nor a
    /// tool: scheduling, backoff sleeps, and waiting on a sibling agent.
    /// Renders the run's time attribution, cache rate, and spend.
    ///
    /// Two regimes, because one formula cannot describe both. With a single
    /// agent running, model + tool + idle partition the wall clock and idle is
    /// the diagnostic that matters: time in neither the provider nor a tool is
    /// backoff, scheduling, or waiting. Once agents run concurrently their
    /// summed time legitimately exceeds the wall clock, and reporting that as
    /// `model 103%` reads as a bug rather than as overlap. In that regime the
    /// percentages become shares of agent time and a concurrency factor
    /// replaces idle.
    fn profile(&self) -> String {
        let wall =
            u64::try_from(self.state.started.elapsed().as_millis().max(1)).unwrap_or(u64::MAX);
        let model = self.state.model_ms.load(Ordering::Relaxed);
        let tool = self.state.tool_ms.load(Ordering::Relaxed);
        let input = self.state.input_tokens.load(Ordering::Relaxed);
        let cached = self.state.cached_tokens.load(Ordering::Relaxed);

        format!(
            "profile {} | cache {}% | ${:.4}",
            attribution(wall, model, tool),
            share(cached, input),
            self.spent_usd()
        )
    }

    fn emit_line(&self, message: &str) {
        let elapsed = self.state.started.elapsed().as_secs();
        let mut stderr = std::io::stderr().lock();
        let _ = writeln!(
            stderr,
            "[{:02}:{:02}] {:<16} {message}",
            elapsed / 60,
            elapsed % 60,
            self.label
        );
        let _ = stderr.flush();
    }

    /// Appends one JSON object to the journal, if there is one.
    fn write_line(&self, line: &serde_json::Value) {
        let Some(journal) = self.state.journal.as_ref() else {
            return;
        };
        if let Ok(mut file) = journal.lock() {
            let _ = writeln!(file, "{line}");
            let _ = file.flush();
        }
    }

    fn write_journal(&self, record: &EventRecord) {
        let Some(journal) = self.state.journal.as_ref() else {
            return;
        };
        let Ok(mut line) = serde_json::to_value(record) else {
            return;
        };
        if let Some(object) = line.as_object_mut() {
            object.insert("agent".to_string(), serde_json::json!(self.label));
        }
        if let Ok(mut file) = journal.lock() {
            let _ = writeln!(file, "{line}");
            let _ = file.flush();
        }
    }
}

impl EventListener for RunTracer {
    fn on_event(&self, record: &EventRecord) {
        self.write_journal(record);
        match &record.event {
            AgentEvent::RunStarted { run_id, .. } => {
                self.emit_line(&format!("run started ({run_id})"));
            }
            AgentEvent::ModelStarted { model, .. } => {
                let count = self.state.model_calls.fetch_add(1, Ordering::Relaxed) + 1;
                self.emit_line(&format!("model call #{count} -> {model}"));
            }
            AgentEvent::ToolStarted { tool_name, .. } => {
                let count = self.state.tool_calls.fetch_add(1, Ordering::Relaxed) + 1;
                self.emit_line(&format!("tool  call #{count} -> {tool_name}"));
            }
            // Where the wall clock actually goes. Without this a run that is
            // waiting on one slow provider call and a run that is doing lots
            // of fast work look identical from the console: both just sit
            // there between events.
            AgentEvent::ModelCompleted {
                started_at_ms,
                usage,
                ..
            } => {
                let elapsed = started_at_ms
                    .and_then(|start| epoch_millis().and_then(|now| now.checked_sub(start)));
                if let Some(elapsed) = elapsed {
                    self.state.model_ms.fetch_add(elapsed, Ordering::Relaxed);
                }
                if let Some(usage) = usage {
                    self.state
                        .input_tokens
                        .fetch_add(usage.input_tokens, Ordering::Relaxed);
                    self.state
                        .cached_tokens
                        .fetch_add(usage.cache_read_tokens, Ordering::Relaxed);
                }
                let detail = usage.as_ref().map_or_else(String::new, |usage| {
                    format!(
                        " in={} cached={} out={}",
                        usage.input_tokens, usage.cache_read_tokens, usage.output_tokens
                    )
                });
                self.emit_line(&format!(
                    "model done    {}{detail} | {}",
                    elapsed.map_or_else(|| "?".to_string(), |ms| format!("{ms}ms")),
                    self.profile()
                ));
            }
            AgentEvent::ToolCompleted {
                tool_name,
                input,
                duration_ms,
                output_bytes,
                error,
                ..
            } => {
                let mut detail = format!("tool  done    {tool_name}");
                if let Some(duration) = duration_ms {
                    self.state.tool_ms.fetch_add(*duration, Ordering::Relaxed);
                    let _ = write!(detail, " in {duration}ms");
                }
                if let Some(bytes) = output_bytes {
                    let _ = write!(detail, ", {bytes} bytes");
                }
                if let Some(message) = error {
                    let _ = write!(detail, ", error: {message}");
                }
                if let Some(arguments) = input {
                    let _ = write!(detail, " | {}", preview(&arguments.to_string()));
                }
                self.emit_line(&detail);
            }
            AgentEvent::ToolFailed {
                tool_name, error, ..
            } => {
                self.emit_line(&format!("tool  failed  {tool_name}: {error}"));
            }
            // Retries and model failures were invisible on the console, so a
            // run could spend ten minutes silently exhausting its retry ladder
            // and look merely slow. These two lines are what turn that into an
            // obvious symptom.
            AgentEvent::RetryScheduled { call_id, attempt } => {
                self.emit_line(&format!("model RETRY   attempt {attempt} for {call_id}"));
            }
            AgentEvent::ModelFailed { error, .. } => {
                self.emit_line(&format!("model FAILED  {error}"));
            }
            _ => {}
        }
    }
}

/// Returns the current Unix time in milliseconds.
fn epoch_millis() -> Option<u64> {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .ok()
        .and_then(|elapsed| u64::try_from(elapsed.as_millis()).ok())
}

fn preview(text: &str) -> String {
    let collapsed = text.split_whitespace().collect::<Vec<_>>().join(" ");
    if collapsed.chars().count() <= CONSOLE_PREVIEW_CHARS {
        return collapsed;
    }
    let kept = collapsed
        .chars()
        .take(CONSOLE_PREVIEW_CHARS)
        .collect::<String>();
    format!("{kept}...")
}

/// Returns `part` as a whole-number percentage of `whole`.
fn share(part: u64, whole: u64) -> u64 {
    part.saturating_mul(100) / whole.max(1)
}

/// Renders how a run's time divides between the provider, tools, and waiting.
///
/// Kept a pure function of its three inputs so both regimes are testable
/// without a live clock.
fn attribution(wall: u64, model: u64, tool: u64) -> String {
    let busy = model.saturating_add(tool);
    if busy > wall {
        return format!(
            "model {}% tool {}% of agent time | concurrency x{}.{}",
            share(model, busy),
            share(tool, busy),
            busy / wall.max(1),
            (busy.saturating_mul(10) / wall.max(1)) % 10
        );
    }
    format!(
        "model {}% tool {}% idle {}%",
        share(model, wall),
        share(tool, wall),
        share(wall.saturating_sub(busy), wall)
    )
}

#[cfg(test)]
mod test;
