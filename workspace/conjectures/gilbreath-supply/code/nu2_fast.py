#!/usr/bin/env python3
"""Fast, correct computation of nu2(n) via the 2-adic submask-XOR DP.

V(d, base) = XOR over submasks o of d of h[base + o].
  Recurrence: d = d1 + 2^m with 2^m highest power of two <= d:
    V(d, base) = V(d1, base) XOR V(d1, base + 2^m).
  V(0, base) = h[base].
T(n,d) = V(d, n-1-d);  nu2(n) = #{d in [2,n-1] : T(n,d)=1}.

Store every row V(d, .) indexed by base (0..N-1-d). O(N^2) space, O(N^2) time.
Cross-check vs direct submask enumeration at small n.
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

def hpow(d):
    m=1
    while (m<<1)<=d: m<<=1
    return m

def nu2_fast(N,h):
    # rows[d] = list over base 0..N-1-d of V(d,base)
    rows=[None]*(N)
    rows[0]=[h[b] for b in range(N)]
    for d in range(1,N):
        m=hpow(d); d1=d-m
        r1=rows[d1]
        maxbase=N-1-d
        new=[0]*(maxbase+1)
        for base in range(maxbase+1):
            new[base]=r1[base]^r1[base+m]
        rows[d]=new
    # read diagonal
    out=[]
    for n in range(2,N+1):
        cnt=0
        for d in range(2,n):
            base=n-1-d
            cnt+=rows[d][base]
        out.append(cnt)
    return out

def nu2_brute(n,h):
    cnt=0
    for d in range(2,n):
        t=0; base=n-1-d; sub=d
        while True:
            t^=h[base+sub]
            if sub==0: break
            sub=(sub-1)&d
        cnt+=t
    return cnt

def main():
    import sys
    N=int(sys.argv[1]) if len(sys.argv)>1 else 1500
    ps=primes_upto_index(N+3)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+2)]
    fast=nu2_fast(N,h)
    ok=True
    for n in [2,3,5,8,13,21,34,55,64,89,100,128]:
        b=nu2_brute(n,h); f=fast[n-2]
        st="OK" if b==f else "MISMATCH"
        if b!=f: ok=False
        print(f"n={n:4d} brute={b:4d} fast={f:4d} {st}")
    print("cross-check %s"%("PASSED" if ok else "FAILED"))
    m=min(fast[n-2]/n for n in range(50,N+1))
    mn=min(range(50,N+1), key=lambda n: fast[n-2]/n)
    print("min nu2/n over [50,%d]=%.4f at n=%d nu2=%d"%(N,m,mn,fast[mn-2]))
    mean=sum(fast[n-2]/n for n in range(50,N+1))/(N-49)
    print("mean nu2/n over [50,%d]=%.4f"%(N,mean))
    below=[n for n in range(50,N+1) if fast[n-2]/n<0.42]
    print("points in [50,%d] with nu2/n<0.42: %s (count %d)"%(N,below[:40],len(below)))

if __name__=="__main__":
    main()
