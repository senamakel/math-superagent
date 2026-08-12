"""Naive oracle for PE236: enumerate spoilage counts, find all valid m.

For each product i, enumerate ALL pairs (s_i, t_i) with
1 <= s_i <= a_i, 1 <= t_i <= b_i.  The per-product condition
    t_i/b_i = m * (s_i/a_i)
is a constraint on the SINGLE rational m shared by all five products:
    m = (t_i/b_i) / (s_i/a_i) = a_i t_i / (b_i s_i).
So m, reduced, must lie in the intersection over i of the set of reduced
values of a_i*t/(b_i*s).  (m>1 is enforced later.)

Then, for each candidate m = p/q found in the intersection, we must decide
whether there EXIST actual integer spoilage counts realizing that m for all
five products and satisfying the overall constraint
    (sum s)/(sum a) = m * (sum t)/(sum b).

Given m = p/q (reduced), the per-product condition fixes the reduced ratio
s_i/t_i = (a_i q)/(b_i p); write this reduced ratio as c_i/d_i.  Then all
solutions for product i are s_i = k_i*c_i, t_i = k_i*d_i with integer
k_i >= 1 and the bounds k_i*c_i <= a_i, k_i*d_i <= b_i, i.e.
1 <= k_i <= K_i = min(a_i//c_i, b_i//d_i).

The overall constraint becomes
    (sum k_i c_i)/SA = (p/q) (sum k_i d_i)/SB
    <=>  q*SB*sum k_i c_i = p*SA*sum k_i d_i
    <=>  sum_i k_i * (q*SB*c_i - p*SA*d_i) = 0.
This is a bounded integer linear equation in k_1..k_5 with each
1 <= k_i <= K_i, solved by subset-sum over the positive and negative
weights (bounded knapsack / two-set intersection).

This is a completely naive oracle: it enumerates every per-product pair
(memory-light: per product we only keep the *distinct* reduced values, at
most a_i*b_i of them but collected via numpy chunking) and, for each
surviving m, an exact bounded integer search for the multipliers k_i.
"""
import numpy as np
from math import gcd
from fractions import Fraction
from itertools import product as iproduct

A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]
SA = sum(A)
SB = sum(B)
N = 5


def per_product_mset(ai, bi, chunk=2**18):
    """All distinct reduced values of ai*t/(bi*s) for 1<=s<=ai, 1<=t<=bi."""
    S = set()
    ss = np.arange(1, ai + 1, dtype=np.int64)
    ts = np.arange(1, bi + 1, dtype=np.int64)
    for lo in range(0, bi, chunk):
        t = ts[lo:lo + chunk]
        # outer products of shape (len(t), ai)
        num_all = ai * t[:, None]                      # ai*t
        den_all = bi * ss[None, :]                     # bi*s
        g_all = np.gcd(num_all, den_all)
        num_r = (num_all // g_all).ravel()
        den_r = (den_all // g_all).ravel()
        vals = np.unique(num_r.astype(np.int64) * (2**40) + den_r)
        for v in vals:
            S.add((v >> 40, v & ((1 << 40) - 1)))
    return S


def overall_has_solution(p, q):
    """Exact check that SOME (k_1..k_5) with 1<=k_i<=K_i satisfies
    sum k_i w_i = 0 where w_i = q*SB*c_i - p*SA*d_i."""
    c = []
    d = []
    K = []
    for i in range(N):
        num = A[i] * q
        den = B[i] * p
        g = gcd(num, den)
        ci, di = num // g, den // g
        Ki = min(A[i] // ci, B[i] // di)
        c.append(ci)
        d.append(di)
        K.append(Ki)
        if Ki < 1:
            return False
    w = [q * SB * c[i] - p * SA * d[i] for i in range(N)]
    pos = [(w[i], K[i]) for i in range(N) if w[i] > 0]
    neg = [(-w[i], K[i]) for i in range(N) if w[i] < 0]
    if not pos and not neg:
        return True  # all weights zero: every (k_1..k_5) works
    if not pos or not neg:
        return False

    def reachable(items):
        cur = {0}
        for wi, Ki in items:
            nxt = set()
            for base in cur:
                add = 0
                for k in range(1, Ki + 1):
                    add += wi
                    nxt.add(base + add)
            cur = nxt
        return cur

    return not reachable(pos).isdisjoint(reachable(neg))


def verify(p, q, kvals):
    """Verify all six equalities exactly with integer arithmetic."""
    s = [kvals[i] * (A[i] * q // gcd(A[i] * q, B[i] * p)) for i in range(N)]
    t = [kvals[i] * (B[i] * p // gcd(A[i] * q, B[i] * p)) for i in range(N)]
    per = all(t[i] * A[i] * q == s[i] * B[i] * p for i in range(N))  # t/b = m s/a
    overall = Fraction(sum(s), SA) == Fraction(p, q) * Fraction(sum(t), SB)
    return per and overall and all(1 <= s[i] <= A[i] and 1 <= t[i] <= B[i]
                                   for i in range(N))


def main():
    sets = [per_product_mset(A[i], B[i]) for i in range(N)]
    for i, S in enumerate(sets):
        print(f"product {i}: distinct reduced a_i*t/(b_i*s) values: {len(S)}")
    inter = set.intersection(*sets)
    print("candidates in per-product intersection:", len(inter))

    # m = num/den, reduced already, keep only m > 1
    cands = [(num, den) for (num, den) in inter if num > den]

    results = []
    for (num, den) in cands:
        if overall_has_solution(num // gcd(num, den), den // gcd(num, den)):
            results.append(Fraction(num, den))
    results = sorted(set(results))
    print()
    print("DISTINCT m > 1 satisfying all six equalities:", len(results))
    for m in results:
        print(f"  {m.numerator}/{m.denominator}")
    print()
    if results:
        print("SMALLEST:", results[0])
        print("LARGEST :", results[-1])
    else:
        print("NO m found")


if __name__ == "__main__":
    main()