"""Independent high-precision verification of the PE620 winning meshing model.

For (c,s,p,q): n_t(d) = [(c-t)*beta + (s+t)*mu]/pi, with beta, mu at the
upper tangency point of a type-t planet at centre separation d.

Model: valid d  <=>  n_p(d), n_q(d) in Z and n_p(d)-n_q(d) == p-q (mod 2).

Here we:
  (1) independently locate the roots of n_p(d) in Z (each integer level k)
      via the float scan, then refine with mpmath bisection to 60 digits,
      and recompute n_q, n_p+n_q to confirm the structural identity
      n_p + n_q = s + c  holds EXACTLY (not just to scan tolerance);
  (2) confirm at arbitrary NON-valid d that n_p+n_q != s+c (so the identity
      is a genuine valid-configuration constraint, not trivial);
  (3) record the monotone range of n_p over (d_min, d_max).
"""
from mpmath import mp, mpf, pi, atan2, sqrt, fabs
import numpy as np
import math
import os

mp.dps = 60
OUT = "/workspace/code/out/winner_refine.txt"
os.makedirs("/workspace/code/out", exist_ok=True)


def n_exact(c, s, t, d, side=1):
    """High-precision n_t(d) = [(c-t)*beta + (s+t)*mu]/pi."""
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
    mu = atan2(y, x - d)
    if side == -1:
        beta = -beta
        mu = -mu
    return ((c - t) * beta + (s + t) * mu) / pi


def find_root(c, s, p, q, k, d0, window):
    """Refine the d for which n_p(d) = k near d0."""
    # n_p(d) increasing in d; bisect n_p(d)-k = 0
    lo = mpf(d0) - mpf(window)
    hi = mpf(d0) + mpf(window)
    flo = n_exact(c, s, p, lo) - k
    fhi = n_exact(c, s, p, hi) - k
    if flo * fhi > 0:
        # widen
        for _ in range(8):
            lo -= mpf(window)
            hi += mpf(window)
            flo = n_exact(c, s, p, lo) - k
            fhi = n_exact(c, s, p, hi) - k
            if flo * fhi <= 0:
                break
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = n_exact(c, s, p, mid) - k
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    d = (lo + hi) / 2
    return d, n_exact(c, s, p, d), n_exact(c, s, q, d)


def n_scan_array(c, s, t, d_array):
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
    return ((c - t) * beta + (s + t) * mu) / pi


def main():
    c, s, p, q = 16, 5, 5, 6
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi)
    rp, rq = p / (2 * pi), q / (2 * pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)

    out = []
    def emit(s_=""):
        print(s_, flush=True)
        out.append(s_)

    emit("Winner-model high-precision check  (c,s,p,q)=(16,5,5,6)")
    emit("n_t=[(c-t)beta+(s+t)mu]/pi; valid iff n_p,n_q in Z, parity p-q;")
    emit("d_min=%.12f d_max=%.12f" % (d_min, d_max))
    emit("=" * 76)

    # locate integer levels of n_p by scan, then refine each with mpmath
    N = (1 << 20) + 1
    dv = np.linspace(d_min, d_max, N)
    np_ = n_scan_array(c, s, p, dv)
    # find d for each integer k by crossing detection (monotone increasing)
    roots = []
    kmin = int(math.floor(np_[0]))
    kmax = int(math.ceil(np_[-1]))
    emit("n_p range over d-grid: %.4f .. %.4f  (integers %d..%d)"
         % (np_[0], np_[-1], kmin, kmax))
    for k in range(kmin, kmax + 1):
        idx = np.where(np.diff(np.signbit(np_ - k)) != 0)[0]
        if idx.size > 0:
            i0 = idx[0]
            d0 = float(dv[i0])
            # if exactly integer we may land between; take flanking
            d, nP, nQ = find_root(c, s, p, q, k, d0, 5 * (d_max - d_min) / N)
            # exclude degenerate endpoints: y of p or q ~ 0
            def y_at(t, d):
                rho = t / (2 * pi); a = R - rho; b = r + rho
                x = (a * a - b * b + d * d) / (2 * d)
                return float(sqrt(max(mp.mpf(a * a - x * x), 0)))
            yp = y_at(p, d)
            yq = y_at(q, d)
            roots.append((k, d, nP, nQ, yp, yq))
    emit("integer-level roots of n_p (before degenerate exclusion): %d" % len(roots))
    rows = []
    for (k, d, nP, nQ, yp, yq) in roots:
        ngap_p = fabs(nP - mp.mpf(k))
        ngap_q = fabs(nQ - mp.nint(nQ))
        # identity check
        sum_ = nP + nQ
        par = (mp.nint(nP) - mp.nint(nQ)) % 2
        valid = (ngap_p < mpf('1e-30')) and (ngap_q < mpf('1e-30')) \
            and (par == (p - q) % 2) and (yp > 1e-8) and (yq > 1e-8)
        rows.append((k, d, nP, nQ, sum_, float(yp), float(yq), valid))
        emit("  n_p level k=%2d  d=%.30f" % (k, float(d)))
        emit("      n_p=%s" % mp.nstr(nP, 25))
        emit("      n_q=%s" % mp.nstr(nQ, 25))
        emit("      n_p+n_q=%s  (target s+c=%d)  |n_q-round|=%.2e  y_p=%.2e y_q=%.2e  valid=%s"
             % (mp.nstr(sum_, 25), s + c, float(ngap_q), yp, yq, valid))

    g = sum(1 for r_ in rows if r_[7])
    emit("")
    emit("g(16,5,5,6) after degenerate+maxgap filter = %d  (oracle 9)  %s"
         % (g, "AGREE" if g == 9 else "DISAGREE"))
    emit("")
    emit("Identity n_p+n_q == s+c (= %d) at every valid root:" % (s + c))
    emit("  sums: %s" % ", ".join("%.1f" % r_[4] for r_ in rows))

    # confirm at arbitrary non-valid d the sum is not s+c
    np.random.seed(1)
    emit("")
    emit("Probe: at arbitrary d, is n_p(d)+n_q(d) = s+c trivially?")
    for _ in range(5):
        d = d_min + (d_max - d_min) * float(np.random.rand())
        nP = n_exact(c, s, p, mp.mpf(d))
        nQ = n_exact(c, s, q, mp.mpf(d))
        emit("  d=%.12f  n_p+n_q=%.20f   (s+c=%d, difference %.2e)"
             % (d, float(nP + nQ), s + c, float(nP + nQ - (s + c))))

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Output saved to %s" % OUT)


if __name__ == "__main__":
    main()