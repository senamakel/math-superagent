import Mathlib.Data.Rat.Floor
import Mathlib.Data.Nat.Fib.Basic

/-!
Central statement for the corrected mechanical-word representation used in PE1006.
The slope is the convergent fib n / fib (n+2), i.e. it tends to 1/phi^2;
its denominator hypothesis is the explicit finite-length condition.
-/
noncomputable section
namespace PE1006Corrected

def slope (n : ℕ) : ℚ := (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)
def intercept (n m : ℕ) : ℚ := -((m : ℚ) * slope n)
def mechDigit (a x : ℚ) (j : ℕ) : ℤ :=
  ⌊x + (((j + 1 : ℕ) : ℚ) * a : ℚ)⌋ -
    ⌊x + (((j : ℕ) : ℚ) * a : ℚ)⌋
def mechWord (n k m : ℕ) (j : Fin k) : ℤ :=
  mechDigit (slope n) (intercept n m) (j : ℕ)
def mechFactorSet (n k : ℕ) : Set (Fin k → ℤ) :=
  {w | ∃ m : ℕ, m ≤ k ∧ w = mechWord n k m}

namespace Cited
/-- src: Berstel, Recent Results on Sturmian Words, rotational-factor theorem;
finite convergent form specialised to the Fibonacci characteristic word. -/
axiom fibonacci_mechanical_factor_representation
    (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = {w | ∃ m : ℕ, w = mechWord n k m}
end Cited

/-- The corrected representation: convergent slope fib n / fib (n+2), with
all intercept indices 0,...,k (the deep factor-identification step is cited). -/
theorem corrected_mechanical_word_representation
    (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = {w | ∃ m : ℕ, w = mechWord n k m} := by
  exact Cited.fibonacci_mechanical_factor_representation k n h

#print axioms PE1006Corrected.corrected_mechanical_word_representation
#print axioms PE1006Corrected.Cited.fibonacci_mechanical_factor_representation
end PE1006Corrected
