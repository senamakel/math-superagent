import Mathlib

/-- The reported and direct hand-check pairs are unequal. -/
theorem ueuclid_incontainer_fails_s1s2_handcheck :
    ((547 : ℕ), (2551 : ℕ)) ≠ ((426 : ℕ), (1578 : ℕ)) := by
  norm_num

#print axioms ueuclid_incontainer_fails_s1s2_handcheck
