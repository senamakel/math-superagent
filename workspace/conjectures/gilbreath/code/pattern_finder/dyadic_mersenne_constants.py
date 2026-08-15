#!/usr/bin/env python3
"""Examine the affine constants c_r for Mersenne periods P=2^k-1, tail-1 word,
and look for a clean closed form. Report c_r and compare against candidate
formulas to identify the structural law."""
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
    cs = []
    ok = True
    for r in range(P):
        diffs = {vals[n + P] - vals[n] for n in range(nmin, nmax - P + 1)
                 if n % P == r}
        if len(diffs) != 1:
            ok = False
            cs.append(None)
        else:
            cs.append(diffs.pop())
    return ok, cs


def main():
    N = 4000
    nmin = 500
    for k in range(2, 7):
        P = 2 ** k - 1
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        ok, cs = per_residue_affine(vals, P, nmin, N)
        c2 = [c // 2 for c in cs]
        print("P=%3d (2^%d-1) affine=%s" % (P, k, ok))
        print("   c_r        =", cs)
        print("   c_r/2      =", c2)
        print("   min c_r    =", min(cs), " mean slope=%.4f" % (sum(cs)/P/P))
        print()


if __name__ == "__main__":
    main()
