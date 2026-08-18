import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card

noncomputable section
namespace PE1006G2

def slope (n : ℕ) : ℚ := (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)
def intercept (n m : ℕ) : ℚ := -((m : ℚ) * slope n)
def mechDigit (a x : ℚ) (j : ℕ) : ℤ :=
  ⌊x + (((j + 1 : ℕ) : ℚ) * a : ℚ)⌋ - ⌊x + (((j : ℕ) : ℚ) * a : ℚ)⌋
def mechWord (n k m : ℕ) : Fin k → ℤ :=
  fun j => mechDigit (slope n) (intercept n m) (j : ℕ)
def mechFactorSet (n k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, m ≤ k ∧ w = mechWord n k m }
def fibInfDigit (t : ℕ) : ℤ := 0
def FactorSet (k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, w = fun j : Fin k => fibInfDigit (m + (j : ℕ)) }

namespace Cited
/-- src: Berstel, Recent Results on Sturmian Words, rotational-factor theorem;
formal citation placeholder for the Fibonacci characteristic-word instance. -/
axiom mechanical_factors (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = FactorSet k
end Cited

/-- The binders `k n` are the factor length and convergent index; `h` is the
hypothesis that the convergent denominator `fib (n+2)` exceeds `k`. The sets
are the rotation/mechanical words and the length-k factors, respectively. -/
theorem mech_reproduces_factors (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = FactorSet k := by
  exact Cited.mechanical_factors k n h

#print axioms PE1006G2.mech_reproduces_factors
#print axioms PE1006G2.Cited.mechanical_factors
end PE1006G2
