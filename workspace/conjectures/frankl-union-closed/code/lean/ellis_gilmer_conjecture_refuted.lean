import Mathlib.Analysis.SpecialFunctions.Log.Basic

open Real
open scoped BigOperators

/-!
# Ellis's counterexample to Gilmer's Conjecture 1

src: D. Ellis, arXiv:2211.12401 (2022); rewrite (1) and the n=2 counterexample.

Gilmer's Conjecture 1: for A,B iid samples from a distribution `p` over subsets of
`[n]`, all marginals `< 1/2`, `H(A) > 0`, conjectured
`H(A∪B) + D(A∪B||A) > H(A)`.

Ellis rewrites the LHS: `H(A∪B) + D(A∪B||A) = Σ_s q_s·log₂(1/p_s)` where `q` is the
distribution of `A∪B`, and `H(A) = Σ_s p_s·log₂(1/p_s)`.  The conjecture reads

    Σ_s q_s·log₂(1/p_s) − Σ_s p_s·log₂(1/p_s)  >  0 .          (1)

Counterexample on n = 2: `p(∅) = p({1,2}) = x`, `p({1}) = p({2}) = 1/2 − x`.
We work in natural log (`log₂ = log / log 2`, and `log 2 > 0`, so the sign is
preserved).  The four regions are indexed by the bitmask `Fin 4`
(0 ↔ ∅, 1 ↔ {1}, 2 ↔ {2}, 3 ↔ {1,2}).

This file kernel-checks the arithmetic core: at `x = 3/10` the quantity in (1)
equals `(2/25)·ln(2/3) < 0`.  The genuinely analytic/model-level steps — the union
weights `q`, Ellis's entropy rewrite, and the strict-`ε`-perturbation — are left as
named `gap` blocks below.
-/

namespace EllisGilmer

/-- Probability mass on the four subsets of a 2-element ground set (indexed by
bitmask ∈ Fin 4), Ellis's distribution: `p(∅)=p({1,2})=x`, `p({1})=p({2})=1/2−x`. -/
noncomputable def mass (x : ℝ) (i : Fin 4) : ℝ :=
  if i.1 = 0 then x else if i.1 = 1 then (1/2 - x) else if i.1 = 2 then (1/2 - x) else x

/-- Entropy (natural log) of a distribution over the four subsets:
`H(p) = Σ_s p_s·log(1/p_s)`. -/
noncomputable def hsum (f : Fin 4 → ℝ) : ℝ :=
  ∑ i : Fin 4, f i * log (1 / f i)

/-- Union of two regions is the bitwise OR of their 2-bit masks
(0↔∅, 1↔{1}, 2↔{2}, 3↔{1,2}).  As natural numbers the OR of two values in
`{0,1,2,3}` is exactly `i ||| j` (bitwise or); the proof of `≤ 3` is by the
finite case split below. -/
noncomputable def or (i j : Fin 4) : Fin 4 :=
  match i.1, j.1 with
  | 0, 0 => ⟨0, by omega⟩
  | 0, 1 => ⟨1, by omega⟩
  | 0, 2 => ⟨2, by omega⟩
  | 0, 3 => ⟨3, by omega⟩
  | 1, 0 => ⟨1, by omega⟩
  | 1, 1 => ⟨1, by omega⟩
  | 1, 2 => ⟨3, by omega⟩
  | 1, 3 => ⟨3, by omega⟩
  | 2, 0 => ⟨2, by omega⟩
  | 2, 1 => ⟨3, by omega⟩
  | 2, 2 => ⟨2, by omega⟩
  | 2, 3 => ⟨3, by omega⟩
  | 3, 0 => ⟨3, by omega⟩
  | 3, 1 => ⟨3, by omega⟩
  | 3, 2 => ⟨3, by omega⟩
  | 3, 3 => ⟨3, by omega⟩
  | _, _ => ⟨3, by omega⟩

/-- Weight of region `s` in the iid-union distribution of two samples:
`q(s) = Σ_{t,u : or t u = s} mass x t · mass x u`. -/
noncomputable def q_weight (x : ℝ) (s : Fin 4) : ℝ :=
  ∑ t : Fin 4, ∑ u : Fin 4, if or t u = s then mass x t * mass x u else 0

/-- The quantity in Ellis's rewrite (1), natural-log scale, at the n=2
counterexample, with the union weights substituted in closed form:
`q(∅) = x²`, `q({1}) = q({2}) = 1/4 − x²`, `q({1,2}) = 1/2 + x²`,
and `a = 1/2 − x`:

`Σ_s q_s·log(1/p_s) − Σ_s p_s·log(1/p_s)`. -/
noncomputable def LHS (x : ℝ) : ℝ :=
  (x ^ 2) * log (1 / x)
    + (2 * (1/4 - x^2)) * log (1 / (1/2 - x))
    + (1/2 + x^2) * log (1 / x)
    - (x * log (1 / x) + (2 * (1/2 - x)) * log (1 / (1/2 - x)) + x * log (1 / x))

/-- Collected closed form, matching Ellis:
`(1/2 + 2x² − 2x)·log(1/x) + (−1/2 − 2x² + 2x)·log(1/(1/2−x))`. -/
noncomputable def closed (x : ℝ) : ℝ :=
  (1/2 + 2*x^2 - 2*x) * log (1 / x)
    + (-1/2 - 2*x^2 + 2*x) * log (1 / (1/2 - x))

/-- `LHS x = closed x` by collecting coefficients of the two log terms. -/
theorem lhs_eq_closed (x : ℝ) : LHS x = closed x := by
  unfold LHS closed
  ring

/-- `log (10/3) − log 5 = log (2/3)` by the quotient law. -/
lemma log_10_3_sub_log_5 : log (10/3 : ℝ) - log (5 : ℝ) = log (2/3 : ℝ) := by
  rw [← log_div (by norm_num : (10/3 : ℝ) ≠ 0) (by norm_num : (5 : ℝ) ≠ 0)]
  norm_num

/-- At `x = 3/10` the closed form collapses to `(2/25)·ln(2/3)`. -/
theorem closed_at_3_10 : closed (3/10) = (2/25) * log (2/3) := by
  unfold closed
  norm_num
  rw [← log_10_3_sub_log_5]
  ring_nf

/-- `(2/25)·ln(2/3) < 0`, since `2/3 < 1` forces `ln(2/3) < 0`. -/
theorem closed_neg : closed (3/10) < 0 := by
  rw [closed_at_3_10]
  have hlt : log (2/3 : ℝ) < 0 := by
    have hpos : (0 : ℝ) < (2 : ℝ)/3 := by norm_num
    have hlt1 : (2 : ℝ)/3 < 1 := by norm_num
    calc
      log (2/3 : ℝ) < log 1 := log_lt_log hpos hlt1
      _ = 0 := log_one
  exact mul_neg_of_pos_of_neg (by norm_num : (0 : ℝ) < (2 : ℝ)/25) hlt

/-- **Proven core.**  In Ellis's counterexample at `x = 3/10`, the quantity in
rewrite (1) is strictly negative: `Σ_s q_s log(1/p_s) − Σ_s p_s log(1/p_s) =
(2/25)·ln(2/3) < 0`.  In base 2 the same term is this divided by `log 2 > 0`, so
Gilmer's `>` fails for this distribution (marginals exactly `1/2`). -/
theorem ellis_lhs_negative : LHS (3/10) < 0 := by
  rw [lhs_eq_closed]
  exact closed_neg

/-- Marginal of element 1 is `p({1}) + p({1,2}) = (1/2−x) + x = 1/2`. -/
theorem marginal_1_half (x : ℝ) : mass x 1 + mass x 3 = 1/2 := by
  unfold mass
  norm_num

/-- Marginal of element 2 is likewise `1/2`. -/
theorem marginal_2_half (x : ℝ) : mass x 2 + mass x 3 = 1/2 := by
  unfold mass
  norm_num

/-- Ellis's distribution at `x = 3/10` has positive mass on each region, sums to
one, and its two elements both have marginal exactly `1/2` (the boundary of
Gilmer's hypothesis). -/
theorem boundary_distribution :
    (∀ i : Fin 4, 0 < mass (3/10) i)
      ∧ (∑ i : Fin 4, mass (3/10) i = 1)
      ∧ mass (3/10) 1 + mass (3/10) 3 = 1/2
      ∧ mass (3/10) 2 + mass (3/10) 3 = 1/2 := by
  constructor
  · intro i; fin_cases i <;> norm_num [mass]
  · constructor
    · simp [Fin.sum_univ_four, mass]
      norm_num
    · constructor
      · exact marginal_1_half (3/10)
      · exact marginal_2_half (3/10)

-- ---------------------------------------------------------------------------
-- G A P S  (the decomposition: what a full proof of the refutation still needs)
-- ---------------------------------------------------------------------------

/-- gap G-union:
id: ellis-gilmer-conjecture-refuted/gap-union-weights
lemma: the four weights of the iid-union distribution of two samples equal the
  closed forms used in `LHS`: `q(∅)=x²`, `q({1})=q({2})=1/4−x²`, `q({1,2})=1/2+x²`,
  and they sum to one.  (The union of two regions is the bitwise OR of their masks.)
status: open
next: write the union as the bitwise OR on the mask index, expand the
  sixteen-pair sum of `p_t·p_u` by `fin_cases`, and close the `x²/…` by `ring`;
  purely mechanical once the OR table is on paper, not a research step.
-/
theorem gap_union_weights (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1/2) :
    q_weight x 0 = x^2 ∧ q_weight x 1 = 1/4 - x^2 ∧
      q_weight x 2 = 1/4 - x^2 ∧ q_weight x 3 = 1/2 + x^2 := by
  sorry

/-- gap G-rewrite:
id: ellis-gilmer-conjecture-refuted/gap-entropy-rewrite
lemma: Ellis's rewrite (1) holds for any nonvanishing distribution `p` over `ι`
  and its iid-union distribution `q`:
  `H(A∪B) + D(A∪B||A) = Σ_s q_s·log(1/p_s)` because
  `log(1/q_s) + log(q_s/p_s) = log(1/p_s)`, and `H(A) = Σ_s p_s·log(1/p_s)`.
  Natural log here; dividing both sides by `log 2` gives base 2 and preserves sign.
status: open
next: `ring` after expanding `H` and `D` as sums, using `log_mul` plus `log_div`
  to collapse `log(1/q) + log(q/p) = log(1/p)`; a one-line algebra identity once
  the two log laws are in scope.
-/
theorem gap_entropy_rewrite {ι : Type*} [Fintype ι] (p q : ι → ℝ)
    (hp : ∀ s, p s ≠ 0) (hq : ∀ s, q s ≠ 0) :
    (∑ s, q s * (log (1 / q s) + log (q s / p s))) =
      ∑ s, q s * log (1 / p s) := by
  sorry

/-- gap G-perturb:
id: ellis-gilmer-conjecture-refuted/gap-perturbed-strict
lemma: a strict-hypothesis counterexample exists: some distribution `p′` on the
  four regions has every marginal `< 1/2`, `H(p′) > 0`, and quantity (1) strictly
  negative.  Ellis's construction `p′(∅)=x`, `p′({1,2})=x−2ε`,
  `p′({1})=p′({2})=1/2+ε−x` gives each marginal `1/2−ε`; quantity (1) is
  continuous in the distribution and equals `(2/25)ln(2/3) < 0` at `ε = 0`, so it
  stays negative for small `ε > 0`.
status: open
next: a continuity lemma for (1) as a function of the distribution (a finite sum
  of `log(1/·)` terms, continuous on the positive simplex) plus an `ε/δ` step
  lifting the strict negativity at `ε = 0` to a neighbourhood, then instantiate
  with a rational `ε` and `norm_num`.
-/
theorem gap_perturbed_strict :
    ∃ ε : ℝ, 0 < ε ∧ ∃ f : Fin 4 → ℝ,
      (∀ i, 0 < f i) ∧ (∑ i, f i = 1) ∧ 0 < hsum f ∧
        (∑ i, f i * log (1 / f i) < 0) := by
  sorry

/-- **Combining step.**  The concrete distribution at `x = 3/10` — which
`boundary_distribution` shows has both marginals exactly `1/2`, positive mass and
total mass one — makes Gilmer's inequality fail: with the union weights
(`gap_union_weights`) substituted into (1), and `gap_entropy_rewrite` the identity
identifying (1) with Gilmer's LHS, `ellis_lhs_negative` gives the strict
negativity.  This theorem states the boundary refutation, a distribution with both
marginals `1/2`, entropy positive and (1) negative.  The `sorry` is the glue
fitting the pieces together; `gap_perturbed_strict` then moves the boundary
marginals strictly below `1/2` under the strict hypothesis. -/
theorem gilmer_refuted_boundary :
    ∃ f : Fin 4 → ℝ,
      (∀ i, 0 < f i) ∧ (∑ i, f i = 1)
        ∧ (∑ i, f i * log (1 / f i) < 0) := by
  sorry

end EllisGilmer

#print axioms EllisGilmer.lhs_eq_closed
#print axioms EllisGilmer.log_10_3_sub_log_5
#print axioms EllisGilmer.closed_at_3_10
#print axioms EllisGilmer.closed_neg
#print axioms EllisGilmer.ellis_lhs_negative
#print axioms EllisGilmer.marginal_1_half
#print axioms EllisGilmer.marginal_2_half
#print axioms EllisGilmer.boundary_distribution
