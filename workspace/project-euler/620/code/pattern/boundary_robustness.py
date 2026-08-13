"""Robustness: find tuples up to n=500 where lo=n_p(d_min+) or hi=n_p(d_max-)
lands within 1e-6 of an integer (where float floor/ceil could go the wrong
way), and re-evaluate those endpoints with mpmath-60.
"""
import math
from mpmath import mp, mpf, pi, atan2, sqrt, fabs

mp.dps = 60


def d_interval(c, s, p, q):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi)
    rp, rq = p / (2 * pi), q / (2 * pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)
    return d_min, d_max


def n_t_mp(c, s, t, d):
    R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi); rho = mpf(t) / (2 * pi)
    a = R - rho; b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y = sqrt(max(a * a - x * x, mpf(0)))
    beta = atan2(y, x); mu = atan2(y, x - d)
    return ((c - t) * beta + (s + t) * mu) / pi


def endpoints_float(c, s, p, q):
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return None
    eps = 1e-11 * max(1.0, d_max - d_min)
    lo = n_t_float(c, s, p, d_min + eps)
    hi = n_t_float(c, s, p, d_max - eps)
    return lo, hi


def n_t_float(c, s, t, d):
    pi = math.pi
    R = c / (2 * pi); r = s / (2 * pi); rho = t / (2 * pi)
    a = R - rho; b = r + rho
    x = (a * a - b * b + d * d) / (2.0 * d)
    y = math.sqrt(max(a * a - x * x, 0.0))
    beta = math.atan2(y, x); mu = math.atan2(y, x - d)
    return ((c - t) * beta + (s + t) * mu) / pi


def count_from(lo, hi):
    return max(0, int(math.ceil(hi)) - int(math.floor(lo)) - 1)


near = []
nmax = 500
count_float = 0
count_mp = 0
for c in range(15, nmax + 1):
    for s in range(5, c - 10):
        for p in range(5, c - s - 5):
            for q in range(p + 1, c - s - p + 1):
                if s + p + q != c:
                    continue
                e = endpoints_float(c, s, p, q)
                if e is None:
                    continue
                lo, hi = e
                g_f = count_from(lo, hi)
                count_float += g_f
                # near-integer boundary detection
                if (abs(lo - round(lo)) < 1e-6) or (abs(hi - round(hi)) < 1e-6):
                    d_min, d_max = d_interval(c, s, p, q)
                    eps = mpf('1e-30')
                    lo_mp = n_t_mp(c, s, p, mpf(d_min) + eps)
                    hi_mp = n_t_mp(c, s, p, mpf(d_max) - eps)
                    g_mp = count_from(float(lo_mp), float(hi_mp))
                    count_mp += g_mp
                    fl = float(lo_mp); fh = float(hi_mp)
                    near.append((c, s, p, q, lo, hi, fl, fh, g_f, g_mp))

print("total G(500) float = %d" % count_float)
print("near-integer-boundary tuples: %d" % len(near))
for row in near[:20]:
    c, s, p, q, lo, hi, fl, fh, gf, gmp = row
    flag = "OK" if gf == gmp else "DIFF"
    print("  (%d,%d,%d,%d) float lo=%.12f hi=%.12f | mp lo=%.12f hi=%.12f | g_float=%d g_mp=%d %s"
          % (c, s, p, q, lo, hi, fl, fh, gf, gmp, flag))
