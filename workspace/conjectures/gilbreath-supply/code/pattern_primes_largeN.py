#!/usr/bin/env python3
"""Is the CLT/collapse dichotomy the RIGHT way to see it? Test the specific
hypothesis that '2-automatic / regular' h collapses while 'unstructured' h
survives, at larger N, on several near-boundary strings, and on the primes.

Also answer the load-bearing question: does the primes' |S|~sqrt(n) survive at
larger N (extend the 4000-term data) or does a rare collapse appear? Extend to
N=12000 exact.
"""
import sys, random, math
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def s_stats(N, h, label):
    mx_sq=mx_lin=0; tot_sq=0; cnt=0
    for n in range(2,N+1):
        S,_=s_sos(n,h[:n])
        if n>=500:
            mx_sq=max(mx_sq,abs(S)/math.sqrt(n))
            mx_lin=max(mx_lin,abs(S)/n)
            tot_sq+=abs(S)/math.sqrt(n); cnt+=1
    print(f"[{label:20s}] max|S|/sqrt(n)={mx_sq:7.2f}  mean={tot_sq/cnt:6.3f}  max|S|/n={mx_lin:.4f}")

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 6000
    ps=primes_upto_index(N+2)
    h_pr=[((ps[j+1]-ps[j])//2)%2 for j in range(N+1)]
    random.seed(9)
    h_rand=[random.randint(0,1) for _ in range(N+1)]
    print(f"N={N}")
    print("(the two 'good' cases at larger N)")
    s_stats(N,h_pr,"primes")
    s_stats(N,h_rand,"random iid")

if __name__=="__main__":
    main()
