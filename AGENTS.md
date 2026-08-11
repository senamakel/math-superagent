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

The runtime has four roles:

- The orchestrator decomposes a problem, delegates focused tasks, and combines
  the results.
- The goals agent translates an objective into completion criteria and spawns
  research or tool-builder subagents until the goal is met or precisely blocked.
- The research agent uses Exa to find definitions, papers, official references,
  or current facts. It returns source URLs, separates evidence from inference,
  and can save reusable notes to Qdrant.
- The tool-builder writes and executes shell or Python tools in `/workspace`.
  It handles numerical checks, counterexample searches, data extraction, and
  other reproducible calculations.

The runtime image must expose both `python` and `python3`, plus `pip` and
`pip3`. Pip installs belong under `/workspace/.python-packages`; do not make the
container root filesystem writable for package installation.

Every tool call has a hard ten-minute deadline. Before substantial execution,
the tool-builder must state both time and space complexity. Algorithms with
exponential time or space complexity are prohibited; choose a polynomial or
better formulation. The timeout is a safety ceiling, not permission to run an
intractable approach.

When changing prompts or agent behavior, keep these rules intact:

1. State assumptions and define ambiguous notation.
2. Show the main derivation or argument. Do not jump straight to the answer.
3. Delegate external fact-finding to `research` and cite the returned sources.
4. Delegate meaningful computation to `tool_builder`. Report the program or
   command and the relevant output.
5. Check edge cases, dimensions, signs, domains, and limiting behavior when
   they apply.
6. Distinguish a proof, a numerical check, a heuristic, and a sourced claim.
7. Say when the evidence is incomplete. Never invent a theorem, citation, or
   computation result.

The runtime is not a formal proof assistant. Do not describe sampled evidence or a
floating-point experiment as proof.

## Runtime architecture

The Rust crate vendors TinyAgents and keeps the integration deliberately small.

```text
src/
├── lib.rs              # public exports
├── agent/              # TinyAgents facade, OpenRouter, Langfuse
├── orchestrator/       # registry, specialists, compression, workspace tools
│   ├── async_subagents.rs # graph-backed asynchronous child-run controls
│   ├── documents.rs    # bounded workspace documents and local search index
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

The executable registry contains `goals`, `research`, and `tool_builder`.
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

Generated workspace files are ignored by Git except for `workspace/.gitkeep`
and `workspace/template/`. When a workspace is first used, the helper copies
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
