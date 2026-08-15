# R-depth-k-finite is REFUTED: S_k is not finite over unbounded even gaps

## target

`R-depth-k-finite` (depth-survival-ladder) — research/weakened/depth-survival-ladder.md:

> "For every fixed k ≥ 1, the set S_k of gap words (2, g_2, ..., g_k) with
> all g_i even positive satisfying A_k(1) ∈ {0,2} is FINITE: each gap is
> bounded by an explicit function of the others and k (a nested absolute value
> is bounded above by the maximum gap, and the condition A_k(1) ≤ 2 forces
> each gap below a computable bound)."

## the refuting family (k = 3)

The ladder's own defining formulas (verbatim):

```
A_2(1) = |g_1 - g_2|
A_3(1) = ||g_1 - g_2| - |g_2 - g_3||
```

Fix g_1 = 2 and g_3 = 2, and let g_2 = 2M run over all even positive integers.
Then, by |a − b| = |b − a|, both inner absolute values are the same quantity
X = |2 − 2M| = 2M − 2, so

```
A_3(1) = ||2 - 2M| - |2M - 2|| = |X - X| = 0  ∈  {0,2}.
```

Hence **(2, 2M, 2) ∈ S_3 for every M ≥ 1**: infinitely many distinct gap words,
with g_2 unbounded while g_1, g_3 and k = 3 are all fixed.

Concrete check (M = 3, g_2 = 6): A_1 = (1,2,6,2), A_2 = (1,4,4),
A_3 = (3,0), so A_3(1) = 0 ∈ {0,2}.

## why this is a genuine counterexample

- g_1, g_3, k are all fixed (2, 2, 3).
- g_2 is unbounded: no function of the fixed data bounds it.
- This directly contradicts "each gap is bounded by an explicit function of the
  others and k" and the asserted finiteness of S_k (instantiated at k = 3).

The intuition the rung gave — "A_nested ≤ max gap, and A_k(1) ≤ 2 forces each
gap below a computable bound" — is simply wrong: bounding A_3(1) ≤ 2 does NOT
bound g_2, because g_2 cancels exactly when g_1 = g_3 (a nested absolute of two
equal quantities is 0 regardless of how large the common distance is). This is
the degenerate "two things coincide" case (g_1 = g_3).

## checking

The formula reading was validated against the real primes: prime gap prefix
(2,2,4) gives A_3(1) = ||2−2|−|2−4|| = 2, matching problem.md's real
A_3 = (1,2,0,0,...), A_3(1) = 2. The cancellation is pure |a−b|=|b−a| algebra,
which holds for all naturals — no search needed (an infinite family cannot be
exhibited by a finite model finder; that is exactly why the elementary identity
is the right tool here).

## claim

```claim
id: depth-k-finite-refuted
statement: R-depth-k-finite is FALSE. For fixed k=3, g_1=2, g_3=2, the family
  (2, 2M, 2) (M >= 1 even) all satisfy A_3(1) = ||2-2M| - |2M-2|| = 0 in
  {0,2}, so (2, 2M, 2) in S_3 for every M: S_3 is INFINITE over unbounded even
  positive gaps, and g_2 is not bounded by any function of g_1, g_3 and k.
  The claim "each gap is bounded by a function of the others and k" fails.
hypotheses: gap word (2, g_2, g_3), all gaps even positive, g_1 = 2 = g_3;
  A_k(1) defined by the ladder's verbatim nested-absolute formulas.
holds-here: yes
status: checked (one-line |a-b|=|b-a| cancellation from the target's own
  defining formula; formula reading validated against problem.md's real row
  A_3(1)=2 for the (2,2,4) prefix). Infinite family, so not exibitable by a
  finite model finder; the algebra is the proof.
bearing: the depth-survival-ladder's stated route "each S_k is finite even
  over unbounded gaps, so depth-k survival is a finite search" is defeated as
  written; the search for S_k is unbounded even at fixed k. The ladder's real
  climb (infinite-horizon via leftward-drift) is untouched, but this specific
  finiteness lemma is refuted and must not be restated as open-with-a-proof.
anchor: code/refute/attack_depth_k_finite.py, code/refute/verify_depth_k_finite.py,
  code/refute/depth_k_finite_claim.p, research/weakened/depth-survival-ladder.md
```

## report to the run

Exact verdict on the target I attacked:

- **statement attacked**: R-depth-k-finite (open rung, depth-survival ladder) —
  the claim that every S_k is finite over unbounded even gaps.
- **answer**: **refuted** — but by an elementary algebraic identity (an
  infinite family), not by a finite model, so `find_counterexample` reports
  `undecided` (it cannot exhibit an infinite set). The one-line witness is the
  genuine content and it is checked against the source formula and the real
  row data.
- size covered: the family is infinite (all even g_2 with g_1=g_3=2); no finite
  bound on g_2 exists, which is precisely what the claim asserted.
