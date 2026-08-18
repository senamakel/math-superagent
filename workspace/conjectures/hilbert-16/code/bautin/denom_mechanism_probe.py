#!/usr/bin/env python3
"""Denominator mechanism probe: is the ilcm-clearing denominator D_d of the
focal value L_d determined by the rotation operator alone?

Both focal-value recurrences (5-param chart family and 6-param general
quadratic focus) solve, at each even degree d, the SAME linear system:

    rot(V_d) + rhs = L_d (u^2+v^2)^{d/2}   (coefficients of monomials
    u^{d-j} v^j, j=0..d)  plus gauge c_{d,0} = 0

with unknowns (c_{d,0},...,c_{d,d}, L_d).  rot and the radial term do not
depend on the number of parameters, so the system matrix M_d is IDENTICAL for
both families; only the right-hand side (from Q1, Q2 times derivatives of the
previous V) differs.

Observed (exact, on disk): the ilcm denominators coincide,
D_d = 8, 192, 18432, 1105920, 22295347200 for d = 4,6,8,10,12.

Hypothesis under test: D_d equals the ilcm of the denominators of the last
row of M_d^{-1} (the row that extracts L_d).  If so, the denominator sequence
is a property of the rotation operator alone -- a derivation for the
denominator identity -- and D_d can be computed WITHOUT the recurrence.

M_d has integer entries (rot has small integer coefficients, the radial term
contributes binomial coefficients, the gauge row is 1), so the last-row
denominators are controlled by det(M_d).
"""
from math import comb
from fractions import Fraction
from sympy import Matrix, ilcm, Rational


def build_M(d):
    """(d+2)x(d+2) integer matrix of the degree-d system.

    Rows: monomials u^{d-0}v^0 .. u^{0}v^d (index j=0..d), then the gauge row.
    Columns: c_{d,0}..c_{d,d} (index j=0..d), then L_d.
    Column j of the rotation block: coefficients of rot(u^{d-j} v^j).
    L_d column: coefficients of -(u^2+v^2)^{d/2}.
    """
    n = d + 1
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for j in range(n):
        # rot(u^{a} v^{b}) = -v*a*u^{a-1}v^b + u*b*u^a v^{b-1}
        a, b = d - j, j
        # term 1: -a u^{a-1} v^{b+1}
        if a >= 1:
            ja, jb = a - 1, b + 1
            assert ja + jb == d
            M[jb][j] += -a          # row index = v-exponent jb
        # term 2: +b u^{a+1} v^{b-1}
        if b >= 1:
            ja, jb = a + 1, b - 1
            assert ja + jb == d
            M[jb][j] += b
    # radial column: -(u^2+v^2)^{d/2} = -sum_k C(d/2,k) u^{2k} v^{d-2k}
    half = d // 2
    for k in range(half + 1):
        jb = d - 2 * k           # v-exponent
        M[jb][n] = -comb(half, k)
    # gauge row: coefficient of c_{d,0} equals 1 (V_d coefficient of u^d)
    M[n][0] = 1
    return Matrix(M)


def row_denom_lcm(Minv_row):
    """ilcm of denominators of the rational entries of a row vector."""
    l = 1
    for e in Minv_row:
        r = Rational(e)
        if r.q != 1:
            l = ilcm(l, r.q)
    return l


def main():
    observed = {4: 8, 6: 192, 8: 18432, 10: 1105920, 12: 22295347200}
    print("# Denominator mechanism probe: D_d vs lcm(last-row denoms of M_d^-1)")
    print("observed D_d:", observed)
    print()
    for d in (4, 6, 8, 10, 12):
        M = build_M(d)
        Minv = M.inv()          # exact rational inverse
        last = Minv.row(d + 1)  # the row that extracts L_d
        l = row_denom_lcm(last)
        det = M.det()
        # det as a fraction (integer); report its size
        detr = Rational(det)
        print(f"d={d:2d}: det(M)=±{abs(detr.p)} (dims {M.rows}x{M.cols}); "
              f"lcm of last-row denominators = {l}; observed D_d = {observed[d]}; "
              f"MATCH={l == observed[d]}")
        # also lcm over ALL rows of the inverse
        lall = 1
        for r in range(M.rows):
            lall = ilcm(lall, row_denom_lcm(Minv.row(r)))
        print(f"      lcm over ALL rows of M^-1 = {lall}; matches D too: "
              f"{lall == observed[d]}")


if __name__ == "__main__":
    main()
