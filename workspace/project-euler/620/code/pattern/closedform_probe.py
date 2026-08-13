"""Probe the closed form: compute g and the endpoints lo=lim n_p(d_min+),
hi=lim n_p(d_max-) for many tuples, and look for structure.
g = # integers strictly between lo and hi (interior open interval).

Also confirm n_p monotone increasing and parity-free counting.
"""
import math
import numpy as np
import os

OUT = "/workspace/code/out/closedform_probe.txt"
os.makedirs("/workspace/code/out", exist_ok=True)


def n_arrays(c, s, t, d_array):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi); rho = t / (2 * pi)
    a = R - rho; b = r + rho
    x = (a * a - b * b + d_array * d_array) / (2.0 * d_array)
    y = np.sqrt(np.maximum(a * a - x * x, 0.0))
    beta = np.arctan2(y, x); mu = np.arctan2(y, x - d_array)
    return ((c - t) * beta + (s + t) * mu) / pi


def d_interval(c, s, p, q):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi)
    rp, rq = p / (2 * pi), q / (2 * pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)
    return d_min, d_max


def endpoints(c, s, p, q):
    """lo = n_p(d_min+), hi = n_p(d_max-) via 2-point probes just inside."""
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return None, None
    eps = 1e-12 * max(1.0, d_max - d_min)
    lo = float(n_arrays(c, s, p, np.array([d_min + eps]))[0])
    hi = float(n_arrays(c, s, p, np.array([d_max - eps]))[0])
    return lo, hi


def g_of(c, s, p, q):
    lo, hi = endpoints(c, s, p, q)
    if lo is None:
        return 0
    # integers strictly between lo and hi
    kmin = math.floor(lo); kmax = math.ceil(hi)
    cnt = 0
    for k in range(kmin + 1, kmax):
        cnt += 1
    return cnt


def main():
    out = []
    def emit(s_=""):
        print(s_, flush=True); out.append(s_)

    c, s, p, q = 16, 5, 5, 6
    lo, hi = endpoints(c, s, p, q)
    emit("(16,5,5,6): n_p(interior endpoints) lo=%.6f hi=%.6f g=%d (oracle 9)"
         % (lo, hi, g_of(c, s, p, q)))

    # gather g and lo/hi for all tuples s+p+q<=40, print a table
    tuples = []
    for total in range(15, 41):
        for s in range(5, total - 10):
            for p in range(5, total - s - 5):
                for q in range(p + 1, total - s - p + 1):
                    if s + p + q <= total:
                        t = (s + p + q, s, p, q)
                        if t not in tuples:
                            tuples.append(t)
    tuples.sort()
    emit("")
    emit("table: c=s+p+q | s | p | q | lo | hi | g")
    for (c, s, p, q) in tuples:
        lo, hi = endpoints(c, s, p, q)
        g = g_of(c, s, p, q)
        emit("%3d %3d %3d %3d | %8.4f | %8.4f | %2d"
             % (c, s, p, q, lo, hi, g))

    # G(n) by formula
    def G(n):
        tot = 0
        for (c, s, p, q) in tuples:
            if c <= n:
                tot += g_of(c, s, p, q)
        return tot
    emit("")
    emit("G(16)=%d (oracle 9)  G(20)=%d (oracle 205)  G(30)=%d  G(40)=%d"
         % (G(16), G(20), G(30), G(40)))

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("saved -> %s" % OUT)


if __name__ == "__main__":
    main()
