"""
Confirm the collapse extremal precisely and check it is the true inf at t=1/2.

Key structural facts (to verify):
  1. Collapse value at t=1/2, a=(3-sqrt5)/2: ratio = w1 = 1 - beta/2, and
     beta=a at t=1/2, giving exactly (1+sqrt5)/4 = phi/2.  Exact derivation:
       - 2a-a^2 = 1-a  (a root of x^2-3x+1=0), so h(2a-a^2)=h(a)
       - numerator = w1^2 h(2a-a^2) = w1^2 h(a); denom = w1 h(a); ratio = w1
       - w1 = (1-beta)+beta/2 = 1 - beta/2
       - beta(t=1/2) = (1/2-a)/(b-a) with b=(1+a)/2  == a  (check)
       - ratio = 1 - a/2 = 1 - (3-sqrt5)/4 = (1+sqrt5)/4 = phi/2
  2. Full 4-param numeric inf at t=1/2 equals phi/2 (matches scan 0.80901699).
"""
import math

log2 = math.log2


def h(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def phi1(p, q):
    return sorted([max(p, q), 0.5, p + q])[1]


def ratio_full(a1, a2, b1, b2, t, alpha):
    """g(P_pq, alpha)/E h(p) for the 2-atom symmetric coupling."""
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0
    if not (0.0 <= a <= t < b <= 1.0):
        return math.inf
    beta = (t - a) / (b - a)
    if not (0.0 < beta <= 1.0):
        return math.inf
    wa = (1.0 - beta) / 2.0
    wb = beta / 2.0
    vals = [a1, a2, b1, b2]
    wts = [wa, wa, wb, wb]
    eh = sum(wts[i] * h(vals[i]) for i in range(4))
    if eh <= 0:
        return math.inf
    e_indep = 0.0
    for i in range(4):
        for j in range(4):
            e_indep += wts[i] * wts[j] * h(vals[i] + vals[j] - vals[i] * vals[j])
    e_coupled = wa * (h(phi1(a1, a2)) + h(phi1(a2, a1))) + wb * (h(phi1(b1, b2)) + h(phi1(b2, b1)))
    g = (1.0 - alpha) * e_indep + alpha * e_coupled
    return g / eh


def main():
    a = (3.0 - math.sqrt(5)) / 2.0
    b = (1.0 + a) / 2.0
    t = 0.5

    # 1. exact derivation check
    beta = (t - a) / (b - a)
    w1 = (1 - beta) + beta / 2.0
    print("=== exact derivation at t=1/2, a=(3-sqrt5)/2 ===")
    print(f"  beta = (1/2-a)/(b-a)  = {beta:.12f}")
    print(f"  beta == a ?           : {abs(beta-a) < 1e-14}  (beta={beta}, a={a})")
    print(f"  ratio = 1 - beta/2    = {1 - beta/2:.12f}")
    print(f"  phi/2 = (1+sqrt5)/4   = {(1+math.sqrt(5))/4:.12f}")
    print(f"  matched to 1e-12      : {abs((1-beta/2)-(1+math.sqrt(5))/4)<1e-12}")
    print(f"  alpha=0 full eval     : {ratio_full(a,a,1.0,a,0.5,0.0):.12f}")

    # 2. brute inf over full 4-param family at t=1/2 (grid), alpha=0 and alpha>0
    print("\n=== full-4-param inf at t=1/2 over an alpha grid ===")
    import numpy as np
    from scipy.optimize import minimize
    rng = np.random.default_rng(1)
    for alpha in [0.0, 0.05, 0.1, 0.2]:
        best = math.inf
        for _ in range(60):
            x0 = np.empty(4)
            x0[0:2] = rng.uniform(0, t, 2)
            x0[2:4] = rng.uniform(t, 1.0, 2)
            cons = ({"type": "ineq", "fun": lambda x: t - (x[0]+x[1])/2},
                    {"type": "ineq", "fun": lambda x: (x[2]+x[3])/2 - t - 1e-6})
            res = minimize(lambda x: ratio_full(*x, t, alpha), x0,
                           method="SLSQP", bounds=[(0,1)]*4, constraints=cons,
                           options={"maxiter":2000,"ftol":1e-13})
            if res.success and res.fun < best:
                best = res.fun
        print(f"  alpha={alpha:.2f}: inf = {best:.12f}")


if __name__ == "__main__":
    main()
