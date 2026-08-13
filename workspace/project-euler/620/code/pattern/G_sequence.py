"""Compute G(n) for n=16..200 by the integer-level formula (no scan),
and dump g for fixed prefixes. Also verify parity condition is vacuous.
g = # integers k strictly between lo=n_p(d_min+) and hi=n_p(d_max-).
"""
import math
import numpy as np
import os

OUT = "/workspace/code/out/G_sequence.txt"
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


def g_of(c, s, p, q):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    eps = 1e-10 * max(1.0, d_max - d_min)
    lo = float(n_arrays(c, s, p, np.array([d_min + eps]))[0])
    hi = float(n_arrays(c, s, p, np.array([d_max - eps]))[0])
    return max(0, int(math.ceil(hi)) - int(math.floor(lo)) - 1)


def all_tuples(n):
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

    # parity vacuous check: s+c+p-q mod 2
    emit("parity condition 2k-(s+c) == p-q (mod2) is algebraically vacuously-")
    emit("satisfied for every attained k because s+c+p-q =")
    emit("  s+(s+p+q)+p-q = 2s+2p == 0 (mod 2).  Confirmed vacuous.")
    emit("")

    # G(n) sequence 16..200
    emit("G(n) for n=16..200 (g summed over s+p+q<=n):")
    Gvals = []
    # cumulative: precompute g for each tuple once
    gcache = {}
    maxc = 200
    for (c, s, p, q) in all_tuples(maxc):
        gcache[(c, s, p, q)] = g_of(c, s, p, q)
    cum = 0
    last = {}
    for n in range(16, 201):
        # add tuples with c==n
        for (c, s, p, q) in all_tuples(n):
            if c == n:
                cum += gcache[(c, s, p, q)]
        Gvals.append((n, cum))
        emit("  G(%3d) = %d" % (n, cum))

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("saved -> %s" % OUT)


if __name__ == "__main__":
    main()
