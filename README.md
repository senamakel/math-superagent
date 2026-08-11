# Math Research Agent

This is a Dockerized agent for solving mathematical problems through careful
derivation, computation, and source-backed research. It is meant for problems
where a good answer may require several kinds of work: understanding the
mathematics, checking a theorem or definition, writing a small program, and
verifying the result before presenting it.

The runtime uses a small registry of specialist agents:

- `orchestrator` breaks a problem into focused tasks and combines the results.
- `research` searches with Exa and returns evidence with source URLs.
- `tool_builder` writes and runs shell or Python tools for numerical checks,
  experiments, data processing, and reproducible calculations.

The container includes `python`, `python3`, `pip`, and `pip3`. Packages installed
with pip are placed in the selected workspace under `.python-packages`, so the
read-only container filesystem stays intact and dependencies persist with the
problem artifacts.

Every tool call has a hard maximum runtime of ten minutes. The tool-builder
must state time and space complexity before substantial execution, and the
runtime rejects commands declared as exponential. Exponential-time and
exponential-space algorithms are outside the allowed operating policy.

Research notes can be saved to a local Qdrant vector database and recalled in
later runs. The database uses deterministic local feature vectors, so it does
not need another embedding API.

All model calls use DeepSeek V4 Flash through OpenRouter and StreamLake by
default. TinyAgents provides the model loop, tools, delegation, and middleware.
Langfuse receives best-effort observations from each run.

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

Two helper commands are also available:

```sh
./agent build   # build the runtime image
./agent shell   # open a shell under the same Docker restrictions
```

## Solve a Project Euler problem

Pass a positive problem number to the Project Euler wrapper:

```sh
./euler 1
./euler 10 "also compare the optimized method with a brute-force check"
```

The wrapper downloads the official statement from Project Euler's minimal
problem endpoint, then runs the custom orchestrator in
`workspace/project-euler/<number>`. It asks the tool-builder to save a written
derivation as `solution.md`, write a reproducible `solution.py`, execute it, and
check the exact answer. The research agent may look up definitions or primary
mathematical references, but the prompt forbids searching for published Project
Euler answers.

The downloaded statement and source URL remain beside the solution:

```text
workspace/project-euler/1/
├── problem.html
├── problem.url
├── solution.md
└── solution.py
```

Generated programs, calculations, and other artifacts appear in
`workspace/default` unless another workspace is selected. A new workspace is
seeded from [`workspace/template/`](workspace/template/) without overwriting
files already present. The seed includes local agent instructions, role
prompts, configuration, and `memory.md`. The runtime reads those files at the
start of every run.

Use `--workspace` to give a run its own subdirectory:

```sh
./agent --workspace prime-number-theorem "Research and test useful bounds for pi(x)"
```

That command mounts only `workspace/prime-number-theorem` at `/workspace`.
`MATH_AGENT_WORKSPACE=prime-number-theorem ./agent "..."` provides the same
selection through an environment variable. Absolute paths, parent traversal,
and symlinks that leave the repository's `workspace/` root are rejected.

## How a run works

The orchestrator decides which specialist should handle each part of the
problem. Research questions go to the Exa-backed research agent. That agent can
recall related notes from Qdrant and save useful sourced findings for later.
Computations and executable checks go to the tool-builder. The orchestrator
then writes one answer that separates cited facts from its own mathematical
reasoning.

Context compression starts at an estimated 300,000 tokens. A model-backed
summary keeps the decisions, assumptions, formulas, source URLs, command
results, and unresolved work. Recent messages remain verbatim. If the summary
call fails, TinyAgents trims old context instead of losing the whole run.

This is a research and computation assistant, not a formal proof checker.
Important results should still be checked against primary sources or a proof
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
Dockerfile                  build and runtime jail
compose.yaml                agent and Qdrant services
scripts/run-agent           helper implementation
scripts/solve-euler         fetch and solve workflow
workspace/                  selectable agent workspaces, ignored by Git
└── template/               seed instructions, prompts, config, and memory
src/
├── agent/                  TinyAgents facade and Langfuse observations
├── orchestrator/           registry, specialists, compression, workspace tools
│   └── vector.rs           Qdrant research store and local feature vectors
├── hello_agent/            small single-agent example
├── error/                  crate-wide errors
└── lib.rs                  public Rust API
examples/
├── orchestrator.rs         Docker runtime entry point
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
