#!/usr/bin/env python3
"""Detrending control: is the persistent autocorrelation of nu2(n)/n a real
structure or an artifact of the secular mean drift (0.44 at n=100 -> 0.497 at
n=4000)? Detrend by subtracting a local running mean (window W), then
recompute the autocorrelation. If rho collapses, the persistence is drift, not
block structure.
"""
import sys
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    ps = primes_upto_index(N + 2)
    h = [((ps[j+1]-ps[j])//2) % 2 for j in range(N+1)]
    nu = [0]*(N+1)
    for n in range(2, N+1):
        _, ones = s_sos(n, h[:n])
        nu[n] = ones
    r = [nu[n]/n for n in range(2, N+1)]
    L = len(r)
    m_global = sum(r)/L
    dev = [x-m_global for x in r]
    var = sum(x*x for x in dev)/L
    def autocorr(seq):
        d=[x-sum(seq)/len(seq) for x in seq]
        v=sum(x*x for x in d)/len(d)
        out=[]
        for k in [1,2,3,5,8,13,21,34,55,80]:
            if k>=len(d): break
            out.append(sum(d[i]*d[i+k] for i in range(len(d)-k))/v/len(d))
        return out
    print(f"N={N} global variance(c)={var:.5e}")
    print("  lag  raw-residual-rho   detrended-rho(W=200)  detrended(W=500)")
    raw = autocorr(dev)
    # detrended residual: r[i] - local_mean(i)
    for W in [200, 500]:
        pass
    det200=[]; det500=[]
    d200=[None]*L; d500=[None]*L
    # local mean via centered running window (skip edges -> NaN, exclude)
    for i in range(L):
        lo=max(0,i-W//2); hi=min(L,i+W//2+1)
        d200[i]=r[i]-sum(r[lo:hi])/(hi-lo)
        d500[i]=r[i]-sum(r[lo:hi])/(hi-lo) if W==500 else None
    # recompute detrended for W=500 separately below
    d500=[None]*L
    W5=500
    for i in range(L):
        lo=max(0,i-W5//2); hi=min(L,i+W5//2+1)
        d500[i]=r[i]-sum(r[lo:hi])/(hi-lo)
    a200=autocorr([x for x in d200 if x is not None])
    a500=autocorr([x for x in d500 if x is not None])
    lags=[1,2,3,5,8,13,21,34,55,80]
    for idx,k in enumerate(lags):
        r1=raw[idx] if idx<len(raw) else float('nan')
        r2=a200[idx] if idx<len(a200) else float('nan')
        r3=a500[idx] if idx<len(a500) else float('nan')
        print(f"  {k:3d}  {r1:+.4f}   {r2:+.4f}   {r3:+.4f}")

if __name__ == "__main__":
    main()
