```approach
idea: lipschitz-excess-lyapunov
mechanism: |
  Halve the nonnegative entries (A_k(i) = 2·h_k(i) for i ≥ 1; h_k(0)=1). The
  single quantity that DEFINES the leading {0,2} block is the local slope
  d_i := h_i − h_{i+1}. A_k+1(i) = |A_k(i) − A_k(i+1)| = 2·|h_i − h_{i+1}| lies
  in {0,2} exactly when |d_i| ≤ 1. Hence (this is an exact identity, not a
  conjecture) the block length of row k+1 is the length of the leading run of
  indices i with |h_i − h_{i+1}| ≤ 1, i.e. b_{k+1} = #{i : |d_j| ≤ 1 for all
  j ≤ i}.

  Every scalar potential tried so far (run-count, turning-point count,
  total-variation of the row, alternating-sum telescope) is blind to the
  threshold "1" that this identity puts at the centre; that is why they all
  died on the XOR zigzag. The functional that is NOT blind to it is the
  one-sided Lipschitz excess

      e_i := max(0, |h_i − h_{i+1}| − 1) ≥ 0,   E(h) := Σ_i e_i.

  E(h) = 0 ⟺ h is 1-Lipschitz ⟺ the entire next row is {0,2}-valued (full
  Gilbreath, protects forever). The block of row k+1 is exactly the length of
  the leading zero-run of the excess sequence (e_i). So the conjecture
  A_k(1) ∈ {0,2} is the statement that this leading zero-run of excess never
  vanishes: b_k ≥ 1 forever. The recharge identity b_k = b_1 + Σ(j_i+1) − (k−1)
  then has a direct excess reading: a (2,4)-event (edge halved 1, intruder
  halved 2) is precisely where a local excess term |h|−1 = 1 is consumed and
  turned back into a {0,1} entry, while erosion is where the excess sequence
  shifts left by one with the zero-run shortening.

  The candidate invariant to prove: E is non-increasing along the triangle
  (or satisfies E(h_{k+1}) ≤ E(h_k) + a boundary correction whose sign is
  controlled by the drain law). If E is a Lyapunov function whose sublevel
  sets are exactly "longer {0,2} prefix", then the block can only shrink when
  the excess at the boundary is forced to zero — and that is the (2,4)-event,
  so regeneration is the only way E is spent, closing the recharge loop.
  This is a rate statement about regeneration (the open content), not another
  erosion verification.
status: proposed
side: general-class / dynamical (attacks regeneration directly; erosion and the block lemma are inputs, not the target)
named-mathematics: 1-Lipschitz cone, one-sided threshold excess functional, Lyapunov function, sublevel-set / zero-run structure, the exact identity b_{k+1} = leading 1-Lipschitz prefix of h_k
speculative: E-monotonicity is unproved and may fail at the Chamberland rigidity pairs (a,a,c,c) where the max-decrease potential stalls; the honest first check is whether E(h_{k+1}) ≤ E(h_k) on the oracle rows, and if it fails, whether the violations are exactly the big-jump (2,4)-events (in which case the corrected inequality E(h_{k+1}) ≤ E(h_k) − (excess consumed by the jump) + (excess injected) is the right form).
falsifier: If E(h_{k+1}) > E(h_k) on any prime row without a compensating big-jump boundary term — and in particular if a big-jump regeneration injects more excess than it consumes — then plain monotonicity is false and only a boundary-corrected version survives (still useful, but weaker). The first step measures exactly this.
first-step: |
  From the oracle rows (witnesses.json depth 600; blocks_depth1000.json depth 1000,
  exact integers) compute, for each live row k: the halved row h_k, the local
  excess sequence e_i = max(0, |h_i − h_{i+1}| − 1), E(h_k) = Σ e_i, the block
  length b_k, and verify the exact identity b_{k+1} = leading zero-run length of
  (e_i). Then test E(h_{k+1}) ≤ E(h_k) and report the first violation row with
  its (edge, intruder, jump) triple; separately tally E-change across each of
  the 60 (2,4)-events. Cost O(depth × width), one row live. A monotone E on all
  998 transitions is a Lyapunov candidate worth formalising in Lean; a violation
  isolaated at big jumps pins down the needed boundary correction.
```

## Why this is not already on disk

- **Not `total-variation-oscillation-potential` / run-count / turning-point (refuted):** those functionals (Σ|h_i − h_{i+1}|, number of runs, number of sign changes) take values on the *whole* oscillation and are blind to whether a local slope exceeds 1. `E` is a *one-sided threshold* functional: it is 0 exactly on the safe stratum, so its sublevel sets carry the block structure those potentials could not see. The minimal refuting string (0,0,1,1)→(0,1,0) for the run-count potential has `E` decreasing (E(0,0,1,1)=1, E(0,1,0)=1), so it does not fall to the same counterexample.
- **Not `ducci-potential-max-decrease` (proposed):** that hunts a windowed max that decreases; `E` is a sum of *local excesses* and is tied to the block by an exact identity.
- **Not `discrete-curvature-flow-flat-prefix` (refuted):** that imported *linear* curvature-flow theory. `E` is a discrete functional on the exact operator; no flow/linearisation is claimed.

## What it would take for this to be wrong

`E` must be non-increasing (up to a controlled boundary term) on the real rows. The smallest input that breaks it is the thing to hunt first: a row where a big (2,4)-jump injects fresh gaps whose local slopes exceed 1 by more than the excess the jump consumed. The oracle check above is exactly that hunt, and it is run *before* any theory is built on `E`.
