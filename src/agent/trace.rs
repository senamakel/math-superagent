//! Live console and JSONL tracing for orchestrator and specialist runs.
//!
//! Without this the operator sees nothing between launching `./agent` and the
//! final answer, and Langfuse only receives the orchestrator's own events
//! because specialist runs are executed on a bare context. `RunTracer` is one
//! listener shared by every run in the tree, so a single stream shows which
//! agent is working, which tool it called, how long the call took, and how much
//! it returned.

use std::io::Write as _;
use std::path::{Path, PathBuf};
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::{Arc, Mutex};
use std::time::Instant;

use tinyagents::harness::events::{AgentEvent, EventListener, EventRecord};

/// Maximum characters of a tool argument or result echoed to the console.
const CONSOLE_PREVIEW_CHARS: usize = 240;

/// A shared listener that prints a compact live trace and appends full event
/// records to a JSONL file inside the workspace.
pub struct RunTracer {
    started: Instant,
    label: Mutex<String>,
    journal: Option<Mutex<std::fs::File>>,
    model_calls: AtomicU64,
    tool_calls: AtomicU64,
}

impl std::fmt::Debug for RunTracer {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("RunTracer")
            .field("model_calls", &self.model_calls.load(Ordering::Relaxed))
            .field("tool_calls", &self.tool_calls.load(Ordering::Relaxed))
            .field("journalled", &self.journal.is_some())
            .finish()
    }
}

impl RunTracer {
    /// Creates a tracer that prints to stderr and, when `journal_path` is
    /// writable, appends every event as one JSON object per line.
    ///
    /// A journal that cannot be opened is dropped rather than reported: tracing
    /// is an aid, and a read-only or full workspace must not fail the run.
    #[must_use]
    pub fn new(journal_path: Option<&Path>) -> Arc<Self> {
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
            started: Instant::now(),
            label: Mutex::new("orchestrator".to_string()),
            journal,
            model_calls: AtomicU64::new(0),
            tool_calls: AtomicU64::new(0),
        })
    }

    /// Returns the conventional journal path for a workspace.
    #[must_use]
    pub fn journal_path(workspace: &Path) -> PathBuf {
        workspace.join("trace.jsonl")
    }

    /// Names the agent whose events follow. Specialist runs set this on spawn
    /// so console lines identify the working agent rather than the harness.
    pub fn set_label(&self, label: impl Into<String>) {
        if let Ok(mut current) = self.label.lock() {
            *current = label.into();
        }
    }

    /// Prints one operator-facing progress line outside the event stream.
    pub fn note(&self, message: &str) {
        self.emit_line(&self.current_label(), message);
    }

    /// Returns how many model and tool calls the tracer has observed.
    #[must_use]
    pub fn counts(&self) -> (u64, u64) {
        (
            self.model_calls.load(Ordering::Relaxed),
            self.tool_calls.load(Ordering::Relaxed),
        )
    }

    fn current_label(&self) -> String {
        self.label
            .lock()
            .map(|label| label.clone())
            .unwrap_or_else(|_| "agent".to_string())
    }

    fn emit_line(&self, label: &str, message: &str) {
        let elapsed = self.started.elapsed().as_secs();
        let mut stderr = std::io::stderr().lock();
        let _ = writeln!(
            stderr,
            "[{:02}:{:02}] {label:<14} {message}",
            elapsed / 60,
            elapsed % 60
        );
        let _ = stderr.flush();
    }

    fn write_journal(&self, record: &EventRecord) {
        let Some(journal) = self.journal.as_ref() else {
            return;
        };
        let Ok(line) = serde_json::to_string(record) else {
            return;
        };
        if let Ok(mut file) = journal.lock() {
            let _ = writeln!(file, "{line}");
            let _ = file.flush();
        }
    }
}

impl EventListener for RunTracer {
    fn on_event(&self, record: &EventRecord) {
        self.write_journal(record);
        let label = self.current_label();
        match &record.event {
            AgentEvent::RunStarted { run_id, .. } => {
                self.emit_line(&label, &format!("run started ({run_id})"));
            }
            AgentEvent::ModelStarted { model, .. } => {
                let count = self.model_calls.fetch_add(1, Ordering::Relaxed) + 1;
                self.emit_line(&label, &format!("model call #{count} -> {model}"));
            }
            AgentEvent::ToolStarted { tool_name, .. } => {
                let count = self.tool_calls.fetch_add(1, Ordering::Relaxed) + 1;
                self.emit_line(&label, &format!("tool  call #{count} -> {tool_name}"));
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
                self.emit_line(&label, &detail);
            }
            AgentEvent::ToolFailed {
                tool_name, error, ..
            } => {
                self.emit_line(&label, &format!("tool  failed  {tool_name}: {error}"));
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
