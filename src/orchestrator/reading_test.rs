//! Unit tests for the reading layer's configuration.
#![allow(clippy::expect_used)]

use super::{
    DEFAULT_CHUNK_BYTES, DEFAULT_MAX_CHUNKS, DEFAULT_SLICE_BYTES, DEFAULT_UNSELECTED_BYTES,
    chunk_bytes, concurrency, enabled_from, max_chunks, slice_ceiling, slice_from,
    unselected_ceiling,
};

#[test]
fn an_unset_flag_leaves_the_recursive_read_in_place() {
    // Every ordinary run. The recursion is opt-out, not opt-in: a run that
    // never heard of the flag gets the whole reading layer.
    assert!(enabled_from(""));
}

#[test]
fn the_flag_is_read_the_way_every_other_off_switch_here_is() {
    for off in ["off", "OFF", "0", "false", "No", " disabled "] {
        assert!(!enabled_from(off), "`{off}` should withhold the tool");
    }
    for on in ["on", "1", "true", "yes", "anything else"] {
        assert!(enabled_from(on), "`{on}` should leave the tool in place");
    }
}

#[test]
fn the_slice_bound_can_never_fall_below_the_ceiling() {
    // Otherwise naming a section returns less than not naming one, which reads
    // as the selection having gone wrong rather than as a misconfiguration.
    assert_eq!(slice_from(8 * 1024, 64 * 1024), 64 * 1024);
    assert_eq!(slice_from(64 * 1024, 8 * 1024), 64 * 1024);
}

#[test]
fn every_knob_falls_back_to_its_default() {
    // The suite runs with none of these set, so this is the shipped
    // configuration — and it pins that a mistyped override cannot silently
    // produce a zero bound, which would turn a limit into a refusal of
    // everything. The flag is left out on purpose: an operator running the
    // suite under `MATH_AGENT_RLM=off` should get a green suite, not a report
    // that the runtime is broken. `enabled_from` covers the decision itself.
    assert_eq!(unselected_ceiling(), DEFAULT_UNSELECTED_BYTES);
    assert_eq!(slice_ceiling(), DEFAULT_SLICE_BYTES);
    assert_eq!(chunk_bytes(), DEFAULT_CHUNK_BYTES);
    assert_eq!(max_chunks(), DEFAULT_MAX_CHUNKS);
    assert!(concurrency() > 0);
}

#[test]
fn the_defaults_are_ordered_so_a_selected_read_sees_more_than_an_unselected_one() {
    const { assert!(DEFAULT_SLICE_BYTES > DEFAULT_UNSELECTED_BYTES) };
}
