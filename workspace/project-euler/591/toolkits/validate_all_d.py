"""Independent validation: for ALL non-square d<100 at n=10^6, compare
brute-force argmin b (scan [0,L]) against Cabanillas-candidate argmin.
This is a full cross-check of the scalable method on every d we need.
"""
import math, time, mpmath as mp
mp.mp.dps = 50
pi = mp.mpf('3.14159265358979323846264338327950288419716939937510')

def cf_terms(x, nterms):
    a = []
    for _ in range(nterms):
        ai = int(mp.floor(x)); a.append(ai)
        x = x - ai
        if x == 0: break
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
    b = {}; cur = beta
    for k in range(1, n + 1):
        bk = min(a[k], mp.ceil(cur / delta[k-1]))
        b[k] = int(bk); cur = bk * delta[k-1] - cur
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

def cand_best(L, alpha, beta):
    cands = [c for c in candidates(alpha, beta) if c <= L]
    cmin = min(cands, key=lambda c: dist(c, alpha, beta))
    return cmin, dist(cmin, alpha, beta)

if __name__ == "__main__":
    n = 1_000_000
    ok_all = True
    t0 = time.time()
    mism = []
    for d in range(2, 100):
        if math.isqrt(d)**2 == d: continue
        sd = mp.sqrt(d)
        L = int(mp.floor(n / sd))
        alpha = sd - mp.floor(sd)
        beta = pi - 3
        bn, bd = brute_best(L, alpha, beta)
        cn, cd = cand_best(L, alpha, beta)
        ok = abs(bd - cd) < mp.mpf('1e-40')
        if not ok:
            ok_all = False
            mism.append((d, bn, cn, bd, cd))
    print(f"n={n}, all {90} d: ALL_MATCH={ok_all}, mismatches={mism}")
    print(f"elapsed {time.time()-t0:.1f}s")