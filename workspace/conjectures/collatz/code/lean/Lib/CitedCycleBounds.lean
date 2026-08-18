import Mathlib

namespace Cited

/-- src: Hercher, 'On the non-existence of Collatz m-cycles', arXiv:2201.00406, Main Theorem 23. -/
axiom no_m_cycle_le_91 : Prop

end Cited

namespace Collatz

/-- The cited theorem is represented as an explicit proposition; downstream
formal consequences require a definition of accelerated cycles and are left
for the next formalisation pass. -/
theorem hercher_cycle_exclusion_placeholder : Cited.no_m_cycle_le_91 := by
  exact Cited.no_m_cycle_le_91

#print axioms hercher_cycle_exclusion_placeholder

end Collatz
