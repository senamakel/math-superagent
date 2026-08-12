> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/arjunbalaji-modal-sms.py.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://raw.githubusercontent.com/ArjunBalaji79/erdos-gyarfas-min-degree-3/main/erdos_gyarfas/experiments/modal_sms.py | converted from plain text -->

## What is in it

- Build SMS WITH the Glasgow subgraph solver (-s) for the forbidden-subgraph
# propagator.…
- SMS image + an INDEPENDENT LRAT proof checker (drat-trim's lrat-check), which
# shares no…


## What it claims

Soundness rests on: SMS symmetry breaking (sound), the Glasgow forbidden-subgraph
propagator (complete subgraph isomorphism), and the min-degree CNF. We VALIDATE
this by reproducing our nauty ground truth (C4-only at n=10 -> 5 classes) and the
n<=16 baseline (0 solutions).

Build is Linux-only and compiles CaDiCaL + the Glasgow solver, so it lives in the
image.

modal run erdos_gyarfas/experiments/modal_sms.py::diag_main
"""
from __future__ import annotations

import modal

app = modal.App("erdos-gyarfas-sms")

*[digest of a 18824 character source; every section, statement, and proof in full at `research/sources/arjunbalaji-modal-sms.py.full.md`]*
