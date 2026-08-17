# es_construct: the six FULL patterns = corner-block-pair patterns (unified finding)

## Background (two established findings this unifies)

**F1 — realized-pattern bijection** (claim `es-construct-realized-pattern-bijection`).
For es_construct(n), B = n-1 blocks. The realized (n-1)-convex block patterns are
exactly the C(B,2) profiles pinned by an unordered block pair {L,R}, 0 <= L < R <= B-1:

```
c_i = 0      for i < L or i > R
c_L = L + 1
c_R = B - R
c_i = 1      for L < i < R
```

sum = B = n-1. (Exact exhaustive n=4..7, sampled n=8.)

**F2 — the six FULL patterns** (claim `es-construct-six-full-patterns`). Among these
realized patterns, exactly six have the property that EVERY realizing (n-1)-subset is
in convex position ("FULL"); every other pattern has a non-convex realization. (Exact
n=5..8, n=9 sampled.)

## NEW finding (this check): which six?

The six FULL patterns are EXACTLY the realized patterns whose pinning pair {L,R} has
BOTH endpoints in the **corner-block set**

```
CO = {0, 1, n-3, n-2}
```

(the two interior blocks adjacent to the endpoint singletons, plus the two endpoints).
Since CO has 4 blocks, there are C(4,2) = 6 such pairs — which is WHY the count is
exactly six.

Concrete example n=6 (B=5, blocks 0..4, CO={0,1,3,4}): the six FULL patterns are the
pairs (0,1),(0,3),(0,4),(1,3),(1,4),(3,4) — exactly the pairs with both ends in CO.
The four non-FULL realized patterns are (2,3),(2,4),(1,2),(0,2) — pairs whose smaller
(c_2=3-bumped) endpoint L or R involves the strictly-interior block index 2.

## Verification (exact, exhaustive)

`code/out/pat_corner_full_check.py`, EXIT 0, exact `lib/es_geom.in_convex_position`,
all C(N,n-1) subsets enumerated at n=5,6,7 (n=7: C(32,6)=906,192):

| n | B | CO | #FULL | all full_pairs in corner set? | corner pairs all FULL? | verdict |
|---|---|---|---|---|---|---|
| 5 | 4 | {0,1,2,3} | 6 | yes (all 6 pairs) | all 6 | FULL==corner-pairs: True |
| 6 | 5 | {0,1,3,4} | 6 | yes (6 of 6) | all 6 | FULL==corner-pairs: True |
| 7 | 6 | {0,1,4,5} | 6 | yes (6 of 6) | all 6 | FULL==corner-pairs: True |

(At n=5, CO is the whole block set, so all C(4,2)=6 realized patterns are FULL —
consistent with the exhaustive n=5 record where indeed every realized pattern is FULL
and total distinct convex subsets = 38 = all patterns. This is the degenerate n where
the 4 blocks are all "corner"; the strict exclusion of the strictly-interior blocks
only takes over at n>=6.)

## Status

**CONJECTURE** — exact exhaustive n=5,6,7. First falsifier: a FULL pattern whose
pinning pair has an interior endpoint in {2..n-4}, or a corner-pair pattern that is not
FULL, at any n. Not found through n=7. n=8 would need C(64,7)~621M enumeration
(too large) — the six known FULL patterns at n=8 all have pairs (from the pattern lists:
A=(0,5), B=(0,B-2)? etc.) so the corner-pair set that is fully realizable at n=8 is
consistent, but un-exhausted.

## Bearing

This is a descriptive structural lemma about the extremal template (GOAL 2/4): it gives
the exact boundary of which block sparsity patterns the (n-1)-convex subsets of the
extremal construction may take with full convexity, expressed as an endpoint-confinement
condition on the pinning pair. It does NOT by itself bound ES(n) — it describes
es_construct only — but it is the exact parameterization of the extremal yardstick and
shows the two previously-separate findings (bijection, six-FULL) are the same structure
viewed by count vs by convexity.

## Files
- `code/out/pat_corner_full_check.py` (verifier, EXIT 0)
- `code/out/pattern_family_claim.md` (F2), `code/out/pattern_bijection_claim.md` (F1)

## False lead recorded (do not re-derive)
The split-gon spectrum's "max union size" / "paper max split-k" = 6,8,10 at n=5,6,7
are the trivial arithmetic 2n-4: the whole set has longest cup AND cap both of size
n-1 (verified via chains_by_rightmost: max cap = max cup = n-1), sharing the rightmost
point, so max union = 2(n-1) - overlap = 2n-4. Not new structure.
