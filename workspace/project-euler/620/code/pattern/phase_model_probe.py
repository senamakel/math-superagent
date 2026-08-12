"""Probe: idler-phase model of PE620 meshing, tested against the oracle.

Derivation (pattern_finder, scratch note 'Phase-condition derivation'):
  Arrangement: ring fixed at O (radius R=c/2pi), sun at (d,0) radius r=s/2pi.
  A planet of size k (radius rho=k/2pi) tangent to both has centre P_k with
      |OP| = a_k = R-rho_k,  |SP| = b_k = r+rho_k
  so  x_k = (a_k^2 - b_k^2 + d^2)/(2d),  y_k = +/- sqrt(a_k^2 - x_k^2).
  Two planets of the same size MUST be the mirror pair (x_k, +/-y_k) (same
  |OP|-|SP| <=> same x), so an arrangement is exactly a choice of d.

  Each planet is a free idler: its spin orientation psi_k is a free
  variable, so its ring-contact congruence fixes psi_k mod 1 without
  constraining the arrangement, and its sun-contact congruence then forces
  the shared sun orientation phi_S to satisfy (arc units, mod 1 pitch):
      r*phi_S = (r + eps*rho_k)*gamma_k + eps*(R-rho_k)*beta_k  (mod 1)
  where beta_k = angle of P_k about O, gamma_k = angle of P_k about S,
  and eps = +/-1 is the external-meshing arc-sign convention.
  All four planets share phi_S, so the conditions are:
      (1) 2*B_p in Z,   (2) 2*B_q in Z,   (3) B_p - B_q in Z   (mod 1)
  with  B_k(eps) = (r + eps*rho_k)*gamma_k + eps*(R-rho_k)*beta_k.

  The previous models used F = R*beta - r*gamma +- rho*psi (with a
  planet-pitch-arc term) and forced positions onto angular lattices about a
  single centre; both returned 0.  This model has NO free lattice: the
  discreteness comes purely from roots of the phase congruences in d, and
  the planet-arc term cancels because the idler spin is free.

  g(c,s,p,q) = number of d in (DL, DU] satisfying (1)-(3) exactly, with
  DL = max_k |a_k - b_k|, DU = min(R + r, R - r - 1) = R - r - 1.
  Endpoint d = DL is excluded (both sizes are axially degenerate there, so
  the two planets of each size coincide -> not four distinct circles).

  Oracle: g(16,5,5,6)=9, G(16)=9, G(20)=205.
"""
import math
import time
import numpy as np
from mpmath import mp, mpf, atan2, sqrt, fabs

mp.dps = 60
OUTFILE = "/workspace/code/out/phase_model_test.txt"


def geom(c, s, p, q):
    """(R, r, rho_p, rho_q, a_p, b_p, a_q, b_q, DL, DU)."""
    R = c / (2 * math.pi)
    r = s / (2 * math.pi)
    rp, rq = p / (2 * math.pi), q / (2 * math.pi)
    ap, bp = R - rp, r + rp
    aq, bq = R - rq, r + rq
    DL = max(abs(ap - bp), abs(aq - bq))
    DU = R - r - 1.0        # 1cm closest S-C boundary gap
    return R, r, rp, rq, ap, bp, aq, bq, DL, DU


def resid(np_d, c, s, p, q, eps):
    """Vectorised residual over an array of d values (float64, first pass)."""
    R, r, rp, rq, ap, bp, aq, bq, DL, DU = geom(c, s, p, q)
    # bprime = r + eps*rho
    bpp = r + eps * rp
    bpq = r + eps * rq
    d = np.asarray(np_d, dtype=np.float64)

    def B(a, b, bp_, ):
        x = (a * a - b * b + d * d) / (2.0 * d)
        y2 = np.clip(a * a - x * x, 0.0, None)
        y = np.sqrt(y2)
        beta = np.arctan2(y, x)
        gamma = np.arctan2(y, x - d)
        return bp_ * gamma + eps * a * beta

    Bp = B(ap, bp, bpp)
    Bq = B(aq, bq, bpq)
    d1 = lambda v: np.minimum(v % 1.0, 1.0 - (v % 1.0))
    res = np.maximum(d1(2 * Bp), np.maximum(d1(2 * Bq), d1(Bp - Bq)))
    return res


def refine(d0, c, s, p, q, eps, halfwidth=1e-4):
    """Refine the residual minimum near d0 with mpmath golden-section."""
    dL = mpf(d0) - mpf(halfwidth)
    dU = mpf(d0) + mpf(halfwidth)
    # crude: dense mpmath scan of the window then take the best
    Nw = 4000
    best = None
    for i in range(Nw + 1):
        dv = dL + (dU - dL) * mpf(i) / Nw
        res = resid_mp(dv, c, s, p, q, eps)
        if best is None or res < best[1]:
            best = (dv, res)
    return best


def resid_mp(d, c, s, p, q, eps):
    """Residual at one d (mpmath)."""
    R, r, rp, rq, ap, bp, aq, bq, DL, DU = geom(c, s, p, q)
    bpp = r + eps * rp
    bpq = r + eps * rq

    def B(a, b, bp_):
        x = (a * a - b * b + d * d) / (2 * d)
        y2 = a * a - x * x
        if y2 < 0:
            return None
        y = sqrt(y2)
        beta = atan2(y, x)
        gamma = atan2(y, x - d)
        return bp_ * gamma + eps * a * beta

    Bp, Bq = B(ap, bp, bpp), B(aq, bq, bpq)
    if Bp is None or Bq is None:
        return None
    d1 = lambda v: min(v % 1, 1 - (v % 1))
    return max(d1(2 * Bp), d1(2 * Bq), d1(Bp - Bq))


def g_count(c, s, p, q, eps, nscan=600000, tol_lo=1e-3, tol_hi=1e-13,
            verbose=True):
    R, r, rp, rq, ap, bp, aq, bq, DL, DU = geom(c, s, p, q)
    if DL >= DU:
        return 0, []
    d = np.linspace(DL, DU, nscan)
    res = resid(d, c, s, p, q, eps)
    # clusters: points below tol_lo
    idx = np.where(res < tol_lo)[0]
    clusters = []
    for i in idx:
        if clusters and i - clusters[-1][-1] <= 3:
            clusters[-1].append(i)
        else:
            clusters.append([i])
    valid = []
    for cl in clusters:
        j = cl[np.argmin(res[cl])]
        d0 = float(d[j])
        dv, rv = refine(d0, c, s, p, q, eps)
        if rv < tol_hi:
            valid.append((dv, rv))
    # dedupe
    uniq = []
    for dv, rv in valid:
        if not uniq or abs(dv - uniq[-1][0]) > mpf('1e-6'):
            uniq.append((dv, rv))
    if verbose:
        print("  eps=%+d  DL=%.6f DU=%.6f nscan=%d  -> %d valid d"
              % (eps, DL, DU, nscan, len(uniq)))
        for dv, rv in uniq:
            print("      d = %s   residual %s"
                  % (mp.nstr(dv, 25), mp.nstr(rv, 6)))
    return len(uniq), uniq


def G_sum(n, eps, verbose=True):
    total = 0
    rows = []
    for s in range(5, n - 10 + 1):
        for p in range(5, n - s - 5 + 1):
            for q in range(p + 1, n - s - p + 1):
                c = s + p + q
                g, _ = g_count(c, s, p, q, eps, verbose=False)
                rows.append((c, s, p, q, g))
                total += g
    return total, rows


def main():
    out = []
    def emit(s=""):
        print(s, flush=True)
        out.append(s)

    emit("PE620 idler-phase model probe (no position lattice; phase roots in d)")
    emit("B_k = (r+eps*rho_k)*gamma_k + eps*(R-rho_k)*beta_k; conditions")
    emit("2B_p, 2B_q, B_p-B_q in Z (mod 1).  d in (DL, R-r-1].")
    emit("=" * 72)

    for eps in (+1, -1):
        t0 = time.perf_counter()
        g, dvals = g_count(16, 5, 5, 6, eps)
        dt = time.perf_counter() - t0
        emit("")
        emit("[%+d] g(16,5,5,6) = %d   (oracle 9)   %s   [%.2fs]"
             % (eps, g, "AGREE" if g == 9 else "DISAGREE", dt))

    # whichever eps gives 9, run G(16) and G(20)
    for eps in (+1, -1):
        g, _ = g_count(16, 5, 5, 6, eps, verbose=False)
        if g == 9:
            emit("")
            emit("=== eps=%+d reproduces g(16,5,5,6)=9; running G checks ===" % eps)
            t0 = time.perf_counter()
            g16, rows16 = G_sum(16, eps)
            emit("[G16] G(16) = %d   (oracle 9)   %s   [%.2fs]"
                 % (g16, "AGREE" if g16 == 9 else "DISAGREE",
                    time.perf_counter() - t0))
            for row in rows16:
                emit("      g(%d,%d,%d,%d) = %d" % row)
            t0 = time.perf_counter()
            g20, rows20 = G_sum(20, eps)
            emit("[G20] G(20) = %d   (oracle 205)   %s   [%.2fs]"
                 % (g20, "AGREE" if g20 == 205 else "DISAGREE",
                    time.perf_counter() - t0))
            emit("    per-pair g (%d pairs):" % len(rows20))
            for row in rows20:
                emit("      g(%2d,%2d,%2d,%2d) = %d" % row)
            with open(OUTFILE, "w") as f:
                f.write("\n".join(out) + "\n")
            return

    with open(OUTFILE, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Neither eps reproduced g(16,5,5,6)=9.")


if __name__ == "__main__":
    main()