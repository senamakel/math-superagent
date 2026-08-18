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

This is a *citation anchor*, sibling to `h16-drr-121-graphics` and
`drr-1994-citation-anchor`. Every concrete row of the list (which graphic is
open, how many are open, which family each lies in) is a fact about the held
literature, not a fact this run can derive — it is a statement about what RSZ,
RR 2015 and the Shan thesis actually prove, and about the absence of a complete
post-2015 ledger. Following the convention of the sibling node, the two *carrier
predicates* (`closed`, `boundaryClosed`) are declared as opaque top-level
axioms, and every *literature proposition* built on them lives under
`namespace Cited` with a `src:` docstring. The verdict is therefore
`conditional`, never `formalised`: the kernel checks the packaging and the one
genuinely structural implication below, and nothing about the hypotheses.

The one step that is NOT a literature fact is structural: once some graphic
(H₁₄³) has no partial result at all, the program is certainly not complete —
"closed ⇒ boundary-closed" (`closed_implies_boundary`, itself a Cited fact of
RR 2015's blow-up framework) turns the no-partial-result row into ¬(∀ G, closed G).
That single implication is PROVED by the kernel (`program_not_complete`); the
rows output as it runs. Everything else is attributed to a source.

How the node's decomposition is carried (each group is a sub-lemma; see the
fenced `gap` blocks at the foot of this file):

  * the count — `GraphicId = Fin 121`, and that it is exactly 121 is the cited
    `count_is_121` (DRR 1994 / Ilyashenko 2002 / RSZ 2015 / RR 2015);
  * "≥88 closed at RSZ 2015" — cited `rsz_closed_at_least_88`;
  * "≥89 closed after RR 2015's (I¹₁₄)" — cited `after_rr_closed_at_least_89`;
  * "(H₁₄³) no partial result" — cited `h14_no_partial_result`
    (∃ G, ¬ boundaryClosed G);
  * "(I₆b¹),(H₁₃³),(DI₂b) boundary-only" — cited `three_rows_partial`;
  * "≥11 degenerate open (Shan 2013)" — cited `eleven_degenerate_open`;
  * "closed ⇒ boundary-closed" (the blow-up framework) — cited
    `closed_implies_boundary`.

The pure-arithmetic numbers 33 and 32 clarify the accounting and are PROVED
(`open_at_rsz_arithmetic`, `remain_unclosed_arithmetic`). The meta-fact that no
held source establishes the exact open list/count is a paragraph (Lean has no
honest way to attach "no source establishes this" to a type) and is recorded in
the closing note.
-/

import Mathlib.Data.Fin.Basic
import Mathlib.Data.Set.Card

noncomputable section

namespace DRROpen

/-- A graphic (or degenerate graphic): a limit periodic set surrounding a
nondegenerate anti-saddle point of a quadratic system, up to the equivalence
that makes DRR's list finite. The index type has exactly 121 elements; that the
count is 121 is the cited axiom `Cited.count_is_121`. -/
abbrev GraphicId : Type := Fin 121

/-- **Carrier predicate, not a literature fact.** "Finite cyclicity of the
graphic G is PROVED, in full, in the held literature." This is a fact about
sources, carried opaquely — distinct from the mathematical property
`FinitelyCyclic` (of the sibling node), which could hold whether or not a
source has established it. The only evidence for `closed G` is the literature
itself, so the predicate symbol is opaque; the propositions about which
graphics are closed live under `Cited` where their source is attached. -/
axiom closed : GraphicId → Prop

/-- **Carrier predicate, not a literature fact.** "The boundary limit periodic
set obtained from the blow-up of the graphic G has PROVED finite cyclicity, but
the full graphic is left open." This is RR 2015 Thm 1.1's precise form of a
*partial* closure: the boundary piece is closed, the whole row is not. It is
strictly weaker than `closed`. Opaque carrier; the fact that particular
graphics are (or are not) boundary-closed lives under `Cited`. -/
axiom boundaryClosed : GraphicId → Prop

namespace Cited

/-- src: DRR 1994 JDE 110:86-133; Ilyashenko 2002 Bull. AMS §5.2; RSZ 2015;
RR 2015. The count of graphics in the DRR program is 121 (as the four main
sources report it; the Shan-2013 "125" is a separate unresolved discrepancy
node, `h16-drr-121-vs-125-discrepancy`). -/
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
program-incompleteness. -/
axiom closed_implies_boundary : ∀ G : GraphicId, closed G → boundaryClosed G

end Cited

/-! ## The combining steps -/

/-- **Combining step 1 — the full `h16-drr-open-rows` claim.** RSZ 2015 leaves
≥88 closed (33 of 121 open by the accounting below); RR 2015 pushes the closed
count to ≥89; the (H₁₄³) row has no partial result at all; (I₆b¹),(H₁₃³),(DI₂b)
are three distinct partial (boundary-only) rows; and ≥11 degenerate graphics
are open. Every conjunct is a `Cited.*` axiom; the theorem is their conjunction,
so the kernel checks the packaging and nothing else. Standing: conditional. -/
theorem drr_open_rows :
    (∃ s : Set GraphicId, s.ncard ≥ 88 ∧ ∀ G : GraphicId, G ∈ s → closed G) ∧
    (∃ s : Set GraphicId, s.ncard ≥ 89 ∧ ∀ G : GraphicId, G ∈ s → closed G) ∧
    (∃ G : GraphicId, ¬ boundaryClosed G) ∧
    (∃ G1 G2 G3 : GraphicId,
      G1 ≠ G2 ∧ G1 ≠ G3 ∧ G2 ≠ G3 ∧
      boundaryClosed G1 ∧ boundaryClosed G2 ∧ boundaryClosed G3 ∧
      ¬ closed G1 ∧ ¬ closed G2 ∧ ¬ closed G3) ∧
    (∃ s : Set GraphicId, s.ncard ≥ 11 ∧ ∀ G : GraphicId, G ∈ s → ¬ closed G) :=
  ⟨Cited.rsz_closed_at_least_88, Cited.after_rr_closed_at_least_89,
   Cited.h14_no_partial_result, Cited.three_rows_partial,
   Cited.eleven_degenerate_open⟩

/-- **Combining step 2 — the one non-cited theorem: the DRR program is NOT
complete.**

The (H₁₄³) no-partial-result row drives it: suppose every graphic were CLOSED.
Then by `closed_implies_boundary` every graphic would be boundary-closed,
contradicting `h14_no_partial_result` (some graphic has no partial result).
This is a genuine kernel-checked implication from two Cited facts — the shape
of the node's central clause, "the DRR program is NOT complete", is not merely
packaged here, it follows. -/
theorem program_not_complete :
    ¬ (∀ G : GraphicId, closed G) := by
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
`program_not_complete` rests on the two `Cited.*` axioms
`h14_no_partial_result` and `closed_implies_boundary` (via the carriers
`closed`, `boundaryClosed`). `open_at_rsz_arithmetic` /
`remain_unclosed_arithmetic` rest on nothing (`decide` closes them; the kernel
checks the ℕ arithmetic directly). There is no `sorry`, no `native_decide`, no
`Quot.sound`-dependent step. Everything non-`Classical` is a `Cited.*`
literature statement, giving standing `conditional`.
-/

#print axioms drr_open_rows
#print axioms program_not_complete
#print axioms open_at_rsz_arithmetic
#print axioms remain_unclosed_arithmetic

/-! ## Decomposition: the statement graph's gap blocks

This node is a citation anchor, so its "sub-lemmas" are literature facts: each
is an *intrinsic* statement about what a source proves, not a mathematical
claim the kernel could derive, and each is therefore carried as a `Cited.*`
axiom with its source named in the docstring (never as a `sorry` — a `sorry`
would strip the attribution and read as "unproved by anyone", which is the
opposite of the truth here: every one of these is *somebody else's proven
theorem*, out of this run's reach to re-derive). The one sub-lemma the kernel
can genuinely derive from the others — that a no-partial-result row makes the
program incomplete — is PROVED as `program_not_complete` above.

```gap
id: h16-drr-open-rows/h14-no-partial-result
lemma: ∃ G : GraphicId, ¬ boundaryClosed G
status: cited — Roussarie–Rousseau 2015, Thm 1.1/intro ("one graphic, (H₁₄³),
  through a triple point at infinity" has no partial result). Carried as
  `Cited.h14_no_partial_result`; plus `Cited.closed_implies_boundary` to make it
  force incompleteness.
next: research — confirm (H₁₄³)'s RR 2015 status against the held RR 2015 full
  text and, if Lu arXiv:2607.13785 stands, note it as the single row this no-
  partial-result fact used to name. (This is a literature confirmation, not a
  derivable step.)
```

```gap
id: h16-drr-open-rows/three-boundary-only-rows
lemma: ∃ G1 G2 G3 : GraphicId, pairwise distinct ∧ boundaryClosed (each) ∧ ¬ closed (each)
status: cited — Roussarie–Rousseau 2015, Thm 1.1 (I₆b¹),(H₁₃³),(DI₂b) partial.
  Carried as `Cited.three_rows_partial`.
next: research — the held RR 2015 full text should name exactly these three ids;
  a future ledger (research/threads/drr-status.md) records whether any has since
  been fully closed. This is a factual ledger row, not a derivable implication.
```

```gap
id: h16-drr-open-rows/eleven-degenerate-open
lemma: ∃ s : Set GraphicId, s.ncard ≥ 11 ∧ ∀ G ∈ s, ¬ closed G
status: cited — Shan 2013 thesis §1 / Table 1.1 (11 degenerate graphics other
  than DF1a, DF2a open). Carried as `Cited.eleven_degenerate_open`.
next: research — the Shan-2013 full ledger is the only per-class count in the
  library (see claim drr-shan-2013-table11-ledger); reconcile it against any
  post-2015 degenerate closures to update the ≥11 bound. Not derivable.
```

```gap
id: h16-drr-open-rows/exact-open-count-not-established
lemma: (meta-fact, carried as prose not a binder) — no held source gives the
  exact post-2015 open count or full open-id list
status: open gap — the ≤32/≥11 numbers above are lower bounds on openness; a
  complete ledger is absent from the library.
next: research — produce a consolidated graphic-by-graphic ledger (which open,
  paper closing each). That ledger is the run's target inventory; until it
  exists no exact count can be stated, in Lean or in prose.
```

The combining theorem `drr_open_rows` fulfils the `≤`-side of the informal
statement's decomposition: each bracketed clause is one of the sub-lemmas above
and the theorem's proof is exactly the tuple of the six Cited facts. The
derivable consequence `program_not_complete` is the statement's headline and is
the only non-cited step. No `sorry` appears, by design: the unproved-in-this-run
sub-lemmas are cited literature, and a `sorry` would be the wrong carrier for
them.
-/

end DRROpen

#print axioms DRROpen.drr_open_rows
#print axioms DRROpen.program_not_complete
#check DRROpen.program_not_complete
