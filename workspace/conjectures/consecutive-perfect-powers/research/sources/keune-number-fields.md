# Keune, "Number Fields" (lecture notes)

**Source URL:** https://doi.org/10.54195/ipvu4488
**Author:** Frans Keune
**Status:** Summary-level record — retrieved via read_sources; full text not stored (download blocked).

## Why this source is in the library

University lecture notes giving the foundational cyclotomic-field statements the problem needs: the ring of integers Z[zeta_m], the cyclotomic polynomials, discriminants, and ramification. It provides the elementary facts in a form the run can quote as sourced.

## Verified statements (from the retrieved excerpt)

- For m >= 1, Q(zeta_m) has degree phi(m) (Euler totient), with zeta_m a primitive m-th root of unity and minimal polynomial the cyclotomic polynomial Phi_m(X).
- **Ring of integers:** the ring of integers of Q(zeta_m) is Z[zeta_m]. In particular Z[zeta_p] is the ring of integers for p prime.
- X^m - 1 factors as Phi_m(X) * h(X) with h(X) in Z[X] monic.
- Discriminant formula: for p prime, r >= 1 with p^r > 2,
    disc(Q(zeta_{p^r})) = ± p^{p^{r-1}(p-1)(p^r - r - 1)}.
- The derivative identity m = zeta_m h(zeta_m) Phi_m'(zeta_m), and norm computations N(Phi_m'(zeta_m)).
- Ramification: the prime p ramifies in Q(zeta_p) (totally ramified).

## Relevance

These are the elementary, citable facts underpinning the factorisation x^p - 1 = prod_{i=1}^{p-1} (x - zeta_p^i) in Z[zeta_p] and the fact that (p) = (1-zeta_p)^{p-1} up to unit. Together with Nguyen's note and Milne's chapter 6, they establish that the run works in a genuine Dedekind domain with a known ramified prime and known discriminant.

## Verified vs not

Verified (from excerpt): degree phi(m), ring of integers = Z[zeta_m], discriminant formula, ramification of p. These are standard results of cyclotomic field theory.
