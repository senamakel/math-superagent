# Full block-count patterns of the (n-1)-convex subsets of es_construct(n)

Computed against the VERIFIED `lib.es_construct` ES lower-bound construction and
the exact `lib.es_geom.in_convex_position` oracle (integer/Fraction arithmetic,
never floating point).

## The finding

For n = 5, 6, 7, 8, among all (n-1)-subsets of X_n = es_construct(n), the
**block-count patterns** p = (p_0, ..., p_{n-2}) for which *every* realizing
subset lies in convex position are **exactly six**, and they are
reversal-symmetric under the block-index involution i -> (n-2)-i:

| label | pattern (block sizes C(n-2,0..n-2)) | total realizations |
|---|---|---|
| A | (0, ..., 0, \|T_{n-3}\|, 1) — all of block n-3 + one of block n-2 | 1 |
| B | (1, \|T_1\|, 0, ..., 0) — one of block 0 + all of block 1 | 1 |
| C | (1, 1, ..., 1) — full transversal | prod_i C(n-2,i) = A001142(n-2) |
| D | (0, 2, 1, ..., 1) — two from block 1, one from each of the rest | C(n-2,1)·C(n-2,2)·prod others |
| E | (1, ..., 1, 2, 0) — reversal of D | " |
| F | (0, 2, 1, ..., 1, 2, 0) — two from block 1, two from block n-3, one from each interior | " |

Every other block-count pattern has at least one (n-1)-subset that is NOT in
convex position.

## Evidence

- **n = 5, 6, 7 — exhaustive** (`code/out/pattern_factor.py`, EXIT 0): every
  (n-1)-subset enumerated with the exact oracle; exactly the six FULL patterns,
  all other pattern classes contain a non-convex realization.
- **n = 8 — complete** (`code/out/pattern_complete_n8.py` + `pattern_hm_n8.py`):
  the six candidates are exhaustively all-convex (largest class 1,012,500
  realizations in `pattern_factor_n8.py`); and every one of the other 868
  block-count patterns is proven non-FULL by an explicit non-convex witness
  (867 found directly, the last (0,0,3,1,1,2,0) refuted by the sampled witness
  indices [14,9,19,32,52,62,57]).
- **n = 9 — randomized** (`code/out/pattern_factor_n9.py`, 60,000 samples of
  each of the six, EXIT 0): no non-convex realization found; supportive, not a
  proof.

## Attempts to break it (all failed to refute the six-pattern claim)

- `code/out/pattern_rule_n7.py`: the naive characterization "no strictly-interior
  block (index 2..n-4) takes ≥ 2 points" is too weak — 72 counterexamples at n=7
  (patterns satisfying the rule that are NOT FULL). So the exact characterization
  is NOT a simple bound rule; it is precisely the 6-pattern family.
- n=8 completeness: every non-six pattern has an explicit non-convex witness.

## Status

CONJECTURE with exact evidence through n=8 (complete) and randomized support at
n=9. The structural explanation is the same as for the full-transversal case
(which is pattern C): es_construct's blocks are minuscule clusters placed on a
strictly convex arc, with the hull one-point-per-block in order (Conjecture A);
small perturbations (the ≤2 takes in the end-adjacent blocks, spread over the
rest) stay on the convexity corridor, while taking ≥3 from any block, or taking
2 from a strictly-interior block, breaks out of it.

**First falsifier**: a non-convex realization of any of the six patterns at any
n; not found through n=8 (exhaustive) and n=9 (sampled). The first place a
counterexample could hide beyond the computed range is a pattern class at n≥10,
whose realization counts are too large to enumerate exhaustively here.

## Bearing

GOAL 2/4 structural-family finding about the extremal template: exactly which
block sparsity patterns the (n-1)-convex subsets of the extremal construction may
have. Pattern C is the known transversal-convexity claim; this finding places it
in the complete family and shows the exact boundary (which blocks may take 2).
It does NOT, by itself, bound ES(n) — it describes es_construct only — so it
carries no direct weight on the conjecture; its value is descriptive structural
precision about the extremal set the run uses as its yardstick.

```claim
id: es-construct-six-full-patterns
statement: In the verified es_construct ES construction X_n (n=5,6,7,8), the (n-1)-convex subsets fall by block-count pattern into EXACTLY six FULL patterns (every realization convex): A=(0^{n-3},|T_{n-3}|,1), B=(1,|T_1|,0^{n-3}), C=(1,...,1) full transversal, D=(0,2,1,...,1), E=(1,...,1,2,0), F=(0,2,1,...,1,2,0); reversal-symmetric in block index. Every other block-count pattern has a non-convex realization. First falsifier: a non-convex realization of any of the six at any n (none through n=8 exhaustive, n=9 sampled).
hypotheses: the es_construct exact-rational placement (XOR clusters on a strictly convex arc with Conjecture-A one-per-block hull); n in {5,6,7,8} for the complete claim; exact convexity via lib/es_geom.
holds-here: yes — this is the run's own verified lower-bound construction; the six-pattern family is a per-template structural regularity.
status: checked (exact exhaustive n=5..8; n=9 sampled)
bearing: GOAL 2/4 — the complete description of which block sparsity patterns the (n-1)-convex subsets of the extremal template may have; generalizes the full-transversal claim (pattern C). Descriptive of es_construct; does not by itself bound ES(n).
anchor: code/out/pattern_factor.py, pattern_factor_n8.py, pattern_complete_n8.py, pattern_hm_n8.py, pattern_factor_n9.py, pattern_rule_n7.py
```
