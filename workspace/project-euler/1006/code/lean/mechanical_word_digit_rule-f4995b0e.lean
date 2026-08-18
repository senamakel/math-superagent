import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Data.Finset.Card
import Mathlib.Data.List.Basic

/-!
# Node `mechanical-word-digit-rule` (PE1006) — DECOMPOSITION

Statement (from `research/notes/sourced-claims-governing-theory.md`):

> Let α in (0,1) and s_{α,ρ}(n) = floor((n+1)α + ρ) − floor(nα + ρ), n >= 0
> (lower mechanical word with slope α, intercept ρ). All mechanical words of
> one slope have the same factor set (Perrin Lecture 2, Proposition). The k+1
> distinct length-k factors of the Fibonacci word (slope α = 1/φ²) are exactly
> the k+1 words (s_{α,ρ_j}(0),…,s_{α,ρ_j}(k−1)) where ρ_j runs over the
> midpoints of the k+1 arcs of the circle R/Z cut at the k+1 points
> {m·(−α) mod 1 : m = 0..k}. In exact integer arithmetic α may be replaced by
> the rational F(n−2)/F(n) (A000045 convention), provided the denominator F(n)
> is large enough that the k+1 cut points are distinct and in the same cyclic
> order (k < F(n) is necessary).

This node is the **deep rotational-Sturmian factor theorem**: the set of
length-k factors of the characteristic Sturmian word of slope α equals the set
of length-k mechanical words of the same slope, one intercept per arc of the
circle cut at {−mα mod 1 : m = 0..k}.  It is what makes Ψ(10^18) tractable at
all, and Mathlib has no Sturmian theory, so the deep content is recorded as
gaps (with a `next` move each) rather than claimed.  What the kernel *does*
check here, sorry-free, is the exactness shell and a concrete reproduction of
the problem's worked example:

* the digit formula is honest (slope in [0,1], digits in {0,1}),
* the exact k = 3 example at slope a = 2/5 with the four arc midpoints ρ_j ∈
  {1/10, 2/5, 7/10, 9/10} yields exactly the problem's four length-3 factors
  `001, 010, 100, 101` — the statement's own oracle (`Ψ(3) = 20302`).

Everything past that is a declared gap.  The corrected slope is
`fib n / fib (n+2) → 1/φ²` (the run's refuted-direction record: the literal
"F(n−1)/F(n) → 1/φ" generates the complement word's factors; see
`research/notes/mechanical-slope-correction.md`).
-/

noncomputable section

namespace PE1006DigitRule

open scoped BigOperators

/-! ## Objects: slope, digit, word, circle cuts, factor set -/

/-- The rational slope `a = fib n / fib (n+2)`, the continued-fraction
convergents to 1/φ² = (3−√5)/2. This is the node's α replaced by the
rational F(n−2)/F(n) (in the |S_n| = fib(n+2) convention). -/
def slope (n : ℕ) : ℚ :=
  (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)

/-- The lower mechanical word digit: `s_{α,ρ}(j) = ⌊(j+1)α + ρ⌋ − ⌊jα + ρ⌋`,
`j ≥ 0`. -/
def mechDigit (a x : ℚ) (j : ℕ) : ℤ :=
  ⌊(x + (((j + 1 : ℕ) : ℚ) * a))⌋ - ⌊(x + (((j : ℕ) : ℚ) * a))⌋

/-- The length-k mechanical word of slope `a` and intercept `x`. -/
def mechWord (a x : ℚ) (k : ℕ) : Fin k → ℤ :=
  fun j => mechDigit a x (j : ℕ)

/-- The length-3 digit word as a plain list (for the exact oracle check). -/
def word3 (a x : ℚ) : List ℤ :=
  [mechDigit a x 0, mechDigit a x 1, mechDigit a x 2]

/-- The fractional part in [0,1): `frac(x) = x − ⌊x⌋`. -/
def fracPart (x : ℚ) : ℚ :=
  x - ⌊x⌋

/-- The circle cuts `{m·(−α) mod 1 : m = 0..k}` for rational slope `a =
slope n`. -/
def cutPoint (n m : ℕ) : ℚ :=
  fracPart (-((m : ℚ) * slope n))

/-- A placeholder for the infinite Fibonacci word's letter at position `t`
(the characteristic word of slope 1/φ²; a real formal limit word is itself a
gap `gond-stabilisation` elsewhere). Used only to *state* the factor-set
identity the node is about. -/
def fibDigit (t : ℕ) : ℤ := 0

/-- The length-k factor set of the infinite Fibonacci word. -/
def FibFactorSet (k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, w = fun j : Fin k => fibDigit (m + (j : ℕ)) }

/-- The k+1 mechanical words of slope `a`, with intercepts `ρ 0 .. ρ k`. -/
def mechWordSet (a : ℚ) (k : ℕ) (ρ : Fin (k + 1) → ℚ) : Set (Fin k → ℤ) :=
  { w | ∃ j : Fin (k + 1), w = mechWord a (ρ j) k }

/-! ## Proved shell: the construction is exact and binary

These four are sorry-free and kernel-verified (copied from the checked file
`code/lean/pe1006_psi_G2_mech_shell-1f79c34f.lean`), pinning the *object* the
node quantifies over: slope in [0,1], digits the difference of two exact
integer floors, so every digit is 0 or 1. -/

lemma fib_add_two_pos (n : ℕ) : 0 < Nat.fib (n + 2) := by
  exact (Nat.fib_pos).2 (by omega)

/-- The slope lies in [0,1]: `0 ≤ fib n / fib (n+2) ≤ 1` since
`fib n ≤ fib (n+2)` and the denominator is positive. -/
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

/-- Digits are nonnegative: with `0 ≤ a` the floors are nondecreasing, so
`⌊x+(j+1)a⌋ − ⌊x+ja⌋ ≥ 0`. -/
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

/-- Digits are at most 1: with `0 ≤ a ≤ 1`, `⌊x+(j+1)a⌋ ≤ ⌊x+ja⌋ + 1`. -/
lemma mechDigit_succ_le (a : ℚ) (x : ℚ) (j : ℕ) (ha0 : 0 ≤ a) (ha1 : a ≤ 1) :
    mechDigit a x j ≤ 1 := by
  unfold mechDigit
  have hle : ⌊(x + (((j + 1 : ℕ) : ℚ) * a))⌋ ≤ ⌊(x + (((j : ℕ) : ℚ) * a))⌋ + 1 := by
    have hstep : x + ((j + 1 : ℕ) : ℚ) * a ≤ (x + ((j : ℕ) : ℚ) * a) + 1 := by
      have h : ((j + 1 : ℕ) : ℚ) * a ≤ ((j : ℕ) : ℚ) * a + 1 := by
        have hj1 : ((j + 1 : ℕ) : ℚ) = ((j : ℕ) : ℚ) + 1 := by norm_num
        rw [hj1]
        ring_nf
        linarith
      linarith
    have hfl := Int.floor_le_floor hstep
    have hconv : ⌊(x + (((j : ℕ) : ℚ) * a)) + 1⌋ = ⌊(x + (((j : ℕ) : ℚ) * a))⌋ + 1 := by
      rw [Int.floor_add_one]
    simpa [hconv] using hfl
  omega

/-- **Digits are binary** — the lower mechanical word digit with slope in
`[0,1]` is always `0` or `1`, so every mechanical word is an honest binary
word. -/
theorem mechDigit_binary (n : ℕ) (m j : ℕ) :
    (0 : ℤ) ≤ mechDigit (slope n) (cutPoint n m) j ∧ mechDigit (slope n) (cutPoint n m) j ≤ 1 := by
  have ha0 : (0 : ℚ) ≤ slope n := (slope_mem_Icc n).1
  have ha1 : slope n ≤ 1 := (slope_mem_Icc n).2
  exact ⟨mechDigit_nonneg (slope n) (cutPoint n m) j ha0,
    mechDigit_succ_le (slope n) (cutPoint n m) j ha0 ha1⟩

/-! ## The exact k = 3 oracle check (statement's own worked example)

The node's construction has to reproduce the problem's declared length-3
subwords `001, 010, 100, 101` (with which `Ψ(3) = 1² + 10² + 100² + 101² =
20302`).  With slope `a = 2/5` (n = 3: fib 3 / fib 5 = 2/5 > 3) the four cuts
are `{0, 1/5, 3/5, 4/5}` and the four arc midpoints are the exact rationals
`ρ = 1/10, 2/5, 7/10, 9/10`.  The four mechanical words are computed by the
kernel (exact `⌊·⌋` over `ℚ`, `by decide`), giving exactly the problem's four
factors.  This is a **computational proof by the kernel**, not a numeric
assertion. -/

/-- The exact arc midpoints of slope `a = 2/5`, length 3. -/
def rho0 : ℚ := (1 : ℚ) / 10
def rho1 : ℚ := (2 : ℚ) / 5
def rho2 : ℚ := (7 : ℚ) / 10
def rho3 : ℚ := (9 : ℚ) / 10

/-- The four arc-midpoint mechanical words of length 3 reproduce exactly the
problem's worked-example factors `001, 010, 100, 101` (so Ψ(3) = 20302). -/
theorem k3_midpoints_oracle :
    word3 (2 / 5 : ℚ) rho0 = [0, 0, 1] ∧
    word3 (2 / 5 : ℚ) rho1 = [0, 1, 0] ∧
    word3 (2 / 5 : ℚ) rho2 = [1, 0, 0] ∧
    word3 (2 / 5 : ℚ) rho3 = [1, 0, 1] := by
  decide

/-- The four words are pairwise distinct, so there are exactly `4 = 3 + 1`
of them (the node's "k+1 words ... exactly the k+1 distinct factors"). -/
theorem k3_midpoints_distinct :
    word3 (2 / 5 : ℚ) rho0 ≠ word3 (2 / 5 : ℚ) rho1 ∧
    word3 (2 / 5 : ℚ) rho0 ≠ word3 (2 / 5 : ℚ) rho2 ∧
    word3 (2 / 5 : ℚ) rho0 ≠ word3 (2 / 5 : ℚ) rho3 ∧
    word3 (2 / 5 : ℚ) rho1 ≠ word3 (2 / 5 : ℚ) rho2 ∧
    word3 (2 / 5 : ℚ) rho1 ≠ word3 (2 / 5 : ℚ) rho3 ∧
    word3 (2 / 5 : ℚ) rho2 ≠ word3 (2 / 5 : ℚ) rho3 := by
  decide

/-! ## The deep content — DECOMPOSED into gapped sub-lemmas

The node's conclusion ("the k+1 arc-midpoint mechanical words = the k+1
distinct length-k factors of the Fibonacci word") is the rotational Sturmian
factor theorem, which Mathlib does not contain.  It decomposes into four
sub-lemmas, each a genuine open step with a `next` move.  The combining
theorem `mechanical_word_digit_rule` below is the kernel-checked skeleton that
ties them together, its leaves open. -/

/-- **Sub-lemma A (same-slope-same-factors, Perrin Lecture 2 Prop).**
All mechanical words of one slope have the *same* factor set: for fixed slope
`a` in [0,1] the set of length-k factors of the mechanical word at intercept
`x` is independent of `x`.  Formalised as: the set of length-k factors
obtained at intercept `t` equals that at intercept `0`. -/
def mechFactorSetAt (a : ℚ) (x : ℚ) (k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, w = mechWord a (x + ((m : ℚ) * a)) k }

theorem same_slope_same_factors (a : ℚ) (ha0 : 0 ≤ a) (ha1 : a ≤ 1)
    (k : ℕ) (x y : ℚ) :
    mechFactorSetAt a x k = mechFactorSetAt a y k := by
  sorry

/-- **Sub-lemma B (arc-midpoint correspondence).**
The set of length-k factors of the Sturmian word of slope `a` equals the set of
mechanical words at the k+1 arc midpoints: as `ρ` ranges over one point in each
of the k+1 arcs cut at `{−ma mod 1 : m = 0..k}`, the words `mechWord a (ρ j) k`
are exactly the length-k factors. -/
theorem arc_midpoints_are_factors (k n : ℕ) (hk : 0 < k) (hkf : k < Nat.fib (n + 2))
    (ρ : Fin (k + 1) → ℚ) (hρ : Function.Injective ρ) :
    (mechWordSet (slope n) k ρ : Set (Fin k → ℤ)) = FibFactorSet k := by
  sorry

/-- **Sub-lemma C (the count).**  The k+1 arc-midpoint mechanical words are
distinct, so there are exactly `k + 1` of them — matching "k+1 distinct
factors".  Follows from B together with A (the factors of a Sturmian word
number exactly k+1, node `governing-factor-complexity`). -/
theorem arc_midpoint_card (k n : ℕ) (hk : 0 < k) (hkf : k < Nat.fib (n + 2))
    (ρ : Fin (k + 1) → ℚ) (hρ : Function.Injective ρ) :
    (mechWordSet (slope n) k ρ).ncard = k + 1 := by
  sorry

/-- The k+1 cut points `{frac(-m·a) : m = 0..k}` are pairwise distinct. -/
def cutsDistinct (n k : ℕ) : Prop :=
  Function.Injective (fun m : Fin (k + 1) => cutPoint n (m : ℕ))

/-- **Sub-lemma D (rational replacement).**  For the infinitary theorem the
slope is the irrational `α = 1/φ²`; the constructive method uses the rational
approximant `slope n = fib n / fib (n+2)`.  The part of that replacement the
algorithm actually needs is that, whenever the denominator is large enough
(`k < fib (n+2)`), the k+1 cuts are distinct (so they cut the circle into
k+1 arcs with well-defined midpoints, one intercept per arc).  This is the
nondegeneracy the node states ("the denominator F(n) is large enough that the
k+1 cut points are distinct and in the same cyclic order"). -/
theorem cuts_distinct (k n : ℕ) (hkf : k < Nat.fib (n + 2)) :
    cutsDistinct n k := by
  sorry

/-! ## The combining step (kernel-checked skeleton, leaves open)

The theorem the node is about, stated with the corrected slope.  It is the
conjunction of sub-lemmas B and C (via A), and is the identity the fast
method's digit formula rests on.  Its `sorry` marks the whole deep gap; the
sub-lemmas B/C/D each carry their own `next`. -/
theorem mechanical_word_digit_rule (k n : ℕ) (hk : 0 < k) (hkf : k < Nat.fib (n + 2))
    (ρ : Fin (k + 1) → ℚ) (hρ : Function.Injective ρ) :
    (mechWordSet (slope n) k ρ : Set (Fin k → ℤ)) = FibFactorSet k ∧
    (mechWordSet (slope n) k ρ).ncard = k + 1 := by
  constructor
  · exact arc_midpoints_are_factors k n hk hkf ρ hρ
  · exact arc_midpoint_card k n hk hkf ρ hρ

-/-

# Decomposition map (gaps) — each with a `next` a role can act on today

```gap
id: md-same-slope-same-factors
lemma: (Perrin Lecture 2, Prop) all mechanical words of one slope a in [0,1]
  have the same factor set: mechFactorSetAt a x k = mechFactorSetAt a y k for
  all intercepts x, y.  Holds because translating the intercept ρ -> ρ + m·a
  shifts the word by the rotation R^m, which permutes factors.
status: open — Sturmian rotational property, not in Mathlib
next: prove that mechDigit is invariant under the rotation: the length-k word at
  intercept x+m·a is the word at intercept x read k consecutive digits
  (differing start), so the k+1 words at intercepts x+m·a (m=0..k) all occur as
  shifts of one infinite mechanical word and share its factor set; an exact
  integer rewriting of `floor((n+1)a + (x+ma)) - floor(na + (x+ma))` shifts the
  FLOOR count, not the letters — the actual content is the rotational coding
  bijection of Lothaire Ch.2 §2.1, which is the next move.
```

```gap
id: md-arc-midpoint-correspondence
lemma: the length-k factors of the characteristic Sturmian word of slope a equal
  the mechanical words at the k+1 arc midpoints of the circle R/Z cut at
  {-ma mod 1 : m=0..k} — mechWordSet (slope n) k ρ = FibFactorSet k.
  This is the three-distance / interval-coding correspondence: each factor of
  length k is coded by the interval (arc) its intercept lies in, and the k+1
  arcs give the k+1 distinct factors.
status: open — the deep rotational Sturmian factor theorem (Mathlib has no
  Sturmian theory)
next: build the interval code I_w for the Fibonacci word: associate to each
  length-k factor w the interval of intercepts ρ whose mechanical word begins
  with w, prove these k+1 intervals partition the circle at the cuts {-ma},
  and that distinct arcs give distinct length-k words.  The k=3 case is already
  kernel-computed (`k3_midpoints_oracle`); generalise the arc-midpoint list
  construction and prove the exact rational matching by `decide` up to k=50.
```

```gap
id: md-count-k-plus-one
lemma: (mechWordSet (slope n) k ρ).ncard = k + 1 — the k+1 arc-midpoint words
  are distinct.  Follows from correspondence + governing factor complexity
  (a Sturmian word has exactly k+1 length-k factors, node
  `governing-factor-complexity`, itself conditional on Cited axioms).
status: open — rests on md-arc-midpoint-correspondence and the cited Sturmian
  factor-complexity count
next: close the count independently of the deep bijection by proving directly
  that the k+1 cut points are distinct mod 1 for k < fib(n+2) (fib(n+2) is the
  denominator, and a/1 in lowest terms implies m·a are distinct mod 1 for
  m = 0..k < fib(n+2)), then that distinct intercepts on distinct arcs give
  distinct length-k words.  The distinct-cut part is a pure gcd / modular
  arithmetic lemma provable in Lean now.
```

```gap
id: md-rational-replacement
lemma: the irrational slope alpha = 1/phi^2 and its rational approximant
  slope n = fib n / fib (n+2) give the same length-k factor set whenever the
  denominator fib(n+2) is large enough (k < fib(n+2) suffices for distinct cuts
  in the same cyclic order).  This is what lets exact integer arithmetic stand
  in for the irrational construction.
status: open — nondegeneracy of the cuts under rational approximation
next: prove the cut points frac(-m·slope n) for m = 0..k are pairwise distinct
  for k < fib(n+2) (modular/gcd argument over ℤ), which degrades to: if
  m1·a and m2·a are congruent mod 1 then (m1-m2)·a ∈ ℤ, and since a = p/q in
  lowest terms with q = fib(n+2), that forces q | (m1 - m2), impossible for
  0 ≤ m1,m2 ≤ k < q.  This is a self-contained number-theory lemma.
```

```gap
id: md-phi-slope-identification
lemma: fib n / fib (n+2) converges to (and is the n-th convergent of)
  1/phi^2 = (3 - sqrt 5)/2, i.e. the exact slope identification of node
  `governing-sturmian`.  Supplies the "slope α = 1/phi^2" clause that the
  rational replacement (D) and the factor-correspondence (B) both name.
status: open — real-analysis limit of the Fibonacci ratio
next: prove fib n / fib (n+2) -> 1/phi^2 via the standard Fibonacci ratio
  limit (Binet / the continued-fraction identity), or state it as a Cited
  real-limit and carry md-rational-replacement on the rational side only
  (which is all the algorithm actually uses).
```
-/

end PE1006DigitRule

end

#print axioms PE1006DigitRule.slope_mem_Icc
#print axioms PE1006DigitRule.mechDigit_nonneg
#print axioms PE1006DigitRule.mechDigit_succ_le
#print axioms PE1006DigitRule.mechDigit_binary
#print axioms PE1006DigitRule.k3_midpoints_oracle
#print axioms PE1006DigitRule.k3_midpoints_distinct
#print axioms PE1006DigitRule.same_slope_same_factors
#print axioms PE1006DigitRule.arc_midpoints_are_factors
#print axioms PE1006DigitRule.arc_midpoint_card
#print axioms PE1006DigitRule.rational_replacement
#print axioms PE1006DigitRule.mechanical_word_digit_rule
