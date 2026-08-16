import Mathlib.Algebra.BigOperators.Intervals

open scoped BigOperators

/-- The sum of the first `n` cubes equals the square of the sum of the first `n`
natural numbers:
`∑ i ∈ Finset.range n, i ^ 3 = (∑ i ∈ Finset.range n, i) ^ 2`. -/
theorem sum_cubes_eq_sq_sum (n : ℕ) :
    (∑ i in Finset.range n, i ^ 3) = (∑ i in Finset.range n, i) ^ 2 := by
  exact Finset.sum_range_cubes n

#print axioms sum_cubes_eq_sq_sum
