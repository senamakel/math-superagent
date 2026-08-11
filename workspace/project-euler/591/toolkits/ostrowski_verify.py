"""Verify Cabanillas (arXiv:1904.01874) Prop 9/10 candidate structure for the
record-holders of ||n*alpha - beta||_Z against brute force on small instances.

Candidates (best right): n=0, terminal prefix, and
    n = sum_{i=1}^{2k-1} b_i q_{i-1} + j*q_{2k-1}, j in 0..b_{2k}-1, k>=1
Candidates (best left):
    n = sum_{i=1}^{2k}   b_i q_{i-1} + j*q_{2k},   j in 0..b_{2k+1}-1, k>=0
where (b_i) is the alpha-numeration of beta and (q_i) are convergent denominators.
"""
from math import ceil

def cf(alpha, nterms):
    """continued fraction partial quotients of irrational alpha in (0,1)."""
    a = []
    x = alpha
    for _ in range(nterms):
        ai = int(x // 1)
        a.append(ai)
        x = x - ai
        if x == 0:
            break
        x = 1.0 / x
    return a

def alpha_numeration(alpha, beta, nterms):
    """(b_i) digits of beta's alpha-numeration, delta sequence."""
    a = cf(alpha, nterms)
    # delta_{-1}=1, delta_0=alpha, delta_k = -a_k delta_{k-1} + delta_{k-2}
    delta = { -1: 1.0, 0: alpha }
    for k in range(1, nterms + 1):
        delta[k] = -a[k - 1] * delta[k - 1] + delta[k - 2]
    b = {}
    cur = beta
    for k in range(1, nterms + 1):
        ak = a[k - 1]
        bk = min(ak, ceil(cur / delta[k - 1]))
        b[k] = bk
        cur = bk * delta[k - 1] - cur
    return b, delta, a

def conv_q(a, nterms):
    """convergent denominators q_{-1}=0,q_0=1,... with the a0=0 offset."""
    q = { -1: 0, 0: 1 }
    # a list is the partial quotients a_1, a_2, ... (a0 = floor(alpha) = 0 here)
    for k in range(1, nterms + 1):
        q[k] = a[k - 1] * q[k - 1] + q[k - 2]
    return q

def candidates(alpha, beta, nterms=40):
    a = cf(alpha, nterms)
    b, delta, a = alpha_numeration(alpha, beta, nterms)
    q = conv_q(a, nterms)
    out = {0}
    # terminal prefix n = sum b_i q_{i-1}  (if expansion terminates) - skip for infinite
    # best RIGHT
    for k in range(1, nterms // 2):
        prefix = sum(b[i] * q[i - 1] for i in range(1, 2 * k))  # i in 1..2k-1
        jmax = b[2 * k] - 1
        for j in range(0, jmax + 1):
            out.add(prefix + j * q[2 * k - 1])
    # best LEFT
    for k in range(0, nterms // 2):
        prefix = sum(b[i] * q[i - 1] for i in range(1, 2 * k + 1))  # i in 1..2k
        jmax = b[2 * k + 1] - 1
        for j in range(0, jmax + 1):
            out.add(prefix + j * q[2 * k])
    return sorted(x for x in out if x >= 0)

def dist(n, alpha, beta):
    v = n * alpha - beta
    f = v - int(v)
    return min(f, 1.0 - f)

def brute_min(L, alpha, beta):
    best = None; bestn = None
    for n in range(0, L + 1):
        d = dist(n, alpha, beta)
        if best is None or d < best:
            best = d; bestn = n
    return bestn, best

def cand_min(L, alpha, beta, nterms=40):
    cands = [n for n in candidates(alpha, beta, nterms) if n <= L]
    best = None; bestn = None
    for n in cands:
        d = dist(n, alpha, beta)
        if best is None or d < best:
            best = d; bestn = n
    return bestn, best

if __name__ == "__main__":
    import itertools
    ok = True
    # test several alpha, beta pairs and several L
    for (alpha, beta) in [
            (2**0.5 - 1, 3.141592653589793 - 3),
            (3**0.5 - 1, 3.141592653589793 - 3),
            (5**0.5 - 2, 0.721349),            # beta ~ 1/sqrt(5)
            (2**0.5 - 1, 0.6180339887 - 0),    # beta irrational ~ golden frac
            (7**0.5 - 2, 0.27789),
    ]:
        for L in [50, 200, 1000]:
            bn, bd = brute_min(L, alpha, beta)
            cn, cd = cand_min(L, alpha, beta, nterms=40)
            match = (abs(bn - cn) < 1e-9 and abs(bd - cd) < 1e-12) or abs(bd - cd) < 1e-12
            # global min value should match (record holder might tie at same distance)
            valmatch = abs(bd - cd) < 1e-12
            status = "OK" if valmatch else "FAIL"
            if not valmatch:
                ok = False
            print(f"alpha={alpha:.5f} beta={beta:.5f} L={L}: brute(n={bn},d={bd:.2e}) "
                  f"cand(n={cn},d={cd:.2e}) {status}")
    print("ALL OK" if ok else "SOME FAILURES")
