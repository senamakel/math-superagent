#!/usr/bin/env python3
"""Find the exact recursion R_{k+1} = F(R_k) for the Mersenne per-residue
half-constant arrays, by aligning indices carefully."""
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


def get_R(k, N=14000):
    P = 2 ** k - 1
    word = [0] * (P - 1) + [1]
    nmin = max(int(N * 0.22), P * 3)
    vals = nu2_seq(word, N)
    ok, cs = per_residue_affine(vals, P, nmin, N)
    assert ok
    return [x // 2 for x in cs]


Rs = {k: get_R(k) for k in range(2, 7)}

for k in (2, 3, 4, 5):
    Rk = Rs[k]; Rn = Rs[k + 1]
    print(f"===== k={k} =====")
    print("Rk  :", Rk)
    print("Rn  :", Rn)
    print(f"len Rk={len(Rk)} len Rn={len(Rn)}")
    # Attempt 1: Rn[r] for large r equals a shifted/transformed Rk
    # Test: is Rn[P_k+1:]  ==  Rn[:P_k]  (self-repetition with transformation)?
    Pk = len(Rk)
    first, second = Rn[:Pk], Rn[Pk:]
    print("Rn[:Pk]  =", first)
    print("Rn[Pk:]  =", second)
    # Is second == halve(first) pointwise except edges?  second == [1] + ...
    print()
