"""Exact-status probe for the three analytic facts of the winning n_t model.

Facts under test:
  F1: n_p(d) + n_q(d) = c + s for all interior d (two-focus ellipse geometry).
  F2: n_p strictly increasing on (d_min, d_max).
  F3: (n_p in Z and n_q in Z, parity n_p-n_q == p-q mod 2)
      reduces to  n_p in Z  (mirror + parity automatic).

Geometry (radii from tooth counts):
  R=c/2pi, r=s/2pi, rho_t=t/2pi, a_t=R-rho_t, b_t=r+rho_t.
  O=(0,0), S=(d,0), upper tangency P_t=(x,y), x=(a_t^2-b_t^2+d^2)/(2d),
  y=sqrt(a_t^2-x^2), beta_t=atan2(y,x), mu_t=atan2(y,x-d).
  n_t = [(c-t)*beta_t + (s+t)*mu_t]/pi = 2*(a_t*beta_t + b_t*mu_t).

Key structural facts (c = s+p+q makes the (a,b) pairs swap):
  a_p=(c-p)/2pi, b_p=(s+p)/2pi ; a_q=(c-q)/2pi=b_p, b_q=(s+q)/2pi=(c-p)/2pi=a_p.
  So (a_q,b_q)=(b_p,a_p): the q-triangle is the mirror of the p-triangle.
"""
import mpmath as mp

mp.mp.dps = 60


def radii(c, s, t):
    pi = mp.pi
    a = (c - t) / (2 * pi)
    b = (s + t) / (2 * pi)
    return a, b


def point_angles(c, s, t, d):
    a, b = radii(c, s, t)
    x = (a * a - b * b + d * d) / (2 * d)
    y = mp.sqrt(mp.fabs(a * a - x * x)) if (a * a - x * x) >= 0 else mp.mpf('0')
    beta = mp.atan2(y, x)
    mu = mp.atan2(y, x - d)
    return beta, mu, x, y


def n_t(c, s, t, d):
    beta, mu, _, _ = point_angles(c, s, t, d)
    return ((c - t) * beta + (s + t) * mu) / mp.pi


def test_identity():
    """F1: n_p + n_q == c+s across many (c,s,p,q,d)."""
    worst = 0
    n1 = n2 = 0
    for c in range(16, 61):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                for q in range(p + 1, c - s - p + 1):
                    a_p, b_p = radii(c, s, p)
                    a_q, b_q = radii(c, s, q)
                    lo = max(abs(a_p - b_p), abs(a_q - b_q)) * 1.0000001
                    hi = min(a_p + b_p, a_q + b_q) * 0.9999999
                    if lo >= hi:
                        continue
                    d = (lo + hi) / 2
                    val = n_t(c, s, p, d) + n_t(c, s, q, d) - (c + s)
                    worst = max(worst, abs(val))
                    n1 += 1
                    if abs(val) > mp.mpf('1e-50'):
                        n2 += 1
    return n1, n2, worst


def test_mirror_angle_identities():
    """beta_q == pi - mu_p and mu_q == pi - beta_p (the mirror swap)."""
    worst1 = worst2 = 0
    for c in range(16, 41):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                for q in range(p + 1, c - s - p + 1):
                    a_p, b_p = radii(c, s, p)
                    lo = abs(a_p - b_p) * 1.00001
                    hi = (a_p + b_p) * 0.99999
                    if lo >= hi:
                        continue
                    d = (lo + hi) / 2
                    bp, mp_, _, _ = point_angles(c, s, p, d)
                    bq, mq, _, _ = point_angles(c, s, q, d)
                    worst1 = max(worst1, abs(bq - (mp.pi - mp_)))
                    worst2 = max(worst2, abs(mq - (mp.pi - bp)))
    return worst1, worst2


def test_monotonicity():
    """F2: n_p strictly increasing on (d_min, d_max): n_p'(d) > 0."""
    pos = neg = zero = 0
    worst_neg = mp.inf
    for c in range(16, 41):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                for q in range(p + 1, c - s - p + 1):
                    pi = mp.pi
                    a_p, b_p = radii(c, s, p)
                    a_q, b_q = radii(c, s, q)
                    R = c / (2 * pi)
                    r = s / (2 * pi)
                    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
                    d_max = min(a_p + b_p, a_q + b_q, R - r - 1)
                    if d_min >= d_max:
                        continue
                    for frac in (0.15, 0.35, 0.55, 0.75, 0.9):
                        d = d_min * (1 - frac) + d_max * frac
                        h = mp.mpf('1e-13') * max(1, abs(d))
                        fp = (n_t(c, s, p, d + h) - n_t(c, s, p, d - h)) / (2 * h)
                        if fp > 0:
                            pos += 1
                        elif fp < 0:
                            neg += 1
                            worst_neg = min(worst_neg, fp)
                        else:
                            zero += 1
    return pos, neg, zero, worst_neg


if __name__ == "__main__":
    print("=== F1: n_p(d)+n_q(d) == c+s (identity) ===")
    n1, n2, worst = test_identity()
    print("  points checked: %d, failures: %d, worst |residual| = %s"
          % (n1, n2, mp.nstr(worst, 5)))

    print("\n=== mirror-angle identities beta_q==pi-mu_p, mu_q==pi-beta_p ===")
    w1, w2 = test_mirror_angle_identities()
    print("  worst |beta_q-(pi-mu_p)| = %s" % mp.nstr(w1, 5))
    print("  worst |mu_q-(pi-beta_p)| = %s" % mp.nstr(w2, 5))

    print("\n=== F2: n_p strictly increasing (n_p' > 0) ===")
    pos, neg, zero, wn = test_monotonicity()
    print("  derivatives: positive=%d negative=%d zero=%d, worst negative=%s"
          % (pos, neg, zero, mp.nstr(wn, 5)))
