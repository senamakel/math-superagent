# Wrong fetch — Kaleda–Shchurov 2011 "primary" full text is a homotopy-theory paper

## What happened

The file `research/sources/kaleda-shchurov-elementary-polycycles-2011-primary.full.md`
claims to be the primary full text of P. I. Kaleda, I. V. Shchurov, "Cyclicity of
elementary polycycles with fixed number of singular points in generic k-parameter
families" (St. Petersburg Math. J. 23(4) (2012), transl. from Algebra i Analiz 23(4)
(2011); DOI 10.1090/S1061-0022-2011-01158-6).

Its actual content is a **homotopy-theory paper** — topological Quillen homology for
algebras and modules over operads in modules over a commutative ring spectrum (Theorems
1.5–1.12: TQ finiteness, TQ Hurewicz, TQ Whitehead, homotopy completion tower). This is
arXiv:1102.1234 under a wrong name/URL, not the Kaleda–Shchurov polycycle paper.

## What is actually established about the Kaleda–Shchurov bound

The abstract quoted in `research/summaries/citations_w2034778875.md` (from the DOI
citation lookup) confirms the paper exists and states: "if the polycycles have a fixed
number of singular points and all the singular points are elementary, then an estimate
of cyclicity holds true, which is polynomial in the number of parameters of the family."

The specific form `E(n,k) ≤ C(n) k^{3n}` with `C(n) = 2^{5n² + 20n}` is NOT in any held
Kaleda–Shchurov full text (none is held). It is quoted in the Dukov 2023 summary
(`research/summaries/dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.md`
line 46: "Kaleda–Shchurov E(n,k) ≤ C(n)k^{3n}, C(n)=2^{5n²+20n}") and in the Dukov 2025
summary — i.e. it is carried at **second-hand (Dukov's survey) + citation-abstract**
level, not verified from the primary.

## Consequence for ROOT.md

ROOT.md line 16 cites `E(n,k)≤(2^(5n^2)+20n) k^(3n)` as "(Kaleda–Shchurov)". The citation
is real, the theorem shape is corroborated by Dukov and the citation abstract, but the
**primary full text is not held** and the file that claimed to be it is a wrong fetch.
Downgrade: `E(n,k) ≤ C(n)k^{3n}`, C(n)=2^{5n²+20n}, is asserted-by-source at
citation/Dukov-survey level, holds-here yes, falsifier = the real primary text.

## Lesson (third instance of the same failure mode)

After the mathnet-paperid lesson and the Springer-DOI lesson: an arXiv ID or DOI can
resolve to a paper with the wrong content when the ID was attached from memory or a
citation guess. Always verify the first lines of a fetched full text against the claimed
title before filing it as primary.
