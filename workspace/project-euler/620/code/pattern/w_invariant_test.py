#!/usr/bin/env python3
"""Numerical test of the off-centre W-invariant meshing model of PE620.

Model source: research/threads/offcentre-mesh-phase-model.md

Geometry: S=(0,0), C=(d,0);  R = c/2pi, r = s/2pi, rho_t = t/2pi;
  a_t = r+rho_t = (s+t)/(2pi)   [|SP|],  b_t = R-rho_t = (c-t)/(2pi)  [|CP|];
  d in (d_min, d_max), d_min = max(|a_p-b_p|,|a_q-b_q|), d_max = R-r-1
  (1 cm closest S-C boundary gap).
Interior angles of triangle S-P-C (all in (0,pi), phi+chi+gamma=pi):
  phi at S, chi at C, gamma at P, from atan2 on the exact P=(x,+-y).

Invariants:  W_t  = s*phi_t  + c*chi_t  - t*gamma_t
             W'_t = s*phi_t  - c*chi_t  + t*gamma_t
Condition sets (each condition is a congruence to an integer, mod 1):
  (A) Ap:=(s*phi_p+c*chi_p)/pi in Z, Aq in Z, cross:=(W_p-W_q)/(2pi) in Z
  (B) cross in Z
  (C) Ep:=(p*gamma_p-c*chi_p)/pi in Z, Eq in Z, cross in Z
      (thread suspects these hold identically at all d -- verified here)
  (D) Ap in Z, Aq in Z, crossD:=(W'_p-W'_q)/(2pi) in Z

Method: float64 numpy scan over [d_min,d_max] (chunked; N=1e7 points for the
oracle case, N=1e6 per pair in the G sums) plus 1e-3 endpoint probes (angle
derivatives diverge at d_min) locates near-integer points of every congruence;
each anchor is refined by mpmath (40 dps) bisection on the exact function to
residue < 1e-24; a d is valid for a set iff every condition of the set has
residue < 1e-9 at it (mpmath). An independent consistency check clusters all
grid points where the set's conjoined residue is < SCAN_TOL and requires each
cluster to be within 200*step of a found valid d.

Complexity per (c,s,p,q): fixed O(N) float64 work + O(#roots) mpmath
refinements; N is a fixed verification budget, not a function of the problem
bound (500). No answer-space enumeration.

Oracle: g(16,5,5,6)=9, G(16)=9, G(20)=205.
"""
import math
import time

import numpy as np
from mpmath import mp, mpf, pi, atan2, sqrt

mp.dps = 40

OUTFILE = "/workspace/code/out/w_invariant_test.txt"

SCAN_TOL = 3e-4            # float64 residue below which a grid point is an anchor
VERIFY_TOL = mpf('1e-9')   # max residue over a set's conditions for a valid d
DEDUPE = mpf('1e-6')       # refined roots closer than this are one d
REFINE_TOL = mpf('1e-24')  # residue the bisection must reach for its own key

ALL_KEYS = ["Ap", "Aq", "cross", "Ep", "Eq", "crossD"]

SETS = [
    ("A", ["Ap", "Aq", "cross"],
     "s*phi_t+c*chi_t in pi*Z (t=p,q) AND W_p-W_q in 2pi*Z"),
    ("B", ["cross"], "W_p-W_q in 2pi*Z"),
    ("C", ["Ep", "Eq", "cross"],
     "t*gamma_t-c*chi_t in pi*Z (t=p,q) AND W_p-W_q in 2pi*Z"
     "  [suspected identically satisfied at all d]"),
    ("D", ["Ap", "Aq", "crossD"],
     "s*phi_t+c*chi_t in pi*Z AND W'_p-W'_q in 2pi*Z,"
     " W'_t = s*phi_t-c*chi_t+t*gamma_t"),
]


# ----------------------------------------------------------------- geometry

def interval(c, s, p, q):
    """(DL, DU) floats: allowed centre separation, open interval."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rp, rq = mpf(p) / (2 * pi), mpf(q) / (2 * pi)
    ap, bp = r + rp, R - rp
    aq, bq = r + rq, R - rq
    DL = max(abs(ap - bp), abs(aq - bq))
    DU = R - r - mpf(1)
    return float(DL), float(DU)


def angles_np(D, a, b):
    """Vectorised interior angles: S=(0,0), C=(d,0), |SP|=a, |CP|=b, P upper."""
    D = np.asarray(D, dtype=np.float64)
    x = (a * a - b * b + D * D) / (2.0 * D)
    y = np.sqrt(np.clip(a * a - x * x, 0.0, None))
    phi = np.arctan2(y, x)
    chi = np.arctan2(y, D - x)
    return phi, chi, np.pi - phi - chi   # phi+chi+gamma = pi


def arr_keys(D, c, s, p, q):
    """All six congruence numerators as float64 arrays over D (each in Z)."""
    D = np.asarray(D, dtype=np.float64)
    R = c / (2 * np.pi)
    r = s / (2 * np.pi)
    rp, rq = p / (2 * np.pi), q / (2 * np.pi)
    ap, bp = r + rp, R - rp
    aq, bq = r + rq, R - rq
    pp, cp, gp = angles_np(D, ap, bp)
    pq, cq, gq = angles_np(D, aq, bq)
    K = {}
    K['Ap'] = (s * pp + c * cp) / np.pi
    K['Aq'] = (s * pq + c * cq) / np.pi
    K['cross'] = (s * (pp - pq) + c * (cp - cq) - p * gp + q * gq) / (2 * np.pi)
    K['Ep'] = (p * gp - c * cp) / np.pi
    K['Eq'] = (q * gq - c * cq) / np.pi
    K['crossD'] = (s * (pp - pq) - c * (cp - cq) + p * gp - q * gq) / (2 * np.pi)
    return K


def angles_mp(d, a, b):
    """Interior angles at mpmath precision (phi at S, chi at C, gamma at P)."""
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    y = sqrt(y2) if y2 > 0 else mpf(0)
    phi = atan2(y, x)
    chi = atan2(y, d - x)
    return phi, chi, pi - phi - chi


def all_keys(d, c, s, p, q):
    """All six congruence numerators at one mpf d (each must be in Z)."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rp, rq = mpf(p) / (2 * pi), mpf(q) / (2 * pi)
    ap, bp = r + rp, R - rp
    aq, bq = r + rq, R - rq
    pp, cp, gp = angles_mp(d, ap, bp)
    pq, cq, gq = angles_mp(d, aq, bq)
    S, C, P, Q = mpf(s), mpf(c), mpf(p), mpf(q)
    K = {}
    K['Ap'] = (S * pp + C * cp) / pi
    K['Aq'] = (S * pq + C * cq) / pi
    K['cross'] = (S * (pp - pq) + C * (cp - cq) - P * gp + Q * gq) / (2 * pi)
    K['Ep'] = (P * gp - C * cp) / pi
    K['Eq'] = (Q * gq - C * cq) / pi
    K['crossD'] = (S * (pp - pq) - C * (cp - cq) + P * gp - Q * gq) / (2 * pi)
    return K


def res_mp(x):
    """Distance of mpf x to the nearest integer, in [0, 0.5]."""
    r = x % mpf(1)
    r = min(r, mpf(1) - r)
    return r


# ------------------------------------------------------------------ scanning

def _anchor_runs(r, sel, D, idx):
    """Cluster near-integer grid points (gap<=3) -> (d, residual) per run."""
    out = []
    i = 0
    while i < len(sel):
        j = i
        while j + 1 < len(sel) and sel[j + 1] - sel[j] <= 3:
            j += 1
        grp = sel[i:j + 1]
        m = grp[int(np.argmin(r[grp]))]
        out.append((float(D[m]), float(r[m])))
        i = j + 1
    return out


def scan_anchors(c, s, p, q, DL, DU, N):
    """Coarse float64 scan of [DL,DU] plus endpoint probes.

    Returns (anchors, maxres, near, step):
      anchors  list of (d0, key, res0): grid points where a key is near-integer
      maxres   dict key -> max residue over every scanned point
      near     dict set name -> list of d where the set's CONJOINED residue
               < SCAN_TOL (capped; used for the coverage cross-check, and
               detects 'identically satisfied' sets)
      step     main-scan grid spacing
    """
    n = int(N)
    step = (DU - DL) / n
    anchors = []
    maxres = {k: 0.0 for k in ALL_KEYS}
    near = {name: [] for name, _, _ in SETS}
    CAP = 2_000_000
    flooded = set()
    CH = 2_000_000

    def _handle_chunk(D, report_near):
        nonlocal anchors
        K = arr_keys(D, c, s, p, q)
        r = {}
        for k in ALL_KEYS:
            V = K[k]
            rr = np.minimum(V % 1.0, 1.0 - (V % 1.0))
            r[k] = rr
            maxres[k] = max(maxres[k], float(rr.max()))
        for k in ALL_KEYS:
            sel = np.where(r[k] < SCAN_TOL)[0]
            for d0, res0 in _anchor_runs(r[k], sel, D, None):
                anchors.append((d0, k, res0))
        if report_near:
            for name, keys, _ in SETS:
                if name in flooded:
                    continue
                con = np.maximum.reduce([r[k] for k in keys])
                sel = np.where(con < SCAN_TOL)[0]
                for gi in sel:
                    if len(near[name]) >= CAP:
                        flooded.add(name)
                        break
                    near[name].append(float(D[gi]))

    # main scan over [DL, DU]
    for start in range(0, n + 1, CH):
        stop = min(start + CH, n + 1)
        D = DL + (DU - DL) * np.arange(start, stop, dtype=np.float64) / n
        _handle_chunk(D, report_near=True)

    # endpoint probes: windows where angle derivatives diverge (d near DL)
    for wlo, whi, nw in ((DL, min(DL + 1e-3, DU), 1_000_000),
                         (max(DU - 1e-3, DL), DU, 1_000_000)):
        if whi <= wlo + 1e-12:
            continue
        for start in range(0, nw + 1, CH):
            stop = min(start + CH, nw + 1)
            D = wlo + (whi - wlo) * np.arange(start, stop, dtype=np.float64) / nw
            _handle_chunk(D, report_near=False)

    return anchors, maxres, near, step


def refine_root(key, d0, c, s, p, q, halfw):
    """mpmath bisection for key(d) = k (nearest integer at the anchor)."""
    x0 = mpf(d0)
    k = int(math.floor(float(all_keys(x0, c, s, p, q)[key]) + 0.5))

    def f(x):
        return all_keys(x, c, s, p, q)[key] - mpf(k)

    h = mpf(halfw)
    a, b = x0 - h, x0 + h
    fa, fb = f(a), f(b)
    for _ in range(6):                     # widen if no sign change yet
        if fa * fb < 0:
            break
        h = h * 10
        if h > mpf('1e-3'):
            return None
        a, b = x0 - h, x0 + h
        fa, fb = f(a), f(b)
    else:
        return None
    for _ in range(400):
        m = (a + b) / 2
        fm = f(m)
        if fm == 0 or (b - a) < mpf('1e-30'):
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2


def refine_all(anchors, c, s, p, q, step):
    """Bisect every anchor; return deduplicated mpf roots (sorted).

    Guards: anchors on or outside the open interval (DL, DU) are skipped
    (endpoints are degenerate: y=0, angles ill-defined); a bisected root is
    kept only if it lies within 200*step of its anchor, inside the interval,
    and refines its own key to REFINE_TOL.
    """
    DL, DU = interval(c, s, p, q)
    dL = mpf(DL) * (1 + mpf('1e-12')) + mpf('1e-12')
    dU = mpf(DU) * (1 - mpf('1e-12')) - mpf('1e-12')
    maxoff = 200.0 * step
    roots = []
    for d0, key, res0 in anchors:
        if not (DL + 1e-9 < d0 < DU - 1e-9):
            continue
        rt = refine_root(key, d0, c, s, p, q, 50 * step)
        if rt is None:
            continue
        if abs(float(rt) - d0) > maxoff:
            continue
        if not (dL < rt < dU):
            continue
        if res_mp(all_keys(rt, c, s, p, q)[key]) < REFINE_TOL:
            roots.append(rt)
    roots.sort()
    uniq = []
    for r in roots:
        if not uniq or r - uniq[-1] > DEDUPE:
            uniq.append(r)
    return uniq


# ------------------------------------------------------------------- report

def run_case(c, s, p, q, N, label, out):
    """Full evaluation of all four condition sets for one (c,s,p,q).

    Returns dict set-name -> (count, [ (d, {key: residue}) ... ]).
    """
    out("")
    out("=== case %s: (c,s,p,q) = (%d,%d,%d,%d),  N=%d ==="
        % (label, c, s, p, q, N))
    DL, DU = interval(c, s, p, q)
    out("    DL = %.12f   DU = %.12f   (open interval, length %.12f)"
        % (DL, DU, DU - DL))
    if DL >= DU:
        out("    interval empty -> g = 0 for every set")
        return {name: (0, []) for name, _, _ in SETS}

    t0 = time.perf_counter()
    anchors, maxres, near, step = scan_anchors(c, s, p, q, DL, DU, N)
    t1 = time.perf_counter()
    out("    scan: %d anchors (per-key near-integer points), max residues:"
        % len(anchors))
    for k in ALL_KEYS:
        out("        max |resid.%s| over grid = %.3e" % (k, maxres[k]))
    out("    [scan %.2fs]" % (t1 - t0))

    roots = refine_all(anchors, c, s, p, q, step)
    t2 = time.perf_counter()
    out("    refined unique roots: %d   [refine %.2fs]" % (len(roots), t2 - t1))
    rows = []
    for d in roots:
        kv = all_keys(d, c, s, p, q)
        rows.append((d, {k: res_mp(kv[k]) for k in ALL_KEYS}))

    per_set = {}
    out("")
    for name, keys, desc in SETS:
        valid = [(d, res) for d, res in rows
                 if max(res[k] for k in keys) < VERIFY_TOL]
        per_set[name] = (len(valid), valid)
        out("  set (%s)  %s" % (name, desc))
        out("      valid d count = %d" % len(valid))
        if not valid:
            # is the set *identically* satisfied (continuum)?
            if all(maxres[k] < 1e-6 for k in keys):
                spot = [DL + (DU - DL) * mpf(i) / 20 for i in range(21)]
                m = max(res_mp(all_keys(d, c, s, p, q)[k])
                        for d in spot for k in keys)
                if m < mpf('1e-15'):
                    out("      IDENTICALLY SATISFIED on the whole interval"
                        " (max spot residue %.2e) -> continuum, cannot match"
                        " a finite oracle count" % float(m))
                else:
                    out("      near-identical on scan grid (max %.2e) but not"
                        " at mpmath spot checks (%.2e)" % (maxres[k], float(m)))
        for d, res in valid:
            tail = ", ".join("%s=%.1e" % (k, float(res[k])) for k in ALL_KEYS)
            out("      d = %s   residues: %s"
                % (mp.nstr(d, 30), tail))
        out("")

    # independent coverage cross-check: every near-integer cluster of the
    # conjoined residue must be matched by a refined valid d
    out("    coverage check (conjoined-residue clusters vs found valid d's):")
    ok = True
    for name, keys, _ in SETS:
        pts = sorted(near[name])
        vd = [d for d, _ in per_set[name][1]]
        if not pts:
            out("        %s: no near-integer grid points (no candidates)" % name)
            continue
        # cluster near points by d within 1e-6
        clusters = []
        for d0 in pts:
            if clusters and d0 - clusters[-1][-1] <= 1e-6:
                clusters[-1].append(d0)
            else:
                clusters.append([d0])
        tol = 200 * step
        bad = 0
        for cl in clusters:
            if not vd or min(abs(c0 - d) for c0 in cl for d in vd) > tol:
                bad += 1
        if bad:
            ok = False
            out("        %s: %d clusters, %d NOT matched by a valid d"
                " (WARNING: possible missed root)" % (name, len(clusters), bad))
        else:
            out("        %s: %d clusters, all matched by a valid d (OK)"
                % (name, len(clusters)))
    out("    coverage %s" % ("OK" if ok else "WARNINGS ABOVE"))
    return per_set


def G_sum(n, N, out, sets_done=None):
    """Sum g over all pairs with s+p+q<=n, p<q, s,p>=5 (c=s+p+q)."""
    pairs = []
    for s in range(5, n + 1):
        for p in range(5, n + 1):
            for q in range(p + 1, n + 1):
                if s + p + q <= n:
                    pairs.append((s + p + q, s, p, q))
    pairs.sort()
    out("")
    out("########## G(%d): %d pairs (c,s,p,q) with s+p+q<=%d "
        "(c=s+p+q) ##########" % (n, len(pairs), n))
    totals = {name: 0 for name, _, _ in SETS}
    for (c, s, p, q) in pairs:
        res = run_case(c, s, p, q, N, "G%d pair" % n, out)
        row = ", ".join("g(%s)=%d" % (name, res[name][0]) for name, _, _ in SETS)
        out("    pair (c,s,p,q)=(%2d,%2d,%2d,%2d): %s"
            % (c, s, p, q, row))
        for name, _, _ in SETS:
            totals[name] += res[name][0]
    out("")
    for name, _, _ in SETS:
        out("  G(%d) set(%s) = %d" % (n, name, totals[name]))
    return totals


def main():
    lines = []

    def out(s=""):
        print(s, flush=True)
        lines.append(s)

    out("PE620  off-centre W-invariant meshing model test")
    out("Source model: research/threads/offcentre-mesh-phase-model.md")
    out("mpmath dps = %d, SCAN_TOL = %g, VERIFY_TOL = 1e-9, N flagships = 1e7"
        % (mp.dps, SCAN_TOL))
    out("Geometry: S=(0,0), C=(d,0); a_t=(s+t)/2pi, b_t=(c-t)/2pi;")
    out("  phi, chi, gamma interior angles at S, C, P (phi+chi+gamma=pi);")
    out("  W_t = s*phi + c*chi - t*gamma, W'_t = s*phi - c*chi + t*gamma.")
    out("Oracle: g(16,5,5,6)=9, G(16)=9, G(20)=205.")
    out("=" * 78)

    per = run_case(16, 5, 5, 6, 10_000_000, "oracle", out)

    sets9 = [name for name, _, _ in SETS if per[name][0] == 9]
    out("")
    out("Sets reproducing g(16,5,5,6)=9: %s" % (sets9 or "NONE"))

    _g16g20 = {}
    for name, _, _ in SETS:
        if per[name][0] == 9:
            G16 = G_sum(16, 10_000_000, out)
            G20 = G_sum(20, 1_000_000, out)
            _g16g20[name] = (G16[name], G20[name])
            out("")
            out("Set (%s): g-flag = 9, G(16) = %d (oracle 9), "
                "G(20) = %d (oracle 205)"
                % (name, G16[name], G20[name]))
            good = (_g16g20[name] == (9, 205))
            out("    -> %s" % ("AGREES 9/9/205" if good else "does not agree"))

    if sets9:
        agree = [name for name, _, _ in SETS
                 if per[name][0] == 9 and name in _g16g20
                 and _g16g20[name] == (9, 205)]
        if agree:
            verdict = ("set %s reproduces 9/9/205 (g(16,5,5,6)=9, G(16)=9,"
                       " G(20)=205)" % agree)
        else:
            verdict = ("no set reproduces 9/9/205; sets with g(16,5,5,6)=9: %s"
                       " (their G sums above disagree)"
                       % [n for n, _, _ in SETS if per[n][0] == 9])
    else:
        verdict = ("no set (A/B/C/D) reproduces 9/9/205; best g(16,5,5,6) "
                   "counts: " + ", ".join(
                       "(%s)=%d" % (name, per[name][0]) for name, _, _ in SETS))
    out("")
    out("VERDICT: " + verdict)

    with open(OUTFILE, "w") as f:
        f.write("\n".join(lines) + "\n")
    out("")
    out("(output written to %s)" % OUTFILE)


if __name__ == "__main__":
    main()