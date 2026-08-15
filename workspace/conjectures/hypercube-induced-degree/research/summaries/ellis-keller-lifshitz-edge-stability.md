# Ellis–Keller–Lifshitz, "Structure of subsets of the discrete cube with small edge boundary" (2018) — summary

Source: https://doi.org/10.19086/da.3668 (read via read_sources; full note at
research/sources/ellis-keller-lifshitz-edge-stability-2018.md)

**Establishes:** sharp stability of the cube edge-isoperimetric inequality. If
F ⊆ {0,1}^n has size m and edge boundary at most g_n(m) + l (the minimum plus an
excess l), then F is within symmetric distance C·l of an extremal G (a
lexicographic initial segment up to cube automorphism), for an absolute
constant C — best possible up to C.

**Technique:** purely combinatorial (no Fourier): induction on n, with an
intermediate structure theorem on intersections with codimension-1 and
codimension-2 subcubes, shifting/compressions, and influence analysis. Notably
codimension-2 (not just codimension-1) is required for the inductive step.

**Why here:** the frontier's highest-cited missing primary source and a genuine
technique treatment of edge-isoperimetric stability, the sharp companion to
Keevash–Long (in library) and Ellis 2011 (in library). Near-minimal edge
boundary = low average internal degree — not low max degree D(S) — so it
confirms the obstruction while providing the standard combinatorial-alternative
method (to the spectral route) and a concrete warning about coordinate
induction (codimension-2 needed).

**Claim:** `ellis-keller-lifshitz-edge-stability` (asserted-by-source).
