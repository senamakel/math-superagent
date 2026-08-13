"""Test the two-evaluation closed form for g:
   g(c,s,p,q) = floor(n_p(DU-)) - ceil(n_p(DL+)) + 1
where n_p(d)=[(c-p)*beta + (s+p)*gamma]/pi is strictly monotone increasing
on (DL,DU), DL=max(|a_t-b_t|) (=|a_q-b_q| since q>p), DU=min(a_t+b_t,
R-r-1) (=R-r-1 gap here).  Endpoints evaluated at DL+eps, DU-eps.
Check against the mpmath-verified table for all tuples.
Also print, for a sample, n_p(DL), n_p(DU), kmin, kmax, g to show the
simplicity of the form.
"""
from mpmath import mp, mpf, pi, atan2, sqrt
import os

mp.dps = 40
DIRT = "/workspace/code/out/mpmath_table.txt"


def n_endpoints(c, s, p, q):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)

    def geom(t, d):
        rho = mpf(t) / (2 * pi)
        a = R - rho
        b = r + rho
        x = (a * a - b * b + d * d) / (2 * d)
        y2 = a * a - x * x
        if y2 <= 0:
            return None
        return sqrt(max(y2, mpf(0)))

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

    lowers = [abs((R - rho) - (r + rho)) for rho in (mpf(p) / (2 * pi), mpf(q) / (2 * pi))]
    uppers = [(R - rho) + (r + rho) for rho in (mpf(p) / (2 * pi), mpf(q) / (2 * pi))]
    DL = max(lowers)
    DU = min(uppers + [R - r - 1])
    return DL, DU


def g_closed(c, s, p, q):
    DL, DU = n_endpoints(c, s, p, q)
    if DL >= DU:
        return 0, (DL, DU, None, None)
    eps = (DU - DL) / mpf(10 ** 6)
    vlo = n_p_val(c, s, p, DL + eps)
    vhi = n_p_val(c, s, p, DU - eps)
    kmin = int(mp.ceil(vlo))
    kmax = int(mp.floor(vhi))
    return max(0, kmax - kmin + 1), (DL, DU, vlo, vhi)


def n_p_val(c, s, p, d):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(p) / (2 * pi)
    a, b = R - rho, r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None
    y = sqrt(y2)
    beta = atan2(y, x)
    gamma = atan2(y, x - d)
    return ((c - p) * beta + (s + p) * gamma) / pi


def main():
    bad = 0
    n = 0
    examples = 0
    print("comparing closed form floor(n_p(DU))-ceil(n_p(DL))+1 vs mpmath g")
    for line in open(DIRT):
        c, s, p, q, g = map(int, line.split())
        gc, (DL, DU, vlo, vhi) = g_closed(c, s, p, q)
        n += 1
        if gc != g:
            bad += 1
            print("MISMATCH c,s,p,q=%d,%d,%d,%d closed=%d mpmath=%d DL=%.6f DU=%.6f vlo=%.5f vhi=%.5f"
                  % (c, s, p, q, gc, g, float(DL), float(DU),
                     float(vlo) if vlo else -1, float(vhi) if vhi else -1))
        if examples < 6:
            print("c=%d s=%d p=%d q=%d: g=%d  n_p(DL)=%.5f n_p(DU)=%.5f  kmin=%d kmax=%d"
                  % (c, s, p, q, g, float(vlo) if vlo else -1,
                     float(vhi) if vhi else -1,
                     int(mp.ceil(vlo)) if vlo else -1,
                     int(mp.floor(vhi)) if vhi else -1))
            examples += 1
    print("checked %d tuples; disagreements: %d" % (n, bad))


if __name__ == "__main__":
    main()