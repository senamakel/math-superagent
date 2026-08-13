# Gatti, rescode GitHub repository (OEIS A347924 / A347925 generator home)

<!-- source: https://github.com/gttrcr/ResearchCode | NOTE: this summary IS the complete document — the download system stores the small repo-root page here; the individual generator file's full text is at sources/gatti-researchcode-A347924-cs.full.md. There is no separate sources/gatti-researchcode-github.full.md on disk. -->

Riccardo Gatti's research-code repository. Structure: `OEIS/` (the sequence generators,
including A347924.cs and A347925.cs held at
`research/sources/gatti-researchcode-A347924-cs.full.md`), `astro/`, `mathematica/`;
45 commits, 0 stars, 1 watcher. No README describing the Gilbreath work.

## What it establishes

Bibliographically: the repo is the canonical location of Gatti's generator programs cited
by OEIS A347924/A347925 ("Program for the generation of the m-th Gilbreath polynomial"). It
confirms the author handles his own OEIS submissions (user gttrcr). No new mathematics is
stated in the repo root; the algorithms live in the OEIS/ files (see the A347924.cs
summary, which documents the exact `MaxK` upper-bound-extension + `FindSequenceFunction`
interpolation construction of P_m).

## Bearing on this run

Together with the two OEIS records, this fully pins down the Gilbreath-polynomial object so
it can be independently implemented (sympy/PARI) and the paper's claimed implication
`p_n − 2^{n−1} ≤ P_{n−1}(1) ⟹ GC(n)` can be tested as a checkable finite statement — the
closest the library can get to the 403-unavailable MDPI text.

## Source status

Public GitHub repo, no licence file; author confirmed. Not peer-reviewed; the OEIS records
(also Gatti's) are the archival half.