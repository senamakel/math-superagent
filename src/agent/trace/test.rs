//! Unit tests for the shared run tracer.
#![allow(clippy::expect_used)]

use std::sync::Arc;

use tinyagents::harness::events::{AgentEvent, EventListener, EventRecord};
use tinyagents::harness::ids::{CallId, EventId, RunId};

use super::{CONSOLE_PREVIEW_CHARS, RunTracer, attribution, preview};

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

#[test]
fn the_profile_attributes_wall_clock_and_cache() {
    use std::sync::atomic::Ordering;

    let tracer = RunTracer::new("orchestrator", None);
    tracer.state.input_tokens.store(1000, Ordering::Relaxed);
    tracer.state.cached_tokens.store(250, Ordering::Relaxed);

    let profile = tracer.profile();
    assert!(profile.contains("model "), "{profile}");
    assert!(profile.contains("tool "), "{profile}");
    // Idle is the diagnostic that matters when one agent is running: time in
    // neither the provider nor a tool is backoff, scheduling, or waiting.
    assert!(profile.contains("idle "), "{profile}");
    assert!(profile.contains("cache 25%"), "{profile}");
    // Spend is reported even before anything has been charged.
    assert!(profile.contains("$0.0000"), "{profile}");
}

#[test]
fn one_agent_partitions_the_wall_clock_and_idle_is_visible() {
    // 200ms in the provider and 50ms in tools out of a 1s run: the remaining
    // 75% is backoff, scheduling, or waiting, which is the diagnostic.
    let rendered = attribution(1_000, 200, 50);
    assert_eq!(rendered, "model 20% tool 5% idle 75%");
}

#[test]
fn concurrent_agent_time_is_reported_as_overlap_not_as_over_100_percent() {
    // Three agents each spending a second inside the provider during one
    // second of wall clock. Their summed time legitimately exceeds it, and
    // rendering that as `model 300%` reads as a bug rather than as overlap.
    let rendered = attribution(1_000, 3_000, 0);
    assert!(rendered.contains("of agent time"), "{rendered}");
    assert!(rendered.contains("concurrency x3.0"), "{rendered}");
    assert!(rendered.contains("model 100%"), "{rendered}");
    assert!(!rendered.contains("idle"), "{rendered}");
}

#[test]
fn recorded_costs_accumulate_across_agents() {
    use super::ModelAccounting;

    let tracer = RunTracer::new("orchestrator", None);
    let child = tracer.child("tool_builder");
    for (agent, usd) in [("orchestrator", 0.001_25), ("tool_builder", 0.000_75)] {
        child.record_model_cost(&ModelAccounting {
            agent: agent.to_string(),
            usd,
            ..ModelAccounting::default()
        });
    }

    // Children share the parent's totals, so the run has one bill.
    assert!(
        (tracer.spent_usd() - 0.002).abs() < 1e-9,
        "{}",
        tracer.spent_usd()
    );
}

#[test]
fn a_middleware_that_short_circuits_leaves_no_line() {
    // Both hooks fire on both sides of every model and tool call, and the
    // events carry only a name. On one measured run they were 5,108 of 6,406
    // events and four fifths of a 24 MB journal, burying the model and tool
    // records an operator opens the trace to read.
    let directory =
        std::env::temp_dir().join(format!("math-agent-middleware-{}", std::process::id()));
    std::fs::create_dir_all(&directory).expect("temporary trace directory is creatable");
    let path = RunTracer::journal_path(&directory);
    let _ = std::fs::remove_file(&path);

    let tracer = RunTracer::new("reflection", Some(path.as_path()));
    for _ in 0..50 {
        tracer.on_event(&record(AgentEvent::MiddlewareStarted {
            name: "context_compression".to_string(),
        }));
        tracer.on_event(&record(AgentEvent::MiddlewareCompleted {
            name: "context_compression".to_string(),
        }));
    }
    let written = std::fs::read_to_string(&path).expect("trace journal is readable");
    assert!(
        written.is_empty(),
        "a hook that returned immediately did nothing worth a line, got: {written}"
    );

    // The run's end still accounts for every one of them, so suppressing the
    // lines cannot be mistaken for the hooks never having run.
    tracer.on_event(&record(AgentEvent::RunCompleted {
        run_id: RunId::new("run-1"),
    }));
    let written = std::fs::read_to_string(&path).expect("trace journal is readable");
    assert!(written.contains("middleware_summary"));
    assert!(written.contains("\"calls\":50"));
    let _ = std::fs::remove_dir_all(&directory);
}

#[test]
fn a_middleware_that_actually_works_is_recorded_where_it_happened() {
    let directory =
        std::env::temp_dir().join(format!("math-agent-middleware-slow-{}", std::process::id()));
    std::fs::create_dir_all(&directory).expect("temporary trace directory is creatable");
    let path = RunTracer::journal_path(&directory);
    let _ = std::fs::remove_file(&path);

    let tracer = RunTracer::new("orchestrator", Some(path.as_path()));
    tracer.on_event(&record(AgentEvent::MiddlewareStarted {
        name: "workspace_checkpoint".to_string(),
    }));
    std::thread::sleep(super::MIDDLEWARE_JOURNAL_THRESHOLD * 3);
    tracer.on_event(&record(AgentEvent::MiddlewareCompleted {
        name: "workspace_checkpoint".to_string(),
    }));

    let written = std::fs::read_to_string(&path).expect("trace journal is readable");
    assert!(written.contains("middleware_executed"));
    assert!(written.contains("workspace_checkpoint"));
    assert!(written.contains("duration_us"));
    let _ = std::fs::remove_dir_all(&directory);
}

#[test]
fn a_run_that_dies_says_so_on_the_console() {
    // A live `organizer` retried the same call six times over two and a half
    // minutes and then died on `openai response contained no choices`. The
    // retry ladder was visible and its outcome was not, so the run simply
    // stopped appearing. The error was in `trace.jsonl` the whole time, which
    // is the wrong place to need it.
    let directory =
        std::env::temp_dir().join(format!("math-agent-run-failed-{}", std::process::id()));
    std::fs::create_dir_all(&directory).expect("temporary trace directory is creatable");
    let path = RunTracer::journal_path(&directory);
    let _ = std::fs::remove_file(&path);

    let tracer = RunTracer::new("organizer", Some(path.as_path()));
    tracer.on_event(&record(AgentEvent::RunFailed {
        run_id: RunId::new("agent-run-13"),
        error: "model error: openai response contained no choices".into(),
    }));
    drop(Arc::try_unwrap(tracer).map(drop));

    let written = std::fs::read_to_string(&path).expect("trace journal is readable");
    assert!(written.contains("no choices"), "{written}");
    assert!(written.contains("agent-run-13"), "{written}");
    let _ = std::fs::remove_dir_all(&directory);
}
