"""Clean verification: g via 2^20 region scan vs g via integer-level formula.

Exact identity (mpmath-confirmed): n_p(d) + n_q(d) == s + c for every
interior d.  Hence:
  valid d <-> n_p(d)=k in Z (then n_q=s+c-k automatically),
  parity 2k-(s+c) == p-q (mod 2),
  degenerate endpoints excluded.
g_formula = # integers k strictly between n_p(d_min) and n_p(d_max)
            with the parity condition.
g_scan = the region-count scan from n_integer_count.py at 2^20 points.
"""
import math
import numpy as np
import os

OUT = "/workspace/code/out/count_formula_test.txt"
os.makedirs("/workspace/code/out", exist_ok=True)


def n_arrays(c, s, t, d_array):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi); rho = t / (2 * pi)
    a = R - rho; b = r + rho
    x = (a * a - b * b + d_array * d_array) / (2.0 * d_array)
    y = np.sqrt(np.maximum(a * a - x * x, 0.0))
    beta = np.arctan2(y, x); mu = np.arctan2(y, x - d_array)
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


def g_scan(c, s, p, q, tol=1e-3, N=1 << 20):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    dv = np.linspace(d_min, d_max, N)
    np_, yp = n_arrays(c, s, p, dv)
    nq, yq = n_arrays(c, s, q, dv)
    rp_ = np.rint(np_); rq_ = np.rint(nq)
    ok_p = np.abs(np_ - rp_) < tol
    ok_q = np.abs(nq - rq_) < tol
    parity = ((rp_.astype(int) - rq_.astype(int)) % 2)
    sel = ok_p & ok_q & (parity == (p - q) % 2)
    regions = 0
    inrun = False
    for k in range(N):
        if sel[k] and not inrun:
            inrun = True; start = k
        elif not sel[k] and inrun:
            inrun = False
            # exclude degenerate: y too small at the region's best point
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


def g_formula(c, s, p, q):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    # n_p at the two open ends (just inside endpoints)
    np_lo, _ = n_arrays(c, s, p, np.array([d_min + 1e-10]))
    np_hi, _ = n_arrays(c, s, p, np.array([d_max - 1e-10]))
    lo = float(np_lo[0]); hi = float(np_hi[0])
    kmin = math.floor(lo); kmax = math.ceil(hi)
    count = 0
    for k in range(kmin + 1, kmax):
        if (2 * k - (s + c) - (p - q)) % 2 != 0:
            continue
        count += 1
    return count


def main():
    out = []
    def emit(s_=""):
        print(s_, flush=True); out.append(s_)

    tuples = []
    for total in range(15, 31):
        for s in range(5, total - 10):
            for p in range(5, total - s - 5):
                for q in range(p + 1, total - s - p + 1):
                    if s + p + q <= total:
                        t = (s + p + q, s, p, q)
                        if t not in tuples:
                            tuples.append(t)
    tuples.sort()

    emit("tuples to check (s+p+q<=30): %d" % len(tuples))
    mismatches = []
    total_g_scan = 0
    total_g_formula = 0
    for (c, s, p, q) in tuples:
        gs = g_scan(c, s, p, q)
        gf = g_formula(c, s, p, q)
        total_g_scan += gs
        total_g_formula += gf
        if gs != gf:
            mismatches.append((c, s, p, q, gs, gf))
    emit("total g over scan = %d, over formula = %d" % (total_g_scan, total_g_formula))
    emit("mismatches: %d" % len(mismatches))
    for m in mismatches[:20]:
        emit("  MISMATCH %s scan=%d formula=%d" % (str(m[0:4]), m[4], m[5]))

    # G(20) and G(30) by formula
    def G_by_formula(n):
        tots = 0
        for (c, s, p, q) in tuples:
            if c <= n:
                tots += g_formula(c, s, p, q)
        return tots
    emit("G(16)[formula]=%d (oracle 9)" % G_by_formula(16))
    emit("G(20)[formula]=%d (oracle 205)" % G_by_formula(20))
    emit("G(30)[formula]=%d" % G_by_formula(30))

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("saved -> %s" % OUT)


if __name__ == "__main__":
    main()
