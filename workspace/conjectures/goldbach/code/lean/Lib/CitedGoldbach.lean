import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.Group.Nat.Even

namespace Cited

/-- src: Kumchev and Tolev, "An invitation to additive prime number theory", arXiv:math/0412220, Theorem 2 (Chen 1973). -/
axiom chen_goldbach_p_two :
  ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N → Even N → ∃ p a : ℕ,
    Nat.Prime p ∧ (Nat.Prime a ∨ ∃ r s : ℕ, Nat.Prime r ∧ Nat.Prime s ∧ r * s = a) ∧ p + a = N

/-- src: Pintz, "A new explicit formula in the additive theory of primes with applications II", arXiv:1804.09084, introduction and Theorem 1. -/
axiom exceptional_set_power_saving : Prop

end Cited

#print axioms Cited.chen_goldbach_p_two
#print axioms Cited.exceptional_set_power_saving
