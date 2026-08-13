"""Verification pipeline for the PE620 closed form

    g(c,s,p,q) = #{ k in Z : n_p(DL) < k < n_p(DU) },
    n_t(d) = [(c-t)*beta + (s+t)*gamma]/pi,
    DL = max_t |a_t - b_t|,  DU = min_t (a_t + b_t, R - r - 1),
    a_t = R - rho_t, b_t = r + rho_t   (R = c/2pi, r = s/2pi, rho_t = t/2pi)

(the model of code/pattern/closedform.py and code/solution.py, previously
validated by the n_integer oracle scan: g(16,5,5,6)=9, G(16)=9, G(20)=205).

Steps:
  --steps abc : (1) run code/pattern/closedform.py vs mpmath_table.txt (c<=38)
                (a) G(n) 16..200 via g_of vs every line of G_sequence.txt
                (b) G(500) via g_of  ->  writes G500_value.txt
                (c) hybrid precision: every tuple c<=500, distance of
                    n_p(DL+eps), n_p(DU-eps) to nearest integer; flag < 1e-7
                    and re-evaluate flagged tuples at mpmath dps=60
  --steps d --scan-lo L --scan-hi H :
                (d) independent scan: integer levels of n_p on a 2^21 grid
                    over (DL,DU), excluding degenerate y_p<=1e-5, vs g_of;
                    results cached in scan_cache_c40.txt (resumable)
  --steps e    : (e) G(16/20/30/40) from the scan cache (needs c<=40 scanned),
                    compared to oracle values and G_sequence.txt lines

All output appended to /workspace/code/out/verify_G500.txt.
"""
import os
import re
import subprocess
import sys
import time

import numpy as np
from mpmath import mp, mpf, pi, atan2, sqrt

from solution import g_of, d_interval, n_t
from pattern.n_integer_count import valid_ds

REPORT = "/workspace/code/out/verify_G500.txt"
CACHE = "/workspace/code/out/scan_cache_c40.txt"
GVAL = "/workspace/code/out/G500_value.txt"
MPTAB = "/workspace/code/out/mpmath_table.txt"
GSEQ = "/workspace/code/out/G_sequence.txt"

mp.dps = 60


def log(text=""):
    print(text, flush=True)
    with open(REPORT, "a") as f:
        f.write(text + "\n")


def tuples(lo, hi):
    """All (c,s,p,q) with 15<=c<=hi, s+p+q=c, s,p>=5, p<q (PE620 domain)."""
    out = []
    for c in range(max(15, lo), hi + 1):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                for q in range(p + 1, c - s - p + 1):
                    if s + p + q == c:
                        out.append((c, s, p, q))
    return out


def g_mp60(c, s, p, q):
    """Bisection ground truth at dps=60: count strictly interior, non-
    degenerate (y_p,y_q > 1e-7) roots of n_p(d) = k over (DL,DU)."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)

    def geom(t, d):
        rho = mpf(t) / (2 * pi)
        a = R - rho
        b = r + rho
        x = (a * a - b * b + d * d) / (2 * d)
        y2 = a * a - x * x
        if y2 <= 0:
            return None
        return a, b, x, sqrt(y2)

    def n_tm(t, d):
        g = geom(t, d)
        if g is None:
            return None
        a, b, x, y = g
        beta = atan2(y, x)
        gamma = atan2(y, x - d)
        return ((c - t) * beta + (s + t) * gamma) / pi

    lowers, uppers = [], []
    for t in (p, q):
        rho = mpf(t) / (2 * pi)
        a, b = R - rho, r + rho
        lowers.append(abs(a - b))
        uppers.append(a + b)
    DL = max(lowers)
    DU = min(uppers + [R - r - 1])
    if DL >= DU:
        return 0
    eps = (DU - DL) / mpf(10 ** 9)
    nlo = n_tm(p, DL + eps)
    nhi = n_tm(p, DU - eps)
    if nlo is None or nhi is None or nlo > nhi:
        return 0
    kmin = int(mp.ceil(nlo))
    kmax = int(mp.floor(nhi))
    cnt = 0
    for k in range(kmin, kmax + 1):
        a, b = DL + eps, DU - eps
        fa = n_tm(p, a) - k
        fb = n_tm(p, b) - k
        if fa * fb > 0:
            continue
        for _ in range(250):
            m = (a + b) / 2
            fm = n_tm(p, m) - k
            if fa * fm <= 0:
                b, fb = m, fm
            else:
                a, fa = m, fm
        d = (a + b) / 2
        yp = geom(p, d)[3]
        yq = geom(q, d)[3]
        if d > DL and d < DU and yp > mpf('1e-7') and yq > mpf('1e-7'):
            cnt += 1
    return cnt


def parse_gseq():
    """G_sequence.txt -> {n: G(n)} for the n=16..200 lines."""
    vals = {}
    for line in open(GSEQ):
        m = re.search(r"G\(\s*(\d+)\)\s*=\s*(\d+)", line)
        if m:
            vals[int(m.group(1))] = int(m.group(2))
    return vals


def step1():
    """Run code/pattern/closedform.py (closed form vs mpmath table, c<=38)."""
    log("=" * 76)
    log("STEP 1: code/pattern/closedform.py vs mpmath_table.txt (c<=38)")
    log("=" * 76)
    r = subprocess.run([sys.executable, "code/pattern/closedform.py"],
                       cwd="/workspace", capture_output=True, text=True)
    out = r.stdout
    log(out)
    m = re.search(r"checked (\d+) tuples; disagreements: (\d+)", out)
    if m:
        n = int(m.group(1))
        bad = int(m.group(2))
    else:
        n, bad = -1, -1
        log("WARNING: could not parse closedform.py summary line")
    log("STEP 1 VERDICT: checked=%d disagreements=%d %s"
        % (n, bad, "OK (expect 0)" if bad == 0 else "FAIL"))
    return bad == 0


def step_a():
    """(a) G(n) for n=16..200 via g_of vs every line of G_sequence.txt."""
    log("")
    log("=" * 76)
    log("STEP (a): G(n) n=16..200 via g_of vs G_sequence.txt")
    log("=" * 76)
    gseq = parse_gseq()
    if len(gseq) != 185:
        log("parsed %d G-lines from G_sequence.txt (expected 185):"
            % len(gseq))
    t0 = time.time()
    per_c = {}
    for (c, s, p, q) in tuples(15, 200):
        per_c[c] = per_c.get(c, 0) + g_of(c, s, p, q)
    cum = 0
    disc = 0
    nmis = 0
    for n in range(16, 201):
        cum += per_c.get(n, 0)
        if n in gseq and gseq[n] != cum:
            disc += abs(cum - gseq[n])
            nmis += 1
            if nmis <= 10:
                log("  MISMATCH n=%d: file=%d recomputed=%d" % (n, gseq[n], cum))
    log("recomputed G(16..200) in %.1f s; total discrepancy=%d over %d mismatched"
        " n-lines" % (time.time() - t0, disc, nmis))
    log("STEP (a) VERDICT: %s" % ("OK (expect 0)" if disc == 0 else "FAIL"))


def step_b():
    """(b) G(500) via g_of; write G500_value.txt with just the integer."""
    log("")
    log("=" * 76)
    log("STEP (b): G(500) via g_of  (all s+p+q<=500 tuples)")
    log("=" * 76)
    tup = tuples(15, 500)
    log("tuples: %d" % len(tup))
    t0 = time.time()
    G500 = 0
    per_c = {}
    for (c, s, p, q) in tup:
        per_c[c] = per_c.get(c, 0) + g_of(c, s, p, q)
    for c in per_c:
        G500 += per_c[c]
    dt = time.time() - t0
    log("G(500) = %d   (%.1f s, %d tuples)" % (G500, dt, len(tup)))
    with open(GVAL, "w") as f:
        f.write("%d\n" % G500)
    log("wrote %s" % GVAL)


def step_c():
    """(c) hybrid precision: endpoint distances to nearest integer for every
    tuple c<=500; flag < 1e-7 and re-evaluate flagged at dps=60."""
    log("")
    log("=" * 76)
    log("STEP (c): hybrid precision pass over all tuples c<=500")
    log("=" * 76)
    tup = tuples(15, 500)
    t0 = time.time()
    flagged = []
    dmin_all = 1.0
    n_eval = 0
    for (c, s, p, q) in tup:
        DL, DU = d_interval(c, s, p, q)
        if DL >= DU:
            continue
        eps = 1e-11 * max(1.0, DU - DL)
        vlo = n_t(c, s, p, DL + eps)
        vhi = n_t(c, s, p, DU - eps)
        dlo = abs(vlo - round(vlo))
        dhi = abs(vhi - round(vhi))
        m = min(dlo, dhi)
        if m < dmin_all:
            dmin_all = m
        n_eval += 1
        if m < 1e-7:
            flagged.append((c, s, p, q, dlo, dhi, vlo, vhi))
    log("tuples evaluated (DL<DU): %d / %d in %.1f s"
        % (n_eval, len(tup), time.time() - t0))
    log("smallest endpoint-to-integer distance over all tuples: %.3e" % dmin_all)
    log("flagged (distance < 1e-7): %d" % len(flagged))
    changed = 0
    for (c, s, p, q, dlo, dhi, vlo, vhi) in flagged[:50]:
        g1 = g_of(c, s, p, q)
        g2 = g_mp60(c, s, p, q)
        log("  flagged c=%d s=%d p=%d q=%d  dlo=%.3e dhi=%.3e  "
            "g_of=%d g_mp60=%d" % (c, s, p, q, dlo, dhi, g1, g2))
        if g1 != g2:
            changed += 1
    if len(flagged) > 50:
        for (c, s, p, q, _, _, _, _) in flagged[50:]:
            if g_of(c, s, p, q) != g_mp60(c, s, p, q):
                changed += 1
    log("STEP (c) VERDICT: flagged=%d, g changed by re-evaluation: %d %s"
        % (len(flagged), changed, "OK (expect 0)" if changed == 0 else "FAIL"))


def scan_cache_load():
    d = {}
    if os.path.exists(CACHE):
        for line in open(CACHE):
            parts = line.split()
            if len(parts) == 5:
                c, s, p, q, g = map(int, parts)
                d[(c, s, p, q)] = g
    return d


def step_d(lo, hi):
    """(d) independent scan chunk: integer levels of n_p on a 2^21 grid over
    (DL,DU), non-degenerate (y_p,y_q > 1e-5), vs g_of.  Cache-resumable."""
    log("")
    log("=" * 76)
    log("STEP (d): scan chunk c=[%d..%d]  (2^21 grid, tol=1e-3, y>1e-5)"
        % (lo, hi))
    log("=" * 76)
    cache = scan_cache_load()
    tup = tuples(lo, hi)
    new = 0
    t0 = time.time()
    for (c, s, p, q) in tup:
        if (c, s, p, q) in cache:
            continue
        gs = len(valid_ds(c, s, p, q, tol=1e-3, N=1 << 21))
        cache[(c, s, p, q)] = gs
        with open(CACHE, "a") as f:
            f.write("%d %d %d %d %d\n" % (c, s, p, q, gs))
        new += 1
    dt = time.time() - t0
    log("chunk: %d tuples (%d new cached) in %.1f s (%.2f s/tuple)"
        % (len(tup), new, dt, dt / max(1, len(tup))))

    # compare g_scan vs g_of for this chunk
    mism = []
    for (c, s, p, q) in tup:
        gs = cache[(c, s, p, q)]
        gf = g_of(c, s, p, q)
        if gs != gf:
            mism.append((c, s, p, q, gs, gf))
    log("scan-vs-g_of mismatches in c=[%d..%d]: %d" % (lo, hi, len(mism)))
    for (c, s, p, q, gs, gf) in mism[:10]:
        DL, DU = d_interval(c, s, p, q)
        log("  MISMATCH c=%d s=%d p=%d q=%d g_scan=%d g_of=%d DL=%.6f DU=%.6f"
            % (c, s, p, q, gs, gf, DL, DU))

    # cross-check against mpmath table where rows exist (c<=38)
    tab = {}
    if os.path.exists(MPTAB):
        for line in open(MPTAB):
            parts = line.split()
            if len(parts) == 5:
                c, s, p, q, g = map(int, parts)
                tab[(c, s, p, q)] = g
    tmis = [(k, cache[k], v) for k, v in tab.items()
            if lo <= k[0] <= hi and cache.get(k) != v]
    log("scan-vs-mpmath_table mismatches (c<=38 rows in chunk): %d" % len(tmis))
    for (k, gs, gt) in tmis[:10]:
        log("  MISMATCH c,s,p,q=%s g_scan=%d table=%d" % (k, gs, gt))
    log("STEP (d) VERDICT (c=[%d..%d]): %s"
        % (lo, hi, "OK (expect 0)" if not mism and not tmis else "FAIL"))


def step_e():
    """(e) G(16/20/30/40) from the scan cache (needs coverage), vs oracle and
    G_sequence.txt."""
    log("")
    log("=" * 76)
    log("STEP (e): G(16/20/30/40) from scan cache")
    log("=" * 76)
    cache = scan_cache_load()
    if not cache:
        log("scan cache empty -- run --steps d chunks first")
        return
    maxc = max(k[0] for k in cache)
    # coverage check: for c<=maxc, all expected tuples present?
    missing = []
    for (c, s, p, q) in tuples(15, maxc):
        if (c, s, p, q) not in cache:
            missing.append((c, s, p, q))
    log("scan cache: tuples=%d, max c=%d, missing in [15..%d]: %d"
        % (len(cache), maxc, maxc, len(missing)))
    if missing:
        log("  first missing: %s" % (missing[:5],))
        log("STEP (e): cannot report G values reliably; run --steps d chunks"
            " to complete c<=40")
        return
    gseq = parse_gseq()
    sum_by_c = {}
    for (c, s, p, q), g in cache.items():
        sum_by_c[c] = sum_by_c.get(c, 0) + g
    cum = 0
    for N in (16, 20, 30, 40):
        cum += sum_by_c.get(N, 0)
        oracle = {16: 9, 20: 205}.get(N)
        seq = gseq.get(N)
        log("  G(%d) [scan] = %d   (G_sequence.txt: %s%s)"
            % (N, cum, seq, "" if seq == cum else "  *** MISMATCH ***"))
        if oracle is not None:
            log("       oracle %d: %s" % (oracle,
                "AGREE" if oracle == cum else "DISAGREE"))
    g40 = cum
    log("STEP (e): G(30), G(40) from the c<=%d scan: %s"
        % (maxc, "reported above" if maxc >= 40 else "G(40) NOT FEASIBLE"
           " (need scan through c=40)"))
    log("  (G(40) value = %d)" % g40)


def main():
    args = sys.argv[1:]
    if "--steps" not in args:
        print(__doc__)
        return
    steps = args[args.index("--steps") + 1]
    os.makedirs("/workspace/code/out", exist_ok=True)
    if "abc" in steps:
        ok1 = step1()
        step_a()
        step_b()
        step_c()
        log("")
        log("PIPELINE (abc) DONE -- primary G(500) recorded above; "
            "step-1-ok=%s" % ok1)
    if "d" in steps:
        if "--scan-lo" not in args or "--scan-hi" not in args:
            print("--steps d needs --scan-lo L --scan-hi H")
            return
        lo = int(args[args.index("--scan-lo") + 1])
        hi = int(args[args.index("--scan-hi") + 1])
        step_d(lo, hi)
    if "e" in steps:
        step_e()


if __name__ == "__main__":
    main()