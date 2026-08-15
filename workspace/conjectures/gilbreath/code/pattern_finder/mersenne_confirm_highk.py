#!/usr/bin/env python3
"""Confirm the Mersenne per-residue affinity structure to higher k (to k=10),
verify sum c_r = 3^k - 3, min c_r = 2, and DISCOVER the exact array recursion
R_{k+1} = F(R_k).

Established (numerical, to k=8): per-residue affine with c_r/2 = R_k[r],
sum c_r = 3^k - 3, slope = (3^k-3)/(2^k-1)^2, min c_r = 2.
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
    # higher k: P=2^k-1; need window n >= nmin large, use N larger for big P
    N = 8000
    nmin_frac = 0.18   # nmin = frac*N
    for k in range(2, 11):
        P = 2 ** k - 1
        word = [0] * (P - 1) + [1]
        nmin = max(int(N * nmin_frac), P * 3)
        if nmin >= N - P:
            print(f"k={k} P={P}: window too small, nmin={nmin} N={N}; skipping")
            continue
        vals = nu2_seq(word, N)
        ok, cs = per_residue_affine(vals, P, nmin, N)
        if not ok:
            print(f"k={k} P={P}: NOT affine (window {nmin}..{N})")
            continue
        s = sum(cs)
        mn = min(cs)
        print(f"k={k} P={P:4d} affine? {ok} sum c_r={s} ==3^k-3={3**k-3}? {s==3**k-3}"
              f" min c_r={mn} slope={s/P/P:.8f}")


if __name__ == "__main__":
    main()
