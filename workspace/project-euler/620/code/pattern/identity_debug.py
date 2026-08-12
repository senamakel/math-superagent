"""Settle: is n_p(d)+n_q(d) == s+c exactly at interior d? (mpmath)
And debug C2 by inspecting integer levels for one tuple.
"""
from mpmath import mp, mpf, pi, atan2, sqrt, fabs
import numpy as np

mp.dps = 60


def n_t_mp(c, s, t, d):
    R = mpf(c) / (2 * pi); r = mpf(s) / (2 * pi); rho = mpf(t) / (2 * pi)
    a = R - rho; b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y = sqrt(max(a * a - x * x, mpf(0)))
    beta = atan2(y, x); mu = atan2(y, x - d)
    return ((c - t) * beta + (s + t) * mu) / pi


def d_interval(c, s, p, q):
    pi = math.pi if hasattr(math := __import__('math'), 'pi') else None
    import math
    R = c / (2 * math.pi); r = s / (2 * math.pi)
    rp, rq = p / (2 * math.pi), q / (2 * math.pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)
    return d_min, d_max


def check_identity(c, s, p, q):
    d_min, d_max = d_interval(c, s, p, q)
    worst = mpf(0)
    for k in range(31):
        d = mpf(d_min) + (mpf(d_max) - mpf(d_min)) * mpf(k) / mpf(30)
        if k == 0:
            d = (mpf(d_min) + mpf(d_max)) / 2
        if k == 30:
            d = (mpf(d_min) + mpf(d_max)) / 2
        np_ = n_t_mp(c, s, p, d)
        nq = n_t_mp(c, s, q, d)
        worst = max(worst, fabs(np_ + nq - mpf(s + c)))
    return worst


tes = [(16,5,5,6), (17,5,5,7), (18,5,6,7), (20,6,6,8), (17,6,5,6), (19,6,6,7)]
print("case          worst|np+nq-(s+c)| @31 interior d (mpmath-60)")
for (c, s, p, q) in tes:
    w = check_identity(c, s, p, q)
    print("(%2d,%d,%d,%d)   %.3e" % (c, s, p, q, float(w)))

# Debug tuple (17,5,5,7): list integer levels of n_p and n_q
print()
print("Debug (17,5,5,7) — integer levels of n_p over the interior")
c, s, p, q = 17, 5, 5, 7
d_min, d_max = d_interval(c, s, p, q)
import math
N = (1 << 18) + 1
dv = np.linspace(d_min, d_max, N)
def n_arr(c, s, t, d):
    R = c/(2*math.pi); r = s/(2*math.pi); rho = t/(2*math.pi)
    a = R-rho; b = r+rho
    x = (a*a - b*b + d*d)/(2.0*d)
    y = np.sqrt(np.maximum(a*a - x*x, 0.0))
    beta = np.arctan2(y, x); mu = np.arctan2(y, x-d)
    return ((c-t)*beta + (s+t)*mu)/math.pi
np_ = n_arr(c, s, p, dv)
nq = n_arr(c, s, q, dv)
lo, hi = np_[0], np_[-1]
print("d_min=%.6f d_max=%.6f  n_p range %.4f..%.4f  n_q range %.4f..%.4f"
      % (d_min, d_max, lo, hi, nq[0], nq[-1]))
tol = 1e-3
for k in range(int(math.floor(lo)), int(math.ceil(hi)) + 1):
    both_p = np.any(np.abs(np_ - k) < tol)
    # n_q integer at same d?
    ok = False
    if both_p:
        sel = np.abs(np_ - k) < tol
        nq_s = nq[sel]
        nq_ok = np.max(np.abs(nq_s - np.rint(nq_s)))
        # parity
        par = (k - np.rint(nq_s[0]).astype(int)) % 2
        print("  k=%d: n_p reaches k=%s; n_q closeness=%.2e parity(p->q)=%d (want %d)"
              % (k, both_p, float(nq_ok), int(par[0]), (p-q) % 2))
