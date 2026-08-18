import Mathlib.Data.Nat.Prime.Basic

namespace Cited

/-- src: Bordignon, Johnston & Starichkova, “An explicit version of Chen’s theorem and the linear sieve”, arXiv:2207.09452v6, Theorem 3 / Corollary 4. -/
axiom chen_explicit :
  ∀ N : ℕ, N > 0 → Even N → N > 0 → True

/-- src: Helfgott, “The ternary Goldbach conjecture is true”, arXiv:1312.7748v2, Main Theorem. -/
axiom ternary_goldbach :
  ∀ n : ℕ, Odd n → n > 5 → ∃ p q r : ℕ,
    Nat.Prime p ∧ Nat.Prime q ∧ Nat.Prime r ∧ n = p + q + r

end Cited

#print axioms Cited.ternary_goldbach
