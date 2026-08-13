#!/usr/bin/env python3
"""Librarian cross-check: verify the newly downloaded OEIS catalogue records
(A090162 family values, A180058 witness pairs) against direct exact arithmetic,
and re-verify the family identity C(n+1,k+1) = C(n,k+2) at the parametrized
points. Exact integer arithmetic only."""
import math
from decimal import Decimal, getcontext

# --- Fibonacci ---
def F(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# --- exact binomial ---
def C(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

# 1. A090162: a(n) = C(F(2n)F(2n+1), F(2n-1)F(2n) - 1)
print("A090162 family values (n=1..4):")
for n in range(1, 5):
    top = F(2 * n) * F(2 * n + 1)
    bot = F(2 * n - 1) * F(2 * n) - 1
    val = C(top, bot)
    print(f"  n={n}: C({top},{bot}) = {val}")

# 2. Identity check: at (n,k) = (F_{2j+2}F_{2j+3}-1, F_{2j}F_{2j+3}-1)
#    C(n+1, k+1) == C(n, k+2), the Singmaster/Lind family.
print("\nFamily identity C(n+1,k+1) == C(n,k+2) at parametrized points:")
for j in range(1, 6):
    n = F(2 * j + 2) * F(2 * j + 3) - 1
    k = F(2 * j) * F(2 * j + 3) - 1
    lhs = C(n + 1, k + 1)
    rhs = C(n, k + 2)
    ok = lhs == rhs
    print(f"  j={j}: n={n} k={k} C(n+1,k+1)=C(n,k+2)={lhs} -> {'OK' if ok else 'MISMATCH'}")

# 3. A180058 pairs: verify each row-count exemplar decomposition.
print("\nA180058 witnesses (half-triangle pairs):")
pairs = {
    2: [(2, 1)],
    6: [(4, 2), (6, 1)],
    120: [(10, 3), (16, 2), (120, 1)],
    3003: [(14, 6), (15, 5), (78, 2), (3003, 1)],
}
for a, reps in pairs.items():
    vals = [C(n, k) for (n, k) in reps]
    ok = all(v == a for v in vals)
    print(f"  a={a}: {reps} -> all equal a? {ok}")

# 4. Convention translation: N(a) (both mirrors + trivial) = 2 * row-count for
#    non-central witnesses (no k = n/2 among the pairs above).
print("\nConvention translation N(a) = 2 * (half-triangle count):")
for a, reps in pairs.items():
    half = len(reps)
    full = 2 * half  # both mirrors + trivial pair: each pair {(n,k),(n,n-k)}
    print(f"  a={a}: {half} half-triangle solutions -> N(a) = {full} (both mirrors, incl. trivial)")

# 5. OEIS A090162 second member against run record.
print("\nCross-check with witnesses.json records:")
expect = {"120": 6, "210": 6, "3003": 8, "1540": 6, "7140": 6, "11628": 6, "24310": 6}
for a, e in expect.items():
    a_int = int(a)
    # count pairs (n,k), 1<=k<n, n<=a, mirror-inclusive, trivial included
    # find all k<=n/2 with C(n,k)=a_int, n<=a_int (trivial row n=a gives 1 pair)
    cnt = 0
    for k in range(1, 40):
        lo, hi = 2 * k, a_int
        while lo <= hi:
            mid = (lo + hi) // 2
            c = C(mid, k)
            if c == a_int:
                cnt += 1
                break
            if c < a_int:
                lo = mid + 1
            else:
                hi = mid - 1
    full = 2 * cnt
    ok = full == e
    print(f"  {a}: counted {cnt} half-triangle, N={full} (expect {e}) -> {'OK' if ok else 'MISMATCH'}")