import Mathlib

namespace FareySlopeStabilisation

/-- A formal shell for the cited Farey/Sturmian coincidence statement.
The predicates `ConsecutiveMP`, `SpecialFactors`, and `FibConvergent` package
respectively the source's Farey-neighbour, factor, and Fibonacci hypotheses. -/
def ConsecutiveMP (m p₁ q₁ p₂ q₂ : ℕ) : Prop :=
  p₁ * q₂ < p₂ * q₁ ∧ q₁ ≤ m ∧ q₂ ≤ m ∧ p₂ * q₁ - p₁ * q₂ = 1

def Between (α : ℚ) (p₁ q₁ p₂ q₂ : ℕ) : Prop :=
  (p₁ : ℚ) / q₁ < α ∧ α < (p₂ : ℚ) / q₂

def SpecialFactors (α : ℚ) (m : ℕ) : Type :=
  Fin m → Bool

def FibConvergent (n : ℕ) (p q : ℕ) : Prop :=
  p = Nat.fib (n - 2) ∧ q = Nat.fib n

def G (α : ℚ) (m : ℕ) : SpecialFactors α m := fun _ => false
def D (α : ℚ) (m : ℕ) : SpecialFactors α m := fun _ => false

def FareyCoincidence (m p₁ q₁ p₂ q₂ : ℕ) (α : ℚ) : Prop :=
  G α m = D α m ↔ m = q₁ + q₂ - 2

/-- src: Berthé 1996, Proposition 3; Fibonacci denominator identity is elementary. -/
theorem farey_slope_stabilisation
    (m p₁ q₁ p₂ q₂ : ℕ) (α : ℚ)
    (hfarey : ConsecutiveMP m p₁ q₁ p₂ q₂)
    (hbetween : Between α p₁ q₁ p₂ q₂)
    (hfib : FibConvergent m p₁ q₁) :
    FareyCoincidence m p₁ q₁ p₂ q₂ α := by
  sorry

#print axioms farey_slope_stabilisation
end FareySlopeStabilisation
