import Mathlib

namespace Collatz

/-- src: standard Collatz conjecture statement, as defined in problem.md. -/
def T (n : ℕ) : ℕ :=
  if Even n then n / 2 else (3 * n + 1) / 2

def CollatzConjecture : Prop :=
  ∀ n : ℕ, 0 < n → ∃ k : ℕ, (T^[k]) n = 1

theorem collatz_conjecture : CollatzConjecture := by
  sorry

#print axioms collatz_conjecture

end Collatz
