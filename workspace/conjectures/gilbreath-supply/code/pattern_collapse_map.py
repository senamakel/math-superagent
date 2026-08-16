#!/usr/bin/env python3
"""Map the fold-collapse boundary: which properties of h push the Lucas fold
toward CLT (|S|~sqrt n, nu2~n/2) vs collapse (|S|~n, nu2 sublinear)?

Controls (the five closed doors + tests) let us find the minimal additional
structure that breaks CLT. Candidates h:
  - random iid               (CLT baseline, generic good)
  - Thue-Morse wt(j) mod 2   (known collapse - closed door 3)
  - slowly-varying: h[j]=j mod 2 alternating
  - periodic h
  - balanced anti-dyadic (closed door 4)
  - 'almost constant with rare defects'
For each: report max|S|/sqrt(n), max|S|/n over n in [300,N]. Collapse = the
latter ~ O(1) (|S| linear). This maps WHERE the generic CLT survives, i.e.
what 'unstructured enough' means.
"""
import sys, random, math
from lib.supply_fold import s_sos

def s_stats(N, h, label):
    mx_sq=mx_lin=0; tot_sq=0; cnt=0
    for n in range(2,N+1):
        S,_=s_sos(n,h[:n])
        if n>=300:
            mx_sq=max(mx_sq,abs(S)/math.sqrt(n))
            mx_lin=max(mx_lin,abs(S)/n)
            tot_sq+=abs(S)/math.sqrt(n); cnt+=1
    print(f"[{label:22s}] max|S|/sqrt(n)={mx_sq:7.2f}  mean/sqrt={tot_sq/cnt:6.3f}  max|S|/n={mx_lin:.4f}")

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 1200
    random.seed(5)
    h_rand=[random.randint(0,1) for _ in range(N+1)]
    def tm(j): return bin(j).count('1')%2
    h_tm=[tm(j) for j in range(N+1)]
    h_alt=[j%2 for j in range(N+1)]          # alternating
    h_per=[(j//2)%2 for j in range(N+1)]     # periodic period 4: 0,0,1,1
    # balanced anti-dyadic: h[j]=1 if j is a power-of-2 gap pattern... use tm XOR period
    h_anti=[tm(j)^(1 if (j & (j-1))==0 else 0) for j in range(N+1)]
    # 'almost constant, rare defect': mostly 0 with a 1 every 1000
    h_def=[1 if j%997==0 else 0 for j in range(N+1)]
    # sparse random: mostly 0, 10% ones - low weight
    h_sparse=[1 if random.random()<0.1 else 0 for _ in range(N+1)]
    print(f"N={N}")
    s_stats(N,h_rand,"random iid")
    s_stats(N,h_tm,"thue-morse")
    s_stats(N,h_alt,"alternating j%2")
    s_stats(N,h_per,"period-4")
    s_stats(N,h_anti,"anti-dyadic-ish")
    s_stats(N,h_def,"rare defect 1/997")
    s_stats(N,h_sparse,"sparse 10%")

if __name__=="__main__":
    main()
