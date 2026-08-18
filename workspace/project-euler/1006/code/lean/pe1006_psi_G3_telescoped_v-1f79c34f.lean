import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Set.Basic

/-!
# G3 — telescoped `v(x)` identity (PE1006)

The run computes `Psi(10^18) mod 101001001` via the second-moment floor-sum
monoid.  The string value of the mechanical word is

    v(x) = sum_{j=0}^{k-1} digit_j(x) * 10^(k-1-j),
    digit_j(x) = floor(x + (j+1)a) - floor(x + j a).

The monoid works with **geometrically weighted** `floor` sums, so the run
replaces the digit-weighted sum by its *telescoped* form: each digit is a
difference of two consecutive floors, and gathering the coefficient of every
`floor(x + l·a)` gives

    v(x) = floor(x + k a) - 10^(k-1) floor(x)
           + 9 * sum_{l=1}^{k-1} 10^(k-1-l) floor(x + l a).

Coefficient check (l = 0..k, the only floors present): LHS coefficient of
`floor(x+l a)` is `+10^(k-l)` from the `(j+1)a` term at `j = l-1` (l = 1..k)
minus `10^(k-1-l)` from the `j·a` term at `j = l` (l = 0..k-1).  For `l = 0`
this is `-10^(k-1)`; for `l = k` it is `+10^0 = 1`; for `1 ≤ l ≤ k-1` it is
`10^(k-l) - 10^(k-1-l) = (10-1)·10^(k-1-l) = 9·10^(k-1-l)`.  Hence the two
sides agree — an exact identity over `ℤ` for any slope `a` and intercept `x`.

The hypotheses `1 ≤ k` and `0 < a < 1` are stated as the run specifies them
(they are not needed for the algebra — the identity is unconditional in `a`)
but are the regime the monoid operates in.

This file states the identity; the proof is the declared gap `by sorry`
(the deliverable here is the complete, kernel-checked STATEMENT).  Groundwork
already checked: the binary/digit shell in
`pe1006_psi_G2_mech_shell-1f79c34f.lean` proves `digit ∈ {0,1}` and the slope
`∈ [0,1]`.
-/

noncomputable section

open scoped BigOperators

namespace PE1006G3

/-- `digit_j(x) = floor(x + (j+1)a) - floor(x + j a)`, the mechanical-word
digit at position `j` for slope `a` and intercept `x`. -/
def digit (a : ℚ) (x : ℚ) (j : ℕ) : ℤ :=
  ⌊(x + (((j + 1 : ℕ) : ℚ) * a : ℚ))⌋ - ⌊(x + (((j : ℕ) : ℚ) * a : ℚ))⌋

/-- The digit-weighted word value: `v(x) = sum_{j=0}^{k-1} digit_j(x) 10^(k-1-j)`. -/
def wordVal (a : ℚ) (x : ℚ) (k : ℕ) : ℤ :=
  ∑ j ∈ Finset.range k, digit a x j * (10 : ℤ) ^ (k - 1 - j)

/-- The telescoped form:
`v(x) = floor(x + k a) - 10^(k-1) floor(x)
        + 9 * sum_{l=1}^{k-1} 10^(k-1-l) floor(x + l a)`.
For `k = 1` the middle sum is empty and the identity reads
`v = floor(x+a) - floor x` (the single-digit case). -/
def telescoped (a : ℚ) (x : ℚ) (k : ℕ) : ℤ :=
  ⌊(x + (((k : ℕ) : ℚ) * a : ℚ))⌋ - (10 : ℤ) ^ (k - 1) * ⌊x⌋ +
    9 * (∑ l ∈ Finset.Icc 1 (k - 1), (10 : ℤ) ^ (k - 1 - l) * ⌊(x + (((l : ℕ) : ℚ) * a : ℚ))⌋)

/-- **G3 telescoped-`v` identity.**  For slope `a` rational in `(0,1)` and
`k ≥ 1`, the digit-weighted mechanical word value equals its telescoped
second-moment form.  Independent of `a` and `x` algebraically; the hypotheses
are the run's operating regime. Proof left as the declared gap. -/
theorem telescoped_v_identity (a x : ℚ) (k : ℕ)
    (hk : 1 ≤ k) (ha0 : 0 < a) (ha1 : a < 1) :
    wordVal a x k = telescoped a x k := by
  sorry

end PE1006G3

end

#print axioms PE1006G3.telescoped_v_identity
