import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.Group.Nat.Even

namespace Goldbach

def IsGoldbachPair (n p q : ℕ) : Prop :=
  Nat.Prime p ∧ Nat.Prime q ∧ p + q = n

def IsGoldbach (n : ℕ) : Prop :=
  ∃ p q : ℕ, IsGoldbachPair n p q

theorem goldbach_conjecture :
    ∀ n : ℕ, 2 < n → Even n → IsGoldbach n := by
  sorry

#print axioms goldbach_conjecture

end Goldbach
