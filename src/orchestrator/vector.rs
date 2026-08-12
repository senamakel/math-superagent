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
