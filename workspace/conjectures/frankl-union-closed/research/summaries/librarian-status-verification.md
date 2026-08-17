# Librarian status — source-completion verification

Cycle date: this run.

## Decision

Library phase is **finished** per operator directive (`stop-adding-sources`, done).
`research/ROOT.md` meets the phase-1 test: it states the minimal-counterexample
structure (|F| ≥ 51), the verification bound (|∪F| ≤ 12, |F| ≤ 50, |F| ≥ 2^(n−1)),
and at least three settled classes (lattice classes, graph formulation,
small/large families) with hypotheses, each tied to a primary source in
`research/sources/`. No further surveys are warranted.

## The one open request, re-verified

`exact-current-published-c8b8` asked for the current PUBLISHED record and whether
Cambie/Liu had since appeared in journals. Re-checked against the live web
(exa_search, 2025). **Unchanged**:

- Cambie arXiv:2212.12500 (c≈0.3823455) — still an arXiv preprint.
- Liu arXiv:2306.08824 (c≈0.38271, conditional on numerically-verified
  hypotheses) — only at IEEE CISS 2024, not a journal.
- Yu, "Dimension-Free Bounds…", Entropy 25(5):767 (2023) — the strongest
  PEER-REVIEWED record, c≈0.38234.
- Alweiss–Huang–Sellke (3−√5)/2 — Electron. J. Combin. 31(3):P3.35 (2024).

This is exactly what claims `published-status-current` and `preprint-status-c`
already assert. The request is answered by the existing library; nothing was
downloaded because the relevant full texts are already in `research/sources/`
(and downloading them again is refused).

## No further gathering

Every angle is covered: entropy era (Gilmer, AHS, Chase–Lovett, Sawin, Pebody,
Boppana, Yu, Cambie, Liu), survey (Bruhn–Schaudt 2013), graph formulation,
lattice & minimal-counterexample, verification, small/large/separating families.
All frontmost rows of `research/FRONTIER.md` are either in the library or are
threads the run has already reasoned through. No request is open beyond the one
above.
