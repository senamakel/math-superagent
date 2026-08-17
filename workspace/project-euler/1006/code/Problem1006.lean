import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Real.Sqrt
import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Card
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Algebra.BigOperators.Intervals

/-!
# PE1006 — mechanical-word / factor structure of the Fibonacci word

Informal claim (the load-bearing structure behind `Ψ(k)`):

  * Let `F` be the infinite Fibonacci word (the limit of `S_0 = 0`,
    `S_1 = 01`, `S_n = S_{n-1}S_{n-2}`; digit sequence OEIS A003849,
    `0100101001001…`).  It is the characteristic Sturmian word of slope
    `α = 1/φ² = (3 - √5)/2`:  its digit at 0-based position `t` is
    `⌊(t+2)α⌋ - ⌊(t+1)α⌋`.
  * For each `k` the set of distinct length-`k` contiguous factors of `F`
    has exactly `k + 1` elements (Sturmian factor complexity `p(k) = k + 1`).
  * These `k + 1` factors are reproduced by the mechanical (rotation)
    construction: with rational slope `a = fib(n)/fib(n+2)`, for any `n` with
    `k < fib(n+2)`, the `k+1` intercepts `x_m = -m·a` (`m = 0..k`) give digits
    `digit_j(x_m) = ⌊x_m + (j+1)a⌋ - ⌊x_m + j·a⌋`, and the set of the `k+1`
    words so obtained is exactly the length-`k` factor set of `F`.

Two index corrections to the run's working notes (numerically verified for
`k = 1..100` in `/tmp/mech*.py` and `/tmp/bridge.py`):

  1. The steering-directive slope `F(n-1)/F(n)` is WRONG: its words contain
     the block `11`, which never occurs in `F`.  The correct rational slope
     is `fib(n)/fib(n+2)` — the continued-fraction convergents to `1/φ²`.
  2. The infinite-word digit formula uses the *irrational* `α = 1/φ²`; the
     rational slopes `fib(n)/fib(n+2)` converge to it, and the mechanical
     *set* (not the position-by-position match) equals the factor set.

All theorems below are statements: each ends in `:= by sorry`.  The point is
that they *elaborate* — every name resolves and the types are right — and
that the statement graph can then schedule proofs of the individual gaps.
-/

noncomputable section
open scoped BigOperators

namespace PE1006

/-- `α = 1/φ² = (3 - √5)/2`, the slope of the Fibonacci word as a Sturmian word. -/
def goldenInverse : ℝ := (3 - Real.sqrt 5) / 2

/-- The digit of the infinite Fibonacci word at 0-based position `t`
(OEIS A003849), given by the characteristic mechanical formula. -/
def fibInfDigit (t : ℕ) : ℤ :=
  ⌊(((t + 2 : ℕ) : ℝ) * goldenInverse)⌋ - ⌊(((t + 1 : ℕ) : ℝ) * goldenInverse)⌋

/-- The length-`k` factor of the infinite Fibonacci word starting at position `m`. -/
def fibFactor (k m : ℕ) : Fin k → ℤ := fun j => fibInfDigit (m + j.1)

/-- The set of all distinct length-`k` factors of the infinite Fibonacci word. -/
def FactorSet (k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, w = fibFactor k m }

/-- One mechanical digit with rational slope `a` and intercept `x`:
`⌊x + (j+1)a⌋ - ⌊x + j·a⌋`. -/
def mechDigit (a : ℚ) (x : ℚ) (j : ℕ) : ℤ :=
  ⌊(x + (((j + 1 : ℕ) : ℚ) * a : ℚ))⌋ - ⌊(x + (((j : ℕ) : ℚ) * a : ℚ))⌋

/-- The mechanical word indexed by intercept `m` (`x_m = -m·a`), length `k`. -/
def mechWord (a : ℚ) (m k : ℕ) : Fin k → ℤ :=
  fun j => mechDigit a (-((m : ℚ) * a)) j

/-- The set of the `k + 1` mechanical words (intercepts `m = 0..k`). -/
def MechSet (a : ℚ) (k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, m ≤ k ∧ w = mechWord a m k }

/-- The rational slope used for length `k`: `fib(n)/fib(n+2)`, a convergent to
`α = 1/φ²`.  The hypothesis will require `k < fib(n+2)`. -/
def mechSlope (n : ℕ) : ℚ :=
  (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)

/-- The numerator of the slope is nonnegative and the denominator positive, so
the slope lies in `[0,1]` where the mechanical digits are meaningful. -/
theorem slope_mem_Icc (n : ℕ) : (0 : ℚ) ≤ mechSlope n ∧ mechSlope n ≤ 1 := by
  sorry

/-- The middle digit difference is always `0` or `1` for any such slope and
intercept, so the mechanical words are binary words. -/
theorem mech_digit_two_valued (a : ℚ) (x : ℚ) (j : ℕ) :
    (0 : ℤ) ≤ mechDigit a x j ∧ mechDigit a x j ≤ 1 := by
  sorry

/-- The infinite Fibonacci word is a binary word: each digit is `0` or `1`. -/
theorem fib_inf_digit_two_valued (t : ℕ) :
    (0 : ℤ) ≤ fibInfDigit t ∧ fibInfDigit t ≤ 1 := by
  sorry

/-- There are arbitrarily large Fibonacci numbers, so an `n` with
`k < fib(n+2)` always exists (exists for every `k`). -/
theorem exists_slope_denominator (k : ℕ) :
    ∃ n : ℕ, k < Nat.fib (n + 2) := by
  sorry

/-- **Main structural claim (count):** the infinite Fibonacci word has exactly
`k + 1` distinct length-`k` factors (Sturmian factor complexity `p(k) = k+1`). -/
theorem fib_factor_count (k : ℕ) :
    (FactorSet k).ncard = k + 1 := by
  sorry

/-- **Main structural claim (mechanical reproduction):** the mechanical
construction with convergent slope `fib(n)/fib(n+2)` (for any `n` with
`k < fib(n+2)`) produces exactly the length-`k` factors of the infinite
Fibonacci word. -/
theorem mech_reproduces_factors (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    MechSet (mechSlope n) k = FactorSet k := by
  sorry

/-- The `k + 1` mechanical words are distinct: their set has cardinal `k + 1`.
(Combined with `mech_reproduces_factors` and `fib_factor_count`.) -/
theorem mech_set_card (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    (MechSet (mechSlope n) k).ncard = k + 1 := by
  sorry

end PE1006

#print axioms PE1006.fib_factor_count
#print axioms PE1006.mech_reproduces_factors
#print axioms PE1006.mech_set_card
#print axioms PE1006.slope_mem_Icc
#print axioms PE1006.mech_digit_two_valued
#print axioms PE1006.fib_inf_digit_two_valued
#print axioms PE1006.exists_slope_denominator
