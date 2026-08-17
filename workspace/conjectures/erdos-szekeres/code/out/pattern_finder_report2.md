# Pattern-finder: sequences extracted from the run's computed data (round 2)

Sequence tools run over the exact oracle's output on the VERIFIED `es_construct`
construction. All values exact; every regularity labelled as proved / conjectured.

## 1. Transversal-convexity — the one NEW structural finding (conjecture, exact n=4..9)

**Claim.** In the verified ES construction X_n (2^{n-2} points, blocks T_i of
size C(n-2,i), no convex n-gon), EVERY full transversal — choosing exactly one
point from each block — lies in **convex position**. Consequently the number of
`(n-1)`-convex subsets that are full transversals equals the total number of full
transversals, `prod_i C(n-2,i) = OEIS A001142(n-2)`.

**Numbers (exact, computed).**
| n | full transversals | all convex? |
|---|---|---|
| 4 | 2  | yes |
| 5 | 9  | yes |
| 6 | 96 | yes |
| 7 | 2500 | yes |
| 8 | 162000 | yes (transversal_convex_n8.py, EXIT 0, zero non-convex) |
| 9 | 26471025 | yes (transversal_convex_n9.py, EXIT 0, zero non-convex) |

- n=4..7 from `seq_extract.py` (full transversal counts 2,9,96,2500 = A001142(n-2),
  all convex via `lib.es_geom.in_convex_position`).
- n=8 out-of-sample (likely-uniform-scaling argument): 162,000 transversals, 0 non-convex.
- n=9 (beyond the suggesting data): 26.47M transversals, 0 non-convex, using exact
  integer-scaled coordinates (uniform scale by lcm — a sign-preserving identity, so
  the arithmetic is exact and matches the Fraction oracle, checked on 3000 random
  transversals).

**Status: CONJECTURE with exact evidence n=4..9, structural reason known.** The
blocks are minuscule clusters (width ~1e-5, height ~1e-7) around centers spread
~1000 apart on a strictly (downward-)convex arc; the outer convex hull of X_n is
exactly one point per block in block order (Conjecture A, PASS at n=5,6,7). A
"sufficiently tiny clusters on a strictly convex arc ⟹ every transversal convex"
lemma would be the general proof. First falsifier: a non-convex transversal at any
n — not found through n=9; n≥10 unchecked (and enumeration cost grows as prod
C(n-2,i)). Whether this is a theorem or an artifact of es_construct's specific
tiny-scale placement is open, but the geometry makes the general lemma plausible.

## 2. gsplit valid-split counts (proved/computed, provenance reproduced)

Rotating-line exact enumerator on es_construct: n=4..7 → **[6, 4, 2, 0]**.
- Reproduced with provenance (EXIT 0) via `gsplit_seq.py` and `seq_extract.py`.
- The n=4 value 6 is new and completes the sequence (prior captures only had n=5,6,7).
- Constant difference −2 (arithmetic progression 12−2n) until n=7 hits 0: no line
  splits X_7 into two (n-1)-avoiding halves of size 16. Scoped to this template;
  consistent with the run's n7-zero finding.
- A000051/A094373 (power-of-two+1) and similar canned sequences do NOT appear here;
  this is a short 4-term arithmetic decay to 0, not a catalogued combinatorial count.

## 3. Distinct (n-1)-convex-subset counts — NOT catalogued (record as dead thread)

`4, 38, 802, 39648` for n=4..7.
- `find_linear_recurrence` (order ≤2): none.
- OEIS: **no match** (recorded so nobody re-searches). Growth ratio ~21·49 argues
  super-exponential; the leading term is dominated by the transversal count
  A001142(n-2) (they coincide at n=4: both 4; thereafter the non-transversal
  convex subsets dominate: 38−9=29, 802−96=706, 39648−2500=37148).

## 4. Block-tightness identity (checked, n=3..11; fails at n=12 in impl.)

Every interior block T_i of X_n achieves longest_cup = n−i−1 and longest_cap =
i+1, so cup+cap = n. Verified exactly at n=3..11; the `cupcap`/`es_block`
implementation violates it first at n=12 (cupcap(8,6) gives cup=8 against bound
≤7). Already recorded in `block_tightness_claim.md`; this run's data agrees
(block_tightness.py: cup_i+i = n constant for interior blocks, n=3..7).

## What is NOT structure (reported so nobody re-derives)

- Onion layer sizes [3,1],[4,4],[5,5,3,3],[6,6,6,5,6,3] — artifact of the radial
  placement, no clean sequence (already in pattern_finder_report).
- The reversal-depth statistic from the allowable-sequence encoder is a CONSTANT
  N−1 for every point (allseq_adjudicate TEST 2): the length-N−1 equality kills the
  "depth = block index" hope, refuted.

## Conjecture to attack next

The transversal-convexity lemma is the strongest candidate: it is exact on the
one verified construction through n=9 and has a clear geometric proof sketch
(tiny clusters on a strictly convex arc). Deriving it would turn an enumeration
(counting convex (n-1)-subsets) into an evaluation for the construction, and
clarifies how the extremal template carries its (n-1)-subsets. The chief
caveat: transversals are only a corner of the (n-1)-convex subsets (the
majority are non-transversal), so proving it does not directly bound ES(n).
