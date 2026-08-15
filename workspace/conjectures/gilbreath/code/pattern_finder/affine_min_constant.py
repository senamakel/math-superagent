#!/usr/bin/env python3
"""Confirm the positive-linear-supply bound for general odd P.

Conjecture: for odd period P (tail-1 word), nu2 is per-residue affine mod
L = 2^ord2(P)-1, AND min_r c_r = 2 (so nu2(n) >= 2n/L - O(1), positive linear).

Print the full c_r array and min for a representative set incl. non-Mersenne.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2
from fractions import Fraction

def build_seq(word, n_terms):
    q = [2, 3]
    per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]

def nu2_map(word, nmax):
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out

def affine_cr(vals, L, nmin, nmax):
    seen = {}
    ok = True
    for n in range(nmin, nmax-L+1):
        d = vals[n+L]-vals[n]
        r = n % L
        if r in seen and seen[r] != d:
            return None
        seen[r] = d
    return seen  # dict r->c_r

def order2(P):
    k = 1; v = 2 % P
    while v != 1:
        v = (v*2) % P; k += 1
        if k > 8*P: return None
    return k

def main():
    print("min c_r per odd P at affine modulus L=2^ord2(P)-1")
    print("="*70)
    # representative incl non-Mersenne: P=5,9,17,21,23,33,51,73,85,89,93
    for P in [3,5,7,9,15,17,21,23,31,33,51,63,73,85,89,93]:
        ord2 = order2(P); L = 2**ord2 - 1
        if L > 3500:
            print("P=%4d L=%6d (skip)"%(P,L)); continue
        nmax = min(L*4+300, 30000); nmin = L+150
        vals = nu2_map([0]*(P-1)+[1], nmax)
        cr = affine_cr(vals, L, nmin, nmax)
        if cr is None:
            print("P=%4d L=%5d NOT affine"% (P, L)); continue
        cvals = [cr[r] for r in range(L)]
        mn = min(cvals)
        mers = ((P+1)&P)==0
        slope = Fraction(sum(cvals), L*L)
        print("P=%4d mers=%s L=%5d min_c_r=%d slope=%s  c_r[:12]=%s"
              % (P, mers, L, mn, slope, cvals[:12]))

if __name__ == "__main__":
    main()
