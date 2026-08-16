# Leaf-to-leaf paths and cycles in degree-critical graphs

Source: https://link.springer.com/article/10.1007/s00493-026-00205-2 (Combinatorica, 2026,
doi:10.1007/s00493-026-00205-2). Full text:
`research/sources/degree-3-critical-leaf-to-leaf-cycles.combinatorica.full.md`.

## What the source establishes

Definition used throughout: an *n*-vertex graph is **degree 3-critical** if it
has `2n - 2` edges and no proper induced subgraph with minimum degree at least 3.

**Theorem 1.** Every *n*-vertex degree 3-critical graph has Ω(log n) distinct cycle
lengths.

**Theorem 2.** Every tree with maximum degree Δ ≥ 3 and ℓ leaves has at least
`log_{Δ-1}((Δ-2)ℓ)` distinct leaf-to-leaf path lengths.

**Theorems 3–5.** For every N ≥ 1 there exist arbitrarily large 1–3 trees (every
vertex degree 1 or 3) with O(N^0.91) distinct leaf-to-leaf path lengths smaller than
N; with the complementary lower bound (every 1–3 tree on ≥ 2^N vertices has
Ω(N^{2/3}) distinct such lengths); and the Ω(log n) cycle-length bound is tight up
to a constant factor.

## Why this matters to the Erdős–Gyárfás run

This is the exact structural class the run's minimal-counterexample thread lives
in. A vertex-minimal counterexample to E–G has no proper subgraph with δ ≥ 3 —
any proper subgraph of a minimal counterexample either has a 2-power cycle (which
the whole graph then has) or has a vertex of degree ≤ 2. Adding edges to raise all
such vertices to degree 3, a degree-3-critical spine is the natural object. The
Erdős–Faudree–Gyárfás–Schelp 1988 question these results resolve is *about* the
cycle spectrum of these graphs.

The connection is structural and worth holding, but **not** a proof step: Ω(log n)
distinct cycle lengths among O(n) possible lengths does not force a power of two,
and the powers of two remain sparse. Theorems 3–5 show the spectrum fidelity of the
extremal class is limited (some 1–3 trees have few small path lengths), which is
the near-counterexample regime Bensmail's construction already exhibits.

```claim
id: dcg-degree3-critical-omn-log-n-cycle-lengths
statement: Every n-vertex degree 3-critical graph (2n-2 edges, no proper induced subgraph with min degree ≥ 3) has Omega(log n) distinct cycle lengths.
hypotheses: G degree 3-critical on n vertices
holds-here: yes (minimal E-G counterexamples are degree-3-closed downward; the class directly constrains their cycle spectrum)
status: asserted
bearing: establishes the cycle-spectrum breadth of the minimal-counterexample spine, but Omega(log n) cycle lengths do not force a power of two; complementary Theorems 3-5 show sparse spectra are possible in the extremal class
anchor: research/sources/degree-3-critical-leaf-to-leaf-cycles.combinatorica.full.md
```
