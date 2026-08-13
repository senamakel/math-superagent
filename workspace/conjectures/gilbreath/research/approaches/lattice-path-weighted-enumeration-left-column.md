```approach
idea: lattice-path-weighted-enumeration-left-column
mechanism: |
  The Gilbreath triangle entry A_k(i) can be expressed as a weighted sum over
  lattice paths from the initial row to cell (k,i) in a directed acyclic graph.
  For the SIGNED forward differences (without absolute value), the weight of
  a path is simply ±1 times the starting value, and the total sum is the
  binomial transform — the enumeration is by Pascal's triangle, which is
  equivalent to counting paths on the integer lattice with NE/SE steps and
  appropriate weights.

  For the ABSOLUTE-VALUE version, the path weight depends on the sign pattern
  of intermediate values: each absolute-value step splits into two signed
  branches, and the total A_k(1) is the sum over all 2^k branches of the
  absolute value of the associated alternating sum. This is a sum over an
  exponentially large set of paths, but with massive cancellations.

  The key structural observation: the value A_k(1) for the PRIME sequence is
  always 0 or 2, which means that among the 2^k signed paths contributing to
  position (k,1), all but at most one cancel, and the survivor (if any) has
  weight exactly 2. This suggests the path weights satisfy a NON-CROSSING or
  BALLOT condition: the "positive" paths and "negative" paths nearly balance,
  and the imbalance is constrained to be small. This is exactly analogous to
  the classical BALLOT THEOREM (Bertrand's ballot problem): the number of
  paths that stay above the diagonal equals the difference of two binomial
  coefficients. In the Gilbreath setting, the "diagonal" corresponds to the
  boundary where the signed alternating sum crosses zero — the absolute value
  "reflects" paths that would go negative, and the net excess after reflection
  is the value at the left column.

  Specifically: start with the identity |a − b| = a + b − 2·min(a,b). The
  linear term a + b gives the Pascal/Rule-90 (mod-2) contribution, which sums
  to 0 or 1. The nonlinear correction −2·min(a,b) introduces the equivalent
  of "reflected paths": whenever the signed sum would go negative, the min
  branch reflects it back to positive. The total A_k(1) is the signed sum
  PLUS the cumulative weight of all reflected paths.

  The conjecture is equivalent to: the cumulative reflected weight at position
  1 never exceeds 1 (in halved units). This is a statement about the
  ENUMERATION of reflected lattice paths. If the reflection sites can be
  characterized (they are exactly where adjacent signed differences have
  opposite signs), and if the reflection sites for the prime sequence are
  "sparse" in a provable sense, then the reflected weight is bounded.

  The concrete analogy: the ballot numbers C(n, ⌊n/2⌋) − C(n, ⌊n/2⌋−1)
  count Dyck paths that never go below the diagonal. The Gilbreath correction
  counts the excess of paths that DO go below the diagonal and get reflected.
  If the "bad" paths can be injected into the "good" paths (via an explicit
  bijection) with a small deficit, the deficit equals the left column value.

  Named mathematics: lattice path enumeration, ballot numbers, Catalan
  numbers, reflection principle (André's reflection method), non-crossing
  partitions, Gessel-Viennot lemma for non-intersecting paths.

  Why it beats existing approaches: this is a purely COMBINATORIAL enumeration
  that replaces the algebraic operator |a−b| with a path-counting problem.
  The refuted mod4-pascal approach attempted a congruence lift and failed on
  the min branch; this approach treats the min branch as the MAIN OBJECT (the
  "reflection" in the path sum), turning the obstruction into the engine.
  The path-counting framework gives access to the Gessel-Viennot determinant
  method and the theory of symmetric functions, which are powerful tools for
  exact combinatorial identities.

  Speculative: whether the reflection sites for the prime gap sequence admit a
  closed-form characterization (likely no), and whether the path-sum
  formulation can be simplified without knowing the exact positions of the
  reflections (the cancellation might be provable statistically, à la the
  Cramér model).
status: proposed
first-step: |
  (a) Write the exact path-sum formula. Starting from row A_1, expand each
  A_k(1) as a sum over signed paths of length k−1 from the initial row to
  position (k,1). Each path is a sequence of choices: at each cell, the value
  is |u − v| = u + v − 2·min(u,v). In the expansion, the term u+v generates
  the linear (Pascal) paths, and −2·min(u,v) generates the "reflected" paths
  where the sign flips. Derive the exact expression for A_k(1) as the linear
  Pascal sum plus a correction sum over reflection events. Verify this formula
  numerically against the depth-200 prime rows (code:
  `code/lattice_path/path_sum_formula.py`).

  (b) Compute, for the prime rows to depth 200, the "reflection count" at
  each row: how many min-branch activations contributed to A_k(1)? Does the
  reflection count stay bounded? If yes, a finite reflection bound would
  prove the conjecture.

  (c) For small k (≤ 8), enumerate the full set of 2^k signed paths and
  characterize which ones survive cancellation to give A_k(1) = 0 or 2.
  Look for a combinatorial structure (e.g., non-crossing matching, or an
  involution pairing paths with opposite signs) that explains the
  cancellation.
```