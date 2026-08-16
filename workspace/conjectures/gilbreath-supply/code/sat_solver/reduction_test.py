#!/usr/bin/env python3
"""Find an EXACT reduction of "equal C_1..C_K" to cheap constraints.

For the SAT encoding we need to know which combination of invariants has the
SAME fiber structure as the full cumulative C_1..C_K histogram grouping.  If a
reduction is exact (same multiset of per-fiber S2-sets), then forcing the
reduction in SAT is equivalent to forcing equal C_1..C_K.

Candidates:
  R2 : C_K histogram + prefix_K + suffix_K
  R5 : C_K histogram + prefix_K + suffix_1
  R6 : C_K histogram only
  (R1 = C_K + prefix_K was already shown a strict refinement by the oracle)

Check over n=4..13, all K.
"""
import sys, os
from itertools import product
from lib.supply_fold import s_sos

def hist(h,L):
    n=len(h); size=1<<L; cnt=[0]*size
    for p in range(n-L+1):
        w=0
        for b in range(L): w=(w<<1)|h[p+b]
        cnt[w]+=1
    return tuple(cnt)
def CK(h,K): return tuple(hist(h,L) for L in range(2,K+2))
def S2(n,h): S,_=s_sos(n,list(h)); return S*S

def full_groups(n, strings, s2v, K):
    g={}
    for h in strings: g.setdefault(CK(h,K),set()).add(s2v[h])
    return sorted([tuple(sorted(v)) for v in g.values()])

def red_groups(n, strings, s2v, K, mode):
    g={}
    for h in strings:
        if mode=='R2':
            sig=(hist(h,K+1), tuple(h[:K]), tuple(h[n-K:]))
        elif mode=='R1':
            sig=(hist(h,K+1), tuple(h[:K]))
        elif mode=='R6':
            sig=(hist(h,K+1),)
        elif mode=='R5':
            sig=(hist(h,K+1), tuple(h[:K]), (h[n-1],))
        g.setdefault(sig,set()).add(s2v[h])
    return sorted([tuple(sorted(v)) for v in g.values()])

def run():
    print("Testing reductions R1(CK+pref), R2(CK+pref+suff), R5(CK+pref+last1),"
          " R6(CK) against full C_1..C_K over n=4..13")
    for mode in ['R2','R5']:
        exact=True
        for n in range(4,14):
            strings=[tuple(x) for x in product([0,1],repeat=n)]
            s2v={h:S2(n,h) for h in strings}
            for K in range(1,n):
                f=full_groups(n,strings,s2v,K)
                r=red_groups(n,strings,s2v,K,mode)
                if f!=r:
                    exact=False
                    print("  %s MISMATCH n=%d K=%d"%(mode,n,K))
        print("%s EXACT: %s" % (mode, exact))
    return 0

if __name__=="__main__":
    sys.exit(run())
