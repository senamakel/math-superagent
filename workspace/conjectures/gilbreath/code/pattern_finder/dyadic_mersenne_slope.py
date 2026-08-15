#!/usr/bin/env python3
"""Exact sum of affine constants c_r for Mersenne periods, to find the closed
form of the density slope sum(c_r)/P^2 and the structural law of c_r."""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(word, n_terms):
    q = [2, 3]
    per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def nu2_seq(word, nmax):
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out


def per_residue_affine(vals, P, nmin, nmax):
    seen = {}
    ok = True
    for n in range(nmin, nmax - P + 1):
        d = vals[n + P] - vals[n]
        r = n % P
        if r in seen and seen[r] != d:
            ok = False
        seen[r] = d
    if not ok:
        return False, []
    return True, [seen[r] for r in range(P)]


def main():
    for k in range(2, 11):
        P = 2 ** k - 1
        N = P * 6 + 1000
        nmin = P * 2 + 100
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        ok, cs = per_residue_affine(vals, P, nmin, N)
        if not ok:
            print("P=%4d not affine in [%d,%d]" % (P, nmin, N)); continue
        S = sum(cs)
        from fractions import Fraction
        slope = Fraction(S, P * P)
        print("P=%4d (2^%d-1)  sum c_r=%d  slope=%s=%.6f  3^k=%d  (S-3^k)=%d"
              % (P, k, S, slope, float(slope), 3 ** k, S - 3 ** k))


if __name__ == "__main__":
    main()
