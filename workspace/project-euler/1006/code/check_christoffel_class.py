"""Verify the Christoffel-conjugacy structure of the length-k factors of the
infinite Fibonacci word W (limit of 0->01, 1->0: 0100101001001...).

For each k in 1..12:
  1. collect the k+1 distinct length-k factors of W,
  2. compute each factor's number of 1s,
  3. group the k+1 factors into orbits under cyclic rotation,
  4. check the hypothesis: does the factor set equal (k rotations of ONE
     Christoffel word) union ONE singular (non-conjugate) word?
     That holds iff gcd(k, m) = 1 where m = round(k/phi^2) is the number of
     ones (a primitive Christoffel word of slope m/k then exists).

Exact integer arithmetic only.
"""

from math import gcd
from fractions import Fraction

from lib.fibword import fib_prefix


def round_ones(k):
    """m = round(k / phi^2), computed in exact rational arithmetic.

    1/phi^2 = (3 - sqrt(5))/2, so  m = round(k(3 - sqrt5)/2)
          = floor((k(3 - sqrt5) + 1)/2).
    Write S = sqrt(5).  We need the unique integer n with
        n <= (k(3-S)+1)/2 < n+1
    i.e.    (3k-(2n+1))/k < S <= (3k-(2n-1))/k.
    Candidate n from a high-precision decimal; then verify/correct against
    the exact rational comparison S > r  <=>  5 > r*r (r > 0), and
    S <= r  <=>  5 <= r*r.  S is irrational so boundaries never hit.
    """
    from decimal import Decimal, getcontext
    getcontext().prec = 40
    S = Decimal(5).sqrt()
    n = int((k * (3 - S) + 1) / 2)   # candidate floor

    def S_gt(r):
        """True iff sqrt(5) > r, r a positive Fraction."""
        return Fraction(5, 1) > r * r

    # required:  (3k-(2n+1))/k  <  S  <=  (3k-(2n-1))/k
    while True:
        L = Fraction(3 * k - (2 * n + 1), k)
        U = Fraction(3 * k - (2 * n - 1), k)
        if not S_gt(L):        # S <= L : n too big
            n -= 1
            continue
        if S_gt(U):            # S > U : n too small
            n += 1
            continue
        return n


def rotations(w):
    n = len(w)
    return {w[i:] + w[:i] for i in range(n)}


def conjugacy_classes(factors):
    """Group factors into orbits under cyclic rotation (restricted to the set)."""
    classes = []
    seen = set()
    for f in factors:
        if f in seen:
            continue
        rot = rotations(f)
        cls = [g for g in factors if g in rot]
        for g in cls:
            seen.add(g)
        classes.append(cls)
    return classes


def main():
    phi2 = (3 + 5 ** 0.5) / 2
    kmax = 12
    W = fib_prefix(5 * kmax + 1)  # safely longer than any needed prefix
    print("W prefix (first 40):", W[:40])
    print()

    for k in range(1, kmax + 1):
        factors = set(W[i:i + k] for i in range(len(W) - k + 1))
        factors = sorted(factors)
        assert len(factors) == k + 1, (k, len(factors))

        ones = [f.count('1') for f in factors]
        classes = conjugacy_classes(factors)
        sizes = sorted((len(c) for c in classes), reverse=True)

        m = round_ones(k)
        g = gcd(k, m)
        primitive = (g == 1)
        # hypothesis: class sizes are {k, 1}
        holds = (sizes == [k, 1]) if k > 0 else False

        print(f"=== k = {k} ===")
        print("  factors:", factors)
        print("  #1s    :", ones)
        print("  classes:", [sorted(c) for c in classes])
        print("  class sizes:", sizes)
        print(f"  m = round(k/phi^2) = {m}, gcd(k,m) = gcd({k},{m}) = {g}, "
              f"primitive Christoffel slope exists: {primitive}")
        print(f"  hypothesis 'k conjugates + 1 singular' holds: {holds} "
              f"(expected {primitive})")
        print()

    # explicit k=4 hand-check
    print("========== k = 4 hand-check ==========")
    k = 4
    factors4 = sorted(set(W[i:i + k] for i in range(len(W) - k + 1)))
    ones4 = [f.count('1') for f in factors4]
    classes4 = conjugacy_classes(factors4)
    print("factors:", factors4)
    print("one-counts:", ones4, "-> matches hand-check {1,2,1,2,2}:",
          sorted(ones4) == sorted([1, 2, 1, 2, 2]))
    print("class sizes:", sorted(len(c) for c in classes4, reverse=True),
          "-> matches hand-check {2,1,2}:",
          sorted(len(c) for c in classes4, reverse=True) == sorted([2, 1, 2]))


if __name__ == "__main__":
    main()
