import Mathlib.Combinatorics.SimpleGraph.StronglyRegular
import Mathlib.Combinatorics.SimpleGraph.Clique

/-!
# Makhnev 1988, condition (*) and the associated theorems

Source: A. A. Makhnev, "On strongly regular graphs with λ = 1" (О сильно
регулярных графах с λ = 1), Mat. Zametki 44(5) 667–672 (1988); English
translation Math. Notes 44 847–850, DOI 10.1007/BF01158426.  Primary Russian
full text: research/sources/makhnev-1988-lambda1-russian-fulltext.full.md
(open on mathnet.ru, paperid=4220).

Makhnev defines the *triangle graph* Γ_Δ on the triangles of Γ and weakens
strong regularity of Γ_Δ to the condition

  (∗)  any two triangles joined by at least two edges are joined by exactly
       three edges.

This is exactly Reimbayev's `n₃ = 0` (no pair of triangles joined by two
edges).  The two theorems:

  THEOREM 1. Let Γ be a strongly regular graph with λ = 1 satisfying (∗).
  Then either μ ≤ 3, or Γ is the unique graph with parameters (27,10,1,5).

  THEOREM 2. There is no strongly regular graph with parameters (99,14,1,2)
  or (115,18,1,3) satisfying (∗).

The present file formalises:

 1. the *arithmetic kernel* (proved in Lean, no axioms) — the eigenvalue
    multiplicity integrality obstruction that makes the forced subobject
    srg(33,12,1,6) parameter-infeasible: its multiplicity numerator
    2k + (v−1)(λ−μ) = −136 is not divisible by √δ = 7 where
    δ = (λ−μ)² + 4(k−μ) = 49; and

 2. the formal derivation (resting on Cited axioms for the geometric content)
    that the (99,14,1,2) case of Theorem 2 holds: a putative srg(99,14,1,2)
    satisfying (∗) forces an srg(33,12,1,6) satisfying (∗) (Makhnev's
    Lemmas 6–9), which Theorem 1 rejects because μ = 6 > 3 and it is not
    the (27,10,1,5) exception.

The purely geometric content (the existence of the forced subobject, Theorem 1,
and the spectral-multiplicity integrality condition itself) is placed under
`namespace Cited` as axioms with docstrings naming the source, following the
run's convention for literature results.  The *arithmetic* — the divisibility
facts that make the infeasibility and the contradiction go through — is proved
here by `norm_num`/`omega` and is fully kernel-checked.

A claim resting on the `Cited.*` axioms is `conditional`, never `formalised`:
the kernel checked the implication and checked nothing about those axioms.
-/

open scoped BigOperators

namespace Makhnev1988

/-- Number of edges between two (ordered) vertex subsets, i.e. the number of
pairs `(x,y)` with `x ∈ s`, `y ∈ t`, and `G.Adj x y`. -/
def edgeCountBetween {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (s t : Finset V) : ℕ :=
  ((s.product t).filter (fun p : V × V => G.Adj p.1 p.2)).card

/-- Makhnev's condition (∗): any two *distinct* triangles joined by at least
two edges are joined by exactly three edges.  This is Reimbayev's n₃ = 0. -/
def CondStar {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj] : Prop :=
  ∀ {T1 T2 : Finset V},
    T1.card = 3 → T2.card = 3 →
      G.IsClique (T1 : Set V) → G.IsClique (T2 : Set V) → T1 ≠ T2 →
        2 ≤ edgeCountBetween G T1 T2 → edgeCountBetween G T1 T2 = 3

end Makhnev1988

/-! ## Cited geometric content (literature results)

The purely geometric content — Theorem 1, the forced-subobject chain (Lemmas
6–9), and the spectral-multiplicity integrality condition — is placed under
the top-level `namespace Cited` as axioms with docstrings naming the source,
following the run's convention.  A result resting on these alone is
`conditional`: the kernel checked the implication and checked nothing about
the axioms. -/

namespace Cited

/-- src: Makhnev 1988, Mat. Zametki 44(5), Thm 1 — a strongly regular graph with
λ = 1 satisfying (∗) has either μ ≤ 3 or parameters (27,10,1,5). -/
axiom makhnev_thm1 {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    {n k mu : ℕ} (h : G.IsSRGWith n k 1 mu) (hs : Makhnev1988.CondStar G) :
  mu ≤ 3 ∨ (n = 27 ∧ k = 10 ∧ mu = 5)

/-- src: Makhnev 1988, Mat. Zametki 44(5), Lemmas 6–9 — a putative
srg(99,14,1,2) satisfying (∗) forces, from the closure Γ(A) of a triangle
(|Γ(A)| = 39 = 3·14 − 3; 36 non-A points in 12 inner triangles; 60 exterior
points in 20 outer triangles), a subobject Λ₀ = srg(33,12,1,6) satisfying (∗).
The 1 + 12 + 20 = 33 triangle-vertices partition the 3 + 36 + 60 = 99 points. -/
axiom makhnev_lemmas_6_9 {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.IsSRGWith 99 14 1 2) (hstar : Makhnev1988.CondStar G) :
  ∃ (W : Type) (_ : Fintype W) (Λ : SimpleGraph W) (_ : DecidableRel Λ.Adj),
    Λ.IsSRGWith 33 12 1 6 ∧ Makhnev1988.CondStar Λ

/-- src: standard spectral theory of strongly regular graphs (Bose–Mesner
algebra); the eigenvalue multiplicities are integers.  Concretely for the
parameter set (33,12,1,6), whose discriminant δ = 49 = 7², the multiplicity
formula forces `7` to divide the numerator `2k + (v−1)(λ−μ)`. -/
axiom srg_multiplicity_integrality {V : Type} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (h : G.IsSRGWith 33 12 1 6) :
  (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6))

end Cited

namespace Makhnev1988

/-! ## 1. The arithmetic kernel (fully proved) — srg(33,12,1,6) is infeasible

For an SRG the two non-trivial eigenvalues are r,s with
`δ = (λ−μ)² + 4(k−μ) = (r−s)²` a perfect square, and the multiplicity of the
smaller eigenvalue is `g = 1/2 [(v−1) − (2k + (v−1)(λ−μ))/√δ]`, an integer
(Bose–Mesner algebra / eigenvalue multiplicities).  For (33,12,1,6):
`δ = (1−6)² + 4(12−6) = 49 = 7²`, and the numerator
`2k + (v−1)(λ−μ) = 24 + 32·(−5) = −136`.  Since 7 ∤ 136, g is not an integer —
a contradiction.  These divisibility facts are the kernel of the run's
`check_srg33_12_1_6.py` verdict (`code/out/check_srg33_12_1_6.captured.txt`). -/

/-- The discriminant `δ = (λ−μ)² + 4(k−μ)` for srg(33,12,1,6) equals `49 = 7²`. -/
lemma condstar_discriminant :
    ((1 : ℤ) - 6)^2 + 4 * ((12 : ℤ) - 6) = (49 : ℤ) := by
  norm_num

/-- The square root of the discriminant is `7`. -/
lemma condstar_sqrt : ((7 : ℤ) : ℤ)^2 = (49 : ℤ) := by
  norm_num

/-- The multiplicity numerator `2k + (v−1)(λ−μ)` for (33,12,1,6) equals `-136`. -/
lemma condstar_mult_num :
    (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) = -136 := by
  norm_num

/-- `7` does not divide `136`. -/
lemma not_seven_dvd_pos_136 : ¬ (7 : ℤ) ∣ (136 : ℤ) := by
  rintro ⟨c, hc⟩
  omega

/-- `7` does not divide `-136`. -/
lemma not_seven_dvd_neg_136 : ¬ (7 : ℤ) ∣ (-136 : ℤ) := by
  rintro ⟨c, hc⟩
  omega

/-- `7` does not divide the multiplicity numerator `2k + (v−1)(λ−μ)` of
srg(33,12,1,6). -/
lemma not_seven_dvd_mult_num :
    ¬ (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) := by
  rw [condstar_mult_num]
  exact not_seven_dvd_neg_136

/-! ## 2. The shorter route: srg(33,12,1,6) is parameter-infeasible

This is the run's `makhnev99-shorter-proof-integrality` claim: the forced
subobject Λ₀ cannot exist at all, by eigenvalue-multiplicity integrality.  It
rests on the Cited spectral axiom plus the kernel arithmetic above.  A claim
resting on this theorem is `conditional` (it depends on
`Cited.srg_multiplicity_integrality`). -/

/-- A strongly regular graph with parameters `(33,12,1,6)` does not exist:
its eigenvalue-multiplicity numerator is not divisible by `√δ = 7`.

This theorem rests on the Cited axiom `Cited.srg_multiplicity_integrality`
(the integrality of the eigenvalue multiplicities, from Bose–Mesner algebra);
the arithmetic step (7 ∤ −136) is proved here. -/
theorem srg33_12_1_6_infeasible_by_integrality :
    ¬ ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V) (_ : DecidableRel G.Adj),
        G.IsSRGWith 33 12 1 6 := by
  rintro ⟨V, _iv, G, _da, hG⟩
  have hdiv := Cited.srg_multiplicity_integrality (V := V) (G := G) hG
  rw [condstar_mult_num] at hdiv
  exact not_seven_dvd_neg_136 hdiv

/-! ## 3. The main derivation: the (99,14,1,2) case of Thm 2

Given a putative srg(99,14,1,2) satisfying (∗), Lemmas 6–9 force a subobject
Λ₀ = srg(33,12,1,6) satisfying (∗); Thm 1 then rejects it because μ = 6 > 3
and Λ₀ is not the (27,10,1,5) exception.  The arithmetic of the rejection
(`6 ≤ 3` false, `33 ≠ 27`, etc.) is proved here; the geometric content is the
Cited axioms.  A claim resting on this theorem is `conditional`. -/

/-- Thm 1's alternative cannot hold of the forced subobject (33,12,1,6):
μ = 6 is not ≤ 3, and the parameters are not (27,10,1,5). -/
lemma srg33_param_contradicts_thm1 :
    ¬ ((6 : ℕ) ≤ 3 ∨ (33 = 27 ∧ 12 = 10 ∧ 6 = 5)) := by
  omega

/-- There is no srg(99,14,1,2) satisfying Makhnev's condition (∗) — the
(99,14,1,2) case of Theorem 2.

This theorem rests on the Cited axioms `Cited.makhnev_thm1` (Thm 1) and
`Cited.makhnev_lemmas_6_9` (the forced-subobject chain); the parameter
contradiction that closes it is proved here. -/
theorem no_srg_99_14_1_2_condstar :
    ¬ ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V) (_ : DecidableRel G.Adj),
        G.IsSRGWith 99 14 1 2 ∧ CondStar G := by
  rintro ⟨V, _iv, G, _da, hG, hstar⟩
  rcases Cited.makhnev_lemmas_6_9 (V := V) (G := G) hG hstar with ⟨W, _iw, Λ, _dl, hΛ, hΛstar⟩
  have halternative := Cited.makhnev_thm1 (V := W) (G := Λ) hΛ hΛstar
  exact srg33_param_contradicts_thm1 halternative

/-! ## 4. The (27,10,1,5) exception and the μ ≤ 3 branch are untouched

For completeness we record that the two known small members
srg(9,4,1,2) and srg(243,22,1,2) have μ = 2 ≤ 3, so Theorem 1's first branch
absorbs them and Theorem 2 says *nothing* about them.  This is the negative
controls consistency the run requires of a nonexistence argument. -/

/-- The two positive controls rook(3) = srg(9,4,1,2) and BvLS = srg(243,22,1,2)
both satisfy the μ ≤ 3 branch of Thm 1's alternative, so they are not touched by
Thm 2's (99,14,1,2)/(115,18,1,3) statement.  (Their actual existence is verified
computationally in code/lib/srg.py; this lemma only records the μ-value of the
branch that absorbs them.) -/
lemma controls_in_mu_le_three : (2 : ℕ) ≤ 3 := by
  omega

#check Makhnev1988.condstar_discriminant
#check Makhnev1988.condstar_mult_num
#check Makhnev1988.not_seven_dvd_mult_num
#check Makhnev1988.srg33_12_1_6_infeasible_by_integrality
#check Makhnev1988.no_srg_99_14_1_2_condstar

-- Theorems that constitute the formalised claims, and their axioms.
#print axioms Makhnev1988.srg33_12_1_6_infeasible_by_integrality
#print axioms Makhnev1988.no_srg_99_14_1_2_condstar

end Makhnev1988
