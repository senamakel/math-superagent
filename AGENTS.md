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

- [`docs/roles.md`](docs/roles.md) — the roles, the source adapters, the two
  recall paths, and which workspace files reach which role's prompt.
- [`docs/solution-loop.md`](docs/solution-loop.md) — the attempt/evaluate graph,
  the two child workflows, and how a tool or provider failure is absorbed.
- [`docs/routing.md`](docs/routing.md) — which role answers which question, what
  each verdict routes to, and the live run behind every threshold.
- [`docs/runtime.md`](docs/runtime.md) — the crate layout, `RunBudget`, and the
  tracing that makes a run legible.
- [`docs/workspace.md`](docs/workspace.md) — where a written file goes, the
  research tree, the scratch, checkpointing, and reading what does not fit.
- [`docs/ledgers.md`](docs/ledgers.md) — the derived ledgers: what each holds,
  the failure each stops, what bounds them, and how a run declares one.
- [`docs/lean-library.md`](docs/lean-library.md) — writing the mathematics as
  Lean rather than prose, the `Cited` namespace, and the first replay's numbers.
- [`docs/memory.md`](docs/memory.md) — the four memory stores, and their audit.
- [`docs/schools.md`](docs/schools.md) — why several mathematicians run one
  problem, each school's bet, and the locking that made it safe.
- [`docs/calibration.md`](docs/calibration.md) — the solved conjectures the
  harness is measured against, the two-layer evidence screen, and what round 1
  measured.

Two pairs read a mathematician's method against this runtime and say what to
build next. They are why several of the rules above exist, so a change to a
control should start from the argument that produced it:

- [`docs/tao-gap-analysis.md`](docs/tao-gap-analysis.md) and
  [`docs/tao-proposals.md`](docs/tao-proposals.md) — Terence Tao's method set
  against the runtime, and the ranked list five built controls came out of.
  Research in [`research/tao/`](research/tao/).
- [`docs/methods-gap-analysis.md`](docs/methods-gap-analysis.md) and
  [`docs/methods-proposals.md`](docs/methods-proposals.md) — ten more
  mathematicians spanning the method space, read for where they *disagree* with
  Tao and each other. Research in
  [`research/mathematicians/`](research/mathematicians/), whose
  `11-harness-inventory.md` is the current capability map.

Keep them consistent with the code. A rule here that the code does not enforce
is the failure this repository keeps recording: a prompt instruction is not a
control, and neither is a document.

## Gating

A withheld tool is withheld by **not registering it**, never by asking the model
to abstain. `MATH_AGENT_RESEARCH=off` / `--no-research` drops `exa_search` and
`oeis_lookup`, so a problem tests reasoning, not lookup. `MATH_AGENT_RLM=off` /
`--no-rlm` drops `map_document`, the chunked whole-document read, as a *spend* —
one call per chunk. Its ceiling is not: above it `read_document` returns an
outline, and `section`, `lines` and `grep_workspace` reach any part.

## Ledgers

A *ledger* is derived state — an append-only queue, or one file per entry —
walked by code and rendered into Markdown. `TASKS.md`, the board, the sub-goals,
the attempts and the ten in [`docs/ledgers.md`](docs/ledgers.md) are this shape.

- **No agent writes one; the write path refuses a derived file.** Editing one is
  work queued for deletion on the next derivation, not a change.
- **Every section caps rows, truncates prose, and says what it left out** — a cut
  list reading as complete is worse than a long one. `ledger/ceiling_test.rs`
  asserts it, and that past the bound more entries do not mean more file.
- **A prompt carries the *index*, not the ledger**: one line per entry, its
  identity and status, ending in the `read_ledger` call that fetches the rest. A
  role told less must be told where the rest is, or it is cheaper *and dumber*.
  `ledger::fit` clamps what is left, and is only a backstop.
- **One write operation:** an event names an entry and merges fields; closing
  keeps the entry with its reason rather than deleting it.
- **A declaration cannot raise a bound, shadow a built-in, or reach a prompt.**
  The tool schema is fixed for a run, so `ledger` is a checked string and never
  an enum, which lets a run define an axis and use it the same turn.
- **Rendered into `derived/`, which the file tools refuse.** The folder name is
  the invariant: nothing in it is hand-written. It stays committed — it is the
  record of what was established — but `read_document` and `grep_workspace`
  refuse it and name `read_ledger`, which bounds and selects by `id`, `status` or
  `query`. Older workspaces migrate once at startup, never overwriting.

- **Lean carries the mathematics, not only the check.** Statements go under
  `code/lean/Lib/`; `derived/LEMMAS.md` derives from them. A result read from the
  literature is an `axiom` under `namespace Cited` and earns `conditional`, never
  `formalised` — and never by typing it, the status being read off the verdict.
  Only `lean_check` writes `code/out/lean/`, which is why `lean-verdict` cannot,
  being in the image and so reachable from `execute_command`. `./lean-check` and
  `scripts/lean-replay --all` reach the kernel without a run.
  [`docs/lean-library.md`](docs/lean-library.md).

## Candidates

Several candidate solutions run at once, each on its own branch and checkout:
`spawn_candidates` starts them, `attempt_diff` reads them back, `archivist` keeps
one.

- **Fork the files, share the memory.** A candidate's checkout is a linked
  worktree, so `code/`, `research/` and its ledgers are its own; memory is not
  re-rooted and must not be, being the only channel between them. Enforced for
  the file tools only — a shell cannot be confined by its cwd.
  [`docs/workspace.md`](docs/workspace.md).
- **One role may make a candidate authoritative.** `adopt_attempt` and
  `abandon_attempt` are the archivist's alone, and it holds no shell and no file
  write — so every trunk change carries a branch and a recorded reason.
- **Adoption copies named files, and is not a merge** — a merge would also take
  the losing candidate's account of why it was right.
- **There is no general git tool** — every operation is a named verb with checked
  arguments; one taking a command line is `execute_command` by another name.

## Schools

A *school* is one way of attacking a problem; two or three run concurrently on
one workspace, sharing the ledgers and a board. Each one's bet:
[`docs/schools.md`](docs/schools.md). Not a second loop, graph, or set of roles.

- **Four things, and it must stay four:** a method-policy overlay layered *after*
  the shared policy, per-role overlays, a bench, its `Thresholds`.
- **The control does not move.** `chisel` is today's runtime, is what an unset
  `MATH_AGENT_SCHOOLS` selects, and has an empty overlay — asserted, not assumed.
- **Thresholds are a struct, not a second set of constants.** `route` and the jq
  both read one; `orchestrator::parity` proves they agree for every school, and
  none may move `blocked`.
- **A board post is asserted, never established.** `teams/BOARD.md` never feeds
  a ledger, and the posting school is baked into the tool.
- **A lock is taken at a tool-call boundary, never below one.** `worklock.rs`
  serialises the write cascade and the checkpoint; the mutex is not reentrant.

## Running and watching a run

Starting a run and watching one are separate commands on purpose.

```sh
./euler 763                     # start or continue problem 763
./euler 763 --no-research       # the same, with web search withheld
./euler 763 --schools chisel,rising-sea   # two schools, one workspace
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

`./euler-tui` **cannot start, stop, or restart anything** — the design, not a
gap: [`docs/runtime.md`](docs/runtime.md#one-start-command) has the evening that
settled it. A viewer that cannot launch cannot start a second run on a
workspace that already has one.

It *can* direct a run that already exists, which narrows that rule without
touching what the rule prevents — a directive appends a line to a file and
creates no container.

```sh
./steer 763 check the n=14 bound against a sieve   # or press i in ./euler-tui
./steer --workspace conjectures/erdos-gyarfas "stop enumerating and prove it"
```

Direction never blocks the run: it is queued in `config/directives.jsonl` —
appended to by the host, never by the run — and picked up at the next boundary,
so it reaches the work in seconds to minutes whether or not anyone is watching.
What became of one goes to `config/DIRECTIVES.md`.

A directive is asserted, not established. It is routed into the next attempt as
an instruction and must never be filed as a claim — which is why the `director`
role acting on one is not given `derived/CLAIMS.md`.
[`docs/solution-loop.md`](docs/solution-loop.md#direction-from-a-human) has what
a directive reaches and what it deliberately cannot.

Start a run detached so it outlives the terminal, then watch it:

```sh
nohup ./euler 763 > workspace/project-euler/763/config/start.log 2>&1 &
```

Two containers on one workspace is the failure to look for, and it is silent —
both runs write, and the damage appears later as an interleaved history. Check
before starting, and **match by mount, not by name**. Stop one with
`docker rm -f <name>`; the workspace survives and the next `./euler` continues.
`start.log` is the only place a failed *start* says why, and the runtime's
console is on the container's **stderr**, so `docker logs` needs `2>&1`.
[`docs/runtime.md`](docs/runtime.md#watching-a-run) has the commands and the
runs behind each of these. Every checkout shares the `math-agent:local` tag, so
a build in one replaces the image another is about to run.

## Calibration runs

An open conjecture gives a run no known destination, so nothing separates a
harness closing in on a proof from one producing plausible activity, and every
architecture change is made blind. A **calibration run** supplies the reference:
a conjecture already solved, stated as open, its answer withheld in code.

```sh
./calibrate unit-distance-plane-chromatic     # start or continue
scripts/eval-report unit-distance-plane-chromatic
```

Watch it with `./diagnose` / `./euler-tui --workspace conjectures/<slug>`.
[`docs/calibration.md`](docs/calibration.md) holds why each rule below exists.

- **The answer key never enters the container.** `GROUND_TRUTH.md`, `RUBRIC.md`
  and the plaintext `screen.terms` live under `evals/<slug>/`, outside the only
  bind-mounted tree. `./calibrate` refuses to start if one is inside the mount.
- **The compiled blocklist is hashed.** `execute_command` reads any file the
  runtime can, so plaintext terms would hand the run the names they withhold.
  The ledger records decisions and never terms.
- **Two layers are controls, the third is not.** The proxy decides which hosts
  are reachable, closing `execute_command`; `orchestrator::screen` sees
  plaintext and decides whether an allowed source reveals the answer. The
  leakage audit catches recall, which no control can stop.
- **`MATH_AGENT_SCREEN` absent means no screen**, so an ordinary run is
  untouched. Named but unreadable is a hard startup failure: an unscreened
  calibration run looks entirely normal and measures nothing.
- **A seed is a time capsule, not a puzzle**, stating the art as of the year
  before the solution — obstruction and leads included. Where it hints
  substantially, `GROUND_TRUTH.md` records how much so a score can discount it.
- **`chisel` is in every school set**, enforced by the launcher: an alternative
  school is evidence only when today's runtime ran beside it. Which schools
  attack a problem is `evals/<slug>/schools`, because that pairing is an
  argument about method and belongs beside the statement it is about.
- Do not add a problem without a `GROUND_TRUTH.md` recording its de-naming
  strength, and a `RUBRIC.md` whose milestones require an artifact, not a claim.

## Docker and workspace rules

The orchestrator must run through `./agent`, which starts the runtime and Qdrant
through Docker Compose. Do not add a host-side fallback for tool execution. The
Docker boundary is part of the security model:

- Run as an unprivileged user, with the root filesystem read-only, all Linux
  capabilities dropped, and `no-new-privileges` enabled.
- Mount only the selected directory below `workspace/` at `/workspace`; never
  the repository, home directory, Docker socket, or broad host paths.
- Keep process, memory, command-time, and command-output limits. Keeping a
  limit is the requirement, its value a judgement —
  [`docs/runtime.md`](docs/runtime.md#the-memory-cap). Read
  `docker events --filter event=oom` when a container vanishes.
- Keep network access because provider, search, and telemetry calls need it.

Every agent working directory is `/workspace`. The helper accepts
`--workspace <relative-subfolder>` or `MATH_AGENT_WORKSPACE` and must reject
absolute paths, traversal, and symlinks that resolve outside the repository's
`workspace/` root. File tools must accept relative paths, reject traversal and
absolute paths, and verify canonical parents before writing. Command tools run
with `/workspace` as their current directory. A prompt instruction is not a
security control; enforce boundaries in code and Docker configuration.

Workspace contents are committed: the derivation, the program and the per-run
notes are the record of how an answer was reached, which is the point of the
product. They belong in history, not in every commit — `.claude/settings.json`
sets `AUTO_COMMIT_EVERY=25` here, and the fine-grained record survives in each
workspace's `.workspace-history`. Do not add a generated artifact to a source
directory.

What is ignored is only what a reader would never open — bytecode, `raw/`, the
bulky enumeration pools, the event logs, the hidden `config/.*.json` caches —
each with a committed readable counterpart beside it, such as
`derived/FRONTIER.md`. Everything a reader would open stays committed.
[`docs/workspace.md`](docs/workspace.md) has the list and the measured hour of
commit spam that set the batch size.

## Secrets

`.env` is local and ignored by Git. Never read, print, log, commit, or paste its
contents. Document variable names and placeholders in `.env.example`.

The runtime currently expects:

- `OPENROUTER_API_KEY`, and optional `OPENROUTER_MODEL`
- `OPENROUTER_MEMORY_API_KEY`, the memory's own; unset shares the run's limit
- `EXA_API_KEY`
- `LANGFUSE_BASE_URL`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`
- `QDRANT_URL`, normally supplied by Compose

The launchers export `.env` over the shell (`scripts/dotenv`), because Compose
prefers the environment to the file and a stale exported key silently outranked
this checkout's for a day. Never put a secret in a Docker command argument.

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

Use a live `./agent` or `./euler <number>` smoke test when changing provider
setup, delegation, research, tool execution, environment forwarding, or Docker
behavior. Live tests spend provider credits, so keep the prompt focused, and
never put a network test in the deterministic suite. The `./euler` wrapper must
fetch the official statement, reject invalid problem numbers, and never prompt
an agent to look a published answer up.

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

Two crates are vendored as Git submodules — `vendor/tinyagents`, the harness
that runs one agent turn, and `vendor/tinyflows`, the state-graph runtime every
control-flow graph is built on, reached through `agent::flow`. Initialize both:

```sh
git submodule update --init --recursive
```

The split is the rule to keep: TinyAgents runs a turn, TinyFlows decides which
turn runs next. A new graph is built with `agent::flow`, never with
`tinyagents::graph`, and the two error types are converted only by
`agent::flow::into_graph` / `from_graph`.

TinyFlows has two layers and this crate uses both: the solution loop runs on the
declarative **workflow engine**, and `agent::flow` drives each detached
sub-agent's single-node graph. [`docs/solution-loop.md`](docs/solution-loop.md)
has the graph, the fan-out and the two child workflows. Five rules hold across
both layers and must not be broken:

- **Derive, never restate.** The workflow role registry is read off
  `AgentRegistry`, the ladder's thresholds are generated from the Rust
  constants, and `parse_reflection` calls `record_verdict`. A second list is a
  second answer to a question about authority or about what ends a run.
- **Execution and outbound HTTP are refused from a workflow** — see
  `orchestrator::caps::execution` and `::network`.
- **The parity harness is not optional.** `route` and `judged_route` are the
  executable specification of the routing policy; `orchestrator::parity` proves
  exhaustively that the jq the engine runs agrees with them, for every school.
- **The body has one exit.** Every path back to the loop head goes through
  `pass`, including a restart — re-entering `attempt` directly would undo the
  judge's own `restarts` increment, so the cap would never trip.
- **Every step reads the step before it, never the accumulator.** The head folds
  at the *top* of a pass. This bug class is invisible to a constant mock, so
  only a test that varies its answers per call catches it.

Do not edit vendored code through the parent repository. Make TinyAgents or
TinyFlows changes upstream, push them there, then update this repository's
gitlink in a separate commit.

Never export `CARGO_TARGET_DIR` or send build output to a temporary directory.
Use the checkout's normal target configuration.

## Git workflow

- Substantial work gets its own worktree and branch: `worktree <slug>`, then
  work in `./worktrees/<slug>`. Small, obvious changes may go straight onto
  `main`. This rule read "do not create or use Git worktrees" for long enough
  that the checkout already held one nobody had removed — a rule the practice
  contradicts is one that stops being read, so it now says what is done.
- Never force-push, rewrite published history, or bypass hooks.
- Keep commits focused, with concise imperative subjects.
- Preserve unrelated user changes in a dirty working tree.

Two git repositories are in play and they are not the same one. This is the
product repository. Each **workspace** has its own, in `.workspace-history`, and
the runtime is what commits to it — `src/orchestrator/vcs.rs` holds every verb,
`docs/workspace.md` has the shape, and no rule above applies to it.

An auto-commit hook may checkpoint edits while work is in progress. Those
commits are expected. Do not reset or rewrite them. Commit manually only when a
specific boundary matters.

## Documentation rules

Keep `README.md`, this file, rustdoc, examples, and runtime behavior consistent.
Write for a reader who has not seen the code. Prefer a concrete command or
example over broad claims.

Keep this file at 500 lines or fewer. `CLAUDE.md` symlinks here, so it is loaded
in full every time, which is what makes length a cost rather than a preference.
Adding a section means finding the lines for it.

`README.md` is read start to finish by someone new, so it is held to the same
intent without the number: the fix for its length is moving what a user does not
need on a first pass, not trimming to a threshold.

**`docs/` is not held to that cap**, because nothing loads those files into a
prompt and nobody reads one end to end. Splitting one on a line count splits an
argument where a number fell rather than at a seam; split it when it has stopped
being about one subject.

The split is by *kind*, not by size. A rule to follow and a check to run stay
here; the evidence behind a rule — the live run that met a ceiling, the number
that turned out wrong, the failure a control was written to stop — goes to the
`docs/` file that owns that subject, listed under *Where the rest of this
lives*. User-facing instructions stay in `README.md`. Do not grow a third tree:
a document with no rule above it is one nobody has a reason to open.

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
