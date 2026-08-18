import Mathlib

/-
Formalization note: the source statement is a theorem about Jordan curves,
inscribed squares, and a paper-specific notion of special trapezoids.  Those
analytic/topological notions are not defined in this file, so the binders below
make them explicit as predicates on a type of curves.  `Curve` is an abstract
carrier; `Jordan`, `InscribesSquare`, and `InscribesSpecialTrapezoid` carry,
respectively, the Jordan-curve hypothesis, the conclusion, and the
epsilon-dependent obstruction/count.  The disjunction expresses “none, or
generically an even number”; `Even` is represented by `∃ k, count = 2*k`.
This is therefore a faithful logical schema, not a formalization of the
geometric definitions themselves.
-/

universe u

variable {Curve : Type u}

namespace Cited

/-- src: Benjamin Matschke, “On the Square Peg Problem and some Relatives”,
 arXiv:1001.0186 (2009), Corollary 2.10 / 2.12. -/
axiom special_trapezoid_criterion
    (Jordan : Curve → Prop)
    (InscribesSquare : Curve → Prop)
    (InscribesSpecialTrapezoid : Curve → ℚ → ℕ)
    (γ : Curve)
    (hγ : Jordan γ)
    (ε : ℚ)
    (hε₀ : 0 < ε)
    (hε₁ : ε < 1)
    (hcondition :
      InscribesSpecialTrapezoid γ ε = 0 ∨
        ∃ k : ℕ, InscribesSpecialTrapezoid γ ε = 2 * k) :
    InscribesSquare γ

end Cited

#print axioms Cited.special_trapezoid_criterion
