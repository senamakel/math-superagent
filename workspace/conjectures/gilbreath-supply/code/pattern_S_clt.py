#!/usr/bin/env python3
"""Confirm the CLT/central-limit interpretation of the |S(n)|~sqrt(n) bound.
Is S(n) behaving like sum of ~n balanced near-independent +-1's (std~sqrt(n)),
with the observed max|S|/sqrt(n)~3.8 just the CLT tail over 4000 trials? If so
the sqrt bound is a CLT heuristic that holds for random AND primes but is
broken by adversarial structured h (Thue-Morse) - NOT a deterministic theorem
about primes. Compute var(S(n)) scaling to confirm std~sqrt(n).
"""
import sys, math
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 4000
    ps=primes_upto_index(N+2)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+1)]
    Ss=[0]*(N+1)
    for n in range(2,N+1):
        S,_=s_sos(n,h[:n]); Ss[n]=S
    # sample std of S(n) within log-bins: std in bin ~ C sqrt(n_center)?
    print("bin(n0,n0+500)  sample-std(S)  sqrt(mid)  std/sqrt(mid)")
    for lo in [300,800,1500,2500,3500]:
        seg=[Ss[n] for n in range(lo,min(lo+500,N+1))]
        m=sum(seg)/len(seg)
        v=sum((x-m)**2 for x in seg)/len(seg)
        mid=(lo+min(lo+500,N+1))/2
        print(f"  {lo:5d}-{min(lo+500,N+1):<5d}  {v**0.5:8.1f}  {mid**0.5:7.1f}  {v**0.5/mid**0.5:.3f}")
    print("\n=> if std/sqrt(mid) ~ const, S(n) is CLT-like std~sqrt(n).")
    print("=> then |S(n)|~sqrt(n) is a CLT heuristic (holds for random h too),")
    print("   NOT a theorem; only proves nu2~n/2 'on average / for almost all n'")

if __name__=="__main__":
    main()
