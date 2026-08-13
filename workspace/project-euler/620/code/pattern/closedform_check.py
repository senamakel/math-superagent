"""Closed-form G check + search for a rational closed form of n_p(DU-).

1) g = floor(n_p(R-r-1)) reproduces G(16)=9 and G(20)=205 (an independent
   route: two endpoint evals, no bisection, no level enumeration).
2) Try to express n_p(DU-) as a closed form in c,s,p by testing, with high
   precision, a few candidate rational expressions; also print the exact
   angle argument (beta/pi, gamma/pi) to spot structure.
"""
import math
from mpmath import mp, mpf, pi, atan2, sqrt

mp.dps = 60


def np_du(c, s, p, q):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(p) / (2 * pi)
    a, b = R - rho, r + rho
    DU = R - r - 1
    rho_q = mpf(q) / (2 * pi)
    a_q, b_q = R - rho_q, r + rho_q
    DL = abs(a_q - b_q)
    d = DU - (DU - DL) / mpf(10 ** 9)
    x = (a * a - b * b + d * d) / (2 * d)
    y = sqrt(a * a - x * x)
    beta = atan2(y, x)
    gamma = atan2(y, x - d)
    return ((c - p) * beta + (s + p) * gamma) / pi


def G_closed(n):
    tot = 0
    for c in range(16, n + 1):
        for s in range(5, c - 10):
            for p in range(5, (c - s - 1) // 2 + 1):
                q = c - s - p
                v = np_du(c, s, p, q)
                tot += int(mp.floor(v))
    return tot


print("G(16) via closed form =", G_closed(16), "(oracle 9)")
print("G(20) via closed form =", G_closed(20), "(oracle 205)")

# Try a rational closed form for n_p(DU-): does it equal
#   (c-p)*(s+p)/(2*(c-p)+(s+p))  or similar?  Search first over simple
# rational functions.
def form1(c, s, p, q):
    # candidate: g ~ floor( (c-s-2)*something )
    return (c - p) / (c - p + (s + p)) * (s + c) * 0.5

# Evaluate a few to try to recognize the exact angle values.
print("\nhigh-precision n_p(DU-) and angle ratios:")
for (c, s, p, q) in [(16, 5, 5, 6), (20, 7, 6, 7), (18, 5, 6, 7), (24, 5, 9, 10)]:
    R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi)
    rho = mpf(p) / (2 * pi)
    a, b = R - rho, r + rho
    DU = R - r - 1
    rho_q = mpf(q) / (2 * pi)
    a_q, b_q = R - rho_q, r + rho_q
    DL = abs(a_q - b_q)
    d = DU - (DU - DL) / mpf(10 ** 9)
    x = (a * a - b * b + d * d) / (2 * d)
    y = sqrt(a * a - x * x)
    beta = atan2(y, x)
    gamma = atan2(y, x - d)
    npv = ((c - p) * beta + (s + p) * gamma) / pi
    print(" c=%d s=%d p=%d q=%d  n_p(DU-)=%s" % (c, s, p, q, mp.nstr(npv, 40)))
    print("    beta/pi=%s  gamma/pi=%s  (c-p)/(s+p)=%s"
          % (mp.nstr(beta / pi, 30), mp.nstr(gamma / pi, 30),
             mpf(c - p) / (s + p)))
    # candidate: n_p = (c-p)*beta/pi + (s+p)*gamma/pi; try ( beta = gamma? )
    print("    beta-gamma/pi =", mp.nstr((beta - gamma) / pi, 30))