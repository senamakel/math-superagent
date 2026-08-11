#!/usr/bin/env python3
"""Verify the Ostrowski-numeration algorithm for best left/right alpha-approximation
against a brute-force oracle on small inputs.

Core subproblem: irrational alpha in (0,1), target beta in [0,1), bound B.
Find b in [0,B] minimizing circular distance dist({b*alpha}, beta).

Algorithm (Cabanillas-Lopez & Labbe arXiv:1904.01874, Props 9 & 10, Alg 3(ii)):
  - CF of alpha: partial quotients a_k, convergent denominators q_k (q_{-1}=0,q_0=1)
  - deltas: delta_{-1}=1, delta_0=alpha, delta_k = -a_k*delta_{k-1}+delta_{k-2}
  - alpha-numeration digits b_k of beta:
        b_k = min(a_k, ceil(beta_{k-1}/delta_{k-1}))
        beta_k = b_k*delta_{k-1} - beta_{k-1}
  - Best RIGHT candidates (Prop 9): n=0;  n = sum_{i=1..2k-1} b_i q_{i-1} + j q_{2k-1}, j in {0..b_{2k}-1}, k>=1
  - Best LEFT candidates (Prop 10):  n = sum_{i=1..2k} b_i q_{i-1} + j q_{2k}, j in {0..b_{2k+1}-1}, k>=0
The answer b in [0,B] is among these candidates (<= B).
"""
from fractions import Fraction
from math import floor, ceil, isqrt

def cf_of_sqrt_frac(d):
    """Return alpha = sqrt(d) - floor(sqrt(d)) as a high-precision Fraction, plus
    its periodic continued fraction [0; a1, a2, ...]."""
    a0 = isqrt(d)
    alpha = None
    # build periodic CF of sqrt(d)
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
    # period = [a1, a2, ..., aT], alpha = [0; a1,...] (periodic)
    per = period  # includes a0? Actually let's recompute carefully
    # The standard: a0=floor(sqrt d). terms after are the period.
    return a0, period  # we'll re-derive alpha below

def alpha_from_cf(a0, period):
    # alpha = sqrt(d) - a0  with CF [0; a1, a2, ...] where period cycles.
    return None

import decimal
from decimal import Decimal, getcontext

def cf_terms_sqrt(d, nterms):
    """Return first nterms partial quotients of sqrt(d): [a0, a1, a2, ...]."""
    a0 = isqrt(d)
    m, n, a = 0, 1, a0
    terms = [a0]
    period = []
    seen = {}
    for _ in range(nterms):
        m = n * a - m
        n = (d - m * m) // n
        a = (a0 + m) // n
        terms.append(a)
        period.append(a)
    return terms, period

def build_arrays(alpha, nterms):
    """alpha in (0,1) irrational. Return a[1..n], q[0..n], delta[0..n]."""
    # CF of alpha = [0; a1, a2, ...]
    # we get them from CF of sqrt(d): alpha's CF is sqrt(d)'s CF minus a0.
    # Instead: compute from alpha directly using Gauss map.
    a = [0]  # 1-indexed
    q = [1]  # q[0] = q_0 = 1 ; need q[-1]=0
    deltas = [alpha]  # delta[0] = delta_0 = alpha ; delta[-1]=1
    x = alpha
    qm1 = 0  # q_{-1}
    qm2 = 1  # q_{-2} (for q_{-2}... actually q_{-1}=0,q_0=1)
    prev_delta = 1.0  # delta_{-1}
    cur_delta = alpha  # delta_0
    ak_list = []
    for k in range(1, nterms + 1):
        ak = int(1 / x)
        ak_list.append(ak)
        a.append(ak)
        # q_k = ak q_{k-1} + q_{k-2}
        qk = ak * q[k - 1] + qm1
        # handle indexing: q list index k, q[k-1]=q_{k-1}
        q.append(qk)
        qm1 = q[k - 1] if k >= 1 else 1
        # delta
        dk = -ak * cur_delta + prev_delta
        deltas.append(dk)
        prev_delta, cur_delta = cur_delta, dk
        x = 1 / x - ak
    return a, q, deltas

def alpha_numeration_digits(beta, a, deltas, nmax):
    """Greedy Algorithm 3(ii): return digits b_k for k=1..nmax."""
    b = [0]  # 1-indexed
    bet = beta
    for k in range(1, nmax + 1):
        ratio = bet / deltas[k - 1]
        bk = int(ceil(ratio)) if ratio > 0 or (ratio == int(ratio)) else int(ratio)
        # ceil in python: -(-ratio//1)
        bk = -((-ratio) // 1)
        bk = min(a[k], bk)
        if bk < 0:
            bk = 0
        b.append(bk)
        bet = bk * deltas[k - 1] - bet
    return b

def candidates(b_digits, q, nmax):
    """Propositions 9 & 10 candidate n values."""
    # prefix sums Sk = sum_{i=1..k} b_i q_{i-1}
    prefix = [0]
    s = 0
    for i in range(1, len(b_digits)):
        s += b_digits[i] * q[i - 1]
        prefix.append(s)
    cands = set()
    cands.add(0)
    # right: n = prefix[2k-1] + j q[2k-1], j in {0..b_{2k}-1}, k>=1
    for k in range(1, nmax // 2 + 1):
        idx = 2 * k - 1
        if idx + 1 < len(b_digits):
            step = q[idx]
            P = prefix[idx]
            for j in range(b_digits[idx + 1]):
                cands.add(P + j * step)
    # left: n = prefix[2k] + j q[2k], j in {0..b_{2k+1}-1}, k>=0
    for k in range(0, nmax // 2 + 1):
        idx = 2 * k
        nxt = 2 * k + 1
        if idx < len(b_digits) and nxt < len(b_digits):
            step = q[idx]
            P = prefix[idx]
            for j in range(b_digits[nxt]):
                cands.add(P + j * step)
    return cands

def circdist(frac, beta):
    d = frac - beta
    if d < 0:
        d += 1
    return min(d, 1 - d)

def algo_best(alpha, beta, B, nterms):
    a, q, deltas = build_arrays(alpha, nterms)
    bd = alpha_numeration_digits(beta, a, deltas, nterms)
    cands = candidates(bd, q, nterms)
    best = 0
    bestd = 2
    for n in cands:
        if 0 <= n <= B:
            f = (n * alpha) - int(n * alpha)
            d = circdist(f, beta)
            if d < bestd - 1e-12:
                bestd = d; best = n
    return best, bestd

def brute(alpha, beta, B):
    best = 0; bd = 2
    for n in range(0, B + 1):
        f = (n * alpha) - int(n * alpha)
        d = circdist(f, beta)
        if d < bd - 1e-12:
            bd = d; best = n
    return best, bd

def test_sqrt_case(d, details=False):
    a0 = isqrt(d)
    alpha = (d ** 0.5) - a0
    import random
    fails = 0
    for _ in range(300):
        B = random.randint(1, 80)
        beta = random.random()
        nterms = 40
        ba, da = algo_best(alpha, beta, B, nterms)
        bb, db = brute(alpha, beta, B)
        if abs(da - db) > 1e-9:
            fails += 1
            if details:
                print(f"  d={d} B={B} beta={beta:.4f}: algo b={ba} d={da:.6f}, brute b={bb} d={db:.6f}")
    return fails

if __name__ == "__main__":
    total = 0
    for d in [2, 3, 5, 7, 10, 13, 17, 19, 21, 29, 41, 97]:
        f = test_sqrt_case(d)
        total += f
        print(f"d={d}: {f} mismatches")
    print("TOTAL mismatches:", total)
