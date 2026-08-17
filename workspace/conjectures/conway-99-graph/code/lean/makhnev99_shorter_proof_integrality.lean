import Mathlib.Combinatorics.SimpleGraph.StronglyRegular
import Mathlib.Combinatorics.SimpleGraph.Clique

/-!
# Makhnev 1988 Thm 2, 99 case — shorter proof via multiplicity integrality

Source: A. A. Makhnev, "On strongly regular graphs with λ = 1" (О сильно
регулярных графах с λ = 1), Mat. Zametki 44(5) 667–672 (1988); English
translation Math. Notes 44 847–850, DOI 10.1007/BF01158426.  Primary Russian
full text: research/sources/makhnev-1988-lambda1-russian-fulltext.full.md
(open on mathnet.ru, paperid=4220).

Claim node: `makhnev99-shorter-proof-integrality`.

The informal statement, restated here *exactly* so that every hypothesis is
carried by a binder:

> Under Makhnev 1988 Thm 2's condition (∗) [n₃ = 0] at (99,14,1,2), the
> argument forces, from the closure of a triangle and its 60 exterior points,
> a subobject Λ₀ = srg(33,12,1,6): the closure has 39 points (= 3·14−3), its 36
> non-A points lie in 12 inner triangles, the 60 outside points give 20 outer
> triangles, and the 1 + 12 + 20 = 33 triangle-vertices partition all
> 3 + 36 + 60 = 99 points.  srg(33,12,1,6) is INFEASIBLE by
> eigenvalue-multiplicity integrality: the g numerator 2k+(v−1)(λ−μ) = −136 is
> not divisible by √δ = 7.  Makhnev rejects Λ₀ via Thm 1 (μ = 6 > 3 and not
> (27,10,1,5)); this run rejects it directly by multiplicity integrality, a
> shorter self-contained proof of the 99 case of Thm 2's n₃ = 0 branch.  This
> asserts nothing about whether srg(99,14,1,2) exists.

What is kernel-checked here and what is not:

 1. **The arithmetic kernel — FULLY PROVED, no axioms.** For the parameter
    triple (33,12,1,6): δ = (λ−μ)² + 4(k−μ) = (1−6)² + 4(12−6) = 49 = 7², the
    multiplicity numerator 2k + (v−1)(λ−μ) = 24 + 32·(−5) = −136, and 7 does
    not divide −136 (equivalently not 136).  These divisibility facts are the
    kernel of the run's `check_srg33_12_1_6.py` verdict
    (`code/out/check_srg33_12_1_6.captured.txt`).

 2. **The spectral-multiplicity integrality step — CITED, not proved here.**
    That an existing SRG with parameters (33,12,1,6) forces `7` to divide the
    numerator 2k + (v−1)(λ−μ) is a theorem of the Bose–Mesner algebra
    (eigenvalue multiplicities are integers, and √δ = 7 is the smaller-root
    denominator).  This run does not formalise the spectral theory of SRGs; it
    carries that step as a `Cited` axiom.  Consequently every theorem using it
    is `conditional`, never `formalised`.

 3. **The forced-subobject chain (Lemmas 6–9) and Thm 1 — CITED.** The claim
    that a putative srg(99,14,1,2) satisfying (∗) forces Λ₀ = srg(33,12,1,6)
    is the sourced geometric content of Makhnev's Lemmas 6–9, reproduced
    arithmetically in `check_makhnev_n3_counts.captured.txt` but not
    re-proved here.  Rejecting Λ₀ by Thm 1 is an alternative route; this file
    carries the shorter direct rejection by integrality.

  A claim resting on any `Cited.*` axiom is `conditional`: the kernel checked
  the implication and checked nothing about the axiom.  `formalised` is used
  only for the arithmetic kernel, which the kernel checked outright.
-/

open scoped BigOperators

namespace Makhnev99

/-- Number of edges between two (ordered) vertex subsets. -/
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

namespace Cited

/-- src: standard spectral theory of strongly regular graphs (Bose–Mesner
algebra / eigenvalue multiplicities of an SRG are integers; discriminant
δ = (λ−μ)² + 4(k−μ) a perfect square).  Concretely for the parameter set
(33,12,1,6), whose discriminant is δ = 49 = 7², the smaller eigenvalue
multiplicity is `g = 1/2 [(v−1) − (2k + (v−1)(λ−μ))/√δ]`, an integer, forcing
`7 ∣ (2k + (v−1)(λ−μ))`. -/
axiom srg_multiplicity_integrality {V : Type} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (h : G.IsSRGWith 33 12 1 6) :
  (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6))

/-- src: Makhnev 1988, Mat. Zametki 44(5), Lemmas 6–9 — a putative
srg(99,14,1,2) satisfying (∗) (n₃ = 0) forces, from the closure Γ(A) of a
triangle (|Γ(A)| = 39 = 3·14 − 3; the 36 non-A points in 12 inner triangles;
the 60 exterior points in 20 outer triangles; the 1 + 12 + 20 = 33
triangle-vertices partitioning the 3 + 36 + 60 = 99 points), a subobject
Λ₀ = srg(33,12,1,6).  The count arithmetic (39 / 12 / 60 / 20 / 33 / 99) is
verified in exact integer arithmetic in
`code/out/check_makhnev_n3_counts.captured.txt`; the existence of the subobject
is taken from the source. -/
axiom makhnev_lemmas_6_9 {V : Type} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (hG : G.IsSRGWith 99 14 1 2) (hstar : CondStar G) :
  ∃ (W : Type) (_ : Fintype W) (Λ : SimpleGraph W) (_ : DecidableRel Λ.Adj),
    Λ.IsSRGWith 33 12 1 6

end Cited

/-! ## 1. The arithmetic kernel (fully proved, formalised) -/

/-- The discriminant `δ = (λ−μ)² + 4(k−μ)` of srg(33,12,1,6) equals `49 = 7²`. -/
lemma discriminant_sq :
    ((1 : ℤ) - 6)^2 + 4 * ((12 : ℤ) - 6) = (7 : ℤ)^2 := by
  norm_num

/-- The multiplicity numerator `2k + (v−1)(λ−μ)` of srg(33,12,1,6) equals `-136`. -/
lemma mult_num :
    (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) = -136 := by
  norm_num

/-- `7` does not divide `136`. -/
lemma not_seven_dvd_136 : ¬ (7 : ℤ) ∣ (136 : ℤ) := by
  rintro ⟨c, hc⟩
  omega

/-- `7` does not divide `-136`. -/
lemma not_seven_dvd_neg_136 : ¬ (7 : ℤ) ∣ (-136 : ℤ) := by
  rintro ⟨c, hc⟩
  omega

/-- `7` does not divide the multiplicity numerator of srg(33,12,1,6). -/
lemma not_seven_dvd_mult_num :
    ¬ (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) := by
  rw [mult_num]
  exact not_seven_dvd_neg_136

/-! ## 2. srg(33,12,1,6) is parameter-infeasible by multiplicity integrality

`conditional`: rests on `Cited.srg_multiplicity_integrality`. -/

/-- No strongly regular graph with parameters `(33,12,1,6)` exists: by the
(eigenvalue-)multiplicity integrality of an SRG the numerator
`2k + (v−1)(λ−μ) = −136` must be divisible by `√δ = 7`, which it is not. -/
theorem srg33_12_1_6_infeasible_by_integrality :
    ¬ ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V) (_ : DecidableRel G.Adj),
        G.IsSRGWith 33 12 1 6 := by
  rintro ⟨V, _iv, G, _da, hG⟩
  have hdiv := Cited.srg_multiplicity_integrality (V := V) (G := G) hG
  rw [mult_num] at hdiv
  exact not_seven_dvd_neg_136 hdiv

/-! ## 3. The (99,14,1,2) case of Thm 2's n₃ = 0 branch

`conditional`: rests on `Cited.srg_multiplicity_integrality` AND
`Cited.makhnev_lemmas_6_9`.  A putative srg(99,14,1,2) satisfying (∗) forces a
subobject Λ₀ = srg(33,12,1,6) (Lemmas 6–9); by the theorem above Λ₀ cannot
exist.  This is the shorter, self-contained rejection of the n₃ = 0 branch: it
needs no appeal to Thm 1.  It asserts nothing about whether srg(99,14,1,2)
exists (only that no such graph satisfies the additional hypothesis (∗)). -/

/-- No srg(99,14,1,2) satisfies Makhnev's condition (∗) [n₃ = 0] — the 99 case
of Thm 2's n₃ = 0 branch, proved here by the direct integrality rejection of
the forced subobject srg(33,12,1,6) rather than by Thm 1. -/
theorem no_srg_99_14_1_2_condstar :
    ¬ ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V) (_ : DecidableRel G.Adj),
        G.IsSRGWith 99 14 1 2 ∧ CondStar G := by
  rintro ⟨V, _iv, G, _da, hG, hstar⟩
  rcases Cited.makhnev_lemmas_6_9 (V := V) (G := G) hG hstar with ⟨W, _iw, Λ, _dl, hΛ⟩
  exact srg33_12_1_6_infeasible_by_integrality ⟨W, _iw, Λ, _dl, hΛ⟩
/-! ## 4. The arithmetic kernel, standalone, formalised -/

/-- The pure-integer claim that underlies the whole node, stated without any
SRG/spectral content: `7` does not divide `2k + (v−1)(λ−μ)` for
`(v,k,λ,μ) = (33,12,1,6)` because that number is `-136`.  This is the
kernel-checked arithmetic behind the infeasibility. -/
theorem not_seven_dvd_33_12_1_6_numerator :
    ¬ (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) := by
  exact not_seven_dvd_mult_num

#check Makhnev99.discriminant_sq
#check Makhnev99.mult_num
#check Makhnev99.not_seven_dvd_mult_num
#check Makhnev99.not_seven_dvd_33_12_1_6_numerator
#check Makhnev99.srg33_12_1_6_infeasible_by_integrality
#check Makhnev99.no_srg_99_14_1_2_condstar

-- The arithmetic kernel: formalised (no axioms).
#print axioms Makhnev99.not_seven_dvd_33_12_1_6_numerator

-- The infeasibility: rests on the Cited spectral axiom -> conditional.
#print axioms Makhnev99.srg33_12_1_6_infeasible_by_integrality

-- The Thm 2 99-case: rests on both Cited axioms -> conditional.
#print axioms Makhnev99.no_srg_99_14_1_2_condstar

end Makhnev99
