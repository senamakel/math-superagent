# Realized (n-1)-convex block patterns of es_construct = pairs of blocks (explicit bijection)

## Finding (NEW, conjecture upgraded to explicit bijection)

**Background (report4, claim `es-construct-realized-pattern-classes-triangular`).** In the
verified ES construction `lib.es_construct(n)` (N = 2^{n-2} points in blocks T_0..T_{n-2},
|T_i| = C(n-2,i), no convex n-gon), the number of **distinct realized block-count patterns**
among the (n-1)-convex subsets equals the triangular number C(n-1,2). That was a *count*
conjecture; the structural explanation (bijection with unordered pairs of blocks) was left
**NOT established**.

**This note makes the bijection explicit and verifies it.** A realized pattern is exactly one
of the C(B,2) profiles (B = n-1 blocks), indexed by an unordered pair of blocks {L,R},
0 ≤ L < R ≤ B-1:

```
c_i = 0        for i < L  or  i > R
c_L = L + 1
c_R = B - R
c_i = 1        for L < i < R
```

Sum: (L+1) + (R−L−1)·1 + (B−R) = B = n−1 ✓ (the right (n-1) total size).

## Verification (exact, exhaustive at n=4..7; sampled at n=8)

`code/out/pattern_bijection_check.py`, EXIT 0, exact `lib/es_geom.in_convex_position`:

| n | B | realized | C(B,2) | formula | missing | spurious | verdict |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 3 | 3 | 3 | 0 | 0 | PASS |
| 5 | 4 | 6 | 6 | 6 | 0 | 0 | PASS |
| 6 | 5 | 10 | 10 | 10 | 0 | 0 | PASS |
| 7 | 6 | 15 | 15 | 15 | 0 | 0 | PASS |
| 8 | 7 | 21 (sample) | 21 | 21 | 0 | 0 | supportive |

At n=4..7 every C(N,n-1) subset was enumerated exactly (n=7: C(32,6)=906,192); the realized
set equals the formula set exactly (zero missing, zero spurious). At n=8 (C(64,7)≈621M too
large) all 21 formula patterns were found realized by sampling — directional support.

## SANITY of the formula against the exhaustive lists

Every pattern in the exact lists of `code/out/maxconvex_structure.captured.txt` / report4
must match the formula. Example n=6 (B=5, blocks 0..4): formula pairs →
  {0,1}: (1,B-1,0,0,0)=(1,4,0,0,0) ✓ [pattern (1,4,0,0,0)]
  {0,2}: (1,1,B-2,0,0)=(1,1,3,0,0) ✓
  {0,3}: (1,1,1,2,0) ✓   {0,4}: (1,1,1,1,1) ✓ (full transversal)
  {1,2}: (0,2,3,0,0) ✓   {1,3}: (0,2,1,2,0) ✓   {1,4}: (0,2,1,1,1) ✓
  {2,3}: (0,0,3,2,0) ✓   {2,4}: (0,0,3,1,1) ✓   {3,4}: (0,0,0,4,1) ✓
  → the 10 patterns of the n=6 exhaustive list, each exactly once. Reversal symmetry
  {L,R} → {B-1-R, B-1-L} and the full-transversal profile {0,B-1}=(1,…,1) are immediate.

## Status

**CONJECTURE** (exact exhaustive n=4..7, sampled-support n=8). It upgrades the triangular
*count* to an exact *classification*: there is a bijection between realized block shapes and
unordered pairs of blocks, with a closed-form profile. First falsifier: a realized (n-1)-convex
pattern at any n outside the formula set, or a formula pattern never realized. Bearing is
descriptive of the extremal template (does not by itself bound ES(n)), but it is the exact
parameterization of the block-shape diversity of the extremal yardstick, and the closed form
turns the enumeration of realized classes into an evaluation for the construction.

```claim
id: es-construct-realized-pattern-bijection
statement: In the verified es_construct ES construction X_n (n=4,5,6,7 exact; n=8 sampled), the realized block-count patterns of (n-1)-convex subsets are exactly the C(B,2) profiles c_L=L+1, c_R=B-R (0<=L<R<=B-1, B=n-1), c_i=1 between, 0 outside; sum = n-1. Equivalently a bijection realized-pattern <-> unordered block pair. Every profile is realized; nothing else is.
hypotheses: the es_construct exact-rational placement; n in {4,5,6,7} exhaustive, n=8 sampled.
holds-here: yes — run's own verified lower-bound construction; exact via lib/es_geom.
status: conjecture (exact exhaustive n=4..7; n=8 sampled-support)
bearing: GOAL 2/4 — exact parameterization of the block-shape diversity of the (n-1)-convex subsets of the extremal template; upgrades the count C(n-1,2) to an explicit closed-form classification. Descriptive of es_construct; does not by itself bound ES(n).
anchor: code/out/pattern_bijection_check.py (EXIT 0), code/out/maxconvex_structure.captured.txt
```

## Recorded while memory server was down

Cognee (note_scratch / remember_memory) refused during this run; per the steering directive the
finding is recorded in this workspace claim file and should be promoted to durable memory when
the server recovers.
