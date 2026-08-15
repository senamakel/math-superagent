#!/usr/bin/env python3
"""Compute fresh Mersenne period-3 nu2 and confirm the per-residue affine
constant; also confirm the P=3 closed form 2*floor((n-1)/3) at larger n.
This is a sanity check that the recurrence machinery gives a genuine closed
form, used to (re)verify the nu2 sequence for round-tripping / OEIS.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(word, n_terms):
    q = [2, 3]; per = len(word)
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


# P=3, tail-1 word [0,0,1]: closed form nu2(n) = 2*floor((n-1)/3)
vals = nu2_seq([0, 0, 1], 4000)
bad = 0
for n in range(2, 4000):
    if vals.get(n) != 2 * ((n - 1) // 3):
        if bad == 0:
            print("first bad n=", n, vals.get(n), 2*((n-1)//3))
        bad += 1
print("P=3 closed-form 2*floor((n-1)/3): violations over [2,4000) =", bad)
print("first 20 nu2 terms:", [vals.get(n) for n in range(2, 22)])
