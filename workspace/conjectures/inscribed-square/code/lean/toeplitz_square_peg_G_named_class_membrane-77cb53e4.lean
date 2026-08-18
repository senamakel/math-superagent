import Mathlib

universe u

structure NamedMembraneData where
  Curve : Type u
  LocallyMonotone : Curve → Prop
  InClass : Curve → Prop
  Generator : Curve → Type u
  Membrane : {γ : Curve} → Generator γ → Type u
  SpecialTrapezoid : {γ : Curve} → {ω : Generator γ} → Membrane ω → Prop
  isGenerator : {γ : Curve} → Generator γ → Prop
  avoids : {γ : Curve} → Generator γ → Prop
  class_contains_locally_monotone : ∀ {γ : Curve}, LocallyMonotone γ → InClass γ
  class_strict : ∃ γ : Curve, InClass γ ∧ ¬ LocallyMonotone γ
  membrane_avoids_iff : ∀ {γ : Curve} (ω : Generator γ),
    avoids ω ↔ ∀ x : Membrane ω, ¬ SpecialTrapezoid x

/--
The binder `d` packages a named class and its membrane model.  `γ` carries
membership in the class.  `ω` carries the generator witness and
`isGenerator ω`; the final universal statement is the literal empty
intersection condition `P₄(ω) ∩ S = ∅`.
-/
theorem named_class_membrane_avoidance
    (d : NamedMembraneData)
    (hC : ∀ γ : d.Curve, d.InClass γ → ∃ ω : d.Generator γ,
      d.isGenerator ω ∧ d.avoids ω) :
    ∀ γ : d.Curve, d.InClass γ → ∃ ω : d.Generator γ,
      d.isGenerator ω ∧ ∀ x : d.Membrane ω, ¬ d.SpecialTrapezoid x := by
  intro γ hγ
  obtain ⟨ω, hgen, hav⟩ := hC γ hγ
  exact ⟨ω, hgen, (d.membrane_avoids_iff ω).mp hav⟩

/- The genuinely geometric existence premise is isolated here; it is not
   proved by this file. -/

#print axioms named_class_membrane_avoidance
