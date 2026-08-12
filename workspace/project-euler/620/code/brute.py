#!/usr/bin/env python3
"""Naive oracle for Project Euler 620 (Planet Gears).

Obvious-correctness over speed.  Reproduces the statement's worked examples
g(16,5,5,6)=9, G(16)=9, G(20)=205 before anything else is attempted.

Physical model
--------------
Ring C (internal gear), circumference c, radius R = c/(2pi), centred at O=(0,0).
Sun  S, circumference s, radius r = s/(2pi), centred at (d,0), off-centre by d.
A planet of circumference k (radius rho = k/(2pi)) is tangent internally to C
and externally to S, so its centre P satisfies
      |P - O| = R - rho   (= a),    |P - S| = r + rho   (= b).
For fixed d this is 0, 1 or 2 points.

Meshing (teeth at pitch 1 cm; "1/2" is tooth-to-groove alignment):
For each of the four planets, simultaneously:
    C-planet mesh:  t_C(Xc) - phi_C - (t_k(Xc) - phi_k) = 1/2   (mod 1)
    S-planet mesh:  t_S(Xs) - phi_S - (t_k(Xs) - phi_k) = 1/2   (mod 1)
in the six gear phases phi.  Algebraically eliminating the phases leaves,
for each planet type k, a doubled condition plus a cross condition:
      2*F_k in Z,   H in Z,   (mod 1)
where (with upper "+" planet of each type)
      F_k = R*beta_k - r*gamma_k + T_k
      H   = F_p - F_q
      beta_k = angle of P about O,  gamma_k = angle of P about S,
      T_k    = rho_k * (signed CCW arc on planet from C-contact to S-contact).

Each valid centre-distance d (the four forced planet positions) is ONE
arrangement, so g(c,s,p,q) = number of valid d in the allowed interval.

This is written explicitly so every symbol can be traced back to the
statement.  Uses mpmath (high precision) + scipy (isolate/refine zeros of the
residual).  Each found solution is re-verified by an independent direct
phase solve (see verify_solution).
"""
from mpmath import mp, mpf, sqrt, atan2, pi, sin, cos, fabs


def R_of(c):
    return mpf(c) / (2 * pi)


def planet_geometry(k, d, R, r):
    """Centre P, angles and arc for one type-k planet (upper, y>=0)."""
    rho = mpf(k) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    rad = a * a - x * x
    if rad < 0:                      # floating error at interval endpoints
        rad = mpf(0)
    y = sqrt(rad)
    beta = atan2(y, x)               # angle of P about O  (C-contact ray too)
    gamma = atan2(y, x - d)          # angle of P about S
    lamC = beta                      # P -> C-contact ray
    lamS = gamma + pi                # P -> S-contact ray
    psi = (lamS - lamC) % (2 * pi)   # CCW arc angle C-contact -> S-contact
    T = rho * psi
    return dict(rho=rho, a=a, b=b, x=x, y=y, beta=beta, gamma=gamma, psi=psi, T=T)


def d_interval(c, s, p, q):
    """Valid centre-distance interval (closed) or None."""
    R = R_of(c)
    r = R_of(s)
    bounds = []
    for k in (p, q):
        rho = mpf(k) / (2 * pi)
        a = R - rho
        b = r + rho
        bounds.append((fabs(a - b), a + b))
    DL = max(lo for lo, _ in bounds)
    DU = min(hi for _, hi in bounds)
    DU = min(DU, R - r - 1)          # closest gap between S and C >= 1 cm
    if DL > DU:
        return None
    return DL, DU


def F_and_H(c, s, p, q, d, T_sign=1):
    """(Fp, Fq) with H = Fp - Fq.  T_sign=+1 is the corrected sign."""
    R = R_of(c)
    r = R_of(s)
    gp = planet_geometry(p, d, R, r)
    gq = planet_geometry(q, d, R, r)
    def Fk(g):
        return g['beta'] * R - g['gamma'] * r + T_sign * g['T']
    return Fk(gp), Fk(gq)


def residual(c, s, p, q, d):
    """Non-negative; ~0 exactly at valid d (corrected +T sign)."""
    Fp, Fq = F_and_H(c, s, p, q, d, T_sign=1)
    H = Fp - Fq
    return fabs(sin(4 * pi * Fp)) + fabs(sin(4 * pi * Fq)) + fabs(sin(2 * pi * H))


def verify_solution(c, s, p, q, d, tol=mpf('1e-20')):
    """Independent check: directly solve the 8 phase equations and confirm all
    hold mod 1.  Returns True iff the 8 congruences are simultaneously
    consistent."""
    R = R_of(c)
    r = R_of(s)
    gp = planet_geometry(p, d, R, r)
    gq = planet_geometry(q, d, R, r)

    def tc(beta):
        return beta * R
    def ts(gamma):
        return gamma * r

    bP, gP, TP = gp['beta'], gp['gamma'], gp['T']
    bQ, gQ, TQ = gq['beta'], gq['gamma'], gq['T']
    # lower planets: mirror, T lower = k - T
    def m1(z):
        return z % 1

    # pick 5 phase unknowns from the 8 equations, solve, check the rest.
    # choose unknowns phi_C, phi_S, phi_{q+}, phi_{q-}, phi_{p-}; solve from
    # C,p+ ; S,p+ ; then derive the others and check the p-/q equations
    phiC = m1(tc(bP) - 0 - mpf(1) / 2)                       # C,p+
    phiS = m1(ts(gP) - TP - mpf(1) / 2)                      # S,p+
    phi_qp = m1(tc(bQ) - phiC + mpf(1) / 2)                  # C,q+
    phi_qm = m1(-tc(bQ) - phiC + mpf(1) / 2)                 # C,q-
    phi_pm = m1(-tc(bP) - phiC + mpf(1) / 2)                 # C,p-

    checks = [
        (-tc(bQ), mpf(q) - TQ, phiS, phi_qm, 'S,q-'),       # S,q- = 1/2
        (-tc(bP), mpf(p) - TP, phiS, phi_pm, 'S,p-'),       # S,p- = 1/2
        (ts(gQ), TQ, phiS, phi_qp, 'S,q+'),                 # S,q+ = 1/2
    ]
    for tS, Tk, phiS_, phik, lab in checks:
        # t_S - phi_S - (t_k - phi_k) =? 1/2
        lhs = (tS - phiS_ - (Tk - phik) - mpf(1) / 2) % 1
        if min(lhs, 1 - lhs) > tol:
            return False
    return True


def g_brute(c, s, p, q, grid_points=40000, verbose=True):
    """Number of valid centre distances (arrangements) for (c,s,p,q)."""
    mp.prec = 80
    R = R_of(c)
    r = R_of(s)
    dr = d_interval(c, s, p, q)
    if dr is None:
        return 0
    DL, DU = dr
    if verbose:
        print(f"  c={c} s={s} p={p} q={q}: d in "
              f"[{mp.nstr(DL, 12)}, {mp.nstr(DU, 12)}]")
    if DL <= 0:
        return 0
    from scipy.optimize import minimize_scalar
    N = grid_points
    step = (DU - DL) / N
    dv = [DL + step * mpf(i) for i in range(N + 1)]
    ev = [residual(c, s, p, q, x) for x in dv]
    TH = mpf('1e-3')
    runs = []
    lo = None
    for i, e in enumerate(ev):
        if e < TH:
            if lo is None:
                lo = i
        else:
            if lo is not None:
                runs.append((lo, i - 1)); lo = None
    if lo is not None:
        runs.append((lo, len(dv) - 1))

    sols = []
    for l, h in runs:
        a, b = dv[l], dv[h]
        if b - a < step:
            a = max(DL, a - 3 * step)
            b = min(DU, b + 3 * step)
        res = minimize_scalar(lambda x: float(residual(c, s, p, q, x)),
                              bounds=(float(a), float(b)), method='bounded',
                              options={'xatol': 1e-20})
        dst = mpf(res.x)
        if residual(c, s, p, q, dst) > mpf('1e-12'):
            continue
        # near-integer test on the corrected conditions
        def ni(x):
            return min(x % 1, 1 - (x % 1))
        Fp, Fq = F_and_H(c, s, p, q, dst, T_sign=1)
        if max(ni(2 * Fp), ni(2 * Fq), ni(Fp - Fq)) > mpf('1e-8'):
            continue
        if not verify_solution(c, s, p, q, dst):
            continue
        # reject degenerate d (coinciding planet positions)
        bad = False
        for k in (p, q):
            rho = mpf(k) / (2 * pi)
            a = R - rho
            b = r + rho
            if fabs(dst - fabs(a - b)) < mpf('1e-13') or \
               fabs(dst - (a + b)) < mpf('1e-13'):
                bad = True
        if bad:
            continue
        if not any(fabs(dst - s0) < mpf('1e-9') for s0 in sols):
            sols.append(dst)
    sols.sort(key=float)
    if verbose:
        for s0 in sols:
            print(f"    d* = {mp.nstr(s0, 22)}")
    return len(sols)


def G_brute(n, verbose=False):
    """G(n) = sum_{s+p+q<=n, s>=5, p>=5, p<q} g(s+p+q,s,p,q)."""
    total = 0
    for s in range(5, n - 10):
        for p in range(5, n - s - 5):
            for q in range(p + 1, n - s - p + 1):
                c = s + p + q
                g = g_brute(c, s, p, q, verbose=verbose)
                total += g
    return total


if __name__ == "__main__":
    print("g(16,5,5,6) =", g_brute(16, 5, 5, 6))
    print("G(16) =", G_brute(16))
    print("G(20) =", G_brute(20))
