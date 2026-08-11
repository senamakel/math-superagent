"""Check what the record b's actually are: convergent denominators of pi/sqrt(d)
and pi*sqrt(d), vs semiconvergents of sqrt(d). Uses exact-ish high precision."""
import sympy as sp

PI = sp.N(sp.pi, 80)

def cf_convergent_denoms(x, N):
    """Return set of convergent denominators q of CF of x with q<=N."""
    xv = x
    # compute CF terms
    a = []
    t = xv
    for _ in range(200):
        ai = sp.floor(t)
        a.append(int(ai))
        if t - ai < sp.Float('1e-60'):
            break
        t = 1 / (t - ai)
        if t > N * 10:
            pass
    # convergents denominators
    q_2, q_1 = 0, 1
    denoms = set()
    for ai in a:
        q = ai * q_1 + q_2
        if q > N:
            break
        denoms.add(q)
        q_2, q_1 = q_1, q
    return denoms

def semiconv_sqrt_d(d, N):
    res = sp.continued_fraction_periodic(0, 1, d)
    a0 = res[0]; period = list(res[1])
    a = [a0] + period * 500
    q_2, q_1 = 0, 1
    denoms = set()
    for k in range(len(a) - 1):
        ak = a[k]
        qk = ak * q_1 + q_2
        qkm1 = q_1
        m = 0
        while True:
            s = m * qk + qkm1
            if s > N:
                break
            denoms.add(s)
            m += 1
            if s >= a[k+1] * qk + qkm1:
                break
        q_2, q_1 = q_1, qk
    return denoms

def records(d, N):
    sd = sp.sqrt(d)
    best = sp.oo
    recs = []
    for b in range(0, N + 1):
        v = b * sd - PI
        r = sp.floor(v + sp.Rational(1, 2))
        err = abs(v - r)
        if err < best:
            best = err
            recs.append(b)
    return recs

for d in [2, 3, 5, 6, 7, 8, 10]:
    N = 2_000_000
    recs = records(d, N)
    pids = cf_convergent_denoms(PI / sp.sqrt(d), N)
    pidx = cf_convergent_denoms(PI * sp.sqrt(d), N)
    ss = semiconv_sqrt_d(d, N)
    m_pids = sum(1 for b in recs if b in pids)
    m_pidx = sum(1 for b in recs if b in pidx)
    m_ss = sum(1 for b in recs if b in ss)
    print(f"d={d}: {len(recs)} records. in pi/sqrt(d) conv: {m_pids}, in pi*sqrt(d) conv: {m_pidx}, in sqrt(d) semiconv: {m_ss}")
    non = [b for b in recs if b not in pids and b not in pidx]
    print("   records not in either pi-CF: ", non)
