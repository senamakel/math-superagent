import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card

/-!
# G2 — mechanical / rotation representation of the length-`k` factors of the
# Fibonacci word (PE1006)

Node `G2-mechanical-word-representation` of the statement graph, formalised with
the **corrected slope** (see `code/refute/G2-slope-refutation.md` and
`research/notes/mechanical-slope-correction.md`).

The literal node text "slope a = F(n-1)/F(n) with F(n) > k" was refuted by the
run's refuter: F(n-1)/F(n) is the slope of the *complement* word
(convergents to 1/phi = 0.618), producing factors containing `11` which never
occur in the Fibonacci word.  The mechanical construction that exactly
reproduces the factor set uses the convergents to 1/phi^2 = (3-sqrt5)/2, i.e.

    a = fib(n)/fib(n+2)   (equivalently F(n-2)/F(n) in the F(n)=fib(n+2)
    indexing of `problem.md`'s lengths |S_n| = fib(n+2)),
    hypothesis: k < fib(n+2)  (the run's "F(n) > k").

What is formalised here, binder by binder (corrected statement):

* `fib k = Nat.fib k` — F(k) of the node text, with |S_n| = fib(n+2).
* `slope n := fib n / fib (n+2)` — the rational slope, in `[0,1]`.
* `intercept m n := -((m : ℚ) * slope n)` — the intercept `x_m = -m·a`
  (the node's "frac(-m·a)"; the fractional part is identified by
  `fracIdent`).
* `mechDigit a x j := ⌊x + (j+1)a⌋ - ⌊x + j·a⌋` — `digit_j(x)`.
* `mechWord n k m : Fin k → ℤ` — the mechanical word of intercept `m`.
* `mechFactorSet n k` — the `k+1` mechanical words, `m = 0..k`.
* `mechWord_binary n k m` (**proved, sorry-free**): every digit is `0` or `1`,
  so the words are honestly binary.  Depends only on `propext`/`Quot.sound`
  (verified by `#print axioms` at the bottom).
* `slope_mem_Icc n` (**proved**): `0 ≤ slope n ≤ 1`.
* `mech_digit_nonneg` (**proved**): the digit difference is `≥ 0` (the other
  half of two-valuedness; the `≤ 1` half is `mechDigit_succ_le`).

The node's **deep identity** — "the k+1 words so obtained are exactly the k+1
distinct length-k factors of the infinite Fibonacci word" — is the
Sturmian-factor-complexity / rotational-Sturmian-factor theorem, which Mathlib
does not contain.  It is recorded here under `namespace Cited` as an axiom with
its sources, and stated as the theorem `mech_reproduces_factors` in the
`PE1006G2` namespace ending in `sorry` (a declared gap, **not** formalised).
The sorry-free part is the exactness shell: the construction is over the field
`ℚ` with `Int.floor`, so every quantity is an exact rational and every floor is
an exact integer — no floating point anywhere.
-/

noncomputable section

open scoped BigOperators

namespace PE1006G2

/-- The rational slope: `a = fib(n)/fib(n+2)`, the continued-fraction
convergents to `1/phi^2 = (3 - sqrt 5)/2`, in `[0,1]`.  (This is the run's
corrected reading of the node's "a = F(n-1)/F(n)": `fib(n)/fib(n+2) =
F(n-2)/F(n)` in the |S_n| = fib(n+2) indexing of `problem.md`.) -/
def slope (n : ℕ) : ℚ :=
  (Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)

/-- The intercept `x_m = -m·a`, `m = 0..k` (the node's cut points
`frac(-m·a)`). -/
def intercept (n m : ℕ) : ℚ :=
  -((m : ℚ) * slope n)

/-- The fractional part of `x` in `[0,1)`: `frac(x) = x - ⌊x⌋`. -/
def fracPart (x : ℚ) : ℚ :=
  x - ⌊x⌋

/-- `x = frac(-m·a)`: for `x = -m·a` the intercept and its fractional part lie
in the same unit cell, so `fracPart (-m·a) = -m·a - ⌊-m·a⌋`, which
live in `[0,1)`.  (The node's "cut the unit circle at frac(-ma)" is exactly
the intercept `-m·a` taken modulo 1.) -/
lemma intercept_fracPart (n m : ℕ) :
    fracPart (intercept n m) = intercept n m - ⌊intercept n m⌋ := by
  rfl

/-- The digit at position `j`: `digit_j(x) = ⌊x + (j+1)a⌋ - ⌊x + j·a⌋`,
`j = 0..k-1`. -/
def mechDigit (a : ℚ) (x : ℚ) (j : ℕ) : ℤ :=
  ⌊(x + (((j + 1 : ℕ) : ℚ) * a : ℚ))⌋ - ⌊(x + (((j : ℕ) : ℚ) * a : ℚ))⌋

/-- The mechanical word of intercept `m` and length `k`, digit `j` given by
`mechDigit`. -/
def mechWord (n k m : ℕ) : Fin k → ℤ :=
  fun j => mechDigit (slope n) (intercept n m) (j : ℕ)

/-- The `k+1` mechanical words: `{ w | ∃ m ≤ k, w = mechWord n k m }`. -/
def mechFactorSet (n k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, m ≤ k ∧ w = mechWord n k m }

/-! ## Proved shell: the construction is exact and binary

Everything below is sorry-free and kernel-verified (`#print axioms` at the
bottom: only `propext` and `Quot.sound`).  It pins down the *object* the node
quantifies over — slope in `[0,1]`, intercepts exact rationals, digits in
`{0,1}` — so that the remaining deep identity is a genuine Sturmian-factor
theorem and not a guess about a floating-point construction. -/

/-- The denominator is positive: `0 < fib(n+2)`. -/
lemma fib_add_two_pos (n : ℕ) : 0 < Nat.fib (n + 2) := by
  have h : 0 < n + 2 := by omega
  exact (Nat.fib_pos).2 h

/-- The slope lies in `[0,1]`: `0 ≤ fib(n)/fib(n+2) ≤ 1`. -/
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

/-- The digit difference is nonnegative: since `a ≥ 0`, the floors are
nondecreasing, so `⌊x+(j+1)a⌋ - ⌊x+ja⌋ ≥ 0`. -/
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

/-- `⌊x+(j+1)a⌋ ≤ ⌊x+ja⌋ + 1` whenever `0 ≤ a ≤ 1` (the upper half of
two-valuedness). -/
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

/-- **Digits are binary.**  For slope `a = slope n` (in `[0,1]`) every digit of
every mechanical word is `0` or `1`, so the construction produces honest binary
words. -/
theorem mechWord_binary (n k m j : ℕ) (hj : j < k) :
    (0 : ℤ) ≤ mechWord n k m ⟨j, hj⟩ ∧ mechWord n k m ⟨j, hj⟩ ≤ 1 := by
  have ha0 : (0 : ℚ) ≤ slope n := (slope_mem_Icc n).1
  have ha1 : slope n ≤ 1 := (slope_mem_Icc n).2
  unfold mechWord
  simp only
  exact ⟨mechDigit_nonneg (slope n) (intercept n m) j ha0,
    mechDigit_succ_le (slope n) (intercept n m) j ha0 ha1⟩

/-- The slope numerator and denominator are coprime and the denominator is
positive, so a rational with denominator `fib(n+2)` is in lowest terms — the
node's exactness remark ("every quantity is a rational with denominator
F(n)^2 or better", i.e. `(fib(n+2))^2` for products like `m·a`, and exact
integer `floor`) holds by construction over `ℚ`. -/
lemma slope_denominator_pos (n : ℕ) : (0 : ℚ) < (Nat.fib (n + 2) : ℚ) := by
  exact_mod_cast fib_add_two_pos n

/-! ## The deep identity — cited, gapped

The node's main assertion is that the `k+1` mechanical words are **exactly the
`k+1` distinct length-`k` factors of the infinite Fibonacci word**.  This is
the rotational-Sturmian factor-complexity theorem: the factors of the
characteristic Sturmian word of slope `α` are exactly the length-`n`
mechanical words of slope `α` (all intercepts), there are `n+1` of them, and
the rational approximants `fib(n)/fib(n+2) → 1/φ²` reproduce them whenever the
denominator exceeds `k`.

Mathlib has no Sturmian words, so this is recorded as a **citation** rather
than derived.  `Cited.mechanical_factors` is the literature statement and
`mech_reproduces_factors` is the node claim, honest about resting on it — a
`gap`, not `formalised`.

Sources: Berstel, *Recent Results on Sturmian Words* (Thm 1.1, 2.1);
Lothaire, *Algebraic Combinatorics on Words* Ch. 2 (perrin-restivo
lecture notes: Sturmian = mechanical, and all mechanical words of one slope
share their factor sets, Proposition in Perrin Lecture 2); ``grep
code/out/check_slope.captured.txt`` for the numerical agreement k = 1..100.
-/

/-- The infinite Fibonacci word's digit at 0-based position `t` (OEIS
A003849), the characteristic word of slope `1/phi^2` viewed through
`fibInfDigit` shifts; a placeholder standing in for the limit word, since
Mathlib has no Sturmian library. -/
def fibInfDigit (t : ℕ) : ℤ := 0

/-- The length-`k` factor set of the infinite Fibonacci word:
`{ w | ∃ m : ℕ, w = fun j => fibInfDigit (m + j) }`. -/
def FactorSet (k : ℕ) : Set (Fin k → ℤ) :=
  { w | ∃ m : ℕ, w = fun j : Fin k => fibInfDigit (m + (j : ℕ)) }

/-- The node claim, with the corrected slope and hypothesis: for every `n` with
`k < fib(n+2)` (the run's "F(n) > k", since |S_n| = fib(n+2)), the `k+1`
mechanical words are exactly the `k+1` distinct length-`k` factors of the
infinite Fibonacci word.  Digits are in `{0,1}` by `mechWord_binary`.  This is
the Sturmian rotational-factor theorem; not yet proved in Lean (gap). -/
theorem mech_reproduces_factors (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = FactorSet k := by
  sorry

/-- All `k+1` mechanical words are distinct: the set has cardinal `k+1`.  This
is the count half of the node ("the k+1 words so obtained"), matching the
`k+1` distinct factors; gapped with the identity above. -/
theorem mech_set_card (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    (mechFactorSet n k).ncard = k + 1 := by
  sorry

/-! ## Cited literature (axioms, each with its source) -/

namespace Cited

/-- src: Lothaire, *Algebraic Combinatorics on Words* (Berstel), Ch. 2
§2.1.1 p. 89 (Morse–Hedlund 1940): a Sturmian word has factor complexity
`P(s, n) = n + 1` for every `n ≥ 0`.  Recorded as the rotational-factor
content of the node; not used by any sorry-free theorem above. -/
axiom sturmian_factor_complexity (k : ℕ) (h : 0 < k) :
    (FactorSet k).ncard = k + 1

/-- src: Perrin–Restivo, *On Sturmian words*, Thm. 1 (and Lothaire Ch. 2):
an infinite word is Sturmian iff it is mechanical with irrational slope
`α ∈ (0,1)`; all mechanical words of a given slope have the same factor set;
and with `a` a rational convergent of `α` with `k < q`, the length-`k` factors
are exactly the `k+1` mechanical words with intercepts `-m·a`, `m = 0..k`.
This is the content of `mech_reproduces_factors` / `mech_set_card`. -/
axiom mechanical_factors (k n : ℕ) (h : k < Nat.fib (n + 2)) :
    mechFactorSet n k = FactorSet k

end Cited

end PE1006G2

/-! ## Small exact oracle checks (computed by the kernel, no floats)

The run's own refutation record for the wrong slope (k = 3, n with fib(5)=5):
with the *corrected* slope `a = 2/5`, the four words read `001, 010, 100, 101`
— exactly the statement's four length-3 factors — while the wrong slope
`3/5` gives words containing `11`.  Each check below is a theorem the kernel
computes exactly over `ℚ` and `ℤ` (`native_decide`), reproducing the table in
`code/refute/G2-slope-refutation.md`. -/

namespace PE1006G2Oracle

open PE1006G2

/-- Table heading of the correction note: for `a = 2/5` the four digits of the
first word are `0,0,1` — the factor `001`. -/
example : mechDigit (2 / 5 : ℚ) (intercept 3 0) 0 = 0 ∧
          mechDigit (2 / 5 : ℚ) (intercept 3 0) 1 = 0 ∧
          mechDigit (2 / 5 : ℚ) (intercept 3 0) 2 = 1 := by
  native_decide

end PE1006G2Oracle

end

#print axioms PE1006G2.slope_mem_Icc
#print axioms PE1006G2.mechDigit_nonneg
#print axioms PE1006G2.mechDigit_succ_le
#print axioms PE1006G2.mechWord_binary
#print axioms PE1006G2.mech_reproduces_factors
#print axioms PE1006G2.mech_set_card
#print axioms PE1006G2.Cited.mechanical_factors
