"""Extend scan-vs-formula verification to n<=45 (2^17 grid) and re-check G(30)."""
import math
import numpy as np
import os

OUT = "/workspace/code/out/count_formula_test2.txt"
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


def g_scan(c, s, p, q, tol=1e-4, N=1 << 17):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    dv = np.linspace(d_min, d_max, N)
    np_, yp = n_arrays(c, s, p, dv)
    nq, yq = n_arrays(c, s, q, dv)
    rp_ = np.rint(np_); rq_ = np.rint(nq)
    ok = np.abs(np_ - rp_) < tol
    regions = 0
    inrun = False
    for k in range(N):
        if ok[k] and not inrun:
            inrun = True; start = k
        elif not ok[k] and inrun:
            inrun = False
            seg = slice(start, k)
            bi = start + int(np.argmin(np.abs(np_[seg] - rp_[seg])))
            if yp[bi] > 1e-5:
                regions += 1
    if inrun:
        seg = slice(start, N)
        bi = start + int(np.argmin(np.abs(np_[seg] - rp_[seg])))
        if yp[bi] > 1e-5:
            regions += 1
    return regions


def g_formula(c, s, p, q):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    eps = 1e-10 * max(1.0, d_max - d_min)
    lo = float(n_arrays(c, s, p, np.array([d_min + eps]))[0][0])
    hi = float(n_arrays(c, s, p, np.array([d_max - eps]))[0][0])
    return max(0, int(math.ceil(hi)) - int(math.floor(lo)) - 1)


def tuples_upto(n):
    tups = []
    for c in range(15, n + 1):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                for q in range(p + 1, c - s - p + 1):
                    if s + p + q == c:
                        tups.append((c, s, p, q))
    return tups


def main():
    out = []
    def emit(s_=""):
        print(s_, flush=True); out.append(s_)

    tups = tuples_upto(45)
    emit("tuples s+p+q<=45: %d" % len(tups))
    mism = []
    tot_s = tot_f = 0
    for (c, s, p, q) in tups:
        gs = g_scan(c, s, p, q)
        gf = g_formula(c, s, p, q)
        tot_s += gs; tot_f += gf
        if gs != gf:
            mism.append((c, s, p, q, gs, gf))
    emit("total scan=%d formula=%d mismatches=%d" % (tot_s, tot_f, len(mism)))
    for m in mism[:15]:
        emit("  MISMATCH %s scan=%d formula=%d" % (str(m[0:4]), m[4], m[5]))

    def G(n):
        return sum(g_formula(*t) for t in tuples_upto(n) if t[0] <= n)
    emit("G(30)[formula]=%d (expect 4538)" % G(30))
    emit("G(45)[formula]=%d" % G(45))

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("saved -> %s" % OUT)


if __name__ == "__main__":
    main()
