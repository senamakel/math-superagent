# TinyAgents Harness

This Rust 2024 library vendors TinyAgents and exposes a small, embeddable
facade for its provider-neutral model, tool, and agent-loop runtime.

## Public API

The [`agent`](src/agent/mod.rs) module re-exports the model, message, tool, and
agent-loop types needed by a host application. `agent::mock` creates a
deterministic offline harness for tests and local development.

[`HelloAgent`](src/hello_agent/mod.rs) is a runnable OpenRouter example. It uses
DeepSeek V4 Flash through StreamLake, exports loop observations to Langfuse,
and provides tools for echoing text, arithmetic, Exa search, and delegating a
focused task to a child agent.

Copy `.env.example` to `.env`, provide the OpenRouter, Exa, and Langfuse
credentials, then run it:

```sh
cargo run --example hello_agent -- "Find a current Rust release and ask a sub-agent to check it"
```

Set `OPENROUTER_MODEL` to override the built-in
`deepseek/deepseek-v4-flash-0731` model. Provider routing remains restricted to
StreamLake.

The original greeting function remains as a small API example while the agent
runtime is integrated by downstream code.

## Layout

```text
src/
├── lib.rs                 # crate docs and public re-exports
├── agent/                 # TinyAgents facade and tests
├── hello_agent/           # OpenRouter agent, basic tools, and sub-agent
├── error/                # crate-wide error type
└── greeting/             # small public API example
vendor/
└── tinyagents/           # pinned TinyAgents submodule
tests/                    # public API integration tests
```

## Development

Initialize the vendored engine and run the contract checks:

```sh
git submodule update --init --recursive
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo build --all-targets --all-features
cargo test --all-features
```

The vendored `tinyagents` dependency is used with its default feature set
disabled. SQLite-backed persistence, the REPL/RLM surfaces, memory domains,
channels, and Web3 are deliberately outside this crate’s scope.

## License

GPL-3.0-only. See [LICENSE](LICENSE).
