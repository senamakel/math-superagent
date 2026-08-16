#!/usr/bin/env python3
"""Consolidated nu2(n) analyzer (all-submask fold form). """
import sys
from math import isqrt

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok = True
        r = isqrt(cand)
        for p in ps:
            if p > r: break
            if cand % p == 0: ok = False; break
        if ok: ps.append(cand)
        cand += 2
    return ps

def nu2_all(N, h):
    seq=[]
    for n in range(2,N+1):
        cnt=0
        for d in range(2,n):
            t=0
            base=n-1-d
            sub=d
            while True:
                t ^= h[base+sub]
                if sub==0: break
                sub=(sub-1)&d
            cnt+=t
        seq.append(cnt)
    return seq

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 1500
    ps = primes_upto_index(N+3)
    h=[((ps[j+1]-ps[j])//2) % 2 for j in range(N+2)]
    seq=nu2_all(N,h)
    # sanity: reproduce a couple published values
    print("sanity nu2 at n=64,128:", seq[64-2], seq[128-2])
    m=min(seq[n-2]/n for n in range(50,N+1))
    print("min nu2/n over n in [50,%d]: %.4f"%(N,m))
    mn=min(range(50,N+1), key=lambda n: seq[n-2]/n)
    print("argmin n=%d ratio=%.4f nu2=%d"%(mn,seq[mn-2]/mn,seq[mn-2]))
    # sub-sequences by n mod powers
    print("nu2(n) n odd :", [seq[n-2] for n in range(2,N+1) if n%2==1][:10])
    print("nu2(n) n even:", [seq[n-2] for n in range(2,N+1) if n%2==0][:10])
    print("nu2(n) n=1 mod4:", [seq[n-2] for n in range(2,N+1) if n%4==1][:12])
    print("nu2(n) n=3 mod4:", [seq[n-2] for n in range(2,N+1) if n%4==3][:12])

if __name__=="__main__":
    main()
