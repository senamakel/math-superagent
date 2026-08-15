#!/usr/bin/env python3
"""Find the TRUE smallest affine modulus for each odd-period tail-1 word.

Strategy: L_pred = 2^ord_2(P) - 1 is a Mersenne number divisible by P, and is
known (conjecturally) affine.  The smallest affine modulus must be a divisor
of L_pred that is a multiple of P (since affinity at a modulus L_0 and the
word has period P implies affinity at any common multiple; and L_pred is
already affine).  Test all divisors D of L_pred with P | D in increasing order.
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

def affine_ok(vals, L, nmin, nmax):
    for r in range(L):
        diffs = {vals[n+L]-vals[n] for n in range(nmin, nmax-L+1) if n % L == r}
        if len(diffs) != 1:
            return False, None
    cr = {r: next(vals[n+L]-vals[n] for n in range(nmin, nmax-L+1) if n%L==r)
          for r in range(L)}
    return True, cr

def divisors_of(L):
    ds = []
    for d in range(1, int(math.isqrt(L))+1):
        if L % d == 0:
            ds.append(d)
            if d*d != L: ds.append(L//d)
    return sorted(ds)

def order2(P):
    k = 1; v = 2 % P
    while v != 1:
        v = (v*2) % P; k += 1
        if k > 6*P: return None
    return k

def main():
    print("TRUE smallest affine modulus L*(P) for odd-period tail-1 words")
    print("L* must divide 2^ord2(P)-1 and be a multiple of P")
    print("="*80)
    Plist = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,
             47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,81]
    for P in Plist:
        ord2 = order2(P)
        Lpred = 2**ord2 - 1
        # divisors of Lpred that are multiples of P, ascending
        cands = [d for d in divisors_of(Lpred) if d % P == 0]
        if len(cands) > 8:  # bound work
            cands = cands[:8]
        best_L = None; best_sum = None
        for D in sorted(cands):
            if D > 6000:
                break
            nmax = min(D*3 + 400, 40000)
            nmin = D + 150
            if nmin >= nmax:
                continue
            vals = nu2_map([0]*(P-1)+[1], nmax)
            ok, cr = affine_ok(vals, D, nmin, nmax)
            if ok:
                best_L = D
                best_sum = cr and sum(cr.values())
                break
        mers = ((P+1)&P)==0
        print("P=%4d mers=%s ord2=%3d L_pred=%8d  L*=%s  sum_c_r@L*=%s"
              % (P, mers, ord2, Lpred, best_L, best_sum))

if __name__ == "__main__":
    main()
