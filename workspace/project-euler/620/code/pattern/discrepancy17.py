"""Resolve the g(17,6,5,6) discrepancy: seqgen said 9, levels.py said 10.

Directly count roots of n_p(d) - k = 0 for each integer k with mpmath
bisection to 40 digits, on the full open interval (DL, DU), reporting each
root's d and whether it is strictly interior.  Also list all levels k with
kmin<=k<=kmax and the sign of n_p - k at the two interior probe points.
"""
from mpmath import mp, mpf, pi, atan2, sqrt
mp.dps = 40

c, s, p, q = 17, 6, 5, 6
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
    return a, b, x, sqrt(y2)


def n_t(t, d):
    g = geom(t, d)
    if g is None:
        return None
    a, b, x, y = g
    beta = atan2(y, x)        # angle at ring centre O
    gamma = atan2(y, x - d)   # angle at sun centre S
    return ((c - t) * beta + (s + t) * gamma) / pi


DL, DU = mpf('0.1591549430918953357688837633725143620345'), \
         mpf('0.7507043740108302454196840471820387494734')
# exact: DL=(q-p)/(2pi), DU=(c-s)/(2pi)-1
eps = (DU - DL) / mpf(10**6)
lo0, hi0 = DL + eps, DU - eps
print("DL=%.17f DU=%.17f lo0=%.17f hi0=%.17f" % (DL, DU, lo0, hi0))
nlo = n_t(p, lo0)
nhi = n_t(p, hi0)
print("n_p(lo0)=%.12f  n_p(hi0)=%.12f" % (nlo, nhi))

kmin = int(mp.ceil(nlo))
kmax = int(mp.floor(nhi))
print("k range %d..%d" % (kmin, kmax))

for k in range(kmin, kmax + 1):
    flo = n_t(p, lo0) - k
    fhi = n_t(p, hi0) - k
    if flo * fhi > 0:
        print("k=%d: no sign change on (lo0,hi0): flo=%.4e fhi=%.4e"
              % (k, flo, fhi))
        continue
    a, b = lo0, hi0
    fa, fb = flo, fhi
    for _ in range(250):
        m = (a + b) / 2
        fm = n_t(p, m) - k
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    d = (a + b) / 2
    yp = geom(p, d)[3]
    yq = geom(q, d)[3]
    ok = mp.fabs(n_t(p, d) - k) < mpf('1e-30') and d > DL and d < DU
    nq = n_t(q, d)
    print("k=%2d root d=%.17f yp=%.4f yq=%.4f interior=%s  n_p(d)-k=%.2e  n_q=%s"
          % (k, d, yp, yq, ok, n_t(p, d) - k, mp.nstr(nq, 20)))

# also check: is n_p monotone on random dense probes?
import random
random.seed(2)
ds = sorted(random.uniform(float(DL), float(DU)) for _ in range(2000))
prev = None
bad = 0
for dv in ds:
    v = n_t(p, mpf(dv))
    if prev is not None and v < prev - mpf('1e-12'):
        bad += 1
    prev = v
print("monotonicity violations in 2000 random samples:", bad)