# Encyclopedia of Mathematics — "Gröbner basis"

Source URL: https://encyclopediaofmath.org/wiki/Gr%C3%B6bner_basis
Full text: `research/sources/eom_groebner-basis.full.md`.

## What it establishes

The definition of a Gröbner basis of an ideal in a polynomial ring over a
field: a generating set whose leading terms (under a chosen monomial order)
generate the leading-term ideal. Properties: Buchberger's criterion and
algorithm; the division algorithm; the uniqueness of the reduced Gröbner
basis; elimination theory (an elimination order makes
`G ∩ K[x_{k+1},…,x_n]` a Gröbner basis of the elimination ideal); ideal
membership, radical and dimension testing via leading-term ideals.
Term orders include lex, graded lex, graded reverse lex, and **weighted
orders**.

## Bearing on the run

- The problem directive's instruments: "Gröbner bases with a weighted order"
  — the run's `ord_0(R_i)` analysis uses the weighted grading `w(a_j) = j`
  (weighted homogeneity of resultants). This entry is the reference for
  weighted monomial orders and elimination.
- The scheme picture (CA as an affine scheme over ℤ, cut out by
  `f(r_i) = f^{(i)}(r_i) = 0`, elimination of the `r_i` via Gröbner) is
  exactly the Diaz-Toca–Gonzalez-Vega / Castryck et al. computation that
  settles d ≤ 7 and d = 12. This entry fixes the definitions that computation
  uses.
- Over ℤ vs over `F_p`: the entry's field setting is the reason the run must
  state which base ring a Gröbner computation ran over (per the directive:
  a basis over ℚ and one over `F_p` answer different questions).

Claim status: reference-level definitions (textbook classical facts).