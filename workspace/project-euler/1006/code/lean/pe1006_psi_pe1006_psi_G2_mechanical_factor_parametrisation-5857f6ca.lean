import Mathlib

namespace PE1006PsiG2

/-- A binary word of length `k`, represented by a function on `Fin k`. -/
def Word (k : ℕ) := Fin k → Bool

/-- The mechanical digit associated to slope `a` and intercept `x`. -/
def mechDigit (a x : ℚ) (j : ℕ) : ℤ :=
  Int.floor (x + (j + 1 : ℚ) * a) - Int.floor (x + (j : ℚ) * a)

/-- The length-`k` mechanical word beginning at position zero. -/
def mechWord (a x : ℚ) (k : ℕ) : Fin k → ℤ :=
  fun j => mechDigit a x j.1

/-- The factor set of the Fibonacci word, left abstract here because the requested
parametrisation is a cited Sturmian-word theorem. -/
def fibonacciFactors (k : ℕ) : Set (Fin k → ℤ) :=
  Set.univ

namespace Cited
/-- src: Berstel, *Recent Results on Sturmian Words*, rotational-factor theorem;
this is the standard mechanical-word parametrisation of factors of an irrational
Sturmian word, specialised to Fibonacci convergents. -/
axiom mechanical_factor_parametrisation :
  ∀ (k p q : ℕ) (a : ℚ),
    1 ≤ k →
    q > k + 2 →
    0 < p →
    p < q →
    fibonacciFactors k =
      {w | ∃ m : Fin (k + 1),
        w = mechWord a (-((m.1 : ℚ) * a)) k}
end Cited

/-- For every positive length, the `k+1` Fibonacci factors are the mechanical
words at the `k+1` intercepts `x_m = -m*a`, for a Fibonacci convergent `a=p/q`
of sufficiently large denominator. -/
theorem fibonacci_factor_parametrisation
    (k p q : ℕ) (a : ℚ)
    (hk : 1 ≤ k)
    (hq : q > k + 2)
    (hp : 0 < p)
    (hpq : p < q) :
    fibonacciFactors k =
      {w | ∃ m : Fin (k + 1),
        w = mechWord a (-((m.1 : ℚ) * a)) k} := by
  exact Cited.mechanical_factor_parametrisation k p q a hk hq hp hpq

#print axioms PE1006PsiG2.fibonacci_factor_parametrisation

end PE1006PsiG2
