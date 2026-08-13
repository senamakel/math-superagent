```approach
idea: subadditive-growth-ergodic-block-length
mechanism: |
  The recharge identity (established, zero failures to depth 800) is:

      b_k = b_1 + Σ_{events i < k} (j_i + 1) − (k − 1)

  where j_i ≥ 0 is the jump size at the i-th (2,4)-event. This is an EXACT
  identity, not an approximation. It decomposes b_k − b_1 into a "recharge
  sum" S_{k−1} = Σ_{i < k} (j_i + 1) and a "consumption" term (k−1).

  Now observe: the recharge sum S_{k−1} is ADDITIVE over disjoint intervals
  of events, and since j_i ≥ 0 always, S is non-decreasing. The consumption
  term is exactly (k−1). So the conjecture b_k ≥ 1 for all k is equivalent
  to S_{k−1} ≥ k − 1 − b_1 = k − 3 for all k.

  Define the "net growth" G_k = b_k + (k−1) = b_1 + S_{k−1}. Then
  G_k − G_{k−1} = b_k − b_{k−1} + 1. During erosion (b_{k} = b_{k−1} − 1),
  G does not change. At a regeneration event, b_k = b_{k−1} + j_i, so
  G_k − G_{k−1} = j_i + 1 ≥ 1. Thus G_k is a NON-DECREASING integer
  sequence, and it increases exactly at regeneration events by j_i + 1.

  The normalized block length L_k = b_k / k satisfies, for large k:

      L_k = (b_1/k) + (S_{k−1}/k) − (1 − 1/k)

  Let r_k = N_k / k be the event density up to row k (N_k = #events before k)
  and J_k = (1/N_k) Σ (j_i + 1) be the average per-event contribution. Then:

      L_k = (b_1/k) + r_k · J_k − 1 + O(1/k)

  For the conjecture to hold, we need b_k ≥ 1 for all k, which is equivalent
  to L_k > 0. As k → ∞, L_k → r · J − 1 where r = lim r_k and J = lim J_k
  (if these limits exist). So proving the conjecture for all sufficiently
  large k reduces to proving r · J > 1.

  The SUBADDITIVE approach: G_k = b_k + k is exactly the object that can be
  studied via subadditive ergodic theory. Consider the process that generates
  the sequence (b_k, intruder y_k, edge x_k). This is a deterministic
  dynamical system on the space of (halved block, intruder) configurations,
  driven by the prime gap sequence. The quantity G_k/k might converge by
  Kingman's subadditive ergodic theorem if the process is stationary (which
  it is not — the primes are not i.i.d.) or has an appropriate mixing
  property.

  Even without stationarity, we can use DETERMINISTIC subadditivity: the
  sequence a_k = −b_k is NOT subadditive (since b_k can jump up), but the
  "worst-case" sequence b*_k = min_{j ≥ k} b_j is non-increasing with a
  controlled decay rate. Alternatively, we can consider the sequence of
  "events per consumption": if we define the random variable T_m = row index
  of the m-th regeneration event, then the inter-event gap ΔT_m = T_{m+1} − T_m
  is the "time" between events. The average jump per event is J̄_m. The
  renewal-reward process (T_m, Σ(j_i+1)) is a counting process. The
  conjecture holds if the reward rate Σ/T exceeds 1. This is a classical
  renewal-reward theorem question.

  The new mathematical content: instead of tracking the microscopic XOR
  dynamics (which is what every other approach does), this approach treats
  the event sequence as a black-box renewal process and bounds its growth
  rate using GLOBAL properties of the prime gap sequence that feed into
  the event triggering. Specifically:

  1. The intruder value y at (2,4)-events comes from the gaps between
     primes. The distribution of y is the distribution of prime gaps
     (halved and conditioned on the event occurring).

  2. The inter-event gap depends on the drain rate and the stall length.
     The drain rate is y_0/2 (deterministically y_0/2 if every erosion
     step has x=2, up to y_0 if x=0 throughout).

  3. A LOWER BOUND on the event rate comes from a WORST-CASE assumption:
     every erosion step has x=0 (no drain) and the stall is maximal.
     Even in this worst case, if y_0 is bounded by G (the maximum prime
     gap in the relevant range), then events occur at least every
     G + stall_max rows. Combined with the jump size being at least 0,
     this gives S_{k−1} ≥ k / (G + stall_max) · 1. For the conjecture,
     this lower bound must exceed 1 — which is impossible for
     stall_max > 0 unless the jump sizes are large.

  The REAL content is that jumps are LARGE relative to inter-event gaps:
  the data shows median jump 4.5, max jump 360K, and the recharge Σ(j+1)
  is vastly larger than k (at k=161, b_{161} ≈ 1.27M, so Σ(j+1) ≈ 1.27M +
  159 ≈ 1.27M, meaning average j+1 ≈ 1.27M/60 ≈ 21K per event, far exceeding
  the inter-event gap which is at most 15 rows). So the event rate lower
  bound from a subadditive/ergodic theorem is not about the COUNT of events —
  it's about the MASS of jumps.

  The central conjecture for this approach: there exists a constant c > 0
  (depending only on the initial sequence's gap statistics) such that

      lim inf_{k→∞} b_k / k ≥ c.

  A proof that c = 0 would not disprove the conjecture (b_k could grow
  sub-linearly). A proof that c > 0 would PROVE the conjecture (b_k → ∞,
  hence b_k ≥ 1 for all large k). The question is: can we bound c from below
  using only the distribution of prime gaps and the deterministic
  step/drain/stall laws, WITHOUT tracking the microscopic block pattern?

  This approach's strength is that it ABSTRACTS AWAY the XOR dynamics: it
  only needs the event rate (from the interplay of gap sizes and edge-flip
  probabilities) and the jump distribution. The XOR dynamics enter only
  through the stall bound and the edge-flip probability. If one can prove
  that, under any 2-then-odds start with bounded gaps, the edge x at the
  boundary is 2 at least a fixed fraction of the time when y=4, then the
  stall is geometrically bounded and the event rate is bounded below by a
  function of the gap distribution alone.

  Why this beats existing approaches:
  - NOT a "track every XOR" approach (unlike Rule 90, renewal, Walsh-Hadamard)
  - NOT a potential/Lyapunov approach on the row entries (unlike Ducci-max,
    total-variation — refuted)
  - It reduces the problem to a single inequality: r · J > 1, where r and J
    are macroscopic statistics of the event process, which might be provable
    from the prime number theorem + gap bounds WITHOUT knowing the microscopic
    XOR pattern
  - It is the ONLY approach that treats the block length b_k itself as the
    primary object rather than the entries of the triangle
  - It frames the conjecture as a growth-rate statement, connecting it to
    classical probability theory (renewal-reward processes) where limit
    theorems are well understood

  Speculative: the existence of the limit r and J for the prime process is
  open. But even without limits, a finite-horizon bound like
  "b_k ≥ c·k for all k ≥ k_0" might be provable by induction using the
  recharge identity and a worst-case bound on the event gap.
status: proposed
first-step: |
  Compute the empirical growth rate from the depth-1000 data. For each
  k = 1..161 (the live regime), compute L_k = b_k / k, r_k = N_k / k,
  and J_k = S_k / N_k (where N_k = event count before k, S_k = Σ(j_i+1)).
  Plot L_k, r_k, J_k, and r_k·J_k − 1 against k. Look for trends:
  is L_k converging? Is r_k·J_k − 1 stable? Compute the minimum of
  r_k·J_k − 1 over the observed range — this is the "safety margin."

  Then formulate the mathematical question: given the gap distribution of
  the first N primes, what is the worst-case inter-event gap (under
  adversarial edge-flip patterns) and the minimum jump size, and does the
  product (event_rate × average_jump_contribution) exceed 1 for all
  sufficiently large N? Write a program that, given a sequence of gaps,
  computes the worst-case b_k evolution (with the block pattern chosen
  adversarially at each step to maximize erosion, subject to the Rule 90
  constraints) and tests whether b_k can ever reach 0. This is a
  game-theoretic formulation: Nature chooses the block pattern to minimize
  regeneration; the gaps are fixed by the primes. Compile the extent to
  which this worst-case analysis is tractable.
```
