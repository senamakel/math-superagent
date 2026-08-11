FROM rust:1.96-bookworm AS builder

WORKDIR /build
COPY Cargo.toml Cargo.lock ./
COPY src ./src
COPY examples ./examples
COPY vendor/tinyagents ./vendor/tinyagents
RUN cargo build --locked --release --example orchestrator

FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install --yes --no-install-recommends ca-certificates curl git jq python3 python3-pip \
    && ln -s /usr/bin/python3 /usr/local/bin/python \
    && ln -s /usr/bin/pip3 /usr/local/bin/pip \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 10001 --shell /usr/sbin/nologin agent \
    && mkdir /workspace \
    && chown agent:agent /workspace

COPY --from=builder /build/target/release/examples/orchestrator /usr/local/bin/math-agent

USER agent
WORKDIR /workspace
ENV MATH_AGENT_CONTAINER=1
ENV AGENT_WORKSPACE=/workspace
ENV QDRANT_URL=http://qdrant:6333
ENV PIP_TARGET=/workspace/.python-packages
ENV PYTHONPATH=/workspace/.python-packages
ENV PIP_NO_CACHE_DIR=1

ENTRYPOINT ["/usr/local/bin/math-agent"]
