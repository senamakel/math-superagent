"""Margin analysis: how close does n_p(DU-) come to an integer, over the
c<=40 tuple set?  If the fractional part is always far from 0/1, float64
floor is safe for the G(500) sum.  Report min distance to nearest integer
and which tuple achieves it.
"""
import math

rows = [tuple(map(int, l.split())) for l in open("/workspace/code/out/mpmath_table.txt")]

# Recompute n_p(DU-) with float64 AND with mpmath for a robust margin.
from mpmath import mp, mpf, pi, atan2, sqrt
mp.dps = 30


def npdu_f64(c, s, p, q):
    R = c / (2 * math.pi)
    r = s / (2 * math.pi)
    rho = p / (2 * math.pi)
    a, b = R - rho, r + rho
    DU = R - r - 1.0
    DL = abs((R - q / (2 * math.pi)) - (r + q / (2 * math.pi)))
    eps = (DU - DL) / 1e7
    d = DU - eps
    x = (a * a - b * b + d * d) / (2 * d)
    y = math.sqrt(max(a * a - x * x, 0.0))
    beta = math.atan2(y, x)
    gamma = math.atan2(y, x - d)
    return ((c - p) * beta + (s + p) * gamma) / math.pi


best = (1.0, None)
for c, s, p, q, g in rows:
    v = npdu_f64(c, s, p, q)
    frac = v - math.floor(v)
    dist = min(frac, 1 - frac)
    if dist < best[0]:
        best = (dist, (c, s, p, q, g, v))
print("min distance of n_p(DU-) to nearest integer:", best[0])
print("tuple:", best[1])
print("worst frac value:", best[1][5] - math.floor(best[1][5]))

# mpmath cross-check of the min-distance tuple
c, s, p, q = best[1][0], best[1][1], best[1][2], best[1][3]
R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi)
rho = mpf(p) / (2 * pi)
a, b = R - rho, r + rho
DU = R - r - 1
DL = abs((R - mpf(q) / (2 * pi)) - (r + mpf(q) / (2 * pi)))
d = DU - (DU - DL) / mpf(10 ** 7)
x = (a * a - b * b + d * d) / (2 * d)
y = sqrt(a * a - x * x)
beta = atan2(y, x); gamma = atan2(y, x - d)
v = ((c - p) * beta + (s + p) * gamma) / pi
frac = v - mp.floor(v)
print("mpmath frac: %.20f  dist to nearest: %.20f" % (frac, min(frac, 1 - frac)))