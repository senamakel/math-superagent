"""
Scan driver for Yu's Gamma_hat(t) toward 1/2.

For each t in an evenly spaced range this computes
    Gamma_hat(t) = sup_{alpha in [0,1]} inf_{4-param coupling} g(P_pq,alpha)/E h(p)
using the existing minimize_over_coupling logic in yu_optimization.py but with a
variant that ALSO returns the argmin coupling (a1,a2,b1,b2) for the optimal alpha.

Usage:
    python yu_scan_driver.py T_START T_STOP T_STEP ALPHA_GRID N_STARTS CAPTURE

Rows are appended to CAPTURE. Each row:  t  Gamma_hat(t)  alpha*  a1 a2 b1 b2
Also prints each row to stdout.

This is a one-off probe (the task says not to modify lib); the minimize logic is
copied here so it can return argmin without touching the shared module.
"""
import math
import sys

import numpy as np
from scipy.optimize import minimize

from yu_optimization import h, phi1, g_at


def inf_over_coupling(alpha, t, n_starts):
    """min g/Eh over (a1,a2,b1,b2); returns (value, best_params)."""
    best = math.inf
    best_x = None
    rng = np.random.default_rng(0)

    def obj(x):
        return g_at(alpha, x[0], x[1], x[2], x[3], t)

    eps = 1e-6
    cons = (
        {"type": "ineq", "fun": lambda x: t - (x[0] + x[1]) / 2.0},
        {"type": "ineq", "fun": lambda x: (x[2] + x[3]) / 2.0 - t - eps},
    )
    bounds = [(0.0, 1.0)] * 4

    for _ in range(n_starts):
        x0 = np.empty(4)
        x0[0], x0[1] = rng.uniform(0, t, 2)
        x0[2], x0[3] = rng.uniform(t, 1.0, 2)
        res = minimize(obj, x0, method="SLSQP", bounds=bounds, constraints=cons,
                       options={"maxiter": 2000, "ftol": 1e-14})
        if res.success and np.isfinite(res.fun) and res.fun < best:
            best = res.fun
            best_x = res.x.copy()
    return best, best_x


def gamma_hat_full(t, alpha_grid, n_starts):
    """Return (Gamma_hat(t), alpha*, a1,a2,b1,b2 at the sup)."""
    best_val = -math.inf
    best_alpha = math.nan
    best_params = None
    for alpha in np.linspace(0.0, 1.0, alpha_grid):
        inf_val, x = inf_over_coupling(alpha, t, n_starts)
        # skip alphas where no feasible coupling was found (x is None -> inf)
        if x is None or not math.isfinite(inf_val):
            continue
        if inf_val > best_val:
            best_val = inf_val
            best_alpha = alpha
            best_params = x
    return best_val, best_alpha, best_params


def main():
    t_start, t_stop, t_step = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    alpha_grid = int(sys.argv[4])
    n_starts = int(sys.argv[5])
    capture = sys.argv[6]

    n = int(round((t_stop - t_start) / t_step)) + 1
    ts = [t_start + i * t_step for i in range(n)]

    with open(capture, "a") as f:
        for t in ts:
            val, alp, x = gamma_hat_full(t, alpha_grid, n_starts)
            xstr = " ".join(f"{v:.9f}" for v in x)
            row = f"{t:.6f}  {val:.8f}  alpha*={alp:.4f}  ({xstr})"
            print(row)
            f.write(row + "\n")
            f.flush()


if __name__ == "__main__":
    main()
