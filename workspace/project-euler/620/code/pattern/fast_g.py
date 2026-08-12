"""Robust fast g(c,s,p,q) via the f-crossing structure + G-sweeps.

Model (resp. tangency_enum.py winning variant sigma=eta=-1):
  Q_t(d) = (c-t)*B_t + (s+t)*G_t  (turns, real)
  B_t = atan2(y,x)/2pi, G_t = atan2(y,x-d)/2pi, centre at
  |OP|=R-rho_t, |SP|=r+rho_t, upper position.
  f(d) := Q_p(d) - Q_q(d) strictly increasing on (DL,DU) (checked per
  case); the two types mesh (residues congruent mod 1) iff f(d) in Z;
  arrangements = mirror-image-identified placements at each valid d ->
  g = #{m in Z : f(DL) < m < f(DU)}, each m crossed once.
"""
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
    g = geometry(c, s, t, d)
    if g is None:
        return None
    R, r, rho, a, b, x, y = g
    B = atan2(y, x) / (2 * pi)
    G = atan2(y, x - d) / (2 * pi)
    return B, G


def Q_t(c, s, t, d):
    ag = angles_turns(c, s, t, d)
    if ag is None:
        return None
    B, G = ag
    return (c - t) * B + (s + t) * G


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


def monotone_check(c, s, p, q, DL, DU, n=600):
    """Check Qp incr, Qq decr, f incr on (DL,DU); sample strictly inside."""
    if DU - DL <= mpf('1e-12'):
        return None
    eps = (DU - DL) / 100000
    ds = [DL + eps + (DU - DL - 2 * eps) * mpf(i) / n for i in range(n + 1)]
    qp, qq = [], []
    for d in ds:
        vp = Q_t(c, s, p, d)
        vq = Q_t(c, s, q, d)
        if vp is None or vq is None:
            return None
        qp.append(vp)
        qq.append(vq)
    f = [qp[i] - qq[i] for i in range(n + 1)]
    def bad(a):
        return sum(1 for i in range(1, len(a)) if a[i] < a[i - 1])
    return {
        'Qp_incr': bad(qp) == 0,
        'Qq_decr': bad(qq) == n,
        'f_incr': bad(f) == 0,
        'f0': f[0], 'f1': f[-1],
    }


def g_fast(c, s, p, q, verbose=False):
    DL, DU = bounds(c, s, p, q)
    if DL >= DU:
        return 0, [], "empty d range"
    diag = monotone_check(c, s, p, q, DL, DU)
    if diag is None:
        return 0, [], "geometry/None at samples"
    if not (diag['Qp_incr'] and diag['Qq_decr'] and diag['f_incr']):
        return 0, [], "monotonicity failed: %s" % (
            {k: v for k, v in diag.items() if isinstance(v, bool)},)
    f0, f1 = diag['f0'], diag['f1']
    mmin = int(floor(f0)) + 1
    mmax = int(ceil(f1)) - 1
    if mmin > mmax:
        return 0, [], "no integer levels in (%.6f, %.6f)" % (float(f0), float(f1))
    roots = []
    for m in range(mmin, mmax + 1):
        lo, hi = DL, DU
        flo = f0 - m
        fhi = f1 - m
        for _ in range(250):
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
    if verbose:
        for d, m, qp, qq in roots:
            print("   d=%.15f  f=%+d  Qp mod1=%.6f  Qq mod1=%.6f"
                  % (float(d), m, float(qp), float(qq)))
    return len(roots), roots, diag


def g_fast_flat(c, s, p, q):
    g, _, _ = g_fast(c, s, p, q)
    return g


def G_sum(n, verbose=False):
    total = 0
    rows = []
    for s in range(5, n - 10 + 1):
        for p in range(5, n - s - 5 + 1):
            for q in range(p + 1, n - s - p + 1):
                c = s + p + q
                g, roots, diag = g_fast(c, s, p, q)
                rows.append((c, s, p, q, g))
                total += g
    return total, rows


def main():
    print("=== G(16) ===")
    g16, rows16 = G_sum(16)
    print("G(16) = %d (oracle 9)  %s" % (g16, "AGREE" if g16 == 9 else "DISAGREE"))
    for row in rows16:
        print("   g(%d,%d,%d,%d) = %d" % row)

    print("\n=== G(20) ===")
    g20, rows20 = G_sum(20)
    print("G(20) = %d (oracle 205)  %s" % (g20, "AGREE" if g20 == 205 else "DISAGREE"))
    for row in rows20:
        print("   g(%2d,%2d,%2d,%2d) = %d" % row)
    bad = [r for r in rows20 if r[4] <= 0]
    print("non-positive rows:", len(bad))


if __name__ == "__main__":
    main()