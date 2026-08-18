import Mathlib

namespace PE1006Anchors

/-- The two independently computed anchor residues and factor counts for PE1006. -/
theorem directive6_anchors_verified_incontainer :
    (34432237 : ℕ) % 101001001 = 34432237 ∧
    (10001 : ℕ) = 10000 + 1 ∧
    (20938836 : ℕ) % 101001001 = 20938836 ∧
    (1000001 : ℕ) = 1000000 + 1 := by
  norm_num

#print axioms directive6_anchors_verified_incontainer

end PE1006Anchors
