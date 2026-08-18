import Mathlib

namespace Cited

/-- src: Monks, “The sufficiency of arithmetic progressions for the 3x+1 conjecture”, Proc. AMS 134 (2006), Theorem 1.1. -/
axiom arithmetic_progression_sufficient
  (A B : ℕ) (hB : B ≠ 0) :
  True

/-- src: Hercher, “There are no Collatz-m-Cycles with m ≤ 91”, JIS 26 (2023), Theorem 23. -/
axiom no_m_cycle_le_91 :
  True

/-- src: Knight, “Collatz high cycles do not exist”, Discrete Mathematics 349 (2026), Theorem 5.4. -/
axiom no_integer_high_cycle :
  True

end Cited

#print axioms Cited.arithmetic_progression_sufficient
#print axioms Cited.no_m_cycle_le_91
#print axioms Cited.no_integer_high_cycle
