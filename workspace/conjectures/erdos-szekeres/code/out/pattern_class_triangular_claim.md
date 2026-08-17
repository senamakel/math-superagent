# Realized block-pattern classes of (n-1)-convex subsets = triangular numbers

## The finding (NEW, conjecture)

For the verified ES construction `lib.es_construct(n)` (N = 2^{n-2} points in
blocks T_0..T_{n-2}, |T_i| = C(n-2,i), no convex n-gon), consider the
(n-1)-convex subsets (largest convex subsets; size n-1). Each such subset has a
**block-count pattern** c = (c_0,...,c_{n-2}), c_i = how many points it takes
from block T_i. Call a pattern **realized** if at least one (n-1)-convex subset
realizes it.

**The number of distinct realized block-pattern classes is exactly the
triangular number C(n-1,2) = C(#blocks, 2):**

| n | #blocks = n-1 | realized classes | C(n-1,2) |
|---|---|---|---|
| 4 | 3 | 3 | 3 |
| 5 | 4 | 6 | 6 |
| 6 | 5 | 10 | 10 |
| 7 | 6 | 15 | 15 |
| 8 | 7 | 21 | 21 |

- n=4..7: **exact and exhaustive** — every (n-1)-subset enumerated with the
  exact `lib.es_geom.in_convex_position` oracle (`code/out/pattern_class_count.py`,
  EXIT 0; C(32,6)=906,192 subsets at n=7).
- n=8: **sampled/supportive**, not exhaustive (C(64,7) ≈ 621M too large). Used a
  candidate-pattern enumeration (874 patterns with sum 7) each sampled K=150
  realizations; found exactly 21 = C(7,2) realized classes
  (`code/out/pattern_class_n8_direct.py`, EXIT 0). Sampling can only *under*-
  count, so at least 21; if the conjecture holds, exactly 21. This is supportive
  evidence, not a proof.

## Exact lists (realized classes, exhaustive n=5,6,7)

n=5 (4 blocks, 3 pts): (0,0,3,1),(0,2,1,1),(0,2,2,0),(1,1,1,1),(1,1,2,0),(1,3,0,0)

n=6 (5 blocks, 4 pts): (0,0,0,4,1),(0,0,3,1,1),(0,0,3,2,0),(0,2,1,1,1),
(0,2,1,2,0),(0,2,3,0,0),(1,1,1,1,1),(1,1,1,2,0),(1,1,3,0,0),(1,4,0,0,0)

n=7 (6 blocks, 5 pts): (0,0,0,0,5,1),(0,0,0,4,1,1),(0,0,0,4,2,0),(0,0,3,1,1,1),
(0,0,3,1,2,0),(0,0,3,3,0,0),(0,2,1,1,1,1),(0,2,1,1,2,0),(0,2,1,3,0,0),
(0,2,4,0,0,0),(1,1,1,1,1,1),(1,1,1,1,2,0),(1,1,1,3,0,0),(1,1,4,0,0,0),(1,5,0,0,0,0)

## Structure observed in the lists

- **Reversal symmetry:** pattern c realized iff reversal(c) realized (block-index
  involution i -> (n-2)-i). Holds in every exact list.
- The all-ones pattern (1,...,1) = the full-transversal pattern (pattern C) is
  always realized (transversal-convexity, an earlier verified claim).
- Each realized class has the "mountain" shape: 0s then a descending/staircase
  profile with at most the two spike blocks taking 2+ points, everything else
  taking 0 or 1. The leading-1 chain (1,...,1,S,0,...,0) for S = block count of
  one bumped block) and its reversals, plus the two-spike patterns.
- The triangular count C(#blocks,2) invites a bijection with unordered pairs of
  blocks: the realized pattern is plausibly the unique monotone profile pinned by
  two "cut" blocks. *This bijection is NOT yet established* — stated here as the
  likely structural explanation to attack.

## Status

**CONJECTURE** (proved exactly n=4..7 via exhaustive exact enumeration; supported
at n=8 by direct sampling finding exactly 21). First falsifier: a realized pattern
class at n=8 beyond the 21, or a count ≠ C(n-1,2) at any n. Since C(64,7) is too
large to enumerate here, the n=8 side is not closed — an exhaustive-or-never
settlement would need smarter isomorph rejection or SAT.

## Relation to the prior FULL-pattern finding (distinct quantity)

The earlier finding (`es-construct-six-full-patterns`) counts patterns where
*every* realizing subset is convex (the six FULL patterns A,B,C,D,E,F). The
present finding counts patterns with *at least one* convex realization. These are
different: at n=6 there are 10 realized classes but only 6 FULL; at n=8, 21
realized but 6 FULL. The two are consistent — the 6 FULL patterns are a subfamily
of the C(n-1,2) realized classes.

## Tools run

- `analyze_sequence([3,6,10,15,21])`: degree-2 polynomial, constant 2nd
  differences = 1, ratios 2.0,1.667,1.5,1.4 — consistent with C(n-1,2).
- `find_linear_recurrence`: order-2 rational fit (5/2 a(n-1) - 5/3 a(n-2)),
  a meaningless over-fit for a binomial; not cited.
- `oeis_lookup([3,6,10,15])`: **A000217 triangular numbers** C(n+1,2) — the
  exact catalogued match (also C(#blocks,2) = C(n-1,2)).

## Bearing

A clean, exact structural regularity of the extremal ES template: the (n-1)-convex
subsets of X_n occupy exactly C(n-1,2) distinct block-sparsity shapes, parameterized
(as conjectured) by an unordered pair of blocks. This is descriptive of
es_construct (it does not by itself bound ES(n)), but it pins down the block-shape
diversity of the extremal yardstick and constrains any bijective/compression
account of the construction's convex subsets.

```claim
id: es-construct-realized-pattern-classes-triangular
statement: In the verified es_construct ES construction X_n (n=4,5,6,7 exact; n=8 sampled), the number of distinct block-count patterns realized by (n-1)-convex subsets equals C(n-1,2) = C(#blocks,2), the triangular numbers 3,6,10,15,(21). Every realized pattern is reversal-symmetric under block-index involution. Conjecture.
hypotheses: the es_construct exact-rational placement; n in {4,5,6,7} for the exact claim, n=8 supportive (sampled, C(64,7) too large to enumerate).
holds-here: yes — run's own verified lower-bound construction; exact via lib/es_geom.
status: conjecture (exact exhaustive n=4..7; n=8 sampled-support)
bearing: GOAL 2/4 structural description of the extremal template; distinct from the 6-FULL-pattern finding. Proposed structural explanation (unproven): bijection with unordered pairs of blocks (the unique monotone profile pinned by two cut blocks).
anchor: code/out/pattern_class_count.py (exact), code/out/pattern_class_n8_direct.py (n=8 sampled)
```
