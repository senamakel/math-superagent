FROM rust:1.96-bookworm AS builder

WORKDIR /build
COPY Cargo.toml Cargo.lock ./
COPY src ./src
COPY examples ./examples
COPY vendor/tinyagents ./vendor/tinyagents
RUN cargo build --locked --release --example orchestrator

FROM debian:bookworm-slim

# The scientific stack is baked into the image rather than pip-installed per
# run. A run that has to install sympy before it can factor anything spends
# minutes of its budget on setup and fails outright if the index is slow, and
# every workspace pays again. These are the libraries this kind of work
# actually reaches for: exact symbolic algebra, arbitrary-precision integers,
# arrays, and graphs. Installed from apt rather than pip because the container
# root filesystem is read-only at runtime, so system packages are the only ones
# guaranteed importable without writing to /workspace first.
RUN apt-get update \
    && apt-get install --yes --no-install-recommends ca-certificates curl git jq python3 python3-pip \
       python3-sympy python3-numpy python3-scipy python3-gmpy2 python3-networkx \
       python3-mpmath python3-pandas python3-matplotlib \
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
