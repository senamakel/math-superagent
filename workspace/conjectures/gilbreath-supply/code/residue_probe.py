#!/usr/bin/env python3
"""Emit sub-sequences of nu2(n) for recurrence/OEIS probing:
  - nu2(n) for n odd, n even  (global residue)
  - nu2(2^k) dyadic
  - nu2(n) for n prime-indexed (n=q_i)
  Also prints the folded image weight along submask-sets (the 'switch density'
  proxy) to see if nu2 tracks it.
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
    rows=[None]*N
    rows[0]=[h[b] for b in range(N)]
    for d in range(1,N):
        m=hpow(d); d1=d-m; r1=rows[d1]; L=N-1-d
        new=[0]*(L+1)
        for base in range(L+1):
            new[base]=r1[base]^r1[base+m]
        rows[d]=new
    return [sum(rows[d][n-1-d] for d in range(2,n)) for n in range(2,N+1)]

def main():
    import sys
    N=int(sys.argv[1]) if len(sys.argv)>1 else 2000
    ps=primes_upto_index(N+3)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+2)]
    nu=nu2_fast(N,h)  # nu[n-2] = nu2(n)
    print("nu2 n odd (n=3,5,7,...):", [nu[n-2] for n in range(3,N+1,2)][:40])
    print("nu2 n even (n=4,6,8,...):",[nu[n-2] for n in range(4,N+1,2)][:40])
    print("nu2 at primes n=q_i (i=1..):", [nu[q-2] for q in ps[1:61]])  # q_2=3..
    print("nu2 at powers of 2 (k=1..):", [nu[(1<<k)-2] for k in range(1, 14) if (1<<k)<=N])
    # ratio nu2(n)/n for n=q_i
    print("nu2(q_i)/q_i for first 40 primes (i=2..):")
    print([round(nu[q-2]/q,3) for q in ps[1:41]])

if __name__=="__main__":
    main()
