#!/usr/bin/env python3
"""Independent refutation check of R-budget-n32 / G-order-k-sensitivity:
is K*(n) = ceil(n/2)?

The weakened target R-budget-n32 asserts K*(n)=ceil(n/2) for 6<=n<=32 (with
n=5 -> 2 = ceil-1 as sole exception). The imported witness table says
n=7->4,9->5,11->6,13->7,15->8  (=ceil).  The run's own kstar_exact.py
concludes n=7->3,9->4,11->5,...  (=floor at odd n).  These cannot both hold.

This script recomputes K* independently with the AUTHORITATIVE cumulative
definition (C_1..C_K = histograms of word lengths 2..K+1 over overlapping
windows, exact integer grouping) and the canonical lib.supply_fold.s_sos
oracle, exhaustively over all 2^n strings.  Exhaustive brute is the mandated
verification oracle (rule 9), declared small.

Complexity class: exponential, oracle_bound n<=15 (2^15=32768 states).
"""
import sys, os
from itertools import product
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from lib.supply_fold import s_sos

def hist(h, L):
    n = len(h)
    size = 1 << L
    cnt = [0]*size
    for p in range(n - L + 1):
        w = 0
        for b in range(L):
            w = (w << 1) | h[p+b]
        cnt[w] += 1
    return tuple(cnt)

def CK(h, K):
    return tuple(hist(h, L) for L in range(2, K+2))

def S2(n, h):
    S, _ = s_sos(n, list(h))
    return S*S

NMAX = 15
imported = {2:1,3:1,4:2,5:2,6:3,7:4,8:4,9:5,10:5,11:6,12:6,13:7,14:7,
            15:8,16:8,17:9,18:9,19:10,20:10}

print("== independent K*(n): cumulative C_1..C_K, exact grouping ==")
print(f"{'n':>3} {'K*':>3} {'ceil':>5} {'floor':>5} {'imported':>9} verdict")
for n in range(2, NMAX+1):
    strings = [tuple(x) for x in product([0,1], repeat=n)]
    s2v = {h: S2(n,h) for h in strings}
    kstar = None
    for K in range(1, n):
        g = {}
        for h in strings:
            g.setdefault(CK(h,K), set()).add(s2v[h])
        any_wit = any(len(v)>1 for v in g.values())
        if not any_wit:
            kstar = K
            break
    if kstar is None:
        kstar = n-1
    ceilv = (n+1)//2
    floorv = n//2
    match = "ceil" if kstar==ceilv else ("floor" if kstar==floorv else "OTHER")
    print(f"{n:>3} {kstar:>3} {ceilv:>5} {floorv:>5} {imported.get(n,'-'):>9}   {match}")

print()
print("== odd-n detail: does the ceil claim fail? ==")
for n in [5,7,9,11,13,15]:
    strings = [tuple(x) for x in product([0,1], repeat=n)]
    s2v = {h: S2(n,h) for h in strings}
    # is there a pair at K = ceil(n/2) - 1 (i.e. does ceil overstate the budget)?
    Ktest = (n+1)//2 - 1
    g={}
    for h in strings:
        g.setdefault(CK(h,Ktest), set()).add(s2v[h])
    wit = any(len(v)>1 for v in g.values())
    print(f"  n={n}: ceil={ (n+1)//2 } floor={ n//2 } | pair-exists-at-K=ceil-1={Ktest}: {wit}")
