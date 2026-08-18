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
use std::sync::Arc;
use std::time::{Duration, Instant};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// The prefix of the one dataset this project owns on the memory server.
///
/// One, not four. The four stores below are separated by `node_set` inside it,
/// and the reason is the server's storage model rather than a simplification:
/// under access control a Cognee dataset *is* a graph database, so filing the
/// library and the sessions as separate datasets would put a source and the
/// session that read it in different graphs, with no edge possible between
/// them. The entity linking across the two is the whole reason a graph store
/// is worth its cost, so the stores share a dataset and differ by node set —
/// which is also the only scoping this deployment has measured as enforced.
///
/// Scoped to the *project* rather than the run: `./euler 763` continues from
/// what is on disk, and a memory that vanished on restart would be worse than
/// the files it sits beside.
///
/// Another project's dataset is not merely filtered out, it is unreachable:
/// this runtime authenticates as one tenant per project, and the server
/// answers a request for another tenant's dataset `404 DatasetNotFoundError`.
const PROJECT_DATASET_PREFIX: &str = "math_agent__";

/// The node set every durable brain document is ingested under.
///
/// Unprefixed, where the other three carry the project: it is the store whose
/// contents are *about* method rather than about this problem. It is still one
/// per tenant — this runtime has never had a brain that spanned problems, the
/// per-problem server made sure of that — and making one would now be a
/// deliberate act of sharing a dataset between tenants rather than a
/// consequence of a name.
const BRAIN_NODE_SET: &str = "math_agent_brain";

/// The prefix of the node set this project's completed sessions carry.
const SESSION_NODE_SET_PREFIX: &str = "project:";

/// The prefix of the node set this project's provisional notes carry.
const SCRATCH_NODE_SET_PREFIX: &str = "scratch:";

/// The prefix of the node set this project's downloaded sources carry.
const LIBRARY_NODE_SET_PREFIX: &str = "library:";

/// Cognee's search type for the passages nearest a phrase.
const CHUNK_SEARCH: &str = "CHUNKS";

/// Cognee's search type for the subject–predicate–object triples themselves,
/// which this deployment cannot answer and which must therefore not be asked
/// for.
///
/// It was the graph half of every fused recall, on the argument that a passage
/// says what one source stated in one place and a triple says what the run
/// connected across sources. The argument holds; the retriever does not. This
/// server answers it `404 {"detail": "In order to use TRIPLET_COMPLETION first
/// use the create_triplet_embeddings memify pipeline. [NoDataError]"}`, and
/// nothing in this runtime runs that pipeline — `/api/v1/memify` is never
/// called. So the graph half of a fused recall failed on **122 of 136** calls
/// in one live `conjectures/casas-alvero` run, and on every one of the 54 in
/// `conjectures/erdos-ternary-2n`: the recall came back passages-only with a
/// parenthesis nobody acted on.
///
/// This is the second time the same shape of bug has shipped — `INSIGHTS` was
/// the first, a name the server's enum does not carry — so the constant stays
/// here rather than being deleted, kept out of [`SCOPE_SAFE_SEARCH_TYPES`] and
/// asserted absent, and [`GRAPH_SEARCH`] answers the same question live.
const UNSUPPORTED_TRIPLET_SEARCH: &str = "TRIPLET_COMPLETION";

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
/// Not a style rule. `node_name` is the scoping that separates this project's
/// four stores from each other — [`VectorStore::search_in`] records the probe
/// — and a retriever that ignores it reads the whole tenant, scratch included.
/// The cross-*project* boundary is the server's now (`compose.shared.yaml`:
/// one tenant per problem, and a request for another tenant's dataset is a
/// `404`), so what is at stake here is narrower than it was and still real:
/// provisional arithmetic returned as durable recall is how a run comes to
/// believe something nobody checked. Reading the server's retriever registry
/// shows several that take no node filter at all:
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
///
/// Scopable is necessary and not sufficient: a retriever this server cannot run
/// at all is off the list too, which is why [`UNSUPPORTED_TRIPLET_SEARCH`] is
/// not on it.
const SCOPE_SAFE_SEARCH_TYPES: [&str; 3] =
    [CHUNK_SEARCH, GRAPH_SEARCH, EXTENDED_GRAPH_SEARCH];

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

/// How long the server's own health report may take before a write gives up on
/// it and treats the silence as the answer.
///
/// A healthy server answers `/health/detailed` in tens of milliseconds for its
/// stores and a second or two for the model check behind them. A broken one
/// answers in **thirty seconds** — the report's `llm_provider.response_time_ms`
/// was exactly `30000`, the timeout of the connection test Cognee runs before
/// every ingest pipeline — so waiting for the answer is waiting for the failure.
/// Eight seconds is past the healthy case and well short of the broken one.
const HEALTH_TIMEOUT: Duration = Duration::from_secs(8);

/// How long one health verdict stands before a write asks again.
///
/// A write path that probed the server every time would double the request
/// count of the busiest tool in the run; one probe a minute bounds the cost and
/// still catches an outage inside the window a single agent turn occupies.
const HEALTH_TTL: Duration = Duration::from_mins(1);

#[derive(Clone, Debug)]
pub(super) struct VectorStore {
    client: reqwest::Client,
    base_url: String,
    project: String,
    session: String,
    /// The one dataset this project owns; see [`PROJECT_DATASET_PREFIX`].
    dataset: String,
    /// The last health verdict and when it was taken, shared by every clone.
    ///
    /// Shared deliberately: the store is cloned into each tool, and a per-tool
    /// cache would probe once per tool per minute rather than once per minute.
    indexing: Arc<tokio::sync::Mutex<Option<(Instant, IngestHealth)>>>,
}

/// What the memory server says about its ability to *index* a document, as
/// opposed to accept one.
///
/// The distinction is the whole of this type. `POST /api/v1/remember` with
/// `run_in_background=true` answers `200 {"status":"running"}` before anything
/// has been read, and Cognee's pipeline then runs a connection test against its
/// model endpoint *before* it persists the upload. When that test fails the
/// pipeline raises in `setup_and_check_environment`, the document is never
/// written, and the only trace is a stack trace in the server's log.
///
/// Measured, not inferred: with the model endpoint returning `403 Key limit
/// exceeded`, a sentinel document posted to `math_agent_brain` came back `200`
/// and never appeared — the dataset held 35 rows before the write and 35 after,
/// and nothing landed in the server's own file storage. The same failure at
/// scale is on disk in two workspaces: `conjectures/conway-99-graph` reported
/// **193** successful `remember_memory` calls into a memory server whose four
/// datasets hold **zero** documents between them, and `conjectures/casas-alvero`
/// reported another **170** writes after the last one that actually persisted.
#[derive(Clone, Debug, PartialEq, Eq)]
enum IngestHealth {
    /// The server reports every component it needs to index working.
    Ready,
    /// The server cannot index right now, in its own words.
    Refusing(String),
}

include!("vector_store.rs");
include!("vector_tools.rs");
include!("vector_values.rs");

#[cfg(test)]
#[path = "vector_test.rs"]
mod test;
