# Slim OpenHuman Agent Harness

This Rust 2024 library vendors the provider-neutral agent engine used by
OpenHuman and exposes a small, embeddable facade. The build intentionally
omits OpenHuman application domains for persistent memory, external channels,
and Web3.

## Public API

The [`agent`](src/agent/mod.rs) module re-exports the model, message, tool, and
agent-loop types needed by a host application. `agent::mock` creates a
deterministic offline harness for tests and local development.

The original greeting function remains as a small API example while the agent
runtime is integrated by downstream code.

## Layout

```text
src/
├── lib.rs                 # crate docs and public re-exports
├── agent/                 # slim OpenHuman facade and tests
├── error/                # crate-wide error type
└── greeting/             # small public API example
vendor/openhuman/
└── tinyagents/           # pinned OpenHuman agent engine submodule
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
