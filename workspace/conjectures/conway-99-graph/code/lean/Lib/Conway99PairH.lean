import Mathlib.Combinatorics.SimpleGraph.StronglyRegular
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Powerset

/-!
# Conway 99 — pair-labeling reduction (statement node)

The pair-labeling reduction for a putative `srg(99,14,1,2)`.  Fix a vertex `0`;
its 14 neighbours form, by `λ = 1`, a perfect matching `7K₂` (each neighbour of
`0` is adjacent to exactly one other neighbour of `0`, so the neighbour-induced
graph is a disjoint union of 7 edges).  Every vertex at distance 2 from `0` is a
non-neighbour and, by `μ = 2`, is adjacent to exactly **two** neighbours of `0`.

The reduction's claim (the run's G-H-unsat line) is that the 84 vertices at
distance 2 from `0` biject with the 84 non-matching 2-subsets of the 14-set
(`C(14,2) − 7 = 84`), that the induced outer graph `H` on them is `12`-regular,
and that the pair-labelling obeys the λ=1 / μ=2 recovery rule:

  * outer pair rule: for outer `u,v` whose labels `Pu,Pv` share
    `s = |Pu ∩ Pv| ∈ {0,1}` elements, `u` and `v` have `1 − s` common *outer*
    neighbours if adjacent, and `2 − s` if non-adjacent;
  * inner–outer rule: the number of outer neighbours of `u` whose label contains
    a given element `a` is `1` if `a ∈ Pu`, else `2 − [mate a ∈ Pu]`.

The file carries **statements only**, ending in `:= by sorry`.  It does not
prove the reduction or the existence of `H`; the `sorry` marks exactly what is
not yet established (the candidate `H` is to be *constructed* by the CP-SAT
encoder on the 84 pair-vertices).  `namespace Cited` holds the literature /
run artifact claim that such an `H` exists, as an axiom with its source.
-/

/-- A perfect matching on the 14 neighbours of `0`: an involution of `Fin 14`
with no fixed points (a disjoint union of 7 transpositions = 7 matching edges).
Forced by `λ = 1`: each neighbour of `0` is adjacent to exactly one other
neighbour of `0`, so the neighbour-induced graph is exactly `7K₂`. -/
def IsPerfectMatching (mate : Fin 14 → Fin 14) : Prop :=
  (∀ i : Fin 14, mate (mate i) = i) ∧ (∀ i : Fin 14, mate i ≠ i)

/-- A 2-subset `p` of `Fin 14` is a *matching pair* if it equals `{i, mate i}`
for some `i` — i.e. it is one of the 7 edges of the matching, and is therefore
*not* a valid label of an outer (distance-2) vertex.  -/
def IsMatchingPair (mate : Fin 14 → Fin 14) (p : Finset (Fin 14)) : Prop :=
  ∃ i : Fin 14, p = ({i, mate i} : Finset (Fin 14))

/-- The 2-subsets of `Fin 14` that are **not** matching pairs: these are
exactly the |Out| = 84 labels that a bijection must realise.  -/
noncomputable def NonMatchingPairs (mate : Fin 14 → Fin 14) : Finset (Finset (Fin 14)) :=
  by
    classical
    exact Finset.univ.filter (fun p : Finset (Fin 14) => p.card = 2 ∧ ¬ IsMatchingPair mate p)

/-- The count is `C(14,2) − 7 = 91 − 7 = 84`.  (Stated, not proved: `:= by
sorry`.  It is the arithmetic behind part (b): the 84 distance-2 vertices and
the 84 non-matching pairs have the same cardinality.) -/
theorem nonmatching_pairs_card (mate : Fin 14 → Fin 14) (hM : IsPerfectMatching mate) :
    (NonMatchingPairs mate).card = 84 := by
  sorry

/-- The number of outer neighbours of `u` whose pair-label contains the element
`a` of `Fin 14`.  This is the count in the inner–outer rule.  -/
def OuterNeighborsContaining {Out : Type} [Fintype Out] [DecidableEq Out]
    (H : SimpleGraph Out) [DecidableRel H.Adj] (P : Out → Finset (Fin 14))
    (u : Out) (a : Fin 14) : ℕ :=
  (Finset.univ.filter (fun w : Out => H.Adj u w ∧ a ∈ P w)).card

/-! ## Part (a): the distance-2 condition

Every vertex at distance 2 from `0` is a non-neighbour of `0`, and by `μ = 2`
is adjacent to exactly two neighbours of `0` (its two common neighbours with
`0`).  -/
theorem dist2_adj_exactly_two_nbrs (G : SimpleGraph (Fin 99)) [DecidableRel G.Adj]
    (hG : G.IsSRGWith 99 14 1 2) (zero : Fin 99) (N0 : Finset (Fin 99))
    (hN0 : N0 = G.neighborFinset zero) :
    ∀ x : Fin 99, x ≠ zero → ¬ G.Adj zero x →
      ((G.neighborFinset x).filter (fun y : Fin 99 => y ∈ N0)).card = 2 := by
  sorry

/-! ## Part (b): the bijection

The 84 distance-2 vertices of `0` (the 84 non-neighbours, since `99 − 1 − 14 =
84`) biject with the 84 non-matching 2-subsets of the 14-set.  The labelling
`P` is injective, its labels are exactly the 2-subsets that are not matching
pairs, and `|Out| = 84`.  -/
theorem distance2_bijects_nonmatching_pairs (G : SimpleGraph (Fin 99)) [DecidableRel G.Adj]
    (hG : G.IsSRGWith 99 14 1 2) (zero : Fin 99) :
    ∃ (mate : Fin 14 → Fin 14), IsPerfectMatching mate ∧
      ∃ (Out : Type) (_ : Fintype Out) (_ : DecidableEq Out),
        Fintype.card Out = 84 ∧
        ∃ (P : Out → Finset (Fin 14)),
          (∀ u : Out, (P u).card = 2 ∧ ¬ IsMatchingPair mate (P u)) ∧
          (∀ p : Finset (Fin 14), p.card = 2 → ¬ IsMatchingPair mate p →
            ∃ u : Out, P u = p) := by
  sorry

/-! ## Part (c): the outer graph is 12-regular

The induced outer graph `H` on the 84 pair-vertices is `12`-regular.  -/
theorem outer_12regular {Out : Type} [Fintype Out] (H : SimpleGraph Out) [DecidableRel H.Adj]
    (hcard : Fintype.card Out = 84) : H.IsRegularOfDegree 12 := by
  sorry

/-! ## The pair rule (adjacent and non-adjacent cases)

For outer `u,v` with labels `Pu,Pv` sharing `s = |Pu ∩ Pv| ∈ {0,1}` elements
(the labels are distinct non-matching 2-subsets, so they share 0 or 1 element),
the number of common *outer* neighbours is `1 − s` if `u ~ v`, and `2 − s` if
`u ≁ v`.  This is precisely the λ=1 / μ=2 recovery rule restricted to the outer
vertices.  -/
theorem outer_pair_rule {Out : Type} [Fintype Out] [DecidableEq Out]
    (H : SimpleGraph Out) [DecidableRel H.Adj] (P : Out → Finset (Fin 14))
    (hcard : Fintype.card Out = 84) :
    ∀ u v : Out, u ≠ v →
      let s : ℕ := (P u ∩ P v).card
      (H.Adj u v → Fintype.card (H.commonNeighbors u v) = 1 - s) ∧
      (¬ H.Adj u v → Fintype.card (H.commonNeighbors u v) = 2 - s) := by
  sorry

/-! ## The inner–outer rule

The number of outer neighbours of `u` whose label contains `a ∈ Fin 14` is `1`
if `a ∈ Pu`, and `2 − [mate a ∈ Pu]` otherwise.  -/
theorem inner_outer_rule {Out : Type} [Fintype Out] [DecidableEq Out]
    (mate : Fin 14 → Fin 14) (H : SimpleGraph Out) [DecidableRel H.Adj]
    (P : Out → Finset (Fin 14)) (hcard : Fintype.card Out = 84) :
    ∀ (u : Out) (a : Fin 14),
      OuterNeighborsContaining H P u a =
        if a ∈ P u then 1 else 2 - (if mate a ∈ P u then 1 else 0) := by
  sorry

/-! ## The candidate outer graph `H` exists

The pair-labeling reduction's operative claim: there is a graph `H` on 84
pair-vertices, `12`-regular, obeying the outer pair rule — the object the
CP-SAT encoder on the 3,486 unordered pair-vertices is meant to construct.  It
is a literature / run artifact claim (the encoder passes on both controls, rook
and bvls, at four roots), placed under `namespace Cited` as an axiom.  -/
namespace Cited

/-- src: this run's pair-labeling reduction (G-H-unsat; the predicate in
`code/pair_label_gate_corrected.py` passes clean on both controls, rook(3) with
84-vertices→4 pair-vertices 1-regular and bvls(243,22)→220 pair-vertices
20-regular, at four roots).  There exists an outer graph `H` on the 84
pair-vertices, `12`-regular, whose pair labels are the 84 non-matching 2-subsets
and which obeys the outer pair rule recovered from λ=1 / μ=2.  -/
axiom exists_H :
  ∃ (mate : Fin 14 → Fin 14), IsPerfectMatching mate ∧
    ∃ (Out : Type) (_ : Fintype Out) (_ : DecidableEq Out)
      (H : SimpleGraph Out) (_ : DecidableRel H.Adj) (P : Out → Finset (Fin 14)),
      Fintype.card Out = 84 ∧
      (∀ u : Out, (P u).card = 2 ∧ ¬ IsMatchingPair mate (P u)) ∧
      H.IsRegularOfDegree 12 ∧
      (∀ u v : Out, u ≠ v →
        let s : ℕ := (P u ∩ P v).card
        (H.Adj u v → Fintype.card (H.commonNeighbors u v) = 1 - s) ∧
        (¬ H.Adj u v → Fintype.card (H.commonNeighbors u v) = 2 - s))

end Cited

namespace Conway99PairH

#check dist2_adj_exactly_two_nbrs
#check distance2_bijects_nonmatching_pairs
#check outer_12regular
#check outer_pair_rule
#check inner_outer_rule
#check Cited.exists_H

#print axioms dist2_adj_exactly_two_nbrs
#print axioms distance2_bijects_nonmatching_pairs
#print axioms outer_12regular
#print axioms outer_pair_rule
#print axioms inner_outer_rule
#print axioms Cited.exists_H

end Conway99PairH
