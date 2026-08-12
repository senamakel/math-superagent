"""Fast g(c,s,p,q) from the f-curve structure.

Model = winning variant (sigma=eta=-1) of tangency_enum.py:
  Q_t(d) = (c-t)*B_t(d) + (s+t)*G_t(d)  (turns, real, not modded)
  B_t = angle about O of planet centre /2pi, G_t = angle about S /2pi,
  with the centre at the intersection of |OP|=R-rho_t, |SP|=r+rho_t.

Structurally observed on (16,5,5,6) and verified here per case:
  Q_p strictly increasing, Q_q strictly decreasing, f = Qp - Qq strictly
  increasing on (DL, DU); the upper residues repeat mod 1 ->
  g = number of integers m with f(DL) < m < f(DU), and each crossing d
  satisfies Q_p == Q_q (mod 1) exactly (UU/LL combos mesh).

Also compute (for the solver's benefit) the reading-A (mirror-pair)
counts under the two candidate phase models:
  M1 (enumeration Q model): 2Qp in Z, 2Qq in Z, Qp-Qq in Z  (mod 1)
  M2 (offcentre W model):    2U_p in Z, 2U_q in Z, W_p-W_q in Z (mod 1),
  U_t = s*phi_t + c*chi_t, W_t = U_t - t*gamma_t, phi/chi/gamma = the
  triangle angles at S/C/P in turns.
"""
import itertools
import numpy as np
from mpmath import mp, mpf, pi, atan2, sqrt, fabs, floor, ceil

mp.dps = 60


def geometry(c, s, t, d):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(t) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None
    y = sqrt(y2)
    return R, r, rho, a, b, x, y


def angles_turns(c, s, t, d):
    """(B, G): B=atan2(y,x)/2pi about O, G=atan2(y,x-d)/2pi about S."""
    g = geometry(c, s, t, d)
    if g is None:
        return None
    R, r, rho, a, b, x, y = g
    B = atan2(y, x) / (2 * pi)
    G = atan2(y, x - d) / (2 * pi)
    return B, G


def Q_t(c, s, t, d):
    """Enumeration-model residue (turns, real): (c-t)*B + (s+t)*G."""
    ag = angles_turns(c, s, t, d)
    if ag is None:
        return None
    B, G = ag
    return (c - t) * B + (s + t) * G


def triangle_angles_turns(c, s, t, d):
    """(phi, chi, gamma) at S, C, P (turns).  P at upper position."""
    g = geometry(c, s, t, d)
    if g is None:
        return None
    R, r, rho, a, b, x, y = g
    # triangle OSP: |OP|=a, |SP|=b, |OS|=d
    cosphi = (b * b + d * d - a * a) / (2 * b * d)   # at S, between SO and SP
    coschi = (a * a + d * d - b * b) / (2 * a * d)   # at O (C), between OC and OP
    cosgam = (a * a + b * b - d * d) / (2 * a * b)   # at P
    phi = mp.acos(cosphi) / (2 * pi)
    chi = mp.acos(coschi) / (2 * pi)
    gamma = mp.acos(cosgam) / (2 * pi)
    return phi, chi, gamma


def bounds(c, s, p, q):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    lo = []
    hi = []
    for t in (p, q):
        rho = mpf(t) / (2 * pi)
        a, b = R - rho, r + rho
        lo.append(abs(a - b))
        hi.append(a + b)
    DL = max(lo)
    DU = min(hi + [R - r - 1])
    return DL, DU


def monotone_check(c, s, p, q, DL, DU, n=400):
    """Verify strict monotonicity of Qp (incr), Qq (decr), f (incr)."""
    ds = [DL + (DU - DL) * mpf(i) / n for i in range(n + 1)]
    qp = [Q_t(c, s, p, d) for d in ds]
    qq = [Q_t(c, s, q, d) for d in ds]
    f = [qp[i] - qq[i] for i in range(n + 1)]
    def bad(a):
        return sum(1 for i in range(1, len(a)) if a[i] < a[i - 1])
    return (bad(qp) == 0, bad(qq) == n, bad(f) == 0,
            qp[0], qp[-1], qq[0], qq[-1], f[0], f[-1])


def g_fast(c, s, p, q, verbose=False):
    """g = count of integers strictly between f(DL) and f(DU).
    Returns (g, roots, diagnostics)."""
    DL, DU = bounds(c, s, p, q)
    if DL >= DU:
        return 0, [], "empty d range"
    diag = monotone_check(c, s, p, q, DL, DU)
    if not (diag[0] and diag[2]):
        return 0, [], "monotonicity FAILED: %s" % (diag,)
    f0, f1 = diag[7], diag[8]
    mmin = int(mp.floor(f0)) + 1
    mmax = int(mp.ceil(f1)) - 1
    if mmin > mmax:
        return 0, [], "no integer levels in (%.6f, %.6f)" % (float(f0), float(f1))

    roots = []
    for m in range(mmin, mmax + 1):
        # bisect f(d) = m on (DL, DU)
        lo, hi = DL, DU
        flo = f0 - m
        fhi = f1 - m
        for _ in range(200):
            mid = (lo + hi) / 2
            fm = Q_t(c, s, p, mid) - Q_t(c, s, q, mid) - m
            if fm == 0:
                break
            if (flo < 0) != (fm < 0):
                hi, fhi = mid, fm
            else:
                lo, flo = mid, fm
        d = (lo + hi) / 2
        qp = Q_t(c, s, p, d) % 1
        qq = Q_t(c, s, q, d) % 1
        roots.append((d, m, qp, qq))
    g = len(roots)
    if verbose:
        for d, m, qp, qq in roots:
            print("   d=%.15f  f-level=%+d  Qp mod1=%.10f  Qq mod1=%.10f"
                  % (float(d), m, float(qp), float(qq)))
    return g, roots, diag


def g_readingA(c, s, p, q, model=1, nscan=400000, verbose=False):
    """Reading A (mirror pairs, distinct circles) root counts by dense scan +
    local bisection.  model=1: enumeration Q residue; model=2: W invariant."""
    DL, DU = bounds(c, s, p, q)
    if DL >= DU:
        return 0, []
    ds = [DL + (DU - DL) * mpf(i) / nscan for i in range(nscan + 1)]
    if model == 1:
        def conds_at(d):
            qp = Q_t(c, s, p, d)
            qq = Q_t(c, s, q, d)
            return (2 * qp) % 1, (2 * qq) % 1, (qp - qq) % 1
    else:
        def conds_at(d):
            try:
                ap = triangle_angles_turns(c, s, p, d)
                aq = triangle_angles_turns(c, s, q, d)
                Up = s * ap[0] + c * ap[1]
                Uq = s * aq[0] + c * aq[1]
                Wp = Up - p * ap[2]
                Wq = Uq - q * aq[2]
                return (2 * Up) % 1, (2 * Uq) % 1, (Wp - Wq) % 1
            except Exception:
                return mpf('0.4'), mpf('0.4'), mpf('0.4')

    def resid(d):
        a, b, cc = conds_at(d)
        return max(min(a, 1 - a), min(b, 1 - b), min(cc, 1 - cc))

    # coarse scan for dips
    r = np.array([float(resid(d)) for d in ds])
    tol = 1e-6
    idx = np.where(r < tol)[0]
    clusters = []
    for i in idx:
        if clusters and i - clusters[-1][-1] <= 2:
            clusters[-1].append(i)
        else:
            clusters.append([i])
    sols = []
    for cl in clusters:
        j = cl[int(np.argmin(r[cl]))]
        d0 = float(ds[j])
        # bisection: find sign changes of each condition near d0
        # simplify: golden-section minimize resid on [d0-5h, d0+5h], h=step
        step = float((DU - DL) / nscan)
        lo, hi = d0 - 8 * step, d0 + 8 * step
        for _ in range(120):
            m1 = (lo + hi) / 2
            m2 = (lo + 2 * hi) / 3 
            # trisection on [lo,hi] using resid at thirds
            a = (2 * lo + hi) / 3
            b = (lo + 2 * hi) / 3
            ra = resid(mpf(a))
            rb = resid(mpf(b))
            if ra < rb:
                hi = b
            else:
                lo = a
        d = (lo + hi) / 2
        rr = resid(d)
        if rr < 1e-11:
            sols.append((d, rr))
    # dedupe
    uniq = []
    for d, rr in sols:
        if not uniq or fabs(d - uniq[-1][0]) > mpf('1e-7'):
            uniq.append((d, rr))
    if verbose:
        for d, rr in uniq:
            a, b, cc = conds_at(d)
            print("   d=%.15f res=%.1e  2Qp=%+.6f 2Qq=%+.6f diff=%+.6f"
                  % (float(d), float(rr), float(a), float(b), float(cc)))
    return len(uniq), uniq


def G_sum(n, verbose=False):
    total = 0
    rows = []
    for s in range(5, n - 10 + 1):
        for p in range(5, n - s - 5 + 1):
            for q in range(p + 1, n - s - p + 1):
                c = s + p + q
                g, roots, diag = g_fast(c, s, p, q)
                rows.append((c, s, p, q, g, diag))
                total += g
    return total, rows


def main():
    print("=== fast f-crossing model ===")
    g, roots, diag = g_fast(16, 5, 5, 6, verbose=True)
    print("g(16,5,5,6) = %d  (oracle 9)  diag=%s" % (g, diag))

    print("\n=== reading-A mirror-pair counts (for the solver) ===")
    for model, name in ((1, "enum Q residue"), (2, "W invariant")):
        n, sols = g_readingA(16, 5, 5, 6, model=model, verbose=False)
        print("  model %s: g = %d" % (name, n))

    print("\n=== G(16) ===")
    g16, rows16 = G_sum(16)
    print("G(16) = %d  (oracle 9)" % g16)
    for row in rows16:
        print("   g(%d,%d,%d,%d) = %d  %s" % row)

    print("\n=== G(20) ===")
    g20, rows20 = G_sum(20)
    print("G(20) = %d  (oracle 205)" % g20)
    for row in rows20:
        print("   g(%2d,%2d,%2d,%2d) = %d  %s" % row)

    # all-positive rows check
    bad = [r for r in rows20 if r[4] <= 0]
    print("non-positive rows under f-model:", len(bad))


if __name__ == "__main__":
    main()