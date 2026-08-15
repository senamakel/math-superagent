#!/usr/bin/env python3
"""Determine the EXACT recursion R_{k+1} = F(R_k) for the Mersenne
per-residue half-constant arrays, using arrays generated directly
(independent route).  Goal: prove sum R_k = (3^k-3)/2 by induction.
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


def get_R(k, N=12000):
    P = 2 ** k - 1
    word = [0] * (P - 1) + [1]
    nmin = max(int(N * 0.22), P * 3)
    vals = nu2_seq(word, N)
    ok, cs = per_residue_affine(vals, P, nmin, N)
    assert ok
    return [x // 2 for x in cs]


Rs = {}
for k in range(2, 8):
    Rs[k] = get_R(k)
    print(f"R{k} = {Rs[k]}")
    print()

# Now find the recursion: express R_{k+1} in terms of R_k.
# R_{k+1} has length 2^{k+1}-1 = 2*P_k + 1 where P_k = 2^k-1.
# Try: R_{k+1}[r] = f(r, R_k[...])  -- test block decomposition.
for k in range(2, 6):
    Rk = Rs[k]; Rn = Rs[k + 1]
    Pk = 2 ** k - 1
    Ln = 2 ** (k + 1) - 1
    print(f"--- k={k} Rk len {Pk}, Rn len {Ln} ---")
    # hypothesis: Rn = [1] + B + C where B,C relate to Rk
    # Test Rn[1:Pk+1] and Rn[Pk+1:]
    B = Rn[1:Pk + 1]
    C = Rn[Pk + 1:]
    print(" Rn[1:Pk+1] =", B)
    print(" Rn[Pk+1:]  =", C)
    print(" 2*Rk       =", [2 * x for x in Rk])
    print(" Rk         =", Rk)
