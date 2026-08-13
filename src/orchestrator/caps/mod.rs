//! This crate's runtime, offered to `TinyFlows` as a capability bundle.
//!
//! `TinyFlows` runs no agent loop, executes nothing, and stores nothing. Every
//! effect a workflow has on the world goes through a trait the embedding host
//! implements, and this module is this crate's side of that: the
//! [`Capabilities`] bundle a workflow run is handed.
//!
//! Each implementation is an adapter over something that already exists here,
//! not a second copy of it. That is deliberate — two implementations of "run an
//! agent" or "call a tool" would drift, and the one a workflow reached would be
//! the one nobody was testing.
//!
//! | Capability | Backed by | Where |
//! |---|---|---|
//! | `tools` | the tool registry | [`tools`] |
//! | `state` | the workspace | [`state`] |
//! | `code` | *refused on purpose* | [`execution`] |
//! | `shell` | *not supplied on purpose* | [`execution`] |
//! | `tasks` | `AsyncSubagentManager` | [`super::runner`] |
//! | `llm`, `memory`, `agent`, `resolver` | still to come | — |
//!
//! # What is deliberately missing
//!
//! Execution. A `code` node is refused and a `shell` node has no runner,
//! because running a command here means declaring its complexity class first —
//! the enforcement of the method policy — and a second execution path would
//! skip that check. [`execution`] carries the full argument. A workflow that
//! needs to run something calls the `execute_command` tool like everything else
//! does.

pub(crate) mod execution;
pub(crate) mod state;
pub(crate) mod tools;

#[cfg(test)]
#[path = "caps_test.rs"]
mod test;
