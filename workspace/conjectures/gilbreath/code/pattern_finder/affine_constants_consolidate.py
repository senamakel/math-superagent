#!/usr/bin/env python3
"""Gather per-residue affine constants c_r for general odd P (tail-1 word),
verifying (a) affinity at L=2^ord2(P)-1, (b) min c_r = 2, (c) all c_r even,
(d) print sum_c_r / (2^ord2-1)^2 = slope and look for a closed form.

Uses lib.rightdiag (the run's canonical exact route) — this is consistent
with affine_modulus_efficient.py but adds the min c_r = 2 check and the
per-residue listing.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2

def build_seq(word, n_terms):
    q = [2, 3]; per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q)-2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]

def nu2_map(word, nmax):
    q = build_seq(word, nmax+1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out

def order2(P):
    k = 1; v = 2 % P
    while v != 1:
        v = (v*2) % P; k += 1
        if k > 8*P: return None
    return k

Plist = [3,5,7,9,11,15,17,21,23,33,51,73,85,89,93]
for P in Plist:
    ord2 = order2(P); L = 2**ord2 - 1
    if L > 5000: 
        print(f"P={P:3d} L={L} skip"); continue
    nmax = min(L*4+300, 30000); nmin = L+150
    vals = nu2_map([0]*(P-1)+[1], nmax)
    # per-residue constants
    seen = {}
    ok = True
    for n in range(nmin, nmax-L+1):
        d = vals[n+L]-vals[n]
        r = n % L
        if r in seen and seen[r] != d:
            ok = False; break
        seen[r] = d
    if not ok:
        print(f"P={P:3d} L={L} NOT affine"); continue
    cs = [seen[r] for r in range(L)]
    S = sum(cs); mn = min(cs); alle = all(c % 2 == 0 for c in cs)
    mers = ((P+1)&P)==0
    print(f"P={P:3d} mers={mers} L={L:5d} affine=1 min_c={mn} all_even={alle} "
          f"sum_c={S} slope={S/L/L:.6f} sum/(P)= {S/P if S%P==0 else S/P:.4f}")
