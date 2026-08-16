#!/usr/bin/env python3
"""THE key question: is |S(n)| = o(n) (sublinear), and is the observed
|S(n)|~sqrt(n) primes-specific or generic?

nu2(n) = (n-2-S(n))/2,  S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}.
If |S(n)| <= (1-2c)n then nu2 >= c n. Empirically |S| <= 3.5 sqrt(n) = o(n),
which would give any c<1/2.

Control: same SOS fold, random h and Thue-Morse h, at the SAME n-ranges.
If random h also gives |S|/sqrt(n) bounded ~ const, then the sqrt bound is
FOLD/GENERIC (some cancellation identity), not prime-specific. That is still
useful: it would mean SUPPLY follows from a generic concentration fact about
the Lucas fold, needing no arithmetic at all (contradicting the switch-density
reduction as the only route).
"""
import sys, random, math
from lib.supply_fold import s_sos

def s_series(N, h):
    Ss=[0]*(N+1)
    for n in range(2,N+1):
        S,_ = s_sos(n, h[:n])
        Ss[n]=S
    return Ss

def report(Ss, ns, label):
    seg=[(Ss[n],n) for n in ns]
    mx=max(abs(s)/math.sqrt(n) for s,n in seg)
    mn=sum(abs(s)/math.sqrt(n) for s,n in seg)/len(seg)
    mxlin=max(abs(s)/n for s,n in seg)
    print(f"[{label}] max|S|/sqrt(n)={mx:.3f} mean|S|/sqrt(n)={mn:.3f} max|S|/n={mxlin:.4f}")

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 3000
    ps=__import__('lib.primes',fromlist=['primes_upto_index']).primes_upto_index(N+2)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+1)]
    Sprime=s_series(N,h)
    # random
    random.seed(3)
    hr=[random.randint(0,1) for _ in range(N+1)]
    Srand=s_series(N,hr)
    # thue-morse
    def tm(j): return bin(j).count('1')%2
    ht=[tm(j) for j in range(N+1)]
    Sthue=s_series(N,ht)
    ns=list(range(300,N+1))
    print(f"N={N}:")
    report(Sprime,ns,"primes")
    report(Srand,ns,"random")
    report(Sthue,ns,"thue-morse")

if __name__=="__main__":
    main()
