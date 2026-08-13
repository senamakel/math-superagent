"""Scholar's independent re-verification of the on-disk PE620 computed claims.

Written fresh from the adopted model's formula (approach file
arc-closure-cs-polynomial.md), NOT importing fast_g / n_integer_count, to check
what the workspace's outputs actually establish:

  n_t(d) = [(c-t)*beta + (s+t)*mu]/pi,  beta = angle of tangency point about
  ring centre O, mu = angle about sun centre S (upper tangency point),
  R = c/2pi, r = s/2pi, a_t = R - t/2pi, b_t = r + t/2pi.
  Claim: (i)  n_p(d) + n_q(d) == c + s for EVERY interior d;
         (ii) valid arrangements <-> n_p(d) in Z (n_q then automatic),
              degenerate endpoints excluded, so
         (iii) g(c,s,p,q) = #{ k in Z : n_p(d_min+) < k < n_p(d_max-) },
              d_min = max(|c-s-2p|,|c-s-2q|)/2pi, d_max = (c-s)/2pi - 1.
  Oracle to reproduce: g(16,5,5,6)=9, G(16)=9, G(20)=205.

Also re-runs the grid region-scan of count_formula_test2.py (N=2^17, tol=1e-4)
vs count_formula_test.py (N=2^20, tol=1e-3) on the single tuple (16,5,5,6) to
diagnose the on-disk scan/formula mismatch (6 vs 9).
"""
import math
import numpy as np
from mpmath import mp, mpf, pi, atan2, sqrt, floor, ceil

mp.dps = 60


def n_t_mp(c, s, t, d):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(t) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    y = sqrt(y2)
    beta = atan2(y, x)
    mu = atan2(y, x - d)
    return ((c - t) * beta + (s + t) * mu) / pi


def d_interval(c, s, p, q):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    lo = []
    hi = []
    for t in (p, q):
        a = R - mpf(t) / (2 * pi)
        b = r + mpf(t) / (2 * pi)
        lo.append(abs(a - b))
        hi.append(a + b)
    d_min = max(lo)
    d_max = min(hi + [R - r - 1])
    return d_min, d_max


def g_formula_mp(c, s, p, q):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min >= d_max:
        return 0
    eps = mpf('1e-12') * (d_max - d_min)
    lo = n_t_mp(c, s, p, d_min + eps)
    hi = n_t_mp(c, s, p, d_max - eps)
    # integers k strictly between lo and hi (n_q = c+s-k automatic)
    kmin = int(floor(lo)) + 1
    kmax = int(ceil(hi)) - 1
    return kmin, kmax, max(0, kmax - kmin + 1), lo, hi


def scan(c, s, p, q, N, tol):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min >= d_max:
        return 0
    dv = np.linspace(float(d_min), float(d_max), N)
    def ns(t):
        R = c / (2 * math.pi); r = s / (2 * math.pi); rho = t / (2 * math.pi)
        a = R - rho; b = r + rho
        x = (a * a - b * b + dv * dv) / (2.0 * dv)
        y = np.sqrt(np.maximum(a * a - x * x, 0.0))
        beta = np.arctan2(y, x); mu = np.arctan2(y, x - dv)
        return ((c - t) * beta + (s + t) * mu) / math.pi, y
    np_, yp = ns(p)
    nq, yq = ns(q)
    rp_ = np.rint(np_); rq_ = np.rint(nq)
    sel = (np.abs(np_ - rp_) < tol) & (np.abs(nq - rq_) < tol) \
        & (((rp_.astype(int) - rq_.astype(int)) % 2) == (p - q) % 2)
    regions = 0
    inrun = False
    for k in range(N):
        if sel[k] and not inrun:
            inrun = True; start = k
        elif not sel[k] and inrun:
            inrun = False
            seg = slice(start, k)
            bi = start + int(np.argmin(np.abs(np_[seg] - rp_[seg])
                                       + np.abs(nq[seg] - rq_[seg])))
            if yp[bi] > 1e-5 and yq[bi] > 1e-5:
                regions += 1
    if inrun:
        seg = slice(start, N)
        bi = start + int(np.argmin(np.abs(np_[seg] - rp_[seg])
                                   + np.abs(nq[seg] - rq_[seg])))
        if yp[bi] > 1e-5 and yq[bi] > 1e-5:
            regions += 1
    return regions


def main():
    out = []
    def emit(s_=""):
        print(s_, flush=True); out.append(s_)

    emit("Scholar fresh re-verification of the adopted n_t model")
    emit("=" * 76)

    # (i) identity n_p + n_q == c + s at arbitrary interior d
    emit("\n(i) Identity n_p(d)+n_q(d) == c+s at arbitrary d (mpmath dp60):")
    for (c, s, p, q) in [(16, 5, 5, 6), (20, 7, 6, 7), (30, 9, 6, 12)]:
        d_min, d_max = d_interval(c, s, p, q)
        for f in (0.2, 0.4, 0.6, 0.8):
            d = d_min + f * (d_max - d_min)
            ssum = n_t_mp(c, s, p, d) + n_t_mp(c, s, q, d)
            emit("   (c,s,p,q)=(%d,%d,%d,%d) d=%.6f n_p+n_q=%s (target %d)"
                 % (c, s, p, q, float(d), mp.nstr(ssum, 20), c + s))

    # (iii) formula g on the oracle triple + all G(20) tuples
    emit("\n(iii) g via endpoint formula (strict interior levels):")
    emit("   g(16,5,5,6): kmin..kmax, g = %s"
         % (g_formula_mp(16, 5, 5, 6),))
    tuples = []
    for total in range(16, 21):
        for s in range(5, total - 10):
            for p in range(5, total - s - 5):
                for q in range(p + 1, total - s - p + 1):
                    if s + p + q <= total:
                        t = (s + p + q, s, p, q)
                        if t not in tuples:
                            tuples.append(t)
    tot = 0
    emit("   G(20) per tuple:")
    for (c, s, p, q) in sorted(tuples):
        kmin, kmax, g, lo, hi = g_formula_mp(c, s, p, q)
        tot += g
        emit("     g(%2d,%2d,%2d,%2d) = %d  [k %d..%d, lo=%.4f hi=%.4f]"
             % (c, s, p, q, g, kmin, kmax, float(lo), float(hi)))
    emit("   G(16) = %d,  G(20) = %d  (oracle 9, 205)"
         % (sum(1 for t in tuples if t[0] <= 16), tot))

    # (ii)+(iv) region-scan resolution diagnosis for (16,5,5,6)
    emit("\n(iv) Region scan of (16,5,5,6) vs grid size/tolerance:")
    for (N, tol, tag) in [(1 << 17, 1e-4, "count_formula_test2 params"),
                          (1 << 20, 1e-3, "count_formula_test params"),
                          (1 << 20, 1e-4, "2^20 with tighter tol"),
                          (1 << 22, 1e-4, "2^22 with tighter tol")]:
        gs = scan(16, 5, 5, 6, N, tol)
        emit("   N=2^%d tol=%.0e : scan g = %d   (%s)"
             % (int(math.log2(N)), tol, gs, tag))

    with open("/workspace/code/out/scholar_verify.txt", "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()