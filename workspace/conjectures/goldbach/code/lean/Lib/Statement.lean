import Mathlib.Data.Nat.Prime.Basic

/-- Binary (strong) Goldbach conjecture. -/
def GoldbachConjecture : Prop :=
  ∀ n : ℕ, n > 2 → Even n → ∃ p q : ℕ, Nat.Prime p ∧ Nat.Prime q ∧ n = p + q

#check GoldbachConjecture
