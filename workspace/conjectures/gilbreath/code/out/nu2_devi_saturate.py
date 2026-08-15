#!/usr/bin/env python3
"""Test whether D(n)=2nu2-n is white noise (uncorrelated, bounded) and whether max|D| saturates."""
import math, os

def load():
    nu2 = {}
    with open("/workspace/code/out/nu2_dense.txt") as f:
        for line in f:
            p = line.split()
            if len(p) == 2:
                nu2[int(p[0])] = int(p[1])
    return nu2

def acf(xs, maxlag):
    m = sum(xs)/len(xs)
    xc = [x-m for x in xs]
    v = sum(x*x for x in xc)
    return [sum(xc[i]*xc[i+lag] for i in range(len(xs)-lag))/v for lag in range(1, maxlag+1)]

def main():
    nu2 = load()
    ns = sorted(nu2)
    D = [2*nu2[n]-n for n in ns]
    N = len(D)

    # acf of D itself (correcting for the parity alternation would be complex; report raw)
    acD = acf(D, 20)
    print("acf(D) lags 1..20 (D=2nu2-n):")
    print("  ".join("%d:%.3f" % (k+1, acD[k]) for k in range(20)))

    # growth of max|D| over successive windows of 5000
    print("\nmax|D| by window of 5000 terms:")
    w = 5000
    for i in range(0, N, w):
        seg = D[i:i+w]
        print("  n=%5d..%-5d max|D|=%-4d  (sqrt(n)=%.1f)" % (i+1, i+len(seg), max(abs(x) for x in seg), math.sqrt(i+w)))

    # is max|D| saturating? linear-regression slope of max|D| on sqrt(window-end)
    # crude: report max|D| at cumulative prefixes
    cum = []
    m = 0
    for i,d in enumerate(D):
        if abs(d)>m: m=abs(d)
        cum.append(m)
    print("\ncumulative max|D| at n = 1e3,2e3,5e3,1e4,2e4,3e4:")
    for t in [1000,2000,5000,10000,20000,30000]:
        print("  n=%6d max|D|=%d  max|D|/sqrt(n)=%.3f" % (t, cum[t-1], cum[t-1]/math.sqrt(t)))

    # fraction of the time |D| is small
    print("\nfraction |D|<=100: %.3f ; <=300: %.3f ; <=640: %.3f" %
          (sum(1 for x in D if abs(x)<=100)/N, sum(1 for x in D if abs(x)<=300)/N, sum(1 for x in D if abs(x)<=640)/N))

    # check for the 1e5 dataset on disk
    for cand in ["/workspace/code/out/nu2_incremental_1e5.txt",
                 "/workspace/code/out/nu2_fluct_30000.txt"]:
        print(cand, "exists:", os.path.exists(cand))

if __name__ == "__main__":
    main()
