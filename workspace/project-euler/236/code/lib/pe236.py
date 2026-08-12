"""PE236 (Luxury Hampers) — exact integer machinery for the derived method.

Shared by the run's programs so the feasibility test lives in one place and
cannot drift between copies.  All arithmetic exact (ints and
fractions.Fraction); no floats except where a caller explicitly formats a
decimal.

Data
----
A[i], B[i]: counts supplied by A and B of product i, in table order
   (Beluga Caviar, Christmas Cake, Gammon Joint, Vintage Port,
    Champagne Truffles).  SA = sum(A), SB = sum(B).

The derived reduction (the method behind solution.py)
----------------------------------------------------
Write m = p/q > 1 reduced.  Per-product condition t_i/b_i = m*s_i/a_i gives
s_i/t_i = (a_i*q)/(b_i*p).  With g_i = gcd(a_i*q, b_i*p) and the coprime
pair c_i = a_i*q/g_i, d_i = b_i*p/g_i, every feasible spoilage pair is
(s_i, t_i) = k_i*(c_i, d_i), 1 <= k_i <= K_i, where

    K_i = min(a_i//c_i, b_i//d_i) = g_i//max(p,q).

Hence per-product feasibility is exactly the gcd threshold g_i >= max(p,q).
The overall condition  sum_i s_i / SA = (p/q)*sum_i t_i / SB  clears
denominators to

    sum_i k_i * (q*SB*c_i - p*SA*d_i) = 0,      1 <= k_i <= K_i,

a bounded-multiplicity subset sum over the five products, solved exactly
with sets of reachable sums on the positive- and negative-weight sides.

Every valid m must be realisable per-product for product 1 (Beluga):
m = a_1*t/(b_1*s) for its (s,t), so candidates are the distinct reduced
fractions of a_1*t/(b_1*s) over 1<=s<=a_1, 1<=t<=b_1 (see base_set).
"""
from fractions import Fraction
from math import gcd

A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]
SA = sum(A)
SB = sum(B)


def base_set(ai, bi):
    """Distinct reduced fractions red(ai*t/(bi*s)) for 1<=s<=ai, 1<=t<=bi.

    Returns a set of (num, den) pairs, each already in lowest terms.
    """
    S = set()
    for t in range(1, bi + 1):
        for s in range(1, ai + 1):
            g = gcd(ai * t, bi * s)
            S.add((ai * t // g, bi * s // g))
    return S


def per_product(p, q):
    """Derived per-product data for reduced m = p/q.

    Returns (c, d, K) where c[i], d[i] is the coprime minimal spoilage pair
    (s_i, t_i) = k*(c_i, d_i) and K[i] the number of multipliers
    (1 <= k <= K[i]) — or None if some product is infeasible
    (g_i = gcd(a_i*q, b_i*p) < max(p, q)).
    """
    c = [0] * 5
    d = [0] * 5
    K = [0] * 5
    for i in range(5):
        g = gcd(A[i] * q, B[i] * p)
        if g < p or g < q:
            return None
        c[i] = (A[i] * q) // g
        d[i] = (B[i] * p) // g
        K[i] = g // max(p, q)
    return c, d, K


def overall_feasible(p, q):
    """True iff all six equalities hold for some integer spoilage counts.

    Uses the bounded subset sum  sum_i k_i*w_i = 0, 1 <= k_i <= K_i, with
    w_i = q*SB*c_i - p*SA*d_i, by computing the reachable positive-weight
    and negative-weight sums as exact sets and checking the intersection.
    """
    pd = per_product(p, q)
    if pd is None:
        return False
    c, d, K = pd
    w = [q * SB * c[i] - p * SA * d[i] for i in range(5)]
    pos = [(w[i], K[i]) for i in range(5) if w[i] > 0]
    neg = [(-w[i], K[i]) for i in range(5) if w[i] < 0]
    if not pos and not neg:
        return True  # all w_i == 0 -> any k_i combination works
    if not pos or not neg:
        return False  # strictly one-sided weights can never balance to 0

    def reachable(items):
        cur = {0}
        for wi, Ki in items:
            nxt = set()
            for base in cur:
                for k in range(1, Ki + 1):
                    nxt.add(base + k * wi)
            cur = nxt
        return cur

    return not reachable(pos).isdisjoint(reachable(neg))


def reconstruct_ks(p, q):
    """Find k_1..k_5 with sum_i k_i*w_i = 0, 1 <= k_i <= K_i, or None.

    Per-stage dicts: stages[j] maps every reachable sum after products
    0..j-1 to (k_j, previous sum), so the k-vector is recovered by walking
    back from 0.  Exact.  Used to exhibit one explicit witness for a m.
    """
    pd = per_product(p, q)
    if pd is None:
        return None
    c, d, K = pd
    w = [q * SB * c[i] - p * SA * d[i] for i in range(5)]
    stages = [{0: None}]
    for i in range(5):
        prev = stages[-1]
        nxt = {}
        for val in prev:
            for k in range(1, K[i] + 1):
                v2 = val + k * w[i]
                if v2 not in nxt:
                    nxt[v2] = (k, val)
        stages.append(nxt)
    if 0 not in stages[-1]:
        return None
    ks = [0] * 5
    val = 0
    for i in range(4, -1, -1):
        k, prev = stages[i + 1][val]
        ks[i] = k
        val = prev
    return ks


def literal_witness(p, q, ks):
    """Verify the six equalities literally with Fraction arithmetic.

    Returns (ok, s, t) with s[i] = ks[i]*c[i], t[i] = ks[i]*d[i];
    ok is True iff
        t_i/b_i == (p/q)*s_i/a_i        for every i, and
        sum(s)/SA == (p/q)*sum(t)/SB,
    and every count lies in its box (1 <= s_i <= a_i, 1 <= t_i <= b_i).
    """
    c, d, _ = per_product(p, q)
    s = [ks[i] * c[i] for i in range(5)]
    t = [ks[i] * d[i] for i in range(5)]
    per = all(
        Fraction(t[i], B[i]) == Fraction(p, q) * Fraction(s[i], A[i])
        for i in range(5)
    )
    overall = Fraction(sum(s), SA) == Fraction(p, q) * Fraction(sum(t), SB)
    bounds = all(1 <= s[i] <= A[i] and 1 <= t[i] <= B[i] for i in range(5))
    return per and overall and bounds, s, t