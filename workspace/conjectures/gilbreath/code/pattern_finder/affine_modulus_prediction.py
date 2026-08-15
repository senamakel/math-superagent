#!/usr/bin/env python3
"""Verify conjecture: affine modulus L of the tail-1 word of odd period P is
the smallest Mersenne number divisible by P, L = 2^ord_2(P) - 1.

For each P compute ord = multiplicative order of 2 mod P, predicted
L_pred = 2^ord - 1, then check per-residue affinity mod L_pred, and ALSO that
no proper divisor of L_pred that is a multiple of P works as a modulus
(so L_pred is the minimal one).
"""
import sys, math
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

def has_affine_suffix(vals, L, nmin, nmax):
    """True iff nu2(n+L)-nu2(n) is per-residue constant mod L over window.
    Returns (ok, sum_of_c_r, c_r)."""
    res = {}
    ok = True
    for r in range(L):
        diffs = {vals[n+L]-vals[n] for n in range(nmin, nmax-L+1) if n % L == r}
        if len(diffs) != 1:
            return False, None, None
        res[r] = diffs.pop()
    return True, sum(res.values()), res

def order2(P):
    """multiplicative order of 2 mod P (P odd)."""
    k = 1; v = 2 % P
    while v != 1:
        v = (v*2) % P; k += 1
        if k > 4*P:
            return None
    return k

def main():
    print("conjecture: affine modulus L(P) = smallest Mersenne 2^k-1 divisible by P")
    print("P in non-Mersenne odd periods")
    print("="*76)
    Plist = [5,9,11,13,17,19,21,23,25,27,29,33,35,37,39,41,43,45,
             47,49,51,53,55,57,59,61,65,67,69,71,73,75,77,81]
    for P in Plist:
        ord2 = order2(P)
        if ord2 is None:
            continue
        Lpred = 2**ord2 - 1
        # cost guard: window ~ few L, incremental O(N^2). skip huge L
        if Lpred > 6000:
            print("P=%4d ord2=%3d L_pred=%d (skip, window too big)"%(P,ord2,Lpred))
            continue
        nmax = min(Lpred*4 + 600, 32000)
        nmin = Lpred + 200
        if nmin > nmax:
            print("P=%4d window empty, skip"); continue
        vals = nu2_map([0]*(P-1)+[1], nmax)
        ok, S, cr = has_affine_suffix(vals, Lpred, nmin, nmax)
        # minimality: check each proper divisor D of Lpred with P|D
        minimal = ok
        if ok:
            for D in range(P, Lpred):
                if Lpred % D == 0 and P % D == 0 if P >= D else False:
                    pass
            # proper divisors multiples of P
            for D in range(2*P, Lpred, P):
                if Lpred % D == 0:
                    if has_affine_suffix(vals, D, nmin, nmax)[0]:
                        minimal = False
        print("P=%4d ord2=%3d L_pred=2^%-3d-1=%4d  affine@L_pred=%s  sum_c_r=%s  minimal=%s"
              % (P, ord2, ord2, Lpred, ok, S, minimal))

if __name__ == "__main__":
    main()
