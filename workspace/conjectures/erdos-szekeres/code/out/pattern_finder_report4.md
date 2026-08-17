# Pattern-finder report (round 4): realized pattern-class count = triangular numbers

## Deliverable

A **new exact structural regularity** of the verified ES extremal template
`es_construct`, distinct from every finding previously recorded.

## The finding

For es_construct(n) (N = 2^{n-2} points, blocks T_0..T_{n-2}, |T_i| = C(n-2,i),
no convex n-gon), the number of **distinct realized block-pattern classes** among
the (n-1)-convex subsets equals the **triangular number C(n-1,2) = C(#blocks,2)**:

- n=4: 3 classes (of 3 blocks)
- n=5: 6 classes (of 4 blocks)
- n=6: 10 classes (of 5 blocks)
- n=7: 15 classes (of 6 blocks)
- n=8: 21 classes (of 7 blocks, sampled)

Verified **exactly and exhaustively for n=4..7** (all C(N,n-1) subsets, exact
`lib.es_geom.in_convex_position`, `code/out/pattern_class_count.py` EXIT 0;
906,192 subsets at n=7). At n=8 (C(64,7) ≈ 621M too large to enumerate) a
candidate-pattern sampling (`pattern_class_n8_direct.py`, 874 patterns × 150
realizations, EXIT 0) found exactly 21 = C(7,2) — supportive, under-count-proof,
not exhaustive.

## Sequence table

- `analyze_sequence([3,6,10,15,21])`: degree-2 poly, constant 2nd differences 1,
  ratios 2.0/1.67/1.5/1.4 — exactly the shape of C(n-1,2).
- `oeis_lookup([3,6,10,15])`: **A000217 triangular numbers** — exact catalogued
  match.
- The length-2 rational "recurrence" the linear-recurrence tool returned is a
  meaningless over-fit for a binomial; not cited.

## Why it is distinct from the six-FULL-pattern finding

FULL patterns = patterns where *every* realizing (n-1)-subset is convex: exactly
six (n=5..8), a subfamily. Realized classes = patterns with *at least one* convex
realization: C(n-1,2) of them. Different quantities; the present count (3,6,10,15,21)
is genuinely new and not in run memory (checked via relate_memory — only the
6-FULL family is recorded).

## Structure in the exact lists

- **Reversal symmetry** under block-index involution i -> (n-2)-i: holds in every
  exact list (n=5,6,7 shown in the claim file).
- All-ones (full-transversal) pattern always realized (consistent with the proven
  transversal-convexity).
- All realized classes are "mountain" profiles: leading 1s, then one or two bumped
  blocks taking ≥2, trailing 0s. Plausible bijection: realized class <-> unordered
  block pair (the two cut blocks pinning the unique monotone profile). **This
  bijection is NOT established** — stated as the structural explanation to attack.

## Status

Conjecture, exact n=4..7 (exhaustive), sampled-support n=8. First falsifier: a
realized class at n=8 beyond the 21, or count ≠ C(n-1,2) at some n. The bearing is
descriptive of the extremal template (does not by itself bound ES(n)); it gives a
compact parameterization of the block-shape diversity of the extremal yardstick.

## Files

- `code/out/pattern_class_count.py` — exact exhaustive n=4..7 (EXIT 0).
- `code/out/pattern_class_n8_direct.py` — n=8 candidate-pattern sampling (EXIT 0).
- `code/out/pattern_class_triangular_claim.md` — full claim note (claim id
  `es-construct-realized-pattern-classes-triangular`, status conjecture).

Note: the Cognee memory server was down during this round (remember_memory /
note_scratch both refused). The finding is therefore recorded in the workspace
claim file and INDEX — to be promoted to durable memory once the server recovers.
Per the steering directive, workspace write was used as the fallback rather than
silently dropping the content.
