# Bacher — Determinants, mod 2 Pascal matrices, Beeblebrox reduction

<!-- source: https://arxiv.org/pdf/0708.1430 | converted from PDF -->

Roland Bacher, "Determinants related to Dirichlet characters modulo 2, 4 and 8 of binomial coefficients and the algebra of recurrence matrices", arXiv:0708.1430 (2007).

## What it establishes

Determinant and LU-factorization structure of matrices built from binomial
coefficients `C(s+t, s)`, `0 ≤ s,t < n`, reduced by various characters. The
relevant case for this problem is the **reduction modulo 2** of the symmetric
Pascal matrix `P(n)` with entries `C(s+t, s) mod 2`.

- **Theorem 2.1.** `det(P(2n)) = (−1)^n` for the reduction mod 2 of the
  symmetric Pascal matrix.
- **Theorem 2.3 / 2.7.** Exact formulae for `det(P(2n+1))` and for the
  determinant of the matrix given by entering the 2-adic valuation `ν₂` of the
  binomial coefficients — `det = (−1)^{n + ds(n)}`-type results, where `ds(n)`
  is the number of 1s in the binary expansion of `n`.
- **Section 6 (main result).** The "Beeblebrox reduction" `χ_B(2m)=0,
  χ_B(4m±1)=±1` (the Dirichlet character mod 4 not factoring through Z/2) gives
  a matrix `Z(n) = (χ_B(C(s+t,s)))` of determinant computed via an explicit
  **LU factorization of the infinite symmetric matrix**.
- Uses **recurrence matrices** — self-similar block matrices forming an algebra
  — as the main tool, linking to automatic sequences, 2-regular structure, and
  automata groups.

## Bearing on this problem

The fold `Φ` is the Pascal-mod-2 matrix. Bacher gives the exact linear-algebraic
structure of such matrices: their determinants (which for square mod-2 Pascal
matrices determine rank behaviour and hence nullity) and an LU factorization
that is exactly the sort of structural decomposition one would want to invert
`Φ` on submask-XOR coordinates. **Correction:** the summary's earlier reference to
"the known rank Φ_n = n−3, nullity-1, ker = span(all-ones) fact" repeats an
inherited fact that is itself wrong; the machine-verified operative rank is
`n−2` (full row rank, nullity 2, kernel = span(even-alt, odd-alt), all-ones =
their sum). Bacher's paper is independent of that error — it concerns square
symmetric Pascal matrices, not this problem's rectangular offset fold — so it
neither corroborates nor refutes the (corrected) rank. The self-similar block
structure (recurrence matrices) still transfers in spirit to `Φ`.

```claim
id: bacher-pascal-det-mod2
statement: For the symmetric Pascal matrix P(n) with entries C(s+t,s) reduced mod 2, det(P(2n)) = (-1)^n, and the mod-2 Pascal-matrix family carries an explicit LU factorization via self-similar block ("recurrence") matrices.
hypotheses: entries C(s+t,s) mod 2, 0 ≤ s,t < n; the LU factorization is of the infinite symmetric block-structured Pascal matrix.
holds-here: The determinant formula is for the *symmetric* Pascal matrix, whereas this problem's fold Φ_n is the rectangular offset matrix C(k-1, j-(n-k)) mod 2. Transfer to Φ_n is not automatic and is a genuine gap to check by direct computation; the self-similar block (recurrence-matrix) structure does transfer in spirit to Φ.
status: asserted-by-source (theorem stated with proof in full text; not independently recomputed for Φ_n here)
bearing: Supplies the published linear-algebraic and self-similar-block structure of Pascal-mod-2 matrices. **Note:** the older "rank n-3, nullity 1, ker = span(all-ones)" phrasing in this note's bearing is superseded — the operative fold's machine-verified rank is n-2 (fold-rank-is-n-2-nullity-2-alternating). Bacher concerns square symmetric Pascal matrices, so it provides structural context, not the rank value of this problem's rectangular fold.
anchor: research/summaries/bacher_beeblebrox_reduction.md
```

**Evidence class:** sourced (published paper; results stated with proofs in the
full text). Not yet cross-checked by an independent computation on the specific
`Φ_n` matrix of this problem.

**What would falsify its bearing:** if the mod-2 Pascal-matrix determinant/LU
structure did not transfer to the *rectangular, row/column-offset* fold matrix
`Φ_n` used here (entries `C(k−1, j−(n−k)) mod 2`). That is a genuine gap to
check by direct computation, not something to assume.
