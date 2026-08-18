import Mathlib.Topology.Instances.AddCircle.Real
import Mathlib.Analysis.InnerProductSpace.PiL2

/-!
Formal statement of Toeplitz's inscribed-square conjecture.

The domain is represented by `AddCircle (1 : ℝ)`, the additive circle ℝ/ℤ.  A
Jordan curve is represented explicitly as a continuous injective map into
`EuclideanSpace ℝ (Fin 2)`.

The square predicate uses the four points in the order selected by the
parameters `t₁ t₂ t₃ t₄`: its algebraic conditions are a common midpoint,
perpendicular diagonals, and equal diagonal lengths.  The additional
`CyclicallyOrdered` hypothesis is what forces this to be a genuine square
rather than a crossed quadrilateral: the four parameter values must occur in
the order `t₁ t₂ t₃ t₄` as one goes around the circle.
-/

open scoped Topology RealInnerProductSpace

namespace Toeplitz

abbrev Circle := AddCircle (1 : ℝ)
abbrev Plane := EuclideanSpace ℝ (Fin 2)

/-- `t₁ t₂ t₃ t₄` occur in this cyclic order around the circle: they have
lifts `a < b < c < d < a + 1` to the real line, each mapping down to the
corresponding point.  This is the "correct cyclic order" hypothesis of the
problem — the condition that separates a genuine inscribed square from a
crossed quadrilateral satisfying the algebraic square equations. -/
def CyclicallyOrdered (t₁ t₂ t₃ t₄ : Circle) : Prop :=
  ∃ a b c d : ℝ,
    a < b ∧ b < c ∧ c < d ∧ d < a + 1 ∧
    (a : Circle) = t₁ ∧ (b : Circle) = t₂ ∧ (c : Circle) = t₃ ∧
    (d : Circle) = t₄

/-- Four points are the vertices of a square in the prescribed cyclic order.
The first condition says the diagonals share a midpoint; the second that they
are perpendicular; the third that they have equal length. -/
def IsInscribedSquare (γ : Circle → Plane) (t₁ t₂ t₃ t₄ : Circle) : Prop :=
  (γ t₁ + γ t₃ = γ t₂ + γ t₄) ∧
  (⟪γ t₁ - γ t₃, γ t₂ - γ t₄⟫ = 0) ∧
  (‖γ t₁ - γ t₃‖ = ‖γ t₂ - γ t₄‖)

/-- Toeplitz's conjecture: every continuous injective parametrized circle in
the plane inscribes a square.

Two hypotheses of the informal statement are *not* encoded here, and this
statement is deliberately weaker than the conjecture as a result:

1. `γ` is required to be injective (an injective continuous parametrization
   of a Jordan curve exists by the Jordan–Schoenflies theorem).  The
   conjecture is usually stated for the curve as a set; the parametrized
   formulation is the standard equivalent one.
2. "Square" is captured by the diagonal conditions of a square in the cyclic
   order of the four vertices (`IsInscribedSquare` plus `CyclicallyOrdered`),
   not by an intrinsic definition of a square as a set of four points.  The
   two are equivalent for nondegenerate squares; formalising that equivalence
   is part of the work, not of the statement.

The pairwise-distinctness conjuncts are redundant given `CyclicallyOrdered`
(lifts `a < b < c < d < a + 1` are pairwise distinct modulo 1) and are kept
only to make the statement readable in isolation. -/
theorem toeplitz_inscribed_square
    (γ : Circle → Plane)
    (hγ_cont : Continuous γ)
    (hγ_inj : Function.Injective γ) :
    ∃ t₁ t₂ t₃ t₄ : Circle,
      CyclicallyOrdered t₁ t₂ t₃ t₄ ∧
      t₁ ≠ t₂ ∧ t₁ ≠ t₃ ∧ t₁ ≠ t₄ ∧
      t₂ ≠ t₃ ∧ t₂ ≠ t₄ ∧ t₃ ≠ t₄ ∧
      IsInscribedSquare γ t₁ t₂ t₃ t₄ := by sorry

#print axioms toeplitz_inscribed_square

end Toeplitz
