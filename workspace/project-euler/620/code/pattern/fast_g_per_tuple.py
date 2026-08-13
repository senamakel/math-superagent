"""PE620: per-tuple strict f-crossing count for G(20), with root diagnostics.

f-crossing model (code/pattern/fast_g.py docstring):
  Q_t(d) = (c-t)*B_t + (s+t)*G_t  (turns),  B/G = atan2 angles of the upper
  tangency point about the ring centre O / sun centre S,
  centre constraints |OP| = R - rho_t, |SP| = r + rho_t.
  f(d) := Q_p(d) - Q_q(d) strictly increasing on (DL,DU); the two planet
  types mesh iff f(d) is an integer (residues congruent mod 1);
  g = #{m in Z : f(DL) < m < f(DU)}, one crossing per m.

This driver recounts g per G(20) tuple with the strict eps-shifted endpoints
at mpmath-60:
  g_int = #{m in Z : f(DL+eps) < m < f(DU-eps)},  eps = 1e-9.
For every crossing root d of every tuple it reports
  n_p = 2 Q_p, n_q = 2 Q_q   (these are the tooth-phase counts of the
  n_integer model n_t = [(c-t)*beta + (s+t)*mu]/pi; identity n_t = 2 Q_t,
  checked exactly), their residues mod 1, tangency ordinates y_p, y_q
  (degenerate iff ~0), and signed distance to the interval endpoints, with
  per-root flags:
    V  root passes n_integer-model admissibility: n_p,n_q integral,
       (round(n_p)-round(n_q)) == p-q (mod 2), y_p,y_q above the grid YTOL
    H  half-integer n_p (equiv. n_q; n_p - n_q = 2m so residues coincide)
    E  root within 1e-6 of an endpoint (|d-DL| < 1e-6 or |d-DU| < 1e-6)
    D  degenerate: y_p or y_q < 1e-6 (either type's tangency points collapse)
Also g_half = #{half-integer levels m+1/2 in (fL,fR)}: for p-q odd the grid
model's roots live on exactly these levels (parity condition), so the
surplus of fast_g over the oracle-consistent split is
g_int - g_grid = g_int - g_half when the grid counts every half-integer level.

The grid reference g_grid = len(valid_ds(...)) reuses n_integer_count.py's
scan (1,048,577-point grid, tol 1e-3, degenerate exclusion y < 1e-5) — the
only per-tuple split on disk reproducing the oracle G(20)=205 — plus a
stability re-check at N = 2^22+1, tol 1e-4 on the differing tuples.

Output: stdout + /workspace/code/out/fast_g_G20.txt
"""
import os
from mpmath import mp, mpf, floor, ceil

from pattern.fast_g import bounds, Q_t, geometry, g_fast_flat
from pattern.n_integer_count import valid_ds

mp.dps = 60

OUT = "/workspace/code/out/fast_g_G20.txt"
EPS = mpf('1e-9')          # endpoint shift for the strict level count
END_TOL = mpf('1e-6')      # "near an endpoint" threshold (user-specified)
Y_TOL = mpf('1e-6')        # root-degeneracy flag threshold (y_p or y_q)
GRID_YTOL = 1e-5           # degenerate exclusion used by the n_integer scan
INT_TOL = mpf('1e-6')      # integrality / half-integrality tolerance


def tuples_20():
    """The 22 G(20) tuples (c,s,p,q) with c = s+p+q, s>=5, p>=5, p<q."""
    out = []
    for s in range(5, 20 - 10 + 1):
        for p in range(5, 20 - s - 5 + 1):
            for q in range(p + 1, 20 - s - p + 1):
                out.append((s + p + q, s, p, q))
    return sorted(out)


def F_at(c, s, p, q, d):
    return Q_t(c, s, p, d) - Q_t(c, s, q, d)


def bisect_level(c, s, p, q, DL, DU, m):
    """Root d of f(d)=m in (DL+eps, DU-eps) by 60-dps bisection."""
    lo, hi = DL + EPS, DU - EPS
    flo, fhi = F_at(c, s, p, q, lo) - m, F_at(c, s, p, q, hi) - m
    assert flo < 0 < fhi, "level %d not strictly inside (%.12f, %.12f)" % (m, flo, fhi)
    for _ in range(250):
        mid = (lo + hi) / 2
        fm = F_at(c, s, p, q, mid) - m
        if fm == 0:
            break
        if (flo < 0) != (fm < 0):
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def root_diagnostics(c, s, p, q, DL, DU, m):
    d = bisect_level(c, s, p, q, DL, DU, m)
    gP, gQ = geometry(c, s, p, d), geometry(c, s, q, d)
    yp, yq = gP[-1], gQ[-1]
    Qp, Qq = Q_t(c, s, p, d), Q_t(c, s, q, d)
    np_, nq_ = 2 * Qp, 2 * Qq
    rp = np_ % 1
    rq = nq_ % 1
    dDL, dDU = d - DL, DU - d

    def cyc(r):
        return min(r, 1 - r)

    res_int = cyc(rp)          # = cyc(rq) exactly: n_p - n_q = 2m in 2Z
    res_half = cyc(rp - mpf('0.5'))
    resid = np_ - nq_ - 2 * m  # should be exactly 0

    half = res_half < INT_TOL
    degen = yp < Y_TOL or yq < Y_TOL
    near_end = dDL < END_TOL or dDU < END_TOL
    ok_int = res_int < INT_TOL  # both integral (same residue)
    parity = (int(round(float(np_))) - int(round(float(nq_)))) % 2 == (p - q) % 2
    y_ok = yp > mpf(GRID_YTOL) and yq > mpf(GRID_YTOL)
    valid = ok_int and parity and y_ok

    flags = ''
    if valid:
        flags += 'V'
    if half:
        flags += 'H'
    if near_end:
        flags += 'E'
    if degen:
        flags += 'D'
    if not flags:
        flags = '-'
    return dict(m=m, d=d, np_=np_, nq_=nq_, rp=rp, rq=rq, resid=resid,
                yp=yp, yq=yq, dDL=dDL, dDU=dDU, flags=flags,
                half=half, degen=degen, near_end=near_end, valid=valid)


def count_half_levels(fL, fR):
    """#{half-integers k+1/2 strictly inside (fL, fR)}."""
    a, b = fL - mpf('0.5'), fR - mpf('0.5')
    lo = int(floor(a)) + 1
    hi = int(ceil(b)) - 1
    return max(0, hi - lo + 1)


def main():
    lines = []
    def emit(s_=""):
        print(s_, flush=True)
        lines.append(s_)

    emit("PE620 G(20) per-tuple strict f-crossing analysis (mpmath-60)")
    emit("f(d) = Q_p(d) - Q_q(d);  g_int  = #{m in Z : f(DL+eps) < m < f(DU-eps)}")
    emit("eps = 1e-9;  n_t = 2 Q_t = [(c-t)*beta + (s+t)*mu]/pi")
    emit("flags: V=n-model valid, H=half-integer n_p, E=near endpoint (<1e-6),")
    emit("       D=degenerate (y_p or y_q < 1e-6); '-' = none")
    emit("g_half = #{half-integer levels} on the same open interval")
    emit("g_fast.py = fast_g.py's own count;  g_grid = n_integer scan (205 split)")
    emit("=" * 132)

    tup = tuples_20()
    tot_int = 0
    tot_py = 0
    tot_grid = 0
    over = []
    for (c, s, p, q) in tup:
        DL, DU = bounds(c, s, p, q)
        fL = F_at(c, s, p, q, DL + EPS)
        fR = F_at(c, s, p, q, DU - EPS)
        mmin = int(floor(fL)) + 1
        mmax = int(ceil(fR)) - 1
        g_int = max(0, mmax - mmin + 1)
        g_half = count_half_levels(fL, fR)
        g_py = g_fast_flat(c, s, p, q)
        g_grid = len(valid_ds(c, s, p, q))
        tot_int += g_int
        tot_py += g_py
        tot_grid += g_grid
        par_cs = (c + s) % 2
        par_pq = (p - q) % 2
        emit("")
        emit("(c,s,p,q)=(%2d,%2d,%2d,%2d)  c+s %s  p-q %s | DL=%.9f DU=%.9f"
             % (c, s, p, q, "EVEN" if par_cs == 0 else "ODD",
                "EVEN" if par_pq == 0 else "ODD", float(DL), float(DU)))
        emit("  fL=%.9f  fR=%.9f   levels m=%d..%d" % (float(fL), float(fR), mmin, mmax))
        for m in range(mmin, mmax + 1):
            r = root_diagnostics(c, s, p, q, DL, DU, m)
            emit("   m=%+3d d=%.12f n_p=%9.6f n_q=%9.6f res_p=%.9f res_q=%.9f"
                 " n_p-n_q-2m=%.1e y_p=%.3e y_q=%.3e |d-DL|=%.2e |DU-d|=%.2e %s"
                 % (r['m'], float(r['d']), float(r['np_']), float(r['nq_']),
                    float(r['rp']), float(r['rq']), float(r['resid']),
                    float(r['yp']), float(r['yq']), float(r['dDL']),
                    float(r['dDU']), r['flags']))
        diff = g_int - g_grid
        mark = "  <<< OVERCOUNT +%d" % diff if diff > 0 else ""
        emit("  g_int=%d  g_half=%d  g_fast.py=%d  g_grid=%d  (g_int-g_grid=%+d)%s"
             % (g_int, g_half, g_py, g_grid, g_int - g_grid, mark))
        if diff > 0:
            over.append((c, s, p, q, g_int, g_half, g_grid))

    emit("")
    emit("=" * 132)
    emit("TOTALS:  g_int sum=%d   g_fast.py sum=%d   g_grid sum=%d   oracle G(20)=205"
         % (tot_int, tot_py, tot_grid))
    emit("fast_g.py vs oracle: %s (overcount %d)"
         % ("AGREE" if tot_py == 205 else "DISAGREE", tot_py - 205))
    emit("g_int (eps-strict) vs oracle: %s (overcount %d)"
         % ("AGREE" if tot_int == 205 else "DISAGREE", tot_int - 205))

    emit("")
    emit("=" * 132)
    emit("EXTRA-ROOT ANALYSIS: tuples where g_int > g_grid  (%d tuples)" % len(over))
    for (c, s, p, q, gi, gh, gg) in over:
        par_pq = (p - q) % 2
        emit("")
        emit("(%2d,%2d,%2d,%2d): g_int=%d  g_half=%d  g_grid=%d   p-q %s, c+s %s"
             % (c, s, p, q, gi, gh, gg, "ODD" if par_pq else "EVEN",
                "ODD" if (c + s) % 2 else "EVEN"))
        emit("  explanation when p-q odd: integer-f roots and half-integer-f")
        emit("  roots are disjoint families; grid counts the half-integer one,")
        emit("  so surplus = g_int - g_half = %d." % (gi - gh))
        DL, DU = bounds(c, s, p, q)
        fL = F_at(c, s, p, q, DL + EPS)
        fR = F_at(c, s, p, q, DU - EPS)
        mmin = int(floor(fL)) + 1
        mmax = int(ceil(fR)) - 1
        for m in range(mmin, mmax + 1):
            r = root_diagnostics(c, s, p, q, DL, DU, m)
            why = []
            if not r['valid']:
                if r['half']:
                    why.append("HALF-INTEGER n_p")
                elif not (r['yp'] > mpf(GRID_YTOL) and r['yq'] > mpf(GRID_YTOL)):
                    why.append("DEGENERATE y<1e-5")
                elif par_pq:
                    why.append("p-q odd: parity n_p-n_q=%+d even vs odd required"
                               % int(round(float(r['np_']))) - int(round(float(r['nq_']))))
                else:
                    why.append("fractional n_p (res=%.3e)" % float(r['rp']))
            if r['near_end']:
                why.append("NEAR-ENDPOINT d=%.6f" % float(r['d']))
            if r['degen']:
                why.append("DEGENERATE y")
            emit("   m=%+3d d=%.12f n_p=%9.6f n_q=%9.6f y_p=%.2e y_q=%.2e %s -> %s"
                 % (m, float(r['d']), float(r['np_']), float(r['nq_']),
                    float(r['yp']), float(r['yq']), r['flags'],
                    "; ".join(why) if why else "n-model valid"))

    # Grid stability check on the differing tuples (finer grid, tighter tol)
    emit("")
    emit("=" * 132)
    emit("GRID STABILITY: re-scan of the %d differing tuples at N=2^22+1, tol=1e-4"
         % len(over))
    for (c, s, p, q, gi, gh, gg) in over:
        g2 = len(valid_ds(c, s, p, q, tol=1e-4, N=(1 << 22) + 1))
        emit("   (%2d,%2d,%2d,%2d): g_grid(1M,tol1e-3)=%d  g_grid(4M,tol1e-4)=%d"
             % (c, s, p, q, gg, g2))

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    emit("")
    emit("Output saved to %s" % OUT)


if __name__ == "__main__":
    main()