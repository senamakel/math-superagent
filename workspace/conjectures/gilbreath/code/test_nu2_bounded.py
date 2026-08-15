#!/usr/bin/env python3
"""Test whether the nu2 fluctuation D(n)=2*nu2(n)-n is bounded (mean-reverting)
rather than a growing random walk. Data: code/out/nu2_dense.txt (n=1..30000).

If D were a genuine random walk with iid increments (or near-iid), its range
over N steps would grow ~ sqrt(N)*sd(inc). If increments are anticorrelated at
lag 1 (~ -0.5, MA(1) with theta=-1), D is essentially a bounded/stationary
fluctuation around 0 -- a MUCH stronger statement than the needed supply bound.
"""
import math

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
    I = [D[i+1]-D[i] for i in range(len(D)-1)]
    N = len(D)

    print("n range:", ns[0], "..", ns[-1], " count", len(ns))
    print("D(n) = 2*nu2(n)-n :  min %d  max %d  range %d" % (min(D), max(D), max(D)-min(D)))
    print("D(0)%+d ... D(last)%+d" % (D[0], D[-1]))
    print("sd(D) = %.1f" % math.sqrt(sum((x-sum(D)/N)**2 for x in D)/(N-1)))
    # what would a random walk predict?
    sdi = math.sqrt(sum((x-sum(I)/len(I))**2 for x in I)/(len(I)-1))
    print("sd(increment I) = %.1f ; random-walk predicted range over %d steps ~ sqrt(%d)*%.1f = %.0f"
          % (sdi, N, N, sdi, math.sqrt(N)*sdi))
    # autocorrelation of D itself at lag 1
    acD = acf(D, 5)
    print("acf(D, lags1..5):", "  ".join("%.3f"%a for a in acD))
    # splitting into windows: does D wander or stay near 0?
    stops = [int(N*k/10) for k in range(1,10)]
    print("D sampled every 3000:")
    for k in range(0, 10):
        idx = int(N*k/10)
        print("  n=%6d  D=%+d" % (ns[idx], D[idx]))

if __name__ == "__main__":
    main()
