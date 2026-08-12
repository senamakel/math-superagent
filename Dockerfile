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

# Lean 4 with a pre-built Mathlib, for the `lean_prover` role. Everything else
# this runtime produces is evidence; a Lean proof that compiles with no `sorry`
# is the thing itself, and that is worth the size. It is the largest layer here
# by a wide margin, and it goes *above* the smaller stacks rather than below
# them: Docker invalidates every layer after the one that changed, so the
# cheapest thing to rebuild belongs last. With this beneath the constraint
# stack, adding one solver package re-downloaded 8,684 Mathlib oleans.
#
# `lake exe cache get` downloads the compiled oleans rather than building
# Mathlib from source — the difference is minutes against many hours. `elan
# default` sets the toolchain globally, not just inside /opt/mathlib4: an
# override is directory-scoped, and the agent's working directory is
# /workspace, where a `lean` invocation would otherwise fail with "no default
# toolchain configured".
ENV ELAN_HOME=/opt/elan
ENV PATH=/usr/local/bin:/opt/elan/bin:$PATH
RUN curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /tmp/elan-init.sh \
    && sh /tmp/elan-init.sh -y --default-toolchain none \
    && rm /tmp/elan-init.sh \
    && git clone --depth 1 https://github.com/leanprover-community/mathlib4.git /opt/mathlib4 \
    && cd /opt/mathlib4 \
    && elan toolchain install "$(cat lean-toolchain)" \
    && elan default "$(cat lean-toolchain)" \
    && lake exe cache get \
    && lake build \
    && lake env printenv LEAN_PATH > /opt/lean_path.txt \
    && chmod -R a+rX /opt/elan /opt/mathlib4 /opt/lean_path.txt

# `lean` is wrapped rather than given an `ENV LEAN_PATH`, because the value is
# the search path of every Mathlib dependency and is only known after the build
# above ran — and `ENV` cannot take a command substitution. Without the full
# path a plain `import Mathlib.…` fails on `unknown module prefix 'Batteries'`,
# which reads as a broken install rather than a missing variable.
#
# The smoke test runs as the unprivileged runtime user, not as root. `lake exe
# cache get` unpacks its oleans mode 600, so every import failed at runtime with
# `Permission denied` on a file that plainly existed — a root-only smoke test
# passes and tells you nothing about the run.
RUN printf '#!/bin/sh\nLEAN_PATH="$(cat /opt/lean_path.txt)${LEAN_PATH:+:$LEAN_PATH}"\nexport LEAN_PATH\nexec /opt/elan/bin/lean "$@"\n' > /usr/local/bin/lean \
    && chmod 0755 /usr/local/bin/lean \
    && printf '%s\n' 'import Mathlib.Combinatorics.SimpleGraph.Finite' > /tmp/smoke.lean \
    && chmod 0644 /tmp/smoke.lean \
    && su agent -s /bin/sh -c 'lean /tmp/smoke.lean' \
    && rm /tmp/smoke.lean

# The constraint-solving stack, for the `solver` role. A declarative encoding
# handed to an engine that does propagation, clause learning, and symmetry
# breaking beats a backtracking search written from scratch in one turn, and
# rewriting one of these by hand is precisely the answer-space search the
# method policy prohibits — so the engines have to be present or the role
# cannot exist. It is the layer most likely to gain a package, so it is placed
# last of the toolchains where a rebuild costs the least.
#
# `eprover`, `pari-gp` and `singular` join them because they answer the same
# kind of question with different machinery, and the roles that use them are
# separate for that reason. E is a first-order saturation prover reading TPTP,
# for statements whose content is quantifier reasoning over relations rather
# than arithmetic. PARI/GP is far faster than sympy on integer factorisation and
# on anything algebraic-number-theoretic. Singular answers ideal membership by
# Gröbner basis, which nothing else installed here does.
#
# `maxima` and `gap` were tried and left out: both segfault or exit silently in
# this container, and naming a tool in a prompt that does not run costs the run
# a turn to discover. SageMath, already installed above, carries that ground.
#
# `nauty` is here rather than with the scientific stack because it belongs to
# the same job: exhaustive generation of graphs up to isomorphism is what turns
# a SAT solver's `UNSAT` from an assertion into a cross-checked bound, and
# `nauty-geng -d3 <n>` is the oracle for any statement about small graphs of
# minimum degree three. Debian prefixes every binary, so it is `nauty-geng`,
# not `geng`.
#
# CP-SAT and PySAT come from pip because Debian ships neither: `python3-ortools`
# resolves as a name and has no installation candidate. They are baked at build
# time into the system site-packages, before PIP_TARGET is set below, because
# the container root filesystem is read-only at runtime and a run that has to
# install its solver before it can encode anything has already lost minutes of
# its budget.
#
# `numpy scipy pandas matplotlib` are re-installed from pip beside them, and
# that is not redundancy. CP-SAT depends on NumPy 2, pip therefore upgrades it,
# and Debian's `python3-matplotlib` and `python3-pandas` are compiled against
# NumPy 1 — so `import igraph`, which pulls matplotlib transitively, printed six
# `_ARRAY_API not found` tracebacks before struggling on. Pip installs into
# `/usr/local/lib/python3/dist-packages`, which precedes the apt tree on
# `sys.path`, so the pip wheels shadow the apt builds and the whole stack agrees
# on one NumPy. `--upgrade` is load-bearing: apt's builds carry dist-info, so
# without it pip reports them already satisfied, installs nothing, and the
# tracebacks survive a build that reported success.
#
# The smoke test runs as the unprivileged runtime user rather than as root, for
# the same reason the Lean one does: a check that passes as root says nothing
# about the run.
RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
       python3-z3 python3-pulp python3-pycosat python3-igraph \
       z3 cvc5 minisat cryptominisat glpk-utils coinor-cbc \
       nauty \
       eprover pari-gp singular \
    && pip3 install --break-system-packages --no-cache-dir --upgrade \
       ortools python-sat numpy scipy pandas matplotlib \
    && rm -rf /var/lib/apt/lists/* \
    && su agent -s /bin/sh -c 'python3 -W error::RuntimeWarning -c "import igraph, matplotlib, pandas, numpy, z3, pycosat, pulp, pysat.solvers; from ortools.sat.python import cp_model"' \
    && su agent -s /bin/sh -c 'nauty-geng -q -c -d3 8 | wc -l' \
    && printf '%s\n' 'fof(a1, axiom, ![X]: (p(X) => q(X))).' 'fof(a2, axiom, p(a)).' \
       'fof(goal, conjecture, q(a)).' > /tmp/smoke.p \
    && chmod 0644 /tmp/smoke.p \
    && su agent -s /bin/sh -c 'eprover --auto --cpu-limit=30 /tmp/smoke.p | grep -q "SZS status Theorem"' \
    && su agent -s /bin/sh -c 'echo "print(factor(2^67-1))" | gp -q' \
    && printf '%s\n' 'ring r=0,(x,y),dp; ideal I=x2+y2-1,x-y; std(I); quit;' > /tmp/smoke.sing \
    && chmod 0644 /tmp/smoke.sing \
    && su agent -s /bin/sh -c 'Singular -q /tmp/smoke.sing' \
    # SageMath is installed several layers above, and this is where it is
    # checked: a smoke test beside its own `apt-get` would put the slowest
    # verification in the image behind the most expensive layer to rebuild.
    # It is verified at all for the reason Lean is — `symbolic_math` is told to
    # reach for `sage`, and a tool named in a prompt that does not run costs
    # the run a turn to discover, which is exactly why `maxima` and `gap` were
    # dropped. It runs as the unprivileged user because Sage writes a dot-
    # directory on first start, and a check that passes only as root says
    # nothing about the run.
    && su agent -s /bin/sh -c 'sage -c "print(factor(2^67-1))" | grep -q 193707721' \
    && rm /tmp/smoke.p /tmp/smoke.sing

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
