"""Derive analytic structure of n_p(DU-) and n_p(DL+).

Geometry at a planet of size t, offset d:
  a_t = R - rho_t  (dist to ring centre O)
  b_t = r + rho_t  (dist to sun centre S)
  beta = angle at O (between +x axis and OP) = atan2(y,x)
  gamma = angle at S = atan2(y, x-d)
  n_t(d) = [(c-t)*beta + (s+t)*gamma]/pi

We know n_p+n_q = s+c (checked).  Explore:
  1. n_p(DL+) where DL=|a_q-b_q| (since q>p the q-pinch wins).  There the
     q-planet's y -> 0, degenerate; n_p finite.
  2. n_p(DU-) where DU=R-r-1 (gap pinch).  There both planets give
     gamma=max angle, the same tangency; find the exact limit.
Try expressing n_p(DU-) and n_p(DL+) and g in closed form.
"""
from mpmath import mp, mpf, pi, atan2, sqrt

mp.dps = 50


def n_t_expr(c, s, t, d):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(t) / (2 * pi)
    a, b = R - rho, r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None
    y = sqrt(y2)
    beta = atan2(y, x)
    gamma = atan2(y, x - d)
    return ((c - t) * beta + (s + t) * gamma) / pi


# c,s,p,q sample; DU = R-r-1 exactly (gap pinch dominates for these).
c, s, p, q = 20, 7, 6, 7
R = mpf(c) / (2 * pi)
r = mpf(s) / (2 * pi)
DU = R - r - 1
rho_p = mpf(p) / (2 * pi)
rho_q = mpf(q) / (2 * pi)
print("c=%d s=%d p=%d q=%d  R=%.10f r=%.10f R-r-1=%.10f" % (c, s, p, q, R, r, DU))
for t in (p, q):
    rho = mpf(t) / (2 * pi)
    a, b = R - rho, r + rho
    # at d=DU, what are x,y?
    x = (a * a - b * b + DU * DU) / (2 * DU)
    y2 = a * a - x * x
    print("  t=%d a=%.8f b=%.8f x=%.8f y2=%.6e" % (t, a, b, x, y2))

# Try a candidate closed form: n_p(DU-) maybe ~ (c-p)/(?) ...
for c in range(16, 28):
    for s in range(5, c - 10):
        for p in range(5, (c - s - 1) // 2 + 1):
            q = c - s - p
            R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi)
            DU = R - r - 1
            rho = mpf(p) / (2 * pi)
            a, b = R - rho, r + rho
            x = (a * a - b * b + DU * DU) / (2 * DU)
            y2 = a * a - x * x
            if y2 <= 0:
                continue
            y = sqrt(y2)
            beta = atan2(y, x)
            gamma = atan2(y, x - DU)
            np = ((c - p) * beta + (s + p) * gamma) / pi
            g = int(mp.floor(np))
            # candidate: floor of ((c-p)+1)? no
            print("c=%2d s=%2d p=%2d q=%2d g=%2d  n_p(DU-)=%.6f  gamma/pi=%.6f beta/pi=%.6f"
                  % (c, s, p, q, g, np, gamma / pi, beta / pi))