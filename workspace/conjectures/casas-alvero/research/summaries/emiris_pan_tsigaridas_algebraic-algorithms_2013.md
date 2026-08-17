# Emiris–Pan–Tsigaridas, "Algebraic Algorithms" (arXiv:1311.3731, Computing Handbook Ch. 10)

**Source URL:** https://arxiv.org/pdf/1311.3731 (ArXiv; also HAL hal-00776270, CRC Press Computing
Handbook Vol. I "Computer Science and Software Engineering", 2013)

**What this source is.** The chapter on algebraic algorithms for the Computing
Handbook (3rd ed.), by Ioannis Z. Emiris (Athens), Victor Y. Pan (CUNY Lehman),
Elias P. Tsigaridas (PolSys/INRIA). Held full text: 2227 lines,
`research/sources/emiris_pan_tsigaridas_algebraic-algorithms_2013.full.md`.
It is the **cited precedent for the run's adopted `uresultant-one-var-eliminant`
approach** — the approach names §4.3 "Polynomial System Solving by Using
Resultants" as the classical source for the Macaulay u-resultant construction
(see `research/approaches/uresultant-one-var-eliminant.md`).

## What it establishes (the load-bearing pieces for CA)

1. **§4.1–4.2 — resultants as solvability conditions.** The Sylvester resultant
   Res_x(f,g) vanishes iff f,g share a root in the algebraic closure; the
   Bézout matrix yields the same determinant; Macaulay's matrix generalizes
   Sylvester to n+1 polynomials in n variables, its determinant being a multiple
   of the classical resultant, with a minor giving the exact resultant for
   generic coefficients (Macaulay 1916). Sparse/toric resultant via Newton
   polytopes and mixed volume (BKK bound) for sparse systems.

2. **§4.3 — the u-resultant (the theorem the CA approach uses).** To solve a
   well-constrained system of n polynomials in n variables, augment by a
   **generic linear polynomial** `p_l = u x + v y + w` (or more generally with
   generic coefficients u): the **u-resultant** is the multivariate resultant of
   the augmented (n+1)-polynomial system. Over ℂ it **factors into linear
   factors** whose coefficients give the common roots of the original system;
   one factor corresponds to the point at infinity. It can be constructed via
   Macaulay's, Dixon's, or sparse formulations, or by hiding a variable in the
   coefficient field. Determinant of the (transposed) Macaulay matrix of the
   running example (bivariate quadratic system augmented by `ux+vy+w`):
   `det M = (u−v+w)(−3u+v+w)(v+w)(u−v)` — the three affine solutions
   (1,−1), (−3,1), (0,1) and one point at infinity. Reducing to a generalized
   eigenproblem when specializing u,v; RUR representation.

**Bearing on the run.** This is the exact theorem behind the approach's
claim "Res_u(I) = c·u^B iff V(I) = {0}": the u-resultant of the CA resultant
ideal I = (R_1,…,R_{n−1}) factors into linear factors over ℂ with one factor
per point of V(I), so it is a pure power of the linear form u−u(0) = u exactly
when 0 is the only point (CA holds). The source is now held where previously
only cited in the approach file; the approach's §4.3 citation is verified
against the actual text (factorisation statement, Macaulay-matrix construction,
Dixon/sparse alternatives). The eigenproblem and RUR paragraphs are the
numerical-search side the run's mandate says must never decide — only the
exact resultant factorization may.

**Char-p note.** This source is char-0/ℂ (factorisation into linear factors
"over the complex numbers"). It does not address the mod-p reduction, which is
exactly where the run's own approach breaks (extra linear factors mod p = the
bad-prime content). The claim-level status stays: approach's theorem holds in
char 0; the char-p break was already located by the run.

**What would falsify the run's use of it.** If a later pass reads the full
§4.3 and finds the factorisation claim stated only for *squarefree / generic*
systems (the chapter says "factors into linear factors over the complex
numbers" without the multiplicity caveat the approach needs for the
zero-dimensional, possibly non-reduced V(I)); the multiplicities come from the
standard u-resultant theory (Lazard) rather than from this chapter. The claim
`uresultant-factors-linear` in `research/approaches/uresultant-one-var-eliminant.md`
should be read as citing this chapter for the *construction and the generic
factorisation*, with Lazard/multiplicity from the CA-specific notes
(`uresultant-multiplicity-certificate-novelty.md`).

```claim
id: uresultant-theorem-held-source
statement: The Macaulay u-resultant construction and its factorisation theorem
  — augment a well-constrained system of n polynomials in n variables by a
  generic linear polynomial with indeterminate coefficients u; the multivariate
  resultant of the augmented (n+1)-system is the u-resultant, which over C
  factors into linear factors whose coefficients give the common roots of the
  original system, one factor for each solution plus one for the point at
  infinity; constructible via Macaulay, Dixon, or sparse resultant matrices —
  is stated verbatim in Emiris–Pan–Tsigaridas, "Algebraic Algorithms",
  arXiv:1311.3731, §4.3 (pp. 19–20 of the held text). This is the theorem the
  run's adopted uresultant-one-var-eliminant approach names as its precedent;
  the source is now HELD in full text (research/sources/emiris_pan_tsigaridas_algebraic-algorithms_2013.full.md).
hypotheses: char-0/C coefficient field; well-constrained square system; generic
  augmentation by a linear form
holds-here: yes — the CA resultant ideal I=(R_1..R_{n-1}) is 0-dimensional when
  CA holds; V(I)={0} iff the u-resultant is a pure power c·u^B; char-0 (the
  chapter explicitly works over C; the char-p break is the extra linear factors,
  already located by the run's own admissibility test)
status: sourced
anchor: research/summaries/emiris_pan_tsigaridas_algebraic-algorithms_2013.md
falsifies: a reading of the full §4.3 that shows the factorisation statement is
  restricted to squarefree/reduced systems (in which case the multiplicity/
  scheme-structure claim must be re-sourced to Lazard)
```