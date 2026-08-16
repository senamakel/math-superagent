"""
High-precision check whether collapse Gamma at t=1/2 equals phi/2 exactly,
or only agrees to ~8 dp by coincidence. entropy involves log, so an exact
algebraic value would be a miracle; measure the agreement at 50 digits.
"""
import mpmath as mp
mp.mp.dps = 60

LN2 = mp.log(2)


def h(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1:
        return mp.mpf(0)
    return -x*mp.log(x)/LN2 - (1-x)*mp.log(1-x)/LN2


def gamma_alpha0_collapse(t, a):
    b = (a + 1) / 2
    beta = (t - a) / (b - a)
    w1 = (1 - beta) + beta / 2
    w2 = beta / 2
    eh = w1 * h(a) + w2 * h(1)
    e_indep = 0.0
    vals = [a, mp.mpf(1)]
    wts = [w1, w2]
    for pi, p in enumerate(vals):
        for qi, q in enumerate(vals):
            e_indep += wts[pi]*wts[qi]*h(p + q - p*q)
    return e_indep / eh


a = (3 - mp.sqrt(5)) / 2
phi = (1 + mp.sqrt(5)) / 2
v = gamma_alpha0_collapse(mp.mpf(1)/2, a)
target = phi/2
print("collapse Gamma at t=0.5 (60 digits):")
print("  v      =", mp.nstr(v, 50))
print("  phi/2  =", mp.nstr(target, 50))
print("  diff   =", mp.nstr(abs(v - target), 50))
print("  relative =", mp.nstr(abs(v-target)/target, 30))
