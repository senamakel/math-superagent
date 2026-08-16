#!/usr/bin/env python3
"""Precise non-rigorous global scan of true inf_P g(P,alpha)/Eh over the FULL
4D two-atom class (correct feasible region: a=(a1+a2)/2<=t<b=(b1+b2)/2<=1,
all atoms free in [0,1]) as t varies, for several alpha.  Purpose: establish the
true crossing t_hat(alpha) that a correct scorer must return, and confirm it
matches Yu's ~0.38234 at alpha=0.035.  NON-rigorous (scipy global minimize) —
used only to know what the rigorous scorer must reproduce.
"""
import numpy as np
from scipy.optimize import differential_evolution, minimize, LinearConstraint


def h(x):
    x = float(np.clip(x, 0.0, 1.0))
    if x <= 0 or x >= 1:
        return 0.0
    return -x*np.log2(x) - (1-x)*np.log2(1-x)


def phi1(p, q):
    return float(np.median([max(p, q), 0.5, p + q]))


def ratio(a1, a2, b1, b2, t, alpha):
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0
    if not (0 <= a <= t < b <= 1):
        return 1e12
    if not (b > a):
        return 1e12
    beta = (t - a) / (b - a)
    if not (0.0 <= beta <= 1.0):
        return 1e12
    wa = (1 - beta) / 2.0
    wb = beta / 2.0
    vals = [a1, a2, b1, b2]
    wts = [wa, wa, wb, wb]
    eh = sum(wts[i]*h(vals[i]) for i in range(4))
    if eh <= 0:
        return 1e12
    e_indep = sum(wts[i]*wts[j]*h(vals[i]+vals[j]-vals[i]*vals[j])
                  for i in range(4) for j in range(4))
    e_coup = 2*wa*h(phi1(a1, a2)) + 2*wb*h(phi1(b1, b2))
    g = (1-alpha)*e_indep + alpha*e_coup
    return g / eh


def global_inf(t, alpha, floor=0.0):
    def obj(x):
        a1, a2, b1, b2 = x
        if not (floor <= a1+a2 <= 2*t and b1+b2 > 2*t):
            return 1e12
        if min(x) < 0 or max(x) > 1:
            return 1e12
        return ratio(a1, a2, b1, b2, t, alpha)
    res = differential_evolution(obj, [(0, 1)]*4, seed=3, tol=1e-14,
                                 maxiter=1200, popsize=30, polish=True)
    cons = [LinearConstraint([[1, 1, 0, 0]], floor, 2*t),
            LinearConstraint([[0, 0, 1, 1]], 2*t, 2)]
    r = minimize(obj, res.x, method="SLSQP", bounds=[(0, 1)]*4,
                 constraints=cons, options=dict(maxiter=4000, ftol=1e-15))
    return min(res.fun, r.fun), (res.x if res.fun <= r.fun else r.x)


def main():
    import sys
    alphas = [float(x) for x in sys.argv[1:]] or [0.035]
    ts = [0.38200, 0.38220, 0.38230, 0.38234, 0.38236, 0.38240, 0.3825, 0.3830]
    for alpha in alphas:
        print(f"=== alpha={alpha} ===")
        for t in ts:
            v, atom = global_inf(t, alpha)
            tag = "CERT>=1" if v >= 1.0 else "below"
            print(f"  t={t:.6f}  inf={v:.10f}  {tag}  atom=({atom[0]:.7f},{atom[1]:.7f},"
                  f"{atom[2]:.7f},{atom[3]:.7f})")


if __name__ == "__main__":
    main()
