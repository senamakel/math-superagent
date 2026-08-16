#!/usr/bin/env python3
"""Direct observable: fold-cell density (= nu2/(n-2)) for primes vs random vs
structured inputs, over n up to N. This is the actual object; confirms the
primes sit in the generic-good class where fold-cell density ~ 0.5 (balanced
submask transforms), versus structured inputs where it collapses.
"""
import sys, random
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def dens_series(N, h):
    out=[]
    for n in range(2,N+1):
        S,ones=s_sos(n,h[:n])
        out.append(ones/(n-2) if n>2 else 0)
    return out

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 1500
    ps=primes_upto_index(N+2)
    h_pr=[((ps[j+1]-ps[j])//2)%2 for j in range(N+1)]
    random.seed(4)
    h_rand=[random.randint(0,1) for _ in range(N+1)]
    h_rand5=[1 if random.random()<0.15 else 0 for _ in range(N+1)]
    def tm(j): return bin(j).count('1')%2
    h_tm=[tm(j) for j in range(N+1)]
    print(f"N={N}")
    for label,h in [("primes",h_pr),("random0.5",h_rand),("random0.15",h_rand5),("thue",h_tm)]:
        d=dens_series(N,h)
        # mean fold density over last half, and at N
        tail=d[len(d)//2:]
        print(f"  [{label:10s}] mean fold-density(last half)={sum(tail)/len(tail):.4f}  at N={d[-1]:.4f}")

if __name__=="__main__":
    main()
