"""Check record b's against semiconvergents of candidate irrationals."""
import math
import mpmath

def cf_terms(x, nterms=500, dps=60):
    mpmath.mp.dps = dps
    t = x
    a = []
    for _ in range(nterms):
        ai = int(mpmath.floor(t))
        a.append(ai)
        rem = t - ai
        if mpmath.almosteq(rem, 0, abs_eps=mpmath.mpf('1e-50')):
            break
        t = 1 / rem
    return a

def semiconvergent_denoms(x, N):
    a = cf_terms(x * 1.0)
    q_2, q_1 = 0, 1
    denoms = set()
    for k in range(len(a) - 1):
        ak = a[k]
        qk = ak * q_1 + q_2
        qkm1 = q_1
        a_next = a[k + 1]
        m = 1
        while True:
            s = m * qk + qkm1
            if s > N:
                break
            denoms.add(s)
            m += 1
            if s >= a_next * qk + qkm1:
                break
        q_2, q_1 = q_1, qk
    return denoms

def conv_denoms(x, N):
    a = cf_terms(x * 1.0)
    q_2, q_1 = 0, 1
    denoms = set()
    for ak in a:
        q = ak * q_1 + q_2
        if q > N:
            break
        denoms.add(q)
        q_2, q_1 = q_1, q
    return denoms

N = 2_000_000
recs_d2 = [0, 3, 5, 10, 418, 1403, 15263, 62584, 176827, 647659]
recs = recs_d2

for name, x in [("pi/sqrt2", mpmath.pi / mpmath.sqrt(2)),
                ("pi*sqrt2", mpmath.pi * mpmath.sqrt(2)),
                ("2pi*sqrt2", 2 * mpmath.pi * mpmath.sqrt(2)),
                ("pi", mpmath.pi),
                ("pi*2", 2 * mpmath.pi)]:
    ss = semiconvergent_denoms(x, N)
    cs = conv_denoms(x, N)
    hit_s = [b for b in recs if b in ss]
    hit_c = [b for b in recs if b in cs]
    print(f"{name}: conv hit={hit_c}  semiconv hit={hit_s}")
