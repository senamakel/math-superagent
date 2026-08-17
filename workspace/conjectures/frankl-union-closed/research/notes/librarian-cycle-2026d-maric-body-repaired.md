# Librarian cycle — Maric-ZV FC-families body repaired; provenance-audit conclusion corrected

## What was found

The library's copy of Marić–Živković–Vučković, "Formalizing Frankl's
Conjecture: FC-families" was the **wrong paper**: it held arXiv:1209.5628
(G. Oberdieck, "A Serre derivative for even weight Jacobi forms", math.NT) —
a modular-forms paper with nothing to do with FC-families — downloaded under a
mistyped arXiv ID. The file carried a DEFECTIVE banner, but this cycle
verified the genuine paper exists at **arXiv:1207.3604** and put its full body
on disk under the correct name.

## What was done

1. Downloaded the genuine full body from the ar5iv rendering of arXiv:1207.3604
   into `research/sources/maric-zivkovic-vuckovic-fc-families-2012.full.md`
   (71 KB, real FC-families content, URL embedded line 1). The Oberdieck body
   is gone.
2. Replaced the stale digest with a real summary
   (`research/summaries/maric-zivkovic-vuckovic-fc-families-2012.md`) carrying
   the primary-source claim block `maric-4-3subsets-7set-fc`: **all families
   containing four 3-element sets whose union is contained in a 7-element set
   are FC-families** (Theorem 5.1(5) and Lemma 9, proved by an Isabelle/HOL-
   verified `ssn` computation; formalisation ~6500 lines, check ~28 min).
3. Indexed both repaired files (`index_document`); the claim is filed and
   returned by `search_claims` (status: proved, anchored to the primary body).
4. Corrected the stale references to the wrong ID:
   - `research/librarian-library-report.md` table row now reads
     `Marić–Živković–Vučković | 1207.3604 | 71,323 / FC-families (repaired...)`;
   - `research/ROOT.md` source-library index now lists `[arXiv:1207.3604]`.
5. Amended the provenance-audit conclusion
   (`research/notes/librarian-provenance-audit-2024-2026.md`): its claim that
   "no source is an unrelated paper filed under a wanted name" was **false** —
   this file was exactly that case, and the audit's identifier-resolution check
   had missed it (an identifier can resolve to the *wrong paper*). Recorded the
   lesson: verify a downloaded body's first-page content against the requested
   title, not only that a URL resolves.

## How the audit was checked

- Confirmed the body's first page is the genuine paper (abstract, authors,
  affiliation, Theorem 5.1 and Lemma 9 located in the primary text).
- Confirmed via `read_sources` on https://arxiv.org/abs/1207.3604 that the ID
  is the correct one ("Formalizing Frankl's Conjecture: FC-families", Marić,
  Živković, Vučković, 2012).
- Confirmed the two other known mislabeled bodies (Vaughan math/0208012 →
  algebroids; Eccles 1210.2044 → Clifford analysis) are properly flagged
  DEFECTIVE with their genuine content carried by genuine bodies on disk
  (Morris/Pulaj/survey; arXiv:1311.2298 bodies).

## Impact

- **No load-bearing claim was corrupted**: the run's FC-machinery claims anchor
  to Vučković–Živković 2017 and Pulaj 2017 (genuine full bodies), and the
  4-3-subsets-of-7-set FC fact was survey-sourced before; it is now primary-
  sourced.
- The three-set question (which 3-set configurations force UC) now has a
  primary-source data point on disk: three 3-sets in a 5-universe, four 3-sets
  in a 6- or 7-universe are all FC (Marić Thm 5.1).
- The open request `exact-current-published-c8b8` is answered by eight claim
  blocks (Yu 0.38234 published; AHS EJC 2024; Cambie/Liu preprints); no re-
  fetch needed.

## State

Library remains complete per the ROOT.md phase-1 bar; gathering stays closed.
No new download beyond the one repaired file.