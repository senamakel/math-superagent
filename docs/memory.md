# The memory: two engines, the four stores, and the audit that found one holding nothing

The runtime's memory is **one server for the box, with four stores inside it per
problem**: the **brain** (`remember_memory`), the **sessions** (one document per
finished agent run), the **library** (every downloaded source), and the
**scratch** (`note_scratch`, provisional work, unreachable from durable recall).

Which server is `MATH_AGENT_MEMORY`, and there are two:

| | `cortex` (default) | `cognee` |
|---|---|---|
| Server | `cortexdb/cortexdb:v0.9.8` | `cognee/cognee:1.4.2` + Neo4j 5.26 Enterprise |
| Graph | its own | Neo4j, one database per dataset |
| Vectors | its own (HNSW over `RocksDB`) | LanceDB, one table per dataset |
| Embeddings | the ladder's `vectors` rung, 3072-dim | `fastembed`, on the server's CPU |
| The four stores are | four scopes | four `node_set`s in one dataset |
| Cross-problem boundary | this runtime's scope construction | the server's, one tenant per problem |
| A write returns when | the index has taken it | the upload has been queued |

`src/orchestrator/vector.rs` is the façade both sit behind — it keeps the type
name every other module already threads through, and turns the *question* a
tool is asking into whichever retriever the selected engine spells it with.
`cortex.rs` and `cognee.rs` are the two clients.
[`docs/roles.md`](roles.md#recall-the-two-ways-back-into-what-is-known) says
which role holds which tool, and [`docs/runtime.md`](runtime.md) has the
deployment.

## Why the engine moved, and what it fixed

Two of the three failures audited below are **structural** under CortexDB
rather than guarded against, which is the whole argument for the change.

- **A write is a verdict.** `POST /v1/experience?wait=indexed` answers when the
  lexical and vector indexes have taken the document, and names the stages that
  completed: `["captured","extracted","indexed","consolidated","compressed"]`.
  Finding 1 below — a `200` for a document that was then silently dropped — has
  no shape here, because the response *is* the answer to "will this be
  recallable". `CogneeStore::refuse_if_not_indexable` had to reconstruct that
  from a separate health probe; `reached_barrier` just reads it.
- **The scratch boundary is a list rather than a filter.** Durable recall reads
  the scopes in `DURABLE_STORES` one at a time and the scratch is not one of
  them, so it is excluded by never being asked for — checkable by reading four
  lines. It also sits at `{root}/scratch:{slug}`, a *sibling* of the durable
  subtree, so a future reader reaching for a traversal does not pick it up.
- **Finding 2 has no counterpart at all.** The graph half of a fused recall
  failed on 122 of 136 calls under Cognee because nothing here ran the pipeline
  its retriever needed. CortexDB's derived layers are the ordinary read path,
  and `relate_memory` reads `facts`/`beliefs` and, on `reach: extended`,
  `understanding` — synthesised concepts each carrying the events that support
  them, a stance and a confidence.

### Measured on 2026-08-29, against the local image and this deployment's ladder

Every number below is from probing `cortexdb/cortexdb:v0.9.8` on this box, with
`CORTEX_LLM_URL` and `CORTEX_EMBEDDING_URL` pointed at the ladder.

- **Readiness is honest and health is not.** With no provider key the server
  starts, reports `/v1/admin/health` `{"status":"healthy"}`, and pins the data
  directory to `mock::3072` embeddings — storing documents whose vectors mean
  nothing, permanently, because the pinning outlives the outage. `ready`
  reported `degraded: true` throughout. That is Finding 1 wearing a different
  coat, so `refuse_if_degraded` refuses a write on `degraded` and the compose
  healthcheck reads `/v1/admin/ready`. **Never gate on `/v1/admin/health`** —
  the vendor's own manifest says so.
- **The gate is on `OPENAI_API_KEY`, not the per-lane key.** With only
  `CORTEX_EMBEDDING_API_KEY` set the server still fell back to mock embeddings.
  `compose.shared.yaml` therefore hands the ladder's key under the name the gate
  reads. This is the same class of failure as Finding 4 below and was found the
  same way — by reading the startup log rather than the health endpoint.
- **A durable write costs one to two seconds, not five.** The distribution is
  bimodal and the first measurement taken here read the wrong mode: 4,951 ms was
  a *first* write to a scope the server had not seen. Steady state is
  **1.0–1.9 s** to `indexed`, **~5 s** for the first write to each new scope,
  and **7–8 ms** to `captured`. The tail belongs to the router rather than the
  memory — three consecutive bare `flash` completions through the same ladder
  measured 960 ms, 6,661 ms and 810 ms, so a ten-second write is that spike
  landing on a first write. Confirmed through the runtime: the first two live
  `remember_memory` calls took 895 ms and 765 ms.

  So the brain, the sessions and the library wait for `indexed` and the scratch
  waits for `captured`. Against Cognee's measured 66, 114 and 177 seconds — and
  one call killed at the ten-minute tool ceiling — a second and a half for a
  *confirmed* write is the better half of both trades. The mistake is worth
  keeping: one sample of a bimodal latency is a number that will be wrong in
  whichever direction it is later quoted.
- **A repeated write is free, and looks alarming in a log.** Live runs show
  `remember_memory ... in 0ms`, which is the idempotency key doing its job:
  several roles storing the *same* sentence produce the same key, and the server
  replays rather than writing again. Checked against the server rather than
  assumed — the brain held two events for many such calls, both distinct and
  both real.
- **`view: "descend"` is not usable and durable recall no longer uses it.**
  This is the one finding that changed the design after it was written. Reading
  the three durable stores as one traversal of their parent worked on the scope
  it was developed against, and then on a live run's workspace returned **zero
  events** while a `granular` recall addressed straight at the brain returned
  **nineteen** — with the brain listed in `/v1/scopes/list` as a registered
  scope the whole time. The same `descend` also returned three events for a
  stranger's actor and zero for the scope's own owner, so it was incoherent and
  not merely incomplete.

  `CortexStore::search` therefore issues three concurrent `granular` recalls
  against `DURABLE_STORES`, a literal list in the source. That costs two extra
  requests, and buys a set of stores that can be read and tested rather than
  inferred, a scratch excluded by never being named, and no dependency on the
  `scope.read.descend` capability. Measured through the runtime afterwards:
  `recall_memory` in **1,069 ms** returning 15 KB.

  The general lesson is the one this file keeps recording. A boundary that
  depends on a server behaviour this runtime cannot predict is not a boundary,
  and the failure mode here was the exact one the engine was chosen to end — a
  recall that silently misses the brain and reports nothing wrong.
- **The scratch boundary holds.** It is now held by the store list above rather
  than by a traversal: the scratch is not in `DURABLE_STORES`, so durable recall
  never asks for it. Its sibling scope placement remains as the second line.
  Live, a run wrote five scratch notes and durable recall returned none of them,
  while a recall addressed at the scratch scope returned them.
- **A source keeps its bytes.** `POST /v1/blobs` takes the file raw, with
  `Content-Type` declaring what it is, and returns a `blob_id` an envelope
  references as `{"kind":"blob_ref"}` — which routes it through the server's own
  content processors. Multipart is refused `415`, which is worth knowing because
  multipart is exactly what the Cognee path sends.
- **The `understanding` layer earns its cost.** One sentence about
  Casas-Alvero produced two concepts with `supported_by` event ids, `stance:
  "supported"`, `confidence: 0.7` and a `coverage_score` — and one of them said
  what the memory did *not* hold. That is the answer `relate_memory` was always
  supposed to give and never once did.

### What it does not fix, stated plainly

**The cross-problem boundary is no longer the server's.** Cognee made each
problem a tenant and answered a request for another tenant's dataset `404`. The
self-hosted CortexDB image cannot: `POST /v1/auth/tokens` answers
`{"error_code":"NOT_CONFIGURED"}`, no environment variable enables the minter,
and the one static `CORTEX_API_KEY` carries every capability the deployment has
— `scope.read.descend` and `scope.read.cross_tenant` included.

What holds the line instead is that every scope is built inside `cortex.rs` from
the workspace label, and **no tool argument reaches a scope**: a role cannot name
another problem's memory because nothing in any schema takes one. That is
weaker, and a bug in scope construction there is a leak nothing outside that file
would report.

Where it actually matters it is not relied on. A calibration run gets its **own
CortexDB and its own data directory** (`compose.eval.yaml`), because the thing
such a run must not reach is another problem's memory — a sibling working on the
same literature is exactly where a withheld answer would be written down — and a
separate process is not a better filter but the absence of a store to filter.
[`docs/calibration.md`](calibration.md) has the rest of that argument.

The vendor also marks its own `self_hosted` and `local_docker_profile` as
**blocked**, meaning untested by them ("no isolated Docker execution environment
restored since Phase 0"). Everything above is this deployment's own measurement
rather than a supported claim, which is a reason to keep `cognee` selectable and
a reason to re-probe on every image bump.

## The Cognee engine, and the audit behind its controls

Everything from here down is about `MATH_AGENT_MEMORY=cognee`. It is kept
because the controls it describes are still live code, and because a memory
engine is a claim about what a run can recall — the only way to hold one to that
claim is to be able to run the other.

Three consequences matter for reading the rest of this file.

- **A tenant is one dataset**, `math_agent__<project>`, and the four stores
  differ by `node_set` inside it. Under access control a Cognee dataset is a
  Neo4j database, so four datasets would put a source and the session that read
  it in graphs with no edge possible between them.
- **The cross-problem boundary is in the server.** A tenant asking for another
  tenant's dataset gets `404 DatasetNotFoundError`, and no key at all gets
  `401`. Access control is also what makes Cognee honour the `datasets` field,
  whose being silently unenforced is the leak recorded further down.
- **Contention is the live risk.** One shared Cognee is what produced a `409
  Conflict` on a `recall_memory` that had already hung the full ten-minute tool
  ceiling, under four concurrent runs. Cognee serialises per dataset rather than
  globally now, and neither that nor a version bump is a measurement. What to
  measure, from `config/trace.jsonl` across concurrently running workspaces: the
  `recall_memory` and `remember_memory` latency distribution against the number
  of runs live at the time, and any `409` at all.

The rest of this file is the evidence behind the rules that guard it. It exists
because an audit on 2026-08-16 asked one question — *can a run recall what its
earlier sessions established?* — and found that on some problems the answer was
no, and that nothing in the runtime said so.

## What the audit did

Nothing about Cognee is published to the host, so each probe below was a `curl`
container joined to the memory network, sending the exact request shapes
`VectorStore` sends. The audit ran against the per-problem servers this
deployment used at the time; the equivalent commands today name the one shared
network and carry the problem's tenant key:

```sh
scripts/memory-inventory conjectures/casas-alvero   # health, then every document
scripts/memory-up conjectures/casas-alvero          # prints the network name
scripts/memory-up --key conjectures/casas-alvero    # prints the tenant's key
docker run --rm --network math-agent-shared_memory \
  -H "X-Api-Key: $key" curlimages/curl:latest -s http://cognee:8000/health/detailed
```

`scripts/memory-inventory` came out of the audit and is the first thing to run
when a run's recall looks thin: it prints the server's own ingest health and
then every dataset with the documents in it, so "the memory is empty" is a
reading rather than a suspicion.

The tool-level record is in each workspace's `config/trace.jsonl`: every
`tool_completed` event carries the tool name, its input and its output, so the
health of the memory over a whole run is a count rather than an impression.

## Finding 1 — a write is accepted, dropped, and reported as stored

`POST /api/v1/remember` with `run_in_background=true` answers
`200 {"status":"running"}` before it has read anything. Cognee's pipeline then
runs a connection test against its model endpoint *before* it persists the
upload (`setup_and_check_environment.py`), and when that test fails the pipeline
raises, the document is never written, and the only trace is a stack trace in
the server's log. The runtime discarded the response body, treated 2xx as
success, and told the model `stored research note <id>`.

Measured three ways on the same afternoon:

- A sentinel document posted to a live `conjectures/casas-alvero` brain returned
  `200`. The dataset held 35 documents before the write and 35 after, and
  nothing appeared in the server's file storage.
- `conjectures/conway-99-graph`: **193** successful `remember_memory` calls in
  its run; its memory server's four datasets hold **zero** documents between
  them, 4 KiB of file storage, and every `recall_memory` — 110 of 112 — came
  back `404 {"detail":"No data found in the system…"}`.
- `conjectures/casas-alvero`: nothing has persisted since 09:17 that day
  (sessions stop at 09:12, the brain at 09:04, the library at 08:18), while the
  run that continued until 23:00 recorded **170** further writes as successful.

The control is `VectorStore::refuse_if_not_indexable`, on the one path every
store's write passes through. It reads `/health/detailed`, which names each
component and its status, and refuses the write in the server's own words when
one is unhealthy. A verdict stands for a minute so the busiest tool in the run
does not double its request count; the probe itself is bounded at twenty
seconds, and a probe that does not answer is a refusal, because the broken case
*is* the slow case — a failed model check answers in exactly 30,000 ms.

That bound was eight seconds until 2026-08-18, and what moved it is worth
recording, because the control did not fail — its evidence changed underneath
it. Eight seconds was chosen when a healthy answer took tens of milliseconds:
one Cognee per problem, on a Docker network, on the same box. Against one shared
server on another machine, with eight runs live and Cognee pinned at its
four-core cap, `/health` answered `200` in **13.7s and 14.0s** — healthy, and
merely saturated. The probe read that as broken and refused two `note_scratch`
writes in a live `conjectures/hilbert-16` run.

So the healthy case is no longer a constant, and the number that anchors the
bound is the broken one: 30,000 ms, exactly. Twenty seconds is past the
loaded-healthy case measured and ten short of the failure. A healthy server that
takes longer than that is a finding about the deployment's headroom — the first
thing to read is `docker stats` on the memory host, where the same incident
showed 393% of a four-core cap — and not a reason to move the bound closer to
thirty, which is where it stops being a probe at all.

What it deliberately does not do is fail a write because the *probe* could not
be sent. An unreachable server is reported by the write that follows it.

## Finding 2 — the graph half of every fused recall had never answered

`recall_memory` is fused: passages nearest the phrasing, plus what the memory
connects around it. The second half asked for `TRIPLET_COMPLETION`, and this
server answers that
`404 {"detail":"In order to use TRIPLET_COMPLETION first use the create_triplet_embeddings memify pipeline. [NoDataError]"}`.
Nothing in this runtime calls `/api/v1/memify`, so it could never have worked:
**122 of 136** fused recalls in one live run, and **54 of 54** in
`conjectures/erdos-ternary-2n`, returned passages and a parenthesis saying the
other half had failed.

This is the second time this shape of bug has shipped — `INSIGHTS` was the
first, a name the server's enum does not carry — so `UNSUPPORTED_TRIPLET_SEARCH`
stays in the source, is kept out of `SCOPE_SAFE_SEARCH_TYPES`, is asserted
absent by a test, and `search_in` refuses it by name with the reason. The fused
half is `GRAPH_COMPLETION` now, which a live probe answered with nodes and
edges — and answered while the model endpoint was down, because `only_context`
returns the retrieved context rather than prose about it.

`GRAPH_COMPLETION_CONTEXT_EXTENSION`, the `reach: extended` option on
`relate_memory`, does need the model endpoint and fails with it: 10 of 20 calls
in one run, 75 of 96 in another, all `409 {"error":"An error occurred during
recall."}`. It now falls back to the immediate neighbourhood and says it did,
rather than returning nothing about a subject the graph knows.

## Finding 3 — a recall result was mostly scaffolding

With `include_references` set, a hit is an object carrying the passage twice —
`text` and `raw.value` — beside `score: null`, `metadata: {}`, `structured:
null` and a dataset UUID. `render_result` pretty-printed the object, so a live
recall reached the prompt as `{ "dataset_id": null, "kind": "chunk", … }` with
the passage escaped inside it, at over twice the tokens of the passage, and the
4,000-character clip then fell inside the scaffolding rather than at the end of
the text. It renders the passage now, naming the dataset it came from, and falls
back to the whole object for a shape it does not recognise.

## Finding 4 — the key the memory server runs on is not the key in `.env`

Docker Compose resolves `${OPENROUTER_API_KEY}` from the **shell environment
first** and the checkout's `.env` only after. On the box this audit ran on, an
interactive shell exported an older key whose daily limit was exhausted, so
every stack started from that shell — memory servers and agent runs alike — ran
on a key returning `403 Key limit exceeded`, while `.env` held a working one.
That is the whole of the cascade above: the ingest pipeline's connection test
fails, every document is dropped, and recall answers `404 No data found`.

It is checkable in one line, and worth checking before reading anything else
into an empty memory:

```sh
printf 'shell %s\n' "$(printf %s "$OPENROUTER_API_KEY" | sha256sum | cut -c1-12)"
docker exec math-agent-shared-cognee-1 sh -c \
  'printf "server %s\n" "$(printf %s "$LLM_API_KEY" | sha256sum | cut -c1-12)"'
docker run --rm --network <network> curlimages/curl:latest -s \
  http://cognee:8000/health/detailed
```

A stack brought up with the checkout's own key reported every component healthy
on the same image and the same compose file, which is the control that makes the
key the cause rather than a coincidence.

Two things changed because of it.

**The launchers now export `.env` over the shell.** `scripts/dotenv` is sourced
by `scripts/memory-up`, `scripts/run-agent` and `scripts/solve-euler`, exports
every name the file defines, and prints — by name, never by value — any variable
whose inherited value it had to override. An override is still one edit to
`.env` away, which is the one place this repository keeps credentials.

**The memory indexes on its own key.** `OPENROUTER_MEMORY_API_KEY` is what
`compose.shared.yaml` hands the *ladder*, through its `env_file`. Cognee itself
is given the ladder's own `MATH_AGENT_API_KEY`, because its `LLM_ENDPOINT` is
the router rather than a provider: handing it an OpenRouter key reaches the
ladder as a bearer token it does not recognise, and every ingest fails `409
AuthenticationError` while `/health/detailed` still reports the model endpoint
healthy. Sharing one key meant the memory stopped storing at exactly the moment
the run had been working hardest: the limit is spent by the run's own model
calls, and the ingest that carries what the run just learned is the write that
gets dropped. A separate key also makes the memory's spend readable on its own,
which is worth having when deciding whether entity extraction is worth what it
costs.

Verified on the arrangement above: a stack brought up through the new path runs
on the memory key — the container's `LLM_API_KEY` hashes to the same twelve
characters as `.env`'s — reports every component healthy, and returned an
ingested document to a question 100 seconds later.

## What is recallable, and what is not

With a healthy stack the loop closes, and this is the measurement rather than
the design: a session document posted at T was returned, whole, in answer to a
question phrased in none of its words, **60 seconds** later — input and final
output, scoped to its own `project:` node set.

What that document holds is one agent run's *input and final output*. It is not
the turns: no tool calls, no intermediate reasoning, no console. A question
about how a result was reached is answered from `trace.jsonl` and the workspace,
not from the memory.

Two gaps in coverage are worth naming because they are silent:

- **The orchestrator's own work is barely in the memory.** `record_session` is
  called once per solve, with `solution-loop` as the agent, *after* the loop
  returns — so a run that is still going, or that was killed, has recorded
  nothing of its own reasoning. A live `conjectures/casas-alvero` server holds
  36 session documents and not one of them is the orchestrator's.
- **The library holds what was downloaded while the server was indexing.** The
  same server holds 18 sources against 53 on disk under `research/sources/`.
  Nothing reconciles the two, and `recall_memory`'s description promises "this
  project's downloaded library" without qualification.

Both are coverage, not correctness: the fix for either is a decision about what
a session document should be, and belongs with
[`docs/solution-loop.md`](solution-loop.md) rather than in the client.
