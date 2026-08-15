```approach
idea: coarea-layer-cake-level-decomposition
mechanism: |
  Every integer-valued row decomposes exactly by its level sets (the layer-cake /
  coarea representation of the l1 norm): for non-negative integers a,b,

      |a - b|  =  sum_{t >= 1}  [ [a >= t] XOR [b >= t] ]   (XOR of two bits, value 0 or 1)

  because |a-b| counts the integer levels t lying strictly between min(a,b)+1
  and max(a,b). This is the standard coarea/layer-cake identity
  |a-b| = sum_t |1_{a>=t} - 1_{b>=t}|.

  Apply it cell by cell. Define the nested binary level arrays

      B^t_k(i) = [ A_k(i) >= t ]  (t = 1,2,3,...; nested: B^t ⊇ B^{t+1}).

  Then EXACTLY, for every interior cell:

      A_{k+1}(i) = sum_{t>=1} ( B^t_k(i) XOR B^t_k(i+1) ).

  So the entire nonlinearity of the absolute-difference operator is moved into a
  SUM over layers, each layer contributing a plain XOR of two bits of the
  parent row. This is a genuine change of coordinates: the conjecture A_k(1) in
  {0,2} becomes

      A_k(1) = |A_{k-1}(1) - A_{k-1}(2)| = sum_t ( B^t_{k-1}(1) XOR B^t_{k-1}(2) )
      is in {0,2}  <=>  the two level-set indicators B^t_{k-1}(1), B^t_{k-1}(2)
      agree at all but at most two levels t.

  The leading {0,2} block of row k+1 is exactly the set of positions i where the
  pair (A_k(i), A_k(i+1)) differs in at most two layers — the "thin" part of the
  level-set boundary structure. Regeneration (the (2,4)-event and its jump) is a
  statement about how the nested level boundaries move under the per-layer XOR.

  Why it is not a re-proposal of the dead threshold/percolation/persistence
  lines: level-set-percolation tracked ONE level predicate and needed monotonicity
  of that predicate (it fails); persistent-homology tracked superlevel-set death
  values (it fails on the saddle bookkeeping); borrow-young tracked the binary
  min-branch choice, which throws away the magnitude. Here ALL layers are kept
  simultaneously and the identity is exact — magnitude is recovered as the
  layer-count, so nothing is discarded. This is a transform, not a scalar
  functional, so it does not inherit the scalar-potential non-monotonicity
  deaths; and it is not magnitude-blind, so it does not inherit the
  comparison-word/CA deaths.
status: refuted
killed-by: |
  The layer-cake identity is exact and grounded (Tzanavaris 2025, Amer. Math.
  Monthly, doi:10.1080/00029890.2025.2583888; Federer's coarea formula) — but the
  program it proposes is the already-refuted scalar-potential class, and the
  transform's own aggregate collapses onto the refuted quantity. Three linked
  grounds:
  (1) The natural aggregate sum_t #{i : B^t_k(i) != B^t_k(i+1)} (per-level boundary
      counts summed over levels) = sum_i |A_k(i) - A_k(i+1)| = TV(row k) = the sum
      of entries of row k+1. So the coarea total "level-boundary mass" is exactly
      the total-variation of the parent row — and the total-variation / run-count
      potential class is MACHINE-REFUTED (approach
      total-variation-oscillation-potential; r(T(x)) <= r(x) fails at halved
      (0,0,1,1) -> (0,1,0), 2 runs -> 3, over all 6,725,600 strings of length <= 8).
  (2) Inside the {0,2} block the per-level bits evolve by XOR/Rule 90 (proved,
      rule90-interior-xor), whose run count GROWS (Sierpinski) — so no per-layer
      boundary-count invariant exists in the very regime the conjecture targets.
      Same obstruction that killed level-set-percolation and persistent-homology.
  (3) "A_k(1) in {0,2} iff the two parent entries agree at all but at most two
      levels" is a faithful restatement of the definition A_k(1) = |A_{k-1}(1) -
      A_{k-1}(2)|, not a reduction. Two entries differing by <= 2 is exactly what
      the conjecture asserts.
  No source applies the layer-cake/coarea decomposition to the iterated
  absolute-difference / Ducci / Gilbreath problem (searched; the layer-cake
  literature is about integrals/measure and yields no discrete invariant of this
  operator). See research/notes/grounding-three-candidates-2026.md.
precedent: |
  Id grounded: the identity is the layer-cake/coarea one-dimensional level-set
  version — https://doi.org/10.1080/00029890.2025.2583888 (Tzanavaris,
  "An Elementary Proof of the Layer Cake Representation Theorem", Amer. Math.
  Monthly, 2025); Federer's coarea formula (level-set form), Maly-Swanson-Ziemer,
  Trans. AMS 2002. Not applied to this problem anywhere (searched several angles).
  Run kills: claim refutation in code/out/check_runcount_lemma.captured.txt
  (TV/run-count potential), rule90-interior-xor (per-level runs grow).
first-step: |
  CLOSED BY REFUTATION — do not spend compute. The aggregate and the per-level
  structure are both the refuted TV/run-count class. Recorded so the next round
  does not re-propose a level-set invariant.
named-mathematics: coarea formula / layer-cake decomposition of l1, level-set
  (suublevel) representation, nested binary arrays, XOR per layer
falsifier: >
  The transform is exact, so it cannot be false as an identity. What kills the
  approach is if the per-layer picture yields no new invariant: i.e., the
  per-layer boundary counts obey nothing cleaner than the scalar total variation
  that was already refuted, and the (2,4)-event has no distinguished per-layer
  signature. First step (c) is exactly that probe; report the per-layer boundary
  trajectories and say whether any single layer or fixed small set of layers
  controls the block front.
side: general-class / dynamical (operator-level; the primes enter only as one
  orbit)
```
