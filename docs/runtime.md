# Runtime architecture, budget, and observability

What the crate is made of, what one run may spend, and how to see what a run actually did. Every number here is a ceiling that a live run has met at least once. The working agreement is [`AGENTS.md`](../AGENTS.md); this file is the part of it that goes deeper than a rule.

## Runtime architecture

The Rust crate vendors TinyAgents and keeps the integration deliberately small.

```text
src/
├── lib.rs              # public exports
├── prompts/            # built-in role prompts, included at compile time
├── agent/              # TinyAgents facade, OpenRouter, Langfuse
│   ├── budget.rs       # per-run call, wall-clock, and capture policy
│   ├── reflection.rs   # in-run middleware that reflects on failing tools
│   ├── resilient.rs    # tool-error and request-timeout wrappers
│   └── trace.rs        # live console and trace.jsonl event listener
├── orchestrator/       # registry, specialists, compression, workspace tools
│   ├── approaches.rs   # candidate lines of attack and why the closed ones closed
│   ├── async_subagents.rs # graph-backed asynchronous child-run controls
│   ├── claims.rs       # claim blocks, the derived ledger, and search_claims
│   ├── code_layout.rs  # measures duplication and grouping in code/
│   ├── digest.rs       # structural digest of a downloaded source
│   ├── documents.rs    # bounded workspace documents and local search index
│   ├── dossier.rs      # the inventor's workspace record, built per delegation
│   ├── frontier.rs     # citation graph of the library, ranked and deduped
│   ├── oeis.rs         # sequence lookup adapter, filed and cross-referenced
│   ├── patterns.rs     # exact sequence analysis and recurrence search
│   ├── requests.rs     # stated gaps, deduped against the ledger and closed
│   ├── threads.rs      # the library's topic axis beside its arrival axis
│   ├── solutions.rs    # graph-backed attempt/reflect/diversify loop
│   └── vector.rs       # Qdrant tools and deterministic local feature vectors
├── hello_agent/        # minimal single-agent example
├── error/              # crate-wide Error and Result<T>
└── greeting/           # legacy template example
examples/
├── orchestrator.rs     # Docker runtime entry point
└── hello_agent.rs      # direct provider example
vendor/tinyagents/      # pinned upstream TinyAgents checkout (one agent turn)
vendor/tinyflows/       # pinned upstream TinyFlows checkout (the state graph)
agent                   # user-facing helper
euler                   # Project Euler problem-number wrapper
compose.yaml            # agent and Qdrant services
scripts/run-agent       # Docker Compose implementation
scripts/solve-euler     # official statement fetch and solve workflow
workspace/              # selectable writable agent workspaces
└── template/           # seed instructions, prompts, config, and memory
```

The executable registry contains `goals`, `research`, `tool_builder`, `coder`,
`sat_solver`, `smt_solver`, `theorem_prover`, `symbolic_math`, `lean_prover`,
`reflection`, `judge`, `pattern_finder`, `inventor`, `librarian`, `scholar`,
and `context_curator`. The `organizer` was removed: its filing job is covered by
the index tools travelling with the document tools, so every role that creates a
file can describe it, rather than by a role whose every cycle competed with the
mathematics and won.

Seven of those — `tool_builder`, `coder`, `sat_solver`, `smt_solver`,
`theorem_prover`, `symbolic_math`, `lean_prover` — carry exactly the same
authority: shell, file write, `apply_patch`, and the document tools. They are
separate roles because they differ in *mandate*, and because their failure
modes have nothing in common: a program that ran but computes the wrong thing,
an `UNKNOWN` reported as solved, an `unsat` from hypotheses that were already
contradictory, a `Theorem` proved from axioms nobody checked, an identity
confirmed by sampling, a `sorry` left undeclared. One prompt hedging between
seven of those is strict about none of them. They are built from one list in
`register_code_writing_agents`, so the shared authority boundary is visible
rather than buried in four near-identical blocks — a tool granted there
reaches all four. Agents are exposed to the orchestrator as TinyAgents
`SubAgentTool` instances. The goals agent also receives the research and
tool-builder delegation tools, so it can pursue a goal through nested, focused
work. All model-visible delegation uses the graph-backed asynchronous
controls: `spawn_agent`, `peek_agent`, `steer_agent`, and `await_agent`. A
spawn returns a run ID immediately. Callers may launch independent work in
parallel, inspect or redirect live runs, and must await every result needed
for their final answer. Do not reintroduce blocking `SubAgentTool` calls.

Fifty runs may execute at once (`MATH_AGENT_MAX_CONCURRENT_AGENTS`); the rest
queue for a slot, and spawning stays non-blocking either way, so a caller gets
its run ID immediately whether or not a slot was free. The cap bounds provider
concurrency rather than rationing work: unbounded fan-out becomes upstream rate
limiting, which the retry ladder then absorbs as simultaneous backoff across
every run. Keep it far above the fan-out the registry can produce. A run holds
its slot while it waits in `await_agent` for children it spawned itself, so a
pool that could fill entirely with parents waiting on queued children would
deadlock; the headroom is what makes that unreachable.
The session dataset is named for the *project*, not the run:
`math_agent_sessions__project_euler_185`. It briefly carried the run id too —
`…__s18cb030630d9e2be-1`, nanoseconds and a pid — which made the name unique per
process, so every restart opened a fresh dataset, and because a run is shown
only its own session dataset, every restart silently *discarded* the session
memory of every earlier run on that problem. One problem restarted eight times
in a day left eight datasets, seven of them unreachable. The run id belongs
inside the document, where `remember_session` already writes it as a `Session:`
line; the dataset is the scope, and the scope is the problem. `visible_datasets`
also accepts `<project>__<anything>`, so the per-run datasets the old naming
stranded are readable again — with the `__` separator required, because without
it project `euler_18` would read `euler_185`'s memory.

`visible_datasets` is an **allowlist**: the shared brain, this project's session
datasets, and this project's library, and nothing else. It was a denylist —
everything except another project's sessions and any scratch — which passes
whatever a name fails to classify, and a live server proved what that costs. A
`project_euler_903_L0` dataset holding thirty-six downloaded sources sat there
from an earlier build, and every run on the box searched it: for a Project Euler
problem that is another problem's literature arriving unasked, and at worst its
answer. A dataset this runtime does not name belongs to another project or an
older build, and neither of those is this run's.

That allowlist was scoping a field the server does not apply, which is why the
isolation now rests on `node_name` instead. A live probe settled it: asking
`/api/v1/recall` for one project's session dataset, then another's, then a
third's by UUID, returned the *same* chunk from a fourth project every time —
the only request that changed the answer was a name matching no dataset at all,
which came back `No datasets found`. So the dataset list is validated and then
ignored, and every run on the box was reading every other project's sessions.
`node_name` filters on the `node_set` each document was ingested under, and the
same probe showed it applied exactly: `project:<a>` returned only `<a>`'s
documents, `project:<b>` only `<b>`'s. Every store already wrote a node set —
`math_agent_brain`, `project:<p>`, `library:<p>`, `scratch:<p>` — so the scopes
existed and nothing read them. `durable_node_sets` names the first three and
never the fourth, which is where the scratch separation now lives; the dataset
list is still sent, because it costs nothing and a server that honours it would
be narrowing the same way. Writers and readers build every node set through one
set of helpers, since a writer and a reader spelling a scope apart is the one
leak nothing would report — the documents would be filed where recall never
looks and the store would simply read as empty.

`relate_memory` was dead for the same reason nothing caught the leak: the
runtime asked for `INSIGHTS`, and this Cognee build's search-type enum has no
such member, so every call ever made returned a 422 listing the eighteen types
it does accept. The graph half of the memory — the half that justifies a graph
store rather than a search box — had never answered anything. `GRAPH_COMPLETION`
is the surviving name for that question, and with `only_context` set it returns
the nodes and edges around the query rather than a model's prose about them.
Both lessons are the same one: a store this runtime cannot see itself failing to
read is indistinguishable from a store with nothing in it, and neither the tests
nor the console said which it was.

The library is the third per-project dataset, `math_agent_library__<project>`,
and it closes the gap between what a run gathered and what it could recall.
`download_document` wrote `research/…` and `index_document` wrote a local
literal-term index; nothing reached Cognee, while every prompt told the roles
that Cognee was the durable catalogue. Filing happens in the download path,
where the bytes are already in hand and free to file. It is best effort and
*reported*: a memory that refused the document must not fail a download that
succeeded, but a library the run believes is searchable and is not is worse
than one it knows is not.

What is filed is the **original bytes**, not the runtime's conversion of them.
Sending `readable::convert`'s Markdown — capped at 200,000 characters — made
the library a copy of one converter's opinion: a PDF whose text layer would not
extract reached Cognee as an error rather than as a paper, a long reference page
arrived with its tail missing, and every structural cue the original carried was
flattened before the graph ever saw it. Cognee runs its own extraction, and it
is better than the runtime's at the one job the runtime does worst — a probe
uploading a PDF got back `Page 1: Theorem 1. …`, with page structure
`pdf-extract` does not produce. The declared content type is passed through, but
magic bytes beat it, on the same evidence the download path records: a PDF
served as `text/html` is still a PDF, and uploading it as text spends the
extraction on the wrong parser.

Two files go up in one request, because `data` is a list on Cognee's side: the
source itself, and a card carrying the project, the workspace path, and the URL.
The card is what keeps a recalled chunk traceable to a file on disk — without
it a passage surfaces naming no source, and a claim nobody can trace is worth
less than no claim. One request rather than two, so a card can never describe a
document whose upload failed.

No character cap applies to the upload, and it does not need one: the size is
bounded where the bytes arrive, by `documents::MAX_DOCUMENT_BYTES`, which
abandons a transfer over 5 MiB mid-stream. Truncating raw bytes would be worse
than truncating text — half a PDF is not a shorter PDF, it is a file the
extractor cannot open.

`ALLOW_HTTP_REQUESTS` is enabled on the memory server, so `/add` and `/remember`
also accept a URL in place of an uploaded file. The download path does not use
it: the runtime has the bytes already, and handing over a URL would mean a
second fetch that skips the 5 MiB bound, the frontier's fetch ledger, and the
`raw/` archive. Note what the flag grants — the *server* performs the fetch,
from inside the Docker network, where the runtime container's egress rules do
not apply. The API stays bound to `127.0.0.1` for that reason.

Every write to Cognee is queued rather than awaited, and one number —
`ENQUEUE_TIMEOUT` — bounds the enqueue for all of them. `remember` used to wait
for indexing to finish, which means waiting on entity extraction: four live
`remember_memory` calls took 66, 114 and 177 seconds, and the fourth met the
ten-minute tool ceiling and was killed, losing the falsified conjecture it
carried. A store a run is charged minutes to write is a store the run stops
writing to.

A failed session write is traced rather than discarded. The four `remember_session`
call sites dropped their results, so a run that never recorded itself and one
that recorded fine read identically on the console and in `trace.jsonl`. The
write stays best effort — the answer is already returned to the caller — but its
silence was the fault, not its optimism.

Every role with memory gets three tools, not two: `remember_memory` writes,
`recall_memory` returns the passages nearest a phrase, and `relate_memory`
returns the *edges* the graph holds around a subject. The third is the one that
justifies a graph store at all — chunk search is what the vector store already
did, so a runtime that only ever recalls chunks is paying for a knowledge graph
and using it as a search box. The distinction is worth stating in each prompt
that needs it: the inventor asks what the memory relates the obstruction to
before proposing a new line, the scholar asks what is already connected to a new
source's central object so its digest can say where the source agrees or
conflicts, and the pattern agent asks before calling a regularity new. Both
searches share one request path on `VectorStore::search`, differing only in
Cognee's `search_type`, so a correction to one cannot drift from the other.

The research agent has Exa plus `recall_research` and `remember_research` tools.
Cognee persists the notes, and the server is **one process for the whole box,
with each problem as a tenant on it**. `compose.yaml` joins its network —
external, named by `MEMORY_NETWORK` — and reaches the server as `cognee:8000`,
with no `depends_on`: the memory server outlives any one run, and a run must
never be able to take it down.

`docker compose -f compose.yaml config --services` yields `agent` alone. What it
talks to is somebody else's stack: `compose.shared.yaml` (`scripts/shared-up`),
holding one Neo4j Enterprise instance, one Cognee and one ladder. `./agent`
starts it first; it is not in the agent's own project, which is what stops a run
being able to take it down.

## The stack is reached by address, and need not be on this box

The shared stack is every problem's memory and none of its compute, so it is the
half worth moving off a machine that is doing the runs. Set
`MATH_AGENT_SHARED_HOST` to an ssh host and `scripts/shared-up` drives Compose
there; the runs reach it over the network instead of by joining its Docker
networks:

| variable | what it names |
| --- | --- |
| `MATH_AGENT_SHARED_HOST` | ssh host running the stack; empty means this box |
| `MATH_AGENT_SHARED_PATH` | the stack's directory on that host |
| `MATH_AGENT_MEMORY_URL` | where Cognee answers |
| `MATH_AGENT_API_BASE_URL` | where the ladder answers |

Compose is run **over ssh** rather than through `DOCKER_HOST=ssh://…`, and the
difference is not stylistic: with a remote `DOCKER_HOST`, Compose resolves the
file's bind mounts against the *client's* filesystem and sends paths that mean
nothing on the daemon's. The stack's files therefore live beside it, in
`MATH_AGENT_SHARED_PATH`.

A run used to reach `cognee:8000` and `ladder:6969` by name over two gatewayless
Docker networks. That is gone, and with it the property that a run container had
no route out at all. What replaces it:

- **`host.docker.internal`** is the default for both addresses, so a single-box
  deployment still works with no configuration: the stack publishes its ports to
  the host it runs on and the run reaches them through the host gateway.
- **The API is authenticated.** Each problem is a tenant with its own key; an
  unkeyed request is `401` and another tenant's dataset is `404`. The boundary
  travels with the request rather than with the network, which is what makes
  publishing acceptable at all. Bind to a tailnet address, not `0.0.0.0`.
- **A calibration run keeps its isolation, differently.** `compose.eval.yaml`
  still leaves the container without a default route, and the memory server and
  the ladder are now two entries in the screen proxy's allowlist rather than two
  networks it is joined to. `scripts/calibrate-run` derives those entries from
  the addresses above rather than taking them separately, because a second place
  to write them down is a second place for them to disagree — and disagreeing
  produces a run with no memory and no model that reads as a broken harness.

The images are not all multi-arch: the ladder is published for amd64 only, so on
an Apple Silicon host it runs emulated. That is acceptable for a proxy, which is
I/O bound rather than compute bound, and `platform: linux/amd64` says so in the
file rather than leaving it to be discovered.

## One memory server, one tenant per problem

Two things separate one problem's memory from another's, and neither is a filter
in this runtime.

The **key** is the first. `ENABLE_BACKEND_ACCESS_CONTROL=true` makes each
problem a Cognee user; `scripts/memory-up <label>` registers it and mints an API
key, `scripts/memory-up --key <label>` prints it, `scripts/run-agent` passes it
in as `COGNEE_API_KEY`, and `VectorStore::from_env` puts it on the HTTP client as
a default `X-Api-Key` header so no call site can forget it. Probed live: a
tenant asking for another tenant's dataset by name gets `404
DatasetNotFoundError`, and a request with no key at all gets `401`. This is also
what makes Cognee honour the `datasets` field, which in single-user mode it
documents as unenforced and which this repository measured leaking
(`docs/memory.md`).

The **graph database** is the second, and it is unchanged in effect from the
per-problem shape it replaced: under access control a Cognee dataset *is* a
Neo4j database, named `cognee<dataset-uuid-hex>`, created by Cognee itself on
first ingest rather than by `scripts/memory-up`. A driver session is bound to one
named database at the Bolt protocol level — a container pointed at one got `[]`
back from `SHOW DATABASES` run inside its own session, and a literal Cypher
`MATCH` for another problem's data came back empty. Multiple databases need
Neo4j **Enterprise**; Community cannot create one at all.

Because a dataset is a graph database, the runtime writes **one dataset per
problem** rather than one per store: the brain, the sessions, the library and
the scratch share `math_agent__<project>` and differ by `node_set`. Four
datasets would put a source and the session that read it in graphs with no edge
possible between them, and the entity linking across the two is the reason a
graph store is worth its cost.

What this bought is the box. One Cognee per problem meant one Python server and
one resident embedding model per problem — measured between 0.6g and a problem
pinned at 3.96g of its 4g cap during cognify — so a dozen problems reserved 24g
of ceiling for their memory alone. One server, capped at `COGNEE_MEM_LIMIT`
(8g), replaces that.

What it costs is contention, which is the failure that split the memory server
per problem in the first place: four concurrent runs against one shared Cognee
produced a `409 Conflict` on a `recall_memory` that had already hung the full
ten-minute tool ceiling, and a run cannot retry ten minutes it has already
spent. Cognee serialises per *dataset* now rather than globally, which is the
reason to try again and not a proof; `docs/memory.md` says what to measure.

The parent and both children use context-compression middleware with an
estimated 300,000-token trigger. The summary should retain mathematical
assumptions, intermediate results, source URLs, tool output, and unfinished
work.

The authenticated OpenAI-compatible router on port 6969 owns model selection,
pricing, caching, and fallback. The runtime sends only two stable model ids:
`flash` for the default tier and `reasoning` for reasoning roles. Both publish
a one-million-token context window to the harness, so compression is based on
the router's real capacity rather than an unrecognized alias.

`compose.shared.yaml` runs the ladder from `ghcr.io/senamakel/llm-ladder-router:latest`
with `pull_policy: always`, mounts the sibling router checkout's `config.toml`, and every stack reaches it as
`http://ladder:6969/v1` on a stable internal network. The one-off agent
container joins that network and its per-problem Cognee network; each problem's
Cognee joins it too, for the entity extraction and summarisation its own
ingestion performs. The ladder also joins a provider-egress network nothing
else sees. One ladder for the box, rather than one per checkout: the ladder used
to live in `compose.yaml`, whose project name is the checkout directory's, so a
second checkout brought up a second ladder and the two fought over port 6969.

The tag is `latest` rather than a sha, and `pull_policy: always` is what makes
that mean anything — Compose otherwise keeps serving whatever `latest` meant
when it first pulled. The router's CI republishes the tag on every push to its
main, so a fix there reaches every problem here through `scripts/shared-up`
rather than an edit to this repository. What that buys was measured on
2026-08-18: a fifteen-minute Surplus edge outage answered `403 Forbidden` to
every ladder, the router classed it as a caller error and handed it back
unreplayed, and five live runs died inside the same minute with a working
second provider one rung below. The fix — 401/403/407 advance the ladder and
park the rung — is a router change, and pinning a sha is what would have kept
it out of this stack. The ladder lives in the shared project rather than in any
run's, so bringing a run up does not recreate the ladder or
interrupt another run, and the internal router network does not give a
calibration container a route around its proxy. The calibration overlay puts
`ladder` in `NO_PROXY` so model traffic stays on that internal link. Host access
is published on `127.0.0.1:6969`. `LADDER_CONFIG_PATH`, `LADDER_ENV_FILE`, and
`LADDER_PORT` override the host-side deployment inputs;
`MATH_AGENT_API_BASE_URL` still replaces the endpoint entirely.

The run's `.env` supplies the memory OpenRouter key and the router checkout's
`.env` supplies its code OpenRouter and Surplus keys. The latter is applied
second when Compose builds the ladder environment. Do not replace that with a
raw `docker run --env-file`: Docker preserves surrounding dotenv quotes in the
credential value, which was measured reaching OpenRouter as a missing
authorization header. `MATH_AGENT_API_KEY` is the caller bearer credential.

Three roles run on the reasoning tier: `judge`, `director`, and `reducer`,
listed in `REASONING_ROLES` and resolved in one place by
`ModelTiers::tier_for`. Membership is two questions and a role has to pass
both. Is its output a judgement nothing mechanical can check — as against a
report of what a program did, which the method policy already routes through
something that checks it? And is it cheap: short output, few calls, not on a
schedule?

`context_curator` is excluded although it judges, because it fails the second
question outright — a run's measured top consumer at 28 model calls, on a
schedule. `scholar` and `research` read whole documents; the pattern agent and
the code writers execute rather than judge; `goals` drives every turn of an
attempt. Tests assert the split in both directions, because the mistake is
silent: adding a role costs money on every run and nothing fails to say so.

### The deepest tier

Three roles sit one tier further up, in `MAX_REASONING_ROLES`: `inventor`,
`reflection`, and `weakener`. They answer a second question on
top of the reasoning tier's — *does the answer keep improving while the model
thinks longer* — and they run on the router's `max-reasoning` ladder, which
carries higher price ceilings and asks each rung for the deepest setting its
model family accepts. The depth is the router's to apply: it injects
`reasoning_effort` per rung, because the accepted values belong to the model
that ends up serving and a rejected one is a 400 the failover loop hands back
rather than stepping past.

Reflection is the clearest case: one of its three fields decides whether a run
reporting progress every attempt is diverted anyway, and telling a new bound
from a new fact is exactly the call a fast model gets wrong. `inventor` is the
run's one generative role, and `weakener` decides whether what is left after a
difficulty is switched off is still worth solving.

What the three have in common besides depth is that they are *rare*: the
inventor runs at a diversify, the weakener beside it, and reflection once per
attempt. That is the other half of what keeps the tier affordable, and it is
why `orchestrator` was moved back down to `reasoning` after a spell up here.
The argument for promoting it was real — every other role's work is downstream
of what the driver commissions — but it is on every turn, and its judgement is
*which bench to commission next*: a choice between a bounded set of named roles
rather than an open question whose answer improves while a model thinks longer.
`goals` never came up, being the higher-volume of the two planners. The two
lists are asserted disjoint, the driver is asserted on the cheaper one from
both sides, and the deepest list is asserted small.

`MATH_AGENT_MODEL`, `MATH_AGENT_REASONING_MODEL` and
`MATH_AGENT_MAX_REASONING_MODEL` can replace the three ids for development —
pointing the last at `reasoning` is how a run opts the deepest tier out without
a rebuild — but provider ladders do not belong here: changing the providers,
their price ceilings, or a ladder's reasoning depth is a router operation. Exa handles search. Langfuse ingestion
is best effort and must not turn a successful answer into a failed run.

Langfuse is also available for querying and reviewing recorded turns. Use
`./langfuse-turns --hours 24 --limit 50` for normalized observations or
`./langfuse-turns --trace <trace-id>` for one trace. Use
`./langfuse-review --hours 24 --limit 100` to retain those turns while flagging
errors, status messages, and missing outputs as improvement candidates. The
helpers load the ignored local `.env`, query Observations API v2, and pass Basic
Auth through curl configuration on standard input so credentials never appear
in process arguments or output. Treat returned inputs and outputs as sensitive.

Every role's workspace context is assembled once, by `RolePrompts::load`, when
the container starts, and for most roles that is right: their job is stated up
front and does not depend on what the run later discovers. The inventor is the
exception, and `dossier.rs` is it. A conjecture launcher defaults to twelve
hours and the inventor is first delegated to hours in, so the `GOAL.md`,
`THREADS.md` and `CLAIMS.md` in its system prompt were the versions that existed
before any of the work it is asked to invent past — the role that most needs to
know what has already been tried was the one least equipped to know it. The
dossier is therefore read from disk at the moment the inventor is spawned, and
delivered in the spawn message rather than the system prompt: the shared method
policy has to lead every prompt so the provider can cache the common prefix, and
a harness's prompt is fixed when it is registered, so a per-invocation system
prompt would mean re-registering the harness on every call. It is packed in
priority order — the goal, then what has been closed, then what is established —
against a token budget (`MATH_AGENT_DOSSIER_TOKENS`, default 16,000), and every
cut is announced, because an inventor silently handed half a ledger re-proposes
what was in the other half.

Do not add memory domains, channels, Web3, SQLite persistence, REPL, or RLM
features unless the user explicitly expands the product scope.

## Run budget

`RunBudget` in `src/agent/budget.rs` is the single source of truth for what one
agent run may spend, and it applies to the orchestrator and every specialist
alike. The defaults are 250 model calls, 4000 tool calls, a one-hour run
ceiling, and a thirty-minute ceiling per tool call. The tool ceiling stays the
inner one — `budget_test.rs` asserts `run_timeout > tool_timeout`, because the
run clock does not honour `StopWithPartial` and an expired tool call does.
Each is overridable through
`MATH_AGENT_MAX_MODEL_CALLS`, `MATH_AGENT_MAX_TOOL_CALLS`,
`MATH_AGENT_RUN_MINUTES`, and `MATH_AGENT_TOOL_MINUTES`; an unset, empty,
unparsable, or zero value keeps the default.

These are far above the `TinyAgents` defaults of 25 model calls and 50 tool
calls, which fit a short question-answering turn rather than an investigation.
A run that reaches the model-call cap stops with partial results instead of
failing, so the work already done survives. Keep it that way: discarding a
completed derivation because a counter tripped is the worst outcome available.

The tool-call cap is the exception, and the reason it is set so far above the
model-call cap. `LimitBehavior::StopWithPartial` is honoured on the model-call
path in the vendored agent loop but not on the tool-call path, which still
fails the run outright. Until that is fixed upstream, the tool cap must stay out
of reach so the graceful cap is always the one that trips. Do not narrow it to
just above the model cap: one model turn can request several tool calls.

The wall clock is a third path with the same defect, and unlike the tool cap it
is *not* out of reach. `run_loop.rs` checks the deadline before each model call
and returns `TinyAgentsError::Timeout` — `StopWithPartial` is not consulted, so
a run that reaches its ceiling fails outright and its accumulated answer is
lost, exactly as a provider error would lose it. Only the long-lived agents can
reach this: a child spawned late inherits a fresh ceiling, but the `goals` run
driving an attempt starts with the run and ages with it. Two live runs spent
their first ninety minutes inside attempt 1 and were on course to meet it. When
that happens the loop itself survives — `delegate` turns the failure into a
report reflection can read — but the attempt's work product does not. Treat a
run ceiling reached mid-attempt as data loss, not as a clean stop.

The run ceiling and the tool ceiling are separate limits and must stay
separate. Collapsing them means a specialist that runs one long computation
dies with it. Whatever the run ceiling is, `await_agent` must be able to wait it
out, or the orchestrator is structurally unable to collect the result of the
deepest work it delegated.

Saying so in the schema was not enough. `wait_seconds` has always accepted up
to the run ceiling, but the harness applied the ten-minute *tool* ceiling on
top, so any wait longer than that died with a timeout error instead of the
child's result — a live `pattern_finder` asked for 600 seconds, was killed at
exactly 600,000 ms, and lost the run it had commissioned. `await_agent` and
`await_agents` therefore override `timeout_policy` with the requested wait plus
a minute of grace. The grace matters: the wait must be the thing that ends, as
it ends by *returning* the child's state, where a deadline replaces that with an
error.

Each model turn is capped at 48000 output tokens (`MATH_AGENT_TURN_OUTPUT_TOKENS`). Generation
is linear in output length, so this is also the wall clock for one turn. It was 12000, and that
number measured the wrong thing: the cap bounds *generated* tokens, and on a reasoning model most
are never visible. Across 4,180 accounted calls on a live Erdős–Gyárfás run, 77.8% of output
tokens went to the hidden reasoning channel, and every turn that hit the ceiling read `out=24000`
with `reasoning_tokens=23999` — one visible token. A 12000 cap was budgeting about 2,600 tokens of
answer and cutting the model off mid-thought.

Raising it costs nothing on the common path, because a cap is not an allowance: over 152 measured
turns the median was 461 tokens and the 90th percentile 5,352, with 3 turns in 152 reaching the
cap. Read the share with `reasoning_tokens` in `trace.jsonl`; the console `out=` figure is the
total and does not separate them.

The inventor keeps a 32000 floor (`RunBudget::for_invention`) even though the default now exceeds
it, so an operator who narrows the cap for a cheap run does not silently reintroduce the
truncation it was written for. `for_invention` is the one budget method that widens; the rest
bound authority, which only narrows.

`ReroutingModel` is outermost, so every provider failure passes it once, and it now notes the cause
and agent on the way past: `AgentEvent::RetryScheduled` carries a call id and an attempt but no
error, so a live `pattern_finder` retried six times over three minutes with the reason recorded
nowhere.

`UntruncatedModel` covers the shape upstream excludes — a turn with text but no tool call. It
re-issues once at the *same* cap, carrying a system message saying the last turn produced nothing
and to call a tool. It used to double the cap instead; the reasoning-channel measurement removed
that, since a turn spending 23,999 of 24,000 tokens thinking is not short of room, and PE236's
`tool_builder` truncated at 12,000, was re-issued at 24,000, and wrote nothing for five minutes.

A timeout is a safety ceiling, not permission to run an intractable approach. Before
substantial execution the tool-builder must state both time and space complexity;
exponential time or space is prohibited, so choose a polynomial or better formulation.

`validate_complexity` enforces that, and the field it reads has been evaded
three times in three different ways. First by notation: a factorial search
wrote `polynomial (O((n!)²))` and the forbidden list looked for `o(n!` , which
the parenthesis defeated. Then by honesty running the wrong way: a truthful
`exponential` on the naive oracle rule 8 *requires* was refused outright, so
the gate punished accuracy and blocked the method policy's own first step —
which is why `exponential` and `factorial` are declarable with a concrete
`oracle_bound`. And then by saying nothing at all: a live run on Project Euler
185 declared `complexity: "backtracking with pruning"` against
`complexity_class: "polynomial"` and was allowed through, because that string
names a method and states no quantity, so neither the class check nor the
notation check had anything to match. Sixteen digits is ten quadrillion
candidates, and the run held a `sat_solver` it never spawned.

So a declaration naming a search strategy over candidate solutions —
`backtrack`, `brute force`, `exhaustive`, `branch and bound` — with no
`oracle_bound` is refused, and the refusal names `sat_solver`, because a gate
that blocks the wrong method without pointing at the right one costs the run a
turn to rediscover it. `enumerate` is deliberately not on that list:
"enumerate the divisors of n" is an honest description of an `O(√n)` method,
and refusing it would repeat the second evasion above. A bounded oracle
declares its bound and never reaches the check, so rule 8 is untouched.

The wider lesson is the one this document keeps recording. Five solver and
prover roles were registered, tool-equipped, prompt-written, and provisioned in
the image, and naming them in the planners' prompts did not get a single one
spawned; the run reached for `tool_builder` and commissioned the prohibited
method instead. A prompt instruction is not a control, and the control belongs
where the action happens.

A command that hits the ceiling is killed, but what it printed is kept and
returned with the timeout reported as its exit status. `Command::output()`
inside a `timeout` discards all of it — the read is dropped mid-flight — so a
program that printed for nine minutes taught the agent nothing, and it could
not tell a computation that was nearly done from one that never got past its
first loop. Two such commands cost one live run twenty of its first
forty-four minutes. The pipes are therefore drained by their own tasks, and
killing the child is what closes them. A timeout is evidence about the method,
and evidence belongs in the result rather than in an error string.

## One start command

`./euler-tui` cannot start, stop, or restart anything, and that is a design
decision with a date on it.

When starting was part of the same command as watching, opening a second view
started a second run on the same workspace. Both wrote the same files and both
made checkpoint commits over each other. That happened three times in one
evening, twice unnoticed for minutes, and the damage is not visible while it is
happening — it shows up later as a checkpoint history that interleaves two
investigations, which is very hard to unpick and impossible to score.

A viewer that cannot launch cannot do it. One start command also means the
question *"is something already running for this problem"* has a single answer
rather than one per terminal.

The narrow exception is direction. `./steer` reaches a run that already exists,
which does not touch what the rule prevents: a directive appends a line to a
file and creates no container.

A run's container is **named for its workspace** — `math-agent-<workspace
subdir>`, e.g. `math-agent-conjectures-hilbert-16` — which is what makes the
collision loud rather than silent: Docker refuses a duplicate name, so a second
`./conjecture hilbert-16` fails at once and says which container already holds
the workspace. `docker ps` also reads as a list of problems being worked on
rather than of random ids.

Checking by **mount** is still the reliable check and is what
`scripts/calibrate-run` does, because the name only covers runs this launcher
started: a container started by hand, or by an older checkout, carries
Compose's generated `<project>-agent-run-<id>` instead — and the project name
is derived from the checkout directory, so a run started from a worktree is
`<worktree>-agent-run-<id>` and a `grep riemann-agent-run` sees nothing at all
while it is live. A shell (`./agent shell`) keeps the generated name on
purpose, so that it can be opened alongside a live run on the same workspace.

## Watching a run

`AGENTS.md` states the rules; these are the commands and the runs behind them.

Start detached so the run outlives the terminal:

```sh
nohup ./euler 763 > workspace/project-euler/763/config/start.log 2>&1 &
```

`start.log` holds the image build and the statement fetch, which happen *before*
any container exists and are therefore the only place a failed start says why.
Everything after that belongs to the container.

Before starting, check nothing is already running on that workspace:

```sh
docker ps --format '{{.Names}}' | grep riemann-agent-run
docker inspect <name> --format '{{range .Mounts}}{{.Source}}{{"\n"}}{{end}}' | grep project-euler
```

Two containers on one workspace is the failure to look for, and it is silent:
both runs work, both write, and the damage shows up later as a checkpoint
history that interleaves two investigations. Stop one with `docker rm -f
<name>`; the workspace survives and the next `./euler` on it continues from what
is on disk.

Match by **mount, not by name**. The Compose project name comes from the
checkout directory, so a worktree's container is not called `riemann-agent-run`
at all and a name filter silently finds nothing.

The runtime's console arrives on the container's **stderr**, not its stdout — a
live container had 643 lines there and none on stdout — so `docker logs` needs
`2>&1`, and any follower must read both streams.

## The memory cap

A run's container is capped at 4 GiB with `memswap_limit` at 8 GiB and 250 MiB
reserved; the shared Neo4j and Cognee are capped at 16 GiB each with 1 GiB
reserved each. Every number is a judgement rather than a requirement — what the
rule in `AGENTS.md` demands is that *some* limit stay. 2 GiB was the wrong
judgement for a run, and a live run said so; so were 4 and 8, under the
arrangement described below.

An Erdős–Gyárfás container was OOM-killed mid-attempt: `oom` and then
`die exit=137` in `docker events`. An OOM kill is the worst failure shape
available here. The kernel stops the process, so nothing reaches the console,
the run simply ceases to appear, and everything in flight is lost — which is why
`docker events --filter event=oom` is the first thing to read when a container
vanishes without an error.

The cap has to cover the Rust runtime, every concurrent child run, and every
Python subprocess they spawn between them, against work that is graph
enumeration and BFS over millions of states. Problem 763 had already recorded
the old cap in its own `MEMORY.md` as a mathematical ceiling — *"exact BFS stops
at N=14"* — which is a sandbox limit written down as a result. That is the
specific damage a too-small cap does: it does not merely stop a run, it teaches
the run something false about the mathematics.

8 GiB then failed the same way, and the failure is worth recording because it
argues the *other* side. The gilbreath run died at 161 minutes — three `oom`
events, then `die exit=137` — while materialising a depth-4000 exact-integer
difference triangle. Every earlier capture answering the same question had
built that triangle a row at a time and fitted comfortably; the OOM came from
holding all of it at once, not from the mathematics getting bigger. So the cap
was raised to 16 GiB on request, and the raise bought a wrong method more room
rather than making a right one possible.

That is the shape to watch for. A cap this size is met by materialising
something that could have been streamed far more often than by a computation
that genuinely needs the space, and each raise makes the next one easier to
ask for. The compose comment used to promise 8 GiB would never move; it moved,
so the note there now records the history instead of making a firmer promise.

The raise to 24 GiB on 2026-08-17 is the only one no run asked for. It was made
against a shape of work this runtime has not yet attempted — a proof whose last
third is a generated certificate, of the kind
[`research/proofatlas/01-sendov-bundle-anatomy.md`](../research/proofatlas/01-sendov-bundle-anatomy.md)
takes apart, whose Lean build wanted one worker under a 32 GiB address-space
limit — and it did not survive the move to a shared memory server. The
accounting that argued for it was per problem: each problem kept its own Cognee
beside the shared Neo4j, and the run's own ceiling was one term in a sum nobody
was adding up.

The sum is what the current numbers are about. Several runs are live at once, so
a per-run ceiling that overcommits by itself overcommits by the number of runs;
4 GiB per run against 250 MiB reserved is a shape that stays inside the box when
a dozen of them are up. The shared half is sized once, together: Neo4j and
Cognee each reserve 1 GiB and are capped at 16 GiB. The reservations do the work
the ceilings do not — they are the floor the scheduler holds for a service that
is idle between a run's turns, which is what stops a busy neighbour from
squeezing the store every other run reads through.

CPU is bounded too, and it is worth knowing that only half of a CPU range is
enforceable here. A run gets **0.1 to 4 vCPU**. The 4 is a hard ceiling
(`cpus`). The 0.1 is not a floor Docker can give: `deploy.resources.
reservations.cpus` is accepted by the Compose schema and silently dropped
outside Swarm — measured on this box, `limits.cpus: 4` became
`NanoCpus=4000000000` while `reservations.cpus: 0.1` left `CpuShares=0` and no
floor of any kind.

So the floor is expressed as scheduling weight instead, which is *relative* and
applies only under contention: a run carries `cpu_shares: 256` against the
default 1024, which says "when every core is wanted, take mine" while still
letting it reach its full four whenever the cores are free. That fits what a run
is — bursty, and for most of its life waiting on a model call using nothing at
all.

The same mechanism is what keeps contention off the memory. Neo4j and Cognee are
capped at 4 cores each and carry `cpu_shares: 2048`, eight times a run's, so
under full load each shared service gets eight times the slice of one run
container. Without it they would compete against a dozen runs at equal priority
and lose by number, and the symptom would be every problem's recall slowing at
once rather than any one run failing.

`memswap_limit` is the *total* of RAM and swap, so 8 GiB grants 4 GiB resident
plus 4 GiB of the box's swap. Docker already allowed swap — `mem_limit` alone
defaults `memswap` to twice the memory — so what changed is that the allowance
is stated rather than inherited.

The 4,524-job Lean build is the one shape that genuinely does not fit, and it
wants a deliberately raised run — `MATH_AGENT_MEM_LIMIT` in the environment —
rather than a standing ceiling every problem is handed.

The failure mode changes with it, and this is the part to internalise. Swap
converts an OOM kill into a slowdown: the container does not die, it gets
slower by orders of magnitude, and every tool call reads as hung. `vmstat 5`
with sustained non-zero `si`/`so` is the signature, and it deserves exactly
what an OOM deserved — a finding about the method. Streaming still beats
materialising at 4 GiB for the reason it did at 8, and the reason it did at 24.

## Observability

Every run in the tree carries a `RunTracer` (`src/agent/trace.rs`). It prints an
elapsed-time console line per model call, tool call, and tool result, labelled
with the agent that produced it, and appends every event as JSON to
`config/trace.jsonl` in the selected workspace. Alongside the event records it writes
a `model_accounting` line per model call carrying the agent, the provider and
model that served it, prompt/cached/output/reasoning tokens, and the USD cost
the provider reported. The event stream cannot supply these: `ModelCompleted`
names neither the route nor the price, and with `allow_fallbacks` on the route
genuinely varies per call. They are read from the response body by
`AccountingModel` (`src/agent/accounting.rs`), which is why it is a model
wrapper rather than an event listener. Cost is recorded as the provider
reports it; deriving it from a local price table would mean reporting fiction
the moment a price changed. The console profile carries the running total. It also prints a line when a
run *fails*, which it did not: a live `organizer` retried one call six times
over two and a half minutes and then died on `openai response contained no
choices`, and the console showed the retry ladder but not its outcome — the
run simply stopped appearing. The error was in `trace.jsonl` the whole time,
which is the wrong place to need it when someone is watching the console.
The document tools refuse to read it
back: a reflection run pulled its own 1.1 MB event log into a single
339,652-token call, blowing past the compression trigger and dropping the
cache hit rate to 26% to re-read a verbatim replay of what it had already
seen. Hiding it from `list_workspace` was not enough, because an agent can
name a path the listing never offered it. Specialist runs also export their own
observations to Langfuse, and payload capture is enabled, so a Langfuse trace
carries the prompts, tool arguments, and results rather than bare ids. Read
`trace.jsonl` or the Langfuse trace when diagnosing a run; do not add a
separate logging mechanism beside them.

When changing prompts or agent behavior, keep these rules intact:

1. State assumptions and define ambiguous notation.
2. Understand before computing, and gather context before implementing.
   Identify the mathematical objects involved and the theory that governs them
   before writing full-size code.
3. Show the main derivation or argument. Do not jump straight to the answer.
4. Do not search the answer space. Enumerating candidates, or every object up
   to the bound in the statement, until one matches is prohibited even when it
   would terminate. A method whose cost grows with that bound rather than with
   the size of the problem's description is the wrong method. Brute force is
   for validating the real method on small instances.
5. Solve by theory. The bound in the statement is chosen to defeat
   enumeration, so the intended solution is a structural fact — a recurrence,
   a bijection, a closed form, a symmetry, a classification — that makes most
   of the search space unnecessary to visit. Name it before implementing it.
6. Attack the method before trusting it. State what would make it wrong and go
   looking for that case; hunt a counterexample as seriously as a proof, and
   report what was searched and how far when none is found. Survive an attempt
   to break a conjecture rather than only confirming it.
7. Say how problems of this shape have been attacked before and why this
   approach beats the alternatives. Record failed approaches with the reason —
   a known dead end is a result.
8. Delegate external fact-finding to `research` and cite the returned sources.
9. Delegate meaningful computation to `tool_builder`. Report the program or
   command and the relevant output.
10. Check edge cases, dimensions, signs, domains, and limiting behavior when
   they apply.
11. Verify by a second, independent route, or say the result is unverified.
12. Distinguish a proof, a numerical check, a heuristic, and a sourced claim.
13. Say when the evidence is incomplete. Never invent a theorem, citation, or
    computation result.

The runtime is not a formal proof assistant. Do not describe sampled evidence or a floating-point experiment as proof.
