# OEIS A347925 — Gilbreath polynomials, coefficient denominators

<!-- source: https://oeis.org/A347925 | NOTE: this summary IS the complete document — the download system stores short OEIS pages as the summary file itself; there is no separate sources/oeis-A347925-gilbreath-polynomial-denominators.full.md on disk (a re-download is refused as a duplicate). -->

Catalogue record (Gatti, submitted Sep 2021) for a(n) = least common denominator of the
n-th Gilbreath polynomial P_n.

## What it establishes

Values: 1, 1, 1, 1, 1, 3, 6, 30, 180, 1260, 181440, 1814400, 19958400, ... (offset 1).
Consistent with the examples: P_6 has denominator 3; P_7 denominator 6; denominators grow
factorial-like (n≥10 essentially (n−1)!·10…: 181440 = 9!/2, 19958400 = 11!/2, ...).
Same definition as A347924: U(S)_x = 2^(n+x−1) + P_n(x), P_n = Σ T(n,i)·x^(i−1)/a(n);
the PARI computes the polynomial fit through m+3 upper-bound extensions and takes
lcm of denominators of the fitted coefficients.

## Bearing on this run

Together with A347924 it fixes the Gilbreath-polynomial object completely: P_m is an
interpolating polynomial of degree ≤ m−1 with rational coefficients (denominators as here),
representing the deviation of the upper-bound Gilbreath sequence from the pure power 2^(m+x−1).
The factorial growth of the denominators is a note of caution: the upper-bound sequence
itself grows like a factorial-free power of 2 plus a factorial-denominator polynomial, so the
claimed "bound" p_n − 2^{n−1} ≤ P_{n−1}(1) is a statement about how close the upper-bound
curve sits to 2^{n+x−1} at x=1. No theorem is stated in this record; the inequality is
Gatti's paper claim.

## Source status

OEIS record, author Riccardo Gatti; links the same Preprints mirror, his generator, Muney
2026, Odlyzko 1993. The b-file covers n=1..24.