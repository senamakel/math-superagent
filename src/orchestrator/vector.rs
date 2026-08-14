//! Cognee-backed durable brain, project-scoped session memory, and the run's
//! provisional scratch.
//!
//! Three stores, and the separation between them is the point. The brain holds
//! what survived checking and every project reads it. The session dataset holds
//! this project's completed agent runs. The *scratch* holds the half-finished
//! arithmetic a run produces on the way to a result — what `SCRATCHPAD.md` used
//! to be — and it is deliberately not reachable from `recall_memory` or
//! `relate_memory`: provisional work is not durable knowledge, and a
//! half-finished calculation surfacing as one is how a run comes to believe
//! something nobody verified. It is also not the knowledge graph. The graph
//! answers what the run's entities are connected to; the scratch answers what
//! this run was in the middle of, which no amount of graph traversal recovers.

use async_trait::async_trait;
use serde_json::{Value, json};
use std::time::Duration;

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

const BRAIN_DATASET: &str = "math_agent_brain";
const SESSION_DATASET_PREFIX: &str = "math_agent_sessions__";

/// The prefix of the per-project dataset holding provisional work.
///
/// Scoped to the *project* rather than the run, for the reason recorded on
/// [`VectorStore::from_env`]: `./euler 763` continues from what is on disk, and
/// a scratch that vanished on restart would be worse than the file it replaces.
const SCRATCH_DATASET_PREFIX: &str = "math_agent_scratch__";

/// The prefix of the per-project dataset holding the downloaded library.
///
/// Scoped to the project because a source is fetched to answer *this* problem:
/// another run's library is a different subject, and reading it is how a run
/// meets a paper nobody here asked for. The brain stays shared; the sources do
/// not.
const LIBRARY_DATASET_PREFIX: &str = "math_agent_library__";

/// The node set every durable brain document is ingested under.
const BRAIN_NODE_SET: &str = "math_agent_brain";

/// The prefix of the node set this project's completed sessions carry.
const SESSION_NODE_SET_PREFIX: &str = "project:";

/// The prefix of the node set this project's provisional notes carry.
const SCRATCH_NODE_SET_PREFIX: &str = "scratch:";

/// The prefix of the node set this project's downloaded sources carry.
const LIBRARY_NODE_SET_PREFIX: &str = "library:";

/// Cognee's search type for the passages nearest a phrase.
const CHUNK_SEARCH: &str = "CHUNKS";

/// Cognee's search type for the subject–predicate–object triples themselves.
///
/// The graph's own contents rather than a model's prose about them. It sits
/// beside [`CHUNK_SEARCH`] in [`VectorStore::search_fused`] because the two
/// fail in opposite directions: a passage says what one source stated in one
/// place, and a triple says what the run connected across sources and never
/// wrote down anywhere. Asking only for passages is what makes a graph store
/// behave like a search box.
const TRIPLET_SEARCH: &str = "TRIPLET_COMPLETION";

/// Cognee's search type for the graph around a subject, walked further out.
///
/// [`GRAPH_SEARCH`] retrieves the immediate neighbourhood; this one extends the
/// context before answering, which is what "what is this connected to, two
/// steps away" needs. Two steps is where a run finds the link nobody stated —
/// the whole reason the graph is worth its cost.
const EXTENDED_GRAPH_SEARCH: &str = "GRAPH_COMPLETION_CONTEXT_EXTENSION";

/// Cognee's search type for the edges the graph holds around a subject.
///
/// It was `INSIGHTS`, which this server rejects outright — the enum it accepts
/// has no such member, so every `relate_memory` call ever made returned a 422
/// naming the eighteen types it does accept, and the graph half of the memory
/// has never answered anything. `GRAPH_COMPLETION` is the surviving name for
/// the same question: it retrieves the nodes and edges around the query and
/// renders them, and with `only_context` set it returns that context rather
/// than a model's prose about it.
const GRAPH_SEARCH: &str = "GRAPH_COMPLETION";

/// Every search type this runtime is allowed to ask for.
///
/// Not a style rule. `node_name` is the *only* scoping this server actually
/// applies — [`VectorStore::search_in`] records the probe, and the server's own
/// code says why: dataset filtering is documented as available only under
/// `ENABLE_BACKEND_ACCESS_CONTROL`, which `compose.memory.yaml` sets to
/// `false`. So a search type is safe here exactly when its retriever accepts
/// `node_name`, and reading the server's retriever registry shows that several
/// do not:
///
/// - `SUMMARIES` takes `top_k` and a session id and no node filter at all.
/// - `CHUNKS_LEXICAL` (BM25) takes `top_k` alone.
/// - `CYPHER` and `NATURAL_LANGUAGE` run a query against the whole graph.
/// - `CODE` and `CODING_RULES` are scoped by something else entirely.
///
/// Asking for any of those would return every other problem's memory, which is
/// the leak [`visible_datasets`] was written to close, reopened through a
/// different field. The loss is real and worth naming: `CHUNKS_LEXICAL` is the
/// one retriever that would match an exact identifier — a theorem's name, an
/// OEIS A-number — that a dense vector rounds off. That gap is covered on disk
/// instead, by `search_documents`, which is a literal-term index over this
/// workspace's own files and cannot see another project's by construction.
const SCOPE_SAFE_SEARCH_TYPES: [&str; 4] = [
    CHUNK_SEARCH,
    TRIPLET_SEARCH,
    GRAPH_SEARCH,
    EXTENDED_GRAPH_SEARCH,
];

/// Results one recall may return.
///
/// Raised from ten, which was the ceiling for as long as recall meant one
/// search returning prose. It is now the budget for a *fused* recall whose hits
/// are split across two retrievers and then deduplicated, so ten hits meant
/// five of each, and five passages is thin for a question about a library of a
/// hundred sources. The bound still exists because the reply lands in a context
/// window: each result is clipped, and the count is what stops forty clipped
/// results from adding up to the same problem.
const MAX_LIMIT: u64 = 40;

/// Results one recall returns when the caller says nothing.
const DEFAULT_LIMIT: u64 = 8;

// A source is uploaded whole rather than capped. The old 200,000-character
// bound existed because the runtime sent its own conversion, which it could
// truncate freely — the full text was on disk beside the digest either way.
// Raw bytes have no such spare copy in Cognee, and truncating them would hand
// the extractor half a PDF. The size is already bounded where it arrives:
// `documents::MAX_DOCUMENT_BYTES` refuses anything over 5 MiB mid-stream, so
// nothing larger than that can reach this path.

/// How long a write may spend enqueueing before the caller is told it failed.
///
/// Every ingest here is backgrounded, so this bounds the *enqueue* and not the
/// indexing. It exists because a hung Cognee must not become a hung agent: a
/// live `remember_memory` ran into the ten-minute tool ceiling and the finding
/// it carried — a falsified conjecture — was lost with it.
const ENQUEUE_TIMEOUT: Duration = Duration::from_secs(30);

#[derive(Clone, Debug)]
pub(super) struct VectorStore {
    client: reqwest::Client,
    base_url: String,
    project: String,
    session: String,
    session_dataset: String,
    scratch_dataset: String,
    library_dataset: String,
}

include!("vector_store.rs");
include!("vector_tools.rs");
include!("vector_values.rs");

#[cfg(test)]
#[path = "vector_test.rs"]
mod test;
