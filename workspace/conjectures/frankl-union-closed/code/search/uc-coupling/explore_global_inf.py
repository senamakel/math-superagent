#!/usr/bin/env python3
"""Fine global numerical search of inf g(P,alpha)/Eh over the 4-param two-atom
class, to locate the true global minimizer (Yu says the optimum is on the
1-param subfamily a1=a2, b1=a2, b2=1). NON-rigorous — just to understand shape
and to tell me whether the certified boundary margin is really ~1e-5.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution


def h(x):
    x = np.clip(x, 0.0, 1.0)
    if x <= 0 or x >= 1:
        return 0.0
    return -x*np.log2(x) - (1-x)*np.log2(1-x)


def phi1(p, q):
    return float(np.median([max(p, q), 0.5, p + q]))


def ratio(a1, a2, b1, b2, t, alpha):
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0
    if not (a <= t < b):
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


def onsub(atom):
    a1, a2, b1, b2 = atom
    return abs(a1-a2) < 1e-5 and abs(b1-a1) < 1e-5 and abs(b2-1) < 1e-4


def global_inf(t, alpha):
    # Correct feasible region: a=(a1+a2)/2<=t, b=(b1+b2)/2>t, all in [0,1].
    # So a1,a2>=0 with a1+a2<=2t; b1,b2 in [0,1] with b1+b2>2t.
    def obj(x):
        a1, a2, b1, b2 = x
        if not (0 <= a1+a2 <= 2*t and b1+b2 > 2*t):
            return 1e12
        return ratio(a1, a2, b1, b2, t, alpha)
    best = 1e12
    best_atom = None
    # differential evolution over the full [0,1]^4 box (feasibility enforced in obj)
    res = differential_evolution(obj, [(0, 1), (0, 1), (0, 1), (0, 1)],
                                 tol=1e-12, polish=True, seed=1,
                                 maxiter=1000, popsize=25)
    if res.fun < best:
        best, best_atom = res.fun, res.x
    # local refine from the winner with the simplex/linear constraints
    from scipy.optimize import LinearConstraint
    cons = [LinearConstraint([[1, 1, 0, 0]], 0, 2*t),
            LinearConstraint([[0, 0, 1, 1]], 2*t, 2)]
    r = minimize(obj, best_atom, method="SLSQP", bounds=[(0, 1)]*4,
                 constraints=cons, options=dict(maxiter=3000))
    if r.fun < best:
        best, best_atom = r.fun, r.x
    return best, best_atom


def main():
    print("t, alpha, global_inf, atom, onsub")
    for t in [0.380, 0.381, 0.382, 0.3825, 0.38234, 0.383]:
        for alpha in [0.035]:
            v, atom = global_inf(t, alpha)
            print(f"t={t:.5f} a={alpha} inf~{v:.10f} atom=({atom[0]:.7f},{atom[1]:.7f},"
                  f"{atom[2]:.7f},{atom[3]:.7f}) onsub={onsub(atom)}")


if __name__ == "__main__":
    main()
