//! The run's durable brain, its project-scoped session memory, its library,
//! and its provisional scratch — over whichever memory engine is selected.
//!
//! Four stores, and the separation between them is the point. The brain holds
//! what survived checking. The sessions hold this project's completed agent
//! runs. The library holds every source the run downloaded. The *scratch* holds
//! the half-finished arithmetic a run produces on the way to a result — what
//! `SCRATCHPAD.md` used to be — and it is deliberately not reachable from
//! `recall_memory` or `relate_memory`: provisional work is not durable
//! knowledge, and a half-finished calculation surfacing as one is how a run
//! comes to believe something nobody verified.
//!
//! # Two engines, one façade
//!
//! [`VectorStore`] is an enum rather than a trait object, and the reason is the
//! rule this repository keeps everywhere else: the set of engines is fixed for
//! a build, so a `match` is exhaustive and a new engine cannot be added without
//! every operation being answered for it. A trait would let one be added with
//! half its methods delegating to a default that quietly does nothing, which is
//! the shape of the failure `docs/memory.md` records — a memory that reports
//! storing and stores nothing.
//!
//! The name is unchanged because it is threaded through ten modules that have
//! no business knowing which engine is behind it. What *did* change is the
//! vocabulary at the boundary: [`Lookup`] replaced the raw Cognee search-type
//! strings the tools used to pass down. A tool asking for `"CHUNKS"` was a tool
//! that could only ever have one engine underneath it, and the string was
//! already the site of two shipped bugs — `INSIGHTS` and `TRIPLET_COMPLETION`,
//! both names this runtime asked for and no server answered.
//!
//! [`cortex`] is the default. [`cognee`] is kept selectable, because a memory
//! engine is a claim about what a run can recall and the only way to hold one
//! to it is to be able to run the other. `MATH_AGENT_MEMORY` selects.

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

#[path = "cognee.rs"]
mod cognee;
#[path = "cortex.rs"]
mod cortex;

/// Results one recall may return.
///
/// Raised from ten, which was the ceiling for as long as recall meant one
/// search returning prose. It is now the budget for a *fused* recall whose hits
/// are split across two lookups and then deduplicated, so ten hits meant five
/// of each, and five passages is thin for a question about a library of a
/// hundred sources. The bound still exists because the reply lands in a context
/// window: each result is clipped, and the count is what stops forty clipped
/// results from adding up to the same problem.
const MAX_LIMIT: u64 = 40;

/// Results one recall returns when the caller says nothing.
const DEFAULT_LIMIT: u64 = 8;

/// The environment variable naming which memory engine a run reaches.
const ENGINE_VARIABLE: &str = "MATH_AGENT_MEMORY";

/// What a recall is asking the memory *for*, as opposed to how one engine
/// spells it.
///
/// The tools used to pass Cognee's own search-type strings straight through,
/// which is why two of them shipped naming a retriever no server answered. A
/// tool now says which of three questions it is asking and each engine decides
/// how to ask it, so a name only one engine understands cannot reach a tool
/// schema, and a question an engine cannot answer is a compile-time hole rather
/// than a `404` in a live run.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Lookup {
    /// The passages nearest the phrasing — what one source said, in the words
    /// it said it in.
    Passages,
    /// What the memory connects around the subject — the links the run made
    /// across sources and never wrote down in one place.
    Connections,
    /// The same question, walked further out. Slower, and where a connection
    /// running through an intermediate nobody asked about actually lives.
    ConnectionsExtended,
}

/// The durable brain, the sessions, the library and the scratch, over one of
/// the two engines.
///
/// Cloned into every tool that holds one, so both variants are cheap to clone
/// and share their state behind an `Arc`.
#[derive(Clone, Debug)]
pub(super) enum VectorStore {
    /// Cognee, with one shared server and one tenant per problem.
    Cognee(cognee::CogneeStore),
    /// `CortexDB`, with one shared server and one scope subtree per problem.
    Cortex(cortex::CortexStore),
}

impl VectorStore {
    /// Builds the store the container was started for.
    ///
    /// `MATH_AGENT_MEMORY` selects: `cortex` (the default) or `cognee`. It is
    /// read here rather than passed in because the choice belongs to the
    /// deployment that started the container, and a run that could change it
    /// mid-flight would be a run whose earlier writes are in a store its later
    /// recalls do not read.
    ///
    /// # Errors
    ///
    /// Returns an error when `MATH_AGENT_MEMORY` names an engine that does not
    /// exist, or when the selected engine's own configuration is missing.
    pub(super) fn from_env() -> Result<Self> {
        Self::from_env_named(&std::env::var(ENGINE_VARIABLE).unwrap_or_else(|_| "cortex".into()))
    }

    /// Builds the store for one named engine, reading the rest of that engine's
    /// configuration from the environment.
    ///
    /// Split from [`VectorStore::from_env`] so the selection can be asserted
    /// without a test mutating process-wide state — which, in a test binary
    /// that runs its cases on threads, is not a test but a race.
    ///
    /// # Errors
    ///
    /// Returns an error when the name matches no engine, or when the engine it
    /// matches is not configured.
    fn from_env_named(engine: &str) -> Result<Self> {
        match engine.trim().to_ascii_lowercase().as_str() {
            "cortex" | "cortexdb" => Ok(Self::Cortex(cortex::CortexStore::from_env()?)),
            "cognee" => Ok(Self::Cognee(cognee::CogneeStore::from_env()?)),
            other => Err(tinyagents::TinyAgentsError::Validation(format!(
                "{ENGINE_VARIABLE}=`{other}` names no memory engine; it is `cortex` or `cognee`"
            ))),
        }
    }

    /// Runs one lookup against this project's durable stores and renders the
    /// hits.
    ///
    /// Returns `Ok(None)` when the memory has nothing, so each caller can say
    /// so in its own words rather than returning an empty result the model has
    /// to interpret.
    ///
    /// # Errors
    ///
    /// Returns an error when the memory server is unreachable, refuses the
    /// request, or answers with something this runtime cannot read.
    pub(super) async fn search(
        &self,
        query: &str,
        lookup: Lookup,
        limit: u64,
    ) -> Result<Option<String>> {
        match self {
            Self::Cognee(store) => store.search(query, lookup, limit).await,
            Self::Cortex(store) => store.search(query, lookup, limit).await,
        }
    }

    /// Runs the passage and connection lookups at once and returns both
    /// answers under one heading each.
    ///
    /// The two answer different questions about the same memory and miss in
    /// opposite directions. Passages find what a source said and are blind to
    /// anything nobody wrote in one place; connections find what the run linked
    /// across sources and are blind to the wording. A run that only ever asks
    /// for passages is paying for a graph store and using it as a search box —
    /// which is what this runtime did for as long as recall meant one search.
    ///
    /// Concurrent because they are independent and the slower one is what the
    /// caller waits for either way; sequential would make the richer answer
    /// cost twice the latency, which is how a richer answer stops being asked
    /// for.
    ///
    /// One side failing is not a failed recall. A connection half that errors
    /// while the passage half answers still leaves the caller better off than
    /// the error would, so a failure becomes a line in the result saying which
    /// half is missing. Both failing propagates the passage side's error,
    /// because then there is nothing to return and silence would read as
    /// "nothing known".
    ///
    /// # Errors
    ///
    /// Returns an error when both lookups fail.
    pub(super) async fn search_fused(&self, query: &str, limit: u64) -> Result<Option<String>> {
        // Split between the two, with the passage side favoured: it is the one
        // that returns readable text, and a link is worth less per row.
        let connection_limit = (limit / 3).max(1);
        let passage_limit = limit.saturating_sub(connection_limit).max(1);
        let (passages, connections) = tokio::join!(
            self.search(query, Lookup::Passages, passage_limit),
            self.search(query, Lookup::Connections, connection_limit)
        );
        let passages = match passages {
            Ok(found) => found,
            Err(error) => {
                let Ok(connections) = connections else {
                    return Err(error);
                };
                return Ok(connections.map(|connections| {
                    format!(
                        "## What this memory connects\n\n{connections}\n\n(The passage search \
                         failed: {error}. Only the connection half of this recall answered.)"
                    )
                }));
            }
        };
        let mut sections: Vec<String> = Vec::new();
        if let Some(passages) = passages {
            sections.push(format!("## Passages\n\n{passages}"));
        }
        match connections {
            Ok(Some(connections)) => {
                sections.push(format!("## What this memory connects\n\n{connections}"));
            }
            Ok(None) => {}
            Err(error) => sections.push(format!(
                "(The connection half of this recall failed: {error}. What is above is the \
                 passage search alone.)"
            )),
        }
        Ok((!sections.is_empty()).then(|| sections.join("\n\n")))
    }

    /// Records one provisional note in this project's scratch.
    ///
    /// # Errors
    ///
    /// Returns an error when the memory server is unreachable or refuses the
    /// note.
    pub(super) async fn note_scratch(&self, text: &str, topic: &str) -> Result<u64> {
        match self {
            Self::Cognee(store) => store.note_scratch(text, topic).await,
            Self::Cortex(store) => store.note_scratch(text, topic).await,
        }
    }

    /// Returns the provisional notes nearest a phrase, and nothing durable.
    ///
    /// # Errors
    ///
    /// Returns an error when the memory server is unreachable or refuses the
    /// request.
    pub(super) async fn recall_scratch(&self, query: &str, limit: u64) -> Result<Option<String>> {
        match self {
            Self::Cognee(store) => store.recall_scratch(query, limit).await,
            Self::Cortex(store) => store.recall_scratch(query, limit).await,
        }
    }

    /// Stores one durable memory in this project's brain.
    ///
    /// # Errors
    ///
    /// Returns an error when the memory server is unreachable, refuses the
    /// document, or does not accept it in time.
    pub(super) async fn remember(&self, text: &str, source: &str) -> Result<u64> {
        match self {
            Self::Cognee(store) => store.remember(text, source).await,
            Self::Cortex(store) => store.remember(text, source).await,
        }
    }

    /// Files one downloaded source in this project's library as the bytes that
    /// arrived, not as the runtime's rendering of them.
    ///
    /// This used to send `readable::convert`'s Markdown, capped at 200,000
    /// characters. That made the library a copy of one converter's opinion: a
    /// PDF whose text layer would not extract arrived as an error rather than
    /// as a paper, a long reference page arrived with its tail missing, and
    /// every structural cue the original carried was already flattened before
    /// the memory saw it. Both engines run their own extraction, so handing
    /// over the original bytes gives each more to work with than the runtime
    /// can, and costs the runtime nothing: the bytes are already in hand from
    /// the download.
    ///
    /// # Errors
    ///
    /// Returns an error when the memory server is unreachable or refuses the
    /// upload.
    pub(super) async fn remember_source(
        &self,
        path: &str,
        url: &str,
        bytes: &[u8],
        content_type: Option<&str>,
    ) -> Result<()> {
        match self {
            Self::Cognee(store) => store.remember_source(path, url, bytes, content_type).await,
            Self::Cortex(store) => store.remember_source(path, url, bytes, content_type).await,
        }
    }

    /// Stores one completed agent session in this project's sessions.
    ///
    /// # Errors
    ///
    /// Returns an error when the memory server is unreachable or refuses the
    /// document.
    pub(super) async fn remember_session(
        &self,
        agent: &str,
        run_id: &str,
        input: &str,
        output: &str,
    ) -> Result<()> {
        match self {
            Self::Cognee(store) => store.remember_session(agent, run_id, input, output).await,
            Self::Cortex(store) => store.remember_session(agent, run_id, input, output).await,
        }
    }
}

include!("vector_tools.rs");
include!("vector_values.rs");

#[cfg(test)]
#[path = "vector_test.rs"]
mod test;
