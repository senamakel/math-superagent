#!/usr/bin/env python3
"""Attack R-submask-sufficiency / G-weak-input-strictness: does ANY FIXED
switch-density-0 binary string have liminf nu2(n)/n > 0?

The run has already shown every fixed sparse family tested (powers of 2,
squares, single fixed 1) has liminf ratio 0. The claimed witness must be
sparse-but-growing. Here we search a broad space of growing support families
S_n (h[j]=1 iff j in S_n) with |S_n| = o(n) and measure the lower envelope of
nu2(n)/n over a large n-range, looking for ANY family that keeps a positive
lower envelope on ALL large n (not just infinitely often).

Exact oracle lib.supply_fold.s_sos (O(n log n)), cross-checked vs literal per
row. This is a MEASUREMENT/search, not a proof. The deliverable: which
growing families keep a positive envelope and where each dies.
"""
import os, sys
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos

def nu2(n,h):
    S, ones = s_sos(n,h)
    return ones

def ind(n,M):
    h=[0]*n
    for j in M:
        if j<n: h[j]=1
    return h

def envelope(fn, n_lo, n_max, step, name):
    lows=[]
    args=[]
    for n in range(n_lo, n_max+1, step):
        h=fn(n)
        r=nu2(n,h)/n
        lows.append((n,r))
        args.append(r)
    whole=min(a for _,a in lows)
    tail=min(a for _,a in lows[len(lows)//2:])
    argmin=min(lows,key=lambda x:x[1])
    print(f"{name:34s} n[{n_lo},{n_max}] step={step} whole_min={whole:.4f} "
          f"tail_min={tail:.4f} argmin={argmin}")
    return whole, tail, argmin

import sympy, math

# Growing sparse families, each with |S_n|=o(n):
# (a) powers of 2 but only at ~ every log n-th, controls: known die
# (b) values n where nu2 drops: avoid exact powers of 2 by shifting every 2^k
#     by a growing offset (so h has 1s near-but-never-at the boundary)
def fam_shifted_pows(n):
    # 1s at 2^k + f(k) where f(k)=k : avoids landing exactly at 2^k
    return ind(n, [(1<<k)+k for k in range(60)])

def fam_shifted_pows2(n):
    # 1s at 2^k + 2^{k-1}
    return ind(n, [(1<<k)+(1<<max(k-1,0)) for k in range(60)])

def fam_thirds(n):
    # 1s at k*2^k  (density 0, avoids powers of 2)
    return ind(n, [k*(1<<k) for k in range(60)])

def fam_two_thirds_pow(n):
    # 1s at floor(2^k * (2/3))
    return ind(n, [int((1<<k)*2/3) for k in range(60)])

def fam_golden(n):
    # 1s at floor(phi * 2^k) -- irrational multiples of powers avoid exact 2^k
    phi=(1+5**0.5)/2
    return ind(n, [int(phi*(1<<k)) for k in range(60)])

def fam_powp63(n):
    # 1s at floor(0.63 * 2^k)
    return ind(n, [int(0.63*(1<<k)) for k in range(60)])

def fam_pow2_plus_pow2half(n):
    # 1s at 2^k + 2^{ceil(k/2)} and 2^k : a cluster near each power
    M=set()
    for k in range(60):
        M.add(1<<k)
        M.add((1<<k)+(1<<(k//2)))
    return ind(n,M)

def fam_log_the_primes(n):
    # place 1s at positions floor(n')/like: use j such that j is 'half primes'
    # Simpler growing family: j = k * k * k (cubes) - density n^{-2/3}
    return ind(n,[k**3 for k in range(1,80)])

def fam_fibonacci_growth(n):
    # j = floor(2^{k^2})? too fast. use j = 2^{k} appended occasional
    # spacing so support ~ log: skip some powers
    return ind(n,[1<<k for k in range(0,60,2)])   # every other power

def main():
    print("=== growing sparse supports (|S_n|=o(n)): lower envelope of nu2/n ===\n")
    tests=[
      ("shifted 2^k+k", fam_shifted_pows),
      ("shifted 2^k+2^{k-1}", fam_shifted_pows2),
      ("k*2^k (thirds)", fam_thirds),
      ("floor(2^k*2/3)", fam_two_thirds_pow),
      ("floor(phi*2^k)", fam_golden),
      ("floor(0.63*2^k)", fam_powp63),
      ("2^k & 2^k+2^{k/2}", fam_pow2_plus_pow2half),
      ("cubes", fam_log_the_primes),
      ("every-other power of 2", fam_fibonacci_growth),
    ]
    for name,fn in tests:
        try:
            envelope(fn, 256, 8192, 256, name)
        except Exception as e:
            print(name, "ERROR", e)
    print("\nNOTE: tail_min = min over top half of range (large-n liminf proxy).")
    print("Only a family with tail_min bounded away from 0 over an increasing")
    print("range would support R-submask-sufficiency / G-weak-input-strictness.")

if __name__=="__main__":
    main()
