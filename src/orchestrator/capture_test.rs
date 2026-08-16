#![allow(clippy::expect_used)]

use super::{Capture, clamp};

#[test]
fn a_short_stream_survives_whole() {
    let mut capture = Capture::bounded(1024);
    capture.push(b"hello world");
    assert_eq!(capture.render(), "hello world");
    assert_eq!(capture.total(), 11);
}

#[test]
fn chunk_boundaries_do_not_change_what_is_kept() {
    let payload: Vec<u8> = (0..4096_u32).map(|byte| (byte % 251) as u8).collect();

    let mut whole = Capture::bounded(256);
    whole.push(&payload);

    let mut piecewise = Capture::bounded(256);
    for chunk in payload.chunks(7) {
        piecewise.push(chunk);
    }

    assert_eq!(whole.render(), piecewise.render());
    assert_eq!(whole.total(), piecewise.total());
}

#[test]
fn both_ends_are_kept_and_the_middle_is_reported() {
    let payload = format!("START{}END", "x".repeat(4096));
    let mut capture = Capture::bounded(256);
    capture.push(payload.as_bytes());
    let rendered = capture.render();

    assert!(rendered.starts_with("START"), "the head is lost: {rendered}");
    assert!(rendered.ends_with("END"), "the tail is lost: {rendered}");
    assert!(
        rendered.contains("bytes truncated from the middle"),
        "a truncated render must say so: {rendered}"
    );
}

#[test]
fn the_tail_keeps_the_larger_share() {
    // A caller that reads one thing reads the end, so a bound must not spend
    // itself on the prefix. This is the property the module documents.
    let payload = vec![b'z'; 100_000];
    let mut capture = Capture::bounded(1024);
    capture.push(&payload);
    let rendered = capture.render();
    let (head, tail) = rendered
        .split_once("\n[")
        .expect("a truncated render carries the marker");
    let tail = tail.split_once("]\n").expect("the marker closes").1;
    assert!(
        tail.len() > head.len(),
        "head {} should be smaller than tail {}",
        head.len(),
        tail.len()
    );
}

#[test]
fn the_kept_window_does_not_grow_with_the_length_of_the_stream() {
    // The bound is on memory, not only on what a caller reads. A `Vec` grown to
    // the full stream and shortened afterwards is what OOM-killed a live
    // container, so the retained bytes must stay flat as the stream grows.
    // Asserted on the two buffers rather than on the render, because the render
    // is a copy and a leak would not show up in its length.
    const BUDGET: usize = 64 * 1024;
    let mut capture = Capture::bounded(BUDGET);
    let chunk = vec![b'y'; 16 * 1024];
    for _ in 0..512 {
        capture.push(&chunk);
    }
    assert_eq!(capture.total, 512 * 16 * 1024);
    assert_eq!(
        capture.head.len() + capture.tail.len(),
        BUDGET,
        "8 MiB of output must be held in one 64 KiB window"
    );
}

#[test]
fn total_counts_what_was_dropped_not_what_was_kept() {
    let mut capture = Capture::bounded(64);
    capture.push(&vec![b'a'; 10_000]);
    assert_eq!(capture.total(), 10_000);
}

#[test]
fn clamping_a_short_string_is_the_identity() {
    assert_eq!(clamp("short", 1024), "short");
}

#[test]
fn clamping_a_long_string_bounds_it_and_says_so() {
    let clamped = clamp(&"y".repeat(50_000), 512);
    assert!(clamped.len() < 50_000);
    assert!(clamped.contains("bytes truncated from the middle"));
}

#[test]
fn a_zero_budget_does_not_panic() {
    // `bounded(0)` is degenerate but reachable if a caller computes a budget.
    // It must clamp rather than divide by zero or loop forever draining a
    // tail it can never shrink.
    let mut capture = Capture::bounded(0);
    capture.push(b"anything at all");
    let rendered = capture.render();
    assert!(rendered.contains("truncated"), "{rendered}");
}

#[test]
fn invalid_utf8_is_rendered_lossily_rather_than_refused() {
    let mut capture = Capture::bounded(1024);
    capture.push(&[0xff, 0xfe, b'o', b'k']);
    assert!(capture.render().contains("ok"));
}
