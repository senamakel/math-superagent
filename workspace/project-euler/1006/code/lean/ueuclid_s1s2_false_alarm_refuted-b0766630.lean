import Mathlib

namespace UEuclidFalseAlarm

/-- The 1-indexed floor-sum moments for `(p,q,r,n,z)=(1,0,1,5,3)`.
The summation index is `t = 1,...,n`, and the weight is `z^(t-1)`. -/
def s1 : ℕ := ∑ t ∈ Finset.range 5, 3 ^ t * ((t + 1 : ℕ) / 1)
def s2 : ℕ := ∑ t ∈ Finset.range 5, 3 ^ t * (((t + 1 : ℕ) / 1) ^ 2)

theorem s1_correct : s1 = 547 := by
  decide

theorem s2_correct : s2 = 2551 := by
  decide

#print axioms s1_correct
#print axioms s2_correct

end UEuclidFalseAlarm
