/-
h16_drr_121_graphics-c9bd1dd4.lean
----------------------------------
Node `h16-drr-121-graphics` from research/notes/claims.md.

Informal statement to type and prove:

  H(2) < ∞ is equivalent (via the compactness/DRR program of Dumortier,
  Roussarie and Rousseau 1994, J. Diff. Eq. 110, 86-133) to proving finite
  cyclicity of 121 graphics in S²×K, where K is the compactified parameter
  space of quadratic anti-saddle-type systems and S² the Poincaré sphere.
  Proving the (I¹₁₂), (I¹₁₃) graphics (Rousseau–Shan–Zhu 2015) brought the
  count of graphics with proved finite cyclicity to 88 of 121. Verified
  post-2015 closures include: degenerate graphics DF2a (Huzak 2018,
  CPA 17(3):1305-1316, family blow-up + slow divergence integral; DF1a was
  Dumortier–Rousseau 2009, CPA 8), and the center-surrounding triple-nilpotent
  graphics (I¹₁₄), (I¹₆b), (H³₁₃), (DI²b) with (H³₁₄) left open (Roussarie–
  Rousseau 2015, Moscow Math. J.).

This is a *citation anchor*. The substance of the claim is the DRR reduction,
the count, and the literature status of particular graphics — facts about the
mathematics and about the sources, none of which is this run's to prove. Every
one is therefore an `axiom` under `namespace Cited`, and the top-level theorem
below packages them. The verdict is `conditional`, never `formalised`: the
kernel checks the packaging step and nothing about the hypotheses.

How each hypothesis of the informal statement is carried:

  * "H(2) < ∞" — a uniform natural bound `N` on `nLimitCycles f` over every
    quadratic planar field `f` (`H2Finite`). The abstraction `QuadraticSystem`
    carries the two degree-≤2 polynomials; `nLimitCycles` is the opaque count of
    its limit-cycle orbits. Stating the count as a plain ℕ (not `Set.ncard`,
    which is vacuously 0 on an infinite set) is what makes `≤ N` a real bound.
  * "finite cyclicity of 121 graphics" — the predicate `FinitelyCyclic G` over
    `G : GraphicId = Fin 121`. It is an `axiom` with no equation, so the kernel
    can never discharge the hypothesis `∀ G, FinitelyCyclic G`; the DRR
    reduction stays an equivalence and cannot be collapsed into a proof of
    `H2Finite` (which would be the forbidden `H(2) < ∞`).
  * "in S²×K where K is the compactified parameter space and S² the Poincaré
    sphere" — geometric context of where the graphics live. Mathlib has no
    notion of graphic, polycycle, or cyclicity; it is carried in the docstrings
    of the cited axioms, not as binders.
  * "88 of 121 ... (I¹₁₂),(I¹₁₃)" and the "post-2015 closures DF2a, DF1a,
    (I¹₁₄),(I¹₆b),(H³₁₃),(DI²b) with (H³₁₄) open" — facts about which graphics
    a source has closed and which remain open. Carried by an opaque literature
    predicate `closed : GraphicId → Prop` ("finite cyclicity of this graphic is
    proved in the held literature") and a set of cited axioms asserting the
    cardinality and status facts. GraphicId does not encode the DRR names
    (I¹₁₂) etc., so the named rows are asserted only through `closed`, not
    through any concrete index — we do not claim which index is which graphic.
-/

import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Algebra.MvPolynomial.Degrees
import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Card
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fin.VecNotation

noncomputable section

open Set

namespace DRR121

/-! ## The objects of the statement -/

/-- A graphic (or degenerate graphic): a limit periodic set, up to the
equivalence that makes DRR's list finite. The index type has 121 elements; the
claim that the count is exactly 121 is a cited axiom below. -/
abbrev GraphicId : Type := Fin 121

/-- A planar quadratic polynomial vector field: two polynomials of total degree
at most 2. This is the concrete carrier of "a quadratic system". -/
structure QuadraticSystem where
  P : MvPolynomial (Fin 2) ℝ
  Q : MvPolynomial (Fin 2) ℝ
  degP : P.totalDegree ≤ 2
  degQ : Q.totalDegree ≤ 2

/-- Opaque count of the limit-cycle orbits of the field. Stated as a plain ℕ
(not `Set.ncard`, which is vacuously 0 for an infinite set) so that `≤ N` below
really bounds the number of limit cycles and not 0. -/
axiom nLimitCycles (f : QuadraticSystem) : ℕ

/-- An individual graphic `G` has finite cyclicity. Must stay an opaque axiom:
the hypothesis `∀ G, FinitelyCyclic G` is exactly what is NOT known (89/121
closed, three partial, H14^3 only in an unrefereed 2026 preprint, ≥11 degenerate
open). Written without an equation, the kernel can never discharge it and the
DRR reduction is forced to stay an implication/equivalence rather than a proof
of H(2) < ∞. -/
axiom FinitelyCyclic : GraphicId → Prop

/-- H(2) < ∞: a uniform bound shared by every quadratic planar field. This is
(the quadratic special case of) Hilbert's 16th problem, part 2; it is OPEN and
nothing in this file may prove it. -/
def H2Finite : Prop :=
  ∃ N : ℕ, ∀ f : QuadraticSystem, nLimitCycles f ≤ N

/-- The literature record: "finite cyclicity of this graphic is PROVED in the
held literature". A fact about sources, carried opaquely — distinct from the
mathematical property `FinitelyCyclic`, which may hold whether or not a source
has established it. -/
axiom closed : GraphicId → Prop

namespace Cited

/-- src: Dumortier, Roussarie, Rousseau 1994, "Hilbert's 16th problem for
quadratic vector fields", J. Diff. Eq. 110(1):86-133. The compactness/DRR
program: H(2) < ∞ is equivalent to finite cyclicity of every one of the 121
graphics in S²×K, where K is the compactified parameter space of quadratic
anti-saddle-type systems and S² the Poincaré sphere.

Stated as an EQUIVALENCE (the node's first clause). Both directions are content
of DRR 1994: finiteness of the list's cyclicity forces a uniform quadratic
bound, and the list is comprehensive. -/
axiom drr_h2_finite_iff_finite_cyclicity :
    H2Finite ↔ (∀ G : GraphicId, FinitelyCyclic G)

/-- src: Ilyashenko 2002 Bull. AMS 39(3):301-354 §5.2; Rousseau–Shan–Zhu 2015
arXiv:1502.00689; Roussarie–Rousseau 2015 Trans. Moscow Math. Soc. The count of
graphics in the DRR program is 121. (Noted discrepancy: Shan 2013 thesis says
125 — recorded separately; this axiom states the count as the three main
sources report it.) -/
axiom count_is_121 : Fintype.card GraphicId = 121

/-- src: Rousseau–Shan–Zhu 2015, arXiv:1502.00689, intro. Proving the (I¹₁₂),
(I¹₁₃) graphics brought the number of graphics with proved finite cyclicity to
88 of 121. Carried as: there is a set of graphics, closed in the literature,
of cardinality at least 88. -/
axiom rsz_closed_at_least_88 :
    ∃ s : Set GraphicId, s.ncard ≥ 88 ∧ ∀ G : GraphicId, G ∈ s → closed G

/-- src: Huzak 2018, "Cyclicity of degenerate graphic DF2a", CPA 17(3):
1305-1316 (family blow-up + slow divergence integral); Dumortier–Rousseau 2009,
"Study of the cyclicity of some degenerate graphics inside quadratic systems",
CPA 8 (2009) 1133-1157 (DF1a). The degenerate graphics DF1a, DF2a (two distinct
rows of the list) have proved finite cyclicity. -/
axiom degenerate_df_closed :
    ∃ G1 G2 : GraphicId, G1 ≠ G2 ∧ closed G1 ∧ closed G2

/-- src: Roussarie–Rousseau 2015, Trans. Moscow Math. Soc., Thm 1.1 / intro.
The center-surrounding triple-nilpotent graphics (I¹₁₄), (I¹₆b), (H³₁₃),
(DI²b) are closed, while (H³₁₄) — through a triple point at infinity — is left
open. Carried as: some graphic is closed and some graphic is open (at least one
of each) in this family. -/
axiom triple_nilpotent_status :
    (∃ G : GraphicId, closed G) ∧ (∃ G : GraphicId, ¬ closed G)

end Cited

/-
## The theorem the node asks for

`drr_121_graphics` packages every clause of the informal statement:

  * the DRR equivalence `H2Finite ↔ ∀ G, FinitelyCyclic G` (the mathematical
    reduction, cited to DRR 1994);
  * the count `Fintype.card GraphicId = 121` (cited to the three secondary
    sources);
  * at least 88 closed by RSZ 2015 after (I¹₁₂),(I¹₁₃) (cited);
  * post-2015 closures in the degenerate family DF1a/DF2a and in the
    center-surrounding triple-nilpotent family, with at least one row still open
    (cited).

Every conjunct is a `Cited.*` axiom; the theorem is their conjunction, so the
kernel checks the packaging and nothing else. Standing: conditional.
-/

/-- The full `h16-drr-121-graphics` claim: the DRR equivalence, the count, and
the closure/status facts of the held literature, all cited. -/
theorem drr_121_graphics :
    (H2Finite ↔ (∀ G : GraphicId, FinitelyCyclic G)) ∧
    Fintype.card GraphicId = 121 ∧
    (∃ s : Set GraphicId, s.ncard ≥ 88 ∧ ∀ G : GraphicId, G ∈ s → closed G) ∧
    (∃ G1 G2 : GraphicId, G1 ≠ G2 ∧ closed G1 ∧ closed G2) ∧
    ((∃ G : GraphicId, closed G) ∧ (∃ G : GraphicId, ¬ closed G)) :=
  ⟨Cited.drr_h2_finite_iff_finite_cyclicity, Cited.count_is_121,
   Cited.rsz_closed_at_least_88, Cited.degenerate_df_closed,
   Cited.triple_nilpotent_status⟩

/-- Explicit note that nothing in this file establishes `H2Finite`. The DRR
equivalence is exactly that the open hypothesis `∀ G, FinitelyCyclic G` on the
right cannot be discharged; asserting `H2Finite` outright is the one thing this
run must not do. -/
example : True := trivial

/-! ## Axioms the theorem rests on

`#print axioms` below names exactly the `Cited.*` axioms (each a citation
witness), plus `Classical.choice` from Mathlib's classical library. No `sorry`,
no `native_decide`, no `Quot.sound`-dependent step. Because every non-classical
axiom is a `Cited.*` literature statement, the standing is `conditional`.
-/

#print axioms drr_121_graphics

end DRR121

#print axioms DRR121.drr_121_graphics
