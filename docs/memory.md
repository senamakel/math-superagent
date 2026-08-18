# The memory: what it holds, and the audit that found it holding nothing

The runtime's memory is one Cognee server per problem, with four stores inside
it: the shared **brain** (`remember_memory`), this project's **sessions** (one
document per finished agent run), its **library** (every downloaded source), and
its **scratch** (`note_scratch`, provisional work, unreachable from durable
recall). The graph store underneath is *not* per problem: one Neo4j Enterprise
instance holds one database per problem, and Cognee is statically pointed at
its own. That boundary is the Bolt protocol's rather than Cognee's, which
matters here because the leak recorded below was Cognee's own dataset filtering
going unenforced — see `compose.shared.yaml` for the probe. `src/orchestrator/vector.rs` and the three files it includes are the
whole of the client; [`docs/roles.md`](roles.md#recall-the-two-ways-back-into-what-is-known)
says which role holds which tool.

This file is the evidence behind the rules that guard it. It exists because an
audit on 2026-08-16 asked one question — *can a run recall what its earlier
sessions established?* — and found that on some problems the answer was no, and
that nothing in the runtime said so.

## What the audit did

Every Cognee is per problem and nothing about it is published to the host, so
each probe below was a `curl` container joined to that stack's compose network,
sending the exact request shapes `VectorStore` sends:

```sh
scripts/memory-inventory conjectures/casas-alvero   # health, then every document
scripts/memory-up conjectures/casas-alvero          # prints the network name
docker run --rm --network cognee-conjectures-casas-alvero_default \
  curlimages/curl:latest -s http://cognee:8000/health/detailed
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
does not double its request count; the probe itself is bounded at eight seconds,
and a probe that does not answer is a refusal, because the broken case *is* the
slow case — a failed model check answers in exactly 30,000 ms.

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
docker exec <stack>-cognee-1 sh -c \
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
`compose.memory.yaml` hands Cognee, falling back to `OPENROUTER_API_KEY` when
unset. Sharing one key meant the memory stopped storing at exactly the moment
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
