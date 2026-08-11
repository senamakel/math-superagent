# Math Research Agent

This is a Dockerized agent for solving mathematical problems through careful
derivation, computation, and source-backed research. It is meant for problems
where a good answer may require several kinds of work: understanding the
mathematics, checking a theorem or definition, writing a small program, and
verifying the result before presenting it.

```text
                ./agent "problem"        ./euler 66
                        │                     │
                        └──────────┬──────────┘
                                   │
┌──────────────────────────────────▼───────────────────────────────────────┐
│ Docker: unprivileged, no capabilities, read-only root                    │
│                                                                          │
│   ┌──────────────┐                                                       │
│   │ orchestrator │  decomposes, delegates, writes the answer             │
│   └──────┬───────┘                                                       │
│          │ one solution loop per run                                     │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │ attempt ──> reflect ──> retry, or diversify when stuck, or done    │  │
│  │ reflection judges every attempt; see "The solution loop" below     │  │
│  └────────────────────────────────────────────────────────────────────┘  │
│          │ spawn_agent(s) returns a run ID immediately                   │
│          │ peek_agent, steer_agent, await_agent(s)                       │
│          ▼                                                               │
│  ┌────────────────┬────────────────┬────────────────┬────────────────┐   │
│  │ goals          │ research       │ tool_builder   │ coder          │   │
│  │ criteria       │ Exa, notes     │ experiments    │ the program    │   │
│  ├────────────────┼────────────────┼────────────────┼────────────────┤   │
│  │ librarian      │ scholar        │ organizer      │ reflection     │   │
│  │ downloads      │ digests them   │ indexes        │ judges one try │   │
│  ├────────────────┼────────────────┼────────────────┼────────────────┤   │
│  │ inventor       │ pattern_finder │                │                │   │
│  │ a new angle    │ exact sequences│                │                │   │
│  └────────────────┴────────────────┴────────────────┴────────────────┘   │
│     on finish: tool_builder ──> organizer                                │
│                research ──> scholar ──> organizer                        │
│          │                                                               │
│          ▼  /workspace: goal, tasks, memory, research/, code/lib/        │
└───────┬─────────────────────────┬─────────────────────┬──────────────────┘
        │                         │                     │
  workspace/<name>/         Qdrant volume       OpenRouter, Exa,
  committed to git          research notes      Langfuse, trace.jsonl
```

Every delegation is asynchronous. A spawn returns a run ID straight away, so
independent research and computation overlap instead of queueing behind each
other, and the orchestrator collects the results when it needs them. The
specialists share one `/workspace`, which is committed as the run proceeds, so
the derivation and the programs survive alongside the answer.

The runtime uses a small registry of specialist agents:

- `orchestrator` breaks a problem into focused tasks and combines the results.
- `goals` turns an objective into completion criteria and spawns focused
  subagents until the criteria are met or blocked.
- `research` searches with Exa, looks computed sequences up in the OEIS, and
  returns evidence with source URLs, working the gaps other roles stated in
  `research/REQUESTS.md` first.
- `tool_builder` writes and runs shell or Python tools for numerical checks,
  experiments, data processing, and reproducible calculations.
- `coder` has the same authority and writes the implementation the run stands
  behind. Splitting the two lets each prompt be strict about one thing: the
  tool-builder about producing a running program quickly, the coder about the
  program being correct.
- `reflection` judges one attempt and extracts the lesson. It has no research
  or execution tools, so it cannot drift into solving what it is judging.
- `pattern_finder` runs exact sequence analysis over results already computed:
  forward differences and polynomial degree, common divisors, residue
  periodicity, and a verified linear-recurrence search. Its tools report only
  what holds for every term supplied; it commissions more terms to test a
  conjecture past the data that suggested it, and looks them up in the OEIS,
  where a match usually carries the closed form.
- `inventor` proposes a different line of attack when the current one stalls.
- `librarian` downloads primary material into the reference library and indexes
  it, following what its own sources cite before searching afresh.
- `scholar` reads that library. It judges each source against the run's goal and
  current beliefs and replaces each stored digest with what the source actually
  establishes, because a downloaded paper nobody has opened has cost the run
  context and taught it nothing. It records each statement as a `claim` block —
  hypotheses, whether they hold here, what backs it — so the library is
  retrievable one statement at a time.
- `organizer` keeps the workspace navigable: folder indexes, the layout of
  `research/`, and `code/lib/INDEX.md` matching the files beside it. It cannot
  delete a result or change what a file says.

## The solution loop

Every run is driven by an explicit attempt, reflect, diversify cycle. There is
no single-turn mode: a hard problem's first approach is usually wrong, and the
single-turn path differed only in throwing that information away.

```text
  attempt ──> reflect ──┬─ solved ────────────────> done
     ▲                  ├─ retry ─────────────────> attempt
     │                  └─ stuck ──> diversify ────┘
     └────────────────────────────────────────────┘
```

Reflection runs after every attempt, not only after failures, and an answer
that was not verified by a second independent route counts as unsolved. A
`SOLVED` verdict is also rejected unless the workspace actually contains a
program: a confident final report with nothing that ever ran is the signature
failure of a small fast model, and ending the loop on it presents a guess as a
result.

The pattern agent runs concurrently with reflection on the same attempt, because
the exploitable regularity in a sequence is usually visible in the first terms a
run computes and waiting for the loop to stall means spending the budget it
would have saved. Past five attempts without a verified answer, each reflection
also re-opens the literature. By then the run knows what it tried and what the
numbers look like, which makes a far better query than the statement alone. The
loop stops after eight attempts and returns what it has.

Diversification triggers on *consecutive* unproductive attempts, so a run making
thin but genuine progress never reaches it. When it does, `diversify` runs three
arms concurrently: the librarian followed by the scholar, the pattern agent, and
the inventor. Between them they bring in material, structure, and a different
approach before the next attempt.

Some runs trigger housekeeping when they finish. A completed `tool_builder` run
starts an `organizer`, and a completed `research` run starts a `scholar` and then
an `organizer`, which is the moment the new files exist and their purpose is still
settled. Those follow-ups are fire-and-forget and serialised, so `await_agent`
returns as soon as the delegated work itself is done and tidying never sits on the
critical path.

The container includes `python`, `python3`, `pip`, and `pip3`, with `sympy`,
`numpy`, `scipy`, `gmpy2`, and `networkx` baked into the image. A run that has
to install `sympy` before it can factor anything spends minutes of its budget on
setup. Packages installed with pip are placed in the selected workspace under
`.python-packages`, so the read-only container filesystem stays intact and
dependencies persist with the problem artifacts.

A recoverable tool failure never ends a run. Every tool is registered through a
resilient wrapper that turns an error into a result the model can read and
correct, and middleware appends advice and escalates when the same tool keeps
failing. A Qdrant conflict, a bad path, or a non-UTF-8 download costs a turn
rather than the run's accumulated work.

A single tool call may run for ten minutes and a whole agent run for two hours.
Within that, an agent gets 250 model calls and 4000 tool calls; a run that
reaches the model-call cap stops and returns what it has rather than
discarding the work. Each model turn is capped at 12000 output tokens, which is
a safety ceiling against an unbounded wall clock rather than a way to make the
model concise. Set low enough to bind an ordinary turn, it truncates the model
mid-generation and buys a retry. Every limit is overridable through the
`MATH_AGENT_*` variables documented in `.env.example`.

The runtime is built to find the structure in a problem rather than to search
its answer space. The tool-builder must state time and space complexity before
substantial execution, and the runtime rejects commands declared as
exponential. A method whose cost grows with the bound in the problem statement
is treated as the wrong method, not as a slow one, and brute force is reserved
for checking the real method on small cases.

Research notes can be saved to a local Qdrant vector database and recalled in
later runs. The database uses deterministic local feature vectors, so it does
not need another embedding API. Pass `--no-research` to withhold web search
entirely, which turns a run into a test of reasoning rather than of lookup.

All model calls use DeepSeek V4 Flash through OpenRouter, preferring the
DeepInfra route by default so the large fixed prompt prefix keeps hitting one
provider's cache. Fallbacks stay enabled, so a busy provider never halts the
runtime. Set `OPENROUTER_MODEL` or `MATH_AGENT_PROVIDER` to change either.
TinyAgents provides the model loop, tools, delegation, and middleware.

## Watching a run

The console shows an elapsed-time line for every model call, tool call, and
tool result, labelled with the agent that produced it:

```text
[00:00] orchestrator     run started (run-1)
[00:00] orchestrator     model call #1 -> deepseek/deepseek-v4-flash-0731
[00:14] orchestrator     model done    13820ms in=9241 cached=8960 out=612 | profile model 96% tool 0% idle 4% | cache 96% | $0.0031
[00:14] orchestrator     tool  call #1 -> spawn_agent
[00:14] tool_builder/agent-run-2  spawned: Read /workspace/problem.md and extract the exact statement...
[00:33] tool_builder/agent-run-2  tool  done    execute_command in 412ms, 1180 bytes
[01:12] orchestrator     solution loop: verdict unsolved, progress yes, next attempt
```

Every model completion carries the run's time attribution, prompt-cache hit
rate, and cumulative spend, so a slow or expensive run is visible without
leaving the console. Once agents run concurrently the percentages become shares
of agent time and a concurrency factor replaces `idle`, because summed agent
time legitimately exceeds the wall clock.

The same events are appended as JSON to `trace.jsonl` in the selected workspace,
alongside a `model_accounting` record per model call naming the agent, the
provider and model that actually served it, the prompt, cached, output, and
reasoning token counts, and the cost the provider reported. With fallbacks
enabled the route genuinely varies per call, so it is read from each response
body rather than derived from a local price table. The orchestrator and every
specialist also export their observations to Langfuse with prompts and tool
payloads attached. Use `trace.jsonl` for a quick local replay and Langfuse when
you need the full prompts; `./langfuse-turns` and `./langfuse-review` query
recorded turns from the host.

The document tools refuse to read `trace.jsonl` back. One reflection run pulled
its own 1.1 MB event log into a single 339,652-token call to re-read a verbatim
replay of what it had already seen.

## Run a problem

Requirements:

- Docker
- OpenRouter, Exa, and Langfuse credentials

Copy the environment template and fill in the local values:

```sh
cp .env.example .env
```

Then give the agent a problem:

```sh
./agent "Research the prime number theorem, explain the main idea, and numerically compare pi(x) with x/log(x) for x up to one million"
```

The shorter form above is equivalent to:

```sh
./agent run "your problem"
```

Three helper commands are also available:

```sh
./agent build     # build the runtime image
./agent shell     # open a shell under the same Docker restrictions
./agent prompts   # print every role's assembled system prompt with token counts
```

`./agent prompts` runs on the host and needs no container, provider key, or
spend. Use it after changing a prompt or the context routing: it is the only way
to see what an agent is actually told without starting a run, and the token
counts matter because every prompt is re-sent on every model call in that role's
run.

## Solve a Project Euler problem

Pass a positive problem number to the Project Euler wrapper:

```sh
./euler 1
./euler 66 --no-research
./euler 10 "also compare the optimized method with a brute-force check"
```

The wrapper downloads the official statement from Project Euler's minimal
problem endpoint, then runs the orchestrator in
`workspace/project-euler/<number>` against a five-phase task: understand the
statement, establish the governing theory, derive the method, implement it, and
verify it independently. Full-size code waits on the derivation, and the worked
examples are the oracle `solution.py` must reproduce before running at scale.

The research agent may look up definitions, named theorems, and standard
algorithms, but the prompt forbids searching for published Project Euler
answers. Pass `--no-research` before the problem number to withhold web search
altogether, which is the honest setting for a problem whose statement is
self-contained.

The downloaded statement, the working files, and the run's event log remain
beside the solution:

```text
workspace/project-euler/66/
├── problem.md          # the statement, converted from the fetched HTML
├── GOAL.md             # system files are upper-case; the run's own prose
├── MEMORY.md
├── CONTEXT.md
├── solution.md
├── INDEX.md            # what each file beside it is for
├── code/               # every program, with its own AGENTS.md and INDEX.md
│   ├── out/            # what those programs produced
│   ├── lib/            # what other programs import, one subject per module
│   └── <question>/     # the programs attacking one question, with its INDEX.md
├── research/           # L0/L1/L2 sources, INDEX.md, and the derived ledgers
├── reflections/L0/     # one note per judged attempt; raw/ holds download bytes
└── config/             # config.toml, problem.url, the ledgers, trace.jsonl
```

Generated programs, calculations, and other artifacts appear in
`workspace/default` unless another workspace is selected. A new workspace is
seeded from [`workspace/template/`](workspace/template/) without overwriting it. The seed includes local agent instructions, role
prompts, configuration, `GOAL.md`, `TASKS.md`, `SCRATCHPAD.md`, `MEMORY.md`, and
empty `research/` and `code/lib/` folders. The runtime reads those files at the
start of every run.

Everything downloaded is filed under `research/`, enforced in code rather than
asked for in a prompt, so gathered material stays separate from the run's own
derivations and programs.

`code/` is a Python package tree, and `/workspace/code` is on `PYTHONPATH`, so
every folder in it is importable by name from any working directory: a helper
at `code/lib/perms.py` is `from lib.perms import lex_ranks`. The tool-builder
accumulates what a second program would repeat under `code/lib/`, one subject
per module, so reading the helper you need costs a few hundred bytes rather
than the whole library; everything else is grouped by the question it attacks.
`orchestrator::code_layout` measures the result — a routine defined in three
separate programs, a `code/` past ten loose files, a folder of programs with no
index — and hands the organizer one fault per cycle. Reuse is measured rather
than requested because asking for it in a prompt did not work: one committed
workspace holds forty-six sibling programs defining `H(n)` seven times over,
beside a helper folder nothing imported.

Every folder carries an `INDEX.md` saying what each file is for, because
`list_workspace` answers what exists but not what anything is *for*, and after a
long run nothing on disk distinguishes the oracle from the answer.
`describe_file` records a purpose and `refresh_index` re-derives the file list
from disk, keeping existing descriptions, marking new files undescribed, and
dropping rows for files that are gone. Descriptions are left to explicit calls
because only the agent that wrote a file knows why, so a forgotten one shows as
a visible gap rather than as an index quietly disagreeing with its folder. Every
reflection is archived under `reflections/` with a filename recording whether it
produced learnings.

Each agent receives only the working files its role actually needs: reflection
sees the goal and the record but never the scratchpad, because provisional
arithmetic is not evidence of progress; the inventor always sees which approaches
already failed; and the pattern agent sees the raw computed data. Indexes are the
cheap exception, costing a few hundred tokens where the files they describe cost
tens of thousands, so each planning role gets the catalogues that change what is
worth delegating next. `AGENTS.md`, the method policy, is the only file every
role receives. The full routing table is in
[`AGENTS.md`](AGENTS.md); `./agent prompts` shows the result.

The workspace is also its own git repository, kept in
`.workspace-history`, and the runtime commits after every successful write, so
an overwritten program or a revised belief stays recoverable.

These files are committed rather than ignored, so a solved problem keeps its
derivation, program, and notes in history. Pip installs under
`.python-packages/`, bytecode caches, and the multi-megabyte `trace.jsonl` event
log are excluded; read a trace locally or in Langfuse.

Downloads are converted to Markdown before they are stored: HTML is stripped of
scripts, styles, and navigation, a PDF's text layer is extracted, and TeX is
preserved intact. The HTML converter is hand-written because a general-purpose
one escapes the backslashes in `\(…\)` and destroys the mathematics. Magic bytes
beat the declared content type, since a PDF served as `text/html` is still a PDF.
Links become reference-style with one list at the end and tracking parameters
removed, so a page's URLs cost a few characters each rather than filling the
context.

A download lands as two files side by side: `<name>.md` holding a bounded digest
and `<name>.full.md` holding the complete text. One real reference page converted
to about 23,000 tokens, and three of those fill a specialist's context before it
has done any work, so reading the short one is the default and reading the long
one is a decision. The digest is *structural* rather than the leading
characters — the heading outline, the abstract, and every paragraph opening
`Theorem`, `Lemma`, `Definition` and the rest — because for a paper the leading
characters are the title and half the introduction while the labelled
statements are the payload. Its citations accumulate in `research/FRONTIER.md`,
ranked by how many of the library's own sources cite each, so a second download
of one already held is refused and a URL three papers agree on rises to the top.

Every runtime agent can use bounded document tools to download HTTP or HTTPS
text, read and store files, make exact edits, index documents and search that
index, plus `search_claims` for what the library establishes and
`request_research` for what it does not. The index lives at
`.document-index.json` in the selected workspace; downloads are capped at 5
MiB, paths cannot leave `/workspace`, and one workspace cannot search another's.

The tool-builder additionally gets `apply_patch`, applying a Codex-format
envelope across several files at once. Two deviations are deliberate: context
matching is exact and an ambiguous hunk is refused rather than fuzzily
resolved, because a patch landing in the wrong place yields a program that runs
and computes something else; and application is atomic, so a bad hunk in the
third file cannot leave the first two rewritten.

Use `--workspace` to give a run its own subdirectory:

```sh
./agent --workspace prime-number-theorem "Research and test useful bounds for pi(x)"
```

That command mounts only `workspace/prime-number-theorem` at `/workspace`.
`MATH_AGENT_WORKSPACE=prime-number-theorem ./agent "..."` provides the same
selection through an environment variable. Absolute paths, parent traversal,
and symlinks that leave the repository's `workspace/` root are rejected.

## How a run works

The orchestrator decides which specialist handles each part of the problem.
Open-ended objectives go to the goals agent, which spawns other specialists and
tracks evidence against explicit completion criteria; research questions go to
the Exa-backed research agent, which recalls related notes from Qdrant and saves
sourced findings; computations and executable checks go to the tool-builder, and
the implementation the answer rests on to the coder. The orchestrator then
writes one answer separating cited facts from its own reasoning.

Subagent work runs asynchronously through TinyAgents graphs. `spawn_agent`
returns a run ID immediately, so independent research and computation run in
parallel; `peek_agent` inspects status, `steer_agent` redirects live work, and
`await_agent` retrieves the response. `spawn_agents` and `await_agents` do the
same for a batch in one turn, which is the shape most delegation takes —
awaiting one run at a time serialises work that already ran in parallel. The
orchestrator and goals agent share this surface; there is no blocking call.

Up to fifty runs execute concurrently; further spawns queue for a slot without
blocking the caller (`MATH_AGENT_MAX_CONCURRENT_AGENTS`). Each agent develops an
affinity for whichever OpenRouter provider served its last turn, so its large
fixed prompt prefix keeps hitting that provider's cache; fallbacks stay enabled,
so a busy provider moves the affinity rather than stalling the run.

Context compression starts at an estimated 300,000 tokens. A model-backed
summary keeps the decisions, assumptions, formulas, source URLs, command
results, and unresolved work; recent messages remain verbatim. If the summary
call fails, TinyAgents trims old context instead of losing the whole run.

This is a research and computation assistant, not a formal proof checker;
important results should still be checked against primary sources or a proof
assistant when the stakes justify it.

## Docker Compose stack

`./agent` uses [`compose.yaml`](compose.yaml) to run two services:

- `agent` is the Rust orchestrator and its specialist tools.
- `qdrant` is the local vector database. Its `qdrant-data` volume persists
  research notes across agent containers and workspace selections.

Stop the background database with `docker compose down`. Add `--volumes` only
when you deliberately want to erase the saved research index.

## Docker boundary

The agent runs as an unprivileged user in Docker. The helper applies these
restrictions:

- all Linux capabilities are dropped;
- `no-new-privileges` is enabled;
- the container root filesystem is read-only;
- process count and memory are capped;
- only the local `workspace/` directory is mounted read-write at `/workspace`;
- the repository and Docker socket are not mounted.

Network access stays enabled because OpenRouter, Exa, and Langfuse require it.
The tool-builder can change files under `/workspace`, but it cannot change the
host repository through the container.

## Repository map

```text
agent                       simple Docker Compose helper
euler                       Project Euler problem wrapper
langfuse-turns              recorded-turn query helper
langfuse-review             recorded-turn review helper
Dockerfile                  build and runtime jail
compose.yaml                agent and Qdrant services
scripts/run-agent           helper implementation
scripts/solve-euler         fetch and solve workflow
workspace/                  selectable agent workspaces, committed with their runs
└── template/               seed instructions, prompts, config, and memory
src/
├── prompts/                built-in role prompts, included at compile time
├── agent/                  TinyAgents facade, OpenRouter, Langfuse
│   ├── accounting.rs       per-call provider, token, and cost accounting
│   ├── budget.rs           per-run call, wall-clock, and capture policy
│   ├── reflection.rs       in-run middleware that reflects on failing tools
│   ├── resilient.rs        tool-error and request-timeout wrappers
│   ├── sticky.rs           provider affinity that keeps the prompt cache warm
│   └── trace.rs            live console and trace.jsonl event listener
├── orchestrator/           registry, specialists, compression, workspace tools
│   ├── async_subagents.rs  graph-backed spawn, peek, steer, and await controls
│   ├── solutions.rs        graph-backed attempt/reflect/diversify loop
│   ├── documents.rs        bounded workspace document storage and search
│   ├── readable.rs, digest.rs   HTML/PDF to Markdown; the digest of a download
│   ├── claims.rs, threads.rs    what the library establishes; where it is going
│   ├── frontier.rs, requests.rs what it cites; what the run is short of
│   ├── oeis.rs             sequence lookup, filed and cross-referenced
│   ├── folder_index.rs, context_tree.rs, code_layout.rs   what is where
│   └── patch.rs, patterns.rs, checkpoint.rs, vector.rs   the rest
├── hello_agent/            small single-agent example
├── error/                  crate-wide errors
└── lib.rs                  public Rust API
examples/
├── orchestrator.rs         Docker runtime entry point
├── dump_prompts.rs         host-side prompt renderer behind `./agent prompts`
└── hello_agent.rs          direct single-agent example
vendor/tinyagents/          pinned TinyAgents submodule
```

The crate deliberately leaves out TinyAgents memory domains, channels, Web3,
SQLite persistence, REPL, and RLM features. The goal is a small mathematical
research runtime, not a general agent platform.

## Development

Initialize the vendored dependency and run the same checks as CI:

```sh
git submodule update --init --recursive
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo build --all-targets --all-features
cargo test --all-features
```

The minimum Rust version is 1.96. See [`AGENTS.md`](AGENTS.md) for repository
rules and implementation conventions.

## License

GPL-3.0-only. See [`LICENSE`](LICENSE).
