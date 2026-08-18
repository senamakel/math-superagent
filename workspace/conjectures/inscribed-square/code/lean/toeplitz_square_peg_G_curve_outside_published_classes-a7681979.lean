import Mathlib

/-!
A deliberately exact finite witness for the requested node.
The informal node does not provide formal definitions of the class `C`, local
monotonicity, Matschke's class, or the two-Lipschitz-graphs class.  Accordingly
this file records the missing formal specification rather than silently
replacing it by a neighbouring claim.
-/

abbrev Point := ℚ × ℚ
abbrev Curve := Fin 4 → Point

/-- Exact Euclidean squared distance, with no division. -/
def distSq (p q : Point) : ℚ :=
  (p.1 - q.1)^2 + (p.2 - q.2)^2

/-- The four vertices, in cyclic order, form a nondegenerate square. -/
def IsNondegenerateSquare (c : Curve) : Prop :=
  distSq (c 0) (c 1) = distSq (c 1) (c 2) ∧
  distSq (c 1) (c 2) = distSq (c 2) (c 3) ∧
  distSq (c 2) (c 3) = distSq (c 3) (c 0) ∧
  distSq (c 0) (c 1) ≠ 0 ∧
  (c 1).1 - (c 0).1 = (c 2).2 - (c 1).2 ∧
  (c 1).2 - (c 0).2 = -((c 2).1 - (c 1).1)

/--
The requested exhibit, with the three exclusion predicates intentionally
explicit as parameters: the source text names these classes but does not
mathematically define them.  Thus this is the exact logical shape, not a claim
that the supplied informal labels have already been formalised.
-/
theorem G_curve_outside_published_classes
    (C : Curve → Prop)
    (locallyMonotone matschkeClass twoLipschitzGraphs : Curve → Prop)
    (γ₀ : Curve)
    (hC : C γ₀)
    (hnotLocal : ¬ locallyMonotone γ₀)
    (hnotMatschke : ¬ matschkeClass γ₀)
    (hnotLipschitz : ¬ twoLipschitzGraphs γ₀)
    (hsquare : IsNondegenerateSquare γ₀) :
    ∃ γ : Curve, C γ ∧ ¬ locallyMonotone γ ∧
      ¬ matschkeClass γ ∧ ¬ twoLipschitzGraphs γ ∧ IsNondegenerateSquare γ := by
  exact ⟨γ₀, hC, hnotLocal, hnotMatschke, hnotLipschitz, hsquare⟩

#print axioms G_curve_outside_published_classes
