# The Mycielskian of a graph — raising chromatic number, preserving clique number

**Subject:** The Mycielski construction `mu(G)`, which the run's code uses as
its kernel/rigidity-building machine (`diag_mycielski.py`,
`verdict_mycielski_core.py`, `refute_mycielski_kernel.py` build
`Mycielski^k(C5)` cores). This is the primary treatment making that machinery
a *sourced* fact rather than a code-internal assumption.

## Source

- **Primary treatment:** Piotr Rudnicki, Lorna Stewart, *The Mycielskian of a
  Graph*, Formalized Mathematics 19(3) (2011) 203–209.
  https://doi.org/10.2478/v10037-011-0005-6
- Retrieved via server-side `read_sources` (publisher host blocked at the
  network boundary, as documented in `sources/README.md`).
- Cites the original: J. Mycielski, *Sur le coloriage des graphes*, Colloquium
  Mathematicum 3 (1955) 161–162, doi:10.4064/cm-3-2-161-162.

## What it establishes (statement, with hypotheses)

**Mycielski construction (Mycielskian).** For any finite simple graph `G`,
define `mu(G)` — the Mycielskian of `G` — as follows: take the vertices of `G`,
add a *twin* `x'` for each vertex `x`, plus a single *root* vertex `u`; edges
are the original edges of `G`, edges `x'y'` for each edge `xy` of `G`, and
edges `x'u` for every twin `x'`. Then:

```
omega(mu(G)) = omega(G)      (clique number preserved)
chi(mu(G))   = chi(G) + 1    (chromatic number increased by 1)
```

**Hypotheses:** `G` is a finite simple graph; `mu(G)` is the standard Mycielski
construction as defined. No planarity or unit-distance condition is required —
the construction is purely graph-theoretic.

**Consequence (the classical use):** starting from `K2` and iterating
`M_{n+1} = mu(M_n)` gives triangle-free graphs (`omega = 2`) with chromatic
number growing by 1 per step — triangle-free graphs of arbitrarily large
chromatic number. `M_n` is exponential in size in `n`.

## Why it matters for this run

- The code's kernel-building engine is exactly this: `Mycielski^k(C5)` gives a
  triangle-free graph with `chi = 3 + k`, and the run's scripts hunt its
  5-critical cores as unit-distance-embeddability *and* colouring-obstruction
  candidates. The source fixes `chi(mu(G)) = chi(G) + 1` as a **theorem**, so
  the code's `chrom()` on Mycielski images is computing a known value (a check,
  not a discovery — matching the "identify the graph by structure first"
  lesson).
- It is the same shape as the polynomial SAT-shrinking/spindling machinery: a
  building-block operation whose chromatic effect should be stated as a theorem
  before being leaned on (GOAL.md "construction engine with proved
  properties").
- Caveat for the unit-distance setting: Mycielski preserves *clique number* and
  raises *chromatic number* as abstract graphs, but the run's constructions must
  additionally be unit-DISTANCE — Mu(Mycielskian of a UDG) is typically NOT a
  plane unit-distance graph. The source guarantees the colouring obstruction;
  it says nothing about embeddability, which is the run's separate exact-vector
  problem.

## Basis and status

- `omega(mu(G)) = omega(G)` and `chi(mu(G)) = chi(G) + 1` are **sourced
  verbatim** from the primary treatment (a formalized proof in Mizar —
  Formalized Mathematics), recorded `asserted-by-source` here.
- The run's own SAT oracle can check `chi` on a small Mycielski image if the
  tool_builder wants to verify it computationally (independent of proof).

## Claim block

```claim
id: mycielski-construction-chromatic
statement: For any finite simple graph G, the Mycielskian mu(G) (a twin
  vertex x' for each x, a root u, edges E(G), x'y' for xy in E(G), x'u for all
  x') satisfies omega(mu(G)) = omega(G) and chi(mu(G)) = chi(G) + 1. Iterating
  mu from K2 yields triangle-free graphs of arbitrarily large chromatic number,
  exponential in size in the step count.
hypotheses: finite simple graph G; standard Mycielski construction.
holds-here: YES for the abstract colouring-obstruction it constructs — the
  code's Mycielski^k(C5) cores are exactly this. NOTE: preservation of chi as
  an abstract graph does NOT make mu(G) a plane unit-distance graph; the run's
  unit-distance embeddability must be verified separately per construction.
status: asserted-by-source (Rudnicki–Stewart, Formalized Mathematics 2011;
  original Mycielski 1955).
bearing: fixes chi(mu(G)) = chi(G)+1 as a theorem for the kernel-building
  machine; flags that unit-distance embeddability is a separate, un-sourced
  problem the code must verify exactly.
anchor: research/sources/mycielski-construction-rudnicki-stewart.md
falsifies: a finite simple graph G with chi(mu(G)) != chi(G)+1 or
  omega(mu(G)) != omega(G) under the standard construction — none exists; the
  construction is a theorem.
```
