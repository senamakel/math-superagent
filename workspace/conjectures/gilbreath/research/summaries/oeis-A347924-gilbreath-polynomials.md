# OEIS A347924 — Gilbreath polynomials, coefficient numerators

<!-- source: https://oeis.org/A347924 | full text: sources/oeis-A347924-gilbreath-polynomials.full.md -->

Catalogue record (Gatti, submitted Sep 2021) for the triangle T(m,n): row m holds the
numerators of the coefficients of the m-th Gilbreath polynomial.

## What it establishes (definition, verbatim from the record)

Let S = (p_1,...,p_m) be the first m primes. The **m-th Gilbreath polynomial** P_m is
defined by: the x-th term of the *upper bound Gilbreath sequence* of S, U(S)_x, satisfies

    U(S)_x = 2^(m+x-1) + P_m(x),   P_m = Σ_{n=1..m} T(m,n)·x^(n-1) / A347925(m).

Rows: m=1: 1; m=2: 1,0; m=3: 1,0,0; m=4: -1,-3,-1,0; m=5: -5,-5,-1,0,0;
m=6: -57,-55,-15,-2,0,0; m=7: -282,-232,-77,-14,-1,0,0; ... Example: P_6 =
(-57 − 55x − 15x² − 2x³)/3, and U(S_{p1..p6})_x = 2^(x+5) + P_6(x).

## Exact construction (from the Michel Marcus PARI, in the record)

For n primes: iterate `U`: append the **largest** k such that the extended finite sequence
is still Gilbreath (k = next prime candidate, `isg` = leading entries of all diff rows
equal 1), take m+3 such extensions v; then `P_m` is the polynomial fit of
`v[k] − 2^(k+m−1)`, with coefficients cleared by their least common denominator.
i.e. the polynomial passed through the m+3 points (x, U(S)_x − 2^(m+x−1)).

## Bearing on this run

This is the run's only **held, checkable artifact** of Gatti's Gilbreath-polynomial route
(the MDPI paper itself 403s from every mirror). The definition lets a later role implement
P_m in sympy/PARI and test the claimed implication path directly (p_n − 2^{n−1} ≤ P_{n−1}(1)).
Note the subtlety: P_m is a fit through m+3 extension points, all ≥ the primes; the record
itself does not state the inequality theorem — the inequality is Gatti's claim in the paper.

## Source status

OEIS sequence record (keyword sign,frac,tabl), author Riccardo Gatti, Sep 20 2021;
links Gatti's Preprints 2020, 2020030145 (the 403 mirror) and his generator program
(gttrcr/ResearchCode OEIS/A347924.cs, held at sources/gatti-researchcode-A347924-cs.full.md),
plus Muney 2026 (arXiv:2606.23721 §14.1) and Odlyzko 1993.