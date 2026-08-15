#!/usr/bin/env python3
"""Sharper ballot claim: min over n in [T,N] of e(n)/n (a linear lower bound).

e(n)=2w(n)-(n-2) depends only on residue signs u_k=(p_k mod4 in {1,3}) mapped to
+1 (1 mod4) / -1 (3 mod4); e(n) = -sum_{k=2}^{n} u_k u_{k+1} for the window
[2,n-1] shaded by the run's convention (gaps g_3..g_n correspond to products
u_2 u_3 .. u_{n-1} u_n).  We compute precisely, matching the run's w.

We seek c(T) = min_{n in [T,N]} e(n)/n over the dense range, to state
e(n) >= c(T)*n with the biggest visible c.  Stream the sieve to N primes.
"""
import sys, time
from math import isqrt

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000_000
N = int(sys.argv[2]) if len(sys.argv) > 2 else 10_000_000

t0=time.time()
sieve=bytearray(b'\x01')*(LIMIT+1); sieve[0]=sieve[1]=0
for i in range(2,isqrt(LIMIT)+1):
    if sieve[i]:
        sieve[i*i::i]=b'\x00'*(((LIMIT-i*i)//i)+1)
print("sieve to %d (%.1fs)"%(LIMIT,time.time()-t0))

idx=0
prev_res=None
w=0
# track e/n minima
c_global=1e9; c_global_n=0
c_by_tail={17:1e9,100:1e9,1000:1e9,10000:1e9,100000:1e9}
c_by_tail_n={}
e_min=1e9; e_min_n=0
for p in range(2,LIMIT+1):
    if not sieve[p]: continue
    idx+=1
    res=p&3
    if idx>=2:
        switch=0 if res==prev_res else 1
        w+=switch
        n=idx+1
        e=2*w-(n-2)
        if e<e_min: e_min=e;e_min_n=n
        r=e/n
        if n>=2 and r<c_global: c_global=r;c_global_n=n
        for T in c_by_tail:
            if n>=T and r<c_by_tail[T]:
                c_by_tail[T]=r; c_by_tail_n[T]=n
    prev_res=res
    if idx>=N+1: break
print("e_min global = %d at n=%d"%(e_min,e_min_n))
print("global min e/n = %.6f at n=%d"%(c_global,c_global_n))
for T in sorted(c_by_tail):
    print("min e/n over n>=[%d] = %.6f at n=%d"%(T,c_by_tail[T],c_by_tail_n[T]))
print("time %.1fs"%(time.time()-t0))
