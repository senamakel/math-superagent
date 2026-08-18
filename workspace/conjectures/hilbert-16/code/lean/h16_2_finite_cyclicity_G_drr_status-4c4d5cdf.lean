/-
h16_2_finite_cyclicity_G_drr_status-4c4d5cdf.lean
----------------------------------
Node `G-drr-status` from research/backward/h16-2-finite-cyclicity.md.

Informal statement to type and prove:

  Which of the 121 DRR graphics have finite cyclicity UNPROVED today, and the
  paper that closed each of the recently closed ones. There exists at least
  one graphic Λ₀ recorded open in the current literature (this is what picks
  the attack target).

This node is the target-selection lemma of the H(2) < ∞ skeleton. The clause
this pass is asked to prove is the second in full: *there exists at least one
graphic recorded open in the current literature*. That is the clause that fixes
the attack target, and it is the one the kernel can actually prove from the
cited hypotheses. Everything else — the full inventory of which ids are open
and which paper closed each recently-closed row — is a fact about the held
sources, not something this run can derive, so it is packaged as `Cited.*`
axioms.

How each clause of the informal statement is carried:

  * "the 121 DRR graphics" — the index type `GraphicId = Fin 121` (in the
    `GDRRStatus` namespace below). That the count is exactly 121 is a cited
    axiom (`Cited.count_is_121`: DRR 1994 / Ilyashenko 2002 / RSZ 2015 /
    RR 2015; the Shan-2013 "125" discrepancy is a separate node).
  * "have finite cyclicity UNPROVED today" — `Cited.closed G` := "finite
    cyclicity of the graphic G is PROVED in the held literature". A fact about
    sources, carried opaquely. `¬ Cited.closed G` = the graphic's finite
    cyclicity is not proved = it is open in the ledger.
  * "the paper that closed each of the recently closed ones" — recorded in the
    docstrings of the Cited axioms and in the research thread (drr-status.md),
    not as a decision procedure. Lean has no honest type for "the paper that
    closed this row", so the ledger of closures lives in the prose and the claim
    graph, not in a binder.
  * "There exists at least one graphic Λ₀ recorded open" — this IS the provable
    content. From the two cited facts
      - some graphic has NO partial result at all (`Cited.h14_no_partial_result`:
        RR 2015 name it (H³₁₄), the one graphic through a triple point at
        infinity), and
      - a fully closed graphic is in particular boundary-closed
        (`Cited.closed_implies_boundary`),
    the theorem `exists_open_graphic` follows: take the no-partial-result
    graphic; it is not boundary-closed, hence (contrapositive of the second) not
    closed, so it is an open graphic. This implication is PROVED by the kernel
    below — it is the shape of the node's second clause and the reason an attack
    target exists to be chosen.

There is no `sorry`, no `native_decide`, no `Quot.sound`-dependent step. The
derived theorems rest only on `Cited.*` axioms (and `Classical.choice`), so
their standing is `conditional`, never `formalised` — the kernel checks the
implication and nothing about the cited hypotheses.
-/

import Mathlib.Data.Fin.Basic
import Mathlib.Data.Set.Card

noncomputable section

namespace GDRRStatus

/-- A graphic: a limit periodic set of the compactified quadratic family, up to
the equivalence that makes DRR's list finite. The index type has 121 elements;
that the count is exactly 121 is the cited axiom `Cited.count_is_121`. -/
abbrev GraphicId : Type := Fin 121

end GDRRStatus

/-!
## The cited literature — one top-level `Cited` namespace, one axiom per fact
-/

namespace Cited

/-- src: the primary/secondary sources of the DRR program (RSZ 2015, RR 2015,
Huzak 2018, Dumortier–Rousseau 2009, and the individual closure papers named in
research/drr-list.md). `closed G` : "finite cyclicity of the graphic G is PROVED
in the held literature". A fact about sources, carried opaquely — distinct from
the mathematical property that G's cyclicity is finite, which could hold whether
or not a source has established it. `¬ closed G` means G is open in the ledger
(its finite cyclicity is not proved). -/
axiom closed : GDRRStatus.GraphicId → Prop

/-- src: Roussarie–Rousseau 2015, Trans. Moscow Math. Soc., Thm 1.1.
`boundaryClosed G` : "the boundary limit periodic set obtained from the blow-up
of the graphic G has PROVED finite cyclicity, but the full graphic is left
open". This is RR 2015 Thm 1.1's precise form of a PARTIAL closure — strictly
weaker than `closed`. -/
axiom boundaryClosed : GDRRStatus.GraphicId → Prop

/-- src: DRR 1994 JDE 110:86-133; Ilyashenko 2002 Bull. AMS §5.2; RSZ 2015;
RR 2015. The count of graphics in the DRR program is 121. (Shan-2013 "125" is a
separate discrepancy node; not restated here.) -/
axiom count_is_121 : Fintype.card GDRRStatus.GraphicId = 121

/-- src: Roussarie–Rousseau 2015, Trans. Moscow Math. Soc., intro (primary text:
"We have a partial result for every graphic, but one (namely (H³₁₄)), through a
triple point at infinity"). Some graphic — the held sources name it (H³₁₄), the
only graphic through a triple point at infinity — has NO partial result at all:
it is not even boundary-closed. This is the strongest form of "recorded open in
the current literature": an open graphic with no partial closure of any kind. -/
axiom h14_no_partial_result :
    ∃ G : GDRRStatus.GraphicId, ¬ boundaryClosed G

/-- src: Roussarie–Rousseau 2015, Thm 1.1 / the blow-up framework. Finite
cyclicity of the full graphic entails finite cyclicity of its boundary limit
periodic set from the same blow-up: `closed G → boundaryClosed G`. This is what
lets a no-partial-result row force program-incompleteness. -/
axiom closed_implies_boundary :
    ∀ G : GDRRStatus.GraphicId, closed G → boundaryClosed G

/-- src: Rousseau–Shan–Zhu 2015, arXiv:1502.00689, intro. Proving (I¹₁₂),
(I¹₁₃) brought the number of graphics with PROVED finite cyclicity to 88 of
121. Carried as: some set of at least 88 graphics is closed. -/
axiom rsz_closed_at_least_88 :
    ∃ s : Set GDRRStatus.GraphicId,
      s.ncard ≥ 88 ∧ ∀ G : GDRRStatus.GraphicId, G ∈ s → closed G

/-- src: Roussarie–Rousseau 2015, Thm 1.2. RR 2015 fully closes (I¹₁₄), so at
least 89 of the 121 have proved finite cyclicity. -/
axiom after_rr_closed_at_least_89 :
    ∃ s : Set GDRRStatus.GraphicId,
      s.ncard ≥ 89 ∧ ∀ G : GDRRStatus.GraphicId, G ∈ s → closed G

/-- src: Roussarie–Rousseau 2015, Thm 1.1. For (I₆b¹), (H₁₃³), (DI₂b) only the
BOUNDARY limit periodic set from the blow-up is closed; the full graphics are
explicitly left open. Carried as: three distinct graphics, each boundary-closed
and not closed. -/
axiom three_rows_partial :
    ∃ G1 G2 G3 : GDRRStatus.GraphicId,
      G1 ≠ G2 ∧ G1 ≠ G3 ∧ G2 ≠ G3 ∧
      boundaryClosed G1 ∧ boundaryClosed G2 ∧ boundaryClosed G3 ∧
      ¬ closed G1 ∧ ¬ closed G2 ∧ ¬ closed G3

/-- src: Shan 2013, PhD thesis, York Univ., Table 1.1 / §1 (reported; needs
primary confirmation of each id). The 11 degenerate graphics other than DF1a,
DF2a are open. Carried as: some set of at least 11 distinct graphics, none
closed. -/
axiom eleven_degenerate_open :
    ∃ s : Set GDRRStatus.GraphicId,
      s.ncard ≥ 11 ∧ ∀ G : GDRRStatus.GraphicId, G ∈ s → ¬ closed G

end Cited

/-! ## The theorems the node asks for -/

namespace GDRRStatus

/-- **The target-selection lemma: there exists at least one graphic Λ₀ recorded
open in the current literature.**

This is the node's second clause and the reason an attack target exists. It is
PROVED from the two cited facts.

Proof: `Cited.h14_no_partial_result` supplies some G with `¬ boundaryClosed G`.
Suppose `closed G`. Then `Cited.closed_implies_boundary G` gives
`boundaryClosed G`, contradicting `¬ boundaryClosed G`. Hence `¬ closed G`. So G
is an open graphic; take Λ₀ := G. -/
theorem exists_open_graphic : ∃ Λ₀ : GraphicId, ¬ Cited.closed Λ₀ := by
  rcases Cited.h14_no_partial_result with ⟨G, hG⟩
  refine ⟨G, ?_⟩
  intro hclosed
  exact hG (Cited.closed_implies_boundary G hclosed)

/-- **The inventory clause of the node**, packaged exactly as the sibling node
`h16-drr-open-rows`: the held literature establishes ≥88 closed at RSZ 2015,
≥89 after RR 2015's full closure of (I¹₁₄), the three boundary-only rows
(I₆b¹),(H₁₃³),(DI₂b), and ≥11 degenerate graphics open. Every conjunct is a
`Cited.*` axiom — this theorem packages the literature and the kernel checks the
packaging; the standing is `conditional`. The exact full list of open ids is NOT
established by any held source (a lower bound on openness, not an exact count)
— stated as prose, since Lean has no honest type for "no held source establishes
this". -/
theorem drr_status_inventory :
    (∃ s : Set GraphicId, s.ncard ≥ 88 ∧ ∀ G : GraphicId, G ∈ s → Cited.closed G) ∧
    (∃ s : Set GraphicId, s.ncard ≥ 89 ∧ ∀ G : GraphicId, G ∈ s → Cited.closed G) ∧
    (∃ G1 G2 G3 : GraphicId,
      G1 ≠ G2 ∧ G1 ≠ G3 ∧ G2 ≠ G3 ∧
      Cited.boundaryClosed G1 ∧ Cited.boundaryClosed G2 ∧ Cited.boundaryClosed G3 ∧
      ¬ Cited.closed G1 ∧ ¬ Cited.closed G2 ∧ ¬ Cited.closed G3) ∧
    (∃ s : Set GraphicId, s.ncard ≥ 11 ∧ ∀ G : GraphicId, G ∈ s → ¬ Cited.closed G) :=
  ⟨Cited.rsz_closed_at_least_88, Cited.after_rr_closed_at_least_89,
   Cited.three_rows_partial, Cited.eleven_degenerate_open⟩

/-- **The thumbnail of the whole node**: the count is 121, the held literature
closes at least 89 of them (88 at RSZ + (I¹₁₄) at RR 2015), and yet there is at
least one graphic recorded open — Λ₀, the attack target. The first two conjuncts
are `Cited.*`; the last is `exists_open_graphic`, proved above. -/
theorem drr_status_thumbnail :
    Fintype.card GraphicId = 121 ∧
    (∃ s : Set GraphicId, s.ncard ≥ 89 ∧ ∀ G : GraphicId, G ∈ s → Cited.closed G) ∧
    (∃ Λ₀ : GraphicId, ¬ Cited.closed Λ₀) :=
  ⟨Cited.count_is_121, Cited.after_rr_closed_at_least_89, exists_open_graphic⟩

/-! ## What this file does NOT establish

  * The exact full list of open graphic ids and the precise post-2015 open
    count. The held sources give a lower bound on openness and name particular
    rows; a complete 121-row ledger is NOT producible because the DRR 1994 raw
    catalogue is not held (see research/drr-list.md and thread drr-status.md).
  * That the open graphic Λ₀ is specifically (H³₁₄). The existence is proved;
    the identification of Λ₀ as (H³₁₄) is the content of the cited source
    (RR 2015 intro), so it cannot be loaded onto a bare `Fin 121` index that
    does not encode DRR names. It is recorded in the docstring of
    `Cited.h14_no_partial_result` and in the claim graph.
  * The paper that closed each recently-closed row (ledger in prose, not a
    binder).
-/

/-! ## Axioms these theorems rest on

`exists_open_graphic` rests on `Cited.h14_no_partial_result` and
`Cited.closed_implies_boundary` (both `Cited.*`, so `conditional`) plus
`Classical.choice` from Mathlib's classical library (the ∃-elimination). It is a
genuine kernel-checked implication from those two axioms — the node's central
clause is derived, not merely packaged.

`drr_status_inventory` and `drr_status_thumbnail` rest on the named `Cited.*`
axioms and nothing else. Every non-`Classical` axiom is a `Cited.*` literature
statement, giving standing `conditional`. There is no `sorry`, no
`native_decide`, no `Quot.sound`-dependent step.
-/

#print axioms exists_open_graphic
#print axioms drr_status_inventory
#print axioms drr_status_thumbnail

end GDRRStatus

#check GDRRStatus.exists_open_graphic
