FROM rust:1.96-bookworm AS builder

WORKDIR /build
COPY Cargo.toml Cargo.lock ./
COPY src ./src
COPY examples ./examples
COPY vendor/tinyagents ./vendor/tinyagents
RUN cargo build --locked --release --example orchestrator

FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install --yes --no-install-recommends ca-certificates curl jq python3-minimal \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 10001 --shell /usr/sbin/nologin agent \
    && mkdir /workspace \
    && chown agent:agent /workspace

COPY --from=builder /build/target/release/examples/orchestrator /usr/local/bin/riemann-agent

USER agent
WORKDIR /workspace
ENV RIEMANN_CONTAINER=1
ENV AGENT_WORKSPACE=/workspace

ENTRYPOINT ["/usr/local/bin/riemann-agent"]
