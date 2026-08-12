# Approach: pure-race limit with explicit finite-L correction

```approach
idea: >
  Prove that p(n,L) = p(n,∞) + O(e^{-cL/n}) for some c>0, compute p(13,∞)
  exactly from the pure-race bump-forest theory, and bound the L=1800 remainder
  below 5×10^{-11}
mechanism: >
  The pure race (L=∞) removes the finish event: every boat rows until bumped or
  is the lead boat. The MC evidence shows p(n,1800) ≈ p(n,∞) for n=2..30,
  with differences ≤ 0.003 and decreasing with n. In the finite race, a boat
  finishes if its finish time is less than the time it would be bumped.
  For boat j at position 40(j-1), the finish distance is L-40(j-1).
  When L is large compared to the inter-boat spacing (40m), most boats finish
  without being involved in a bump, and the bump graph is dominated by the
  pure-race structure. The correction comes from boats that would have bumped
  in the pure race but finish first in the finite race. The probability of
  such a "pre-empted bump" decays exponentially in L/(n*v_typical).
  The pure-race parity p(n,∞) is a functional of the speed-ordering + magnitude
  alone — no finish line — and is exactly computable via the convex-minorant
  cluster decomposition (pure-race bump clusters = GCM segments, distribution
  known: Stirling numbers of the first kind). Within each cluster, the forest
  structure depends only on the relative speed ordering. The parity for the
  pure race may admit an exact formula in terms of record statistics.
status: proposed
first-step: >
  Compute exact p(5,∞) by extending the pure-race oracle (L=1e9 or analytic)
  and compare to p(5,1800) from MC (0.53273±0.00029). Measure the difference
  Δ_5 = p(5,∞) - p(5,1800). Derive the exponential bound: for a bump between
  boats i,j to be pre-empted by j's finish, we need v_j > (L-40(j-1))/T where
  T is the bump-arrival time. Bound P(pre-emption) ≤ something like
  exp(-(L-40n)/(40n)) using the Exp(1) tail. If Δ_n ≤ e^{-(L-40n)/C} for some
  explicit C, then at n=13, L=1800 the correction is below 5×10^{-11} and
  p(13,1800) = p(13,∞) to 10dp.
```