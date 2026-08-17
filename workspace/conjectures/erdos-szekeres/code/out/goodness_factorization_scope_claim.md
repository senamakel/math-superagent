# Per-block goodness factorization: scope-survival test (steer directive)

## The steer request

The goodness factorization produced exact per-block functions g_0..g_5 that
factorize the total (n-1)-convex-subset count, with palindromic symmetry
g_i = g_{(n-2)-i}. The steer asks to (a) capture it with the capture idiom,
(b) write the claim with its scope, and (c) — the deciding question — whether
the factorization survives on sets that are NOT this construction, before
building anything on it.

## Captures (clean, EXIT 0, safe idiom)

- `code/out/goodness_recovered.captured.txt` — the recorded g-values, EXIT 0.
- `code/out/factorization_survival.captured.txt` — the deciding survival test.

## The factorization (exact, n=4..7)

For es_construct(n) (2^{n-2} points, blocks T_0..T_{n-2}, |T_i|=C(n-2,i)):

```
n=4 g_0..g_2: {0:1,1:1} {0:1,1:2,2:1} {0:1,1:1}         total 4
n=5 g:         {0:1,1:1} {0:1,1:3,2:3,3:1}^2 {0:1,1:1}  total 38
n=6 g_1=g_3:   {0:1,1:4,2:6,4:1};  g_2: {0:1,1:6,3:10}   total 802
n=7 g_1=g_4:   {0:1,1:5,2:10,5:1}; g_2=g_3:{0:1,1:10,3:46,4:41} total 39648
```

Palindromic symmetry g_i = g_{(n-2)-i} holds in every exact list. The
all-patterns-factorized flag is True at n=4..7 (prod_i g_i(c_i) == exact count
for EVERY block pattern).

## The deciding question: does it survive off the construction?

**Test (n=6, then n=7, exact)** — keep the SAME blocks, change only placement:

| placement | total convex | patterns | factorization | g values |
|---|---|---|---|---|
| ARC (es_construct's own) | 802 | 10 | **True** | recorded (identical) |
| STAIRCASE (x=+i, y=-i, steep negative cross-slopes) | 802 | 10 | **True** | **identical** to arc |
| SCRAMBLED (y-centres off the arc) | 1464 | 30 | **False** | mismatches: (0,0,2,3,0) 60≠24, (0,0,3,2,0) 60≠6, ... |

**n=7 confirmation (factorization_staircase_n7.py, EXIT 0, exact C(32,6)=906192):** the
staircase placement reproduces the arc placement *exactly* — total 39648, 15 patterns,
factorization=True on both, and **g values identical arc vs staircase**, including the
distinctive n=7 middle-block g_2=g_3={0:1,1:10,3:46,4:41} and g_1=g_4={0:1,1:5,2:10,5:1}.
So the placement-invariance across ES-consistent placements holds at n=6 AND n=7.

So:
- The factorization **holds on both ES-consistent placements** (convex-arc and
  staircase), with **identical g values and identical totals** — it is
  placement-invariant across the ES-consistent (convex-corridor) family, not an
  artifact of the arc coordinates per se.
- It **breaks** when the convexity corridor is destroyed (scrambled y): 30
  patterns, per-block product no longer equals counts. So it is **not** a
  property of the abstract block decomposition alone.

## Scope of the claim (what it does and does not say)

**Holds:** the factorization is a real regularity of the es_construct extremal
template and of any placement keeping block one-per-point on a convex corridor
(convex arc OR staircase). Exact n=4..7 (n=6,7 verified on both placements with
identical g); n=8 supportive by sampling.

**Does not hold (this is the boundary):** on a general placement of the same
blocks that breaks the convexity corridor, the per-block product factorization
fails. Therefore it does NOT characterize abstract n-avoiding sets or general
block decompositions — it characterizes ES-consistent (convex-corridor)
placements.

**Deciding consequence for the question "is it a discovery or an artifact":**
It is a *structural property of the ES template family*, not of the general
configuration space. It cannot by itself be used to bound ES(n), because the
failure on scrambled placements shows the factorization depends on the convex
corridor, which is exactly the placement structure the ES construction (not an
arbitrary n-avoiding set) posits. This matches the earlier transversal-convexity
finding (report3): those template properties are placement-corridor artifacts,
correctly scoped to the construction.

## OEIS (negative results, recorded so nobody re-searches)

- `[1,10,46,41]` (the distinctive n=7 middle-block goodness g for c=3,4) — **no
  OEIS entry**.
- `[4,38,802,39648]` (total (n-1)-convex-subset count) — **no OEIS entry**.
- `[3,6,10,15,21]` (realized pattern-class count) — OEIS A000217 triangular
  numbers, the catalogued C(n-1,2) (recorded in prior rounds).

## Sequence-tool verdicts on the key sequences (exact, conjectures)

| sequence | tool verdict |
|---|---|
| [6,4,2,0] gsplit valid splits n=4..7 | degree-1 poly, const diff −2; trivial 12−2n, matches n7-zero |
| [3,6,10,15,21] realized classes | degree-2 poly, 2nd diff 1 → C(n-1,2) = A000217 |
| [2,9,96,2500,162000,26471025] full transversals | A001142(n-2)=prod C(n-2,i), proved identity |
| [4,38,802,39648] distinct convex subsets | not low-degree poly, no linear recurrence, OEIS miss |
| [1,10,46,41] n=7 middle-block g | no linear recurrence, OEIS miss |

All arithmetic exact (Fraction/integer determinants via lib.es_geom); all fits
are conjectures over the supplied terms, not proofs of continuation.

## Status

CONJECTURE (exact n=4..7): the block-pattern count factorization with
per-block goodness g_i and palindromic symmetry holds for es_construct and for
all ES-consistent (convex-corridor/staircase) placements of its blocks (verified
identical g and totals at n=6 and n=7), and FAILS on corridor-breaking
placements (verified at n=6). First falsifier beyond the recorded range: a
non-factorizing pattern or different g at some n≥8 on any convex-corridor
placement (n=8 supportive only). The deciding question has been asked and
answered: the factorization does not survive on arbitrary placements, so it is a
template/placement property, not a general n-avoiding-set invariant. Captures:
code/out/goodness_recovered.captured.txt, code/out/factorization_survival.captured.txt,
code/out/factorization_staircase_n7.captured.txt.
