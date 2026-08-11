"""Project Euler 591 — Best Approximations by Quadratic Integers.

For each non-square d in [2,99], find
    b_d = argmin over b in [0, L]  of  || b*{sqrt(d)} - {pi} ||_Z
where L = floor(1e13/sqrt(d)), {.} is the fractional part and ||.||_Z the
distance to the nearest integer.  Then
    a_d = nint(pi - b_d*sqrt(d))   (nearest integer),   integral part of the BQA.
We report |a_d| and S = sum_d |a_d|.

b_d is found with the Cabanillas (arXiv:1904.01874) Prop 9/10 candidate-set
method: the candidate set (all "records" of the inhomogeneous three-distance
sequence) contains the argmin, and we pick the candidate of minimum distance.
Verified in toolkits/test_method_scale.py against brute force at n=1e6 for many
d, and against the d=2, n=1e13 oracle giving a = -6188084046055.

All arithmetic on convergents/candidates is exact integer; pi and sqrt(d) are
high-precision mpmath floats.
"""
import math
import mpmath as mp

PI = mp.mpf('3.1415926535897932384626433832795028841971693993751058209749445923')

def cf_terms(x, nterms):
    """Continued fraction [a1; a2, ...] (1-indexed) of x, nterms terms."""
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
    """Denominators q_k of convergents: q[0]=1, q[k]=a[k]q[k-1]+q[k-2]."""
    q = {-1: 0, 0: 1}
    for k in range(1, len(a)):
        q[k] = a[k] * q[k - 1] + q[k - 2]
    return q

def numeration(alpha, beta, a, nterms):
    """Cabanillas alpha-numeration digits b[k] and deltas delta[k]."""
    n = min(nterms, len(a) - 2)
    delta = {-1: mp.mpf(1), 0: alpha}
    for k in range(1, n + 2):
        delta[k] = delta[k - 2] - a[k] * delta[k - 1]
    b = {}
    cur = beta
    for k in range(1, n + 1):
        bk = min(a[k], mp.ceil(cur / delta[k - 1]))
        b[k] = int(bk)
        cur = bk * delta[k - 1] - cur
    return b, delta

def candidates(alpha, beta, nterms):
    """Cabanillas Prop 9/10 candidate set (non-negative integers)."""
    a = cf_terms(alpha, nterms)
    q = conv_q(a)
    b, delta = numeration(alpha, beta, a, nterms)
    out = {0}
    for k in range(1, nterms // 2 + 1):
        idx_end = 2 * k - 1
        if idx_end > nterms or idx_end not in b:
            break
        pref = sum(b[i] * q[i - 1] for i in range(1, idx_end + 1) if i in b)
        jmax = (b[2 * k] - 1) if 2 * k in b else 0
        for j in range(0, jmax + 1):
            out.add(pref + j * q[2 * k - 1])
    for k in range(0, nterms // 2):
        idx_end = 2 * k
        if idx_end > nterms:
            break
        pref = sum(b[i] * q[i - 1] for i in range(1, idx_end + 1) if i in b)
        jmax = (b[2 * k + 1] - 1) if 2 * k + 1 in b else 0
        for j in range(0, jmax + 1):
            out.add(pref + j * q[2 * k])
    return sorted(x for x in out if x >= 0)

def dist(b, alpha, beta):
    v = b * alpha - beta
    fr = v - mp.floor(v)
    return min(fr, 1 - fr)

def solve_d(d, n):
    sd = mp.sqrt(d)
    L = int(mp.floor(n / sd))
    alpha = sd - mp.floor(sd)
    beta = PI - 3  # {pi}
    # Number of CF terms: denominators grow ~ alpha'^k; pick until L is reached.
    nterms = 400
    while True:
        a = cf_terms(alpha, nterms)
        q = conv_q(a)
        if q.get(nterms - 1, 0) > L * 4:
            break
        nterms *= 2
    cands = [c for c in candidates(alpha, beta, nterms) if c <= L]
    b_d = min(cands, key=lambda c: dist(c, alpha, beta))
    a_d = mp.nint(PI - b_d * sd)
    return b_d, a_d, len(cands)

def main():
    n = 10**13
    lines = []
    S = 0
    for d in range(2, 100):
        if int(math.sqrt(d)) ** 2 == d:
            continue  # square
        b, a, nc = solve_d(d, n)
        absa = abs(int(a))
        S += absa
        lines.append(f"{d} {b} {int(a)} {absa}  n_cand={nc}")
        print(f"d={d:2d} b={b:14d} a={int(a):15d} |a|={absa:15d} cand={nc}")
    Sfmt = f"{'S':4s} {'':14s} {'':15s} {S:15d}"
    lines.append(Sfmt)
    with open("results_full.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print(Sfmt)

if __name__ == "__main__":
    main()
