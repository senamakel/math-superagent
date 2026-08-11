"""Best left/right alpha-approximation for the PE591 core subproblem.

Given non-square d, target beta in [0,1), and bound B >= 0, find b in [0,B]
minimizing the circular distance from {b*alpha} to beta, where
alpha = sqrt(d) - floor(sqrt(d)) in (0,1).

Governing theorem (Cabanillas-Lopez & Labbe, arXiv:1904.01874,
Propositions 9 & 10, Algorithm 3(ii)): the minimizer lies among candidates

  RIGHT (Prop 9): n = 0 ;  n = sum_{i=1..2k-1} b_i q_{i-1} + j*q_{2k-1},
                            j in {0..b_{2k}-1}, k>=1
  LEFT  (Prop 10): n =     n = sum_{i=1..2k} b_i q_{i-1} + j*q_{2k},
                            j in {0..b_{2k+1}-1}, k>=0

built from the CF of alpha = [0; a1,a2,...], the continuants
q_{-1}=0,q_0=1,q_k=a_k q_{k-1}+q_{k-2}, the convergent errors
delta_{-1}=1,delta_0=alpha,delta_k=-a_k delta_{k-1}+delta_{k-2} (>0, down to 0),
and the greedy alpha-numeration digits b_k = min(a_k, ceil(beta_{k-1}/delta_{k-1}))
with beta_k = b_k*delta_{k-1} - beta_{k-1}.

Complexity O(log B): q_k grows geometrically for a quadratic alpha, so only
O(log B) levels k are needed. All candidate b values <= B are exact integers;
the circular distances are computed in mpmath at DPS=200 to resolve the tiny
winning gaps.

Returns (best_b, best_dist, candidates) where best_b is the b in [0,B] with
minimal circular distance best_dist, and candidates is the sorted list of all
candidate values <= B.
"""
import math


def _sqrt_cf_period(d):
    """Periodic continued fraction a0 + [0; a1, a2, ...] of sqrt(d).

    Returns (a0, period) where a0 = floor(sqrt(d)) and period is the repeating
    block [a1, a2, ..., a_L] (a_L = 2*a0). Exactly, integer arithmetic.
    """
    a0 = math.isqrt(d)
    m, n, a = 0, 1, a0
    period = []
    seen = {}
    while True:
        key = (m, n, a)
        if key in seen:
            break
        seen[key] = len(period)
        m = n * a - m
        n = (d - m * m) // n
        a = (a0 + m) // n
        period.append(a)
    return a0, period


def core_best(d, beta, B, dps=200, max_digits=20000):
    """Return (best_b, best_dist, candidates). See module docstring."""
    import mpmath as mp
    mp.mp.dps = dps
    mp.pretty = True

    if B < 0:
        return 0, mp.mpf(1), [0]

    a0, period = _sqrt_cf_period(d)
    L = len(period)
    alpha = mp.sqrt(mp.mpf(d)) - a0

    # Build q_k, p_k (exact ints), delta_k (mp) up to when q_k > B.
    q = {-1: 0, 0: 1}
    p = {-1: 1, 0: 0}
    delta = {-1: mp.mpf(1), 0: alpha}

    def digit(k):
        return period[(k - 1) % L]

    # Build until q[k] > B with a safety margin, or hit max_digits.
    k = 1
    need_more = True
    while need_more and k <= max_digits:
        ak = digit(k)
        q[k] = ak * q[k - 1] + q[k - 2]
        p[k] = ak * p[k - 1] + p[k - 2]
        delta[k] = -ak * delta[k - 1] + delta[k - 2]
        if q[k] > B:
            need_more = False
        k += 1
    nmax = k - 1  # last index built

    # Greedy alpha-numeration of beta: digits b_k (1-indexed).
    b = {}
    bet = beta
    for kk in range(1, nmax + 1):
        ak = digit(kk)
        ratio = bet / delta[kk - 1]
        # ceil of positive ratio at high precision
        cr = int(ratio)
        if mp.mpf(cr) < ratio:
            cr += 1
        bk = min(ak, max(0, cr))
        b[kk] = bk
        bet = bk * delta[kk - 1] - bet

    # prefix_i = sum_{t=1..i} b_t * q_{t-1}
    prefix = {0: 0}
    s = 0
    for i in range(1, nmax + 1):
        s += b[i] * q[i - 1]
        prefix[i] = s

    cands = set()
    cands.add(0)  # trivial right candidate n=0

    # RIGHT candidates (Prop 9): idx=2k-1, j in {0..b_{2k}-1}
    kk = 1
    while 2 * kk <= nmax:
        idx = 2 * kk - 1
        step = q[idx]
        P = prefix[idx]
        bmax = b.get(2 * kk, 0)
        for j in range(bmax):
            n = P + j * step
            if n <= B:
                cands.add(n)
        kk += 1

    # LEFT candidates (Prop 10): idx=2k, j in {0..b_{2k+1}-1}
    kk = 0
    while 2 * kk + 1 <= nmax:
        idx = 2 * kk
        step = q[idx]
        P = prefix[idx]
        bmax = b.get(2 * kk + 1, 0)
        for j in range(bmax):
            n = P + j * step
            if n <= B:
                cands.add(n)
        kk += 1

    cands = sorted(c for c in cands if 0 <= c <= B)

    # Evaluate each candidate's circular distance to beta.
    def circdist(n):
        f = n * alpha - mp.floor(n * alpha)
        d = f - beta
        if d < 0:
            d += 1
        return min(d, 1 - d)

    best_b = None
    best_d = mp.mpf(2)
    for n in cands:
        d = circdist(n)
        if d < best_d:
            best_d = d
            best_b = n
    if best_b is None:
        best_b = 0
        best_d = circdist(0)
    return best_b, best_d, cands
