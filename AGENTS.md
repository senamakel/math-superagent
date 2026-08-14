# Repository Guidelines

This file is the working agreement for humans and coding agents in this
repository. `CLAUDE.md` points here so every agent follows the same rules.

## What this repository is

This repository contains a Dockerized mathematical problem-solving agent. Its specialty is
deep research: it combines mathematical reasoning with source discovery,
small programs, numerical experiments, and explicit verification.

The product should help a reader understand why an answer is true, not merely
produce a plausible final expression. Preserve that standard in prompts,
tools, examples, tests, and documentation.

## Where the rest of this lives

This file is the working agreement: the rules to follow and the checks to run.
The design rationale behind them — every threshold that a live run has already
met, and what it cost — is one level down, so that a rule stays readable and the
evidence for it stays available.

- [`docs/roles.md`](docs/roles.md) — the twenty-two roles, the source adapters,
  the two recall paths, and which workspace files reach which role's prompt.
- [`docs/solution-loop.md`](docs/solution-loop.md) — the attempt/evaluate graph,
  the two child workflows, and how a tool or provider failure is absorbed.
- [`docs/routing.md`](docs/routing.md) — which role answers which question, what
  each verdict routes to, and the live run behind every threshold.
- [`docs/runtime.md`](docs/runtime.md) — the crate layout, `RunBudget`, and the
  tracing that makes a run legible.
- [`docs/workspace.md`](docs/workspace.md) — where a written file goes, the
  research tree, the scratch, and checkpointing.
- [`docs/ledgers.md`](docs/ledgers.md) — the nine derived ledgers: what each
  holds, and the failure each was written to stop.
- [`docs/schools.md`](docs/schools.md) — why several mathematicians run on one
  problem, what each school is a bet on, and the locking that made it safe.

Two pairs read a mathematician's method against this runtime and say what to
build next. They are why several of the rules above exist, so a change to a
control should start from the argument that produced it:

- [`docs/tao-gap-analysis.md`](docs/tao-gap-analysis.md) and
  [`docs/tao-proposals.md`](docs/tao-proposals.md) — Terence Tao's method set
  against the runtime, and the ranked list five built controls came out of.
  Research in [`research/tao/`](research/tao/).
- [`docs/methods-gap-analysis.md`](docs/methods-gap-analysis.md) and
  [`docs/methods-proposals.md`](docs/methods-proposals.md) — ten more
  mathematicians, chosen so the set spans the method space rather than one
  corner of it, and read for where they *disagree* with Tao and with each other.
  Research in [`research/mathematicians/`](research/mathematicians/), whose
  `11-harness-inventory.md` is the current capability map and supersedes
  `research/tao/03-harness-inventory.md`.

Keep them consistent with the code. A rule here that the code does not enforce
is the failure this repository keeps recording: a prompt instruction is not a
control, and neither is a document.

## Research gating

`MATH_AGENT_RESEARCH=off`, or the `--no-research` flag on `./agent` and
`./euler`, withholds `exa_search` and `oeis_lookup`, so a self-contained
problem tests the runtime's reasoning rather than its ability to look an answer
up. It is enforced by not registering the tool, not by asking the model to
abstain: a prompt instruction is not a control. The workspace note tools stay
available, so the agent can still record and recall its own findings.

## Schools

A *school* is one way of attacking a problem, and two or three run concurrently
on one workspace. `chisel` — attack where it stands, compute first — is the
runtime as it has always been, and is both the default and the control:
`MATH_AGENT_SCHOOLS` unset means `chisel` alone, and its overlay is the empty
string so its prompts stay byte-identical to what preceded schools.
`rising-sea` enlarges the setting instead of attacking the goal; `adversarial`
refutes a statement before spending an attempt proving it.

```sh
./euler 1006 --schools chisel,rising-sea,adversarial
```

A school is four things and must stay four: a method-policy overlay layered
*after* the shared policy, optional per-role overlays, a bench, and its
`Thresholds`. Not a second loop, graph, workspace, or set of roles — those are
shared, because the point is several mathematicians in one workspace rather than
several runtimes in one container. Four rules hold:

- **The control does not move.** Anything changing what `chisel` sends changes
  the baseline every other school is measured against; the tests assert
  byte-identity rather than trusting it.
- **Thresholds are a struct, not a second set of constants.** `route` and the
  jq the engine runs both read one `Thresholds`, and `orchestrator::parity`
  proves they agree for *every* school, exhaustively. No school may move
  `blocked`: a provider failure is not a methodological question.
- **A board post is asserted, never established.** `teams/BOARD.md` is derived
  from an append-only queue and is never an input to a derived ledger. The
  posting school is baked into the tool at registration rather than being an
  argument, so none can post as another.
- **A lock is taken at a tool-call boundary and never below one.**
  `src/orchestrator/worklock.rs` serialises the write cascade and the git
  checkpoint; `tokio::sync::Mutex` is not reentrant, so a lock at the leaf would
  stop the run.

Rationale and the mathematicians behind each school:
[`docs/schools.md`](docs/schools.md).

## Running and watching a run

Starting a run and watching one are separate commands on purpose.

```sh
./euler 763                     # start or continue problem 763
./euler 763 --no-research       # the same, with web search withheld
./euler-tui 763                 # watch it, a tab per team
./euler-tui 763 --replay        # read the last run's log; touch nothing
./euler-tui 763 --plain         # no tabs, stream to stdout, as when scripting
```

A Project Euler problem has one number as its answer and a ceiling on how long
it can reasonably take. An open conjecture has neither, so it gets its own
launcher and its own task shape — build the library, extract what is known,
build the oracle, then loop — and the workspace rather than a number is its
identity:

```sh
./conjecture erdos-gyarfas      # start or continue workspace/conjectures/erdos-gyarfas
./euler-tui --workspace conjectures/erdos-gyarfas
```

`./conjecture <slug>` requires `workspace/conjectures/<slug>/problem.md` to
exist and reads `GOAL.md` beside it. The statement, what counts as a result,
and the leads into the literature are the workspace's, not the script's: a
launcher that carried the mathematics would need editing for every problem.

`./euler-tui` **cannot start, stop, or restart anything**. That is the design,
not a gap: when starting was part of the same command, opening a second view
started a second run on the same workspace — both writing the same files and
both making checkpoint commits over each other. That happened three times in one
evening, twice unnoticed for minutes. A viewer that cannot launch cannot do it,
and one start command means "is something already running for this problem" has
a single answer rather than one per terminal.

It *can* direct a run that already exists, which narrows that rule without
touching what the rule prevents — a directive appends a line to a file and
creates no container.

```sh
./steer 763 check the n=14 bound against a sieve   # or press i in ./euler-tui
./steer --workspace conjectures/erdos-gyarfas "stop enumerating and prove it"
```

Direction never blocks the run. It is queued in the workspace and picked up at
the next boundary, so a directive reaches the work in seconds to minutes rather
than immediately, and the run keeps going whether or not anyone is watching.
What became of one is written to that workspace's `config/DIRECTIVES.md`; the
queue itself is `config/directives.jsonl`, appended to by the host and never by
the run. See [`docs/solution-loop.md`](docs/solution-loop.md#direction-from-a-human)
for what a directive reaches and what it deliberately cannot.

A directive is asserted, not established. It is routed into the next attempt as
an instruction and must never be filed as a claim — the `director` role that
acts on one is not given `research/CLAIMS.md` for exactly that reason.

Start a run detached so it outlives the terminal, then watch it:

```sh
nohup ./euler 763 > workspace/project-euler/763/config/start.log 2>&1 &
```

`start.log` holds the image build and the statement fetch, which happen before
any container exists and are therefore the only place a failed start says why.
Everything after that is the container's, readable with `docker logs` or
`./euler-tui`.

Before starting anything, check nothing is already running for that workspace:

```sh
docker ps --format '{{.Names}}' | grep riemann-agent-run
docker inspect <name> --format '{{range .Mounts}}{{.Source}}{{"\n"}}{{end}}' | grep project-euler
```

Two containers on one workspace is the failure to look for, and it is silent:
both runs work, both write, and the damage shows up later as a checkpoint
history that interleaves two investigations. Stop a run with
`docker rm -f <name>`; the workspace survives and the next `./euler` on it
continues from what is on disk.

The runtime's console arrives on the container's **stderr**, not its stdout —
a live container had 643 lines there and none on stdout — so `docker logs`
needs `2>&1` and any follower must read both streams.

## Docker and workspace rules

The orchestrator must run through `./agent`, which starts the runtime and Qdrant
through Docker Compose. Do not add a host-side fallback for tool execution.

The Docker boundary is part of the security model:

- Run as an unprivileged user.
- Drop all Linux capabilities and keep `no-new-privileges` enabled.
- Keep the root filesystem read-only.
- Do not mount the repository, home directory, Docker socket, or broad host
  paths into the runtime.
- Mount only the selected directory below `workspace/` at `/workspace` for
  agent-written files.
- Keep process, memory, command-time, and command-output limits. Keeping a
  limit is the requirement; the value is a judgement, and 2 GiB was the wrong
  one. A live Erdős–Gyárfás container was OOM-killed mid-attempt — `oom` then
  `die exit=137` in `docker events` — and an OOM kill is the worst failure shape
  available here: the kernel stops the process, so nothing is written to the
  console, the run simply ceases to appear, and everything in flight is lost.
  Read `docker events --filter event=oom` when a container vanishes without an
  error. The cap covers the Rust runtime, every concurrent child run, and every
  Python subprocess they spawn between them, against work that is graph
  enumeration and BFS over millions of states; problem 763 had already recorded
  the old cap in its own `MEMORY.md` as a mathematical ceiling, "exact BFS stops
  at N=14", which is a sandbox limit masquerading as a result.
- Keep network access because provider, search, and telemetry calls need it.

Every agent working directory is `/workspace`. The helper accepts
`--workspace <relative-subfolder>` or `MATH_AGENT_WORKSPACE` and must reject
absolute paths, traversal, and symlinks that resolve outside the repository's
`workspace/` root. File tools must accept relative paths, reject traversal and
absolute paths, and verify canonical parents before writing. Command tools run
with `/workspace` as their current directory. A prompt instruction is not a
security control; enforce boundaries in code and Docker configuration.

Workspace contents are committed. The derivation, the program, and the per-run
notes are the record of how an answer was reached, which is the point of the
product, so they belong in history rather than only on the machine that produced
them.

They belong in history, not in every commit. A live run writes into `workspace/`
continuously, so a host-side auto-commit hook firing on each tool call turns
that into commit spam: one measured hour produced 97 commits on `main`, 87 of
them touching nothing but `workspace/`, with model-written subjects that did not
always match their diffs — one read `remove outdated project euler problem 763
files` for a change that removed nothing and added five lines to a prompt.
`.claude/settings.json` therefore sets `AUTO_COMMIT_EVERY=25` for this
repository. Everything is still committed and nothing is excluded; it is
batched. The fine-grained record is not lost either, because the runtime keeps
its own per-write checkpoint in each workspace's `.workspace-history`, which is
what `WorkspaceCheckpoint` is for. Do not add a generated artifact to a source directory; leave it in its
workspace.

What is ignored is what a reader would never open: `.python-packages/` (pip
installs, which land in the workspace only because the container root filesystem
is read-only), bytecode caches, `raw/`, the bulky enumeration pools beside the
counts that cite them, `trace.jsonl` and `console.log`, and the hidden
`config/.*.json` state. The trace is several megabytes per run and the
derivation and notes already carry the reasoning worth keeping; read it locally
or in Langfuse instead. The hidden JSON is the runtime's own cache of the
frontier, the request ledger, and the document index, rewritten on nearly every
tool call — each already has a committed human-readable counterpart beside it,
`research/FRONTIER.md` and `research/REQUESTS.md`, which is what the derivation
cites. Everything a reader would open stays committed.

## Secrets

`.env` is local and ignored by Git. Never read, print, log, commit, or paste its
contents. Document variable names and placeholders in `.env.example`.

The runtime currently expects:

- `OPENROUTER_API_KEY`
- optional `OPENROUTER_MODEL`
- `EXA_API_KEY`
- `LANGFUSE_BASE_URL`
- `LANGFUSE_PUBLIC_KEY`
- `LANGFUSE_SECRET_KEY`
- `QDRANT_URL`, normally supplied by Compose

Compose loads the trusted local `.env` and passes configuration to the agent.
Do not put secret values directly in Docker command arguments.

## Build and test contract

Run these commands from the repository root before reporting code complete:

```sh
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo build --all-targets --all-features
cargo test --all-features
```

Also run the checks that match the changed surface:

```sh
RUSTDOCFLAGS="-D warnings" cargo doc --no-deps --all-features
sh -n agent euler steer langfuse-turns langfuse-review scripts/run-agent \
  scripts/solve-euler scripts/langfuse-turns scripts/langfuse-review
./agent build
docker compose config --quiet
```

Use a live `./agent` smoke test when changing provider setup, delegation,
research, tool execution, environment forwarding, or Docker behavior. Live
tests spend provider credits, so keep the prompt focused. Never put live network
tests in the deterministic unit-test suite.

Use `./euler <number>` for Project Euler smoke tests. Keep fetched statements
and generated solutions under `workspace/project-euler/<number>`. The wrapper
must fetch the official statement, reject invalid problem numbers, and avoid
prompts that ask agents to find published answers.

Do not ignore or delete a failing test to make CI pass. Fix the cause or report
the blocker with the failing output.

## Rust conventions

Use Rust 2024 and standard `rustfmt` output. The minimum supported Rust version
is 1.96.

- Use `snake_case` for modules, functions, fields, and locals.
- Use `PascalCase` for types and traits.
- Use `SCREAMING_SNAKE_CASE` for constants.
- Keep public exports in `src/lib.rs`.
- Default to private APIs and expose only what callers need.
- Put substantial types in `types.rs` when a module grows large.
- Put module tests in `src/<module>/test.rs`, wired with `mod test`.
- Do not create general `utils.rs` or `helpers.rs` dumping grounds.
- Do not use `unsafe`; the crate forbids it.

Public items need rustdoc. Public fallible functions need an `# Errors` section,
and public functions that can panic need `# Panics`.

Library code must not use `unwrap()`, `expect()`, `panic!()`, `todo!()`, or
`unimplemented!()`. Tests and examples may use `expect()` only when the message
states the invariant.

Use the crate-wide error type for application errors. Add a specific variant
when callers need to distinguish the failure. Keep error messages lowercase
and omit trailing punctuation.

## Tools and research changes

Tools are authority boundaries. Give each specialist only the tools it needs.
The research agent and the librarian get the ways onto the web — search,
similarity, contents, deep research, and the two structured adapters — and
every one is withheld under `MATH_AGENT_RESEARCH` by not being registered. The
tool-builder gets workspace file and command tools. The orchestrator gets
specialist delegation tools, not direct shell access. Recall is granted broadly
rather than narrowly, and the argument for it is the same one: reading what the
run already established is how a role avoids re-establishing it. See
[*Recall: the two ways back into what is known*](docs/roles.md#recall-the-two-ways-back-into-what-is-known)
for who is excluded and why.

For a new tool:

- define a narrow JSON schema with required fields and no extra properties;
- validate every argument before side effects;
- bound network responses, command duration, and output size;
- return enough context for the model to verify what happened;
- test successful behavior and rejection paths;
- update the specialist prompt and registry metadata.

Prefer primary sources for mathematical definitions and results: original
papers, official documentation, standards, and maintained institutional
references. Search output is evidence to inspect, not text to copy blindly.
Keep URLs in the research result so the orchestrator can cite them.

## Dependencies and vendored code

Check the standard library and existing dependencies before adding a crate. For
new dependencies:

- use a caret-compatible version, not an exact pin;
- disable default features when that meaningfully reduces the graph;
- enable only required features;
- add a comment in `Cargo.toml` explaining the dependency;
- keep `Cargo.lock` committed.

Two crates are vendored as Git submodules. Initialize both with:

```sh
git submodule update --init --recursive
```

- `vendor/tinyagents` — the harness that runs one agent turn: the model
  providers, the tool runtime, middleware, and steering.
- `vendor/tinyflows` — the state-graph runtime every control-flow graph in this
  crate is built on, reached through `agent::flow`. It is the same runtime that
  used to be consumed from TinyAgents, extracted into TinyFlows and maintained
  there.

The split is the rule to keep: TinyAgents runs a turn, TinyFlows decides which
turn runs next. A new graph is built with `agent::flow`, never with
`tinyagents::graph`, and the two error types are converted only by
`agent::flow::into_graph` / `from_graph`.

TinyFlows has two layers and this crate now uses both, for different things.

The solution loop **runs on the declarative workflow engine**. The engine owns
the routing — the `loop` head with the run's state as its accumulator, and the
ladders as `switch` nodes carrying jq — and each step is a `tool_call` into the
Rust that was written against live runs. That split is the point: the control
flow is a document an outside agent can read and patch, and the steps that
drain a directive, salvage a timed-out attempt, and open the arms beside the
loop are not reimplemented in JSON.

`agent::flow` is the lower-level state-graph runtime. It still drives each
detached sub-agent's own single-node graph. The state-graph solution loop is
gone; the workflow engine is the only path, and it has not yet run an hour of
live mathematics.

The loop calls two child workflows. `orchestrator::workflow_research` runs once
before the first attempt — establish what the workspace has, then go looking for
what it does not — and `orchestrator::workflow_goals` decides, on a cadence,
whether to decompose the goal. Each is a child rather than more nodes in the
loop because its policy is its own: a run-once stage put inside a graph whose
whole subject is repetition is how it ends up repeated, and "how often is the
goal decomposed" is a decision an operator should change without a rebuild.

Everything after an attempt is a **fan-out**, not a chain. Judge, reflect,
patterns, invention and the goal decomposition read the same attempt and none
reads another, so they run concurrently and converge on one merge. Three of them
used to be `tokio::spawn`s hidden inside `reflect_step`'s body, which meant the
graph could not draw them, graph policy could not bound them, and no checkpoint
could land between them. The merge folds counters by delta rather than by
picking a winner, because a reset and an increment on the same counter both
happen and both have to survive.

Five rules hold across both:

- Derive, never restate. The workflow role registry is read off `AgentRegistry`,
  the routing ladder's thresholds are generated from the Rust constants, and
  `parse_reflection` calls `record_verdict` rather than reimplementing it. A
  second list is a second answer to a question about authority, about a
  threshold that cost a live run to learn, or about what ends a run.
- Execution and outbound HTTP are refused from a workflow. See
  `orchestrator::caps::execution` and `::network` — running a command means
  declaring a complexity class first, and reaching the network means going
  through a tool that bounds the response and that research gating can withhold.
- The parity harness is not optional. `route` and `judged_route` are no longer
  what a run executes; they are the executable specification of the routing
  policy, and `orchestrator::parity` proves the jq the engine runs agrees with
  them. It is exhaustive rather than sampled so an off-by-one cannot slip
  through. Any change to either side must keep it green.
- The body has one exit. Every path back to the loop head goes through `pass`,
  because the engine's `nodes` map is cumulative and a fold with more than one
  node to read will eventually read a stale one. A restart goes through it too:
  re-entering `attempt` directly would undo the judge's own `restarts`
  increment, so the cap that bounds restarts would never trip.
- Every step reads the step before it, never the accumulator. The head folds at
  the *top* of a pass, so for the whole of a pass `nodes.solve.state` is what the
  *previous* one ended with. Only `attempt` reads it, because only `attempt` runs
  there. This class of bug is invisible to a constant mock — pass N−1 and pass N
  look identical — so a test that varies its answers per call is the only kind
  that catches it.

Do not edit vendored code through the parent repository. Make TinyAgents or
TinyFlows changes upstream, push them there, then update this repository's
gitlink in a separate commit.

Never export `CARGO_TARGET_DIR` or send build output to a temporary directory.
Use the checkout's normal target configuration.

## Git workflow

- Work in the current checkout. Do not create or use Git worktrees.
- Do not create feature branches.
- Commit directly to `main` and push `main` to its configured remote.
- Never force-push, rewrite published history, or bypass hooks.
- Keep commits focused, with concise imperative subjects.
- Preserve unrelated user changes in a dirty working tree.

An auto-commit hook may checkpoint edits while work is in progress. Those
commits are expected. Do not reset or rewrite them. Commit manually only when a
specific boundary matters.

## Documentation rules

Keep `README.md`, this file, rustdoc, examples, and runtime behavior consistent.
Write for a reader who has not seen the code. Prefer a concrete command or
example over broad claims.

Keep this file at 500 lines or fewer. It was 1,734 lines for long enough that
the rule read as advice: `CLAUDE.md` symlinks here, so every session and every
review paid for a hundred kilobytes to find one rule, and nothing measured what
that cost. That is what makes length a cost here rather than a preference — this
file is loaded in full, every time, by a reader looking for one thing.

`README.md` is read start to finish by someone new, so it is held to the same
intent without the number: it is 641 lines today, which is too long, and the fix
is to move what a user does not need on their first pass rather than to trim
paragraphs down to a threshold.

**`docs/` is not held to that cap.** Nothing loads those files into a prompt and
nobody reads one end to end; a reader arrives at `docs/ledgers.md` because a rule
above it sent them there, reads the section that explains that rule, and leaves.
For a file read by section, splitting on a line count is not a saving — it moves
the cost from scrolling to deciding which of two files a subject ended up in, and
it splits an argument at the point a number happened to fall rather than at a
seam. The cap was applied there once and produced exactly that: `docs/roles.md`
held at 499 lines by trimming an argument rather than by having finished it.

The split is by *kind*, not by size. A rule to follow and a check to run stay
here. The evidence behind a rule — the live run that met a ceiling, the number
that turned out to be wrong, the failure a control was written to stop — goes to
the file in `docs/` that owns that subject, listed under *Where the rest of this
lives*. User-facing instructions stay in `README.md`. Do not grow a third tree
beside those two: `docs/` holds the rationale for what is in this file, and a
document with no rule above it is a document nobody has a reason to open.

A `docs/` file still earns its length. Split one when it has stopped being about
one subject — which is a judgement about what a reader came for, not a line
count.

## Working agreement for coding agents

1. Inspect the surrounding code before editing and match its conventions.
2. Execute a clear task directly. Do not stop for a plan when the next step is
   obvious.
3. Stay within scope. Raise unrelated problems instead of folding them into the
   change.
4. Deliver finished code without placeholders or commented-out alternatives.
5. Preserve security checks, tests, lints, and Docker restrictions.
6. Report commands actually run and their real outcomes.
7. Ask only when an irreversible choice or genuine product fork blocks work.
