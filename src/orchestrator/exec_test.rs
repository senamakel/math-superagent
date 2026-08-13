//! Unit tests for the shell tool's output bounding and timeout behaviour.
#![allow(clippy::expect_used)]

use std::time::{Duration, Instant};

use super::{
    COMMAND_LOG, COMMAND_LOG_ENTRY_BYTES, COMMAND_LOG_MARK, COMMAND_LOG_MAX_BYTES, Capture,
    ExecuteCommand, MAX_COMMAND_OUTPUT_BYTES, clipped, trimmed,
};

/// A workspace of this test's own, so one test's log is not another's.
fn workspace_named(name: &str) -> std::path::PathBuf {
    let path = std::env::temp_dir().join(format!("exec-test-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).expect("the test workspace is created");
    path
}

fn captured(bytes: &[u8], chunk: usize) -> Capture {
    let mut capture = Capture::default();
    for piece in bytes.chunks(chunk) {
        capture.push(piece);
    }
    capture
}

#[test]
fn output_that_fits_is_passed_through_untouched() {
    assert_eq!(captured(b"answer: 661\n", 4).render(), "answer: 661\n");
}

#[test]
fn oversized_command_output_keeps_the_end_where_the_answer_is() {
    // A verification script prints its working first and its conclusion last.
    // Keeping only the head discarded the answer of a run that had computed it.
    let mut raw = b"START-OF-RUN\n".to_vec();
    raw.resize(MAX_COMMAND_OUTPUT_BYTES * 2, b'x');
    raw.extend_from_slice(b"\n[final answer] 4,3,1\n");

    let rendered = captured(&raw, 7_000).render();
    assert!(
        rendered.contains("[final answer] 4,3,1"),
        "the tail must survive"
    );
    assert!(rendered.contains("START-OF-RUN"), "the head must survive");
    assert!(rendered.contains("truncated from the middle"));
}

#[test]
fn the_kept_window_does_not_grow_with_the_length_of_the_stream() {
    // The bound is on memory, not only on what the model reads. A `Vec` grown
    // to the full stream and shortened afterwards is what OOM-killed a live
    // container, so the retained bytes must stay flat as the stream grows.
    let mut capture = Capture::default();
    let chunk = vec![b'y'; 16 * 1024];
    for _ in 0..512 {
        capture.push(&chunk);
    }
    assert_eq!(capture.total, 512 * 16 * 1024);
    assert_eq!(
        capture.head.len() + capture.tail.len(),
        MAX_COMMAND_OUTPUT_BYTES,
        "8 MiB of output must be held in one 64 KiB window"
    );
    assert!(capture.render().len() < MAX_COMMAND_OUTPUT_BYTES + 200);
}

#[test]
fn the_boundary_between_the_two_kept_ends_is_exact() {
    // Exactly the budget: nothing is dropped, so the render must be the input
    // rather than the input with a truncation notice wedged into the middle.
    let raw = vec![b'z'; MAX_COMMAND_OUTPUT_BYTES];
    let rendered = captured(&raw, 1_000).render();
    assert_eq!(rendered.len(), MAX_COMMAND_OUTPUT_BYTES);
    assert!(!rendered.contains("truncated"));

    // One byte more, and the notice appears with a count of one.
    let mut raw = raw;
    raw.push(b'z');
    assert!(
        captured(&raw, 1_000)
            .render()
            .contains("[1 bytes truncated")
    );
}

#[test]
fn invalid_utf8_is_rendered_lossily_rather_than_refused() {
    // A program that prints one bad byte has still told the run something.
    let rendered = captured(&[b'o', b'k', 0xff, b'!'], 1).render();
    assert!(rendered.starts_with("ok"));
    assert!(rendered.ends_with('!'));
}

#[tokio::test]
async fn a_command_that_outlives_its_ceiling_still_returns_what_it_printed() {
    let workspace = std::env::temp_dir();
    let tool = ExecuteCommand::new(workspace, Duration::from_millis(300));
    let output = tool
        .run("echo started; sleep 30")
        .await
        .expect("the command runs");
    assert!(output.status.is_none(), "a killed command has no exit code");
    assert!(
        output.stdout.render().contains("started"),
        "what it printed before the ceiling is evidence and must survive"
    );
}

#[tokio::test]
async fn a_timed_out_command_that_forked_does_not_hold_the_tool_open() {
    // Killing the shell alone left descendants holding the inherited pipe write
    // ends, so `read_to_end` never returned and the call hung well past its own
    // ceiling. The group is signalled, and the drains are bounded besides.
    let workspace = std::env::temp_dir();
    let tool = ExecuteCommand::new(workspace, Duration::from_millis(300));
    let started = Instant::now();
    let output = tool
        .run("sleep 120 & echo forked; sleep 120")
        .await
        .expect("the command runs");
    let elapsed = started.elapsed();
    assert!(output.status.is_none());
    assert!(
        elapsed < Duration::from_secs(20),
        "the call returned in {elapsed:?}; a surviving descendant must not hold the pipes open"
    );
    assert!(output.stdout.render().contains("forked"));
}

#[tokio::test]
async fn a_command_that_exits_reports_its_code() {
    let tool = ExecuteCommand::new(std::env::temp_dir(), Duration::from_secs(30));
    let output = tool.run("exit 3").await.expect("the command runs");
    assert_eq!(output.status.and_then(|status| status.code()), Some(3));
}

/// Running a program has to leave something behind. Output that reached only
/// the model died with the attempt at `DEFAULT_RUN_MINUTES`, and a live run
/// executed two programs for 2 KB of results while `code/out/` stayed empty.
#[tokio::test]
async fn what_a_command_printed_is_written_to_the_workspace() {
    let workspace = workspace_named("records-output");
    let tool = ExecuteCommand::new(workspace.clone(), Duration::from_secs(30));
    let output = tool
        .run("echo 'genus is 0'")
        .await
        .expect("the command runs");
    tool.record(
        "echo 'genus is 0'",
        "0",
        &output.stdout.render(),
        &output.stderr.render(),
    )
    .await;

    let log = std::fs::read_to_string(workspace.join(COMMAND_LOG)).expect("the log is written");
    assert!(log.contains("echo 'genus is 0'"), "the command is recorded");
    assert!(log.contains("genus is 0"), "what it printed is recorded");
    assert!(log.contains("exit: 0"), "how it ended is recorded");
}

/// A killed command is evidence about the method, so its partial output is
/// recorded with the timeout rather than dropped.
#[tokio::test]
async fn a_killed_command_still_leaves_its_partial_output() {
    let workspace = workspace_named("records-a-kill");
    let tool = ExecuteCommand::new(workspace.clone(), Duration::from_millis(300));
    let output = tool
        .run("echo 'reached M=200'; sleep 30")
        .await
        .expect("the command runs");
    assert!(output.status.is_none());
    tool.record(
        "python3 search.py",
        "timed out after 540 seconds, killed",
        &output.stdout.render(),
        &output.stderr.render(),
    )
    .await;

    let log = std::fs::read_to_string(workspace.join(COMMAND_LOG)).expect("the log is written");
    assert!(log.contains("reached M=200"), "how far it got must survive");
    assert!(log.contains("timed out"), "and that it was killed");
}

/// Workspace contents are committed, so the log has a ceiling. It is enforced
/// by dropping whole entries from the front: the newest run is the one the next
/// attempt needs.
#[test]
fn the_log_drops_whole_entries_from_the_front_once_it_is_full() {
    let filler = "x".repeat(COMMAND_LOG_MAX_BYTES);
    let log = format!("{COMMAND_LOG_MARK}$ old\n{filler}{COMMAND_LOG_MARK}$ newest\nexit: 0\n");
    let kept = trimmed(log);

    assert!(kept.len() <= COMMAND_LOG_MAX_BYTES, "the ceiling is enforced");
    assert!(kept.contains("$ newest"), "the most recent entry is kept");
    assert!(!kept.contains("$ old"), "the oldest entry is dropped");
    assert!(
        kept.starts_with(COMMAND_LOG_MARK),
        "a trim cuts at an entry boundary, not mid-entry"
    );
}

/// One entry over the whole ceiling is kept rather than cut mid-character;
/// the next append trims it. A statement full of `x₂P` would not survive a
/// byte-offset cut.
#[test]
fn a_single_oversized_entry_is_not_cut_mid_character() {
    let log = format!("{COMMAND_LOG_MARK}$ one\n{}", "π".repeat(COMMAND_LOG_MAX_BYTES));
    assert!(trimmed(log.clone()) == log);
}

/// A clipped stream keeps its end, for the same reason the model's rendering
/// does: a program prints its conclusion last.
#[test]
fn a_clipped_stream_keeps_the_conclusion() {
    let text = format!("{}\n[final] rank <= 3\n", "y".repeat(COMMAND_LOG_ENTRY_BYTES * 2));
    let short = clipped(&text);

    assert!(short.len() <= COMMAND_LOG_ENTRY_BYTES + 64);
    assert!(short.contains("[final] rank <= 3"), "the conclusion survives");
    assert!(short.starts_with("[earlier output dropped]"), "and the cut is stated");
}
