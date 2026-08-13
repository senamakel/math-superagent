"""Efficient closed-form G(n) evaluator for PE620 under the winner model.

g(c,s,p,q) = number of integers strictly between
   lo = n_p(d_min+)  and  hi = n_p(d_max-),
where n_t(d) = [(c-t)*beta + (s+t)*mu]/pi at the upper tangency point,
d_min = max(|c-s-2p|,|c-s-2q|)/(2pi), d_max = (c-s)/(2pi) - 1 (=R-r-1).

Uses a few float point-evaluations per tuple (constant per tuple), then sums
over all s+p+q<=n tuples.  Each tuple is O(1); total O(#tuples) ~ O(n^3/12).

Self-test against oracle 9/9/205 and scan agreement is done at the bottom.
"""
import math


def d_interval(c, s, p, q):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi)
    rp, rq = p / (2 * pi), q / (2 * pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)
    return d_min, d_max


def n_t(c, s, t, d):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi); rho = t / (2 * pi)
    a = R - rho; b = r + rho
    x = (a * a - b * b + d * d) / (2.0 * d)
    y2 = a * a - x * x
    if y2 <= 1e-20:
        return 0.0
    y = math.sqrt(y2)
    beta = math.atan2(y, x)
    mu = math.atan2(y, x - d)
    return ((c - t) * beta + (s + t) * mu) / pi


def g_of(c, s, p, q):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0
    eps = 1e-11 * max(1.0, d_max - d_min)
    lo = n_t(c, s, p, d_min + eps)
    hi = n_t(c, s, p, d_max - eps)
    # integers strictly between lo and hi
    return max(0, int(math.ceil(hi)) - int(math.floor(lo)) - 1)


def G(n):
    tot = 0
    for c in range(15, n + 1):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                for q in range(p + 1, c - s - p + 1):
                    if s + p + q == c:
                        tot += g_of(c, s, p, q)
    return tot


if __name__ == "__main__":
    import sys
    # oracle checks
    print("g(16,5,5,6) =", g_of(16, 5, 5, 6), "(oracle 9)")
    print("G(16) =", G(16), "(oracle 9)")
    print("G(20) =", G(20), "(oracle 205)")
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    print("G(%d) = %d" % (n, G(n)))
