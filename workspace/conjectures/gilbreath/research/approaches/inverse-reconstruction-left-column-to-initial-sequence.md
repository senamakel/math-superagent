```approach
idea: inverse-reconstruction-left-column-to-initial-sequence
mechanism: |
  Every approach on disk studies the FORWARD evolution: start with the primes
  and watch the left column emerge. This approach studies the INVERSE problem:
  start with a hypothetical left column and reconstruct backward to see what
  initial sequence would produce it. The conjecture says the actual left
  column is (1,1,1,...), so if any deviation — say A_k(1) = 4 — produced a
  reconstructed initial row contradicting known properties of the primes
  (parity, positivity, gap bounds, or the specific values of the first few
  primes), then that deviation is impossible.

  The reconstruction step is well-posed: from A_{k+1}(i) = |A_k(i) − A_k(i+1)|
  we get two branches A_k(i+1) = A_k(i) ± A_{k+1}(i). Starting from the known
  left column A_k(0) = 1 for all k and the known first row A_1, each row A_k
  is reconstructed from A_{k+1} by resolving these ± choices. The parity
  constraint (A_k(i) even for i ≥ 1) uniquely determines the sign in most
  cases: the two branches give opposite parity when A_{k+1}(i) is odd, and
  same parity when A_{k+1}(i) is even — the latter case is exactly the
  ambiguity that matters for the conjecture.

  The key theorem to prove: there exists a unique 2-then-odds sequence whose
  Gilbreath triangle has left column identically 1, and that sequence is
  (up to finite prefix) exactly the primes. More practically: if any entry
  of the left column deviates from 1, the backward reconstruction violates
  either the parity constraint or the gap bound within a finite number of
  steps (the deviation "propagates rightward" in the reconstruction and hits
  a contradiction).

  This is NOT the refuted backward-extension-automaton (which studied local
  valid-extension sets of finite prefixes). This is a GLOBAL reconstruction
  of the entire triangle from its left edge, using parity to prune the
  exponential ± branch tree. The engine is constraint propagation: a single
  deviation at the left column propagates along anti-diagonals of the
  triangle, and the collection of propagated constraints eventually demands
  a gap value that is impossible (too large, wrong parity, or negative).

  Named mathematics: inverse problem for difference tables, binomial
  inversion with sign resolution, constraint propagation, the "inverse
  Gilbreath problem" (studied globally by Muney 2026 and Alkan et al. 2023
  for finite prefixes, but here applied to the infinite triangle with the
  left-column-to-initial-sequence direction).
status: proposed
first-step: |
  Write the exact backward recurrence. For a hypothetical left column
  L = (1, a_1, a_2, ...) with each a_k ∈ {0,2} (the conjecture's claim),
  reconstruct row A_1 from rows A_2, A_3, ... using A_k(i+1) = A_k(i) ±
  A_{k+1}(i) with parity pruning. For small k (≤ 20), compute the set of
  all possible reconstructed A_1 prefixes and check whether they ever include
  a 2-then-odds sequence with even gaps beyond some bound. Then introduce a
  SINGLE deviation (a_k = 4 for some k) and track how far the reconstruction
  can proceed before hitting a contradiction. The deliverable: an explicit
  bound B such that any left-column deviation at row k forces a contradiction
  within B(k) reconstruction steps, or a demonstration that no such finite
  bound exists (in which case the approach is refuted). Code:
  `code/inverse_reconstruction/backward_reconstruct.py`.
```