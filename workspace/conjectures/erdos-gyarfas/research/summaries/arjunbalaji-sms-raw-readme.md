> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/arjunbalaji-sms-raw-readme.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://raw.githubusercontent.com/ArjunBalaji79/erdos-gyarfas-min-degree-3/main/README.md | converted from plain text -->

## What is in it

- Erdős–Gyárfás conjecture for minimum-degree-3 graphs
  - Result
  - Two independent methods
  - Verification
  - Repository layout
  - Reproducing
    - Local validation gates (fast)
Requires Python ≥ 3.10, `python-sat`, `networkx`, and…
    - SMS frontier (the main result)
Requires a [Modal](https://modal.com) account (`pip…
- the frontier: n=17..31 (each returns UNSAT = no such graph)
modal run --detach…
    - CEGAR cross-check (no Modal needed for small n)
```bash
PYTHONPATH=. python -m…
  - Citing this work
  - License


## What it claims

A SAT-based verification that every graph of minimum degree at least 3 on **at most
31 vertices** contains a cycle whose length is a power of two — establishing that
any minimum-degree-3 counterexample to the **Erdős–Gyárfás conjecture** must have at
least **32 vertices**.

This raises the published *general* minimum-degree-3 frontier from `n ≥ 17` (Royle &
Markström, ~2004) to `n ≥ 32`, and is, to our knowledge, the first application of
SAT methods to this conjecture. Since the cubic class is contained in the
minimum-degree-3 class, it also surpasses Markström's separate cubic bound of 30.
Verifying through `n = 31` settles the entire range in which `C₄, C₈, C₁₆` are the
only admissible power-of-two cycle lengths (`C₃₂` first fits at `n = 32`).

*[digest of a 5152 character source; every section, statement, and proof in full at `research/sources/arjunbalaji-sms-raw-readme.full.md`]*
