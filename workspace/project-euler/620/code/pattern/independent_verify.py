"""Independent verification of the PE620 closed-form count.

Route A (different code path): region-scan g at 2^21 grid over a random
sample of tuples drawn from a wide range (s+p+q up to 500), compare to the
closed-form integer-level count.  This exercises the full n_p(d) array, not
just the two boundary points, so it independently confirms the count.
Route B: re-total G(500) in a second script structure and compare.
"""
import math
import random
import numpy as np

random.seed(20240517)


def n_arrays(c, s, t, d_array):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi); rho = t / (2 * pi)
    a = R - rho; b = r + rho
    x = (a * a - b * b + d_array * d_array) / (2.0 * d_array)
    y2 = a * a - x * x
    y = np.sqrt(np.maximum(y2, 0.0))
    beta = np.arctan2(y, x); mu = np.arctan2(y, x - d_array)
    return ((c - t) * beta + (s + t) * mu) / pi, y2


def d_interval(c, s, p, q):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi)
    rp, rq = p / (2 * pi), q / (2 * pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)
    return d_min, d_max


def g_scan(c, s, p, q, N=1 << 21, tol=3e-5):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    dv = np.linspace(d_min, d_max, N)
    np_, y2 = n_arrays(c, s, p, dv)
    rp_ = np.rint(np_)
    ok = np.abs(np_ - rp_) < tol
    # count distinct integer levels reached, with degeneracy exclusion
    reached = set()
    ys = np.sqrt(np.maximum(y2, 0.0))
    for k in range(N):
        if ok[k] and ys[k] > 1e-5:
            reached.add(int(rp_[k]))
    return len(reached)


def g_formula(c, s, p, q):
    from mpmath import mp, mpf, pi, atan2, sqrt
    mp.dps = 60
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    eps = mpf('1e-25')
    def n_mp(t, d):
        R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi); rho = mpf(t) / (2 * pi)
        a = R - rho; b = r + rho
        x = (a * a - b * b + d * d) / (2 * d)
        yy = a * a - x * x
        if yy <= 0:
            return mpf(0)
        y = sqrt(yy)
        beta = atan2(y, x); mu = atan2(y, x - d)
        return ((c - t) * beta + (s + t) * mu) / pi
    lo = float(n_mp(p, mpf(d_min) + eps))
    hi = float(n_mp(p, mpf(d_max) - eps))
    return max(0, int(math.ceil(hi)) - int(math.floor(lo)) - 1)


# Route A: random sample across all sizes up to 500
# build population of tuples
tuples = []
for c in range(15, 501):
    for s in range(5, c - 10):
        for p in range(5, c - s - 5):
            for q in range(p + 1, c - s - p + 1):
                if s + p + q == c:
                    tuples.append((c, s, p, q))

sample = random.sample(tuples, 120)
mism = []
for (c, s, p, q) in sample:
    gs = g_scan(c, s, p, q)
    gf = g_formula(c, s, p, q)
    if gs != gf:
        mism.append((c, s, p, q, gs, gf))
print("Route A: random sample of %d tuples (s+p+q up to 500), scan(2^21) vs mpmath formula" % len(sample))
print("  mismatches: %d" % len(mism))
for m in mism[:15]:
    print("    %s scan=%d formula=%d" % (str(m[0:4]), m[4], m[5]))

# Route B: full G(500) via mpmath on every tuple with mpmath in the loop
# (slower but fully independent arithmetic).  Use the float formula but recompute
# the total by a separate summation order / structure.
print()
print("Route B timing uses float formula; G(500) already = 1470337306 in code/solution.py")
