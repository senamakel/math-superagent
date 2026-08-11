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

## Expected problem-solving behavior

The runtime has seven roles plus an explicit solution loop.

- The orchestrator decomposes a problem, delegates focused tasks, and combines
  the results.
- The goals agent translates an objective into completion criteria and spawns
  specialist subagents until the goal is met or precisely blocked.
- The research agent uses Exa to find definitions, papers, official references,
  or current facts. It returns source URLs, separates evidence from inference,
  and can save reusable notes to Qdrant.
- The tool-builder writes and executes shell or Python tools in `/workspace`.
  It handles numerical checks, counterexample searches, data extraction, and
  other reproducible calculations. It is the only role with shell authority.
- The reflection agent judges one attempt and extracts one lesson. It has no
  research or execution tools on purpose: a judge that can start solving stops
  judging. Its hardest job is refusing to call an unverified answer solved.
- The pattern-recognition agent runs exact sequence analysis over results the
  run already computed. Its tools report only what holds for every term
  supplied, and label the finding a conjecture, because an invented pattern
  costs more than no pattern.
- The inventor proposes a different line of attack when the current one has
  stalled, backed by research. It is told what failed so it does not re-propose
  it.
- The librarian builds a local reference library under `reference/` so the rest
  of the run reads primary material instead of guessing.

## The solution loop

`orchestrator::solutions` is a `TinyAgents` graph, not a prompt:

```text
  attempt ──> reflect ──┬─ solved ────────────────> done
     ▲                  ├─ retry ─────────────────> attempt
     │                  └─ stuck ──> diversify ────┘
     └────────────────────────────────────────────┘
```

Reflection runs after *every* attempt, not only after a failure, because the
lesson from a partial success is what stops the next attempt repeating it.
`diversify` runs the librarian, the pattern agent, and the inventor
concurrently, and only when repeated attempts stop making progress; it is the
step that breaks a loop reflection alone cannot.

Keep the routing policy in `route` a plain function of the state. It is the
part of this design most likely to be wrong and the part a live run is least
able to demonstrate cheaply, so it must stay unit-testable without a provider.
Two rules in it are load-bearing: an unparsable verdict must not count as
solved, and the attempt ceiling must outrank the stuck rule or the loop can
diversify forever.

The loop is the only execution path. Do not add a single-turn mode back: it
differed only in discarding the reflection, and a switch between them is one
more thing to get wrong.

## Failure handling

A recoverable tool failure must never end a run. Tools are registered through
`ResilientTool`, which turns an `Err` into a `ToolResult` carrying the error so
the model can correct itself; `ReflectionMiddleware` then appends advice, and
escalates when the same tool fails repeatedly. Before this existed, a Qdrant
`409`, a `/workspace/`-prefixed path, a `403`, and a non-UTF-8 download each
destroyed an entire run's accumulated work. Do not reintroduce a tool whose
argument or transport failure propagates out of the run.

The runtime image must expose both `python` and `python3`, plus `pip` and
`pip3`. Pip installs belong under `/workspace/.python-packages`; do not make the
container root filesystem writable for package installation.

## Run budget

`RunBudget` in `src/agent/budget.rs` is the single source of truth for what one
agent run may spend, and it applies to the orchestrator and every specialist
alike. The defaults are 250 model calls, 4000 tool calls, a two-hour run
ceiling, and a ten-minute ceiling per tool call. Each is overridable through
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

The run ceiling and the tool ceiling are separate limits and must stay
separate. Collapsing them means a specialist that runs one long computation
dies with it. Whatever the run ceiling is, `await_agent` must be able to wait it
out, or the orchestrator is structurally unable to collect the result of the
deepest work it delegated.

A timeout is a safety ceiling, not permission to run an intractable approach.
Before substantial execution, the tool-builder must state both time and space
complexity. Algorithms with exponential time or space complexity are
prohibited; choose a polynomial or better formulation.

## Research gating

`MATH_AGENT_RESEARCH=off`, or the `--no-research` flag on `./agent` and
`./euler`, withholds `exa_search` from the research agent, so a self-contained
problem tests the runtime's reasoning rather than its ability to look an answer
up. It is enforced by not registering the tool, not by asking the model to
abstain: a prompt instruction is not a control. The workspace note tools stay
available, so the agent can still record and recall its own findings.

## Observability

Every run in the tree carries a `RunTracer` (`src/agent/trace.rs`). It prints an
elapsed-time console line per model call, tool call, and tool result, labelled
with the agent that produced it, and appends every event as JSON to
`trace.jsonl` in the selected workspace. Specialist runs also export their own
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
5. Delegate external fact-finding to `research` and cite the returned sources.
6. Delegate meaningful computation to `tool_builder`. Report the program or
   command and the relevant output.
7. Check edge cases, dimensions, signs, domains, and limiting behavior when
   they apply.
8. Verify by a second, independent route, or say the result is unverified.
9. Distinguish a proof, a numerical check, a heuristic, and a sourced claim.
10. Say when the evidence is incomplete. Never invent a theorem, citation, or
    computation result.

The runtime is not a formal proof assistant. Do not describe sampled evidence or a
floating-point experiment as proof.

## Runtime architecture

The Rust crate vendors TinyAgents and keeps the integration deliberately small.

```text
src/
├── lib.rs              # public exports
├── agent/              # TinyAgents facade, OpenRouter, Langfuse
│   ├── budget.rs       # per-run call, wall-clock, and capture policy
│   ├── reflection.rs   # in-run middleware that reflects on failing tools
│   ├── resilient.rs    # tool-error and request-timeout wrappers
│   └── trace.rs        # live console and trace.jsonl event listener
├── orchestrator/       # registry, specialists, compression, workspace tools
│   ├── async_subagents.rs # graph-backed asynchronous child-run controls
│   ├── documents.rs    # bounded workspace documents and local search index
│   ├── patterns.rs     # exact sequence analysis and recurrence search
│   ├── solutions.rs    # graph-backed attempt/reflect/diversify loop
│   └── vector.rs       # Qdrant tools and deterministic local feature vectors
├── hello_agent/        # minimal single-agent example
├── error/              # crate-wide Error and Result<T>
└── greeting/           # legacy template example
examples/
├── orchestrator.rs     # Docker runtime entry point
└── hello_agent.rs      # direct provider example
vendor/tinyagents/      # pinned upstream TinyAgents checkout
agent                   # user-facing helper
euler                   # Project Euler problem-number wrapper
compose.yaml            # agent and Qdrant services
scripts/run-agent       # Docker Compose implementation
scripts/solve-euler     # official statement fetch and solve workflow
workspace/              # selectable writable agent workspaces
└── template/           # seed instructions, prompts, config, and memory
```

The executable registry contains `goals`, `research`, `tool_builder`,
`reflection`, `pattern_finder`, `inventor`, and `librarian`.
Agents are exposed to the orchestrator as TinyAgents `SubAgentTool` instances.
The goals agent also receives the research and tool-builder delegation tools,
so it can pursue a goal through nested, focused work.
All model-visible delegation uses the graph-backed asynchronous controls:
`spawn_agent`, `peek_agent`, `steer_agent`, and `await_agent`. A spawn returns a
run ID immediately. Callers may launch independent work in parallel, inspect
or redirect live runs, and must await every result needed for their final
answer. Do not reintroduce blocking `SubAgentTool` calls.
The research agent has Exa plus `recall_research` and `remember_research` tools.
Qdrant persists the notes in a named Compose volume. The vector tools use a
small deterministic feature-hashing encoder, not an external embedding model.

The parent and both children use context-compression middleware with an
estimated 300,000-token trigger. The summary should retain mathematical
assumptions, intermediate results, source URLs, tool output, and unfinished
work.

OpenRouter uses `deepseek/deepseek-v4-flash-0731` through StreamLake unless
`OPENROUTER_MODEL` overrides the model. Exa handles search. Langfuse ingestion
is best effort and must not turn a successful answer into a failed run.

Langfuse is also available for querying and reviewing recorded turns. Use
`./langfuse-turns --hours 24 --limit 50` for normalized observations or
`./langfuse-turns --trace <trace-id>` for one trace. Use
`./langfuse-review --hours 24 --limit 100` to retain those turns while flagging
errors, status messages, and missing outputs as improvement candidates. The
helpers load the ignored local `.env`, query Observations API v2, and pass Basic
Auth through curl configuration on standard input so credentials never appear
in process arguments or output. Treat returned inputs and outputs as sensitive.

Do not add memory domains, channels, Web3, SQLite persistence, REPL, or RLM
features unless the user explicitly expands the product scope.

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
- Keep process, memory, command-time, and command-output limits.
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
them. Do not add a generated artifact to a source directory; leave it in its
workspace.

Three things are ignored: `.python-packages/` (pip installs, which land in the
workspace only because the container root filesystem is read-only), bytecode
caches, and `trace.jsonl`. The trace is several megabytes per run and the
derivation and notes already carry the reasoning worth keeping; read it locally
or in Langfuse instead.

## Document conversion

`readable::to_markdown` converts every downloaded document before it is
stored. HTML becomes Markdown, a PDF's text layer is extracted, plain text
passes through, and genuinely binary content returns an error that names the
format and says to find another source.

Two details are deliberate and should not be simplified away:

- The HTML converter is hand-written rather than taken from a crate because
  mathematical sources carry TeX, delimited `\(…\)` or `$…$`, and a
  general-purpose converter escapes the backslashes and destroys it. There is a
  regression test using a real Project Euler statement.
- Magic bytes beat the declared content type. Servers mislabel routinely, and a
  PDF served as `text/html` is still a PDF.

Links are compressed. Anchors become reference-style `[text][n]` with one
`## Links` list at the end, so a URL repeated a dozen times on a page is
written once; tracking parameters (`utm_*`, `fbclid`, and similar) are stripped.
A reference page's navigation targets otherwise fill the context with URLs the
agent will never follow.

The PDF extractor runs inside `catch_unwind` because it panics on malformed
input, and a panic there would destroy work unrelated to the document.

## Research folder

Every downloaded document is filed under `research/`, enforced by
`documents::research_path` rather than requested in a prompt. Downloads are the
one kind of file that arrives from outside the run, and separating them from the
run's own derivations is what lets an agent tell at a glance what it gathered
from what it worked out. A path already inside `research/` is left alone;
anything else is moved into it, with `/workspace/` and `./` prefixes trimmed
first so the common spellings do not produce `research/workspace/...`.

The librarian keeps `research/INDEX.md` current, and receives it as context so
it does not download the same paper twice.

## Workspace discovery and the reflection log

`list_workspace` renders a bounded tree with file sizes. Agents previously knew
only the file names their prompt happened to mention, so work already on disk
went unread; sizes matter because they distinguish a finished derivation from
an empty placeholder. The listing hides `.workspace-history`,
`.python-packages`, `__pycache__`, the document index, and `trace.jsonl`, and
truncates rather than dumping an unbounded tree.

Every reflection is archived to `reflections/<epoch_ms>_<outcome>.md`, where the
outcome is `nothing` or `<n>_learnings`. The name carries the result so a
directory listing alone shows which attempts taught the run something. Writing
the log is best effort: the lesson is already in the loop state, and losing the
archive copy must not cost the run the lesson.

## Workspace context routing

Context is authority, and it is also noise. `role_context` in
`src/orchestrator/mod.rs` decides which working files enter each agent's system
prompt. Only `AGENTS.md`, the method policy, goes to everyone.

| Role | Additional files |
| --- | --- |
| orchestrator, goals | `config.toml`, `goal.md`, `tasks.md`, `memory.md` |
| tool_builder | the above plus `scratchpad.md` |
| reflection | `goal.md`, `tasks.md`, `memory.md` |
| pattern_finder | `goal.md`, `memory.md`, `scratchpad.md` |
| inventor, research | `goal.md`, `memory.md` |
| librarian | `goal.md`, `memory.md`, `research/INDEX.md` |

Three of these are load-bearing rather than tidy-minded:

- Reflection must see `goal.md`. It judges whether the criteria are met, and
  judging against criteria it cannot see is guesswork; a wrong `SOLVED` ends
  the investigation.
- The inventor must see `memory.md` for its failed-approaches section. Without
  it, it re-proposes what already failed, which is the one thing it exists not
  to do.
- Reflection must *not* see `scratchpad.md`. Provisional arithmetic is not
  evidence of progress, and treating it as such keeps the loop retrying.

Adding a file to every role is the easy mistake. Ask what the role has to
decide, and give it only what that decision needs.

## Workspace checkpointing

`checkpoint::WorkspaceCheckpoint` commits the workspace after every successful
write, so a rewritten `solution.py` or an edited belief in `memory.md` is
recoverable instead of lost, and the commit sequence reads as an account of how
the answer was reached.

History lives in `.workspace-history`, not `.git`, with an explicit work tree.
A conventional `.git` would make the product repository treat each workspace as
an embedded repository and refuse to track through it. Only writing tools
trigger a commit, an unchanged tree is a no-op rather than an error, and a
failed checkpoint never fails the tool that succeeded.

When a workspace is first used, the helper copies
the template into it without replacing existing files. The runtime appends
`AGENTS.md`, `config.toml`, `memory.md`, and the relevant role prompt to each
agent's built-in system policy. `goal.md`, `tasks.md`, and `scratchpad.md` are
also loaded. Workspace context must never replace built-in tool or container
restrictions.

Every runtime agent receives the workspace document tools: bounded download,
read, write, exact edit, index, and search. The index is
`/workspace/.document-index.json` and contains only relative paths in the
selected workspace. Keep the 5 MiB per-document limit and reject non-HTTP
downloads, traversal, symlink escapes, non-UTF-8 content, and missing exact-edit
targets.
Do not move generated artifacts into source directories unless the user asks
to promote a specific artifact into the product.

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
sh -n agent euler langfuse-turns langfuse-review scripts/run-agent \
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
The research agent gets Exa and the Qdrant note tools. The tool-builder gets
workspace file and command tools. The orchestrator gets specialist delegation
tools, not direct shell access.

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

TinyAgents lives at `vendor/tinyagents` as a Git submodule. Initialize it with:

```sh
git submodule update --init --recursive
```

Do not edit vendored code through the parent repository. Make TinyAgents
changes upstream, push them there, then update this repository's gitlink in a
separate commit.

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

Keep every Markdown file at 500 lines or fewer. Put durable operational guidance
in this file and user-facing instructions in `README.md` instead of creating a
separate documentation tree.

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
