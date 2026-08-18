# Librarian cycle 2026-08-19 — PE1006 reference library audit

Scope: verify the canonical reference tier, close the open request gaps, repair
defective sources, and keep the ledger honest.

## What was found broken and repaired

1. **`research/sources/abelian-repetitions-sturmian.full.md` was a 25-byte Lean
   stub** (`import Mathlib\n#check 0`), not the paper "Abelian Repetitions in
   Sturmian Words" (arXiv:1209.6013) that its summary claimed. Re-downloaded
   from https://arxiv.org/abs/1209.6013 (8041 bytes, real arXiv record);
   summary rewritten. The `.bak` copy of the stub is harmless.
2. **MathWorld pages cited by three summaries were not in `research/sources/`:**
   `mathworld-morse-hedlund-theorem.full.md`, `mathworld-sturmian-sequence.full.md`,
   `mathworld-rabbit-sequence.full.md`. Content captured via read_sources and
   written as full texts (each with its source URL).
3. **`research/summaries/bin̄ner-reciprocity-fulltext.md` and
   `research/summaries/binner-reciprocity-floor-square-functions.md` were digest
   templates.** Full text read (630 lines); real summary written, including the
   verified example (2732, 8411, 1221) → Σr²=28850219593, Σiq=196956430,
   Σq²=63853169, and Theorem 3 (the Euclidean reciprocity the universal-Euclidean
   recursion shares).

## What was added (primary tier)

- `research/sources/bonardo-frid-shallit-valid-factorizations-fibonacci-prefixes-ar5iv.full.md`
  — Bonardo–Frid–Shallit, "The number of valid factorizations of Fibonacci
  prefixes", TCS; https://ar5iv.labs.arxiv.org/html/1806.09534. The frontier's
  top-ranked missing primary source (16 citations by the library's own sources);
  the standard reference for standard-word prefix decompositions of Fibonacci
  prefixes.
- `research/sources/masakova-pelantova-powers-factors-recurrence-sturmian-ar5iv.full.md`
  — Masáková–Pelantová, "Relation between powers of factors and recurrence
  function characterizing Sturmian words", https://ar5iv.labs.arxiv.org/html/0809.0603.
  The modern reference for the recurrence function R(n) of Sturmian words, behind
  the run's first-occurrence-window axis.
- Both indexed; summaries written; their citations added to the frontier.

## What could NOT be obtained (recorded, not papered over)

- **Morse–Hedlund 1938 "Symbolic dynamics"** (Bull. AMS 44, 815–866): the AMS
  DOI (https://doi.org/10.1090/s0002-9904-1938-06743-2) resolves to a journal
  landing page only. The file is now explicitly marked DOWNLOAD FAILED — do not
  cite it as the paper.
- **Morse–Hedlund 1940 "Symbolic dynamics II. Sturmian trajectories"** (Amer. J.
  Math. 62, 1–42): JSTOR DOI (https://doi.org/10.2307/2371441) returns a paywall
  "Client Challenge" stub; no source file was created.
- Equivalent free coverage is in the library: mathworld-morse-hedlund-theorem,
  coven-hedlund-sequences-minimal-block-growth-1973, lothaire-sturmian-words-C2,
  perrin-restivo-sturmian-lecture.

## Open request gaps

The four `request_research` rows (citable-statement-theorem-039a,
citable-name-treatment-0c91, citable-precise-statement-600d,
citable-precise-statement-d2e7) carry `answers:` closures on disk
(`research/summaries/requests-closed-recap.md`,
`research/summaries/claim-universal-euclidean-geometric-floor-sum.md`) but the
rendered requests ledger lags — known renderer gap, previously recorded.

## Discrepancy to hand to the next cycle

`research/summaries/scholar-digest-complete.md` claims "every source ... its
summary ... replaced. No Digest only templates remain." **Falsified by grep
(2026-08-19): 31 summaries in `research/summaries/` still carry the digest
template** (allouche-shallit-automatic-sequences-book, three-distance,
berstel-vuillon, bucci-*, cambridge-*, cassaigne-*, de-luca-*, formal-intercepts,
frid-sturmian-equivalent-definitions, glen-*, hegedus-nagy, hieronymi-*,
huang-wen, lattice-rectangles, li-wu-*, lothaire-*, and more). The full texts
exist; the bounded summaries were never written. This is a scholar backlog, not
a source defect — recorded here so nobody re-trusts the completion claim.

## Files touched this cycle

- wrote: research/sources/{mathworld-morse-hedlund-theorem, mathworld-sturmian-sequence, mathworld-rabbit-sequence}.full.md
- wrote: research/sources/morse-hedlund-symbolic-dynamics-1938-ams-abstract.full.md (DOWNLOAD FAILED marker)
- repaired: research/sources/abelian-repetitions-sturmian.full.md
- added: research/sources/bonardo-frid-shallit-valid-factorizations-fibonacci-prefixes-ar5iv.full.md
- added: research/sources/masakova-pelantova-powers-factors-recurrence-sturmian-ar5iv.full.md
- wrote summaries: abelian-repetitions-sturmian, morse-hedlund-1938-ams-abstract,
  bonardo-frid-shallit-valid-factorizations, masakova-pelantova-powers-factors,
  bin̄ner-reciprocity-fulltext, binner-reciprocity-floor-square-functions
- indexed all of the above
- memory: librarian-cycle-2026-08-19 (Cognee)
