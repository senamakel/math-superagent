//! The `CortexDB` engine: one server for the box, one scope subtree per problem,
//! four stores separated by where they sit in that subtree.
//!
//! # What this engine answers that the last one did not
//!
//! Two of the three failures `docs/memory.md` records are structural here
//! rather than guarded against.
//!
//! - **A write is a verdict.** `POST /v1/experience?wait=indexed` answers when
//!   the vector and lexical indexes have taken the document, and names the
//!   stages that completed. Cognee's write answered `200 {"status":"running"}`
//!   before it had read anything, and a pipeline that then failed left a stack
//!   trace in a log nobody was reading — which is how one workspace recorded
//!   193 stored findings into a server holding none. There is no equivalent of
//!   `CogneeStore::refuse_if_not_indexable` to write here because the write
//!   itself reports what that probe had to infer.
//! - **The scratch boundary is a list, not a filter.** Durable recall reads the
//!   scopes in [`DURABLE_STORES`] one at a time, and the scratch is not one of
//!   them — so it is excluded by never being asked for, which is checkable by
//!   reading four lines. It also sits at `{root}/scratch:{slug}`, a *sibling*
//!   of the durable subtree rather than a child, so a future reader who reaches
//!   for a subtree traversal does not pick it up by accident. Cognee held the
//!   same line with a `node_set` filter the server happened to honour.
//!
//!   The subtree traversal was in fact the first design here, and
//!   [`CortexStore::search`] records why it is gone: `view: "descend"` returned
//!   nothing on a live run's workspace while the brain it should have reached
//!   held nineteen events, and returned different counts for different actors
//!   on the same scope. A durable recall that can silently miss the brain is
//!   the failure this engine was chosen to end.
//!
//! # What it does not answer
//!
//! **The cross-problem boundary is this runtime's, not the server's.** Cognee
//! made each problem a tenant and answered a request for another tenant's
//! dataset `404`. The self-hosted `CortexDB` image cannot: `POST /v1/auth/tokens`
//! answers `NOT_CONFIGURED`, there is no environment variable that enables the
//! minter, and the one static `CORTEX_API_KEY` carries every capability the
//! deployment has — `scope.read.descend` and `scope.read.cross_tenant`
//! included. So what keeps one problem out of another's memory is that every
//! scope in this file is built from [`CortexStore::project`], which comes from
//! the workspace label the container was started with, and **no tool argument
//! reaches a scope**. A role cannot name another problem's memory because
//! nothing in any schema takes a scope.
//!
//! That is a weaker guarantee than the one it replaces and it is written down
//! rather than glossed: a bug in scope construction here is a cross-problem
//! leak that nothing outside this file would report. Where it actually matters
//! — a calibration run, where another problem's memory could carry the answer
//! being withheld — the deployment does not rely on this at all and gives the
//! run its own server and data directory. `compose.eval.yaml` is where that is
//! arranged and `docs/calibration.md` has the argument.

use serde_json::{Value, json};
use std::sync::Arc;
use std::time::{Duration, Instant};

use super::{Lookup, Result, point_id, slug, source_file_name, source_mime, truncate_chars};

/// The scope every store this runtime writes hangs below.
///
/// A `ws:` segment, because the whole of this deployment is one workspace in
/// `CortexDB`'s sense and the problems are what divide it. Overridable so that
/// two deployments sharing one server do not share one tree.
const DEFAULT_SCOPE_ROOT: &str = "ws:math-agent";

/// The scope segment holding the three durable stores for one problem.
const PROJECT_SEGMENT: &str = "project";

/// The scope segment holding one problem's provisional notes.
///
/// A sibling of [`PROJECT_SEGMENT`] rather than a child of it, and that is the
/// whole of the scratch boundary. See this module's header.
const SCRATCH_SEGMENT: &str = "scratch";

/// The store holding what survived checking.
const BRAIN_STORE: &str = "store:brain";

/// The store holding this project's completed agent runs.
const SESSION_STORE: &str = "store:session";

/// The store holding every source this project downloaded.
const LIBRARY_STORE: &str = "store:library";

/// The stores durable recall reads, most authoritative first.
///
/// A literal rather than a traversal, and `CortexStore::search` records the
/// live failure that made it one. The scratch is absent, which is what keeps
/// provisional arithmetic out of durable recall — being absent from this list
/// is the control, and the scratch's sibling scope placement is the second
/// line rather than the only one.
pub(super) const DURABLE_STORES: [&str; 3] = [BRAIN_STORE, LIBRARY_STORE, SESSION_STORE];

/// The barrier a durable write waits for.
///
/// `indexed` means the lexical and vector indexes have taken the document, so
/// the write's own response is the answer to "will this be recallable" — the
/// question Cognee could only be asked separately, and lied about.
///
/// Measured against a local server whose extraction model is the ladder's
/// `flash`, and the distribution matters more than any single number:
///
/// - **1.0–1.9s** for a one-sentence note, steady state. This is the cost a
///   run actually pays, and it is almost entirely the extraction model call —
///   what a knowledge graph costs at write time.
/// - **~5s** for the *first* write to a scope the server has not seen, which
///   is once per problem per store rather than once per write.
/// - A tail set by the router rather than by the memory: three consecutive
///   bare `flash` completions through the same ladder measured 960ms, 6,661ms
///   and 810ms. A write that takes ten seconds is that spike landing on a
///   first write, not the memory degrading.
///
/// The first measurement taken here was 4.95s and it was a first write read as
/// though it were the steady state. It is recorded because the mistake is the
/// reusable part: one sample of a bimodal latency is a number that will be
/// wrong in whichever direction it is later quoted.
///
/// It is not `consolidated`. That barrier waits for the belief and concept
/// layers, which the manifest says blocks on an out-of-process model call with
/// no bound worth putting a timeout on — and those layers are rebuilt on their
/// own schedule anyway, so waiting for them would buy a run nothing it does not
/// get a minute later for free.
const DURABLE_BARRIER: &str = "indexed";

/// The barrier a scratch note waits for.
///
/// `captured` is durable at WAL append and answered in **7–8ms** measured,
/// against 1.0–1.9s for the same note at [`DURABLE_BARRIER`]. A scratch note is
/// written mid-derivation, and waiting on an index would put the memory on the
/// critical path of the arithmetic it is describing — which is exactly what the
/// file it replaced did not do.
///
/// The cost is real and bounded: a `recall_scratch` issued immediately after a
/// `note_scratch` may legitimately miss it. That is a race rather than a
/// retrieval failure, and it is the correct trade for a store whose whole
/// contract is that nothing in it has been checked.
const SCRATCH_BARRIER: &str = "captured";

/// How long a durable write may block before the caller is told it failed.
///
/// The steady-state write is under two seconds and the ceiling is ninety, which
/// is wide on purpose: the gap is the ladder under load — a bare completion
/// through it was measured at 6.7s while its neighbours took under a second —
/// and a write refused because
/// the router was busy would lose a finding the run has already done the work
/// to establish. What it must not become is the ten-minute tool ceiling that
/// killed a live `remember_memory` mid-write and took a falsified conjecture
/// with it — a bound the *tool* enforces is a bound nobody chose.
const WRITE_TIMEOUT: Duration = Duration::from_secs(90);

/// How long a recall may block before the caller is told it failed.
const RECALL_TIMEOUT: Duration = Duration::from_secs(120);

/// How long the server's readiness report may take before a write treats the
/// silence as the answer.
const READY_TIMEOUT: Duration = Duration::from_secs(20);

/// How long one readiness verdict stands before a write asks again.
///
/// A write path that probed the server every time would double the request
/// count of the busiest tool in the run; one probe a minute bounds the cost and
/// still catches an outage inside the window a single agent turn occupies.
const READY_TTL: Duration = Duration::from_mins(1);

/// How much of one recalled passage reaches the prompt.
const PASSAGE_CLIP: usize = 4_000;

#[derive(Clone, Debug)]
pub(in crate::orchestrator) struct CortexStore {
    client: reqwest::Client,
    base_url: String,
    /// The workspace label, slugged. Every scope is built from this and from
    /// nothing a tool can supply; see this module's header.
    project: String,
    session: String,
    root: String,
    /// The last readiness verdict and when it was taken, shared by every clone.
    ///
    /// Shared deliberately: the store is cloned into each tool, and a per-tool
    /// cache would probe once per tool per minute rather than once per minute.
    readiness: Arc<tokio::sync::Mutex<Option<(Instant, Readiness)>>>,
}

/// What the server says about its ability to store something worth recalling.
///
/// Not the same question as whether it is up. A `CortexDB` with no reachable
/// embedding provider does not refuse writes — it pins the data directory to a
/// **mock** embedding provider, stores the documents, and reports
/// `degraded: true`. Recall then returns vectors that mean nothing, and the
/// pinning survives a restart, so every document written during the outage is
/// permanently unrecallable while `/v1/admin/health` says `healthy` throughout.
///
/// That is Cognee's Finding 1 in a different coat — a write accepted and made
/// worthless — and it is why this refuses on `degraded` rather than on `ready`
/// alone. `/v1/admin/health` is not read at all: the manifest says outright
/// that it returns 200 with unreadable storage or mock providers and must never
/// gate traffic.
#[derive(Clone, Debug, PartialEq, Eq)]
enum Readiness {
    /// The server reports it can store and index for real.
    Ready,
    /// The server cannot, in its own words.
    Refusing(String),
}

/// Which memory layers answer one of the three questions a [`Lookup`] asks.
///
/// The mapping is the substance of this engine's answer to `relate_memory`.
/// Passages are the events themselves and the episodes grouping them: what was
/// written, in the words it was written in. Connections are the *derived*
/// layers — facts and beliefs the server extracted across documents — which is
/// the question a passage search cannot answer. The extended reach adds
/// `understanding`, the synthesised concepts, each carrying the events that
/// support it and a stance and confidence; that is the layer that says what the
/// memory has concluded rather than what it holds.
pub(super) const fn layers(lookup: Lookup) -> &'static [&'static str] {
    match lookup {
        Lookup::Passages => &["events", "episodes"],
        Lookup::Connections => &["facts", "beliefs"],
        Lookup::ConnectionsExtended => &["facts", "beliefs", "understanding"],
    }
}

include!("cortex_store.rs");
include!("cortex_values.rs");
