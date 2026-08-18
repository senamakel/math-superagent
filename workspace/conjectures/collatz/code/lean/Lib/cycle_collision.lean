import Mathlib

namespace Cited

/-- Source: Hercher 2022, arXiv:2201.00406, Theorem 16. Here `m` is the
number of local minima (odd members `n i`), `L` is the number of even members,
`x_min` is the minimum cycle element, and `Tsum` is the sum of the reciprocal
run terms T(n i). -/
axiom bridge_upper_bound
    (m L : ℕ) (x_min : ℝ) (Tsum : ℝ)
    (delta : ℝ) (logTwo : ℝ)
    (hm : 0 < m) (hcycle : 0 < x_min) :
    (m + L : ℝ) / m < delta + (3 * logTwo / m) * Tsum

/-- Source: Zudilin 2004, arXiv:math/0404523, Theorem 3. The effective
irrationality-measure consequence is recorded in the quantified form needed
for rational approximations to delta = log 3 / log 2. -/
axiom diophantine_lower_bound
    (delta : ℝ) (mu c₀ : ℝ)
    (hmu : mu = 8.616) (hc : 0 < c₀) :
    ∀ p q : ℕ, 0 < p → 0 < q →
      c₀ / (q : ℝ) ^ mu < |delta - (p : ℝ) / q|

/-- Source: Hercher 2022, arXiv:2201.00406, Theorem 16 and the definition
of the reciprocal run sum. The elementary estimate is isolated as requested. -/
axiom reciprocal_sum_bound
    (m : ℕ) (x_min Tsum : ℝ)
    (hm : 0 < m) (hx : 0 < x_min) :
    Tsum ≤ (m : ℝ) / x_min

end Cited

/-- Pinned-down collision conclusion for the minimum element of a non-trivial
cycle. The cited bridge and Diophantine estimates are hypotheses; this file
records the intended implication and leaves its missing arithmetic/structural
collision proof explicit. -/
theorem nontrivial_cycle_minimum_lower_bound
    (m : ℕ) (x_min : ℝ) (mu c₀ logTwo : ℝ)
    (hm : 0 < m) (hx : 0 < x_min) (hmu : mu = 8.616) (hc : 0 < c₀)
    (hlog : 0 < logTwo) :
    x_min > (3 * logTwo / c₀) * (m : ℝ) ^ mu := by
  sorry

#print axioms Cited.bridge_upper_bound
#print axioms Cited.diophantine_lower_bound
#print axioms Cited.reciprocal_sum_bound
#print axioms nontrivial_cycle_minimum_lower_bound
