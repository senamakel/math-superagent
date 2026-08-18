import Mathlib

namespace GasullSantana2024

/-- An abstract count of limit cycles of degree `n`; `H` is the Hilbert function. -/
def H : ℕ → ℕ := fun _ => 0

/-- Structural theorem: the Hilbert counts increase by at least one, and a
finite uniform bound yields a structurally stable hyperbolic realization.
The latter is represented abstractly by `Realizable`; the open status is
represented by a proposition rather than asserted as a theorem about `H`. -/
def Realizable (n b : ℕ) : Prop := ∃ k : ℕ, k ≤ b ∧ H n = k

/- gap
id: gasull-monotonicity
lemma: ∀ n : ℕ, H (n + 1) ≥ H n + 1
status: open
next: formalize the lower-bound construction for H(n+1) from a degree-n field and verify its degree and hyperbolicity hypotheses
-/

/- gap
id: gasull-finite-realization
lemma: (∀ n : ℕ, ∃ b : ℕ, H n < b) → ∀ n : ℕ, ∃ b : ℕ, Realizable n b
status: open
next: state the structural-stability and hyperbolicity hypotheses explicitly, then connect a finite supremum to a maximizing polynomial field
-/

/- gap
id: gasull-open-quadratic
lemma: ¬ (∃ b : ℕ, H 2 < b)
status: open
next: replace this status proposition by a cited-status predicate for the literature, since openness is not a mathematical theorem derivable from the definition of H
-/

/-- Combining step: the three component statements imply the structural-status
package. This is intentionally conditional on the open leaves. -/
theorem structural_status_from_parts
    (hmono : ∀ n : ℕ, H (n + 1) ≥ H n + 1)
    (hreal : (∀ n : ℕ, ∃ b : ℕ, H n < b) →
      ∀ n : ℕ, ∃ b : ℕ, Realizable n b)
    (hopen : ¬ (∃ b : ℕ, H 2 < b)) :
    (∀ n : ℕ, H (n + 1) ≥ H n + 1) ∧
    ((∀ n : ℕ, ∃ b : ℕ, H n < b) →
      ∀ n : ℕ, ∃ b : ℕ, Realizable n b) ∧
    ¬ (∃ b : ℕ, H 2 < b) := by
  exact ⟨hmono, hreal, hopen⟩

#print axioms structural_status_from_parts

end GasullSantana2024
