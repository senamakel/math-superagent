#!/usr/bin/env python3
"""Efficient: confirm per-residue affinity at L = 2^ord2(P)-1 for tail-1 words.

Reports sum_c_r and the mean slope (sum_c_r)/L^2, plus L and ord2.
Tests validity at L_pred only (not minimality).  Bound L to keep O(L^2) small.
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

def affine_ok(vals, L, nmin, nmax):
    seen = {}
    ok = True
    for n in range(nmin, nmax-L+1):
        d = vals[n+L]-vals[n]
        r = n % L
        if r in seen and seen[r] != d:
            return False, None
        seen[r] = d
    return True, sum(seen.values())

def order2(P):
    k = 1; v = 2 % P
    while v != 1:
        v = (v*2) % P; k += 1
        if k > 8*P: return None
    return k

def main():
    print("Affine modulus L=2^ord2(P)-1 for odd tail-1 words: affinity + slope")
    print("="*80)
    Plist = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,
             47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,81,83,85,89,91,93,
             95,97,99,101,103,105,107,109,111]
    for P in Plist:
        ord2 = order2(P)
        L = 2**ord2 - 1
        if L > 4000:
            print("P=%4d ord2=%3d L=%8d (skip)"%(P,ord2,L)); continue
        nmax = min(L*4 + 300, 30000)
        nmin = L + 150
        if nmin >= nmax:
            print("P=%4d window empty"); continue
        vals = nu2_map([0]*(P-1)+[1], nmax)
        ok, S = affine_ok(vals, L, nmin, nmax)
        mers = ((P+1)&P)==0
        slope = Fraction(S, L*L) if ok else None
        print("P=%4d mers=%s ord2=%3d L=%6d affine=%s sum_c_r=%d slope=%s (%.5f)"
              % (P, mers, ord2, L, ok, S if ok else -1,
                 slope if slope else 0, float(slope) if slope else 0))

if __name__ == "__main__":
    main()
