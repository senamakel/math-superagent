#!/usr/bin/env python3
"""Correlate nu2(n) with the local switch (gap-parity) density of h over the
window used by T(n,d), d in [2,n-1], reading h[n-1-d .. n-1] i.e. the last
(n-1) bits of the window ending at n. Specif: does nu2(n) track the fraction
of 1s in that window?
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

def main():
    import sys
    N=int(sys.argv[1]) if len(sys.argv)>1 else 4000
    ps=primes_upto_index(N+3)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+2)]
    rows=[None]*N
    rows[0]=[h[b] for b in range(N)]
    for d in range(1,N):
        m=hpow(d); d1=d-m; r1=rows[d1]; L=N-1-d
        new=[0]*(L+1)
        for base in range(L+1):
            new[base]=r1[base]^r1[base+m]
        rows[d]=new
    nu=[sum(rows[d][n-1-d] for d in range(2,n)) for n in range(2,N+1)]
    # window switch density: for cell n, the h-window is h[0..n-1] (since
    # n-1-d+o in [n-1-d, n-1], union over d in [2,n-1] covers h[0..n-1]).
    # fraction of 1s in h[0..n-1] (first n bits, i.e. gaps 0..n-2 -> n-1 bits)
    print("n   nu2/n   switch_frac(nu2-window)")
    # cumulative switch density
    cum=0
    fracs=[]
    for n in range(2,N+1):
        cum+= h[n-1]  # h index n-1 = gap q_n-q_{n-1}
        frac=cum/n
        fracs.append(frac)
    # Pearson correlation between nu2(n)/n and frac(n) over 50..N
    xs=[nu[n-2]/n for n in range(50,N+1)]
    ys=[fracs[n-2] for n in range(50,N+1)]
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    cov=sum((a-mx)*(b-my) for a,b in zip(xs,ys))/len(xs)
    vx=sum((a-mx)**2 for a in xs)/len(xs)
    vy=sum((b-my)**2 for b in ys)/len(ys)
    corr=cov/(vx**0.5*vy**0.5+1e-12)
    print("Pearson corr(nu2/n, switch_frac) over [50,%d] = %.4f"%(N,corr))
    # also correlation with the local (last-window) switch density, not cum
    # local over last w=100 gaps ending at n
    for w in [100, 250]:
        xs2=[]; ys2=[]
        for n in range(max(50,w+1), N+1):
            xs2.append(nu[n-2]/n)
            ys2.append(sum(h[n-w:n])/w)
        mx=sum(xs2)/len(xs2); my=sum(ys2)/len(ys2)
        cov=sum((a-mx)*(b-my) for a,b in zip(xs2,ys2))/len(xs2)
        vx=sum((a-mx)**2 for a in xs2)/len(xs2)
        vy=sum((b-my)**2 for b in ys2)/len(ys2)
        corr2=cov/(vx**0.5*vy**0.5+1e-12)
        print(f"Pearson corr(nu2/n, local switch w={w}) over [{max(50,w+1)},{N}] = {corr2:.4f}")

if __name__=="__main__":
    main()
