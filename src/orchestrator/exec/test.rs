//! Unit tests for the shell tool's output bounding and timeout behaviour.
#![allow(clippy::expect_used)]

use std::time::{Duration, Instant};

use super::{Capture, ExecuteCommand, MAX_COMMAND_OUTPUT_BYTES, validate_complexity};

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
    assert!(captured(&raw, 1_000).render().contains("[1 bytes truncated"));
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

#[test]
fn a_bounded_oracle_may_declare_an_intractable_class() {
    validate_complexity("factorial in n", "factorial", Some("n <= 7"))
        .expect("a declared bound is what makes brute force legitimate");
}

#[test]
fn an_unbounded_intractable_class_is_refused() {
    assert!(validate_complexity("exponential", "exponential", None).is_err());
    assert!(validate_complexity("exponential", "exponential", Some("  ")).is_err());
}

#[test]
fn prose_disagreeing_with_the_class_is_refused() {
    // `polynomial (O((n!)²))` is how the notation check was once defeated.
    assert!(validate_complexity("polynomial (O((n!)^2))", "polynomial", None).is_err());
}

#[test]
fn a_search_strategy_named_instead_of_a_cost_is_refused_and_points_at_the_solver() {
    let refusal = validate_complexity("backtracking with pruning", "polynomial", None)
        .expect_err("naming a search strategy states no quantity");
    assert!(
        refusal.to_string().contains("sat_solver"),
        "a gate that blocks the wrong method must name the right one"
    );
}

#[test]
fn enumerating_divisors_is_an_honest_polynomial_description() {
    validate_complexity("O(sqrt(n)) time, O(1) space, enumerate divisors", "polynomial", None)
        .expect("refusing this would punish accuracy");
}
