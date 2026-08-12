"""Brute-force oracle for PE236 (Luxury Hampers).

Naive but obviously correct. Exact integer arithmetic.

Definition (from the statement):
  a_i, b_i : counts supplied by A and B of product i.
  s_i, t_i : counts that spoiled for A and B of product i, 1<=s_i<=a_i, 1<=t_i<=b_i.
  Per-product condition: B's rate worse than A by factor m>1:
        t_i / b_i  = m * (s_i / a_i)          for every i.
  Overall condition:  A's rate worse than B by the same m:
        (Sum s_i)/(Sum a_i) = m * (Sum t_i)/(Sum b_i).

Method (still brute force, only the bookkeeping is efficient):
  * Any valid m must be one of the reduced fractions
        red( a_1 * t / (b_1 * s) ),   1<=s<=a_1, 1<=t<=b_1
    achievable by product 1 (the product with the fewest (s,t) pairs).
    Collect that set C.
  * For each (p,q) in C with p>q (=m>1), test the full set of six conditions.
    Per product i with m=p/q we need s_i/t_i = (a_i q)/(b_i p), so the minimal
    pair is  c_i = a_i q/g,  d_i = b_i p/g,  g = gcd(a_i q, b_i p),  and any
    solution is s_i = k c_i, t_i = k d_i with 1 <= k <= K_i = min(a_i//c_i, b_i//d_i).
    Feasible per product iff K_i >= 1 (equivalently min(g/q, g/p) >= 1).
    Overall then needs  q*SB*sum(k_i c_i) = p*SA*sum(k_i d_i), i.e.
        sum_i k_i * (q*SB*c_i - p*SA*d_i) = 0,   1 <= k_i <= K_i,
    solved by exact subset-sum over the five products.
"""
from math import gcd


A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]
SA = sum(A)
SB = sum(B)


def base_set(ai, bi):
    """All reduced fractions red(ai*t/(bi*s)) with 1<=s<=ai, 1<=t<=bi."""
    S = set()
    for s in range(1, ai + 1):
        for t in range(1, bi + 1):
            num = ai * t
            den = bi * s
            g = gcd(num, den)
            S.add((num // g, den // g))
    return S


def overall_feasible(p, q):
    """Test all six conditions for reduced m = p/q.  Returns True if valid."""
    c = [0] * 5
    d = [0] * 5
    K = [0] * 5
    for i in range(5):
        num = A[i] * q
        den = B[i] * p
        g = gcd(num, den)
        ci = num // g
        di = den // g
        c[i] = ci
        d[i] = di
        K[i] = min(A[i] // ci, B[i] // di)
        if K[i] < 1:
            return False  # not even feasible per product i
    # overall: sum_i k_i * w_i = 0,  w_i = q*SB*c_i - p*SA*d_i
    w = [q * SB * c[i] - p * SA * d[i] for i in range(5)]
    pos = [(w[i], K[i]) for i in range(5) if w[i] > 0]
    neg = [(-w[i], K[i]) for i in range(5) if w[i] < 0]
    if not pos and not neg:
        return True  # all w_i == 0 -> every k works
    if not pos or not neg:
        return False

    def totals(items):
        cur = {0}
        for wi, Ki in items:
            nxt = set()
            for base in cur:
                for k in range(1, Ki + 1):
                    nxt.add(base + k * wi)
            cur = nxt
        return cur

    sp = totals(pos)
    sn = totals(neg)
    return not sp.isdisjoint(sn)


def main():
    # Smallest product by number of (s,t) pairs is product 1.
    i0 = min(range(5), key=lambda i: A[i] * B[i])
    print(f"base product index {i0}: a={A[i0]} b={B[i0]} -> {A[i0]*B[i0]} (s,t) pairs")
    C = base_set(A[i0], B[i0])
    print("distinct achievable m in base product:", len(C))
    results = []
    for (num, den) in C:
        if num <= den:
            continue  # need m > 1
        g = gcd(num, den)
        p, q = num // g, den // g
        if overall_feasible(p, q):
            results.append((p, q))
    results.sort(key=lambda x: x[0] / x[1])
    print("total valid m:", len(results))
    for p, q in results:
        print(f"  m = {p}/{q}  ~ {p/q:.9f}")
    if results:
        print("SMALLEST", results[0][0], "/", results[0][1])
        print("LARGEST ", results[-1][0], "/", results[-1][1])


if __name__ == "__main__":
    main()
