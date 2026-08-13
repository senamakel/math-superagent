//! Why a workflow cannot make arbitrary HTTP requests here.
//!
//! `TinyFlows`' `http_request` node reaches the outside world through the
//! required [`HttpClient`] capability. This crate supplies one that refuses.
//!
//! The argument is the same one [`super::execution`] makes about running
//! commands, applied to the network. Reaching the network here goes through a
//! tool — `exa_search` for discovery, the document tools for fetching and
//! reading a paper — and each of those bounds the response, records what was
//! fetched, and can be withheld: `MATH_AGENT_RESEARCH=off` withholds
//! `exa_search` by *not registering it*, because a prompt instruction is not a
//! control.
//!
//! An unbounded HTTP client reachable from any workflow node would undo all
//! three at once. Research gating would stop being a gate, because a workflow
//! could call the same endpoint directly. Nothing would bound the response, and
//! the size limits exist because an unbounded body is how a run loses its
//! context window to one page. And nothing would record the fetch, so the
//! request ledger the derivation cites would stop being complete.
//!
//! So the network stays behind the tools, where the gate and the ledger are.

use async_trait::async_trait;
use serde_json::Value;
use tinyflows::caps::HttpClient;
use tinyflows::error::{EngineError, Result as EngineResult};

/// An [`HttpClient`] that refuses, and says where to go instead.
#[derive(Clone, Copy, Debug, Default)]
pub(crate) struct RefusingHttpClient;

#[async_trait]
impl HttpClient for RefusingHttpClient {
    /// Always fails.
    ///
    /// # Errors
    ///
    /// Always returns a capability error naming the supported path. See the
    /// module documentation for why this is not a gap to be filled in later.
    async fn request(&self, _request: Value, _conn: Option<&str>) -> EngineResult<Value> {
        Err(EngineError::Capability(
            "this host does not make arbitrary HTTP requests from an `http_request` node: the \
             network is reached through tools that bound the response and record the fetch, and \
             that research gating can withhold. Use a `tool_call` node"
                .into(),
        ))
    }
}

#[cfg(test)]
#[path = "network_test.rs"]
mod test;
