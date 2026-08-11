"""Test the full method at moderate scale (n = 10^6, L = n/sqrt(d)):

1. Brute force b_d in [0,L] that minimizes ||b alpha - beta||.
2. Cabanillas candidate set; b_cand = candidate minimizing distance (or the
   candidate closest below L in the record order).
3. Check |I| = nint(b sqrt(d) - pi) and I = nint(pi - b sqrt(d)) signs.
4. Check b_d == the Cabanillas candidate with minimum distance.
"""
import math, mpmath as mp
mp.mp.dps = 60
pi = mp.mpf('3.1415926535897932384626433832795028841971693993751058209749445923')

def cf_terms(x, nterms):
    a = []
    for _ in range(nterms):
        ai = int(mp.floor(x))
        a.append(ai)
        x = x - ai
        if x == 0:
            break
        x = 1 / x
    return a

def conv_q(a):
    q = { -1: 0, 0: 1 }
    for k in range(1, len(a)):
        q[k] = a[k] * q[k-1] + q[k-2]
    return q

def numeration(alpha, beta, a, nterms):
    n = min(nterms, len(a) - 2)
    delta = { -1: mp.mpf(1), 0: alpha }
    for k in range(1, n + 2):
        delta[k] = delta[k-2] - a[k] * delta[k-1]
    b = {}
    cur = beta
    for k in range(1, n + 1):
        bk = min(a[k], mp.ceil(cur / delta[k-1]))
        b[k] = int(bk)
        cur = bk * delta[k-1] - cur
    return b, delta

def candidates(alpha, beta, nterms=80):
    a = cf_terms(alpha, nterms)
    q = conv_q(a)
    b, delta = numeration(alpha, beta, a, nterms)
    out = {0}
    for k in range(1, nterms // 2 + 1):
        idx_end = 2*k - 1
        if idx_end > nterms or idx_end not in b: break
        pref = sum(b[i] * q[i-1] for i in range(1, idx_end + 1) if i in b)
        jmax = (b[2*k] - 1) if 2*k in b else 0
        for j in range(0, jmax + 1):
            out.add(pref + j * q[2*k - 1])
    for k in range(0, nterms // 2):
        idx_end = 2*k
        if idx_end > nterms: break
        pref = sum(b[i] * q[i-1] for i in range(1, idx_end + 1) if i in b)
        jmax = (b[2*k + 1] - 1) if 2*k + 1 in b else 0
        for j in range(0, jmax + 1):
            out.add(pref + j * q[2*k])
    return sorted(x for x in out if x >= 0)

def dist(n, alpha, beta):
    v = n * alpha - beta
    fr = v - mp.floor(v)
    return min(fr, 1 - fr)

def brute_best(L, alpha, beta):
    best = None; bestn = None
    for n in range(0, L + 1):
        d = dist(n, alpha, beta)
        if best is None or d < best:
            best = d; bestn = n
    return bestn, best

def test_d(d, n):
    sd = mp.sqrt(d)
    L = int(mp.floor(n / sd))
    alpha = sd - mp.floor(sd)
    beta = pi - 3
    bn, bd = brute_best(L, alpha, beta)
    cands = [c for c in candidates(alpha, beta) if c <= L]
    cmin = min(cands, key=lambda c: dist(c, alpha, beta))
    cd = dist(cmin, alpha, beta)
    ok = (bn == cmin) or abs(bd - cd) < mp.mpf('1e-40')
    I = -mp.nint(bn * sd - pi)   # a = nint(pi - b sqrt d); here negative
    Ialt = mp.nint(pi - bn * sd)
    return bn, bd, cmin, cd, ok, I, Ialt, abs(bn*sd - pi - mp.nint(bn*sd - pi))

if __name__ == "__main__":
    n = 1_000_000
    print(f"n={n}: testing d in {{2,3,5,6,7,8,10,11,13,92,83,57}}")
    for d in [2,3,5,6,7,8,10,11,13,92,83,57]:
        bn, bd, cmin, cd, ok, I, Ialt, f = test_d(d, n)
        print(f"  d={d:2d}: brute b={bn:8d} d={mp.nstr(bd,6)} | cand b={cmin:8d} d={mp.nstr(cd,6)} "
              f"| match={ok} | a=nint(pi-b√d)={Ialt} (I={I}) err={mp.nstr(f,4)}")