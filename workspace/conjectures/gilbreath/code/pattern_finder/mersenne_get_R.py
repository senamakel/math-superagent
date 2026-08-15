#!/usr/bin/env python3
"""Find the EXACT recursion R_{k+1} = F(R_k) for the Mersenne per-residue
half-constant arrays by generating them for k=2..12 and searching for the
block rule.  Goal: prove sum c_r = 3^k-3 by induction."""
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


def get_R(k, N=12000, nmin_frac=0.22):
    P = 2 ** k - 1
    word = [0] * (P - 1) + [1]
    nmin = max(int(N * nmin_frac), P * 3)
    vals = nu2_seq(word, N)
    ok, cs = per_residue_affine(vals, P, nmin, N)
    assert ok, f"not affine k={k}"
    return cs


Rs = {}
for k in range(2, 8):
    Rs[k] = get_R(k)
    c = Rs[k]
    R = [x // 2 for x in c]
    Rs[k] = R
    print(f"k={k} P={2**k-1} sum c_r={sum(c)} (3^k-3={3**k-3}) R={R}")
    print()
