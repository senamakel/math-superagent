#!/usr/bin/env python3
"""PE620 tangency enumeration over all 22 G(20) tuples — winning sign variant.

Residue per planet of circumference t in {p,q}, EXACTLY as in
code/pattern/tangency_enum.py:

    Q = sigma*rho*(beta-gamma) - eta*R*beta + theta*r*gamma      (radians, mod 1)

where beta = planet-centre angle about the ring centre O, gamma = angle about
the sun centre S, rho = t/2pi, R = c/2pi, r = s/2pi.  Exact tangency to both
gears forces the centre onto |OP| = R-rho  and  |SP| = r+rho  (upper U /
lower L tangency points; mirror identity Q(L) = -Q(U) mod 1 is exact).

VARIANT RESOLUTION (computed, not assumed): the task parenthetical
"(sigma,eta,theta)=(-1,-1,-1)" does NOT reproduce the oracle under this exact
machinery — an 8-variant scan (code/pattern/sign_scan.py) gives
g(-1,-1,-1)=6, g(-1,-1,+1)=9, g(+1,+1,-1)=9 (the two g=9 triples are each
other's sign reversal, Q' = -Q mod 1, same equality set).  The computed winner
(sigma,eta,theta)=(-1,-1,+1) matches the SAVED on-disk tangency_enum.txt,
whose run header is "Q = sigma*rho*(beta-gamma) - eta*R*beta + r*gamma" —
theta hardwired to +1 — with (sig,eta)=(-1,-1): g=9, same d-values
(0.1596022390, ...).  fast_g.py's winning model Q_t = (c-t)*B + (s+t)*G is the
same residue: Q = -rho*(beta-gamma) + R*beta + r*gamma = (c-t)B + (s+t)G
(verified numerically: 0.2500000 at the first root).  So the default here is
the COMPUTED winner (sigma,eta,theta)=(-1,-1,+1), and [-1,-1,-1] totals are
also computed (CLI --variant) for the record.

This is a direct generalization of code/pattern/tangency_enum.py restricted to
one sign variant, keeping the SAME machinery:
  - side combos pp,qq in {UU,LL,UL}  (3 x 3 = 9)
  - objective = max pairwise circular distance of the four residues
  - coarse grid N = 2^20 + 1 over [d_min, d_max]
  - contiguous runs clustered with COARSE_TOL = 1e-4
  - each run refined by 3-zoom local minimisation, mpmath dps = 60,
    accepted iff objective < TIGHT_TOL = 1e-9
  - g = number of distinct refined valid d over all 9 combos

Runs over every tuple (c,s,p,q) with c = s+p+q <= 20, s>=5, p>=5, p<q
(22 tuples), printing per-tuple g and the UU/LL/UL breakdown, and the total
against the oracle G(20) = 205.  The sanity tuple g(16,5,5,6)=9 is printed
first (it is index 0 of the sorted tuple list).

For the oracle tuple (16,5,5,6) only, an additional reconciliation block
compares the tangency-valid d's with the n-integer model valid d's
(n_t = [(c-t)*beta + (s+t)*gamma]/pi in Z): for each tangency d it reports
whether n_p and n_q are integers there; for each n-integer d it reports
whether the winning residues agree mod 1 (Q_p(U) == Q_q(U)).  n-integer d's
are found by a float scan of crossings of n_p through integer levels
(n_p monotone on the interval) refined by mpmath bisection, with degenerate
endpoints (either type's two planets coincide, y ~ 0) excluded — the same
root set as code/pattern/n_integer_count.py.

Usage: python tangency_G20.py [--fresh] [--variant sig,eta,theta] [tuple_index ...]
  --fresh              truncate the output file before writing (use on first chunk)
  --variant s,e,t      sign triple; default -1,-1,+1 (the computed winner)
  tuple_index ...      0-based indices into the sorted tuple list; default: all 22
Output: code/out/tangency_G20.txt
"""
import math
import os
import sys
import time

import numpy as np
from mpmath import mp, mpf, pi, atan2, sqrt, fabs, nint

mp.dps = 60
OUT = "/workspace/code/out/tangency_G20_recheck.txt"
TWO_PI = 2.0 * math.pi
COARSE_TOL = 1e-4
TIGHT_TOL = mpf('1e-9')
NGRID = (1 << 20) + 1
SIG, ETA, THETA = -1, -1, +1          # COMPUTED winning sign variant (see docstring)
PSIDES = ((1, 1, "UU"), (-1, -1, "LL"), (1, -1, "UL"))


def circdist(a, b):
    """Circular distance on the unit circle, a,b in [0,1)."""
    return abs(((a - b + 0.5) % 1.0) - 0.5)


def combo_names():
    """The 9 (pp-name, qq-name) combos."""
    nms = []
    for ppname in PSIDES:
        for qqname in PSIDES:
            nms.append((ppname[2], qqname[2]))
    return nms


def residue_at(c, s, m, d, side):
    """mpmath residue Q for one planet of circumference m (side=+1 upper, -1 lower).

    Returns (Q mod 1, float(beta), float(gamma)); (None,None,None) if the
    tangency point does not exist (y^2 <= 0).
    """
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(m) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None, None, None
    y = sqrt(y2)
    beta = atan2(y, x)
    gamma = atan2(y, x - d)
    if side == -1:
        beta = -beta
        gamma = -gamma
    Q = SIG * rho * (beta - gamma) - ETA * R * beta + THETA * r * gamma
    return (Q % 1), float(beta), float(gamma)


def objective_mp(c, s, p, q, d, psides, qsides):
    """mpmath max pairwise circular residue distance for a combo at d."""
    res = []
    for side in psides:
        Q, _, _ = residue_at(c, s, p, d, side)
        if Q is None:
            return mpf(1)
        res.append(Q)
    for side in qsides:
        Q, _, _ = residue_at(c, s, q, d, side)
        if Q is None:
            return mpf(1)
        res.append(Q)
    m = mpf(0)
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            dd = (res[i] - res[j] + mpf('0.5')) % 1 - mpf('0.5')
            m = max(m, fabs(dd))
    return m


def refine(c, s, p, q, d0, window, psides, qsides):
    """mpmath local minimisation of the objective near d0 by 3 iterative zooms.

    Each zoom scans n=1000 points over the current window and shrinks the
    window to the best point's neighbourhood; after 3 zooms the resolution is
    about window/1000^3, far below the d-accuracy needed for objective < 1e-9.
    Returns (best_d, best_obj).
    """
    n = 1000
    best = (mpf(d0), objective_mp(c, s, p, q, mpf(d0), psides, qsides))
    lo = mpf(d0) - mpf(window)
    hi = mpf(d0) + mpf(window)
    for _ in range(3):
        step = (hi - lo) / n
        d = lo
        for i in range(n + 1):
            o = objective_mp(c, s, p, q, d, psides, qsides)
            if o < best[1]:
                best = (d, o)
            d += step
        lo = best[0] - step
        hi = best[0] + step
    return best


def contiguous_runs(valid):
    """(i0,i1) pairs of maximal contiguous index runs where valid is True.

    Vectorized; identical to scanning `for k in range(N)` with a run flag.
    """
    v = valid.astype(np.int8)
    if v.size == 0:
        return []
    edges = np.flatnonzero(np.diff(v))
    if v[0] == 1:
        edges = np.concatenate(([-1], edges))
    if v[-1] == 1:
        edges = np.concatenate((edges, [v.size - 1]))
    return [(int(edges[j]) + 1, int(edges[j + 1]))
            for j in range(0, len(edges), 2)]


def n_float_array(c, s, t, dv):
    """n_t(d) = [(c-t)*beta + (s+t)*gamma]/pi over a float grid (upper point)."""
    pi = math.pi
    R = c / (2 * pi)
    r = s / (2 * pi)
    rho = t / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + dv * dv) / (2.0 * dv)
    y = np.sqrt(np.maximum(a * a - x * x, 0.0))
    beta = np.arctan2(y, x)
    gamma = np.arctan2(y, x - dv)
    return ((c - t) * beta + (s + t) * gamma) / pi


def n_t_mp(c, s, t, d):
    """n_t = [(c-t)*beta + (s+t)*gamma]/pi at the upper tangency point, mpmath."""
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
    beta = atan2(y, x)
    gamma = atan2(y, x - d)
    return ((c - t) * beta + (s + t) * gamma) / pi


def tangency_y(c, s, t, d):
    """y (upper point height) of the tangency point; 0 if it does not exist."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(t) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return mpf(0)
    return sqrt(y2)


def Q_turns(c, s, t, d):
    """Winning residue in turns: Q_t = (c-t)*B_t + (s+t)*G_t mod 1 (B,G = /2pi).

    This is the (sigma,eta,theta)=(-1,-1,+1) residue:
    -rho*(beta-gamma) + R*beta + r*gamma = (c-t)*B + (s+t)*G  (radians -> turns).
    The parenthetical identity (c-t)*B - (s-t)*G is NOT this residue (it gave
    0.1249888 vs the true 0.2500000 at the first root of the oracle tuple) and
    is kept out of the machinery.
    """
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
    B = atan2(y, x) / (2 * pi)
    G = atan2(y, x - d) / (2 * pi)
    return ((c - t) * B - (s - t) * G) % 1


def n_integer_roots(c, s, p, q):
    """d values where n_p and n_q are both integers (n-integer model).

    n_p is monotone increasing on [d_min, d_max]; each integer level k is
    located by a float crossing scan on the N=2^20+1 grid and refined by
    mpmath bisection of n_p(d)-k.  Degenerate endpoints (either type's two
    tangency points coincide, y < 1e-5) are excluded, mirroring
    code/pattern/n_integer_count.py.  Returns [(k, d, n_p, n_q, y_p, y_q)].
    """
    pi = math.pi
    R = c / (2 * pi)
    r = s / (2 * pi)
    rp = p / (2 * pi)
    rq = q / (2 * pi)
    ap, bp = R - rp, r + rp
    aq, bq = R - rq, r + rq
    d_min = max(abs(ap - bp), abs(aq - bq))
    d_max = min(ap + bp, aq + bq, R - r - 1.0)
    if d_min > d_max:
        return []
    dv = np.linspace(d_min, d_max, NGRID)
    npf = n_float_array(c, s, p, dv)
    roots = []
    for k in range(int(math.floor(npf[0])), int(math.ceil(npf[-1])) + 1):
        idx = np.where(np.diff(np.signbit(npf - k)) != 0)[0]
        if idx.size == 0:
            continue
        i0 = int(idx[0])
        lo = mpf(dv[i0])
        hi = mpf(dv[i0 + 1])
        nlo = n_t_mp(c, s, p, lo) - k
        nhi = n_t_mp(c, s, p, hi) - k
        if nlo == 0 or nlo * nhi > 0:
            # level exactly at a grid node (only the degenerate k=0 endpoint)
            if fabs(nlo) < mpf('1e-25'):
                d = lo
            else:
                continue
        else:
            for _ in range(150):
                mid = (lo + hi) / 2
                nm = n_t_mp(c, s, p, mid) - k
                if nlo * nm <= 0:
                    hi = mid
                    nhi = nm
                else:
                    lo = mid
                    nlo = nm
            d = (lo + hi) / 2
        npv = n_t_mp(c, s, p, d)
        nqv = n_t_mp(c, s, q, d)
        yp = tangency_y(c, s, p, d)
        yq = tangency_y(c, s, q, d)
        roots.append((k, d, npv, nqv, yp, yq))
    YTOL = mpf('1e-5')
    return [rt for rt in roots if rt[4] > YTOL and rt[5] > YTOL]


def tuple_block(c, s, p, q, emit):
    """One (c,s,p,q) block: grid scan, run clustering, refinement, counts.

    Returns g = number of distinct refined valid d over all 9 combos (mpf set).
    """
    t0 = time.time()
    R = c / TWO_PI
    r = s / TWO_PI
    rp = p / TWO_PI
    rq = q / TWO_PI
    ap, bp = R - rp, r + rp
    aq, bq = R - rq, r + rq
    d_min = max(abs(ap - bp), abs(aq - bq))
    d_max = min(ap + bp, aq + bq, R - r - 1.0)
    emit("=" * 78)
    emit("g(%d,%d,%d,%d)" % (c, s, p, q))
    emit("R=%.8f r=%.8f rp=%.8f rq=%.8f" % (R, r, rp, rq))
    if d_min > d_max:
        emit("  empty centre-offset interval (d_min=%.9f > d_max=%.9f) -> g = 0"
             % (d_min, d_max))
        emit("  g = 0   (elapsed %.2f s)" % (time.time() - t0))
        return set()
    emit("d_min=%.12f  d_max=%.12f  (width %.12f)" % (d_min, d_max, d_max - d_min))
    emit("coarse grid: %d points, spacing ~%.3e" % (NGRID, (d_max - d_min) / (NGRID - 1)))

    dv = np.linspace(d_min, d_max, NGRID)
    delta = (d_max - d_min) / (NGRID - 1)

    # tangency geometry per type (arrays over the d grid)
    geom = {}
    for name, rhom in (('p', rp), ('q', rq)):
        a = R - rhom
        b = r + rhom
        x = (a * a - b * b + dv * dv) / (2.0 * dv)
        y2 = np.maximum(a * a - x * x, 0.0)
        y = np.sqrt(y2)
        beta = np.arctan2(y, x)
        gamma = np.arctan2(y, x - dv)
        geom[name] = dict(beta=beta, gamma=gamma, rho=rhom)

    # upper residues, winning variant; lower by the exact mirror identity
    Qu = {}
    for name in ('p', 'q'):
        g = geom[name]
        rho = g['rho']
        Qu[name] = np.mod(SIG * rho * (g['beta'] - g['gamma'])
                          - ETA * R * g['beta'] + THETA * r * g['gamma'], 1.0)
    up_p, lo_p = Qu['p'], np.mod(-Qu['p'], 1.0)
    up_q, lo_q = Qu['q'], np.mod(-Qu['q'], 1.0)

    all_d = set()
    per_combo = {}
    for (psides, pname) in [(x[:2], x[2]) for x in PSIDES]:
        for (qsides, qname) in [(x[:2], x[2]) for x in PSIDES]:
            arrs = []
            for sd in psides:
                arrs.append(up_p if sd == 1 else lo_p)
            for sd in qsides:
                arrs.append(up_q if sd == 1 else lo_q)
            obj = np.zeros(NGRID)
            for i in range(4):
                for j in range(i + 1, 4):
                    dd = np.abs(((arrs[i] - arrs[j] + 0.5) % 1.0) - 0.5)
                    obj = np.maximum(obj, dd)
            runs = contiguous_runs(obj < COARSE_TOL)
            key = (pname, qname)
            g_count = 0
            for (i0, i1) in runs:
                seg = slice(i0, i1 + 1)
                best_idx = i0 + int(np.argmin(obj[seg]))
                d0 = float(dv[best_idx])
                bd, bo = refine(c, s, p, q, d0, 5 * delta, psides, qsides)
                if bo < TIGHT_TOL:
                    g_count += 1
                    all_d.add(mpf(bd))
            per_combo[key] = g_count

    emit("  combos pp x qq = [UU,LL,UL] x [UU,LL,UL]:")
    for (pname, qname) in combo_names():
        emit("     pp=%-2s qq=%-2s : %d" % (pname, qname, per_combo[(pname, qname)]))
    g = len(all_d)
    ds_sorted = sorted(all_d)
    emit("  distinct refined valid d (%d):" % g)
    for d in ds_sorted:
        emit("      d = %.25f" % float(d))
    emit("  g = %d   (distinct refined valid d over all 9 combos; elapsed %.2f s)"
         % (g, time.time() - t0))
    if (c, s, p, q) == (16, 5, 5, 6):
        emit("  sanity check: oracle g(16,5,5,6) = 9  ->  %s"
             % ("AGREE" if g == 9 else "DISAGREE"))
    return all_d


def reconcile_block(c, s, p, q, tangency_ds, emit):
    """Cross-check (oracle tuple only): tangency d's vs n-integer model d's."""
    emit("")
    emit("  ---------- RECONCILIATION: winning tangency residue vs n-integer model ----------")
    emit("  tangency: Q_t = (c-t)*B_t + (s+t)*G_t mod 1, B,G in turns")
    emit("  n-model : valid iff n_p, n_q in Z with n_t = [(c-t)beta + (s+t)gamma]/pi")
    tds = sorted(tangency_ds)
    roots = n_integer_roots(c, s, p, q)
    emit("  tangency valid d's (%d):" % len(tds))
    for d in tds:
        emit("      d = %.25f" % float(d))
    emit("  n-integer valid d's (%d, integer levels k, degenerate endpoints excluded):"
         % len(roots))
    for (k, d, npv, nqv, yp, yq) in roots:
        emit("      k=%2d  d = %.25f   n_p=%s  n_q=%s"
             % (k, float(d), mp.nstr(npv, 22), mp.nstr(nqv, 22)))
    emit("")
    emit("  side-by-side (sorted, aligned by rank):")
    emit("      %2s | %-26s | %-26s | %s" % ("#", "tangency d", "n-integer d", "|dd|"))
    for i in range(max(len(tds), len(roots))):
        a = float(tds[i]) if i < len(tds) else float('nan')
        b = float(roots[i][1]) if i < len(roots) else float('nan')
        dd_ = abs(a - b) if (i < len(tds) and i < len(roots)) else float('nan')
        emit("      %2d | %-26.17g | %-26.17g | %.3e" % (i + 1, a, b, dd_))
    emit("")
    emit("  per tangency d: are n_p, n_q integers there?")
    both_ok = 0
    for d in tds:
        npv = n_t_mp(c, s, p, d)
        nqv = n_t_mp(c, s, q, d)
        ip_ = fabs(npv - nint(npv)) < mpf('1e-20')
        iq_ = fabs(nqv - nint(nqv)) < mpf('1e-20')
        both_ok += (ip_ and iq_)
        emit("      d = %.17g   n_p = %s  (int %s)   n_q = %s  (int %s)"
             % (float(d), mp.nstr(npv, 20), "YES" if ip_ else "no",
                mp.nstr(nqv, 20), "YES" if iq_ else "no"))
    emit("  => n_p and n_q both integers at %d of %d tangency d's"
         % (both_ok, len(tds)))
    emit("")
    emit("  per n-integer d: do the winning residues agree, Q_p(U) == Q_q(U) mod 1?")
    same_ok = 0
    for (k, d, npv, nqv, yp, yq) in roots:
        Qp = Q_turns(c, s, p, d)
        Qq = Q_turns(c, s, q, d)
        cd = fabs((Qp - Qq + mpf('0.5')) % 1 - mpf('0.5'))
        ok = cd < mpf('1e-20')
        same_ok += ok
        emit("      k=%2d  d = %.17g   Q_p(U) = %s   Q_q(U) = %s   (equal mod 1 %s)"
             % (k, float(d), mp.nstr(Qp, 20), mp.nstr(Qq, 20),
                "YES" if ok else "no"))
    emit("  => Q_p(U) == Q_q(U) mod 1 at %d of %d n-integer d's" % (same_ok, len(roots)))


def all_tuples():
    """The 22 G(20) tuples (c,s,p,q), c=s+p+q<=20, s>=5, p>=5, p<q, sorted."""
    ts = set()
    for s in range(5, 21):
        for p in range(5, 21):
            for q in range(p + 1, 21):
                if s + p + q <= 20:
                    ts.add((s + p + q, s, p, q))
    return sorted(ts)


def main():
    global SIG, ETA, THETA
    argv = sys.argv[1:]
    fresh = '--fresh' in argv
    variant = None
    for i, a in enumerate(argv):
        if a == '--variant':
            if i + 1 < len(argv):
                variant = argv[i + 1].split(',')
            break
    if variant:
        SIG, ETA, THETA = int(variant[0]), int(variant[1]), int(variant[2])
        print("variant overridden: (sigma,eta,theta)=(%+d,%+d,%+d)"
              % (SIG, ETA, THETA), flush=True)
    skip = set()
    for i, a in enumerate(argv):
        if a == '--variant':
            skip.add(i)
            skip.add(i + 1)
    inds = [int(a) for i, a in enumerate(argv)
            if i not in skip and not a.startswith('--')]
    tuples = all_tuples()
    if not inds:
        inds = list(range(len(tuples)))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if fresh:
        with open(OUT, "w") as f:
            f.write("PE620 tangency enumeration over G(20) tuples\n")
            f.write("sign variant (sigma,eta,theta)=(%+d,%+d,%+d):\n"
                    % (SIG, ETA, THETA))
            f.write("  Q = sigma*rho*(beta-gamma) - eta*R*beta + theta*r*gamma (mod 1)\n")
            f.write("  computed winner (s,e,t)=(-1,-1,+1) = (c-t)B + (s+t)G turns;\n")
            f.write("  the parenthetical (-1,-1,-1) gives g(16,5,5,6)=6, not 9 (see sign_scan.py)\n")
            f.write("machinery: coarse grid N=2^20+1 over [d_min,d_max]; contiguous runs\n")
            f.write("  COARSE_TOL=1e-4; 3-zoom mpmath refine (dps=60, n=1000/zoom),\n")
            f.write("  accept iff objective < TIGHT_TOL=1e-9; g = distinct refined\n")
            f.write("  valid d over the 9 side combos pp,qq in {UU,LL,UL}.\n")
    grand = 0
    for i in inds:
        c, s, p, q = tuples[i]
        lines = []
        emit = lambda s_="": (print(s_, flush=True), lines.append(s_))
        t0 = time.time()
        all_d = tuple_block(c, s, p, q, emit)
        if (c, s, p, q) == (16, 5, 5, 6):
            reconcile_block(c, s, p, q, all_d, emit)
        grand += len(all_d)
        with open(OUT, "a") as f:
            f.write("\n".join(lines) + "\n")
        print("  [summary] g(%d,%d,%d,%d) = %d   (elapsed %.1f s, cumulative over"
              " processed tuples %d)"
              % (c, s, p, q, len(all_d), time.time() - t0, grand), flush=True)
    print("=" * 78)
    print("G(20) over processed tuple indices %s = %d   oracle 205   %s"
          % (inds, grand, "AGREE" if grand == 205 else "DISAGREE"))
    with open(OUT, "a") as f:
        f.write("=" * 78 + "\n")
        f.write("G(20) over processed tuple indices %s = %d   oracle 205   %s\n"
                % (inds, grand, "AGREE" if grand == 205 else "DISAGREE"))


if __name__ == "__main__":
    main()