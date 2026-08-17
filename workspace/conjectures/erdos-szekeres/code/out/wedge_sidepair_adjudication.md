# Wedge/ray-split bipartitions on es_construct(7) — adjudicated result

**Task:** `wedge-split-n7-arbiter` (directive 16). **Executed by:** tool_builder.
**Status:** settled by machine, capture `code/out/wedge_sidepair.captured2.txt` (EXIT 0).

## Method

A convex wedge of angle < π is the intersection of two open half-planes whose
boundary lines meet at an apex; a reflex wedge is the complement of one. The
complete, brute-force-validated list of the N(N−1) open half-plane sides of the
set is exactly what `gsplit_enum_definitive.py` proved exhaustive against the
2^N disjoint-hulls oracle (zero missing, zero extra). So every wedge-realizable
bipartition is an intersection of two open half-plane sides, and enumerating
PAIRS of sides is a SUPERSET of the wedge-realizable bipartitions. A zero valid
count there would be strictly stronger than a zero over wedges.

All geometry exact (integer/Fraction determinants, `lib.es_geom.orient`),
`es_construct` blocks from the verified `lib.es_construct`, validity by
`has_convex_k_subset(·,6)` (no convex 6-gon in a half), 28 workers.

**Positive control (non-negotiable):** witness apex (2400,2725) at n=7 gives a
valid split (both halves 6-avoiding, re-verified independently by
`largest_convex_subset`, 2^16 each); its bipartition MUST appear among the
intersections and among the valid splits. PASS both times.

## Numbers (n=7, es_construct)

| quantity | value |
| --- | --- |
| open half-plane sides | 992 = N(N−1), validated |
| pairs of sides | 491,536 |
| pairs with |inter| = 16 | 13,030 |
| distinct size-16 bipartitions | 2,454 |
| distinct VALID splits (both halves 6-avoiding) | **27** |
| witness bipartition present | True |
| witness split realized as proper wedge at (2400,2725) | True |
| wall clock | 156.7 s (28 workers) |

## What this settles

- **Single open half-planes (`gsplit_phase2.captured.txt`, re-captured EXIT 0):**
  4 / 2 / 0 valid splits at n = 5 / 6 / 7. The single-line splitting induction
  f(n) ≤ 2f(n−1) fails on this template at n=7.
- **Double-wedge family (superset of wedge cuts): 27 valid splits at n=7.** So
  the failure at n=7 is a property of single-line cuts, not of all two-ray
  separations: the double-wedge cut family does realize (n−1)-avoiding splits
  of this 2^{n−2}-point set into two 2^{n−3}-halves.
- **Framing question (directive 14/16): which cut family realizes the known
  even/odd block split?** `wedge_evenodd_alln.captured.txt` (EXIT 0): at n=5,6
  the even/odd block bipartition is NOT a single open half-plane side but IS an
  intersection of two open half-plane sides; at n=7 it is NEITHER
  (`wedge_evenodd_check.captured.txt`, EXIT 0), although both halves are
  independently 6-avoiding (largest convex subset = 5 on each, exact 2^16
  verification). The even/odd split is therefore NOT realizable as a wedge cut
  on this template at n=7 — a distinct structural fact about the extremal
  construction.

## Scope (strict, per steer 2/14)

All statements are about the **verified `es_construct` template only**, at the n
stated. They say nothing about other extremal sets, about the general G-split
lemma, or about the ES upper bound. The double-wedge superset family is
exhaustive for the side-pair intersections; full apex-cell wedge-realizability
of all 27 splits (a lower bound per split) is NOT claimed — the apex probe in
step (6) is exact but coarse (witness apex + a rational grid).

## Files

- `code/out/wedge_sidepair.captured2.txt` — the completed run (EXIT 0).
- `code/out/wedge_sidepair.captured.txt` — earlier truncated capture (no (5)/(6),
  superseded by captured2).
- `code/out/wedge_evenodd_check.py` / `.captured.txt` — n=7 even/odd membership test.
- `code/out/wedge_evenodd_alln.py` / `.captured.txt` — n=5,6,7 family-membership table.
- Superseded: `wedge_split_enum.py`, `wedge_cell_enum_corrected.py`
  (directive-15 per-cell enumeration, intractable, abandoned by directive 16),
  `wedge_enum_full_captured.txt` (abandoned at order 121/387).

## Record for the run

The task ledger is owned by the director; this entry should be closed with the
numbers above as the reason. Board post written by tool_builder.