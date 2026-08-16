#!/usr/bin/env python3
"""Ceasaro/averaged lower-tail of nu2 from the S~random-walk structure.

nu2(n) = (n-2-S(n))/2. The empirical CLT says var(S(n)) ~ n, i.e. |S| ~ sqrt(n).
By a strong-law / martingale-difference or Kolmogorov-type bound on the
partial sums S(n) (if the increments behaved like the CLT suggests), almost all
n have |S(n)| <= n^alpha for alpha>1/2. This script measures the ACTUAL tail:
for thresholds c, the density of n<=N with nu2(n)/n < c. GOAL priority 1 is
exactly a density-1 c bound. From |S|<=n^a (a in (1/2,1)) one gets
nu2(n)/n >= 1/2 - n^{a-1} >= some c on all n past a point => density-1/cofinite.
Report how small a: over [200,N], max_a such that |S(n)| <= n^a for all n.
"""
import math

def main():
    Ss=[]; ns=[]
    for line in open('code/out/supply_endpoint_density.txt'):
        parts=line.split()
        if len(parts)<3 or parts[1]!='primes': continue
        ns.append(int(parts[0])); Ss.append(int(parts[2][2:]))
    start=300
    # find minimal a s.t. |S(n)| <= n^a for all n in [start,N]
    Ns=[500,1000,2000,4000]
    for N in Ns:
        seg=[(s,n) for s,n in zip(Ss,ns) if start<=n<=N]
        a=max(math.log(abs(s))/math.log(n) for s,n in seg if s!=0)
        mx=max(abs(s) for s,_ in seg)
        print(f"N={N}: minimal a (|S|<=n^a for all {start}..{N}) = {a:.4f}   max|S|/n^0.5={mx/math.sqrt(N):.2f}")
        # implied c from |S| <= n^a: nu2/n >= 1/2 - n^{a-1}; worst n=start
        c = 0.5 - start**(a-1)
        print(f"    implied uniform c (from a) = {c:.4f}")
    # density of low-tail
    print("\ndensity of n with nu2/n < c (upper-tail of |S|):")
    for c in [0.40,0.42,0.45,0.48]:
        for N in [1000,2000,4000]:
            seg=[(s,n) for s,n in zip(Ss,ns) if 100<=n<=N]
            bad=sum(1 for s,n in seg if (n-2-s)/2/n < c)
            print(f"  c={c:.2f} N={N}: density of nu2/n<c = {bad/len(seg):.4f} ({bad})")

if __name__=="__main__":
    main()
