# Lane, "Asymptotic distribution of residues in Pascal's triangle mod p" (2023)

<!-- source: https://arxiv.org/abs/2309.12942 | converted from HTML -->

Full text at `research/sources/lane-asymptotic-residues-pascal-2023.full.md`. Connor
Lane, arXiv:2309.12942 (15 pp., 1 figure), math.NT.

## What it establishes

Fix a prime p. Standard objects: `T_p(n)` = number of nonzero residues in row n
of Pascal's triangle mod p; `φ_p(n)` = number of nonzero residues in the first n
rows mod p. The paper generalizes to Dirichlet-character weighted counts
`T_χ(n), φ_χ(n)`, and studies

`A_n(r)` := number of occurrences of the residue `r` (a fixed nonzero residue
mod p) in the first n rows of Pascal's triangle mod p.

- **Barat–Grabner showed** `A_n(r) ~ φ_p(n)/(p-1)` for all primes p and nonzero
  residues r (odd entries spread evenly among the nonzero residues mod p).
- **Lane's contribution**: an alternative, self-contained proof with an
  **explicit error term**: `A_n(r) = φ_p(n)/(p-1) + O(n^ϑ)` for a parameter ϑ
  defined in the paper (Section 5), improving the previous bound. Also discusses
  the distribution of `A_p(r)`.

## Bearing on Singmaster / on the binary-digit thread

This is a *distribution* result on residues mod p across all rows, adjacent to
but distinct from the thread's question. It says: among the coefficients in the
first n rows, each nonzero residue mod p occurs about equally often, with an
explicit error. Applied to the odd-only triangle (p=2, where the only nonzero
residue is 1), the nontrivial content is the *total* count `φ_2(n)` (Gould's
`Σ 2^{popcount(m)}`), and Lane's theorem adds nothing beyond that for p=2 — the
"even distribution" is vacuous when there is one nonzero residue. Where it
matters is **general p**: for odd a, representations `C(n,k)=a` must land in
residue classes mod p dictated by a; Lane quantifies how many coefficients in a
row region can carry a given residue, which is a partial-statistics analogue of
the multiplicity question. It does not address equal *integer values* across
rows, so the thread's gap (value multiplicity) is untouched, but it provides a
distributional benchmark: any value-multiplicity structure must sit inside a
residue distribution that is provably near-uniform.

## Notes

- Secondary result quoted here from the abstract; the paper's ϑ is not computed
  numerically in the digest and would need the full text for an explicit
  constant. Rooted in the Barat–Grabner digital-function literature already
  cited in the held Rowland survey.