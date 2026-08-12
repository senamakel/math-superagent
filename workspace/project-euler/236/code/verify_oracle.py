"""Independent verification of code/brute.py's oracle for PE236.

Two independent checks:
  A. For every m reported valid by brute.py, reconstruct an explicit witness
     (s_i = k_i*c_i, t_i = k_i*d_i) via subset-sum/backtracking and verify the
     six equalities LITERALLY with exact Fraction arithmetic:
         per product i:  t_i/b_i == (p/q) * s_i/a_i
         overall:        sum(s_i)/sum(a_i) == (p/q) * sum(t_i)/sum(b_i)
  B. Recompute the valid-m set from a DIFFERENT base product (index 0) and
     confirm the count is the same 35 and the same set.

This is a second route to the same numbers, independent of brute.py's own
subset-sum reachability logic in the reported-answer path.
"""
from fractions import Fraction
from math import gcd


A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]
SA = sum(A)
SB = sum(B)


def base_set(ai, bi):
    S = set()
    for s in range(1, ai + 1):
        for t in range(1, bi + 1):
            num = ai * t
            den = bi * s
            g = gcd(num, den)
            S.add((num // g, den // g))
    return S


def witness(p, q):
    """Return k_1..k_5 with sum k_i w_i = 0 and 1<=k_i<=K_i, or None."""
    c = [0] * 5
    d = [0] * 5
    K = [0] * 5
    for i in range(5):
        g = gcd(A[i] * q, B[i] * p)
        c[i] = (A[i] * q) // g
        d[i] = (B[i] * p) // g
        K[i] = min(A[i] // c[i], B[i] // d[i])
        if K[i] < 1:
            return None
    w = [q * SB * c[i] - p * SA * d[i] for i in range(5)]
    # subset-sum DP with parent tracking, keeping the states dict of each stage.
    # stages[i] = states after products 0..i-1 have been added.
    stages = []
    states = {0: None}
    stages.append(states)
    for i in range(5):
        nxt = {}
        for val, prev in states.items():
            for k in range(1, K[i] + 1):
                v2 = val + k * w[i]
                if v2 not in nxt:
                    nxt[v2] = (k, val)
        states = nxt
        stages.append(states)
    if 0 not in states:
        return None
    ks = [0] * 5
    val = 0
    for i in reversed(range(5)):
        k, prev = stages[i + 1][val]  # stages[i+1] includes product i
        ks[i] = k
        val = prev
    return ks


def literal_check(p, q, ks):
    """Check the six equalities literally with Fractions."""
    s = [ks[i] * (A[i] * q // gcd(A[i] * q, B[i] * p)) for i in range(5)]
    t = [ks[i] * (B[i] * p // gcd(A[i] * q, B[i] * p)) for i in range(5)]
    per_product = True
    for i in range(5):
        lhs = Fraction(t[i], B[i])
        rhs = Fraction(p, q) * Fraction(s[i], A[i])
        if lhs != rhs:
            per_product = False
            break
    overall = (Fraction(sum(s), SA) ==
               Fraction(p, q) * Fraction(sum(t), SB))
    return per_product and overall, s, t


def main():
    # ---- Check A: every reported m has a literal witness ----
    reported = [(1476, 1475), (60, 59), (902, 885), (3321, 3245), (41, 40),
                (123, 118), (63, 59), (328, 295), (533, 472), (738, 649),
                (1353, 1180), (205, 177), (1722, 1475), (697, 590),
                (492, 413), (1066, 885), (287, 236), (1230, 1003),
                (369, 295), (615, 472), (1599, 1180), (80, 59), (81, 59),
                (82, 59), (2460, 1711), (861, 590), (615, 413), (451, 295),
                (369, 236), (492, 295), (205, 118), (738, 413), (108, 59),
                (574, 295), (123, 59)]
    bad = 0
    for p, q in reported:
        ks = witness(p, q)
        if ks is None:
            print(f"FAIL: m={p}/{q}: no subset-sum witness")
            bad += 1
            continue
        ok, s, t = literal_check(p, q, ks)
        if not ok:
            print(f"FAIL: m={p}/{q}: literal six-equality check failed")
            print(f"  s={s} t={t}")
            bad += 1
        else:
            print(f"OK   m={p}/{q}: witness s={s} t={t}")
    print(f"Check A: {len(reported) - bad}/{len(reported)} m values have a "
          f"literal witness satisfying all six equalities")

    # ---- Check B: independent count from base product 0 ----
    C = base_set(A[0], B[0])
    results = []
    for (num, den) in C:
        if num <= den:
            continue
        g = gcd(num, den)
        p, q = num, den  # base_set returns reduced pairs, so g=1
        if witness(p, q) is not None:
            results.append((p, q))
    # Sort by fraction VALUE (p/q), not by tuple (p,q): tuple order is
    # lexicographic and would misreport the extremes in Check C.
    results = sorted(set(results), key=lambda pq: Fraction(pq[0], pq[1]))
    reported_set = set(reported)
    independent_set = set(results)
    print(f"Check B: independent base-0 count = {len(results)} "
          f"(brute.py reported {len(reported_set)})")
    print("Check B: sets equal:", independent_set == reported_set)

    # ---- Check C: smallest/largest agree ----
    if results:
        print("Check C: smallest", results[0][0], "/", results[0][1])
        print("Check C: largest ", results[-1][0], "/", results[-1][1])


main()