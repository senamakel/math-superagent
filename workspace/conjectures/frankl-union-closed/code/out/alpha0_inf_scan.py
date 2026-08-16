#!/usr/bin/env python3
"""alpha0_inf_scan.py

Attack the claim that at t=1/2, alpha=0, the inf of the two-atom coupling
ratio g(P,0)/Eh(p) over the FULL 4-parameter class equals phi/2 = 0.809016994.

At alpha=0 the coupled term vanishes, so
    g(P,0)/E h(p) = E_{P_p^{x2}} h(p+q-pq) / E h(p)   (iid-OR ratio of the marginal)
which depends only on the MARGINAL P_p of the admissible coupling:
    atoms a1,a2 (weight (1-beta)/2 each), b1,b2 (weight beta/2 each),
    beta = (t-a)/(b-a),  a=(a1+a2)/2 <= t=0.5 < b=(b1+b2)/2,  beta in (0,1], E h(p)>0.

The unconstrained minimum of the iid-OR ratio over ALL distributions is
(3-sqrt5)/2 = 0.381966 (the iid barrier).  The question is whether the
restriction to these admissible marginals forces the inf up to phi/2 (as the
claim asserts) or whether some admissible marginal gives < phi/2 (refuting the
"global sup = phi/2" part of the claim).

Method: high-precision exact-arithmetic evaluation of the ratio, minimized by
(i) a broad latin/grid multistart with SLSQP (float, locating candidates) and
(ii) a reference evaluation of each located candidate at 50-digit mpmath.

Oracle-function semantics: ratio(P) is computed directly from the definition
(the entropy of the OR of two independent copies of the marginal, divided by
the marginal entropy).  No lib.uc needed here (no finite family involved; this
is the continuous coupling objective).
"""
import math, random, itertools
from mpmath import mp, mpf, log, sqrt

mp.dps = 50

def h(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1-x)*math.log2(1-x)

def ratio(a1, a2, b1, b2, t=0.5):
    """iid-OR ratio of the marginal of the two-atom coupling at (t,alpha=0)."""
    a = 0.5*(a1+a2); b = 0.5*(b1+b2)
    if not (a <= t < b):
        return None
    if (b - a) <= 0:
        return None
    beta = (t - a)/(b - a)
    if not (0 < beta <= 1):
        return None
    wa = (1-beta)/2.0   # weight of each of a1,a2
    wb = beta/2.0       # weight of each of b1,b2
    atoms = [a1, a2, b1, b2]
    wts   = [wa, wa, wb, wb]
    eh = sum(w*h(q) for w,q in zip(wts, atoms))
    if eh <= 0:
        return None
    eor = 0.0
    for i in range(4):
        for j in range(4):
            p = atoms[i]; q = atoms[j]
            eor += wts[i]*wts[j]*h(p + q - p*q)
    return eor/eh

def ratio_mp(a1,a2,b1,b2,t=mpf("0.5")):
    a = (mpf(a1)+mpf(a2))/2; b = (mpf(b1)+mpf(b2))/2
    if not (a <= t < b) or (b-a) <= 0:
        return None
    beta = (t-a)/(b-a)
    if not (0 < beta <= 1):
        return None
    wa = (1-beta)/2; wb = beta/2
    atoms=[mpf(a1),mpf(a2),mpf(b1),mpf(b2)]; wts=[wa,wa,wb,wb]
    def hm(x):
        if x<=0 or x>=1: return mpf(0)
        return -x*log(x)/log(2)-(1-x)*log(1-x)/log(2)
    eh = sum(w*hm(q) for w,q in zip(wts,atoms))
    if eh <= 0: return None
    eor = mpf(0)
    for i in range(4):
        for j in range(4):
            p=atoms[i]; q=atoms[j]
            eor += wts[i]*wts[j]*hm(p+q-p*q)
    return eor/eh

def objective(x):
    a1,a2,b1,b2 = x
    r = ratio(a1,a2,b1,b2)
    if r is None:
        return 1e9
    return r

PHI2 = (1+math.sqrt(5))/4.0
BARRIER = (3-math.sqrt(5))/2.0
print("phi/2 =", PHI2, " (3-sqrt5)/2 =", BARRIER)
print()

# --- (i) multistart SLSQP-style local search over admissible (a1,a2,b1,b2) ---
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(0)
best = 1e9; best_x=None
bounds = [(0.0,1.0)]*4
for trial in range(400):
    x0 = rng.uniform(0.0,1.0,4)
    # ensure feasible star: a<=0.5<b
    if 0.5*(x0[0]+x0[1]) > 0.5:
        # mirror a-pair below 0.5
        x0[0]=rng.uniform(0,0.5); x0[1]=rng.uniform(0,0.5-x0[0])
    if 0.5*(x0[2]+x0[3]) <= 0.5:
        x0[2]=rng.uniform(0.5,1.0); x0[3]=rng.uniform(0.5-x0[2]+0.5,1.0) if False else rng.uniform(0.5,1.0)
    res = minimize(objective, x0, method='SLSQP', bounds=bounds,
                   options={'maxiter':200,'ftol':1e-12})
    if res.fun < best:
        best = res.fun; best_x = res.x
print("best ratio found (float SLSQP, two-atom alpha=0 t=1/2):", best)
print("best_x (a1,a2,b1,b2):", best_x)
print("vs phi/2 =", PHI2, "  gap =", PHI2 - best)
print()

# --- (ii) reference 50-digit evaluation of the best candidate ---
if best_x is not None:
    rm = ratio_mp(*best_x)
    print("mpmath 50-digit ratio at best_x =", rm)
    print("difference from phi/2 =", rm - PHI2)
print()

# --- (iii) targeted grid: two-point-like marginals designed to push ratio low ---
# Try marginals where the b-pair weight beta is large and b atoms high (h~0),
# a pair at extreme {0, p}: the shape that minimises the unconstrained ratio.
print("Targeted scan for low ratios (marginals with b weight large, h(b)~0):")
grid_low = 1e9; grid_x=None
for a1 in [0.0, 0.1, 0.2, 0.3, 0.382, 0.4, 0.49]:
    for a2 in [0.0, 0.1, 0.2, 0.3, 0.382, 0.4, 0.49]:
        if 0.5*(a1+a2) > 0.5: continue
        for a_hi in [0.7, 0.8, 0.9, 0.95, 0.98, 1.0]:
            b1 = a_hi
            for b2 in [0.5, 0.6, 0.7, 0.8, 0.9, 0.98, 1.0]:
                if 0.5*(b1+b2) <= 0.5: continue
                r = ratio(a1,a2,b1,b2)
                if r is not None and r < grid_low:
                    grid_low=r; grid_x=(a1,a2,b1,b2)
print("lowest ratio on targeted grid:", grid_low, "at", grid_x)
rm = ratio_mp(*grid_x) if grid_x else None
print("mpmath 50-digit:", rm)
print()
print("Barrier check reminder: unconstrained iid-OR min =", BARRIER, " (< phi/2" , PHI2, ")")
