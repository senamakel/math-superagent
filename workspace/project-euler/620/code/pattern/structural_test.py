"""Test the structural conjectures of the PE620 winner model.

Model (from code/pattern/n_integer_count.py, reproduces 9/9/205):
  n_t(d) = [(c-t)*beta + (s+t)*mu]/pi,  beta=angle of planet centre about
  ring centre O=(0,0), mu=angle about sun centre S=(d,0), at the UPPER
  tangency point of a type-t planet.
  Valid d  <=>  n_p(d), n_q(d) in Z  and  n_p(d)-n_q(d) == p-q (mod 2),
  with degenerate endpoints (y~0) excluded.

Conjectures to test:
  C1 (identity):  n_p(d) + n_q(d) == s + c   for ALL d in [d_min, d_max]
                  (so n_q integrality is implied by n_p integrality).
  C2 (count):     g(c,s,p,q) == # of integers k with n_p(d_k)=k for an
                  interior non-degenerate d and 2k-(s+c) == p-q (mod 2)
                  [parity].  If n_p is monotone increasing, each integer k
                  is attained at exactly one d.
  C3 (monotonic): n_p strictly increasing on (d_min, d_max).
"""
import math
import numpy as np
import os

OUT = "/workspace/code/out/structural_test.txt"
os.makedirs("/workspace/code/out", exist_ok=True)


def n_arrays(c, s, t, d_array):
    pi = math.pi
    R = c / (2 * pi)
    r = s / (2 * pi)
    rho = t / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d_array * d_array) / (2.0 * d_array)
    y = np.sqrt(np.maximum(a * a - x * x, 0.0))
    beta = np.arctan2(y, x)
    mu = np.arctan2(y, x - d_array)
    return ((c - t) * beta + (s + t) * mu) / pi, y


def d_interval(c, s, p, q):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi)
    rp, rq = p / (2 * pi), q / (2 * pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)
    return d_min, d_max


def g_scan(c, s, p, q, tol=1e-3, N=None):
    """Grid-scan g (as in n_integer_count.py)."""
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    if N is None:
        N = (1 << 20) + 1
    dv = np.linspace(d_min, d_max, N)
    np_, yp = n_arrays(c, s, p, dv)
    nq, yq = n_arrays(c, s, q, dv)
    rp_ = np.rint(np_)
    rq_ = np.rint(nq)
    ok_p = np.abs(np_ - rp_) < tol
    ok_q = np.abs(nq - rq_) < tol
    parity = ((rp_.astype(int) - rq_.astype(int)) % 2)
    sel = ok_p & ok_q & (parity == (p - q) % 2)
    # select one representative per contiguous valid region
    regions = 0
    inrun = False
    for k in range(N):
        if sel[k] and not inrun:
            inrun = True
        elif not sel[k] and inrun:
            inrun = False
            regions += 1
    if inrun:
        regions += 1
    # also count only non-degenerate regions
    return regions


def g_formula(c, s, p, q, N=None):
    """Conjecture C2: count of integer levels of n_p in the interior."""
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0, 0.0, 0.0
    if N is None:
        N = (1 << 20) + 1
    dv = np.linspace(d_min, d_max, N)
    # add tiny interior offset to avoid endpoint degeneracy in the value at edge
    np_lo, yp_lo = n_arrays(c, s, p, np.array([d_min + 1e-9]))
    np_hi, yp_hi = n_arrays(c, s, p, np.array([d_max - 1e-9]))
    lo = float(np_lo[0])
    hi = float(np_hi[0])
    # integers k strictly between... actually attained integers: k with
    # floor(lo) < k < ceil(hi), choosing interior.  Use: k in (lo, hi).
    kmin = math.floor(lo)
    kmax = math.ceil(hi)
    count = 0
    for k in range(kmin + 1, kmax):  # strictly interior integers
        # parity condition 2k-(s+c) == p-q (mod 2)
        if (2 * k - (s + c) - (p - q)) % 2 != 0:
            continue
        count += 1
    return count, lo, hi


def main():
    out = []
    def emit(s_=""):
        print(s_, flush=True)
        out.append(s_)

    # ---------- C1 identity over G(20) pairs ----------
    pairs20 = [(s + p + q, s, p, q)
               for s in range(5, 20 - 10)
               for p in range(5, 20 - s - 5)
               for q in range(p + 1, 20 - s - p + 1)]

    emit("=== C1: is n_p(d)+n_q(d) == s+c identically over d? (fine grid) ===")
    W_ID = 1e-9
    c1_bad = []
    Nc1 = (1 << 16) + 1
    for (c, s, p, q) in sorted(pairs20):
        d_min, d_max = d_interval(c, s, p, q)
        if d_min > d_max:
            continue
        dv = np.linspace(d_min, d_max, Nc1)
        np_, _ = n_arrays(c, s, p, dv)
        nq, _ = n_arrays(c, s, q, dv)
        diff = np.max(np.abs(np_ + nq - (s + c)))
        if diff > W_ID:
            c1_bad.append((c, s, p, q, diff))
    emit("pairs checked: %d, identity failures: %d" % (len(pairs20), len(c1_bad)))
    for b in c1_bad[:10]:
        emit("  FAIL %s  maxdiff=%.3e" % (str(b[0:4]), b[4]))

    # ---------- C2 count formula vs scan, over many more tuples ----------
    emit("")
    emit("=== C2: g_scan(region count) vs g_formula(integer-level count) ===")
    Nscan = (1 << 16) + 1   # medium grid for scan (fast, tol tight)
    mismatches = []
    ncheck = 0
    # all tuples s+p+q <= 30
    tuples = []
    for total in range(15, 31):
        for s in range(5, total - 10):
            for p in range(5, total - s - 5):
                for q in range(p + 1, total - s - p + 1):
                    if s + p + q <= total:
                        tuples.append((s + p + q, s, p, q))
    tuples = list(dict.fromkeys(tuples))
    emit("checking %d distinct tuples (s+p+q<=30) at N=2^16+1 grid" % len(tuples))
    for (c, s, p, q) in tuples:
        gs = g_scan(c, s, p, q, tol=1e-3, N=Nscan)
        gf, lo, hi = g_formula(c, s, p, q, N=Nscan)
        ncheck += 1
        if gs != gf:
            mismatches.append((c, s, p, q, gs, gf, lo, hi))
    emit("checked %d tuples, scan-vs-formula mismatches: %d" % (ncheck, len(mismatches)))
    for m in mismatches[:5]:
        emit("  MISMATCH %s  scan=%d formula=%d (lo=%.4f hi=%.4f)" %
             (str(m[0:4]), m[4], m[5], m[6], m[7]))

    # ---------- C3 monotonicity ----------
    emit("")
    emit("=== C3: n_p monotone increasing over (d_min,d_max)? ===")
    mono_bad = []
    for (c, s, p, q) in tuples:
        d_min, d_max = d_interval(c, s, p, q)
        if d_min > d_max:
            continue
        dv = np.linspace(d_min, d_max, Nc1)
        np_, _ = n_arrays(c, s, p, dv)
        if np.any(np.diff(np_) < -1e-7):
            mono_bad.append((c, s, p, q))
    emit("monotonicity failures: %d" % len(mono_bad))

    # ---------- high-precision identity check for the oracle case ----------
    emit("")
    emit("=== C1 high-precision (mpmath) for (16,5,5,6) at 40 sample d ===")
    from mpmath import mp, mpf, pi, atan2, sqrt, fabs
    mp.dps = 60
    c, s, p, q = 16, 5, 5, 6
    d_min, d_max = d_interval(c, s, p, q)
    def n_t_mp(c, s, t, d):
        R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi); rho = mpf(t) / (2 * pi)
        a = R - rho; b = r + rho
        x = (a * a - b * b + d * d) / (2 * d)
        y = sqrt(max(a * a - x * x, 0))
        beta = atan2(y, x); mu = atan2(y, x - d)
        return ((c - t) * beta + (s + t) * mu) / pi
    worst = mpf(0)
    for k in range(40):
        d = mpf(d_min) + (mpf(d_max) - mpf(d_min)) * mp.mpf(k) / mp.mpf(39)
        if k in (0, 39):
            d = (mpf(d_min) + mpf(d_max)) / 2  # avoid degenerate edges
        np_ = n_t_mp(c, s, p, d)
        nq = n_t_mp(c, s, q, d)
        diff = fabs(np_ + nq - mpf(s + c))
        if diff > worst:
            worst = diff
    emit("worst |n_p+n_q-(s+c)| over 40 interior d (mpmath-60): %.2e" % worst)

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("saved -> %s" % OUT)


if __name__ == "__main__":
    main()
