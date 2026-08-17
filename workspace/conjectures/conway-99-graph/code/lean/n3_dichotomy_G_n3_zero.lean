import Mathlib.Combinatorics.SimpleGraph.StronglyRegular
import Mathlib.Combinatorics.SimpleGraph.Clique

/-!
# G-n3-zero — no srg(99,14,1,2) has n₃ = 0

Source: A. A. Makhnev, "On strongly regular graphs with λ = 1" (О сильно
регулярных графах с λ = 1), Mat. Zametki 44(5) 667–672 (1988); trans. Math.
Notes 44 847–850.  Primary Russian full text: research/sources/
makhnev-1988-lambda1-russian-fulltext.full.md (open on mathnet.ru,
paperid=4220).

Claim node: `n3-dichotomy/G-n3-zero` in research/backward/n3-dichotomy.md.

## The statement, restated exactly

> No srg(99,14,1,2) has `n3 = 0`, where `n3 = 0` is Makhnev's condition
> (∗): no pair of *disjoint* triangles is joined by exactly 2 edges.
> Under (∗), Makhnev's closure of a triangle forces a subobject
> Λ₀ = srg(33,12,1,6), which is parameter-infeasible.

Every hypothesis is carried by a binder:

 * `G` is an `srg(99,14,1,2)` — `G.IsSRGWith 99 14 1 2`.
 * `n3_zero G` — no pair of disjoint 3-cliques (triangles) has exactly two
   cross edges between them.  This is the honest reading of "n₃ = 0".  The
   earlier `CondStar` in makhnev99_shorter_proof_integrality.lean quantified
   over *all* distinct triangle pairs; two triangles sharing a vertex are
   joined by ≥ 4 cross edges, so that version was unsatisfiable (hence
   vacuously true) for any graph with intersecting triangles.  Here we
   restrict the quantification to `Disjoint T1 T2`, matching the node's
   wording and making the condition live.

## What is kernel-checked here and what is cited

1. **Arithmetic kernel (FORMALISED, no axioms).**  For srg(33,12,1,6),
   δ = (1−6)² + 4(12−6) = 49 = 7², the multiplicity numerator
   2k + (v−1)(λ−μ) = 24 + 32·(−5) = −136, and 7 ∤ 136 (hence 7 ∤ −136).
   So srg(33,12,1,6) has no integral eigenvalue multiplicity.

2. **Spectral-multiplicity integrality of an SRG (CITED).**  An existing
   SRG forces 7 to divide the numerator — a Bose–Mesner algebra theorem
   carried as `Cited.srg_multiplicity_integrality`.  Anything using it is
   `conditional`.

3. **The forced-subobject chain (Makhnev Lemmas 6–9, CITED).**  A putative
   srg(99,14,1,2) with n₃ = 0 forces Λ₀ = srg(33,12,1,6) from a triangle's
   closure (|Γ(A)| = 39; the 60 exterior points in 20 outer triangles; the
   1 + 12 + 20 = 33 triangle-vertices partition the 3 + 36 + 60 = 99 points).
   Carried as `Cited.makhnev_lemmas_6_9`; the count arithmetic is verified in
   code/out/check_makhnev_n3_counts.captured.txt.

The dichotomy theorem `no_srg_99_14_1_2_n3_zero` is therefore `conditional`
(it rests on the two Cited axioms), while the arithmetic kernel
`not_seven_dvd_33_12_1_6_numerator` is `formalised`.

Nothing here asserts whether srg(99,14,1,2) exists; it asserts only that no
such graph has n₃ = 0.
-/

open scoped BigOperators

namespace N3Dichotomy

/-- Number of cross edges between two (ordered) vertex subsets `s` and `t`,
counted over `s.product t`.  For *disjoint* `s,t`, each undirected cross edge
`{x,y}` with `x ∈ s`, `y ∈ t` lies in `s.product t` exactly once, so the
directed count equals the number of undirected cross edges.  Hence for
disjoint triangles "joined by exactly 2 edges" means
`edgeCountBetween G T1 T2 = 2`. -/
def edgeCountBetween {V : Type} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (s t : Finset V) : ℕ :=
  ((s.product t).filter (fun p : V × V => G.Adj p.1 p.2)).card

/-- The node's n₃ = 0 condition (Makhnev's (∗) restricted to where it bites):
no pair of *disjoint* triangles is joined by exactly 2 edges. -/
def n3_zero {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj] : Prop :=
  ∀ {T1 T2 : Finset V},
    T1.card = 3 → T2.card = 3 →
      G.IsClique (T1 : Set V) → G.IsClique (T2 : Set V) →
        Disjoint T1 T2 → edgeCountBetween G T1 T2 ≠ 2

namespace Cited

/-- src: standard spectral theory of strongly regular graphs (Bose–Mesner
algebra; eigenvalue multiplicities of an SRG are integers).  For the parameter
set (33,12,1,6), whose discriminant is δ = 49 = 7², the smaller eigenvalue
multiplicity `g = 1/2 [(v−1) − (2k + (v−1)(λ−μ))/√δ]` is an integer, forcing
`7 ∣ (2k + (v−1)(λ−μ))`. -/
axiom srg_multiplicity_integrality {V : Type} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (h : G.IsSRGWith 33 12 1 6) :
  (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6))

/-- src: Makhnev 1988, Mat. Zametki 44(5), Lemmas 6–9 — a putative
srg(99,14,1,2) satisfying (∗) (n₃ = 0) forces, from the closure Γ(A) of a
triangle (|Γ(A)| = 39 = 3·14 − 3; the 36 non-A points in 12 inner triangles;
the 60 exterior points in 20 outer triangles; the 1 + 12 + 20 = 33
triangle-vertices partitioning the 3 + 36 + 60 = 99 points), a subobject
Λ₀ = srg(33,12,1,6).  The count arithmetic is verified in exact integer
arithmetic in code/out/check_makhnev_n3_counts.captured.txt; the existence of
the subobject is taken from the source. -/
axiom makhnev_lemmas_6_9 {V : Type} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (hG : G.IsSRGWith 99 14 1 2) (hn3 : n3_zero G) :
  ∃ (W : Type) (_ : Fintype W) (Λ : SimpleGraph W) (_ : DecidableRel Λ.Adj),
    Λ.IsSRGWith 33 12 1 6

end Cited

/-! ## 1. The arithmetic kernel (formalisable, proved outright) -/

/-- The discriminant `δ = (λ−μ)² + 4(k−μ)` of srg(33,12,1,6) equals 49 = 7². -/
lemma discriminant_sq : ((1 : ℤ) - 6)^2 + 4 * ((12 : ℤ) - 6) = (7 : ℤ)^2 := by
  norm_num

/-- The multiplicity numerator `2k + (v−1)(λ−μ)` of srg(33,12,1,6) equals -136. -/
lemma mult_num : (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) = -136 := by
  norm_num

/-- `7` does not divide `136`. -/
lemma not_seven_dvd_136 : ¬ (7 : ℤ) ∣ (136 : ℤ) := by
  rintro ⟨c, hc⟩
  omega

/-- `7` does not divide `-136`. -/
lemma not_seven_dvd_neg_136 : ¬ (7 : ℤ) ∣ (-136 : ℤ) := by
  rintro ⟨c, hc⟩
  omega

/-- `7` does not divide the multiplicity numerator of srg(33,12,1,6), because
that numerator is `-136`. -/
lemma not_seven_dvd_mult_num :
    ¬ (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) := by
  rw [mult_num]
  exact not_seven_dvd_neg_136

/-! ## 2. srg(33,12,1,6) is parameter-infeasible (conditional) -/

/-- No strongly regular graph with parameters (33,12,1,6) exists: multiplicity
integrality forces `7 ∣ −136`, which is false.  `conditional`: rests on
`Cited.srg_multiplicity_integrality`. -/
theorem srg33_12_1_6_infeasible :
    ¬ ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V) (_ : DecidableRel G.Adj),
        G.IsSRGWith 33 12 1 6 := by
  rintro ⟨V, _iv, G, _da, hG⟩
  have hdiv := Cited.srg_multiplicity_integrality (V := V) (G := G) hG
  rw [mult_num] at hdiv
  exact not_seven_dvd_neg_136 hdiv

/-! ## 3. The G-n3-zero dichotomy theorem (conditional) -/

/-- No srg(99,14,1,2) has n₃ = 0 (Makhnev's (∗)): a putative such graph forces
a subobject Λ₀ = srg(33,12,1,6) (Makhnev Lemmas 6–9), which is
parameter-infeasible by multiplicity integrality.  This is the 99 case of
Makhnev Thm 2's n₃ = 0 branch, proved here by the direct integrality rejection
of the forced subobject.  It asserts nothing about whether srg(99,14,1,2)
exists — only that no such graph satisfies the extra hypothesis n₃ = 0.

`conditional`: rests on `Cited.makhnev_lemmas_6_9` and
`Cited.srg_multiplicity_integrality`. -/
theorem no_srg_99_14_1_2_n3_zero :
    ¬ ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V) (_ : DecidableRel G.Adj),
        G.IsSRGWith 99 14 1 2 ∧ n3_zero G := by
  rintro ⟨V, _iv, G, _da, hG, hn3⟩
  rcases Cited.makhnev_lemmas_6_9 (V := V) (G := G) hG hn3 with ⟨W, _iw, Λ, _dl, hΛ⟩
  exact srg33_12_1_6_infeasible ⟨W, _iw, Λ, _dl, hΛ⟩

/-! ## 4. The pure-integer kernel, standalone -/

/-- The kernel-checked arithmetic behind the whole node: `7` does not divide
`2k + (v−1)(λ−μ)` for (v,k,λ,μ) = (33,12,1,6), because that number is `-136`. -/
theorem not_seven_dvd_33_12_1_6_numerator :
    ¬ (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6)) := by
  exact not_seven_dvd_mult_num

#check N3Dichotomy.discriminant_sq
#check N3Dichotomy.mult_num
#check N3Dichotomy.not_seven_dvd_mult_num
#check N3Dichotomy.not_seven_dvd_33_12_1_6_numerator
#check N3Dichotomy.srg33_12_1_6_infeasible
#check N3Dichotomy.no_srg_99_14_1_2_n3_zero

-- The arithmetic kernel: formalised (no axioms).
#print axioms N3Dichotomy.not_seven_dvd_33_12_1_6_numerator

-- The srg(33,12,1,6) infeasibility: rests on the Cited spectral axiom -> conditional.
#print axioms N3Dichotomy.srg33_12_1_6_infeasible

-- The G-n3-zero dichotomy: rests on both Cited axioms -> conditional.
#print axioms N3Dichotomy.no_srg_99_14_1_2_n3_zero

end N3Dichotomy
