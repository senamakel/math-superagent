# Math Research Agent

> [!NOTE]
> This is my workspace to focus on solving complicated math problems based on
> four fundamental insights I've derived from building harnesses and agents.
> 
> 1. Cost of tokens/intelligence has dropped significantly (Deepseek V4 flash) making it incredibly efficient to burn large amount of tokens for intelligence
> 2. Context rot can be reduced with tiering of agents (subagents)
> 3. Running agents at scale, concurrently and parallely is where the efficiency lies (Rust and using OpenHuman). Building an orchestrator layer where agents can share memory, work and code is what multiplies intelligence.
> 4. Self learning loops is key towards reaching towards a shared goal.
>
> In this repo you'll find the exact architecture I've used to solve problems and conjectures. It is run entirely on DeepSeek v4 for less than 100$ in tokens.
> Initial runs faced issues and roadblocks so I started building this engine by getting it to solve simple problems on Project Euler before scaling it up to more complex problems and conjectures.
>
> The idea to solve conjectures is that if we have a capable enough harness with decent memory, coding tools (Python) and massive parallelism; then what if we could download all the possible documentations and attempts that were made to prove/disprove the conjecture, compress that into a sizable enough context (10k token limit for context and memory) and just throw a LOT of agents into it?
> 
> The entire system was run on a 32 GB RAM, 30 core CPU Linux machine and a 2 TB NVME SSD.

> [!NOTE]
> NOTE #2
>
> I've shifted my work towards OpenCompany and hivemind based agents.

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
│  │ librarian      │ scholar        │ reflection     │ judge          │   │
│  │ downloads      │ digests them   │ learns         │ checks conduct │   │
│  ├────────────────┼────────────────┼────────────────┼────────────────┤   │
│  │ inventor       │ pattern_finder │ context_curator│                │   │
│  │ a new angle    │ exact sequences│ the brief      │                │   │
│  └────────────────┴────────────────┴────────────────┴────────────────┘   │
│     on finish: research ──> scholar                                      │
│          │                                                               │
│          ▼  /workspace: goal, tasks, research artifacts, code/lib/       │
└───────┬─────────────────────────┬─────────────────────┬──────────────────┘
        │                         │                     │
  workspace/<name>/         CortexDB             local router, Exa,
  committed to git          durable memory       Langfuse, trace.jsonl
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
- `reflection` is the learning agent: it recalls prior lessons, judges one
  attempt, and has its new lesson stored automatically. It has no
  research or execution tools, so it cannot drift into solving what it judges.
- `pattern_finder` runs exact sequence analysis over results already computed:
  forward differences and polynomial degree, common divisors, residue
  periodicity, and a verified linear-recurrence search. Its tools report only
  what holds for every term supplied; it commissions more terms to test a
  conjecture past the data that suggested it, and looks them up in the OEIS,
  where a match usually carries the closed form.
- `inventor` proposes a different line of attack when the current one stalls.
- `context_curator` owns `CONTEXT.md`, the brief nearly every other role is sent
  on every model call. It runs as a standing team every
  `MATH_AGENT_CONTEXT_MINUTES` (five by default) and keeps that one file current
  and within `MATH_AGENT_CONTEXT_TOKENS` (ten thousand): the established results
  and their basis, the approaches that died and why, what the numbers look like,
  and what the memory holds from earlier runs on this problem — invisible to
  this one until somebody carries it into the file everyone already reads. It has
  no shell, no web search, and no delegation, so curating what the run knows
  cannot become a second investigation beside the solve.
- `librarian` downloads primary material into the reference library, following
  what its own sources cite before searching afresh.
- `scholar` reads that library. It judges each source against the run's goal and
  current beliefs and replaces each stored digest with what the source actually
  establishes, because a downloaded paper nobody has opened has cost the run
  context and taught it nothing. It records each statement as a `claim` block —
  hypotheses, whether they hold here, what backs it — so the library is
  retrievable one statement at a time.

Every role has `recall_memory` and `remember_memory`. The memory server is the
only cross-run memory; research sources and program output remain ordinary
current-run artifacts. Every completed or failed agent session is also stored,
named for the workspace project and runtime session. Recall reaches this
problem's brain, library and sessions, and never its scratch — provisional work
is not durable knowledge. Which server that is, and what keeps one problem's
memory out of another's, is [`docs/memory.md`](docs/memory.md).

## The solution loop

Every run is driven by an explicit research, attempt, evaluate cycle. There is
no single-turn mode: a hard problem's first approach is usually wrong, and the
single-turn path differed only in throwing that information away.

```text
  research ──> attempt ──┬─> judge ──────────┐
      (once)     ▲       ├─> reflect ────────┤
                 │       ├─> patterns ───────┤
                 │       ├─> invention ──────┼─> merge ──> solved ──> done
                 │       ├─> library (opens) ┤         ├─> retry ────┐
                 │       └─> goals ──────────┘         └─> stuck ────┤
                 └──────────────────────────────────────────────────-┘
```

Research runs once, before anything is attempted: establish what the workspace
already has, then go looking for what it does not. Everything after an attempt
runs *at the same time* — five questions about the same report, none of which
reads another's answer — so a cycle costs the slowest of them rather than the
sum.

The judge and the reflection answer different questions. Reflection asks whether
the answer is right, and it alone can end the loop; an answer that was not
verified by a second independent route counts as unsolved, and so does a
confident final report with no program behind it. The judge asks whether the
attempt was *conducted* in a way the next one should inherit, and returns
PROCEED, STEER, or RESTART.

Reflection runs after every attempt, not only after failures, because the lesson
from a partial success is what stops the next attempt repeating it. The pattern
agent runs after every attempt too, because the exploitable regularity in a
sequence is usually visible in the first terms a run computes — it is one of the
concurrent arms rather than something waited for.
Past five attempts without a verified answer, each reflection also re-opens the
literature: by then the run knows what it tried and what the numbers look like,
which makes a far better query than the statement alone. Diversification triggers
on *consecutive* unproductive attempts, so a run making thin but genuine progress
never reaches it. The loop stops after eight attempts and returns what it has.

Every threshold above is a number a live run has already met, and the reasoning
for each one is in [`docs/solution-loop.md`](docs/solution-loop.md).

The container includes `python`, `python3`, `pip`, and `pip3`, with `sympy`,
`numpy`, `scipy`, `gmpy2`, and `networkx` baked into the image, alongside the
constraint stack (`z3`, `cvc5`, CP-SAT, PySAT, `nauty`) and Lean 4 with a
pre-built Mathlib. A run that has to install `sympy` before it can factor
anything spends minutes of its budget on setup. Packages installed with pip are
placed in the selected workspace under `.python-packages`, so the read-only
container filesystem stays intact and dependencies persist with the problem
artifacts.

A recoverable tool failure never ends a run. Every tool is registered through a
resilient wrapper that turns an error into a result the model can read and
correct, and middleware appends advice and escalates when the same tool keeps
failing. A memory request failure, a bad path, or a non-UTF-8 download costs a
turn rather than the run's accumulated work.

A single tool call may run for ten minutes and a whole agent run for two hours.
Within that, an agent gets 250 model calls and 4000 tool calls; a run that
reaches the model-call cap stops and returns what it has rather than discarding
the work. Every limit is overridable through the `MATH_AGENT_*` variables
documented in `.env.example`, and [`docs/runtime.md`](docs/runtime.md) says what
each one is protecting against.

The runtime is built to find the structure in a problem rather than to search
its answer space. The tool-builder must state time and space complexity before
substantial execution. An intractable declaration is refused unless it carries a
concrete `oracle_bound` — brute force validating the real method on small
instances is legitimate, an unbounded search is not — and so is a declaration
that names a search strategy instead of a cost.

One memory server is the sole durable memory. Every role can recall prior
results, lessons, sources, and failed approaches, and the three roles whose
output is durable knowledge can store them. Pass `--no-research` to withhold web
search; recall remains available.

All general model calls go through the authenticated OpenAI-compatible router
on port 6969. Ordinary roles send model id `flash`; the roles listed in
`REASONING_ROLES` — the judge, the director, the reducer and the orchestrator
itself — send `reasoning`; and the three in `MAX_REASONING_ROLES` —
`inventor`, `reflection`, `weakener` — send `max-reasoning`,
the router's deepest ladder, which pays more per token and asks each rung for
the deepest thinking setting its model family accepts. All three tiers
advertise a one-million-token context window, while the router owns the
provider, price, depth, and fallback ladder.
Host-side calls default to `http://localhost:6969/v1`; Compose reaches that same
router as `http://ladder:6969/v1` on a shared internal network and publishes it
only on host loopback. One ladder serves every checkout and every problem on the
box — it lives in `compose.shared.yaml` beside the graph store, not in any one
run's project, and tracks `ghcr.io/senamakel/llm-ladder-router:latest` so a fix
in the router repository arrives on the next `scripts/shared-up`. The pinned image mounts the sibling
`llm-ladder-router/config.toml`; `LADDER_CONFIG_PATH` and `LADDER_ENV_FILE`
override those host paths when the repositories live elsewhere.
TinyAgents provides the model loop, tools, delegation, and middleware.


## Watching a run

The console shows an elapsed-time line for every model call, tool call, and
tool result, labelled with the agent that produced it:

```text
[00:00] orchestrator     run started (run-1)
[00:00] orchestrator     model call #1 -> flash
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

That one stream carries every role and child run they spawn, which is right for
a trace and noisy for watching. `./euler-tui <number>` watches the same box
behind a tab per team:

```sh
./euler 763                     # start or continue the run
./euler-tui 763                 # watch it, a tab per team
./euler-tui 763 --replay        # read the last run's log; touch nothing
./euler-tui 763 --plain         # no tabs, stream to stdout, as when scripting
```

The workspace is the identity, not the problem number, so anything else is
watched by naming it:

```sh
./conjecture erdos-gyarfas      # start or continue an open-problem run
./euler-tui --workspace conjectures/erdos-gyarfas
```

`euler-tui` **cannot start, stop, or restart a run**. That is the design rather
than a gap: when starting was part of the same command, opening a second view
started a second run on the same workspace — both writing the same files and
both making checkpoint commits over each other. `docker logs` replays a
container from its start, so attaching an hour in still populates every tab
before the first frame.

It can direct a run that already exists. Press `i`, type, and press Enter; or
from another terminal:

```sh
./steer 763 check the n=14 bound against a sieve
./steer --workspace conjectures/erdos-gyarfas "stop enumerating and prove it"
```

The run never waits for you: a directive is queued in the workspace, reaches the
next attempt word for word above anything the run concluded on its own, and a
`director` role updates the files that decide what happens next. It cannot force
a restart, end the run, or make an unverified answer count as solved. What
happened to it is written to `config/DIRECTIVES.md`. Sending is refused under
`--replay` and unavailable under `--plain`. See
[`docs/solution-loop.md`](docs/solution-loop.md#direction-from-a-human).

It is a `ratatui` binary, built behind the optional `tui` feature so the
runtime image — which has no terminal — does not carry a terminal library. The
`./euler-tui` wrapper builds it once in release mode and then execs it.

`Tab`, `n`, or the right arrow move to the next team and `Shift-Tab`, `p`, or
the left arrow to the previous; the digits jump straight to one; the arrows and
page keys scroll back, `g` returns to live, `i` opens a line to direct the run,
and `q` detaches without stopping it. Input is polled every 15ms and every event waiting is consumed before
the next repaint, so a keypress lands immediately and a held arrow scrolls by
its whole run rather than one line per frame.

Lines are coloured by what they report, so the shape of a run is readable while
it scrolls: faults red, the loop's own verdicts yellow and bold, a spawn blue, a
started tool call cyan and a finished one green — the gap between those two is
where a ten-minute command sits, visible as a colour nothing has answered yet.
Model calls are dimmed, because they are the bulk of the stream and rarely what
is being looked for. The status bar turns red when the run has met a fault and
carries the count. A terminal without colour falls back to plain attributes.

The loop's own lines — attempt boundaries, judge scores, verdicts, team
lifecycle — appear in *every* tab, because they are the run's spine and nobody
should have to be on the right tab to see one.

Nothing is filtered out of the record: the raw stream is teed verbatim to
`config/console.log` in the workspace, so `grep` and the existing tooling work
unchanged, and a tab nobody opened still loses nothing. Without a terminal the
command degrades to a plain tee, so the same invocation works when a person is
watching and when something is scraping.

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
- local router, Exa, and Langfuse credentials

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

## Measure the harness against a solved conjecture

An open conjecture gives a run no known destination, so there is no way to tell
a harness closing in on a proof from one producing plausible mathematical
activity. A **calibration run** supplies one: a problem that has already been
solved, stated as open, with the literature carrying its answer withheld in
code — at the container's network boundary and again at the tool layer.

```sh
./calibrate unit-distance-plane-chromatic     # start or continue
scripts/eval-report unit-distance-plane-chromatic
```

Watch it exactly as any other conjecture run, with `./diagnose --workspace
conjectures/<slug>` and `./euler-tui --workspace conjectures/<slug>`.

Three problems ship, spanning three ways of attacking one:
`unit-distance-plane-chromatic` (construction and machine verification),
`hypercube-induced-degree` (one idea, no scale), and
`consecutive-perfect-powers` (deep machinery, and whether the run knows it is
out of its depth). See [`evals/README.md`](evals/README.md) for the set and
[`docs/calibration.md`](docs/calibration.md) for what the controls do and,
just as importantly, what they cannot: blocking retrieval does not block
recall, and the report says so.

## Solve a Project Euler problem

Pass a positive problem number to the Project Euler wrapper:

```sh
./euler 1
./euler 66 --no-research
./euler 10 "also compare the optimized method with a brute-force check"
```

The solution loop runs on a declarative workflow graph. The engine owns the
routing — which attempt follows which verdict — and each step is a call into
the same Rust the loop has always used. So the control flow is a document that
can be read, patched through validated operations, and rendered, while the
steps that carry a directive into an attempt or salvage a timed-out one are
unchanged.

The loop is not the only graph. It calls a child workflow that decides, on a
cadence, whether to work backward from the goal and write down what would
suffice to prove it — so a decomposition is opened beside the first attempt
rather than after it, and the loop never waits for one.

Give the renderer a directory for every flow, or a file for the loop alone:

```sh
cargo run --features graph-debug --bin graph-render -- diagrams/
cargo run --features graph-debug --bin graph-render -- loop.png
```

### Open conjectures

A Project Euler problem has one number as its answer and a ceiling on how long
it can reasonably take. An open conjecture has neither, so `./conjecture <slug>`
carries a different task shape: build the reference library first, extract what
is actually known about the problem, build an exact oracle, and only then work
the attempt loop. It reads `workspace/conjectures/<slug>/problem.md` and
`GOAL.md` — the statement and what counts as a result live in the workspace, not
in the script.

```sh
./conjecture erdos-gyarfas
```

`workspace/conjectures/erdos-gyarfas/` is the worked example: the Erdős–Gyárfás
conjecture, that every finite simple graph with minimum degree at least 3 has a
cycle whose length is a power of two. It is open, and the run is told so — the
deliverable is a partial result stated exactly, never a claim of the whole.

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
├── CONTEXT.md         # the shared brief, curated and token-budgeted
├── solution.md
├── INDEX.md            # what each file beside it is for
├── code/               # every program, with its own AGENTS.md and INDEX.md
│   ├── out/            # what those programs produced
│   ├── lib/            # what other programs import, one subject per module
│   └── <question>/     # the programs attacking one question, with its INDEX.md
├── research/           # sources/, summaries/, notes/, and the run's own prose
├── derived/            # the ledgers the runtime renders — never hand-written
├── attempts/<id>/      # one candidate solution's own checkout, on its own branch
└── config/             # config.toml, problem.url, the queues, trace.jsonl
```

`derived/` is committed and meant to be read by people, but the agent's file
tools refuse it: a rendered ledger is reached with `read_ledger`, which bounds
what it returns and can select one entry rather than returning all of them.

Generated programs, calculations, and other artifacts appear in
`workspace/default` unless another workspace is selected. A new workspace is
seeded from [`workspace/template/`](workspace/template/) without overwriting it. The seed includes local agent instructions, role
prompts, configuration, `GOAL.md`, `derived/TASKS.md`, and
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
Code folders may carry an `INDEX.md` saying what each file is for, because
`list_workspace` answers what exists but not what anything is *for*, and after a
long run nothing on disk distinguishes the oracle from the answer.
`describe_file` records a purpose and `refresh_index` re-derives the file list
from disk, keeping existing descriptions, marking new files undescribed, and
dropping rows for files that are gone. Descriptions are left to explicit calls
because only the agent that wrote a file knows why, so a forgotten one shows as
a visible gap rather than as an index quietly disagreeing with its folder.
Research and learning folders deliberately have no `INDEX.md`; their durable
catalogue and recall path is the memory server.

Each agent receives only the working files its role actually needs: reflection
sees the goal and the record but never the scratchpad, because provisional
arithmetic is not evidence of progress; the inventor recalls which approaches
already failed; and the pattern agent sees the raw computed data. `AGENTS.md`, the method policy, is the only file every
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
the Exa-backed research agent; computations and executable checks go to the
tool-builder, a reduction already stated as a finite decision problem to the
`sat_solver`, and so on across the roles. The orchestrator then writes
one answer separating cited facts from its own reasoning.

Subagent work runs asynchronously. `spawn_agent` returns a run ID immediately,
so independent research and computation run in parallel; `peek_agent` inspects
status, `steer_agent` redirects live work, and `await_agent` retrieves the
response, with `spawn_agents` and `await_agents` doing the same for a batch in
one turn. There is no blocking call. Up to fifty runs execute concurrently and
further spawns queue for a slot without blocking the caller.

Context compression starts at an estimated 300,000 tokens; a model-backed
summary keeps the decisions, assumptions, formulas, source URLs, command
results, and unresolved work, and recent messages remain verbatim.

[`docs/roles.md`](docs/roles.md) says what each role may reach and what it is
told; [`docs/runtime.md`](docs/runtime.md) covers the budget, the provider
affinity, and the tracing.

This is a research and computation assistant, not a formal proof checker;
important results should still be checked against primary sources or a proof
assistant when the stakes justify it.


## Docker Compose stack

`./agent` uses [`compose.yaml`](compose.yaml), and by default it starts exactly
one service: `agent`, the Rust orchestrator and its specialist tools.
`docker compose config --services` returns `agent` alone.

The memory server is **one process for every problem**
([`compose.shared.yaml`](compose.shared.yaml), alongside the ladder). A run
reaches it by address — `MATH_AGENT_MEMORY_URL`, defaulting to the host gateway
— rather than by joining its Docker network, so the whole stack can live on a
machine of its own: it is every problem's memory and none of its compute, and
`MATH_AGENT_SHARED_HOST` is what puts it there. There is no `depends_on`: the
memory server outlives any one run, and a run must never be able to take it
down.

`MATH_AGENT_MEMORY` picks which one. **`cortex`**, the default, is a CortexDB:
it carries its own knowledge graph and its own vector index, embeds through the
ladder, and answers a write only once the indexes have taken it — so a write
that returns is a document that can be recalled, which is not a property the
alternative has. **`cognee`** is that alternative, a Cognee plus the Neo4j
Enterprise instance it stores its graph in; both sit behind a Compose profile,
so an ordinary `scripts/shared-up` starts neither.

The four stores — the brain, the sessions, the library and the scratch — are
the same either way, and so is the rule that durable recall cannot reach the
scratch. What differs is what separates one problem's memory from another's:
under `cognee` the server refuses another tenant's dataset outright, and under
`cortex` it is the scope the runtime builds from the workspace label, with no
tool argument able to name one. [`docs/memory.md`](docs/memory.md) is the
comparison, the measurements behind the switch, and what the weaker boundary
costs — including why a calibration run gets a memory server of its own rather
than relying on it.

`scripts/memory-up <workspace-label>` resolves and checks the address;
`scripts/memory-up --key <workspace-label>` prints the credential. Under
`cognee`, `scripts/memory-inventory <workspace-label>` says which datasets a
problem holds, and its graph is readable in a browser at
`http://localhost:7474` (`neo4j` / `cognee-local`).

One shared server replaced one container per problem, which cost a server and a
resident embedding model each and made the `mem_limit` of the tenth stack the
question of whether it fit on the box at all. The failure to watch for in return
is contention: a shared Cognee is what produced a `409 Conflict` on a
`recall_memory` that had already hung the full ten-minute tool ceiling, under
four concurrent runs. [`docs/memory.md`](docs/memory.md) has what to measure if
it returns.

Both engines are reached over their HTTP APIs rather than as embedded libraries,
so the runtime and anything else looking at the same server always read and
write one service-owned store instead of opening independent copies of it.

## Docker boundary

The agent runs as an unprivileged user in Docker. The helper applies these
restrictions:

- all Linux capabilities are dropped;
- `no-new-privileges` is enabled;
- the container root filesystem is read-only;
- process count and memory are capped;
- only the selected `workspace/` subdirectory is mounted read-write at
  `/workspace`;
- the repository and Docker socket are not mounted.

Network access stays enabled because the model providers, Exa, and Langfuse require it.
The tool-builder can change files under `/workspace`, but it cannot change the
host repository through the container.

## Repository map

```text
agent                       simple Docker Compose helper
euler                       Project Euler problem wrapper
conjecture                  open-conjecture run wrapper
euler-tui                   tabbed console for one run, a tab per team
langfuse-turns              recorded-turn query helper
langfuse-review             recorded-turn review helper
Dockerfile                  build and runtime jail
compose.yaml                the agent service, one container per run
scripts/                    the helpers' implementations
workspace/                  selectable agent workspaces, committed with their runs
└── template/               seed instructions, prompts, and config
src/prompts/                built-in role prompts, included at compile time
src/agent/                  TinyAgents facade, providers, budget, tracing
src/orchestrator/           registry, specialists, workspace and document tools
src/bin/euler_tui.rs        the tabbed console, behind the `tui` feature
examples/                   the Docker entry point and two direct examples
docs/                       the rationale behind the rules in AGENTS.md
vendor/tinyagents/          pinned TinyAgents submodule (the agent turn)
vendor/tinyflows/           pinned TinyFlows submodule (the state graph)
```

[`docs/runtime.md`](docs/runtime.md) carries the module-by-module map and says
what each one is responsible for. It lives there rather than here because a
file-level tree in a README drifts silently: nothing fails when a module is
added, so the map quietly stops describing the crate.

The crate deliberately leaves out TinyAgents memory domains, channels, Web3,
SQLite persistence, REPL, and RLM features, and takes TinyFlows with default
features only — its workflow engine, host capabilities, Chrome companion, and
durable store are all a host concern this crate already solves its own way. The goal is a small mathematical
research runtime, not a general agent platform.

## Development

Initialize the vendored dependencies and run the build contract:

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
