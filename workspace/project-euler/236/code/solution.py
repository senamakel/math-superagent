"""Derived exact-arithmetic solver for PE236 (Luxury Hampers).

Finds every m > 1 for which the six equalities hold, with exact integer
arithmetic only, and reports the largest as a reduced fraction.

Method (the structural reduction; each step is proved in lib/pe236.py):
  1. Any valid m satisfies the per-product condition for product 1
     (t_1/b_1 = m*s_1/a_1), so m = a_1*t/(b_1*s) for some 1<=s<=a_1,
     1<=t<=b_1.  Candidates are the distinct reduced fractions of those
     pairs with numerator > denominator (m > 1).
  2. For a reduced candidate m = p/q, per-product feasibility is the gcd
     threshold g_i = gcd(a_i*q, b_i*p) >= max(p,q); the minimal spoilage
     pair is (c_i, d_i) = (a_i*q, b_i*p)/g_i and the multipliers run
     1 <= k_i <= K_i = g_i//max(p,q).
  3. The overall equality reduces to the exact bounded subset sum
     sum_i k_i*(q*SB*c_i - p*SA*d_i) = 0, solved with sets of reachable
     sums on the positive- and negative-weight sides.

Complexity: O(a_1*b_1) gcds to build the candidate set (a_1, b_1 are fixed
input data), then per candidate five gcds and — only for candidates passing
all five gcd thresholds — a 5-product subset sum with sets bounded by
prod_i K_i.  No search over anything larger than the fixed input data.

Validation: asserts total valid m == 35 and smallest == 1476/1475 (the
statement's oracle); for the largest, reconstructs an explicit witness
k_i and checks all six equalities literally with fractions.Fraction.
"""
from fractions import Fraction

from lib.pe236 import A, B, base_set, overall_feasible, reconstruct_ks, literal_witness


def main():
    a1, b1 = A[0], B[0]  # product 1 = Beluga Caviar
    print(f"candidate base: product 1, a1={a1}, b1={b1}, "
          f"({a1*b1} (s,t) pairs)")

    cand = sorted((p, q) for (p, q) in base_set(a1, b1) if p > q)
    print(f"distinct reduced candidates with m > 1: {len(cand)}")

    valid = [(p, q) for (p, q) in cand if overall_feasible(p, q)]
    valid.sort(key=lambda pq: Fraction(pq[0], pq[1]))

    assert len(valid) == 35, f"expected 35 valid m, got {len(valid)}"
    assert valid[0] == (1476, 1475), \
        f"smallest should be 1476/1475, got {valid[0][0]}/{valid[0][1]}"
    assert valid[-1] == (123, 59), \
        f"largest disagrees with prior runs' 123/59: got {valid[-1][0]}/{valid[-1][1]}"

    print(f"\ntotal valid m: {len(valid)}")
    for p, q in valid:
        print(f"  m = {p}/{q}  ~ {p/q:.9f}")

    print("\nSMALLEST:", valid[0][0], "/", valid[0][1])
    print("LARGEST :", valid[-1][0], "/", valid[-1][1])

    # Explicit witness and literal six-equality verification for the largest.
    p, q = valid[-1]
    ks = reconstruct_ks(p, q)
    assert ks is not None, f"no subset-sum witness for largest m {p}/{q}"
    ok, s, t = literal_witness(p, q, ks)
    print(f"\nlargest m = {p}/{q}: k = {ks}")
    print("  s =", s)
    print("  t =", t)
    for i in range(5):
        lhs = Fraction(t[i], B[i])
        rhs = Fraction(p, q) * Fraction(s[i], A[i])
        print(f"  product {i}: t_i/b_i = {lhs}"
              f"   (p/q)*s_i/a_i = {rhs}"
              f"   equal: {lhs == rhs}")
    lhs = Fraction(sum(s), sum(A))
    rhs = Fraction(p, q) * Fraction(sum(t), sum(B))
    print(f"  overall: sum(s)/SA = {lhs}"
          f"   (p/q)*sum(t)/SB = {rhs}"
          f"   equal: {lhs == rhs}")
    assert ok, "literal six-equality check failed for the largest m"
    print("  LITERAL SIX-EQUALITY CHECK PASSED for largest m")

    print("\nFINAL ANSWER:", p, "/", q)


if __name__ == "__main__":
    main()