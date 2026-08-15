//! Every knob on how a document that does not fit is read, in one place.
//!
//! The reading layer is three cooperating pieces — [`super::outline`]'s
//! ceiling, its slice bound, and [`super::recursive`]'s chunked read — and
//! they were three sets of constants in two files. That is the shape this
//! repository keeps having to undo: a second list is a second answer, and an
//! operator asking "how much of a file can a role see" had to read both
//! modules to find out.
//!
//! # Why the recursion is the one that switches off
//!
//! The ceiling is a *control*. It stops a single call putting a hundred
//! thousand tokens into a context window, costs nothing, and is on for every
//! run — an operator who wants more raises it rather than removing it.
//!
//! The recursion is a *spend*. One `map_document` over a 428 KB source is
//! eighteen provider calls that the caller did not individually authorise, and
//! there are runs where that is the wrong trade: a cheap model behind
//! `OPENROUTER_MODEL` where eighteen chunk reads cost more than they are worth,
//! a calibration run being measured on what the harness can do without it, or
//! an offline reproduction where the run must not spend at all. So it is
//! optional, and `MATH_AGENT_RLM=off` withholds it.
//!
//! Withheld by **not registering the tool**, never by asking the model to
//! abstain — the same enforcement as `MATH_AGENT_RESEARCH`, and for the same
//! reason. A run without it still has the outline, the selected read and the
//! search, so a large document stays readable; what it loses is the ability to
//! ask one question of a whole file.
//!
//! # The rule every override follows
//!
//! A missing, empty, unparsable or zero value keeps the default. An operator
//! who mistypes a number gets the runtime's judgement rather than a failed
//! start or, worse, a silent zero that turns a bound into a refusal of
//! everything.

use crate::agent::budget::positive_env;

/// Names the flag that withholds the recursive read.
const RECURSION_VAR: &str = "MATH_AGENT_RLM";

/// How much of a document one unselected `read_document` may return.
///
/// Set at the size of a long note rather than of a short paper: everything the
/// run writes about itself — a belief, an approach, a thread — is comfortably
/// below it and reads exactly as it did before, and everything above it is a
/// source or a derived ledger that has structure worth navigating.
const DEFAULT_UNSELECTED_BYTES: usize = 24 * 1024;

/// How much text one *selected* read may return.
///
/// Larger than [`DEFAULT_UNSELECTED_BYTES`], because a caller naming a range
/// has said what it wants and a section that happens to be long is not an
/// accident. It is still bounded: the bound is what makes "read it in ranges"
/// terminate rather than being one `lines: "1-"` away from the behaviour the
/// ceiling exists to remove.
const DEFAULT_SLICE_BYTES: usize = 48 * 1024;

/// Bytes of source one chunk read sees.
///
/// Roughly six thousand tokens: small enough that a model attends to all of it
/// rather than to its ends, and large enough that a section of a paper usually
/// survives inside one chunk instead of being cut across two.
const DEFAULT_CHUNK_BYTES: usize = 24 * 1024;

/// Chunks one `map_document` call will read.
///
/// At [`DEFAULT_CHUNK_BYTES`] this covers a 1.5 MB region — every document in a
/// live workspace, with room over. A region larger than this is answered over
/// the first sixty chunks and *says* so, because a partial answer presented as
/// a complete one is the failure that tool exists to avoid.
const DEFAULT_MAX_CHUNKS: usize = 60;

/// Chunk reads in flight at once.
///
/// The container shares one provider connection pool with the run that is
/// waiting on the tool, and sixty concurrent requests would starve it.
const DEFAULT_CONCURRENCY: usize = 6;

/// Reads a `usize` override, keeping `default` unless the value is a positive
/// number the platform can hold.
fn bytes(name: &str, default: usize) -> usize {
    positive_env(name)
        .and_then(|value| usize::try_from(value).ok())
        .unwrap_or(default)
}

/// Decides the recursion flag from a raw variable value.
///
/// Split from [`recursion_enabled`] so the decision can be tested without
/// setting a process-wide variable — `set_var` is `unsafe`, and `unsafe` is
/// forbidden in this crate. Same reason [`super::dossier`] splits its budget.
fn enabled_from(value: &str) -> bool {
    !matches!(
        value.trim().to_ascii_lowercase().as_str(),
        "off" | "0" | "false" | "no" | "disabled"
    )
}

/// Returns whether `map_document` is registered this run.
///
/// `MATH_AGENT_RLM=off` withholds it. Every other value — including an unset
/// variable, which is every ordinary run — leaves it in place.
pub(super) fn recursion_enabled() -> bool {
    enabled_from(&std::env::var(RECURSION_VAR).unwrap_or_default())
}

/// The unselected-read ceiling, overridable with `MATH_AGENT_READ_CEILING`.
pub(super) fn unselected_ceiling() -> usize {
    bytes("MATH_AGENT_READ_CEILING", DEFAULT_UNSELECTED_BYTES)
}

/// The selected-read bound, overridable with `MATH_AGENT_READ_SLICE`.
///
/// Held at or above [`unselected_ceiling`] by [`slice_from`].
pub(super) fn slice_ceiling() -> usize {
    slice_from(
        bytes("MATH_AGENT_READ_SLICE", DEFAULT_SLICE_BYTES),
        unselected_ceiling(),
    )
}

/// Holds the slice bound at or above the unselected ceiling.
///
/// An operator who raises the ceiling and forgets this would otherwise get a
/// runtime where naming a section returns *less* than not naming one, which
/// reads as the selection having gone wrong rather than as a misconfiguration.
fn slice_from(slice: usize, ceiling: usize) -> usize {
    slice.max(ceiling)
}

/// Bytes one chunk read sees, overridable with `MATH_AGENT_RLM_CHUNK_BYTES`.
pub(super) fn chunk_bytes() -> usize {
    bytes("MATH_AGENT_RLM_CHUNK_BYTES", DEFAULT_CHUNK_BYTES)
}

/// Chunks one call reads, overridable with `MATH_AGENT_RLM_MAX_CHUNKS`.
pub(super) fn max_chunks() -> usize {
    bytes("MATH_AGENT_RLM_MAX_CHUNKS", DEFAULT_MAX_CHUNKS)
}

/// Chunk reads in flight, overridable with `MATH_AGENT_RLM_CONCURRENCY`.
pub(super) fn concurrency() -> usize {
    bytes("MATH_AGENT_RLM_CONCURRENCY", DEFAULT_CONCURRENCY)
}

#[cfg(test)]
#[path = "reading_test.rs"]
mod test;
