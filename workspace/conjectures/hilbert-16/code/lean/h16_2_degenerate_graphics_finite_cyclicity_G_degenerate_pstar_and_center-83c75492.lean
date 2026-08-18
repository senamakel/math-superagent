import Mathlib.Data.Set.Card

/-!
Node `h16-2-degenerate-graphics-finite-cyclicity/G-degenerate-pstar-and-center`.

The source node says that two residual strata remain after the generic
slow-divergence analysis: the center stratum, where the SDI vanishes
identically, and the non-desingularizable exceptional point P*. The analytic
Bautin/Darboux and Huzak-style estimates are not proved here. This file states
the exact conditional recombination lemma: if each residual stratum has a
finite supplied bound and the strata cover the parameters, their union has the
maximum bound.

Binder correspondence:
* `Parameter` is the normal-form parameter space.
* `centerStratum` carries the identically-zero-SDI center conditions;
  `centerBound` carries the missing Bautin-blow-up/Darboux estimate.
* `pstar` carries the non-desingularizable P* stratum; `pstarBound` carries
  the missing port of the Huzak closure.
* `cycles` is a finite-set encoding of cycles counted by displacement zeros.
* `hpartition` is the residual-strata cover.
-/

namespace DegeneratePstarCenter

/-- Data for the two residual strata of a normal-form family. -/
structure ResidualData (Parameter Cycle : Type) where
  centerStratum : Set Parameter
  pstar : Set Parameter
  cycles : Parameter → Finset Cycle
  centerBound : ℕ
  pstarBound : ℕ
  hcenter : ∀ p, p ∈ centerStratum → (cycles p).card ≤ centerBound
  hpstar : ∀ p, p ∈ pstar → (cycles p).card ≤ pstarBound
  hpartition : ∀ p, p ∈ centerStratum ∨ p ∈ pstar

/-- The residual center/P* strata admit one common bound, the maximum of the
 two supplied stratum bounds. -/
theorem residual_strata_uniform_bound
    {Parameter Cycle : Type} (D : ResidualData Parameter Cycle) :
    ∃ N : ℕ, ∀ p : Parameter, (D.cycles p).card ≤ N := by
  refine ⟨max D.centerBound D.pstarBound, ?_⟩
  intro p
  rcases D.hpartition p with hp | hp
  · exact le_trans (D.hcenter p hp) (Nat.le_max_left _ _)
  · exact le_trans (D.hpstar p hp) (Nat.le_max_right _ _)

#print axioms residual_strata_uniform_bound

end DegeneratePstarCenter
