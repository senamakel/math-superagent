"""Clean re-derivation of the tooth-mesh phase and a fine-grid count of valid d.

Meshing phase for one planet of type m (radius rho = m/2pi), sun radius r,
ring radius R, S at (d,0):
    E_m = R*beta - r*gamma - rho*psi   (cm, mod 1)
where beta = angle of planet centre about O, gamma = angle about S,
psi = planet-pitch arc (radians) from its S-contact to its C-contact.

For the two mirror positions of a type (upper/lower) both planets must mesh,
and the two types must mesh with the same global references, so valid d needs:
    E_pU - E_pL in Z   (mod 1)
    E_qU - E_qL in Z
    E_pU - E_qU in Z
We scan d finely and count isolated near-integer d; report which ones, and
compare the count with g(16,5,5,6)=9.
"""
from mpmath import mp, mpf, pi, atan2, sqrt, sin, cos, fabs
mp.dps = 80


def E_exact(c, s, m, d, mirror=1):
    """Phase value for one planet, mirror=+1 upper, mirror=-1 lower."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(m) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y = sqrt(a * a - x * x)
    # beta about O, gamma about S.  Use signed (mirror flips sign of y).
    yb = mirror * y
    beta = atan2(yb, x)
    gamma = atan2(yb, x - d)
    # psi: planet arc from S-contact to C-contact.
    # S-contact direction from P is toward S: angle = atan2(-yb, -(x-d)) + pi...
    # C-contact direction from P is outward (toward +u_r from O through P).
    # Use: lamC (as seen from P) points from P away-> ring = direction (P-O) = atan2(yb,x)
    # lamS points from P toward S = direction (S-P) = atan2(-yb, d - x)
    lamC = atan2(yb, x)                 # outward radial (toward ring)
    lamS = atan2(-yb, d - x)            # toward S
    psi = (lamS - lamC) % (2 * pi)
    T = rho * psi
    return R * beta - r * gamma - T, beta, gamma, psi


def main():
    c, s, p, q = 16, 5, 5, 6
    R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi)
    rp, rq = mpf(p) / (2 * pi), mpf(q) / (2 * pi)
    DL = max(abs((R - rp) - (r + rp)), abs((R - rq) - (r + rq)))
    DU = min((R - rp) + (r + rp), (R - rq) + (r + rq), R - r - 1)
    print("d-range:", mp.nstr(DL, 8), "..", mp.nstr(DU, 8))

    N = 400000
    step = (DU - DL) / N
    def nearint(x): 
        x = x % 1
        return min(x, 1 - x)

    sols = []
    prev = None
    for i in range(N + 1):
        d = DL + step * i
        EpU, *_ = E_exact(c, s, p, d, +1)
        EpL, *_ = E_exact(c, s, p, d, -1)
        EqU, *_ = E_exact(c, s, q, d, +1)
        EqL, *_ = E_exact(c, s, q, d, -1)
        cond = max(nearint(EpU - EpL), nearint(EqU - EqL), nearint(EpU - EqU))
        if cond < mpf('1e-9'):
            sols.append((d, cond, EpU % 1, EpL % 1, EqU % 1, EqL % 1))
    # cluster
    clust = []
    for s0 in sorted(sols, key=lambda t: float(t[0])):
        if clust and s0[0] - clust[-1][0] < step * 5:
            # keep the more central one
            if s0[1] < clust[-1][1]:
                clust[-1] = s0
        else:
            clust.append(s0)
    # refine using mpmath findroot? Just report raw and densify around each
    print("raw candidate points:", len(sols), " clusters:", len(clust))
    for d, cond, a, b, cc, dd in clust[:40]:
        print(f"  d={mp.nstr(d,20)} cond={mp.nstr(cond,6)}"
              f" EpU={mp.nstr(a,10)} EpL={mp.nstr(b,10)}"
              f" EqU={mp.nstr(cc,10)} EqL={mp.nstr(dd,10)}")


if __name__ == '__main__':
    main()