"""Corrected PE591 solver — considers BOTH signs of b.

For d non-square, n=1e13, find (a,b), |a|,|b|<=n, minimizing |pi - (a+b sqrt(d))|.
Equivalently: for each b, a=round(pi-b*sqrt(d)) clamped to [-n,n], error=||b sqrt(d)-pi||_Z.
b can be positive or negative.  By symmetry:
  - b>=0:  minimize ||b alpha - beta||_Z  over b in [0, L], alpha={sqrt d}, beta={pi}
  - b<0:   let m=-b>0, then b sqrt(d)-pi = -m sqrt(d)-pi, fractional part tracking
           ||m alpha - (-beta)|| = ||m alpha - (1-beta)||_Z  (since -beta ≡ 1-beta mod 1)
So run the Cabanillas candidate method for BOTH beta and 1-beta, take the global min,
then a = nint(pi - b sqrt(d)) with sign of b kept.
Verification: reproduces examples 1-4.
"""
import math, mpmath as mp

PI = mp.mpf('3.1415926535897932384626433832795028841971693993751058209749445923')

def cf_terms(x, nterms):
    a = []
    for _ in range(nterms):
        ai = int(mp.floor(x)); a.append(ai)
        x = x - ai
        if x == 0: break
        x = 1 / x
    return a

def conv_q(a):
    q = {-1: 0, 0: 1}
    for k in range(1, len(a)):
        q[k] = a[k] * q[k-1] + q[k-2]
    return q

def numeration(alpha, beta, a, nterms):
    n = min(nterms, len(a) - 2)
    delta = {-1: mp.mpf(1), 0: alpha}
    for k in range(1, n + 2):
        delta[k] = delta[k-2] - a[k] * delta[k-1]
    b = {}; cur = beta
    for k in range(1, n + 1):
        bk = min(a[k], mp.ceil(cur / delta[k-1]))
        b[k] = int(bk); cur = bk * delta[k-1] - cur
    return b, delta

def candidates(alpha, beta, nterms):
    a = cf_terms(alpha, nterms)
    q = conv_q(a)
    b, delta = numeration(alpha, beta, a, nterms)
    out = {0}
    for k in range(1, nterms // 2 + 1):
        idx_end = 2*k - 1
        if idx_end > nterms or idx_end not in b: break
        pref = sum(b[i]*q[i-1] for i in range(1, idx_end+1) if i in b)
        jmax = (b[2*k]-1) if 2*k in b else 0
        for j in range(0, jmax+1):
            out.add(pref + j*q[2*k-1])
    for k in range(0, nterms // 2):
        idx_end = 2*k
        if idx_end > nterms: break
        pref = sum(b[i]*q[i-1] for i in range(1, idx_end+1) if i in b)
        jmax = (b[2*k+1]-1) if 2*k+1 in b else 0
        for j in range(0, jmax+1):
            out.add(pref + j*q[2*k])
    return sorted(x for x in out if x >= 0)

def dist(b, alpha, beta):
    v = b*alpha - beta
    fr = v - mp.floor(v)
    return min(fr, 1-fr)

def solve_d_both(d, n, verbose=False):
    sd = mp.sqrt(d)
    L = int(mp.floor(n / sd))
    alpha = sd - mp.floor(sd)
    beta = PI - 3                     # {pi}
    beta2 = 1 - beta                   # { -pi } = 1 - {pi}
    nterms = 200
    while True:
        a = cf_terms(alpha, nterms)
        q = conv_q(a)
        if q.get(nterms-1, 0) > L*4:
            break
        nterms *= 2
    cands1 = [c for c in candidates(alpha, beta, nterms) if c <= L]
    cands2 = [c for c in candidates(alpha, beta2, nterms) if c <= L]
    b1 = min(cands1, key=lambda c: dist(c, alpha, beta))
    b2 = min(cands2, key=lambda c: dist(c, alpha, beta2))
    d1 = dist(b1, alpha, beta)        # b>0 candidate
    d2 = dist(b2, alpha, beta2)       # b<0 candidate (b = -b2)
    # also include b=0
    if verbose:
        print(f"  d={d}: pos b={b1} err={mp.nstr(d1,6)}; neg b=-{b2} err={mp.nstr(d2,6)}")
    if d1 <= d2:
        b = b1
    else:
        b = -b2
    a = mp.nint(PI - b*sd)
    return b, int(a), abs(int(a))

def run_all(n):
    S = 0
    rows = []
    for d in range(2, 100):
        if math.isqrt(d)**2 == d: continue
        b, a, absa = solve_d_both(d, n)
        S += absa
        rows.append((d, b, a, absa))
    return S, rows

if __name__ == "__main__":
    mp.mp.dps = 80
    # examples
    print("=== worked examples ===")
    for d, n in [(2,10),(5,100),(7,10**6),(2,10**13)]:
        b, a, absa = solve_d_both(d, n, verbose=True)
        print(f"d={d} n={n}: (a={a}, b={b}) |a|={absa}")
    print("=== full run n=1e13 ===")
    S, rows = run_all(10**13)
    for (d,b,a,absa) in rows:
        print(f"d={d:2d} b={b:14d} a={a:15d} |a|={absa:15d}")
    print("S =", S)
    with open('/workspace/results_full_bothsides.txt','w') as f:
        for (d,b,a,absa) in rows:
            f.write(f"{d} {b} {a} {absa}\n")
        f.write(f"S {S}\n")