# Pattern-finder report — round 2

## What changed since the last pass

The Makhnev/Reimbayev n3 pivot moved from *pending* to *checked* on both
controls during this run (see `makhnev-1988-condition-captured.txt`,
`hexagon_identity_verified.captured.txt`). I re-derived the local data with an
independent script (`code/out/n3_deduction_check.py`, exact integer arithmetic
over the adjacency matrices) and surfaced — and fixed — a subtlety in the join
count.

## Finding A — n3 (RE-CHECKED here, exactly)

For an `srg(v,k,1,2)` with `lambda=1, mu=2`, let `n3` = number of *disjoint*
triangle pairs joined by exactly 2 edges (the two parameters Reimbayev's order-6
structure hangs on; shared-vertex pairs are joined by >=3 edges and never
contribute). Measured exactly on both existing members:

| graph | T (triangles) | join histogram (disjoint pairs) | n3 |
|---|---|---|---|
| rook(3) srg(9,4,1,2) | 6 | {3:6} (all disjoint pairs) | **0** |
| BvLS srg(243,22,1,2) | 891 | {0:133650, 1:240570, 3:8910, 2:0} | **0** |

Both histograms are complete: sum = C(T,2) minus shared-vertex pairs = 396495−13365
= 383130, exactly the disjoint-pair total. So **both existing members have n3 = 0**
and both attain the Reimbayev hexagon lower bound (bound attained iff n3=0).

Variable naming note: my first pass mixed shared-vertex pairs into the histogram
(their {4:13365} and rook's {4:9}); the *correct* Makhnev count is over disjoint
pairs only, which gives n3=0 above. The shared-vertex 4-joined pairs are a
separate, non-load-bearing set.

## Finding B — the sharp separation (SOURCED, not derived here)

Makhnev's primary-text theorem (research/sources/makhnev-1988-lambda1-russian-fulltext.full.md,
Thm 2) proves **no srg(99,14,1,2) satisfies condition (*)**, i.e. no such graph has
n3 = 0. Combining with Finding A's check:

> **Any putative srg(99,14,1,2) is forced to have n3 >= 1 — it cannot attain the
> Reimbayev hexagon lower bound, while both existing family members DO attain it.**

This is the parameter-specific separation that the spectral routes (integrality,
Krein, absolute bound) could not produce: 9 (n3=0) and 243 (n3=0) sit exactly at
the bound; 99 is forced strictly above it. The equilogic must be labelled
correctly:

- **Checks performed here (exact):** n3=0 on both controls; both histograms
  complete.
- **Sourced, not reproduced here:** Makhnev Thm 2's exclusion of n3=0 at 99.
  I did *not* verify his 99-proof (it builds an srg(33,12,1,6) subobject from a
  triangle's closure). So "99 has n3>=1" is a **consequence of a published
  proof I have not machine-checked**, not a fresh derivation of this run.

## Sequences that showed no further structure

The family sequences from `code/out/derived_design_sequences.py` —
distance-2 counts `[4,84,220,6160,493024]`, outer blocks
`[0,140,660,110880,81348960]`, eigenvalue multiplicities `[4,54,132,3280,250914]`,
`[4,44,110,2992,243104]` — all satisfy **no low-order constant-coefficient linear
recurrence** (checked up to order 4 on 5 terms) and are exactly the quartic-in-`u`
closed forms from `k = u^2+u+2`. No new law there; the `a=7` integrality
characterization already captures them.

## Bottom line

No new *sequence* structure in the family (all governed by known closed forms).
The genuinely new content this round is the n3 pivot reaching *checked* status on
both controls, plus the precise separation it yields against 99 (sourced via
Makhnev 1988). This is the one count that separates 99 from both positive
controls — a real candidate lever — but its 99-half rests on a source proof not
re-derived here, and it is NOT a nonexistence proof (it only forces n3≥1,
consistent with the standing open status).
