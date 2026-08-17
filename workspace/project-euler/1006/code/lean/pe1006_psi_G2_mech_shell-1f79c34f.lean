import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Basic

/-!
# G2 — exact binary shell of the mechanical-word construction (PE1006)

Sorry-free companion of the node statement
`pe1006_psi_G2_mechanical_word_representation-1f79c34f.lean` (which keeps the
gapped deep identity).  This file proves the four theses that pin down the
*object* the node quantifies over, with the **corrected slope**
`a = fib(n)/fib(n+2)` → 1/phi^2 (the literal "a = F(n-1)/F(n)" in the node
text was refuted: `code/refute/G2-slope-refutation.md`):

* `slope_mem_Icc n : 0 ≤ slope n ∧ slope n ≤ 1` — the slope is in `[0,1]`;
* `mechDigit_nonneg` / `mechDigit_succ_le` — a digit is the difference of two
  `Int.floor` values and lies in `{0,1}` whenever `0 ≤ a ≤ 1`;
* `mechWord_binary n k m j (hj : j < k)` — every digit of every mechanical
  word is `0` or `1`, so the k+1 words are honest binary words.

Exactness remark of the node: every quantity is a rational (over `ℚ`,
denominator `fib(n+2)^2` or better) and every floor is an exact integer
(`Int.floor`); no floats anywhere.  Kernel-verified, axioms `propext`,
`Classical.choice`, `Quot.sound` (`#print axioms` at the bottom).
-/

noncomputable section

namespace PE1006G2Shell

/-- `a = fib(n)/fib(n+2)`, the continued-fraction convergents to
`1/phi^2 = (3 - sqrt 5)/2`, in `[0,1]`. -/
def slope (n : ℕ) : ℚ :=
  (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)

/-- The intercept `x_m = -m·a`, the node's cut points `frac(-m·a)`. -/
def intercept (n m : ℕ) : ℚ :=
  -((m : ℚ) * slope n)

/-- `digit_j(x) = ⌊x + (j+1)a⌋ - ⌊x + j·a⌋`, `j = 0..k-1`. -/
def mechDigit (a : ℚ) (x : ℚ) (j : ℕ) : ℤ :=
  ⌊(x + (((j + 1 : ℕ) : ℚ) * a : ℚ))⌋ - ⌊(x + (((j : ℕ) : ℚ) * a : ℚ))⌋

/-- The mechanical word of intercept `m` and length `k`. -/
def mechWord (n k m : ℕ) : Fin k → ℤ :=
  fun j => mechDigit (slope n) (intercept n m) (j : ℕ)

/-- `0 < fib(n+2)`: the denominator of the slope is positive. -/
lemma fib_add_two_pos (n : ℕ) : 0 < Nat.fib (n + 2) := by
  exact (Nat.fib_pos).2 (by omega)

/-- The slope lies in `[0,1]`. -/
theorem slope_mem_Icc (n : ℕ) :
    (0 : ℚ) ≤ slope n ∧ slope n ≤ 1 := by
  constructor
  · unfold slope
    exact div_nonneg (Nat.cast_nonneg _) (le_of_lt (Nat.cast_pos.mpr (fib_add_two_pos n)))
  · unfold slope
    rw [div_le_one]
    · have hN : n ≤ n + 2 := by omega
      exact_mod_cast Nat.fib_mono hN
    · exact_mod_cast fib_add_two_pos n

/-- Digits are nonnegative: floors are nondecreasing, so with `0 ≤ a` the
second floor is at least the first. -/
lemma mechDigit_nonneg (a : ℚ) (x : ℚ) (j : ℕ) (ha0 : 0 ≤ a) :
    (0 : ℤ) ≤ mechDigit a x j := by
  unfold mechDigit
  apply sub_nonneg.mpr
  apply Int.floor_le_floor
  have hj : (0 : ℚ) ≤ (((j + 1 : ℕ) : ℚ) - ((j : ℕ) : ℚ)) := by norm_num
  have hmul : (0 : ℚ) ≤ (((j + 1 : ℕ) : ℚ) - ((j : ℕ) : ℚ)) * a := mul_nonneg hj ha0
  have hx : x + ((j : ℕ) : ℚ) * a ≤ x + ((j + 1 : ℕ) : ℚ) * a := by
    have hstep : ((j : ℕ) : ℚ) * a ≤ ((j + 1 : ℕ) : ℚ) * a := by
      have heq : ((j + 1 : ℕ) : ℚ) * a = ((j : ℕ) : ℚ) * a + (((j + 1 : ℕ) : ℚ) - ((j : ℕ) : ℚ)) * a := by ring
      rw [heq]
      exact le_add_of_nonneg_right hmul
    linarith
  exact hx

/-- Digits are at most 1: with `0 ≤ a ≤ 1`, the second floor exceeds the
first by at most one unit cell. -/
lemma mechDigit_succ_le (a : ℚ) (x : ℚ) (j : ℕ) (ha0 : 0 ≤ a) (ha1 : a ≤ 1) :
    mechDigit a x j ≤ 1 := by
  unfold mechDigit
  have hle : ⌊(x + (((j + 1 : ℕ) : ℚ) * a : ℚ))⌋ ≤ ⌊(x + (((j : ℕ) : ℚ) * a : ℚ))⌋ + 1 := by
    have hstep : x + ((j + 1 : ℕ) : ℚ) * a ≤ (x + ((j : ℕ) : ℚ) * a) + 1 := by
      have h : ((j + 1 : ℕ) : ℚ) * a ≤ ((j : ℕ) : ℚ) * a + 1 := by
        have hj1 : ((j + 1 : ℕ) : ℚ) = ((j : ℕ) : ℚ) + 1 := by norm_num
        rw [hj1]
        ring_nf
        linarith
      linarith
    have hfl := Int.floor_le_floor hstep
    have hconv : ⌊(x + (((j : ℕ) : ℚ) * a : ℚ)) + 1⌋ = ⌊(x + (((j : ℕ) : ℚ) * a : ℚ))⌋ + 1 := by
      rw [Int.floor_add_one]
    simpa [hconv] using hfl
  omega

/-- **Digits are binary**: every digit of every mechanical word is `0` or `1`.
The k+1 mechanical words are honest binary words of length `k`. -/
theorem mechWord_binary (n k m j : ℕ) (hj : j < k) :
    (0 : ℤ) ≤ mechWord n k m ⟨j, hj⟩ ∧ mechWord n k m ⟨j, hj⟩ ≤ 1 := by
  have ha0 : (0 : ℚ) ≤ slope n := (slope_mem_Icc n).1
  have ha1 : slope n ≤ 1 := (slope_mem_Icc n).2
  unfold mechWord
  simpa using ⟨mechDigit_nonneg (slope n) (intercept n m) j ha0,
    mechDigit_succ_le (slope n) (intercept n m) j ha0 ha1⟩

/-! ## Kernel-computed oracle checks (exact `ℚ`/`ℤ`, no floats)

The refutation record's corrected row: for `a = 2/5` the digits of intercept
`m = 0` are `0,0,1` — the factor `001` of the problem's length-3 set
`{001,010,100,101}`.  `native_decide` computes exact floors over `ℚ`. -/

namespace Oracle

open PE1006G2Shell

example : mechDigit (2 / 5 : ℚ) (intercept 3 0) 0 = 0 := by
  native_decide

example : mechDigit (2 / 5 : ℚ) (intercept 3 0) 1 = 0 := by
  native_decide

example : mechDigit (2 / 5 : ℚ) (intercept 3 0) 2 = 1 := by
  native_decide

end Oracle

end PE1006G2Shell

end

#print axioms PE1006G2Shell.slope_mem_Icc
#print axioms PE1006G2Shell.mechDigit_nonneg
#print axioms PE1006G2Shell.mechDigit_succ_le
#print axioms PE1006G2Shell.mechWord_binary