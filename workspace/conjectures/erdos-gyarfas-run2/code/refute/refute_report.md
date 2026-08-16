# Refutation report: attacking the settled rungs of the E-G weakened ladder

Refuter, running against the two asserted-settled rungs
`R-delta3-n12-small-target` and `R-delta3-n16-three-targets` of the weakened
ladder `erdos-gyarfas-power-of-two-cycle` (see `research/WEAKENED.md`).

## Which statement was attacked, and why

The two rungs, as recorded:

- `R-delta3-n12-small-target`: every finite simple graph G with δ(G) ≥ 3 on at
  most 12 vertices contains a cycle of length 4 or 8. (off: unbounded n,
  prescribed sparse length, long-cycle reach) — marked **settled**.
- `R-delta3-n16-three-targets`: every finite simple graph G with δ(G) ≥ 3 on
  at most 16 vertices contains a cycle of length 4, 8, or 16. (off: unbounded
  n, long-cycle reach) — marked **settled**.

I chose these because they are finite, fully within the reach of exact model
search, and their "settled" status rests on a single 2026 preprint (Balaji,
SMS SAT search to 31 vertices) that the run itself flags as **asserted, under
review, with no formal proof certificate**, and whose n≤16 baseline the run's
own oracle has not reproduced (task `verify-2conn-class-oracle` is open and its
prior output `g_heart_verify_n8.out` is corrupt). A finite rung whose evidence
is uncertified is the kind of statement a refuter can actually decide, unlike
the unbounded targets.

## Structural reduction (the sharpest danger case)

A counterexample to either rung must contain no 4-cycle (else it has a
power-of-two cycle), so its girth is ≥ 5.

- **n≤12**: Moore bound for min-degree 3 — a girth-6 graph needs ≥ 14 vertices,
  a girth-7 graph ≥ 22. So on ≤ 12 vertices the girth is exactly 5 and
  n ∈ {10, 11, 12}. The whole rung reduces to: *every min-degree-3 girth-5
  graph on 10/11/12 vertices has an 8-cycle.*
- **n≤16**: the danger cases are (a) girth-5 graphs on ≤ 16 vertices, and
  (b) girth-6 graphs on 14/15/16 vertices (girth-7 needs ≥ 22). In every case
  girth ≥ 5 kills C4 and n ≤ 16 kills C16, so the rung for such a graph hinges
  **entirely on the 8-cycle**.

The two sharpest concrete cages to check and confirm the 8-cycle in:

- Petersen (n=10, cubic, girth 5, the (3,5)-cage) — the n=10 case.
- Heawood (n=14, cubic, girth 6, the (3,6)-cage) — the smallest girth-6 case.

Both survive. `find_counterexample` **proved** the Petersen 8-cycle from the
pinned graph (a second independent mechanism agreeing with the oracle).

## Hand-checked 8-cycle in the Heawood graph

Line *i* of the Fano plane contains points {i, i+1, i+3} mod 7. The cycle

    0 - L0 - 1 - L5 - 6 - L3 - 4 - L4 - 0

with L0={0,1,3}, L5={5,6,1}, L3={3,4,6}, L4={4,5,0} (points 0,1,6,4 and lines
L0,L5,L3,L4, all distinct) is a genuine simple 8-cycle. Every edge checked:
0∈L0 ✓, 1∈L0 ✓, 1∈L5 ✓, 6∈L5 ✓, 6∈L3 ✓, 4∈L3 ✓, 4∈L4 ✓, 0∈L4 ✓.

So the Heawood (the smallest girth-6 danger) is **not** an 8-cycle-free graph,
and the n≤16 rung survives this attack.

## What the searches returned

- `find_counterexample` on the pinned-Heawood 8-cycle encoding: **undecided**
  (no model of size reached, no proof).
- On the n=12 and n=16 δ≥3 counterexample model searches: **undecided** (the
  model finder cannot decide 12–16-vertex graph existence in its budget).
- On the pinned-Petersen 8-cycle encoding: **proved** (corroborates the oracle
  on the n=10 girth-5 danger case).

## The honest verdict

The two rungs are **corroborated, not refuted, and not independently
re-derived**. Concretely:

- No counterexample found for either rung.
- The directional evidence is: both sharpest cages (Petersen girth-5 n=10 and
  Heawood girth-6 n=14) contain 8-cycles, and a single complete isomorph-free
  SAT search (Balaji 2026) asserts every δ ≥ 3 graph on ≤ 31 vertices has a
  C4/C8/C16.
- But that 31-vertex bound is **asserted, not machine-reproduced here**, and
  the run's own oracle has not yet reproduced even the n≤16 baseline. So
  "settled" in `research/WEAKENED.md` is stronger than the evidence the run
  currently holds.

The single genuinely open danger that would still refute the n≤16 rung is a
**non-regular** min-degree-3 graph of girth 6 on 15 or 16 vertices with no
8-cycle and no 16-cycle. Balaji's search would have covered it, but that is the
one claim I could not independently decide with the tooling available.

## Files

- `code/refute/heawood_n16.py` — oracle probe (Heawood + Petersen): reports
  girth, δ, cycle counts for the two danger cages.
- `code/refute/heawood_8cycle.p` — TPTP: pinned Heawood, conjecture 8-cycle →
  undecided.
- `code/refute/petersen_8cycle.p` — TPTP: pinned Petersen, conjecture 8-cycle →
  proved.
- `code/refute/n12_counterexample.p`, `code/refute/n16_counterexample.p` —
  TPTP δ≥3 counterexample model searches → undecided.
