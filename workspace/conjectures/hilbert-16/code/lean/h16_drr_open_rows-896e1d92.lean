/-
h16_drr_open_rows-896e1d92.lean
----------------------------------
Node `h16-drr-open-rows` from research/notes/claims.md.

Informal statement to type and prove:

  The DRR program is NOT complete: at least 33 of the 121 graphics were still
  open as of RSZ 2015 (88 closed), and the open rows lie overwhelmingly in the
  nilpotent and degenerate families. Named open / partially-open rows:
    (i)   (H₁₄³) — the one graphic through a triple point at infinity with no
          partial result in Roussarie–Rousseau 2015;
    (ii)  (I₆b¹), (H₁₃³), (DI₂b) — only their boundary limit periodic sets are
          closed (RR 2015 Thm 1.1); the full graphics are explicitly left open;
    (iii) the 11 degenerate graphics other than DF1a, DF2a (Shan 2013 thesis).
  The exact full list of open graphic ids and the precise post-2015 open count
  are NOT established by any held source. The open count is a lower bound on
  openness, not the exact number.

This is, like the sibling `h16-drr-121-graphics` and `drr-1994-citation-anchor`
nodes, a *citation anchor*. Every concrete row of the list (which graphic is
open, how many are open, which family each lies in) is a fact about the held
literature, not a fact this run can derive: it is a statement about what RSZ,
RR 2015 and the Shan thesis actually prove, and about the absence of a complete
post-2015 ledger. Those facts are therefore `axiom`s under `namespace Cited`,
and the top-level `drr_open_rows` theorem packages their conjunction. The one
step that is NOT a literature fact is structural: once some graphic (H₁₄³) has
no partial result at all, the program is certainly not complete — and that
single implication is PROVED by the kernel below (`program_not_complete`).
The verdict here is `conditional`, never `formalised`: the kernel checks the
packaging and the one implication, and nothing about the hypotheses.

How each clause of the informal statement is carried:

  * "121 graphics" — the index type `GraphicId = Fin 121`; the claim that the
    count is exactly 121 is a cited axiom (`count_is_121`), matching DRR 1994 /
    Ilyashenko 2002 / RSZ 2015 / RR 2015. (The Shan-2013-says-125 discrepancy is
    a separate node, `h16-drr-121-vs-125-discrepancy`; this file states the
    count as the four main sources give it.)
  * "at least 88 closed by RSZ 2015" — a set `s` of graphics, each CLOSED
    (finite cyclicity proved) in the held literature, with `s.ncard ≥ 88`
    (`rsz_closed_at_least_88`).
  * "after RR 2015's full closure of (I¹₁₄) on top of RSZ's 88" — a set with
    `s.ncard ≥ 89` of closed graphics (`after_rr_closed_at_least_89`). The
    numbers 33 (=121-88) and 32 (=121-89) that the claim's accounting leans on
    are the pure ℕ identities `open_at_rsz_arithmetic` and
    `remain_unclosed_arithmetic`, PROVED by `norm_num`.
  * "(H₁₄³) ... no partial result" — carried as `h14_no_partial_result`:
    some graphic is not even *boundary-closed* (`¬ boundaryClosed G`), i.e. it
    has no partial result at all. `boundaryClosed` is "the boundary limit
    periodic set from the blow-up has proved finite cyclicity" — a strictly
    weaker state than the full graphic being closed.
  * "only their boundary limit periodic sets are closed for (I₆b¹),(H₁₃³),
    (DI₂b); full graphics open" — three DISTINCT graphics each
    `boundaryClosed` and `¬ closed` (`three_rows_partial`).
  * "the 11 degenerate graphics other than DF1a, DF2a open (Shan 2013)" — a set
    of at least 11 distinct graphics, none closed (`eleven_degenerate_open`).
  * "the exact full list and precise post-2015 open count are NOT established
    by any held source" — a meta-fact about this run's library, not a
    mathematical hypothesis; carried in the header prose and the closing note,
    not as a binder (it is genuinely a paragraph, and Lean has no honest way to
    attach "no held source establishes this" to a type).

The derivable (kernel-checked) theorem: with the cited `closed_implies_boundary`
(see below) — a fully closed graphic is in particular boundary-closed, since
closing the full graphic closes its boundary set — the no-partial-result row
(H₁₄³) forces `¬ (∀ G, closed G)`. That is exactly "the DRR program is NOT
complete", and it is the one strictly-proved (non-cited) statement in this
file: its only non-`Classical` hypotheses are the two `Cited.*` axioms
`h14_no_partial_result` and `closed_implies_boundary`.
-/

import Mathlib.Data.Fin.Basic
import Mathlib.Data.Set.Card

noncomputable section

namespace DRROpen

/-- A graphic (or degenerate graphic): a limit periodic set surrounding a
nondegenerate anti-saddle point of a quadratic system, up to the equivalence
that makes DRR's list finite. The index type has exactly
`121 = Fintype.card GraphicId` elements; that the count is 121 is the cited
axiom `count_is_121`. -/
abbrev GraphicId : Type := Fin 121

namespace Cited

/-- src: the primary/secondary sources of the DRR program (RSZ 2015, RR 2015,
Huzak 2018, Dumortier–Rousseau 2009) that establish individual graphics. The
predicate `closed G`: "finite cyclicity of the graphic G is PROVED, in
full, in the held literature." This is a fact about sources, carried opaquely
(distinct from the mathematical property `FinitelyCyclic`, which could hold
whether or not a source has established it). The only evidence for `closed G`
is the literature itself, so the predicate symbol lives here under `Cited`. -/
axiom closed : GraphicId → Prop

/-- src: Roussarie–Rousseau 2015, Trans. Moscow Math. Soc., Thm 1.1. The
predicate `boundaryClosed G`: "the boundary limit periodic set obtained
from the blow-up of the graphic G has PROVED finite cyclicity, but the full
graphic is left open." This is RR 2015 Thm 1.1's precise form of a *partial*
closure: the boundary piece is closed, the whole row is not. It is strictly
weaker than `closed`. -/
axiom boundaryClosed : GraphicId → Prop

/-- src: DRR 1994 JDE 110:86-133; Ilyashenko 2002 Bull. AMS §5.2; RSZ 2015;
RR 2015. The count of graphics in the DRR program is 121 (as the four main
sources report it; the Shan-2013 "125" is a separate unresolved discrepancy
node). -/
axiom count_is_121 : Fintype.card GraphicId = 121

/-- src: Rousseau–Shan–Zhu 2015, arXiv:1502.00689, intro. Proving (I¹₁₂),
(I¹₁₃) brought the number of graphics with PROVED finite cyclicity to 88 of
121. Carried as: some set `s` of at least 88 graphics is closed in the held
literature. -/
axiom rsz_closed_at_least_88 :
    ∃ s : Set GraphicId, s.ncard ≥ 88 ∧ ∀ G : GraphicId, G ∈ s → closed G

/-- src: Roussarie–Rousseau 2015, Trans. Moscow Math. Soc., Thm 1.2. RR 2015
fully closes (I¹₁₄) on top of RSZ's 88, so at least 89 of the 121 graphics have
proved finite cyclicity. Carried as a set of at least 89 closed graphics. -/
axiom after_rr_closed_at_least_89 :
    ∃ s : Set GraphicId, s.ncard ≥ 89 ∧ ∀ G : GraphicId, G ∈ s → closed G

/-- src: Roussarie–Rousseau 2015, intro (primary text: "We have a partial result
for every graphic, but one (namely (H₁₄³)), through a triple point at
infinity"). (H₁₄³) is the one graphic through a triple point at infinity with
NO partial result at all. Carried as: some graphic is not even boundary-closed
(so a fortiori not closed). -/
axiom h14_no_partial_result :
    ∃ G : GraphicId, ¬ boundaryClosed G

/-- src: Roussarie–Rousseau 2015, Thm 1.1. For (I₆b¹), (H₁₃³), (DI₂b) only the
BOUNDARY limit periodic set from the blow-up is closed; the full graphics are
explicitly left open ("intend to address the problem in the next future").
Carried as: three distinct graphics, each boundary-closed and not closed. -/
axiom three_rows_partial :
    ∃ G1 G2 G3 : GraphicId,
      G1 ≠ G2 ∧ G1 ≠ G3 ∧ G2 ≠ G3 ∧
      boundaryClosed G1 ∧ boundaryClosed G2 ∧ boundaryClosed G3 ∧
      ¬ closed G1 ∧ ¬ closed G2 ∧ ¬ closed G3

/-- src: Shan 2013, PhD thesis, York Univ. (summary), Table 1.1 / §1: the 11
degenerate graphics other than DF1a, DF2a are open (DF1a, DF2a closed by
Dumortier–Rousseau 2009 and Huzak 2018 respectively). Carried as: some set of
at least 11 distinct graphics, none of them closed. -/
axiom eleven_degenerate_open :
    ∃ s : Set GraphicId, s.ncard ≥ 11 ∧ ∀ G : GraphicId, G ∈ s → ¬ closed G

/-- src: Roussarie–Rousseau 2015, Trans. Moscow Math. Soc., Thm 1.1 / the
blow-up framework. The structural content of a *partial* closure: finite
cyclicity of the full graphic entails finite cyclicity of its boundary limit
periodic set obtained from the same blow-up — `boundaryClosed` is exactly the
weakening of `closed` at which RR 2015 reports rows like (I₆b¹),(H₁₃³),(DI₂b)
as partly closed. This is what lets the no-partial-result row (H₁₄³) force
program-incompleteness below. -/
axiom closed_implies_boundary : ∀ G : GraphicId, closed G → boundaryClosed G

end Cited

/-! ## The theorem the node asks for -/

/-- The full `h16-drr-open-rows` claim: RSZ 2015 leaves ≥88 closed (so 33 of
121 open by the accounting below); RR 2015 pushes the closed count to ≥89; the
(H₁₄³) row has no partial result at all; (I₆b¹),(H₁₃³),(DI₂b) are three
distinct partial rows (boundary-only); and ≥11 degenerate graphics are open.
Every conjunct is a `Cited.*` axiom; the theorem is their conjunction, so the
kernel checks the packaging and nothing else. Standing: conditional. -/
theorem drr_open_rows :
    (∃ s : Set GraphicId, s.ncard ≥ 88 ∧ ∀ G : GraphicId, G ∈ s → Cited.closed G) ∧
    (∃ s : Set GraphicId, s.ncard ≥ 89 ∧ ∀ G : GraphicId, G ∈ s → Cited.closed G) ∧
    (∃ G : GraphicId, ¬ Cited.boundaryClosed G) ∧
    (∃ G1 G2 G3 : GraphicId,
      G1 ≠ G2 ∧ G1 ≠ G3 ∧ G2 ≠ G3 ∧
      Cited.boundaryClosed G1 ∧ Cited.boundaryClosed G2 ∧ Cited.boundaryClosed G3 ∧
      ¬ Cited.closed G1 ∧ ¬ Cited.closed G2 ∧ ¬ Cited.closed G3) ∧
    (∃ s : Set GraphicId, s.ncard ≥ 11 ∧ ∀ G : GraphicId, G ∈ s → ¬ Cited.closed G) :=
  ⟨Cited.rsz_closed_at_least_88, Cited.after_rr_closed_at_least_89,
   Cited.h14_no_partial_result, Cited.three_rows_partial,
   Cited.eleven_degenerate_open⟩

-- The theorem above references the Cited axioms; `closed`/`boundaryClosed`
-- are just `Cited.closed`/`Cited.boundaryClosed` under the namespace, so the
-- shorter names are definitional no-ops. (Kept for readability.)

/-- **The one non-cited theorem of this file: the DRR program is NOT complete.**

The (H₁₄³) no-partial-result row drives it: suppose every graphic were CLOSED.
Then by `closed_implies_boundary` every graphic would be boundary-closed,
contradicting `h14_no_partial_result` (some graphic has no partial result).
This is a genuine kernel-checked implication from the two axioms — the shape
of the node's central clause, "the DRR program is NOT complete", is not merely
packaged here, it follows. -/
theorem program_not_complete :
    ¬ (∀ G : GraphicId, Cited.closed G) := by
  rintro hall
  rcases Cited.h14_no_partial_result with ⟨G, hG⟩
  exact hG (Cited.closed_implies_boundary G (hall G))

/-- The claim's own accounting, stripped to the pure arithmetic it leans on:
at RSZ 2015, 88 closed of 121 leaves 33 open; after RR 2015's full closure of
(I¹₁₄) (89 closed), 32 of 121 are left not fully closed. These two ℕ
identities are PROVED — they are the "at least 33 / at least 32" numbers of the
informal claim, up to the caveat that an open/closed partition is only a lower
bound in the source, never an exact accounting. -/
theorem open_at_rsz_arithmetic : 121 - 88 = 33 := by decide

/-- See `open_at_rsz_arithmetic`: after RR 2015 closes (I¹₁₄), 121 - 89 = 32 of
the 121 are not fully closed (= the 33 at RSZ minus the one RR closes). -/
theorem remain_unclosed_arithmetic : 121 - 89 = 32 := by decide

/-- What this file does NOT establish, stated so no reader has to infer it: the
exact full list of open graphic ids and the precise post-2015 open count. The
held sources give a lower bound on openness and name particular rows; a
complete ledger is the live gap (research/threads/drr-status.md). Nothing here
asserts a full enumeration. -/
example : True := trivial

/-! ## Axioms these theorems rest on

`drr_open_rows` rests on the five `Cited.*` axioms and nothing else.
`program_not_complete` rests on `Cited.h14_no_partial_result` and
`Cited.closed_implies_boundary` (both named `Cited.*`, so `conditional`).
`open_at_rsz_arithmetic` /
`remain_unclosed_arithmetic` rest on nothing (`decide` closes them; the
kernel checks the ℕ arithmetic directly). Everything non-`Classical` is a
`Cited.*` literature statement, giving standing `conditional`. There is no
`sorry`, no `native_decide`, no `Quot.sound`-dependent step.
-/

#print axioms drr_open_rows
#print axioms program_not_complete
#print axioms open_at_rsz_arithmetic
#print axioms remain_unclosed_arithmetic

end DRROpen

#print axioms DRROpen.drr_open_rows
#print axioms DRROpen.program_not_complete
#check DRROpen.program_not_complete
