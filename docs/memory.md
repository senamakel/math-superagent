# The memory: what it holds, and the audit that found it holding nothing

The runtime's memory is **one Cognee server for the box, with each problem as a
tenant on it**, and four stores inside each tenant: the **brain**
(`remember_memory`), the **sessions** (one document per finished agent run), the
**library** (every downloaded source), and the **scratch** (`note_scratch`,
provisional work, unreachable from durable recall). `src/orchestrator/vector.rs`
and the three files it includes are the whole of the client;
[`docs/roles.md`](roles.md#recall-the-two-ways-back-into-what-is-known) says
which role holds which tool, and [`docs/runtime.md`](runtime.md) has the
tenancy: how a tenant is provisioned, what the key does, and what one Cognee
replaced.

Three consequences matter for reading the rest of this file, because most of it
was measured against the shape that came before.

- **A tenant is one dataset**, `math_agent__<project>`, and the four stores
  differ by `node_set` inside it. Under access control a Cognee dataset is a
  Neo4j database, so four datasets would put a source and the session that read
  it in graphs with no edge possible between them.
- **The cross-problem boundary moved into the server.** It used to be a Bolt-
  level fact about a container statically pointed at one database, with an
  allowlist in this runtime computing which datasets to name. It is now the
  server refusing: a tenant asking for another tenant's dataset gets `404
  DatasetNotFoundError`, and no key at all gets `401`. Access control is also
  what makes Cognee honour the `datasets` field, whose being silently unenforced
  is the leak recorded further down.
- **Contention is the live risk again.** One shared Cognee is what produced a
  `409 Conflict` on a `recall_memory` that had already hung the full ten-minute
  tool ceiling, under four concurrent runs. Cognee serialises per dataset rather
  than globally now, and the server is three minor versions on, and neither of
  those is a measurement. What to measure, from `config/trace.jsonl` across the
  concurrently running workspaces: the `recall_memory` and `remember_memory`
  latency distribution against the number of runs live at the time, and any
  `409` at all. A tail that grows with concurrency is this failure returning,
  and the answer is to shard tenants across a second Cognee — the compose file
  starts one per project name — rather than to raise the tool ceiling.

This file is the evidence behind the rules that guard it. It exists because an
audit on 2026-08-16 asked one question — *can a run recall what its earlier
sessions established?* — and found that on some problems the answer was no, and
that nothing in the runtime said so.

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
