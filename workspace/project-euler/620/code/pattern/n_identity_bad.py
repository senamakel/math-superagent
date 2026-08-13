"""Locate the exact points where n_p+n_q=c+s fails for (30,8,6,16)."""
import mpmath as mp
mp.mp.dps = 60


def radii(c, s, t):
    pi = mp.pi
    return (c - t) / (2 * pi), (s + t) / (2 * pi)


def angles(c, s, t, d):
    a, b = radii(c, s, t)
    x = (a * a - b * b + d * d) / (2 * d)
    y = mp.sqrt(mp.fabs(a * a - x * x))
    return mp.atan2(y, x), mp.atan2(y, x - d), x, y


def n_t(c, s, t, d):
    beta, mu, _, _ = angles(c, s, t, d)
    return ((c - t) * beta + (s + t) * mu) / mp.pi


c, s, p, q = 30, 8, 6, 16
pi = mp.pi
a_p, b_p = radii(c, s, p)
a_q, b_q = radii(c, s, q)
R = c / (2 * pi); r = s / (2 * pi)
lo = max(abs(a_p - b_p), abs(a_q - b_q))
hi = min(a_p + b_p, a_q + b_q, R - r - 1)
print("d range [%.17g, %.17g]" % (lo, hi))

n = 200000
worst = 0
worst_d = None
for k in range(n):
    d = lo + (hi - lo) * mp.mpf(k) / (n - 1)
    res = abs(n_t(c, s, p, d) + n_t(c, s, q, d) - (c + s))
    if res > worst:
        worst = res
        worst_d = d
print("worst residual %.3e at d=%.17g" % (worst, worst_d))

# near that d, print a few points
for k in range(10):
    d = lo + (hi - lo) * mp.mpf(k) / (n - 1)
    print("  d=%.17g residual=%.3e" % (
        d, abs(n_t(c, s, p, d) + n_t(c, s, q, d) - (c + s))))
