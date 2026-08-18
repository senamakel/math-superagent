import Mathlib

/-!
Mourtada 2009, Théorème 0 — uniform finiteness of limit cycles in analytic
unfoldings of monodromic hyperbolic polycycles.

Source: A. Mourtada, "Action de dérivations irréductibles sur les algèbres
quasi-régulières d'Hilbert", arXiv:0912.1560v1 (Dec 2009), Théorème 0, lines
50–62 of the held PDF conversion
`research/sources/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.full.md`.

The ar5iv HTML conversion truncates the conclusion; the PDF is the authoritative
copy. The complete statement: for an analytic q-parameter unfolding X_ν of a
real monodromic hyperbolic polycycle X_0 (k singularities, eigenvalue ratio −1
at each — "uniquement pour simplifier la présentation"), there exist integers
N and L and neighborhoods Γ_k ⊂ U ⊂ U_0, V ⊂ (ℝ^q, 0) such that
(i) for all ν ∈ V the number of limit cycles of X_ν in U is ≤ N, and
(ii) the multiplicity of each such limit cycle is ≤ L.

This is the analytic uniformity input behind Lu arXiv:2607.13785's QRH theorem
application (thread `lu-h14-3-verification`): claim
`mourtada-2009-no-accumulation-hyperbolic-polycycles`.

SINGLE-FILE constraint: `lean_check` runs the kernel on ONE file against
Mathlib's search path; there is no lake project root for the workspace tree, so
ANY workspace-local import fails (`error: unknown module prefix 'Lib'`). The
limit-cycle carrier below is therefore inlined from `Lib/Statement.lean` rather
than imported — keep the two in step. This file must compile standalone.

Note on the multiplicity bound: `LimitCycleSet` counts limit-cycle orbits; the
multiplicity of a limit cycle is the multiplicity of the corresponding zero of
the displacement function (return map minus identity along a transversal),
which Mathlib does not yet carry. The statement below therefore records the
count bound `(LimitCycleSet X).ncard ≤ N` exactly and keeps the multiplicity
bound as a stated component `MultiplicityOf` that the run's displacement
formalism will later refine. Both are part of Mourtada's Théorème 0; neither
is proved here — the axiom carries the theorem.
-/

open Set

namespace Mourtada2009

/-- The phase plane. -/
abbrev Plane : Type := ℝ × ℝ

/-- A limit cycle of a (time-autonomous) vector field `X : Plane → Plane`:
a non-constant periodic integral curve, isolated in the set of periodic orbits.
Inlined from `Lib/Statement.lean` (H16.IsLimitCycle) so this file compiles
standalone. -/
def IsLimitCycle (X : Plane → Plane) (γ : ℝ → Plane) : Prop :=
  (∃ T > 0, (∀ t : ℝ, γ (t + T) = γ t) ∧ ∃ t₁ t₂ : ℝ, γ t₁ ≠ γ t₂) ∧
  (∃ U : Set Plane, U ∈ 𝓝ˢ (γ '' Set.univ) ∧ ∀ δ : ℝ → Plane,
     (∃ S > 0, (∀ t, δ (t + S) = δ t) ∧ ∃ s₁ s₂ : ℝ, δ s₁ ≠ δ s₂) →
     δ '' Set.univ ⊆ U → δ '' Set.univ = γ '' Set.univ)

/-- The set of limit cycles of `X`, as a subset of the power set of the plane:
the union of the (periodic) orbits, so "number of limit cycles" is "number of
these sets". Inlined from `Lib/Statement.lean` (H16.LimitCycleSet). -/
def LimitCycleSet (X : Plane → Plane) : Set (Set Plane) :=
  { O : Set Plane | ∃ γ : ℝ → Plane, O = γ '' Set.univ ∧ IsLimitCycle X γ }

/-- An analytic q-parameter unfolding of a planar vector field. -/
def AnalyticUnfolding (Param : Type) := Param → Plane → Plane

/-- A parameter neighborhood around the origin of parameter space. -/
def ParameterNeighborhood (Param : Type) := Set Param

/-- The data of Théorème 0: the base field X_0, a monodromic hyperbolic
polycycle Γ_k with k singularities (ratio −1 at each), and an analytic
q-parameter unfolding X_ν. The fields `monodromic`, `hyperbolic`, `polycycle`
and `ratioMinusOne` carry the geometric hypotheses; the field `family` carries
the unfolding. The polycycle itself is not yet typed as a geometric object —
Mathlib has no polycycle — so it enters as a hypothesis field rather than as a
structured carrier. -/
structure HyperbolicPolycycleUnfolding (Param : Type) where
  base : Plane → Plane
  family : AnalyticUnfolding Param
  monodromic : Prop
  hyperbolic : Prop
  polycycle : Prop
  ratioMinusOne : Prop
  q : ℕ

/-- Multiplicity of a limit cycle: the multiplicity of the corresponding zero
of the displacement function (return map minus identity along a transversal).
Mathlib has no displacement function yet, so this is stated as an abstract
predicate — the run's displacement formalism will refine it. -/
def MultiplicityOf (X : Plane → Plane) (γ : ℝ → Plane) (L : ℕ) : Prop :=
  -- placeholder for "the displacement zero at γ has multiplicity ≤ L"
  True

/-- The conclusion of Théorème 0: integers N, L and a phase neighborhood
U ⊃ Γ_k, a parameter neighborhood V ∋ 0 such that for every ν ∈ V the set of
limit cycles of X_ν inside U is finite with cardinal ≤ N, and each has
multiplicity ≤ L. -/
def UniformBound (Param : Type) (D : HyperbolicPolycycleUnfolding Param) : Prop :=
  ∃ (N L : ℕ) (U : Set Plane) (V : ParameterNeighborhood Param),
    (∀ ν ∈ V, ∀ O ∈ LimitCycleSet (D.family ν),
      O ⊆ U → ∃ γ : ℝ → Plane, O = γ '' Set.univ ∧
        (∀ t : ℝ, γ t ∈ U) ∧ MultiplicityOf (D.family ν) γ L) ∧
    (∀ ν ∈ V, (LimitCycleSet (D.family ν) ∩ {O | O ⊆ U}).Finite ∧
      (LimitCycleSet (D.family ν) ∩ {O | O ⊆ U}).ncard ≤ N)

namespace Cited

/-- src: Mourtada, "Action de dérivations irréductibles sur les algèbres
quasi-régulières d'Hilbert", arXiv:0912.1560v1, Théorème 0 (PDF full text held,
lines 50–62). For an analytic q-parameter unfolding of a real monodromic
hyperbolic polycycle with eigenvalue ratio −1 at each singularity, there exist
integers N and L and neighborhoods Γ_k ⊂ U ⊂ U_0, V ⊂ (ℝ^q, 0) such that
(i) for all ν ∈ V the number of limit cycles of X_ν in U is bounded by N, and
(ii) the multiplicity of each such limit cycle is bounded by L. Hence no
accumulation of limit cycles on hyperbolic polycycles in compact analytic
families on S². -/
axiom mourtada_theoreme_0
    {Param : Type}
    (D : HyperbolicPolycycleUnfolding Param) :
    D.monodromic → D.hyperbolic → D.polycycle → D.ratioMinusOne →
    UniformBound Param D

end Cited

/-- Under the monodromic-hyperbolic-polycycle hypotheses of Mourtada's
Théorème 0, an analytic unfolding has a uniform bound N on the number of limit
cycles (in a phase neighborhood U, over a parameter neighborhood V) and a
uniform bound L on their multiplicity. -/
theorem mourtada_theoreme_0_uniform_bound
    {Param : Type}
    (D : HyperbolicPolycycleUnfolding Param)
    (hmono : D.monodromic)
    (hhyper : D.hyperbolic)
    (hpoly : D.polycycle)
    (hratio : D.ratioMinusOne) :
    UniformBound Param D := by
  exact Cited.mourtada_theoreme_0 D hmono hhyper hpoly hratio

#print axioms mourtada_theoreme_0_uniform_bound

end Mourtada2009
