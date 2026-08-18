import Mathlib.Data.Fin.Basic

noncomputable section

namespace DRR94

opaque SmoothPlanarField : Type
opaque Graphic : Type
opaque AttractingHyperbolicSaddle : SmoothPlanarField → Prop
opaque AttractingSemihyperbolicPoint : SmoothPlanarField → Prop
opaque OppositeCharacterPair : SmoothPlanarField → Prop
opaque FixedConnections : SmoothPlanarField → Prop
opaque RatioGreaterThanOne : SmoothPlanarField → Prop
opaque Cyclicity : SmoothPlanarField → Graphic → ℕ
opaque QuadraticSystem : Type
opaque QuadraticGraphic : QuadraticSystem → Graphic → Prop
opaque GenericConditions : QuadraticSystem → Prop

namespace Cited
axiom quadratic_field_as_smooth : QuadraticSystem → SmoothPlanarField
/-- src: Dumortier–Roussarie–Rousseau, Nonlinearity 7(3) (1994), abstract. -/
axiom attracting_mixed_graphic_cyclicity_one :
  ∀ X G, FixedConnections X →
    (AttractingHyperbolicSaddle X ∧ RatioGreaterThanOne X) →
    AttractingSemihyperbolicPoint X → Cyclicity X G = 1
/-- src: Dumortier–Roussarie–Rousseau, Nonlinearity 7(3) (1994), abstract. -/
axiom opposite_character_graphic_cyclicity_two :
  ∀ X G, FixedConnections X → OppositeCharacterPair X → Cyclicity X G = 2
/-- src: Dumortier–Roussarie–Rousseau, Nonlinearity 7(3) (1994), abstract. -/
axiom quadratic_33_graphics_at_most_two :
  ∀ X G, QuadraticGraphic X G →
    (GenericConditions X ∨ ¬ GenericConditions X) →
    Cyclicity (quadratic_field_as_smooth X) G ≤ 2
end Cited

/- gap
id: drr94-mixed-cyclicity-one
lemma: ∀ X G, FixedConnections X → (AttractingHyperbolicSaddle X ∧ RatioGreaterThanOne X) → AttractingSemihyperbolicPoint X → Cyclicity X G = 1
status: cited-axiom, unproved here
next: formalize the fixed-connection and attracting hypotheses using a concrete planar-flow model, then compare its return-map displacement germ with the cited theorem
-/

/- gap
id: drr94-opposite-character-cyclicity-two
lemma: ∀ X G, FixedConnections X → OppositeCharacterPair X → Cyclicity X G = 2
status: cited-axiom, unproved here
next: define opposite character from local eigenvalue/transition-map data and prove the corresponding displacement-map zero bound
-/

/- gap
id: drr94-quadratic-33-bound
lemma: ∀ X G, QuadraticGraphic X G → (GenericConditions X ∨ ¬ GenericConditions X) → Cyclicity (Cited.quadratic_field_as_smooth X) G ≤ 2
status: cited-axiom, unproved here
next: state the finite 33-graphic enumeration and connect each row to one of the two general hypotheses or its generic exceptional case
-/

theorem drr94_cyclicity_1_2_abstract :
    (∀ X G, FixedConnections X →
      (AttractingHyperbolicSaddle X ∧ RatioGreaterThanOne X) →
      AttractingSemihyperbolicPoint X → Cyclicity X G = 1) ∧
    (∀ X G, FixedConnections X → OppositeCharacterPair X → Cyclicity X G = 2) ∧
    (∀ X G, QuadraticGraphic X G →
      (GenericConditions X ∨ ¬ GenericConditions X) →
      Cyclicity (Cited.quadratic_field_as_smooth X) G ≤ 2) := by
  exact ⟨Cited.attracting_mixed_graphic_cyclicity_one,
    Cited.opposite_character_graphic_cyclicity_two,
    Cited.quadratic_33_graphics_at_most_two⟩

#print axioms drr94_cyclicity_1_2_abstract
end DRR94
