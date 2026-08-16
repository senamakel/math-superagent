#!/usr/bin/env python3
"""Structural probes on the exact nu2(n) over n=2..N.

Conventions:
  A (all submasks): T(n,d) = XOR over o in [0..d], o submask of d, of h[n-1-d+o].
    This reproduces the measured ~0.49 center. [problem.md: XOR over submasks]
  A_minus_d: same but excludes the full submask d (XOR with the fixed top
    window bit h[n-1], a bounded convention change).
We report min ratio in [50,N] for both, plus dyadic powers (collapse test).
"""
from math import isqrt

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok=True; r=isqrt(cand)
        for p in ps:
            if p>r: break
            if cand%p==0: ok=False; break
        if ok: ps.append(cand)
        cand+=2
    return ps

def main():
    N=int(__import__('sys').argv[1]) if len(__import__('sys').argv)>1 else 800
    ps=primes_upto_index(N+3)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+2)]
    seq=[]
    for n in range(2,N+1):
        cnt=0
        for d in range(2,n):
            t=0; base=n-1-d; sub=d
            while True:
                t^=h[base+sub]
                if sub==0: break
                sub=(sub-1)&d
            cnt+=t
        seq.append(cnt)
    print("N=%d"%N)
    print("n from 50..%d"%(N))

    # min ratio (convention A)
    m=min(seq[n-2]/n for n in range(50,N+1))
    mn=min(range(50,N+1), key=lambda n: seq[n-2]/n)
    print("convention A (all submasks): min nu2/n = %.4f at n=%d (nu2=%d)"
          %(m,mn,seq[mn-2]))

    # convention A_minus_d: toggle by h[n-1] (the full submask d adds h[base+d]=h[n-1])
    # each T flips if h[n-1]=1, so count -> (n-3)-count; if h[n-1]=0 same.
    # Build average over the range of min, but per-n it's deterministic:
    def B(n):
        cnt=seq[n-2]
        if h[n-1]==1:
            cnt = (n-1-2+1) - cnt   # number of d in [2,n-1] is n-2; flip all
        return cnt
    vals=[B(n)/n for n in range(50,N+1)]
    mb=min(vals); mnb=50+vals.index(mb)
    print("convention A-less-d (top bit toggle): min nu2/n = %.4f at n=%d"
          %(mb,mnb))

    print("dyadic powers (collapse test, conv A):")
    p2=2
    while p2<=N:
        print("  n=2^%d=%d  nu2=%d  nu2/n=%.4f"
              %(p2.bit_length()-1,p2,seq[p2-2],seq[p2-2]/p2))
        p2*=2

if __name__=="__main__":
    main()
