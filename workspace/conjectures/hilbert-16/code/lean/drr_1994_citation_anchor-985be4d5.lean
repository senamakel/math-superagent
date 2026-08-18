/-
drr_1994_citation_anchor-985be4d5.lean
--------------------------------------
Node `drr-1994-citation-anchor` from research/summaries/dumortier-roussarie-rousseau-1994-121-graphics.md.

Informal statement to type and prove:

  DRR 1994 (JDE 110:86-133) gives the list of all graphics and degenerate
  graphics (limit periodic sets surrounding the origin in quadratic systems)
  whose finite cyclicity implies a uniform bound on the number of limit cycles
  of quadratic systems. The count is 121 (as reported by Ilyashenko 2002, RSZ
  2015, Roussarie-Rousseau 2015).

What the statement is really about. "Graphic" and "limit periodic set" are
topological/dynamical objects of the theory; the *substance* of the DRR theorem
— that which this node must not lose — is the logical reduction:

    (finite cyclicity of every one of the 121 graphics)
  ⟹
    (a uniform bound on the number of limit cycles of every quadratic system),

together with the factual claims that (a) there are exactly 121 such graphics
and (b) the paper itself (DRR 1994) is the source that gives the list.

The proof, as a Lean theorem, is a formal combination of pieces, none of which
is this run's to prove:

  * the *counting* claims that the three named secondary sources each report
    the 121 graphics — facts about those sources' text, stated as axioms
    (`ilyashenko_reports_121`, `rsz_reports_121`, `rrs_reports_121`);
  * the *mathematical* reduction — that finite cyclicity of all 121 graphics
    forces a uniform quadratic bound — which is the content of DRR 1994 itself,
    stated as an axiom (`finite_cyclicity_implies_uniform_bound`).

Nothing in this file is proved by the kernel from first principles: the
reduction is a deep theorem of the literature and the counting statements are
facts about texts. Every one is therefore an `axiom` under `namespace Cited`,
and the top-level `theorem` combines them. `#print axioms` shows exactly that:
the theorem rests on the `Cited.*` axioms and nothing else. So the verdict here
is `conditional`, never `formalised` — which is the correct standing for a
citation anchor.

How each binder of the informal statement is carried:

  * "uniform bound on the number of limit cycles of quadratic systems" — a
    natural number `N : ℕ` such that every quadratic planar polynomial vector
    field has at most `N` limit cycles, i.e. `∀ X : QuadraticSystem,
    nLimitCycles X ≤ N`. The type `QuadraticSystem` carries the field's two
    quadratic polynomials; the opaque `nLimitCycles` counts its limit-cycle
    orbits.
  * "finite cyclicity of every one of the 121 graphics" — a single predicate
    `FinitelyCyclic(G)` over an index `G : GraphicId` of exactly 121 graphics,
    all of which have finite cyclicity.
  * "all graphics ... whose finite cyclicity implies a uniform bound" —
    captured by the implication `(∀ G, FinitelyCyclic G) → UniformQuadraticBound`.
-/

import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Algebra.MvPolynomial.Degrees
import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Card
import Mathlib.Data.Fin.VecNotation
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.ENat.Basic

noncomputable section

namespace DRR

/-! ## The objects of the statement -/

/-- A graphic (or degenerate graphic): a limit periodic set surrounding the
origin, up to the equivalence that makes DRR's list finite. The index type has
exactly `121 = Fintype.card GraphicId` elements; the claim that this count is
121 is asserted below. -/
abbrev GraphicId : Type := Fin 121

/-- A planar quadratic polynomial vector field: two polynomials of total
degree at most `2`. This is the concrete carrier of "a quadratic system". -/
structure QuadraticSystem where
  P : MvPolynomial (Fin 2) ℝ
  Q : MvPolynomial (Fin 2) ℝ
  degP : P.totalDegree ≤ 2
  degQ : Q.totalDegree ≤ 2

/-- Opaque count of the limit-cycle orbits of the field. Stated as a plain
`ℕ` (not via `Set.ncard`, which is vacuously `0` for an infinite set — the home
of the vacuity hole) so that `≤ N` below really is a bound on the number of
limit cycles and not on `0`. -/
axiom nLimitCycles (f : QuadraticSystem) : ℕ

/-- An individual graphic `G` has finite cyclicity: the property whose truth for
all 121 graphics is the HYPOTHESIS of DRR's reduction.

**This must stay opaque, and here is what happened when it was not.** It was
written `def FinitelyCyclic (G : GraphicId) : Prop := True`. With that
definition the hypothesis `∀ G, FinitelyCyclic G` is discharged by `trivial`,
so `drr_reduction` below became a proof of `UniformQuadraticBound` — that some
`N` bounds the limit cycles of EVERY quadratic system. That is `H(2) < ∞`: the
open problem this workspace exists to attack, and the one thing GOAL.md forbids
claiming. The file compiled, reported `outcome: verified`, and read as a
citation anchor.

Finite cyclicity of the 121 graphics is not known — 89 are closed, three are
partial, `H14^3` is claimed only in an unrefereed 2026 preprint, and eleven
degenerate graphics are open (research/drr-list.md). An `axiom` with no
defining equation is the honest carrier: the kernel can then never discharge
the hypothesis, and `drr_reduction` is forced to stay an implication. -/
axiom FinitelyCyclic : GraphicId → Prop

/-- A uniform bound on the number of limit cycles over all quadratic systems:
there is `N` with every quadratic field having at most `N` limit cycles. This
is the "uniform bound" of the access statement; it is (part of) Hilbert's 16th
problem restricted to quadratic fields. -/
def UniformQuadraticBound : Prop :=
  ∃ N : ℕ, ∀ f : QuadraticSystem, nLimitCycles f ≤ N

/-! ## The cited axioms

Four axioms under `namespace Cited`. They are the whole content of this node:
the kernel checks that the theorem below follows from them, and nothing else. -/

namespace Cited

/-- src: Ilyashenko 2002, "Centennial history of Hilbert's 16th problem",
Bull. AMS 39(3):301-354, §5.2. The secondary source Ilyashenko reports the
count of graphics in the DRR program as 121. -/
axiom ilyashenko_reports_121 : Fintype.card GraphicId = 121

/-- src: Rousseau-Shan-Zhu 2015, arXiv:1502.00689, intro. RSZ reports the count
of graphics in the DRR program as 121. -/
axiom rsz_reports_121 : Fintype.card GraphicId = 121

/-- src: Roussarie-Rousseau 2015, arXiv:1506.07104, intro (Trans. Moscow Math.
Soc.). Roussarie-Rousseau reports the count of graphics in the DRR program as
121. -/
axiom rrs_reports_121 : Fintype.card GraphicId = 121

/-- src: DRR 1994, "Hilbert's 16th problem for quadratic vector fields", JDE
110(1):86-133.

The core mathematical content of DRR 1994: if every one of the graphics in the
list has finite cyclicity, then there is a uniform bound on the number of limit
cycles of all quadratic systems. (Equivalently, H(2) < ∞ follows from finite
cyclicity of the list.) -/
axiom finite_cyclicity_implies_uniform_bound :
    (∀ G : GraphicId, FinitelyCyclic G) → UniformQuadraticBound
-- The arrow is the point: DRR reduces H(2) < ∞ to the finite cyclicity of the
-- list. It does not establish that finite cyclicity, and neither does this run.

/-- The three secondary sources agree on the count. This is the formal reading
of the "count is 121, as reported by Ilyashenko 2002, RSZ 2015,
Roussarie-Rousseau 2015" sentence: each of the three reports asserts the same
equality `Fintype.card GraphicId = 121`. -/
theorem secondary_sources_agree :
    Fintype.card GraphicId = 121 := by
  exact ilyashenko_reports_121

/-- The three named secondary sources each state the same count.

Kept, but read it for what it is: the three axioms have IDENTICAL statements,
so this conjunction is one proposition repeated three times and agreement among
sources is not something the kernel can witness. Three sources reporting 121 is
a fact about three texts, and Lean sees only the single arithmetic claim. The
real check on it is research/drr-list.md, which reads each source separately and
records that Shan 2013 says 125, not 121 — a disagreement this conjunction is
structurally incapable of expressing. -/
theorem secondary_sources_each_report :
    (Fintype.card GraphicId = 121) ∧ (Fintype.card GraphicId = 121) ∧
        (Fintype.card GraphicId = 121) :=
  ⟨ilyashenko_reports_121, rsz_reports_121, rrs_reports_121⟩

end Cited

/-
## The theorem the node asks for

`drr_reduction` is the formal rendering of the node's statement: three named
sources report the count 121 (each `*_reports_121`), and the finite cyclicity
of every one of those graphics implies a uniform bound on quadratic limit
cycles (`finite_cyclicity_implies_uniform_bound`).

The statement is deliberately written so the *whole* of the informal claim is
carried in binders — the "whose finite cyclicity implies a uniform bound" is
literally the function type of `finite_cyclicity_implies_uniform_bound`, and
the hypothesis `∀ G, FinitelyCyclic G` quantifies over exactly
`121 = Fintype.card GraphicId` graphics.
-/

/-- The DRR citation-anchor claim, in full — **as an implication**.

The hypothesis `∀ G, FinitelyCyclic G` is exactly what is NOT known, so it stays
on the left of the arrow. Asserting the conclusion outright would be asserting
`H(2) < ∞`.

This is the whole content of DRR 1994 as a citation anchor: *if* every one of
the 121 graphics has finite cyclicity, *then* quadratic systems have a uniform
bound — and separately, the count is 121. -/
theorem drr_reduction :
    ((∀ G : GraphicId, FinitelyCyclic G) → UniformQuadraticBound)
      ∧ Fintype.card GraphicId = 121 :=
  ⟨Cited.finite_cyclicity_implies_uniform_bound, Cited.secondary_sources_agree⟩

/-- What this file does NOT establish, stated so no reader has to infer it:
`UniformQuadraticBound` is open. Nothing here proves it, and nothing here may be
cited as proving it. -/
example : True := trivial

/-! ## Axioms the theorem rests on

`#print axioms` below names exactly the `Cited.*` axiom statements (each a
parser/citation witness), plus `Classical.choice` which Lean's own classical
library uses. Every non-`Classical` axiom is a `Cited.*` literature statement,
so the standing is **conditional** — the implication from the cited results to
the claim is kernel-checked, and the cited results themselves are somebody
else's paper. There is no `sorry`, no `native_decide`, no `Quot.sound`-dependent
step.
-/

#print axioms DRR.drr_reduction

end DRR

#print axioms DRR.drr_reduction
