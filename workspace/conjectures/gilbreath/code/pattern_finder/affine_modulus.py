#!/usr/bin/env python3
"""NEW: find the smallest affine modulus L for each odd-period tail-1 word.

nu2(n) = #2s in maximal {0,2} suffix of right diagonal through q_n.
Per-residue-affine mod L means: for each residue r mod L, nu2(n+L)-nu2(n) is a
constant over the window (same for all n ≡ r mod L).

Mersenne P=2^k-1 have L=P.  P=5 is affine mod 15 (=3P) but not mod 5.
Question: for general odd P, what is the smallest L (as a multiple of P?)
with per-residue affinity?  Is there a pattern in L/P?
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

def nu2_map(word, nmax):
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out

def affine_mod(vals, L, nmin, nmax):
    """True iff nu2(n+L)-nu2(n) constant per residue mod L over [nmin,nmax-L]."""
    for r in range(L):
        diffs = {vals[n+L]-vals[n] for n in range(nmin, nmax-L+1) if n % L == r}
        if len(diffs) != 1:
            return False
    return True

def smallest_affine_modulus(P, nmax, nmin, max_mult=8):
    vals = nu2_map([0]*(P-1)+[1], nmax)
    for m in range(1, max_mult+1):
        L = m*P
        if affine_mod(vals, L, nmin, nmax):
            return m, L
    return None, None

def main():
    print("Smallest affine modulus L=m*P for odd-period tail-1 words.")
    print("P=2^k-1 (Mersenne) known to be affine at L=P.  Is L always m*P?")
    print("="*72)
    Plist = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,
             47,49,51,53,57,59,63]
    for P in Plist:
        nmax = P*8 + 500
        nmin = P*2 + 100
        m, L = smallest_affine_modulus(P, nmax, nmin)
        mers = ((P+1)&P)==0  # P = 2^k-1
        print("P=%4d  mersenne=%s  affine-modulus m=%s  L=%s"
              % (P, mers, m, L))

if __name__ == "__main__":
    main()
