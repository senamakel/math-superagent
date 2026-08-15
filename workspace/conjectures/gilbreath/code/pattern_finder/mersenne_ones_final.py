#!/usr/bin/env python3
"""Corrected final confirmation: ones positions of the Mersenne c_r/2 array.
Correct formula: ones at r = 0 and r = 2^k - 2^j for j = 1..k-1."""
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
            ok = False; cs.append(None)
        else:
            cs.append(diffs.pop())
    return ok, cs

def get_c(k, N=14000):
    P = 2 ** k - 1
    word = [0] * (P - 1) + [1]
    nmin = max(int(N * 0.22), P * 3)
    vals = nu2_seq(word, N)
    ok, cs = per_residue_affine(vals, P, nmin, N)
    assert ok
    return cs

def is_pow2(x):
    return x >= 1 and (x & (x - 1)) == 0

okA = okB = okC = okD = True
for k in range(2, 11):
    c = get_c(k); P = 2 ** k - 1
    R = [x // 2 for x in c]
    ones = sorted([r for r in range(P) if R[r] == 1])
    pred = sorted([0] + [2 ** k - 2 ** j for j in range(1, k)])
    okA &= (ones == pred)
    okB &= (R[1] == 2 ** (k - 1) - 1)
    okC &= all(is_pow2(R[r]) or r == 1 for r in range(P))
    okD &= (sum(c) == 3 ** k - 3)
print(f"ALL k=2..10: ones-positions(A)={okA}  R[1]=2^(k-1)-1 (B)={okB}  "
      f"pow2-elsewhere(C)={okC}  sum c_r=3^k-3 (D)={okD}")
print("\nones positions (r where c_r/2 == 1):")
for k in range(2, 11):
    c = get_c(k); P = 2 ** k - 1
    R = [x // 2 for x in c]
    ones = sorted([r for r in range(P) if R[r] == 1])
    print(f"  k={k:2d} P={P:4d}: {ones}")
