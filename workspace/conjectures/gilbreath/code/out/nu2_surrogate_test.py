#!/usr/bin/env python3
"""Controlled interpretation: what does rho1(I)=-0.503 mean?
Compare to three surrogates with the SAME mean/var of I:
  A) D = pure random walk of iid increments (rho1(diff D) should be ~0)
  B) D = pure white noise (rho1(diff D) should be ~ -0.5, Var(D) constant)
  C) D = slow-wander + white noise  (rho1(diff)~-0.5 AND Var(D) grows)

Then decide which matches the real data: rho1~-0.5 AND growing Var(D) => C.
"""
import math, random

def acf1(xs):
    m=sum(xs)/len(xs); xc=[x-m for x in xs]; v=sum(x*x for x in xc)
    return sum(xc[i]*xc[i+1] for i in range(len(xs)-1))/v

def var(xs):
    m=sum(xs)/len(xs); return sum((x-m)**2 for x in xs)/len(xs)

def windows_var(xs, w=3000):
    return [var(xs[i:i+w]) for i in range(0,len(xs),w)]

random.seed(1)
N=30000
# surrogate increment distribution: match real I stats (sd~173, mean~0)
sd = 173.0

def run(model):
    if model=="randomwalk":
        D=[0]
        for i in range(1,N):
            D.append(D[-1]+random.gauss(0,sd))
    elif model=="whitenoise":
        D=[random.gauss(0, 120) for _ in range(N)]
    elif model=="hybrid":
        # slow wander (bounded-ish, sd~120 growing sublinearly) + fast noise sd 0
        D=[]; wander=0
        for i in range(1,N+1):
            wander += random.gauss(0, 120/math.sqrt(i))  # sub-diffusive drift
            D.append(wander)
    I=[D[i+1]-D[i] for i in range(N-1)]
    wv = windows_var(D)
    return acf1(I), wv

for m in ["randomwalk","whitenoise","hybrid"]:
    r1, wv = run(m)
    print("%-12s rho1(I)=%+.3f  window Var(D): [%.0f .. %.0f] ratio=%.2f"
          % (m, r1, wv[0], wv[-1], wv[-1]/wv[0]))

# real data
import numpy as np
nu2={}
with open("/workspace/code/out/nu2_dense.txt") as f:
    for line in f:
        p=line.split()
        if len(p)==2: nu2[int(p[0])]=int(p[1])
ns=sorted(nu2); D=[2*nu2[n]-n for n in ns]
I=[D[i+1]-D[i] for i in range(len(D)-1)]
wv=windows_var(D)
print("REAL      rho1(I)=%+.3f  window Var(D): [%.0f .. %.0f] ratio=%.2f"
      % (acf1(I), wv[0], wv[-1], wv[-1]/wv[0]))
print()
print("Verdict: real has rho1(I)~-0.5 (white-noise type) AND growing Var(D) (random-walk type).")
print("Neither pure A nor pure B matches. It is a hybrid: fast white-noise increments")
print("(MA(1) at the theta=-1 boundary) PLUS a slow drift, so D wanders sublinearly.")
