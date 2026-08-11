"""Verify Cabanillas Prop 9/10 (arXiv:1904.01874) candidate structure.

We follow the paper EXACTLY (irrational alpha case, Prop 9/10 Case 2):
  best right: {n alpha} >= beta;  n = sum_{i=1}^{2k-1} b_i q_{i-1} + j q_{2k-1}, j in 0..b_{2k}-1
  best left : {n alpha} <= beta;  n = sum_{i=1}^{2k}   b_i q_{i-1} + j q_{2k},   j in 0..b_{2k+1}-1
where (b_i) from Algorithm 3(ii): b_k = min(a_k, ceil(beta_{k-1}/delta_{k-1})), beta_k = b_k delta_{k-1} - beta_{k-1}.
Check: every RECORD HOLDER of ||n alpha - beta|| over 0..N is in the candidate set,
and (more importantly) the argmin value over 0..N equals the min over candidates within N.
Uses exact-ish arithmetic via fractions where possible; alpha,beta fixed irrationals -> high-precision mpmath.
"""

import math
import mpmath as mp

mp.mp.dps = 60

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
    """convergent denominators q[-1]=0,q[0]=1 and q[k] for k>=1; a is [a0,a1,...]."""
    q = { -1: 0, 0: 1 }
    for k in range(1, len(a) + 1):
        q[k] = a[k-1] * q[k-1] + q[k-2]
    return q

def numeration(alpha, beta, a, nterms):
    """Algorithm 3(ii): digits b_k, deltas delta_k (delta_-1=1, delta_0=alpha,...).
    Here `a` = full CFE list [a0,a1,a2,...] so the k-th partial quotient (k>=1) is a[k]."""
    delta = { -1: mp.mpf(1), 0: alpha }
    # delta_k = delta_{k-2} - a_k delta_{k-1}, with a_k = a[k] (a[0]=a0=0 here)
    for k in range(1, nterms + 2):
        delta[k] = delta[k-2] - a[k] * delta[k-1]
    b = {}
    cur = beta
    for k in range(1, nterms + 1):
        bk = min(a[k], mp.ceil(cur / delta[k-1]))
        b[k] = int(bk)
        cur = bk * delta[k-1] - cur
    return b, delta

def candidates(alpha, beta, nterms=45):
    a = cf_terms(alpha, nterms)
    q = conv_q(a)
    b, delta = numeration(alpha, beta, a, nterms)
    out = {0}
    # best right: k in N* -> index 1..2k-1 (max odd <= nterms)
    for k in range(1, nterms // 2 + 1):
        idx_end = 2*k - 1
        if idx_end > nterms: break
        pref = sum(b[i] * q[i-1] for i in range(1, idx_end + 1))
        jmax = b[2*k] - 1 if 2*k <= nterms else 0
        for j in range(0, jmax + 1):
            out.add(pref + j * q[2*k - 1])
    # best left: k in N -> 2k <= nterms-1
    for k in range(0, nterms // 2):
        idx_end = 2*k
        if idx_end > nterms: break
        pref = sum(b[i] * q[i-1] for i in range(1, idx_end + 1))
        # j in 0..b_{2k+1}-1; if 2k+1 > nterms, b=0 -> only j=0
        jmax = b[2*k + 1] - 1 if 2*k + 1 <= nterms else 0
        for j in range(0, jmax + 1):
            out.add(pref + j * q[2*k])
    return sorted(x for x in out if x >= 0), b, q

def dist(n, alpha, beta):
    v = n * alpha - beta
    fr = v - mp.floor(v)
    return min(fr, 1 - fr)

def brute_records(N, alpha, beta):
    """all strictly-decreasing record values of ||n alpha - beta|| over n in [0,N] with holder n."""
    best = mp.mpf(10)
    recs = []
    for n in range(0, N + 1):
        d = dist(n, alpha, beta)
        if d < best - mp.mpf('1e-40'):
            best = d
            recs.append((n, d))
    return recs

def run(alpha, beta, N, nterms=45):
    recs = brute_records(N, alpha, beta)
    cands, b, q = candidates(alpha, beta, nterms)
    cset = set(cands)
    # (1) all record holders after 0 must be candidates
    holders = [n for (n, d) in recs if n > 0]
    missing = [n for n in holders if n not in cset]
    # (2) global minimum VALUE over 0..N (not fixed to candidate) equals min over candidates <= N
    brute_min = min(d for (n, d) in recs)
    cand_in = [n for n in cands if n <= N]
    cand_min = min(dist(n, alpha, beta) for n in cand_in) if cand_in else None
    match = cand_min is not None and abs(brute_min - cand_min) < mp.mpf('1e-30')
    return recs, missing, cand_min, brute_min, match, b, cands

if __name__ == "__main__":
    beta = mp.mpf('3.1415926535897932384626433832795028841971693993751058209749445923') - 3
    print("testing alpha = sqrt(d) - floor(sqrt(d)) for d in {2,3,5,7,11}, beta={pi}")
    for sq in [2,3,5,7,11]:
        alpha = mp.sqrt(sq) - mp.floor(mp.sqrt(sq))
        for N in [200, 1000, 5000]:
            recs, missing, cmin, bmin, match, b, cands = run(alpha, beta, N)
            status = "OK" if match else "FAIL"
            print(f"  d={sq} N={N}: brute_min={mp.nstr(bmin,5)} cand_min={mp.nstr(cmin,5)} "
                  f"match={match} missing_holders={missing[:8]} #recs={len(recs)} #cands={len(cands)}")
            if len(missing) > 0:
                print(f"    MISSING record holders: {missing} (need to check if they're in candidate set)")