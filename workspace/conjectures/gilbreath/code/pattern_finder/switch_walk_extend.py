#!/usr/bin/env python3
"""Independent check + extension of the mod-4 switch walk e(n) >= 0.

Definitions (p_k = k-th prime; p_1=2, p_2=3, p_3=5, ...):
  bit_k = 1 if p_{k+1} != p_k (mod 4), i.e. prime gap == 2 (mod 4).
  w(n)  = #{ k : 2 <= k <= n-1, bit_k = 1 }   (window [2,n-1])
  e(n)  = 2*w(n) - (n-2)                       (switches minus non-switches)

Reported: e(n) >= 0 for all n in [2,1000000], min over n>=17 is 5.
Recompute from a fresh sieve and hunt the first violation beyond.
"""
import sys, time, math

def primes_upto(limit):
    if limit < 3:
        return []
    sieve = bytearray(b'\x01') * ((limit >> 1) + 1)
    sieve[0] = 0
    r = int(limit ** 0.5)
    for i in range(1, (r >> 1) + 1):
        if sieve[i]:
            step = 2*i + 1
            start = (step*step) >> 1
            sieve[start::step] = b'\x00' * (((len(sieve)-1-start)//step) + 1)
    out = [2]
    out.extend(2*i+1 for i in range(1, len(sieve)) if sieve[i])
    return out

def main(nmax):
    # need primes up to p_{nmax}; p_n ~ n log n
    Nneed = nmax + 5
    plim = int(Nneed*(math.log(Nneed)+math.log(math.log(Nneed))+1)) + 1000
    t0 = time.time()
    pr = primes_upto(plim)
    print(f"sieve to {plim}: {len(pr)} primes ({time.time()-t0:.1f}s)")
    # residues res[k] = p_k mod 4, res[1]=2, res[2]=3, ...
    res = [0] + [p & 3 for p in pr]
    have = len(pr)
    print(f"have primes p_1..p_{have}; need p_{nmax}; ok={have>=nmax}")
    if have < nmax:
        print("NOT ENOUGH PRIMES, abort"); return
    e = [0]*(nmax+1)   # e[n]; e[0],e[1] unused
    for n in range(2, nmax+1):
        # add gap between p_{n-1} and p_n: bit index k=n-1
        e[n] = e[n-1] + (1 if res[n-1] != res[n] else -1)
    vals = e[2:]
    gmin = min(vals)
    gmin_at = [n for n in range(2,nmax+1) if e[n]==gmin][0]
    viol = sum(1 for v in vals if v < 0)
    first = None
    for n in range(2,nmax+1):
        if e[n]<0: first=(n,e[n]); break
    print(f"e(n)>=0 for all n in [2,{nmax}]: {'YES' if viol==0 else 'NO'}  viol={viol} first={first}")
    print(f"global min e = {gmin} at n={gmin_at}")
    for T in [17,100,1000,10000,100000,1000000]:
        if T <= nmax:
            seg = e[T:]
            m = min(seg)
            ma = [n for n in range(T,nmax+1) if e[n]==m][0]
            print(f"min e over n>={T}: {m} at n={ma}")
    print(f"final e({nmax}) = {e[nmax]}")
    # spot-check against captured: n=100 e=24? captured e(100)? "min e(n)>=100: 24"
    for n in [17,44,100,1000,1003,10000,100000,1000000]:
        if n<=nmax:
            print(f"  e({n}) = {e[n]}")

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv)>1 else 1000000
    main(nmax)
