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

# SageMath. It is the most capable tool on this list and by far the largest:
# 723 packages, and every rebuild pays for them. It is installed in its own
# layer, after the smaller stack above and before the binary is copied in, so
# the cost is paid once and cached — editing Rust source invalidates only the
# COPY below it, not this.
RUN apt-get update \
    && apt-get install --yes --no-install-recommends sagemath \
    && rm -rf /var/lib/apt/lists/*

# The constraint-solving stack, for the `solver` role. A declarative encoding
# handed to an engine that does propagation, clause learning, and symmetry
# breaking beats a backtracking search written from scratch in one turn, and
# rewriting one of these by hand is precisely the answer-space search the
# method policy prohibits — so the engines have to be present or the role
# cannot exist. Placed after SageMath so editing this list does not invalidate
# that layer.
#
# CP-SAT and PySAT come from pip because Debian ships neither: `python3-ortools`
# resolves as a name and has no installation candidate. They are baked at build
# time into the system site-packages, before PIP_TARGET is set below, because
# the container root filesystem is read-only at runtime and a run that has to
# install its solver before it can encode anything has already lost minutes of
# its budget.
RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
       python3-z3 python3-pulp python3-pycosat python3-igraph \
       z3 cvc5 minisat cryptominisat glpk-utils coinor-cbc \
    && pip3 install --break-system-packages --no-cache-dir ortools python-sat \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /build/target/release/examples/orchestrator /usr/local/bin/math-agent

USER agent
WORKDIR /workspace
ENV MATH_AGENT_CONTAINER=1
ENV AGENT_WORKSPACE=/workspace
ENV QDRANT_URL=http://qdrant:6333
ENV PIP_TARGET=/workspace/.python-packages
# Pip installs first, then the run's own code. `/workspace/code` on the path is
# what makes reuse work at all: every agent's working directory is /workspace,
# so `from lib.perms import lex_ranks` resolved only by accident, when a
# program happened to be started as `python code/<name>.py` and Python put that
# folder on the path itself. Any other invocation raised ImportError, and the
# committed workspaces carry three separate `sys.path.insert` dialects from
# agents working that out the hard way — after which they stopped importing and
# started pasting, one of them ending with seven copies of the same function.
# Reuse has to be the cheap path or it does not happen.
ENV PYTHONPATH=/workspace/.python-packages:/workspace/code
ENV PIP_NO_CACHE_DIR=1

ENTRYPOINT ["/usr/local/bin/math-agent"]
