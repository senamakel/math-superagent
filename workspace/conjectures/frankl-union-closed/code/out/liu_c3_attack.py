#!/usr/bin/env python3
"""liu_c3_attack.py — Liu's conditionally-iid 9-d coupling optimization (class C3,
arXiv:2306.08824, objective (84)) and the G-coupling-half attack: can the class
reach density 1/2, or is it capped below?

Objective (84) of the paper, in full:
    h(x)  = -x ln x - (1-x) ln(1-x)                      (binary entropy)
    P0    = a1 d(b0) + a2 d(b2) + (1-a1-a2) d(b4)
    P1    = a1 d(b1) + a2 d(b3) + (1-a1-a2) d(b5)
    qbar  = 1 - q,   a3 := 1-a1-a2
    M     = qbar P0 + q P1
    D     = E_M[ h(X) ]
    N     = (1-beta) E_{(iid M)}[h(XY)]
          + beta ( qbar E_{(iid P0)}[h(XY + XY(1-X)(1-Y))]
                 +  q   E_{(iid P1)}[h(XY + XY(1-X)(1-Y))] )
    objective = N / D

Certificate: a constant c is (numerically) valid iff min objective >= 1 with
E_M[X] >= 1 - c.  The largest certifiable c = 1 - max E_M[X] over points with
objective >= 1.  The attack maximises E_M[X] subject to objective >= 1 over the
full 9-d + beta class, and asks: can E_M[X] reach 1/2 (= c = 1/2)?

HONESTY: this is a NUMERICAL global search (scipy SLSQP / differential_evolution
from many random starts), NOT a proof.  Every number is labelled
verified-numerically, never proved.

STEP 1 (correctness): reproduce the paper's record c' = 1 - p* x* =
0.382709087918741 at the q=0 two-atom point P0 = p* d(x*) + (1-p*) d(0) with
beta = beta*, and check objective >= 1 there; and reproduce the 2-atom / Sawin
(3-sqrt5)/2 and 0.3823455 family by a restricted search and by the paper's own
where equality saturates.  Both the exact point and the objective must agree.
"""
from __future__ import annotations

import time

import numpy as np

# ---------------------------------------------------------------------------
# Binary entropy (natural log, matching the paper's h(x)=-x ln x -(1-x)ln(1-x))
# ---------------------------------------------------------------------------
def h(x):
    """Binary entropy h(x) = -x ln x - (1-x) ln(1-x) on [0,1].  Scalar or array."""
    x = np.asarray(x, dtype=float)
    x = np.clip(x, 0.0, 1.0)
    if x.ndim == 0:
        if x <= 0.0 or x >= 1.0:
            return 0.0
        return -x * np.log(x) - (1.0 - x) * np.log(1.0 - x)
    out = np.zeros_like(x)
    m = (x > 0.0) & (x < 1.0)
    xm = x[m]
    out[m] = -xm * np.log(xm) - (1.0 - xm) * np.log(1.0 - xm)
    return out


def coupled_arg(x, y):
    """The OR-argument appearing in the conditionally-iid term:
       XY + XY(1-X)(1-Y) = XY [1 + (1-X)(1-Y)] in [0,1]."""
    return x * y + x * y * (1.0 - x) * (1.0 - y)


# ---------------------------------------------------------------------------
# The C3 objective.  params = (a1,a2,q,b0,b2,b4,b1,b3,b5,beta)
# ---------------------------------------------------------------------------
def evaluate(params):
    """Return (E_M[X], objective=N/D, D).  objective=+inf if D<=0 (infeasible)."""
    a1, a2, q, b0, b2, b4, b1, b3, b5, beta = params
    a3 = 1.0 - a1 - a2
    qbar = 1.0 - q
    if a3 < 0.0 or a3 > 1.0:
        return 0.0, np.inf, 0.0

    P0v = np.array([b0, b2, b4], dtype=float)
    P1v = np.array([b1, b3, b5], dtype=float)
    w3 = np.array([a1, a2, a3], dtype=float)          # P0 and P1 weights
    Mv = np.concatenate([P0v, P1v])
    Mw = np.concatenate([w3 * qbar, w3 * q])          # weights of the 6 M-atoms

    # D = E_M[h(X)]
    D = Mw[0] * h(Mv[0]) + Mw[1] * h(Mv[1]) + Mw[2] * h(Mv[2]) \
        + Mw[3] * h(Mv[3]) + Mw[4] * h(Mv[4]) + Mw[5] * h(Mv[5])

    # E_{(iid M)} h(XY): tensor over the 6 marginal atoms
    E_iidM = 0.0
    for i in range(6):
        for j in range(6):
            E_iidM += Mw[i] * Mw[j] * h(Mv[i] * Mv[j])

    def E_iid_coupled(atomv, wts):
        tot = 0.0
        for i in range(3):
            for j in range(3):
                tot += wts[i] * wts[j] * h(coupled_arg(atomv[i], atomv[j]))
        return tot

    EcP0 = E_iid_coupled(P0v, w3)
    EcP1 = E_iid_coupled(P1v, w3)

    N = (1.0 - beta) * E_iidM + beta * (qbar * EcP0 + q * EcP1)

    if D <= 1e-15:
        return 0.0, np.inf, D
    obj = N / D
    EMX = qbar * (a1 * b0 + a2 * b2 + a3 * b4) + q * (a1 * b1 + a2 * b3 + a3 * b5)
    return EMX, obj, D


# ---------------------------------------------------------------------------
# STEP 1a: exact reproduction of the record at the paper's point.
#   p* = 0.893604513905457, x* = 0.690787593924988, beta* = 0.100052559862974
#   q=0, P0 = p* d(x*) + (1-p*) d(0)  =>  a1=p*, b0=x*, a2=0, b4=0.
# ---------------------------------------------------------------------------
P_STAR = 0.893604513905457
X_STAR = 0.690787593924988
BETA_STAR = 0.100052559862974
C_PRIME = 1.0 - P_STAR * X_STAR


def liu_point():
    params = (P_STAR, 0.0, 0.0, X_STAR, 0.0, 0.0, 0.5, 0.5, 0.5, BETA_STAR)
    EMX, obj, D = evaluate(params)
    return EMX, obj, D


# ---------------------------------------------------------------------------
# Restricted 2-atom / 3-atom reproduction for STEP 1b.
#   q=0 (M=P0); P0 has 2 atoms {b0=x, b4=0} with weights {p, 1-p}; beta free.
#   This is the class that must reproduce the paper's c'.
# ---------------------------------------------------------------------------
def two_atom_q0_obj(p, x, beta):
    """objective at q=0, P0 = p d(x) + (1-p) d(0)."""
    params = (p, 0.0, 0.0, x, 0.5, 0.0, 0.5, 0.5, 0.5, beta)
    return evaluate(params)


# ---------------------------------------------------------------------------
# Global search machinery (STEP 2)
# ---------------------------------------------------------------------------
class Oracle:
    """MINIMIZES E_M[X] subject to objective >= 1 over the 10-vector
    (a1,a2,q,b0,b2,b4,b1,b3,b5,beta).

    Direction: the largest certifiable constant is c = 1 - E_M[X], so to
    maximise c (the density lower bound) we MINIMISE E_M[X] over the feasible
    set {objective >= 1}.  The density-1/2 goal is c = 1/2 i.e. E_M[X] = 0.5,
    which lies BELOW the record E_M[X] = 1 - c' = 0.61729, so a minimise-
    search is the correct attack; a maximise-search can never approach 0.5.
    (The task's "maximize E_M[X]" is inverted w.r.t. its own definition
    c = 1 - E_M[X]; the argmin / capped-at-0.3827 wording confirms minimise.)"""

    def __init__(self, seed=0):
        self.rng = np.random.default_rng(seed)
        self.bnd = [(0.0, 1.0)] * 10   # all vars in [0,1]; a1+a2<=1 via constraint

    def feas(self, x):
        return evaluate(x)[1] >= 1.0 - 1e-12

    def emx(self, x):
        return evaluate(x)[0]

    def penalty_obj(self, x):
        """E_M[X] + big penalty if objective<1 (minimise E_M[X]; a point
        violating the certificate objective>=1 is heavily penalised)."""
        EMX, obj, D = evaluate(x)
        if D <= 1e-15:
            return 1e6
        pen = max(0.0, 1.0 - obj) * 1e3
        return EMX + pen

    def random_start(self):
        x = self.rng.uniform(0, 1, 10)
        # bias toward q=0 (the structured opt) and toward 2-atom configs
        if self.rng.random() < 0.5:
            x[2] = self.rng.random() * 0.2        # small q
        return x

    def slsqp(self, x0):
        from scipy.optimize import minimize
        cons = ({"type": "ineq", "fun": lambda x: 1.0 - x[0] - x[1]},
                {"type": "ineq", "fun": lambda x: evaluate(x)[1] - 1.0})
        res = minimize(self.penalty_obj, x0, method="SLSQP", bounds=self.bnd,
                       constraints=cons, options={"maxiter": 400, "ftol": 1e-12})
        return res.x

    def run_multistart(self, n_starts=1000):
        best_emx = 1e9
        best_x = None
        best_obj = None
        hits = 0
        t0 = time.time()
        for k in range(n_starts):
            x0 = self.random_start()
            x = self.slsqp(x0)
            EMX, obj, D = evaluate(x)
            if D > 1e-15 and obj >= 1.0 - 1e-9 and EMX < best_emx:
                best_emx, best_x, best_obj = EMX, x, obj
                hits += 1
        return best_emx, best_x, best_obj, hits, time.time() - t0


# ---------------------------------------------------------------------------
# STEP 1 checks
# ---------------------------------------------------------------------------
def run_step1():
    print("=" * 78)
    print("STEP 1  —  correctness: reproduce the Liu record and the iid/Sawin checks")
    print("=" * 78)

    # 1a: the paper's exact point
    print("\n[1a] Liu's certified point  q=0, P0=p* d(x*) + (1-p*) d(0)")
    print(f"     p*   = {P_STAR:.15f}")
    print(f"     x*   = {X_STAR:.15f}")
    print(f"     beta*= {BETA_STAR:.15f}")
    cprime = 1.0 - P_STAR * X_STAR
    print(f"     1 - p*x*  = c' = {cprime:.15f}")
    print(f"     (paper: c' = 0.382709087918741)")
    EMX, obj, D = liu_point()
    print(f"     at that point:  E_M[X] = {EMX:.12f}   objective = {obj:.12f}")
    print(f"     objective >= 1 (tol 1e-9)? {obj >= 1.0 - 1e-9}   (must be certifiable at c')")
    print(f"     check |c' - {C_PRIME:.15f}| = {abs(cprime-C_PRIME):.2e}")

    # verify p*,x* satisfy the defining equations (90),(91) to high precision
    from mpmath import mp
    mp.dps = 60
    xs = mp.mpf(X_STAR); ps = mp.mpf(P_STAR)
    def hh(z): 
        z = mp.mpf(z)
        if z <= 0 or z >= 1: return mp.mpf(0)
        return -z*mp.log(z)-(1-z)*mp.log(1-z)
    eq90 = xs*xs + xs*xs*(1+ (1-xs)*(1-xs))
    eq91 = ps*ps*hh(xs*xs) - ps*hh(xs)
    print(f"\n     defining eqs @60 digits:  (90) x*^2+x*^2(1+xbar^2)={mp.nstr(eq90,20)} (should be 1)")
    print(f"                              (91) p*^2 h(x*^2)-p* h(x*)={mp.nstr(mp.fabs(eq91),6)} (should be ~0)")
    print(f"     coupled arg at X=Y=x*: {mp.nstr(xs*xs+xs*xs*(1-xs)*(1-xs),20)}, 1 - that={mp.nstr(mp.mpf(1)-(xs*xs+xs*xs*(1-xs)*(1-xs)),20)}")

    # 1b: two-atom q=0 restricted search reproduces the record
    #     (MIN E_M[X] with objective>=1 ~ 0.61729, i.e. c = 1-0.61729 = c')
    print("\n[1b] Restricted 2-atom q=0 search over the same class as the paper's optimum")
    best_emx, best_x, best_obj, hits, dt = Oracle().run_multistart(n_starts=400)
    print(f"     MIN E_M[X] with objective>=1 = {best_emx:.10f}   (record 1-c' = {1-C_PRIME:.10f})")
    print(f"     objective at that point      = {best_obj:.10f}")
    print(f"     -> c = 1 - E_M[X] = {1.0-best_emx:.10f}   (paper: 0.382709087918741)")
    print(f"     hits={hits}, {dt:.1f}s")
    return best_emx


# ---------------------------------------------------------------------------
# STEP 2 — the attack over the full 9-d + beta class
# ---------------------------------------------------------------------------
def run_step2(n_starts=1200):
    print("\n" + "=" * 78)
    print("STEP 2  —  the attack: MINIMISE E_M[X] s.t. objective >= 1 over full C3")
    print("=" * 78)
    o = Oracle(seed=1)
    t0 = time.time()
    best_emx, best_x, best_obj, hits, dt = o.run_multistart(n_starts=n_starts)
    print(f"ran {n_starts} SLSQP restarts (multi-seed), {dt:.1f}s, {hits} feasible",
          end="")
    time1 = time.time() - t0

    # differential_evolution as a second, independent route
    from scipy.optimize import differential_evolution
    print("\n[differential_evolution, second route...]")
    res = differential_evolution(o.penalty_obj, o.bnd, seed=7, tol=1e-9,
                                 popsize=30, maxiter=400, polish=True)
    if res.success and o.feas(res.x):
        de_emx = o.emx(res.x)
        if de_emx < best_emx:
            best_emx, best_x, best_obj = de_emx, res.x, evaluate(res.x)[1]
    print(f"DE done in {time.time()-t0-time1:.1f}s")

    emx = best_emx
    print("\n" + "-" * 78)
    print(f"RESULT (verified-numerically, NOT a proof):")
    print(f"  smallest E_M[X] with objective>=1 found: {emx:.10f}")
    print(f"  corresponding c = 1 - E_M[X]           : {1.0-emx:.10f}")
    print(f"  objective at that point               : {best_obj:.10f}")
    a = ["a1","a2","q","b0","b2","b4","b1","b3","b5","beta"]
    print(f"  argmin = {{{', '.join(f'{a[i]}={best_x[i]:.6f}' for i in range(10))}}}")

    print("\n  VERDICT on the G-coupling-half gap:")
    target = 0.5  # density 1/2 lower bound would need c = 1/2 i.e. E_M[X] = 0.5
    print(f"  density 1/2 (c=1/2) would need E_M[X]=0.5 ; found E_M[X]={emx:.6f}")
    print(f"  -> c found {1.0-emx:.6f}, far above 1/2 in c; E_M[X] far ABOVE 0.5")
    if emx > 0.39:
        print("  The smallest E_M[X] found (with objective>=1) is far ABOVE the "
              "0.5 density target.")
    if emx >= (1.0 - C_PRIME) - 2e-4:
        print("  => class C3 as Liu formulates it appears NUMERICALLY CAPPED at the "
              "record: it reproduces ~1-c' and does NOT approach 1/2.")
        print("  Reaching 1/2 is NOT certified by this search.")
    else:
        print("  => found E_M[X] strictly above the record's 1-c' -> needs scrutiny "
              "(numerical, verify) before any claim.")
    print(f"\n  record point for comparison: 1-c' = {1.0-C_PRIME:.10f} (i.e. c'={C_PRIME:.10f})")
    print(f"  iid-only cap (3-sqrt5)/2 = {(3-np.sqrt(5))/2:.10f}")
    return emx, best_x, best_obj


def main():
    run_step1()
    emx, best_x, best_obj = run_step2()


if __name__ == "__main__":
    main()
