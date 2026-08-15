#!/usr/bin/env python3
"""Independently recompute the per-residue affine constants c_r for Mersenne
periods P=2^k-1 (tail-1 word) and test the recursive structure of the c_r/2
array.  This is a second, independent route to the constants that
mersenne_constants_structure.py / dyadic_mersenne_constants.py report.

Verified claims to attack:
  (1) sum_{r} c_r == 3^k - 3
  (2) mean slope == (3^k-3)/(2^k-1)^2
  (3) the c_r/2 array satisfies a self-similar recursion (find it)
"""
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
    N = 6000
    nmin = 800
    arrays = {}
    for k in range(2, 9):
        P = 2 ** k - 1
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        ok, cs = per_residue_affine(vals, P, nmin, N)
        c2 = [c // 2 for c in cs]
        arrays[k] = (P, c2)
        s = sum(cs)
        print("k=%d P=%3d affine=%s sum c_r=%d == 3^k-3=%d ? %r  slope=%.6f"
              % (k, P, ok, s, 3 ** k - 3, s == 3 ** k - 3,
                 s / P / P))
        print("   c_r/2 =", c2)
        print()

    # Recursion hypothesis: does A_{k+1} = f(A_k)?
    print("\n--- recursion probe ---")
    for k in range(2, 6):
        Pk, Ak = arrays[k]
        Pn, An = arrays[k + 1]
        half = Pk + 1  # (P_{k+1}+1)/2 = P_k+1
        # An[0] == 1; check An[1:half]
        left = An[1:half]
        right = An[half:]
        print(f"k={k}: An(1..{half-1}) = {left}")
        print(f"     An({half}..)    = {right}")
        print(f"     A_k            = {Ak}")
        print()


if __name__ == "__main__":
    main()
