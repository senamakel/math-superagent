# Approach: generic initial ideal (gin) of the resultant ideal

```approach
idea: Replace "compute the Gröbner basis of I = (R_1,…,R_{n−1}) ⊂ Q[a_1,…,a_{n−1}]"
       (the run's measured d=8 wall) with "compute the generic initial ideal
       gin(I)". By Galligo's theorem gin(I) is Borel-fixed, and by
       Bayer–Stillman gin(I) has the same depth, regularity, projective
       dimension, and number of minimal generators as I — so CA in the
       Schaub–Spivakovsky form ht(I) = n−1 can be read off gin(I) provided gin(I)
       is a complete intersection of Borel-fixed monomial generators. The bet:
       the Borel-fixed generators of gin(I_n) follow a rigid pattern in n
       (gin is determined by the Hilbert function, a much smaller object than a
       GB at a bad order), and that pattern is checkable well past n=8, where
       direct Gröbner elimination fails.
mechanism: The run's engine is exact elimination over Z/Q, which dies on the
       single-Gröbner-basis wall because the *basis* blows up. gin(I) is the
       initial ideal after a *generic* linear change of coordinates; it is
       Borel-fixed (stable under the Borel subgroup), hence has the canonical
       combinatorial form (a monomial ideal closed under the Borel partial
       order), and Bayer–Stillman prove it preserves all the homological
       invariants that CA needs: ht(I), depth, regularity, and (via the
       Hilbert–Burch / complete-intersection criterion) whether I is a complete
       intersection. So the n−1 resultants are reduced to one Borel-fixed
       monomial ideal whose generators one might determine or verify by
       pattern, and whose height equals ht(I) — a combinatorial certificate of
       CA_n that avoids ever computing the full GB of the R_i at a bad term
       order. The char-0 content is Galligo's theorem itself, which is FALSE in
       characteristic p (Bayer–Stillman produced counterexamples): in char p the
       initial ideal after a generic coordinate change need not be Borel-fixed,
       so the combinatorial certificate does not exist there.
status: proposed
first-step: (1) tool_builder, Singular/sympy over Q: for n = 4, 5, 6 form
       I_n = (R_1,…,R_{n−1}) with R_i = Res_x(f, H_i f) as integer polynomials
       in a_1..a_{n−1}; apply a generic (random rational) coordinate change,
       compute the degree-reverse-lex GB of the transformed ideal, take its
       initial ideal, and record: the Borel-fixed monomial generators, the
       Hilbert function, regularity, and ht = n−1. (2) Confirm each gin is
       Borel-fixed (check every generator is closed under x_j ↦ x_i, i<j) and a
       complete intersection, as the oracle guard. (3) Look for the pattern in
       the generators across n = 4,5,6 that would let n = 20 be *verified* from
       a conjectured gin without computing it.
precedent: none. `tropical-resultant-fan` (refuted) used the full Gröbner fan
       (all weight vectors) and died on the fan dominating the single-GB cost;
       gin is a single Borel-fixed ideal, not a fan, and its homological
       content is Bayer–Stillman, not tropical. `milnor-local-multiplicity`
       (refuted) and `deformation-obstruction-bad-points` (adopted) are about
       regularity/complete-intersection via minors; gin is the *initial-ideal
       in generic coordinates* route to the same invariants.
charp-break: Galligo's theorem (gin is Borel-fixed over char 0) fails in
       positive characteristic — Bayer–Stillman give explicit char-p examples
       where the generic initial ideal is not Borel-fixed. Since the entire
       certificate (Borel-fixed monomial generators + the homological transfer)
       rests on Galligo, the argument has no char-p analogue by construction:
       this is the named, located char-0-only step the workspace's admissibility
       test demands, and it fails the test in exactly the way a correct CA proof
       must.
```

## What is known and what is speculative

- **Sourced (classical, exact statements to be cited):** Galligo 1974/1979
  (gin is Borel-fixed in char 0); Bayer–Stillman (gin preserves depth,
  regularity, projective dimension, and detects Cohen–Macaulayness /
  complete intersections); the Borel-fixed ideal is determined by its Hilbert
  function. These are standard, but the run has not yet fetched their exact
  statements — the first step does not depend on them, the pattern-search does.
- **This run's own (owned):** ht(I_n) = n−1 ⟺ CA_n (Schaub–Spivakovsky, held);
  the single-GB wall at d=8 (computational-boundary, held). The gin route is a
  new way to decide ht(I_n) that does not compute the GB of the R_i directly.
- **Speculative (the bet):** that gin(I_n) is a complete intersection with a
  pattern in n, verifiable at n=20 without a full GB. Unproved; first step
  checks n=4,5,6 before the bet is taken.

## Why it is not a closed approach

`symmetric-product-diagonal-equivariant` (refuted) used S_n-equivariant geometry
of the symmetric power and died on the radical being CA restated. `bezoutian-
hankel-rank` (refuted) was matrix ranks. `tropical-resultant-fan` (refuted) was
the full fan. gin is the initial ideal in a single generic coordinate system —
a combinatorial, Borel-fixed object whose homological invariants Bayer–Stillman
prove coincide with I's — and none of the closed lines is that object.
