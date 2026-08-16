"""
Yu's finite-dimensional optimization (Entropy 2023), implemented from the verbatim
transcription in research/notes/yu-optimization-verbatim.md.

Correctness check: reproduce Gamma_hat(0.38234) >= 1.00000889 at the paper's
certified point alpha=0.035, a1=a2=a=0.3300622, b1=a, b2=1.

Reference (paper, line 71-166 of the .full.md):
    phi(1,p,q) = median{ max{p,q}, 1/2, p+q }
    g(P_pq, alpha) = (1-alpha) E_{P_p^{otimes2}} h(p+q-pq) + alpha E_{P_pq} h(phi(1,p,q))
    Gamma_hat(t) = sup_alpha inf_{P_pq} g(P_pq, alpha) / E h(p)
    P_pq = (1-beta) Q_{a1,a2} + beta Q_{b1,b2},  Q_{x,y} = (1/2) d_{(x,y)} + (1/2) d_{(y,x)}
    a = (a1+a2)/2, b = (b1+b2)/2,  0 <= a <= t < b <= 1,  beta = (t-a)/(b-a) > 0
"""
from __future__ import annotations

import math

import numpy as np
from scipy.optimize import minimize

log2 = math.log2


def h(x: float) -> float:
    """Binary entropy, h(0)=h(1)=0 by convention."""
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def phi1(p: float, q: float) -> float:
    """phi(1,p,q) = median{ max{p,q}, 1/2, p+q } (multiset median)."""
    return float(np.median([max(p, q), 0.5, p + q]))


def g_at(alpha: float, a1: float, a2: float, b1: float, b2: float, t: float) -> float:
    """
    Evaluate g(P_pq, alpha) / E h(p) for the two-atom symmetric coupling
    P_pq = (1-beta) Q_{a1,a2} + beta Q_{b1,b2},  beta = (t-a)/(b-a).
    Returns +inf if the constraint set is violated or E h(p) == 0.
    """
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0
    if not (0.0 <= a <= t < b <= 1.0):
        return math.inf
    beta = (t - a) / (b - a)
    if not (0.0 < beta <= 1.0):
        return math.inf

    # joint P_pq atoms: (a1,a2),(a2,a1) each w=(1-beta)/2; (b1,b2),(b2,b1) each w=beta/2
    wa = (1.0 - beta) / 2.0
    wb = beta / 2.0

    # E h(p): marginal P_p atoms a1,a2 each wa; b1,b2 each wb
    eh = wa * (h(a1) + h(a2)) + wb * (h(b1) + h(b2))
    if eh <= 0.0:
        return math.inf

    # E_{P_p^{otimes 2}} h(p+q-pq): product of marginal with itself
    vals = [a1, a2, b1, b2]
    wts = [wa, wa, wb, wb]
    e_indep = 0.0
    for i in range(4):
        for j in range(4):
            p, q = vals[i], vals[j]
            e_indep += wts[i] * wts[j] * h(p + q - p * q)

    # E_{P_pq} h(phi(1,p,q))
    e_coupled = wa * (h(phi1(a1, a2)) + h(phi1(a2, a1))) + wb * (h(phi1(b1, b2)) + h(phi1(b2, b1)))

    g = (1.0 - alpha) * e_indep + alpha * e_coupled
    return g / eh


def reproduce_paper_point() -> None:
    """Check the paper's certified point: should give ~= 1.00000889."""
    alpha = 0.035
    a = 0.3300622
    t = 0.38234
    val = g_at(alpha, a, a, a, 1.0, t)
    # also check beta matches the paper's 0.1560676
    b = (a + 1.0) / 2.0
    beta = (t - a) / (b - a)
    print(f"paper point: alpha={alpha}, a={a}, b1=a, b2=1, t={t}")
    print(f"  beta = {beta:.7f} (paper: 0.1560676)")
    print(f"  Gamma_hat(t) >= {val:.8f} (paper: 1.00000889)")
    return val


def minimize_over_coupling(alpha: float, t: float, n_starts: int = 24) -> float:
    """
    inf over (a1,a2,b1,b2) of g/Eh for fixed alpha,t, with the constraint
    0 <= a=(a1+a2)/2 <= t < b=(b1+b2)/2 <= 1.  Multi-start box+constraint search.
    """
    best = math.inf
    rng = np.random.default_rng(0)

    def obj(x):
        a1, a2, b1, b2 = x
        return g_at(alpha, a1, a2, b1, b2, t)

    # inequality constraints (scipy >=0 means feasible):
    #   a <= t   ->  t - (a1+a2)/2 >= 0
    #   b >  t   ->  (b1+b2)/2 - t >= eps
    eps = 1e-6
    cons = (
        {"type": "ineq", "fun": lambda x: t - (x[0] + x[1]) / 2.0},
        {"type": "ineq", "fun": lambda x: (x[2] + x[3]) / 2.0 - t - eps},
    )
    bounds = [(0.0, 1.0)] * 4

    for _ in range(n_starts):
        x0 = rng.uniform(0.0, 1.0, 4)
        # make a feasible start: a in [0,t], b in (t,1]
        x0[0], x0[1] = rng.uniform(0, t, 2)
        x0[2], x0[3] = rng.uniform(t, 1.0, 2)
        res = minimize(obj, x0, method="SLSQP", bounds=bounds, constraints=cons,
                       options={"maxiter": 2000, "ftol": 1e-14})
        if res.success and np.isfinite(res.fun) and res.fun < best:
            best = res.fun
    return best


def gamma_hat(t: float, alpha_grid: int = 61, n_starts: int = 12) -> tuple[float, float]:
    """Gamma_hat(t) = sup_alpha inf_coupling g/Eh.  Returns (value, optimal alpha)."""
    best_val = -math.inf
    best_alpha = math.nan
    for alpha in np.linspace(0.0, 1.0, alpha_grid):
        inf_val = minimize_over_coupling(alpha, t, n_starts=n_starts)
        if inf_val > best_val:
            best_val = inf_val
            best_alpha = alpha
    return best_val, best_alpha


if __name__ == "__main__":
    reproduce_paper_point()
