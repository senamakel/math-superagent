//! Unit tests for the shared run tracer.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use tinyagents::harness::events::{AgentEvent, EventListener, EventRecord};
use tinyagents::harness::ids::{CallId, EventId, RunId};

use super::{CONSOLE_PREVIEW_CHARS, RunTracer, preview};

fn record(event: AgentEvent) -> EventRecord {
    EventRecord {
        id: EventId::new("evt-0"),
        offset: 0,
        event,
    }
}

#[test]
fn children_share_the_parent_counters_and_clock() {
    let parent = RunTracer::new("orchestrator", None);
    let child = parent.child("tool_builder");

    parent.on_event(&record(AgentEvent::ModelStarted {
        call_id: CallId::new("call-1"),
        model: "openrouter".to_string(),
    }));
    child.on_event(&record(AgentEvent::ToolStarted {
        call_id: CallId::new("call-2"),
        tool_name: "execute_command".to_string(),
    }));

    assert_eq!(parent.counts(), (1, 1));
    assert_eq!(child.counts(), (1, 1));
}

#[test]
fn journal_records_every_event_with_its_agent_label() {
    let directory = std::env::temp_dir().join(format!("math-agent-trace-{}", std::process::id()));
    std::fs::create_dir_all(&directory).expect("temporary trace directory is creatable");
    let path = RunTracer::journal_path(&directory);
    let _ = std::fs::remove_file(&path);

    let tracer = RunTracer::new("research", Some(path.as_path()));
    tracer.on_event(&record(AgentEvent::RunStarted {
        run_id: RunId::new("run-1"),
        thread_id: None,
    }));
    drop(Arc::try_unwrap(tracer).map(drop));

    let written = std::fs::read_to_string(&path).expect("trace journal is readable");
    assert!(written.contains("\"agent\":\"research\""));
    assert!(written.contains("run-1"));
    let _ = std::fs::remove_dir_all(&directory);
}

#[test]
fn preview_collapses_whitespace_and_bounds_length() {
    assert_eq!(preview("a\n  b\tc"), "a b c");
    let long = "x".repeat(CONSOLE_PREVIEW_CHARS * 2);
    let shortened = preview(&long);
    assert!(shortened.ends_with("..."));
    assert_eq!(shortened.chars().count(), CONSOLE_PREVIEW_CHARS + 3);
}
