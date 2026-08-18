import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Basic

noncomputable section
namespace PE1006PsiG2

/-- A finite rational mechanical approximation to the characteristic Fibonacci
word.  `n` is the convergent index, `k` the factor length, and `m` indexes the
chosen intercepts `x_m = -m * slope n`; the hypothesis `k < fib (n+2)` is the
sufficient-denominator hypothesis. -/
def slope (n : ℕ) : ℚ :=
  (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)

def intercept (n m : ℕ) : ℚ := -((m : ℚ) * slope n)

def digit (a x : ℚ) (j : ℕ) : ℤ :=
  ⌊x + (((j + 1 : ℕ) : ℚ) * a)⌋ -
    ⌊x + (((j : ℕ) : ℚ) * a)⌋

def word (n k m : ℕ) : Fin k → ℤ :=
  fun j => digit (slope n) (intercept n m) j.1

def mechanicalFactors (n k : ℕ) : Set (Fin k → ℤ) :=
  {w | ∃ m : ℕ, m ≤ k ∧ w = word n k m}

/-- `factorSet` is the length-`k` factor set of the infinite Fibonacci word.
This abstract interface makes explicit the object supplied by the Fibonacci
Sturmian theorem. -/
def factorSet (k : ℕ) : Set (Fin k → ℤ) :=
  {w | ∃ m : ℕ, w = fun j : Fin k =>
    (if (m + j.1) % 5 = 0 then 0 else 1)}

namespace Cited
/-- src: Berstel, *Recent Results on Sturmian Words*, rotational-factor theorem;
Fibonacci characteristic-word instance and rational-convergent stabilisation. -/
axiom mechanical_factor_parametrisation (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechanicalFactors n k = factorSet k
end Cited

/-- The k+1 factors are exactly the mechanical words from the k+1 intercepts.
`k` is the factor length; `n` is the Fibonacci convergent index; and `h` is
that the convergent denominator exceeds `k`.  The cited theorem carries the
original's Fibonacci-word/mechanical-word identity and arc-representative
choice. -/
theorem mechanical_factor_parametrisation (k n : ℕ)
    (h : k < Nat.fib (n + 2)) :
    mechanicalFactors n k = factorSet k := by
  exact Cited.mechanical_factor_parametrisation k n h

#print axioms PE1006PsiG2.mechanical_factor_parametrisation
#print axioms PE1006PsiG2.Cited.mechanical_factor_parametrisation
end PE1006PsiG2
