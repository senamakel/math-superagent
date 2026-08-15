#!/usr/bin/env python3
"""Directly test which moduli are affine for P=11 and P=13 (tail-1 word).

P=11: L_pred=1023=3*11*31.  Candidate multiples of P dividing 1023: 33, 341, 1023.
      First scan said 'not affine' at L=11..88 (m=1..8), so 33 fails -> is it 341 or 1023?
P=13: L_pred=4095=3^2*5*7*13.  Multiples of 13 dividing 4095: 13, 39, 65, 91, 195,
      273, 455, 585, 1365, 4095.  Which are affine?  (first scan said L<=104 not)
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
        if k >= 2: out[k] = cycle_and_nu2(dd)[1]
    return out

def affine_ok(vals, L, nmin, nmax):
    seen = {}
    for n in range(nmin, nmax-L+1):
        d = vals[n+L]-vals[n]; r = n % L
        if r in seen and seen[r] != d: return False, None
        seen[r] = d
    return True, sum(seen.values())

def order2(P):
    k=1; v=2%P
    while v!=1:
        v=(v*2)%P; k+=1
        if k>8*P: return None
    return k

def test(P, moduli, nmax=20000, nmin=None):
    vals = nu2_map([0]*(P-1)+[1], nmax)
    print("P=%d ord2=%d" % (P, order2(P)))
    for L in moduli:
        if nmin is None: ni = L+150
        else: ni = nmin
        if ni >= nmax-L:
            print("  L=%6d (window too small)"%L); continue
        ok, S = affine_ok(vals, L, ni, nmax)
        print("  L=%6d affine=%s sum_c_r=%s" % (L, ok, S))

if __name__ == "__main__":
    print("P=11 tail-1 word, candidate affine moduli (multiples of 11 dividing 1023):")
    test(11, [33, 341, 1023])
    print()
    print("P=13 tail-1 word, candidate moduli (multiples of 13 dividing 4095):")
    test(13, [39, 65, 91, 195, 273, 455, 585, 1365, 4095])
