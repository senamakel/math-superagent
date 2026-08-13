# Salez, "The Erdős–Straus conjecture: New modular equations and checking up to N=10^17"

Source: arXiv:1406.6307.
Full text: `research/sources/salez-seven-modular-equations.full.md`

## What it establishes (sourced)

- **Rosati parametrisation (Prop 1)**: for `p` an odd prime, `4/p` is
  3-Egyptian iff there are positive integers `A,B,C,D` with
  `4ABCD = A+B+pC` and `(ABD,p)=1`  (Type I / equation (1))
  OR `4ABCD = p(A+B)+C` and `(ABCD,p)=1` (Type II / equation (2)).
  Converse is *sufficient* (not necessary) for composite `n`.
- **Complete set of 7 modular equations (Prop 3 + Lemma 1 + Cor 1)**: for
  `p` an odd prime polynomial of degree 1, `4/p` is 3-Egyptian iff one of
  seven modular equations (14a,b,c and 15a,b,c,d) holds. This is a *complete*
  set for degree-1 prime polynomials: no other constant-coefficient modular
  equation can solve such a class. Three of the seven are new (14c, 15c, 15d);
  the other four reduce to Rosati (1954) and Yamamoto (1965).
- Only the residual six residues survive the sieve to `N=10^17`.
- **Reduction to `n ≡ 1 mod 24`**: by simple identities, handled if
  `n ≡ −1 mod 3`, `n ≡ −1 mod 4`, or `n ≡ −3 mod 8`; hence it suffices to
  treat primes `p ≡ 1 mod 24`. The six open residues {1,121,169,289,361,529}
  mod 840 are exactly the `p ≡ 1 mod 24` class after intersecting with the
  `mod 5` & `mod 7` filters (Swett's choice).
- Verification: sieve over `n ≡ r mod 892371480`, `r` in the residual set,
  claims every `n < 10^17` (non-square) has a modular certificate; checked
  51.7M squares separately. Program in C++.

## Implication for the run

This is the definitive statement of the modular-equation obstruction: the
seven equations are **exhaustive**. Therefore a new identity family covering
`n ≡ 1 (mod 840)` *cannot* be expressed as one of these seven constant-
coefficient modular equations; it must be of "a still unknown new type", in
Salez's own words. This bounds what a symbolic ansatz search can legitimately
find — anything that collapses to one of the seven shapes is a rediscovery.
