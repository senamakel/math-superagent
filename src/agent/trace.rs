//! Live console and JSONL tracing for orchestrator and specialist runs.
//!
//! Without this the operator sees nothing between launching `./agent` and the
//! final answer, and Langfuse only receives the orchestrator's own events
//! because specialist runs are executed on a bare context. A `RunTracer` is
//! attached to every run in the tree. Each one carries a fixed label so
//! concurrent specialists stay distinguishable, and all of them share one
//! start time, one counter pair, and one journal file, so the console shows a
//! single ordered stream of the whole investigation.

use std::io::Write as _;
use std::path::{Path, PathBuf};
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::{Arc, Mutex};
use std::time::Instant;

use tinyagents::harness::events::{AgentEvent, EventListener, EventRecord};

/// Maximum characters of a tool argument echoed to the console.
const CONSOLE_PREVIEW_CHARS: usize = 240;

/// State shared by every tracer in one investigation.
#[derive(Debug)]
struct TraceState {
    started: Instant,
    journal: Option<Mutex<std::fs::File>>,
    model_calls: AtomicU64,
    tool_calls: AtomicU64,
}

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
                    detail.push_str(&format!(" in {duration}ms"));
                }
                if let Some(bytes) = output_bytes {
                    detail.push_str(&format!(", {bytes} bytes"));
                }
                if let Some(message) = error {
                    detail.push_str(&format!(", error: {message}"));
                }
                if let Some(arguments) = input {
                    detail.push_str(&format!(" | {}", preview(&arguments.to_string())));
                }
                self.emit_line(&detail);
            }
            AgentEvent::ToolFailed {
                tool_name, error, ..
            } => {
                self.emit_line(&format!("tool  failed  {tool_name}: {error}"));
            }
            _ => {}
        }
    }
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

#[cfg(test)]
mod test;
