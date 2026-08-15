#!/usr/bin/env python3
"""Autocorrelation / memory structure of the nu2(q_n) supply fluctuation.

nu2_dense.txt is a run-computed exact series nu2(n) for n=1..30000.
D(n) = 2*nu2(n) - n  (the supply fluctuation; nu2 ~ n/2 means D stays small).
Increment  I(n) = D(n+1) - D(n) = 2*(nu2(n+1)-nu2(n)) - 1.

We measure:
  - mean/var of I(n) over n>=2 (is the walk driftless? what variance?)
  - autocorrelation of I at lags 1..60 (short-range memory in the supply)
  - autocorrelation of the sign of I
  - running max |D|/sqrt(n) to test the LIL/sqrt scaling claim
Nothing is invented: all integers come from the file.
"""
import math
from collections import Counter

def load():
    nu2 = {}
    with open("/workspace/code/out/nu2_dense.txt") as f:
        for line in f:
            p = line.split()
            if len(p) == 2:
                nu2[int(p[0])] = int(p[1])
    return nu2

def mean(xs):
    return sum(xs)/len(xs)

def var(xs):
    m = mean(xs)
    return sum((x-m)**2 for x in xs)/len(xs)

def autocorr(xs, maxlag):
    m = mean(xs)
    xc = [x-m for x in xs]
    v = sum(x*x for x in xc)
    out = []
    for lag in range(1, maxlag+1):
        num = sum(xc[i]*xc[i+lag] for i in range(len(xs)-lag))
        out.append(num/v)
    return out

def main():
    nu2 = load()
    ns = sorted(nu2)
    D = [2*nu2[n]-n for n in ns]
    I = [D[i+1]-D[i] for i in range(len(D)-1)]

    print("n range 1..%d;  D(n)=2nu2-n;  I(n)=D(n+1)-D(n), %d increments" % (ns[-1], len(I)))
    print("mean I = %.4f   (0 => driftless walk; near-negative means nu2 barely grows)" % mean(I))
    print("var  I = %.2f   sd(I)=%.2f" % (var(I), math.sqrt(var(I))))
    c = Counter(I)
    print("most common I values:", c.most_common(8))
    print("sign split: neg=%d zero=%d pos=%d" % (sum(1 for x in I if x<0), sum(1 for x in I if x==0), sum(1 for x in I if x>0)))

    ac = autocorr(I, 40)
    print("\nAutocorrelation of I at lags 1..40 (after lag0=1.0):")
    print("  ".join("%d:%.3f" % (i+1, ac[i]) for i in range(40)))
    # count |ac| > 0.05 after lag 3
    big = [i+1 for i in range(40) if abs(ac[i]) > 0.05]
    print("lags with |ac|>0.05:", big)

    # runs test on sign of I (no autocorr should mean random signs)
    signs = [1 if x>0 else (-1 if x<0 else 0) for x in I]
    # longest run of same nonzero sign
    best=0;cur=0
    for s in signs:
        if s==0:
            cur=0
        else:
            cur = cur+1 if cur else 1
            if cur>best: best=cur
    print("longest same-sign run of I:", best)

    # fluctuation scaling: max |D|/sqrt(n), and with sqrt(n ln(n))
    worst=None; w2=None
    for n in ns:
        d=D[n-1]
        r=abs(d)/math.sqrt(n)
        if worst is None or r>worst[0]: worst=(r,n,abs(d))
        r2=abs(d)/math.sqrt(n*math.log(n)) if n>=3 else 0
        if w2 is None or r2>w2[0]: w2=(r2,n,abs(d))
    print("max |D|/sqrt(n)   = %.3f at n=%d (|D|=%d)" % worst)
    print("max |D|/sqrt(nlnn)= %.3f at n=%d (|D|=%d)" % w2)

if __name__ == "__main__":
    main()
