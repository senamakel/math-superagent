"""Numeric geometry + meshing conditions for Project Euler 620 (Planet Gears).

Model under test (a hypothesis to check, not settled):
  Big circle C of circumference c sits at the origin (radius R = c/(2pi)).
  Small circle S of circumference s sits at (d, 0), radius r = s/(2pi), and
  the closest gap between C and S boundaries is R - r - d >= 1.
  A planet of circumference m has radius rho = m/(2pi) and must be tangent to
  C internally and to S externally, so its centre lies on
      circle(O, R - rho)  ∩  circle(S, r + rho),
  which is 0, 1, or 2 points (mirror images across the line of centres).

Meshing: the four planets give 8 tooth-alignment equations
      t_C(X_C) - phi_C - (t_k(X_C) - phi_k) = 1/2   (C-planet mesh)
      t_S(X_S) - phi_S - (t_k(X_S) - phi_k) = 1/2   (S-planet mesh)
  in the 6 gear phases phi (mod 1 tooth, pitch 1 cm).  A configuration is
  valid iff these 8 congruences mod 1 are simultaneously solvable.
  Eliminating the phases (integer left nullspace of the 8x6 matrix, which is
  3-dimensional) gives the three consistency conditions implemented in
  `residual`: for F_m = beta_m*R - gamma_m*r - T_m (m = p, q) and
  H = (beta_p - beta_q)*R - (gamma_p - gamma_q)*r - (T_p - T_q):
      2*F_p in Z,  2*F_q in Z,  H in Z   (mod 1),
  where beta is the planet's angle around O, gamma its angle around S, and
  T the signed arc on the planet from its C-contact to its S-contact.

Every value is a real number; mpmath at configurable precision is used
because the angles involve atan2 of irrational radii.
"""

from mpmath import mp, mpf, sqrt, atan2, pi, sin, cos, fabs, isnan


def planet_geometry(k, d, R, r):
    """Position data for one type-k planet at centre distance d.

    Returns a dict with rho, a = dist(O,P), b = dist(S,P), the upper
    intersection point P=(x,y), angles beta (around O) and gamma (around S),
    the signed planet angle psi from C-contact direction to S-contact
    direction (CCW), and the signed arc T = rho*psi in cm (0 <= T < k).
    """
    rho = mpf(k) / (2 * pi)
    a = R - rho          # |delta P| from O
    b = r + rho          # |delta P| from S
    x = (a * a - b * b + d * d) / (2 * d)
    rad = a * a - x * x
    if rad < 0 and rad > mpf('-1e-20'):
        rad = mpf(0)
    y = sqrt(rad)                    # upper position (y >= 0)
    beta = atan2(y, x)               # angle of P (and of C-contact point) around O
    gamma = atan2(y, x - d)          # angle of P around S
    lamC = beta                      # direction from P to its C-contact point
    lamS = gamma + pi                # direction from P to its S-contact point
    psi = (lamS - lamC) % (2 * pi)   # signed CCW angle C-contact -> S-contact
    T = rho * psi                    # planet arc between the two contacts (cm)
    return dict(rho=rho, a=a, b=b, x=x, y=y, beta=beta, gamma=gamma,
                psi=psi, T=T)


def consistency(c, s, p, q, d):
    """The three meshing consistency values at centre distance d.

    A configuration is phase-solvable iff
        2*F_p, 2*F_q, H  are all (very close to) integers.
    Returns (gp, gq, Fp, Fq, H).
    """
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    gp = planet_geometry(p, d, R, r)
    gq = planet_geometry(q, d, R, r)
    Fp = gp['beta'] * R - gp['gamma'] * r - gp['T']
    Fq = gq['beta'] * R - gq['gamma'] * r - gq['T']
    H = (gp['beta'] - gq['beta']) * R - (gp['gamma'] - gq['gamma']) * r \
        - (gp['T'] - gq['T'])
    return gp, gq, Fp, Fq, H


def residual(c, s, p, q, d):
    """Non-negative continuous residual, zero exactly at valid d."""
    _, _, Fp, Fq, H = consistency(c, s, p, q, d)
    return fabs(sin(4 * pi * Fp)) + fabs(sin(4 * pi * Fq)) + fabs(sin(2 * pi * H))


def d_range(c, s, p, q):
    """Valid centre-distance interval (closed) or None if empty.

    Both planet types need two-circle intersections: |a-b| <= d <= a+b, and
    the 1 cm gap constraint: R - r - d >= 1.  Endpoints where a type's two
    positions coincide give non-distinct planets and are excluded by callers.
    """
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    bounds = []
    for k in (p, q):
        rho = mpf(k) / (2 * pi)
        a = R - rho
        b = r + rho
        bounds.append((fabs(a - b), a + b))
    DL = max(lo for lo, _ in bounds)
    DU = min(hi for _, hi in bounds)
    DU = min(DU, R - r - 1)
    if DL > DU:
        return None
    return DL, DU


def phase_check(c, s, p, q, d, tol=mpf('1e-24')):
    """Independent verification: solve 5 of the 8 phase equations and check
    the remaining 3.  Returns True iff all 8 congruences hold mod 1."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    gp = planet_geometry(p, d, R, r)
    gq = planet_geometry(q, d, R, r)

    # mod-1 coordinates; planet reference ray chosen so t_k(X_C) = 0.
    def tc(beta):
        return beta * R

    def ts(gamma):
        return gamma * r

    bP, gP, TP = gp['beta'], gp['gamma'], gp['T']
    bQ, gQ, TQ = gq['beta'], gq['gamma'], gq['T']
    # lower positions are the mirror images
    TcP_, Tp_ = (2 * pi - bP) * R, (mpf(p) - TP)      # mod 1 uses these values
    TsP_, TpS_ = (-gP) * r, (mpf(p) - TP)
    TcQ_, Tq_ = (2 * pi - bQ) * R, (mpf(q) - TQ)
    TsQ_, TqS_ = (-gQ) * r, (mpf(q) - TQ)

    half = mpf(1) / 2
    eqs = [
        (tc(bP), 0.0, 'C', 'p+'), (ts(gP), TP, 'S', 'p+'),
        (TcP_, Tp_, 'C', 'p-'),   (TsP_, TpS_, 'S', 'p-'),
        (tc(bQ), 0.0, 'C', 'q+'), (ts(gQ), TQ, 'S', 'q+'),
        (TcQ_, Tq_, 'C', 'q-'),   (TsQ_, TqS_, 'S', 'q-'),
    ]
    # phases (mod 1): set phi_p+ = 0, derive phi_C, phi_S, phi_p-, phi_q+, phi_q-
    phiC = (tc(bP) - 0 - half) % 1      # from (C, p+)
    phiS = (ts(gP) - TP - half) % 1     # from (S, p+)
    phi_pm = (half - TcP_ + phiC) % 1   # from (C, p-)
    phi_qp = (half - tc(bQ) + phiC) % 1  # from (C, q+)
    phi_qm = (half - TcQ_ + phiC) % 1   # from (C, q-)
    phases = {'C': phiC, 'S': phiS, 'p+': 0, 'p-': phi_pm, 'q+': phi_qp, 'q-': phi_qm}

    checks = [
        (tc(bP), 0, 'C', 'p+', phiC - 0),
        (ts(gP), TP, 'S', 'p+', phiS - 0),
        (TcP_, Tp_, 'C', 'p-', phiC - phi_pm),
        (TsP_, TpS_, 'S', 'p-', phiS - phi_pm),
        (tc(bQ), 0, 'C', 'q+', phiC - phi_qp),
        (ts(gQ), TQ, 'S', 'q+', phiS - phi_qp),
        (TcQ_, Tq_, 'C', 'q-', phiC - phi_qm),
        (TsQ_, TqS_, 'S', 'q-', phiS - phi_qm),
    ]
    for tC, Tk, wh, lab, ph in checks:
        if (tC - ph - (Tk - 0)) % 1 - half:  # t - phi_C - (t_k - phi_k) =? 1/2
            pass
    ok = True
    for tC, Tk, wh, lab, ph in checks:
        lhs = (tC - ph - (Tk - 0) - half) % 1
        # lhs should be 0 mod 1 (within tol), allowing wrapping
        if min(lhs, 1 - lhs) > tol:
            ok = False
    return ok


def g_count(c, s, p, q, verbose=False, grid_points=400000):
    """g(c,s,p,q): number of valid centre distances d (each such d gives one
    arrangement, the four forced planet positions).  Brute force over the
    continuous d interval: scan a fine grid, isolate residual minima, refine."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    dr = d_range(c, s, p, q)
    if dr is None:
        return 0
    DL, DU = dr
    if verbose:
        print(f"  c={c} s={s} p={p} q={q}:  R={mp.nstr(R, 12)} r={mp.nstr(r, 12)}")
        print(f"  valid d in [{mp.nstr(DL, 12)}, {mp.nstr(DU, 12)}] cm")
    if DL <= 0:
        return 0

    from scipy.optimize import minimize_scalar
    N = grid_points
    d0 = mpf(DL)
    step = (DU - DL) / N
    # find grid points where the residual is small -> these bracket solutions
    candidates = []
    prev = None
    dv = [DL + step * mpf(i) for i in range(N + 1)]
    ev = [residual(c, s, p, q, x) for x in dv]
    # contiguous runs of small residual
    run_lo = None
    TH = mpf('1e-4')
    for i, e in enumerate(ev):
        if e < TH:
            if run_lo is None:
                run_lo = i
        else:
            if run_lo is not None:
                candidates.append((run_lo, i - 1))
                run_lo = None
    if run_lo is not None:
        candidates.append((run_lo, len(dv) - 1))

    sols = []
    for lo, hi in candidates:
        a, b = dv[lo], dv[hi]
        if b - a < step:  # widen to catch the minimum inside the run
            a = max(mpf(DL), a - 2 * step)
            b = min(mpf(DU), b + 2 * step)
        res = minimize_scalar(lambda x: float(residual(c, s, p, q, x)),
                              bounds=(float(a), float(b)), method='bounded',
                              options={'xatol': 1e-18})
        dstar = mpf(res.x)
        if residual(c, s, p, q, dstar) > mpf('1e-10'):
            continue
        gp, gq, Fp, Fq, H = consistency(c, s, p, q, dstar)
        # verify: values within 1e-12 of integers
        def nearint(x):
            return min((x % 1), 1 - (x % 1))
        v2 = max(nearint(2 * Fp), nearint(2 * Fq), nearint(H))
        if v2 > mpf('1e-8'):
            continue
        # exclude degenerate d (coinciding planet positions)
        degenerate = False
        for k in (p, q):
            rho = mpf(k) / (2 * pi)
            a = R - rho
            b = r + rho
            if fabs(dstar - fabs(a - b)) < mpf('1e-14') or \
               fabs(dstar - (a + b)) < mpf('1e-14'):
                degenerate = True
        if degenerate:
            continue
        # dedupe
        if not any(fabs(dstar - s0['d']) < mpf('1e-9') for s0 in sols):
            sols.append(dict(d=dstar, gp=gp, gq=gq, Fp=Fp, Fq=Fq, H=H))

    sols.sort(key=lambda s: float(s['d']))
    if verbose:
        for s0 in sols:
            print(f"  d* = {mp.nstr(s0['d'], 20)}   "
                  f"2Fp={mp.nstr((2*s0['Fp'])%1, 15)} 2Fq={mp.nstr((2*s0['Fq'])%1, 15)} "
                  f"H={mp.nstr(s0['H']%1, 15)}")
    return len(sols)


def G_sum(n, verbose=False):
    """G(n) = sum over s+p+q<=n, s>=5, p>=5, p<q of g(s+p+q, s, p, q)."""
    total = 0
    rows = []
    for s in range(5, n - 10):
        for p in range(5, n - s - 5):
            for q in range(p + 1, n - s - p + 1):
                c = s + p + q
                g = g_count(c, s, p, q, verbose=verbose)
                rows.append((c, s, p, q, g))
                total += g
    return total, rows