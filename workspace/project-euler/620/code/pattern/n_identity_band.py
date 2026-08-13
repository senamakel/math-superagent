"""Debug: where does the mirror-angle identity n_p+n_q=c+s hold?

The mirror relation beta_q=pi-mu_p and mu_q=pi-beta_p requires 0<x_p<d
(the upper p tangency point between the two foci horizontally).  The identity
n_p+n_q=c+s follows from it.  Locate the d-range where 0<x_p<d and check
whether the identity is exactly valid there and fails outside.
"""
import mpmath as mp
mp.mp.dps = 60


def radii(c, s, t):
    pi = mp.pi
    return (c - t) / (2 * pi), (s + t) / (2 * pi)


def angles(c, s, t, d):
    a, b = radii(c, s, t)
    x = (a * a - b * b + d * d) / (2 * d)
    y = mp.sqrt(mp.fabs(a * a - x * x))
    beta = mp.atan2(y, x)
    mu = mp.atan2(y, x - d)
    return beta, mu, x, y


def n_t(c, s, t, d):
    beta, mu, _, _ = angles(c, s, t, d)
    return ((c - t) * beta + (s + t) * mu) / mp.pi


def scan(c, s, p, q, n=2000):
    pi = mp.pi
    a_p, b_p = radii(c, s, p)
    a_q, b_q = radii(c, s, q)
    R = c / (2 * pi); r = s / (2 * pi)
    lo = max(abs(a_p - b_p), abs(a_q - b_q))
    hi = min(a_p + b_p, a_q + b_q, R - r - 1)
    if lo >= hi:
        return
    nbad = 0
    for k in range(n):
        d = lo + (hi - lo) * mp.mpf(k) / (n - 1)
        bp, mp_, xp, yp = angles(c, s, p, d)
        bq, mq, xq, yq = angles(c, s, q, d)
        iden = n_t(c, s, p, d) + n_t(c, s, q, d) - (c + s)
        m1 = abs(bq - (pi - mp_))
        m2 = abs(mq - (pi - bp))
        inband = (xp > 0) and (xp < d)
        tol = mp.mpf('1e-30')
        ok = abs(iden) < tol
        if not ok:
            nbad += 1
        if nbad == 1 and k % 7 == 0:
            pass
        # print the first bad point with context
        if abs(iden) > 1e-9 and not inband:
            print("  d=%.5f xp=%.5f (xp<d=%s, xp>0=%s) iden=%.6f m1=%.3f m2=%.3f"
                  % (d, xp, xp < d, xp > 0, iden, m1, m2))
    print("  scanned %d points on [%.5f,%.5f]: identity-bad count = %d"
          % (n, lo, hi, nbad))


if __name__ == "__main__":
    for tup in [(16, 5, 5, 6), (20, 5, 5, 10), (30, 8, 6, 16)]:
        print("=" * 30)
        print("c,s,p,q =", tup)
        scan(*tup)
