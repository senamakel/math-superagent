#!/usr/bin/env python3
"""Gradient probe: how does the fold collapse depend on the density p of 1s in a
RANDOM string, and how does a single 1 ('rare defect') vs a random 10% differ?

suggests the boundary input property. Also test 'random but with k large
consecutive structure' (blocky) vs 'random' - does blockiness (still not
2-automatic, but autocorrelated) push toward collapse?
"""
import sys, random, math
from lib.supply_fold import s_sos

def s_mxlin(N, h):
    mx=0
    for n in range(2,N+1):
        S,_=s_sos(n,h[:n])
        if n>=300:
            mx=max(mx,abs(S)/n)
    return mx

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 800
    random.seed(13)
    print(f"N={N}, max|S|/n over [300,{N}]")
    for p in [0.01,0.1,0.3,0.5]:
        h=[1 if random.random()<p else 0 for _ in range(N+1)]
        print(f"  random density {p}: {s_mxlin(N,h):.4f}")
    # single 1 at a big index
    h=[0]*(N+1); h[N-500]=1
    print(f"  single 1 at index {N-500}: {s_mxlin(N,h):.4f}")
    # blocky: random but 25% flat runs
    h=[]; j=0
    while len(h)<N+1:
        rv=random.randint(0,1); L=random.randint(1,20)
        h += [rv]*min(L,N+1-len(h))
    print(f"  blocky (flat runs ~1..20): {s_mxlin(N,h):.4f}")
    # random but with one long all-1 run (structurally has a long constant run)
    h=[random.randint(0,1) for _ in range(N+1)]
    for i in range(200,N): h[i]=1
    print(f"  random + long 1-run: {s_mxlin(N,h):.4f}")

if __name__=="__main__":
    main()
