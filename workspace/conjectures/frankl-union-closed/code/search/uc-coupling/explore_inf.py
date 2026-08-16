#!/usr/bin/env python3
"""Numerical (NON-rigorous) exploration of inf_P g(P,alpha)/Eh over the 4-param
two-atom class, to understand its shape before building the rigorous scorer.

For fixed (t, alpha) minimise g(P,alpha)/E h(p) over atoms (a1,a2,b1,b2) with
    a1,a2 in [0,t], b1,b2 in [t,1], (b1+b2)/2 > t, and a=(a1+a2)/2 < t (beta>0),
using multiple scipy starts.  Reports the min value and whether the argmin lies
on the 1-parameter subfamily (a1=a2=b1=a, b2=1) that Yu identifies.
"""
import numpy as np
from scipy.optimize import minimize


def h(x):
    x = np.clip(x, 0.0, 1.0)
    if x <= 0 or x >= 1:
        return 0.0
    return -x*np.log2(x) - (1-x)*np.log2(1-x)


def phi1(p, q):
    return float(np.median([max(p, q), 0.5, p + q]))


def ratio(atom, t, alpha):
    """atom = (a1,a2,b1,b2); returns scalar g(P,alpha)/E h(p)."""
    a1, a2, b1, b2 = atom
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0
    if not (a <= t < b):
        return 1e9
    if b <= a:
        return 1e9
    beta = (t - a) / (b - a)
    if not (0.0 <= beta <= 1.0):
        return 1e9
    wa = (1 - beta) / 2.0
    wb = beta / 2.0

    vals = [a1, a2, b1, b2]
    wts = [wa, wa, wb, wb]
    eh = sum(wts[i] * h(vals[i]) for i in range(4))
    if eh <= 0:
        return 1e9

    e_indep = sum(wts[i] * wts[j] * h(vals[i] + vals[j] - vals[i]*vals[j])
                  for i in range(4) for j in range(4))
    e_coup = 2*wa*h(phi1(a1, a2)) + 2*wb*h(phi1(b1, b2))
    g = (1-alpha)*e_indep + alpha*e_coup
    return g / eh


def inf_at(t, alpha, n_starts=30, seed=0):
    """Approximate global min over the feasible atom box."""
    rng = np.random.default_rng(seed)
    best = 1e9
    best_atom = None
    # structured starts: Yu subfamily sweep a in [0,t]
    for a in np.linspace(0.001, t*0.99, 12):
        for b2v in (1.0, 0.9, 0.8, t + 0.05):
            x0 = np.array([a, a, a, b2v])
            r = minimize(ratio, x0, args=(t, alpha), method="L-BFGS-B",
                         bounds=[(0, t), (0, t), (t+1e-9, 1), (t+1e-9, 1)])
            if r.fun < best:
                best = r.fun
                best_atom = r.x
    # random starts
    for _ in range(n_starts):
        a1, a2 = rng.uniform(0, t, 2)
        b1, b2 = rng.uniform(t, 1, 2)
        x0 = np.array([a1, a2, b1, b2])
        r = minimize(ratio, x0, args=(t, alpha), method="L-BFGS-B",
                     bounds=[(0, t), (0, t), (t+1e-9, 1), (t+1e-9, 1)])
        if r.fun < best:
            best = r.fun
            best_atom = r.x
    return best, best_atom


def main():
    for t in (0.370, 0.378, 0.380, 0.382, 0.38234, 0.383, 0.385):
        for alpha in (0.035,):
            best, atom = inf_at(t, alpha)
            a1, a2, b1, b2 = atom
            onsub = (abs(a1-a2) < 1e-6 and abs(b1-a1) < 1e-6 and abs(b2-1) < 1e-3)
            print(f"t={t:.6f} alpha={alpha}  inf~{best:.8f} "
                  f"atom=({a1:.6f},{a2:.6f},{b1:.6f},{b2:.6f}) onsub={onsub}")
    print("\n-- Yu's known values --")
    best, atom = inf_at(0.38234, 0.035)
    print(f"t=0.38234 alpha=0.035  inf~{best:.8f} atom=({atom[0]:.7f},{atom[1]:.7f},"
          f"{atom[2]:.7f},{atom[3]:.7f})")


if __name__ == "__main__":
    main()
