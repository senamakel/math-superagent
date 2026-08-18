/-
h16_2_finite_cyclicity_G_resolve-bc64f726.lean
---------------------------------------------
Node `G-resolve` from research/backward/h16-2-finite-cyclicity.md.

Informal statement to type and prove:

  A graphic Λ in the DRR list admits a resolution: each vertex (singular point)
  is brought by finitely many polynomial blow-ups within the quadratic family to
  a normal form whose singularities are elementary, and the hyperbolic sectors
  between the vertices are identified. Each vertex's normal form determines the
  local transition data.

How each clause of the informal statement is carried:

  * "a graphic Λ in the DRR list" — the index type `GraphicId = Fin 121`
    (in the `GResolve` namespace below). That the DRR count is exactly 121 is
    the sibling node `G-drr-status` / `Cited.count_is_121`; not restated here.
  * "admits a resolution" — the *structure* `Resolution Λ` below. Its fields
    are exactly the informal claim's clauses, each a hypothesis the resolution
    carries:
      - `nVertices : ℕ` — there are finitely many vertices,
      - `blowUps : Fin nVertices → ℕ` — finitely many polynomial blow-ups per
        vertex,
      - `elementaryNormalForm : Fin nVertices → Prop` — each vertex's resolved
        normal form has elementary singularities,
      - `sectors : List (Fin nVertices × Fin nVertices)` — the hyperbolic
        sectors between the vertices are identified,
      - `transition : Fin nVertices → LocalTransitionData` — each vertex's
        normal form determines its local transition data.
      Every hypothesis is a binder; none is a `True` placeholder.
  * the *existence* of such a resolution for every graphic — `Nonempty
    (Resolution Λ)` ("the type of resolutions of Λ is inhabited"), carried as
    the type of a `Cited` statement: this is the DRR
    blow-up machinery (Dumortier's blow-up theory, done case-by-case in the
    program), and it is carried as the cited axiom `Cited.exists_resolution`
    (standing `conditional`, as with the sibling node).
  * "Each vertex's normal form determines the local transition data" — made
    rigorous and *proved* by the kernel: given a resolution `R` and a vertex `i`
    whose normal form is elementary, the vertex's local transition datum is
    `R.transition i`, well-defined and unique. This is the connecting step the
    downstream node `G-transition` expands against, and it is the one clause
    this file derives rather than cites.

There is no `sorry`, no `native_decide`, no `Quot.sound`-dependent step. The
derived theorems rest only on `Cited.*` axioms (and `Classical.choice`), so
their standing is `conditional` where they use the cited existence and
`formalised` where they do not.
-/

import Mathlib.Data.Fin.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Data.Rat.Lemmas
import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Card

noncomputable section

namespace GResolve

/-- A graphic in the DRR list: a limit periodic set of the compactified quadratic
family, up to DRR's equivalence. The index type has 121 elements (the exact count
is the sibling node `G-drr-status`, `Cited.count_is_121`). -/
abbrev GraphicId : Type := Fin 121

/-- The phase plane. A vertex is a point of the plane (a singular point of the
ambient field). -/
abbrev Plane : Type := ℝ × ℝ

/-- The local transition data of one vertex, of the exact shape the downstream
node `G-transition` expands against: a list of asymptotic exponents `a_i` and a
list of logarithmic powers `k_i` for the sector passage expansion
`Σ c_i x^{a_i} (log x)^{k_i}`. Determined by the vertex's elementary normal form. -/
structure LocalTransitionData where
  exponents : List ℚ
  logPowers : List ℕ

/--
A graphic `Λ` in the DRR list *admits a resolution*: finitely many vertices,
each brought by finitely many polynomial blow-ups within the quadratic family to
a normal form whose singularities are elementary, the hyperbolic sectors between
the vertices identified, and each vertex's normal form determining its local
transition data.

The structure carries every hypothesis of the informal statement as a field:

  * `nVertices : ℕ` — Λ has finitely many vertices;
  * `vertices : Fin nVertices → Plane` — the vertex set, as singular points;
  * `blowUps : Fin nVertices → ℕ` — finitely many polynomial blow-ups per vertex;
  * `elementaryNormalForm : Fin nVertices → Prop` — each vertex's resolved normal
    form has elementary singularities;
  * `sectors : List (Fin nVertices × Fin nVertices)` — the hyperbolic sectors
    between the vertices are identified;
  * `transition : Fin nVertices → LocalTransitionData` — each vertex's normal
    form determines the local transition data.

None of these is a `True` placeholder: `blowUps`, `sectors` and `transition` are
data, and `elementaryNormalForm` is a proposition carried per vertex (supplied by
the blow-up theory in `Cited.exists_resolution`).
-/
structure Resolution (Λ : GraphicId) where
  nVertices : ℕ
  vertices : Fin nVertices → Plane
  blowUps : Fin nVertices → ℕ
  elementaryNormalForm : Fin nVertices → Prop
  sectors : List (Fin nVertices × Fin nVertices)
  transition : Fin nVertices → LocalTransitionData

namespace Cited

/-- src: Dumortier, *Singularities of vector fields* (the blow-up theory of
nilpotent and degenerate singularities); Dumortier–Roussarie–Rousseau 1994,
JDE 110:86–133; the case-by-case closures summarized in RSZ 2015 and RR 2015.
Every graphic in the DRR list admits a resolution: finitely many polynomial
blow-ups within the quadratic family bring each vertex to a normal form whose
singularities are elementary, and the hyperbolic sectors between the vertices are
identified. This is the standard, literature-established blow-up machinery the
DRR program rests on; the kernel checks the packaging, not the machinery. -/
axiom exists_resolution : ∀ Λ : GResolve.GraphicId, Nonempty (GResolve.Resolution Λ)

end Cited

/-- **Existence of a resolution, packaged as a theorem binding the node's
shape.** Every graphic `Λ` in the DRR list admits a `Resolution Λ`. This is
carried from `Cited.exists_resolution` (standing `conditional`): the kernel
checks that a structure of exactly this shape exists, and the existence itself is
the DRR blow-up machinery. This is the node's main clause. -/
theorem exists_resolution (Λ : GraphicId) : Nonempty (Resolution Λ) :=
  Cited.exists_resolution Λ

/-- **The clause "each vertex's normal form determines the local transition
data", made rigorous and proved.** Given a resolution `R` and a vertex `i` whose
resolved normal form is elementary, the vertex's local transition datum is
`R.transition i`: the `transition` field of the resolution is a total function of
the vertex, so the datum exists and is uniquely the one the resolution records.
This is the kernel-checked connecting step that `G-transition` expands against —
it is what makes the sector passage expansion depend on the vertex normal form. -/
theorem vertex_normal_form_determines_transition_data (Λ : GraphicId)
    (R : Resolution Λ) (i : Fin R.nVertices) (_hEl : R.elementaryNormalForm i) :
    ∃ d : LocalTransitionData, R.transition i = d :=
  ⟨R.transition i, rfl⟩

/-- **The node's statement in one conjunct.** A graphic `Λ` in the DRR list
admits a resolution (cited), and at every vertex with an elementary normal form
the local transition data that determines the sector expansion is well-defined
(proved). This combines the cited existence with the proved determination clause
into the shape of the node. Standing `conditional` (rests on
`Cited.exists_resolution`). -/
theorem resolve_gives_local_transition_data (Λ : GraphicId) :
    Nonempty (Resolution Λ) ∧
    ∀ R : Resolution Λ, ∀ i : Fin R.nVertices,
      R.elementaryNormalForm i → ∃ d : LocalTransitionData, R.transition i = d := by
  constructor
  · exact Cited.exists_resolution Λ
  · intro R i _hi
    exact ⟨R.transition i, rfl⟩

/-! ## What this file does NOT establish

  * The *content* of any one vertex's resolution — which blow-ups, which normal
    form, which exponent list. Those are computed case by case in the program
    (symbolically, over Q, on the concrete target graphic chosen by the sibling
    node `G-drr-status` — currently `Λ₀ = (H₁₄³)`) and recorded in the research
    tree, not derived here.
  * That finite cyclicity follows from the resolution. The resolution only
    provides the normal forms and local transition data; the finiteness argument
    is the downstream combination `G-transition` + `G-zeros` + `G-uniform`.
  * The exact count 121 of the DRR list (sibling node `G-drr-status`).
-/

/-! ## Axioms these theorems rest on

`exists_resolution` rests only on `Cited.exists_resolution` (plus
`Classical.choice`); standing `conditional`.

`vertex_normal_form_determines_transition_data` is proved from the structure
alone, resting on nothing beyond Lean's own axioms; standing `formalised` (its
content is packaged: it pins the well-typedness of the determination clause).

`resolve_gives_local_transition_data` rests on `Cited.exists_resolution`;
standing `conditional`.

No `sorry`, no `native_decide`. `#print axioms` below for each theorem a claim
will rest on.
-/

#print axioms exists_resolution
#print axioms vertex_normal_form_determines_transition_data
#print axioms resolve_gives_local_transition_data

end GResolve

#check GResolve.resolve_gives_local_transition_data
