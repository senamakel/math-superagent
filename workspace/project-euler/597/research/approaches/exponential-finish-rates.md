# Approach: Reformulation in exponential-finish-rate coordinates w_j = v_j/(L−p_j)

```approach
idea: Change variables to w_j = v_j/(L−p_j) ∼ Exp(L−p_j), turning the finish events into proper exponential clocks (with boat-dependent rates), and then reformulate the bump chronology as a deterministic-ratio comparison on these exponential variates — restoring the competing-exponentials / Plackett-Luce machinery that the original v-coordinates lost.
mechanism: Boat j finishes at time T_j^F = 1/w_j. Since w_j ∼ Exp(λ_j) with rate λ_j = L − 40(j−1), the finish events ARE competing exponential clocks — the very machinery that the refuted treap recursion wrongly assumed for the inverse-exponential finish times in v-coordinates. In w-coordinates, the hazard of finishing is constant (rate λ_j), and conditional on no finish having occurred yet, the residual finish times remain Exp(λ_j) by the memoryless property.

A bump i→j (with i<j) occurs at time T_{ij}^B = 40(j−i)/(v_i−v_j) = 40(j−i)/(λ_i w_i − λ_j w_j). The condition for bump i→j to be the next event is:

  T_{ij}^B < T_k^F for all rowing k,  and  T_{ij}^B < T_{kℓ}^B for all other possible bumps (k,ℓ).

Now, T_k^F = 1/w_k. For T_{ij}^B < 1/w_k, we need 40(j−i)/(λ_i w_i − λ_j w_j) < 1/w_k. This is equivalent to 40(j−i) w_k < λ_i w_i − λ_j w_j. This is a LINEAR inequality in w (since w_j > 0). Similarly, T_{ij}^B < T_{kℓ}^B expands to (j−i)(λ_k w_k − λ_ℓ w_ℓ) < (ℓ−k)(λ_i w_i − λ_j w_j) — also linear in w.

Thus, in w-coordinates, the condition "event e is the next to occur" is a polyhedral cone defined by linear inequalities. And the w_j are independent exponentials with KNOWN rates λ_j. This means we can compute the probability of each transition in the event-driven DP using the competing-exponentials formula: for a set of exponential clocks with rates μ_1,…,μ_m, the probability that clock r fires first is μ_r/Σ μ_s — provided the clocks are independent exponentials.

The finish clocks ARE independent exponentials (rates λ_j). The bump "clocks" are NOT exponentials — T_{ij}^B = 40(j−i)/(λ_i w_i − λ_j w_j) is not an exponential random variable. However, the EVENT that a particular bump is the next event is defined by linear inequalities on w, and the probability can be computed by integrating the product of exponential densities over the corresponding polyhedral cone. This is a lower-dimensional integral than the original simplex-volume approach because the exponential densities factor: P(event e) = ∫_{cone(e)} ∏_{j=1}^n λ_j e^{−λ_j w_j} dw.

The crucial advantage: because the exponential density factorises as a product and the cone is defined by homogeneous linear inequalities, this integral can be evaluated in closed form via partial fractions / inclusion-exclusion on the linear forms defining the cone — a standard technique for exponential-polynomial integrals over polyhedra. Specifically, for a simplicial cone C = {w : A w ≥ 0}, the integral ∫_C ∏ λ_j e^{−λ_j w_j} dw equals a sum of terms of the form (product of some λ's) / (determinant of a submatrix of A), generalising the "rate-ratio product" formula for competing exponentials. This gives a polynomial (in n) algorithm for each transition probability, replacing the super-exponential arrangement enumeration.

The full DP then runs over the 2^n survivor subsets, but with each transition probability computed in O(n³) by this exponential-integral formula rather than by enumerating arrangement cells. Total complexity: O(2^n · n³) = O(10⁵) operations for n=13. The parity weight propagates multiplicatively as in the first approach.
status: proposed
first-step: Derive the closed-form integral formula for P(bump i→j is the next event | current survivors S) in w-coordinates, for a 3-boat example. Verify numerically against brute-force MC: for n=3, L=160, compute the exact probability of each possible first event by the w-integral formula, check that they sum to 1 and that the resulting parity-weighted sum equals the known p(3,160) = 56/135.
```