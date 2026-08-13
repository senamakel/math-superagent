"""Print g and n_p(DU-eps) for many tuples to find a closed form.

Since g = floor(n_p(DU-)) (n_p(DL+) in (0,1) always), print exact n_p(DU-)
for c<=40 and look for structure: dependence on c-p, s+p, products, ratios.
"""
from mpmath import mp, mpf, pi, atan2, sqrt

mp.dps = 50


def vals(c, s, p, q):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)

    def n_t(t, d):
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

    lowers = [abs((R - mpf(t) / (2 * pi)) - (r + mpf(t) / (2 * pi))) for t in (p, q)]
    uppers = [(R - mpf(t) / (2 * pi)) + (r + mpf(t) / (2 * pi)) for t in (p, q)]
    DL = max(lowers)
    DU = min(uppers + [R - r - 1])
    eps = (DU - DL) / mpf(10 ** 7)
    vlo = n_t(p, DL + eps)
    vhi = n_t(p, DU - eps)
    npdu = n_t(p, DU - eps)
    nqdu = n_t(q, DU - eps)
    return vlo, npdu, nqdu, DL, DU


print("c  s  p  q   g   n_p(DU-)    n_q(DU-)   (s+c)   n_p+n_q")
for c in range(16, 30):
    for s in range(5, c - 10):
        for p in range(5, (c - s - 1) // 2 + 1):
            q = c - s - p
            vlo, npdu, nqdu, DL, DU = vals(c, s, p, q)
            g = int(mp.floor(npdu))
            print("%2d %2d %2d %2d  %2d   %9.6f  %9.6f   %3d   %9.6f"
                  % (c, s, p, q, g, npdu, nqdu, s + c, npdu + nqdu))