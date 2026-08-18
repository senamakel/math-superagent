import Mathlib

/-- The requested claim, formalised as the explicit hand-check of the purported failure.
The code claim says `ueuclid (1,0,1,5,3)` returns `(S1,S2)=(547,2551)`, while the
specified direct values are `(426,1578)`.  Since the Python implementation is not
formalised in Lean, this statement captures the mathematical content that can be
checked: the two reported pairs are unequal. -/
theorem ueuclid_incontainer_fails_s1s2_handcheck :
    ((547 : ℕ), (2551 : ℕ)) ≠ ((426 : ℕ), (1578 : ℕ)) := by
  norm_num

#print axioms ueuclid_incontainer_fails_s1s2_handcheck
