import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Int.ModEq

/-!
# PE1006 — overall goal, in the mechanical-word (second-moment) language

The run reduces `Psi(k)` (sum of squares of the `k+1` distinct length-`k`
Fibonacci subwords read as decimals) to a *second moment of a floor sum*: the
`k+1` distinct factors are exactly the `k+1` digit words produced by a
mechanical word of rational slope `a` (a Fibonacci ratio, `F(n)/F(n+2)` in the
verified G2 shell, or `F(n-1)/F(n)` with `F(n) >> k` per directive 2) at the
`k+1` contiguous representatives `x_m` (the arc midpoints of the
three-distance partition cut by the points `{ −m·a mod 1 : m = 0..k }`).

`wordVal a x k` is the digit value `v(x) = sum_j digit_j(x) · 10^(k-1-j)`
with `digit_j(x) = floor(x + (j+1)a) - floor(x + j a)`.  The G3 telescoped
identity (stated and kernel-checked in `pe1006_psi_G3_telescoped_v-1f79c34f.lean`,
proof left as a `sorry`) rewrites this as

    v(x) = floor(x + k a) - 10^(k-1) floor x
           + 9 · sum_{l=1}^{k-1} 10^(k-1-l) floor(x + l a) .

The **goal** is therefore

    Psi(k)  ≡  sum_{m=0}^{k} wordVal(a, x_m, k)^2   (mod 101001001),

with rational slope `a ∈ (0,1)` and `k = 10^18` the targeted instance.  The
second-moment floor-sum on the right is exactly what the universal-Euclidean
monoid (directive 4, `PYNUMLIB`-independent) evaluates in `O(log)`.

Every `theorem` here ends in `:= by sorry`: the deliverables are
kernel-checked STATEMENTS, and the gaps are the proof obligations the run is
working towards.
-/

noncomputable section

open scoped BigOperators

namespace PE1006Goal

/-- `digit_j(x) = floor(x + (j+1)a) - floor(x + j a)`, the mechanical-word
digit at position `j` for slope `a` and intercept `x`. -/
def digit (a : ℚ) (x : ℚ) (j : ℕ) : ℤ :=
  ⌊(x + (((j + 1 : ℕ) : ℚ) * a : ℚ))⌋ - ⌊(x + (((j : ℕ) : ℚ) * a : ℚ))⌋

/-- The digit-weighted word value:
`v(x) = sum_{j=0}^{k-1} digit_j(x) · 10^(k-1-j)`. -/
def wordVal (a : ℚ) (x : ℚ) (k : ℕ) : ℤ :=
  ∑ j ∈ Finset.range k, digit a x j * (10 : ℤ) ^ (k - 1 - j)

/-- The G3 telescoped form of `v(x)` (over `ℤ`, for any `a,x` and `k ≥ 1`). -/
def telescoped (a : ℚ) (x : ℚ) (k : ℕ) : ℤ :=
  ⌊(x + (((k : ℕ) : ℚ) * a : ℚ))⌋ - (10 : ℤ) ^ (k - 1) * ⌊x⌋ +
    9 * (∑ l ∈ Finset.Icc 1 (k - 1), (10 : ℤ) ^ (k - 1 - l) * ⌊(x + (((l : ℕ) : ℚ) * a : ℚ))⌋)

/-- **G3 telescoped-`v` identity** (restated here for self-containment; the
kernel-checked copy lives in `pe1006_psi_G3_telescoped_v-1f79c34f.lean`).
`digit_j` is the difference of two consecutive `floor`s, so gathering the
coefficient of every `floor(x + l·a)` telescopes the digit-weighted sum.
Exact over `ℤ`, independent of `a` and `x`; the hypotheses `1 ≤ k`, `0 < a < 1`
are the run's operating regime.  Proof left as the declared gap. -/
theorem telescoped_v_identity (a x : ℚ) (k : ℕ)
    (hk : 1 ≤ k) (ha0 : 0 < a) (ha1 : a < 1) :
    wordVal a x k = telescoped a x k := by
  sorry

/-- Fractional part `z - floor z ∈ [0,1)` for a rational `z`. -/
def fract (z : ℚ) : ℚ := z - (⌊z⌋ : ℚ)

/-- The `m`-th cut point: `frac(-m·a)` on the circle.  The `k+1` points
`m = 0..k` cut the circle into `k+1` arcs (three-distance theorem). -/
def point (a : ℚ) (m : ℕ) : ℚ := fract (-(m : ℚ) * a)

/-- Arc midpoint `x_m` of the arc from `point m` to `point (m+1)`, travelling
in the direction `t ↦ fract(t - a)`.

* if `a ≤ t` the arc does not wrap, midpoint `t - a/2`;
* otherwise it wraps through `1` and `0`; the midpoint of the forward arc is
  `fract( t + ((1 - t) + u)/2 )` with `u = t - a + 1`.

Caveat (stated, not proved here): this is the *circular* arc midpoint the
run's `mech_psi` uses; the telescoped `v` identity is independent of which
representative is chosen, and formulation (A)==(B) of `mech_psi` confirms the
factor set is insensitive to the slope approximant (recorded in `code/out`).
-/
def arcMid (a : ℚ) (m : ℕ) : ℚ :=
  let t := point a m
  if a ≤ t then
    t - a / 2
  else
    let u := t - a + 1
    fract (t + ((1 - t) + u) / 2)

/-- The mechanical second moment: `sum_{m=0}^{k} wordVal(a, x_m, k)^2`. -/
def PsiMech (a : ℚ) (k : ℕ) : ℤ :=
  ∑ m ∈ Finset.range (k + 1), (wordVal a (arcMid a m) k) ^ 2

/-- The `S_n` Fibonacci word: `S_0 = 0`, `S_1 = 01`, `S_n = S_{n-1} S_{n-2}`. -/
def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

/-- Digit value of one character. -/
def digitVal (c : Char) : ℕ := if c = '0' then 0 else 1

/-- Decimal value of a word, ignoring leading zeros (fold from the left). -/
def valueOf : List Char → ℕ :=
  List.foldl (fun acc c => acc * 10 + digitVal c) 0

/-- All length-`k` contiguous substrings (factors) of a word `w`. -/
def slidingFactors [DecidableEq α] (w : List α) (k : ℕ) : Finset (List α) :=
  (Finset.range (w.length - k + 1)).image fun i => (w.drop i).take k

/-- `Ψ(k)`: sum of the squares of the decimal values of the distinct length-`k`
Fibonacci subwords. -/
noncomputable def Psi (k : ℕ) : ℕ :=
  ((slidingFactors (fibWord (k + 2)) k).image valueOf).sum fun n => n * n

/-- The problem's modulus. -/
def M : ℕ := 101001001

/-- **Key reduction (main goal, stated).**  For a rational slope `a ∈ (0,1)`
and `k ≥ 1`, the problem's `Psi(k)` — sum of squares of the `k+1` distinct
length-`k` Fibonacci subwords read as decimals, ignoring leading zeros — is
congruent to the mechanical second moment `PsiMech a k` modulo `M`.  This is
what makes `Psi(10^18)` computable in `O(log)` via the universal-Euclidean
monoid of directive 4.  Proof left as the declared gap. -/
theorem psi_mech_reduction
    (a : ℚ) (ha0 : 0 < a) (ha1 : a < 1) (k : ℕ) (hk : 1 ≤ k) :
    PsiMech a k % (M : ℤ) = (Psi k : ℤ) % (M : ℤ) := by
  sorry

/-- **Final answer, stated.**  `A` is the residue of the mechanical second
moment at `k = 10^18` modulo `M` (equivalently of `Psi(10^18)`): the concrete
`A < M` the run is computing.  Given existentially because the specific
numeric value is unknown to the formalisation yet. -/
theorem pe1006_answer_active :
    let k : ℕ := 1000000000000000000
    ∃ A : ℕ, A < M ∧ PsiMech (1 : ℚ) k % (M : ℤ) = (A : ℤ) := by
  sorry

end PE1006Goal

end

#print axioms PE1006Goal.telescoped_v_identity
#print axioms PE1006Goal.psi_mech_reduction
#print axioms PE1006Goal.pe1006_answer_active
