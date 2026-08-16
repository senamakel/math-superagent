"""Quick benchmark: float reproduction of the paper point, and cost of
mpmath.iv interval evaluations for the 22 h-calls in one Gamma_hat scan step.
Not a deliverable; scratch for sizing the scorer."""
import math
import time

from mpmath import iv, mp

# ---- float reference (from yu_optimization.py) ----
log2 = math.log2


def h(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def phi1(p, q):
    return sorted([max(p, q), 0.5, p + q])[1]


def g_at(alpha, a1, a2, b1, b2, t):
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0
    if not (0.0 <= a <= t < b <= 1.0):
        return math.inf
    beta = (t - a) / (b - a)
    if not (0.0 < beta <= 1.0):
        return math.inf
    wa = (1.0 - beta) / 2.0
    wb = beta / 2.0
    eh = wa * (h(a1) + h(a2)) + wb * (h(b1) + h(b2))
    if eh <= 0.0:
        return math.inf
    vals = [a1, a2, b1, b2]
    wts = [wa, wa, wb, wb]
    e_indep = 0.0
    for i in range(4):
        for j in range(4):
            e_indep += wts[i] * wts[j] * h(vals[i] + vals[j] - vals[i] * vals[j])
    e_coupled = wa * (h(phi1(a1, a2)) + h(phi1(a2, a1))) + wb * (h(phi1(b1, b2)) + h(phi1(b2, b1)))
    g = (1.0 - alpha) * e_indep + alpha * e_coupled
    return g / eh


alpha = 0.035
a = 0.3300622
t = 0.38234
v = g_at(alpha, a, a, a, 1.0, t)
print(f"float paper point Gamma_hat >= {v:.12f}")


# ---- interval version, timed ----
def h_iv(x):
    lo, hi = x
    lo = max(lo, mp.mpf(0)); hi = min(hi, mp.mpf(1))
    if lo >= 1 or hi <= 0:
        return (mp.mpf(0), mp.mpf(0))
    ln2 = mp.log(mp.mpf(2))
    # x log2 x on interval [lo,hi]; x log2 x is not monotone near 0, but we clamp lo>0
    # For tightness evaluate at endpoints; interval of x*log2(x) on [lo,hi] with lo>0.
    lxz = mp.mpf(0)  # placeholder
    return (mp.mpf(0), mp.mpf(0))


# Instead measure the real mpmath.iv cost
def bench_iv(n_iters, prec):
    mp.prec = prec
    iv.pretty = False
    t0 = time.time()
    s = 0
    for _ in range(n_iters):
        x = iv.mpf('0.3300622')
        y = iv.mpf('0.38234')
        z = -x * (iv.log(x) / iv.log(iv.mpf(2))) - (iv.mpf(1) - x) * (iv.log(iv.mpf(1) - x) / iv.log(iv.mpf(2)))
        s += float(z.a)
    dt = time.time() - t0
    return dt


if __name__ == "__main__":
    for prec in (53, 72, 96, 120):
        dt = bench_iv(20000, prec)
        print(f"prec={prec}: 20000 single h-evals (2 log2 each) in {dt:.3f}s")
