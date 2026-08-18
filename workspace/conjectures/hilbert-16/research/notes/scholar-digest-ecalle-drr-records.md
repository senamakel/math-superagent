# Scholar pass — digest of the latest library records (librarian cycle)

Cognee was down this cycle (memory server unresponsive), so durable findings
are persisted to workspace files per the standing LIBRARY-STATUS convention.

## What this pass did

Replaced six placeholder digests for genuinely-new records with real notes
carrying claim blocks and wikilinks, and converted four HTML-renderings-plus-one
PDF duplicate summaries into pointers to their already-digested siblings.

## New real notes (each with a claim block → CLAIMS.md)

1. **Écalle 1990** (`research/summaries/ecalle-1990-finitude-accelerosommation.md`,
   claim `ecalle-1990-accelerosommation-record`): record + reference list only;
   body paywalled. **This is the first Écalle-side primary record in the
   library.** Key finding: the held bibliography identifies the
   **Écalle–Martinet–Moussu–Ramis CRAS 304 (1987) "Non-accumulation des
   cycles-limites" I/II (pp. 375-378 / 431-434) as the open-format target most
   likely to carry the Écalle-side proof concisely.** No theorem statement of
   the 1990 chapter is in the library — so the run still cannot state Écalle's
   finite-cyclicity hypotheses or answer problem.md test-1 for the Écalle side.

2. **Roussarie 1986** (`research/summaries/roussarie-1986-separatrix-loop-limit-cycles.md`,
   claim `roussarie-1986-separatrix-loop-record`): record + bibliography; the
   **founding derivation–division paper** of the DRR program. Reference list
   names its instruments: Cherkas successor function (1981),
   Andronov–Leontovich–Gordon–Maier (1971), Dulac 1923, Sternberg 1958,
   Ilyashenko 1984, **Khovanskii Bézout-for-Liouville-functions (IHES M/81/45,
   1981)** — the fewnomial zero bound the run's displacement-zero arguments
   trace to.

3. **Dumortier–El Morsalani–Rousseau 1996** (claim `drr-demr-1996-elementary-graphics-abstract`):
   abstract-level. Khovanskii method; compensation principle (points compensate
   ⇔ graphic surrounds a center); **some regular transition maps NOT tangent to
   the identity** — a caution for any displacement-composition argument.
   Author-list correction: it is El Morsalani, not Roussarie, as third author.

4. **DRR94 cyclicity 1/2** (claim `drr-drr94-cyclicity-1-2-abstract`): C^∞ general
   theorems — graphic of attracting hyperbolic saddles + attracting
   semi-hyperbolic points ⇒ cyclicity 1; one hyperbolic + one semi-hyperbolic
   of opposite character ⇒ cyclicity 2; 33 quadratic graphics ≤ 2 (5 generic).

5. **Christopher–Li–Torregrosa 2024 book TOC** (claim
   `clt-2024-book-weak-h16-n2-chapter`): Part II Ch.4 = "A Unified Proof of the
   Weak Hilbert's 16th Problem for n=2" (pp. 193-209). Book-form confirmation
   the weak (tangential) n=2 problem is settled; corrected my own first draft to
   note this is a theorem for all n (BNY), so it is a book-form n=2-in-particular
   treatment, not a new finiteness statement.

## Duplicates converted to pointers (carry nothing new)

`buzzi-gasull-santana-cyclicity-hyperbolic-polycycles-2024.html.md` →
`h16-hyperbolic-polycycle-cyclicity-lower-bound-bgs2024`;
`marin-villadelprat-dulac-coefficient-properties-2024-arxiv.html.md` →
`h16-mv-dulac-coefficient-formulas-2024`;
`dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.html.md` →
`h16-dukov-multiplicity-hyperbolic-polycycles-2023`;
`queiroz-arakaki-santana-persistent-hyperbolic-polycycles-2025.html.md` →
`h16-persistent-polycycle-cyclicity-qas2025`;
`mourtada-1991-cyclicite-finie-polycycles-hyperboliques-pdf.md` →
`h16-mourtada-1991-hyperbolic-finite-cyclicity-primary`. Each now points to
its fully-digested sibling.

## Anchors that do not resolve

Two claim blocks cite source files NOT on disk (record-page conversions were
never saved as `.full`): `research/sources/drr-dumortier-roussarie-rousseau-1994-hilbert-16-quadratic.full.md`
and `research/sources/roussarie-1994-elementary-graphics-cyclicity-1-2.full.md`.
I re-anchored the roussarie-1994 claim to its summary (the only held content).
The DRR 1994 claim `drr-1994-record-held-verbatim` still cites the non-existent
`.full`; its real held content is the two record summaries.

## Open gap (Écalle side) — request tool declined to queue

The request tool declined a request for the Écalle-side theorem statement
because the library "already carries 8 claims bearing on this" — but all 8 are
bibliographic records, none states Écalle's theorem hypotheses. The gap is real
and not answered by the held claims. Recorded here so a later pass can open it
precisely against the tool: the library needs the body of Écalle 1990 (LNM 1455)
or the EMMR 1987 CRAS note, to state (a) where analyticity enters the
accelero-summation proof, (b) whether it covers non-hyperbolic polycycles, and
(c) whether Yeung's Ilyashenko-side critique has an Écalle-side counterpart.

## Contradictions / inconsistencies noted

- The derived ledger lists `drr-rr-boundary-only-for-3-graphics` as
  contradicting `drr-88-then-closed-all-four` — a claim **not on disk** (dangling
  id). Harmless; noted for cleanup.
- `data-contamination-llibre-zhang` (the held "llibre-zhang-lienard-survey" is a
  power-grid paper) is a known library contamination, unchanged.

## Final state

The six genuinely-new sources are now real notes; the five duplicates are
pointers; every new claim block reaches `derived/CLAIMS.md`. Nothing load-bearing
is newly established by these records (they are provenance/bibliographic anchors
for the elementary and Écalle sides); the surviving open question from this pass
is the Écalle-side theorem statement, tracked above.
