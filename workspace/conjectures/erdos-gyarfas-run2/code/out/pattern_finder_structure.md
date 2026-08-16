# Pattern-finder: exploitable structure in the run's computed data

## Two clean findings

### Finding 1 — The 2-connected δ≥3 count sequence is OEIS A006289 (exact identification)

The number of nonisomorphic **2-connected** graphs with **minimum degree ≥ 3**
on n vertices:

```
n = 4  5   6    7      (8)
    1  3  19  149   (2581 predicted)
```

- Computed by the corrected ear-decomposition generator
  (`code/lib/biconnected_gen.generate_2connected_levels`), which was itself
  validated against A002218 (total 2-connected counts 1,3,10,56,468) and an
  independent brute-force enumeration for n ≤ 6.
- `oeis_lookup` on 1,3,19,149 returns A006289 (number of series-reduced
  2-connected graphs), whose next terms are 2581, 84151, 5201856, …
- **This match is exact by definition, not a numerical coincidence.** A
  2-connected graph has no vertex of degree 0 or 1. So "minimum degree ≥ 3"
  ⟺ "no vertex of degree 2" ⟺ **series-reduced**. Hence the count sequence is
  A006289 for all n. Verified exactly over n = 4..7; a catalogued
  identification (sourced), conjectured to hold for all n. It predicts the
  n=8 value is **2581** (generator cannot currently reach n=8 — 7123 total
  2-connected graphs is too slow under the pairwise-VF2 dedup).
- Disambiguation: A006289 and A054316 (2-connected 3-edge-connected) both
  start 1,3,19,149 but **diverge at n=8** (2581 vs 2578). Our class is
  series-reduced = A006289, not the 3-edge-connected class. This matters if
  the generator is ever extended to n=8.

### Finding 2 — G-heart verification is clean: no 2-connected δ≥3 counterexample on n ≤ 7

Over **every** 2-connected graph with δ ≥ 3 on n ≤ 7 vertices, checked with
the exact brute-force oracle `erdos_gyarfas.has_power_of_two_cycle`:

```
n : #2conn δ≥3 : #with a 4/8/16-cycle : #without
3 :     0     :          0            :   0
4 :     1     :          1            :   0
5 :     3     :          3            :   0
6 :    19     :         19            :   0
7 :   149     :        149            :   0
```

**zero** graphs avoid a 4/8/16-cycle in this class up to n=7. This is the
sharpest exact 2-connected-specific verification the run has, and it is
consistent with (and slightly sharpens) the literature's general bound: any
δ≥3 counterexample needs ≥ 31 vertices (Balaji SMS), and the 2-connected
restriction does not change that up to n=7.

This is **verified-numerically**, not a proof: it rests on the correctness of
the oracle (validated against the worked examples and an independent
edge-subgraph enumerator) and the exactness of the 2-connected generator
(validated against A002218 + independent enumeration).

## Data corruption found and corrected

`code/out/g_heart_verify_n8.out` reports 2-connected counts
`1,1,4,19,121,1042` with **0** δ≥3 graphs at every level, and "VERIFIED"
verdicts. This is **stale output from the abandoned old `layer_by_layer`
generator** (the 1,1,4,19,121 prefix is the A280939 numerical-coincidence
sequence, not the true 2-connected count), and its δ≥3 count of 0 at every
level is factually wrong — the corrected generator finds 1, 3, 19, 149 such
graphs for n=4..7. Its VERIFIED verdicts are therefore **vacuous** (they
checked zero graphs) and must not be cited. The regeneration confirms zero
counterexamples, so the *conclusion* survives, but the corrupt file's rows
are wrong.

## Sequences with NO usable structure

- **2-connected counts A002218**: super-exponential; no low-degree polynomial,
  no constant-coefficient linear recurrence (orders 1..8). Nothing to extract.
- **Near-miss minimal orders** 24 (avoid {4,8}), 78 (avoid {4,8,16}), 540
  (avoid {4,8,16,32}): only 3 terms, ratios 3.25, 6.92 and all divisible by 6
  (they are all even *and* divisible by 3 because cubic graphs have even vertex
  count with the handshake restriction). Too few terms and no known pattern to
  warrant a fit; note the shared factor 6 only.

## What the structural regularities suggest

1. **A006289 is a lever, not just a label.** The literature's general
   verification bound is 31 vertices (Balaji). The number of series-reduced
   2-connected candidates grows only as A006289 (2581 at n=8), far slower than
   the total 2-connected class (7123 at n=8) or the general δ≥3 class. This is
   exactly the class a minimal counterexample would have to live in (a minimal
   counterexample is 2-connected? — needs checking — and near-cubic), so a
   SAT/backtracking verification of *this* class is dramatically cheaper per
   vertex and could extend the verified 2-connected-specific range well past
   n=7 toward matching/beating the 31-vertex general bound.
2. **A006289's growth is a concrete workload model.** Extending the 2-connected
   δ≥3 verification to n=8 needs 2581 graphs (vs 7123 total), to n=9 needs
   84151 — still enumerable by a canonically-hashed generator where the
   pairwise-VF2 one is not. This is the concrete next scaling target.

## Status of claims

- Finding 1 (A006289 count = 2-connected-series-reduced): **catalogued
  identification, exact over n=4..7, conjectured all n**, sourced to OEIS
  A006289, arithmetic computed and checked.
- Finding 2 (no 2-connected δ≥3 counterexample on n ≤ 7): **verified
  numerically** (exact oracle over the exact bijectively-generated class),
  not a proof; extends the known 2-connected-specific range only in that the
  run's own oracle re-confirms it cleanly.

All numbers above are from programs run this cycle (see the command log), not
from any imagination; the only non-computed data are the OEIS catalogue terms.
