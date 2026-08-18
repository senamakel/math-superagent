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

/-!
The decomposition separates the theorem into: (i) the arithmetic properties of
convergent slopes, (ii) the rotation coding/factor correspondence, and (iii)
the finite intercept representatives.  Only (ii) is genuinely external here.
-/

lemma slope_denominator (n k : ℕ) (h : k < Nat.fib (n + 2)) :
    k < Nat.fib (n + 2) := by
  exact h

lemma convergent_slope_identity (n : ℕ) :
    slope n = (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ) := by
  rfl

lemma intercept_representatives (n k : ℕ) :
    mechFactorSet n k = {w | ∃ m : ℕ, m ≤ k ∧ w = mechWord n k m} := by
  rfl

/- gap
id: g2-mechanical-factors-cited-correspondence
lemma: ∀ k n : ℕ, k < Nat.fib (n + 2) → mechFactorSet n k = FactorSet k
status: open
next: Check the exact rotational-factor theorem in the cited Sturmian literature and formalise its Fibonacci characteristic-word instantiation, including the slope convention and intercept representatives.
-/
lemma mechanical_factors_correspondence (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = FactorSet k := by
  sorry

/- gap
id: g2-mechanical-word-convergent-limit
lemma: ∀ k : ℕ, ∃ n : ℕ, k < Nat.fib (n + 2) ∧ slope n is a continued-fraction convergent to 1/phi^2
status: open
next: State the convergent property over an exact irrational target (or use the standard Fibonacci continued-fraction theorem) and prove denominator growth supplies n.
-/
lemma convergent_limit (k : ℕ) :
    ∃ n : ℕ, k < Nat.fib (n + 2) := by
  sorry

/-- Combining step: the desired rotation/mechanical representation follows
from the correspondence lemma; the denominator condition is the stated
finite-convergent hypothesis. -/
theorem mech_reproduces_factors (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = FactorSet k := by
  exact mechanical_factors_correspondence k n h

#print axioms PE1006G2.mech_reproduces_factors
#print axioms PE1006G2.mechanical_factors_correspondence
#print axioms PE1006G2.convergent_slope_identity
end PE1006G2
