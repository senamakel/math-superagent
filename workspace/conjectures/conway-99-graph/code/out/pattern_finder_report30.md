# Pattern-finder report — round 30: independent re-certification of the sequence catalogue and one mislabel correction

## What this round did

An independent sweep of the sequence surface, re-running the exact tools on the
signature family sequences and deriving the in-`u` polynomial structure of every
one. The 29 prior rounds declared the sequence line closed; this round
re-verified that verdict with fresh computations and found exactly **one
genuine correction** (an induced-C4 mislabel in a capture) — everything else
holds as recorded.

## The in-u census — every family count is a divisor-63-governed polynomial

All family counts are exact low-degree **polynomials in u** over the feasible
index set `u ∈ {1,3,4,10,31}` (driven by `a = 2u+1 | 63`), confirmed by sympy
(`code/out/pattern_finder_degree_census.py`):

| quantity | degree in u | values |
|---|---|---|
| k = u²+u+2 | 2 | 4,14,22,112,994 |
| v (vertices) | 4 | 9,99,243,6273,494019 |
| triangles T = vk/6 | 6 | 6,231,891,117096,81842481 |
| induced C5 = vk(k-2)(k-4)/5 | 10 | 0,33264,384912,1669320576,96451036488576 |
| hexagons (n3=0) | 12 | 6,209286,4980690,146767540920,79371206037594576 |
| n3-cap = k(k-2)(k²+2)/8 | 8 | 18,4158,26730,19320840,121781611728 |
| distance-2 = k(k-2)/2 | 4 | 4,84,220,6160,493024 |
| outer blocks = k(k-2)(k-4)/12 | 6 | 0,140,660,110880,81348960 |
| replication (k-4)/2 | 2 | 0,5,9,54,495 |
| matching-pairs/vertex k(k-2)/8 | 4 | 1,21,55,1540,123256 |
| true induced C4 = vk(k-2)/8 | 6 | 9,2079,13365,9660420,60890805864 |

Three quantities are **rational functions** of u that happen to be integer-valued
at the feasible index points (their integrality is exactly the a|63 division):

- coclique Hoffman α = v(u+1)/(k+u+1): 3,22,45,561,15408
- multiplicity m_r: 4,54,132,3280,250914
- multiplicity m_s: 4,44,110,2992,243104

Every product-count above reproduces the recorded tables exactly (triangles,
C5, coclique verified term-by-term against the on-disk captures). This is the
established catalogue class: quartic-or-higher in u at five non-consecutive
index points, so `analyze_sequence` correctly reports "not a low-degree
polynomial" and `find_linear_recurrence` correctly reports "no order ≤ 4
constant-coefficient fit" — these are **not** counter-evidence, they are the
signature of the divisor-63 family.

## The one genuine correction: induced-C4 is mislabelled in a capture

`code/out/induced_C4_family.py` labels `v*k*(k-2)/4` as "induced-C4". That value
is the **nonedge count** `v(v-1-k)/2`, not the induced-C4 count. The corrected
identity (proved in `inducedC4_correction.captured.txt` from the c7 fact plus
double-counting, and the capture's own analytic argument) is:

    true induced C4 = (1/2)·C(μ,2)·#nonedges = #nonedges/2 = v·k·(k-2)/8

Hence the true induced-C4 family sequence is **half** the tabulated one:

    nonedges   vk(k-2)/4 : 18,  4158,   26730,  19320840, 121781611728
    true ic4   vk(k-2)/8 :  9,  2079,   13365,   9660420,  60890805864

`oeis_lookup` on the true induced-C4 sequence: **no match** (new, distinct miss).
At 99 the forced value is **2079** induced C4 (not 4158 as the mislabelled
capture implies). This does not change any structural conclusion — it is still a
parameter-determined count that survives on both controls — but the earlier
capture's number would mislead a downstream reader, so the correction is recorded
here and in a scratch note.

**Independent re-verification of the correction** (`code/out/pattern_finder_ic4_verify.py`):
rook(3) brute-forces 9 induced C4 (= 9·4·2/8, match True); BvLS direct common-
neighbour sweep gives nonedges/2 = 13365 (= 243·22·20/8, match True), with the
c7 fact (common neighbours of a nonedge pair nonadjacent) asserted throughout.
Both controls reproduce v·k·(k-2)/8 exactly.

## Confirmed non-patterns (no exploitable regularity)

- The n3-seed radius survivor trace `[1,2,5,11,19,19,19]` is a mechanism trace
  (complete-but-capped enumeration), not an indexed sequence with a definable
  extrapolation; radius 6 is a stable fixpoint (19 survivors, all free bits 0),
  so the seed extends locally to every radius. No local obstruction; confirmed
  exact in `n3_grow_radius.captured.txt`.
- The incidence p-rank values (rook 5, doily 10, GQ 27 → 21, BvLS 243/231) are
  4 distinct-parameter measurements, not an indexed sequence; round 21 exposed
  the generic-overfit of any low-order fit. No separation (and none proveable
  without a second srg(99,14,1,2)).
- The n3-join histogram {3:·, 4:·} and {0,1,3,4:·} distributions are
  single-graph facts, not sequences.

## The exact verdict (unchanged across 30 rounds, now re-derived this round)

**Every** on-disk integer sequence of structural significance is one of:
1. a divisor-63-governed polynomial in u (or a rational function integer-valued
   exactly at the feasible index points) — **parameter-determined**, holding for
   ANY member of the family, so it cannot separate 99 from the two existing
   controls 9 and 243 (both of which are in the family and force the same
   closed form); or
2. a mechanism/enumeration trace with no first falsifying term; or
3. a small list of p-rank/SNF measurements at distinct parameter points, not an
   indexed sequence.

**No sequence on disk separates srg(99,14,1,2) from its controls.** Every number
a nonexistence argument would compute at 99 (2079 induced C4, 33264 induced C5,
209286 hexagons, 231 triangles, n3-cap 4158, coclique 22, degree/multiplicity
values) is already determined by the parameters and is attained (with the same
form) by rook(3) and BvLS. The genuinely 99-specific structural values remain
the **coclique bound 22** and the forced **1 ≤ n₃ ≤ 4158** (Makhnev conditional
+ order-6 cap) — individual values, not sequence lines.

## What would falsify this

- A 6th feasible family member does not exist (next candidate a=129∤63 by the
  a|63 integrality theorem), so no family sequence has a computable 6th term to
  test a closed form against — the closed forms are exhaustive over the family.
- Any count that **differed** at 99 from its parameter-determined value would be
  a genuine finding; but because 99 is μ=2 like rook/BvLS, both controls force
  the same value, so no such count can exist that the two controls already
  saturate.

## Files

- `code/out/pattern_finder_verify_closed_forms.py` — triangles/C5/coclique/
  multiplicities exact sympy verification (values match recorded tables).
- `code/out/pattern_finder_degree_census.py` — the in-u degree census above.
- `code/out/pattern_finder_true_ic4.py` — the corrected induced-C4 sequence.
- This report.
