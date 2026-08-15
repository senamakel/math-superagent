#!/usr/bin/env python3
"""Rigor: is D(n)=2nu2-n a bounded stationary (white-noise) process, or a growing random walk?

Signature test 1 (MA(1) boundary): if D is iid white noise, then I(n)=D(n+1)-D(n)
has acf rho1 == -0.5 exactly and rho_k==0 for k>=2. Verified already (rho1=-0.503).
  -> implies D is NOT a random walk (a random walk has I uncorrelated, rho1=0).

Signature test 2 (stationarity): white noise has CONSTANT variance over time.
  Var of D in disjoint time windows; is it stable or growing like n?

Signature test 3 (consistency): for iid D, Var(I)=2 Var(D)(1-rho1) = Var(D) when rho1=-0.5.
  Check Var(I) vs Var(D).

Signature test 4: I must be uncorrelated at all lags k>=2 (nothing left over).
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

def mean(xs): return sum(xs)/len(xs)
def var(xs):
    m = mean(xs); return sum((x-m)**2 for x in xs)/len(xs)
def acf(xs, maxlag):
    m = mean(xs); xc=[x-m for x in xs]; v=sum(x*x for x in xc)
    return [sum(xc[i]*xc[i+lag] for i in range(len(xs)-lag))/v for lag in range(1, maxlag+1)]

def main():
    nu2 = load()
    ns = sorted(nu2)
    D = [2*nu2[n]-n for n in ns]
    N = len(D)
    I = [D[i+1]-D[i] for i in range(N-1)]

    print("== signature 2: stationarity of D (constant variance across windows, 3000-wide) ==")
    w = 3000
    vs = []
    for i in range(0, N, w):
        seg = D[i:i+w]
        vs.append(var(seg))
    print("Var(D) per window:", ["%.1f"%v for v in vs])
    print("(if Var is ~constant, D is stationary/bounded; if it grows like n, D is a random walk)")
    print("mean of window variances = %.1f, ratio last/first = %.2f" % (mean(vs), vs[-1]/vs[0]))

    print("\n== signature 3: Var(I) vs Var(D) consistency ==")
    vD = var(D); vI = var(I)
    print("Var(D)=%.1f  Var(I)=%.1f  ratio Var(I)/Var(D)=%.3f  (iid-D predicts 1.0)" % (vD, vI, vI/vD))
    print("sd(D)=%.1f  sd(I)=%.1f" % (math.sqrt(vD), math.sqrt(vI)))

    print("\n== signature 4: I uncorrelated at all lags (already rho1~-0.5, rho_k~0) ==")
    # partial: D's second increments J(n)=I(n+1)-I(n) would have rho1 = -0.5 again if I white
    J = [D[i+2]-2*D[i+1]+D[i] for i in range(N-2)]
    acJ = acf(J, 6)
    print("acf of J=I diff, lags1..6:", " ".join("%.3f"%a for a in acJ), " (want only lag1=-0.5)")

    print("\n== decisive: running max of |D| vs time ==")
    cm=[0]*N
    m=0
    for i,d in enumerate(D):
        if abs(d)>m: m=abs(d)
        cm[i]=m
    for t in [1000,5000,10000,20000,30000]:
        print("  n=%6d runmax|D|=%4d   sqrt(n)=%.1f  ratio=%.3f" % (t, cm[t-1], math.sqrt(t), cm[t-1]/math.sqrt(t)))
    # linear-regression of runmax on n (not sqrt n): a bounded process has slope ~0 on n
    # slope of cm on sqrt(n) over the last 10000 vs first 10000
    import numpy as np
    nsqrt = np.sqrt(np.arange(1,N+1))
    s_first = np.polyfit(nsqrt[:4000], cm[:4000], 1)[0]
    s_last  = np.polyfit(nsqrt[-4000:], cm[-4000:], 1)[0]
    print("slope runmax|D| on sqrt(n): first4000=%.4f last4000=%.4f  (if ~0 in last, |D| is saturating/bounded)" % (s_first, s_last))

if __name__ == "__main__":
    main()
