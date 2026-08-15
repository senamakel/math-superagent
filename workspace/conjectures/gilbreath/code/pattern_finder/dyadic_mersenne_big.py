#!/usr/bin/env python3
"""Push the Mersenne-affine classification to large Mersenne periods (511, 1023)
over a wide window. O(N^2) incremental diagonals. Each P: 511 over N=8000 is
~64M diffs, 1023 over N=8000 is ~64M diffs too (O(N^2) independent of P)."""
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
    seen = {}
    for n in range(nmin, nmax - P + 1):
        d = vals[n + P] - vals[n]
        r = n % P
        if r in seen and seen[r] != d:
            ok = False
        seen[r] = d
    if not ok:
        return False, []
    cs = [seen[r] for r in range(P)]
    return True, cs


def main():
    for (P, N, nmin) in [(255, 6000, 1000), (511, 10000, 2000), (1023, 12000, 3000)]:
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        ok, cs = per_residue_affine(vals, P, nmin, N)
        nres = len(set(vals[n + P] - vals[n] for n in range(nmin, N - P + 1)))
        if ok:
            print("P=%4d (Mersenne) AFFINE  min c=%d  mean slope=%.4f  n in [%d,%d]"
                  % (P, min(cs), sum(cs)/P/P, nmin, N))
        else:
            print("P=%4d AFFINE? NO  distinct(P-step increments)=%d  n in [%d,%d]"
                  % (P, nres, nmin, N))


if __name__ == "__main__":
    main()
