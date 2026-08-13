#!/usr/bin/env python3
"""Independent reproduction of the genus-closed-form integrality lemma.

Claim (research/notes/genus-integrality-proved.md, claim id
genus-closed-form-integrality): for all integers m, n >= 1,

    N(m,n) = (m-1)(n-1) + 1 - gcd(m,n)   is even,

so g(m,n) = N(m,n)/2 is always an integer.  This is the closed form
g(m,n) = ((m-1)(n-1)+1-gcd(m,n))/2 for the genus of C(x,m)=C(y,n).

The lemma is proved by a four-case parity argument, not by sampling.  This
program is the machine re-check of the full range 1..799 (all four parity
classes), plus a per-class breakdown, in exact integer arithmetic.  It is
linear in the number of pairs (799^2 ~ 6.4e5 gcd calls), constant memory.

Convention note: m, n here are the polynomial degrees (the k1, k2 of
C(x,k1) = C(y,k2) in problem.md, with m < n the interesting case); the
integrality statement holds for all pairs, including m = n and m > n.
"""
import math
import sys

LIMIT = 799  # TASKS.md item 4: parity check over 1..799

counts = {(p, q): [0, 0] for p in (0, 1) for q in (0, 1)}  # (m%2, n%2) -> [odd, even]
total_odd = 0
total_pairs = 0
first_odd = None
for m in range(1, LIMIT + 1):
    for n in range(1, LIMIT + 1):
        N = (m - 1) * (n - 1) + 1 - math.gcd(m, n)
        key = (m % 2, n % 2)
        counts[key][N % 2] += 1
        total_pairs += 1
        total_odd += N % 2
        if N % 2 and first_odd is None:
            first_odd = (m, n, N)

print(f"Parity check of N(m,n) = (m-1)(n-1)+1-gcd(m,n) over 1 <= m, n <= {LIMIT}")
print(f"Total pairs checked: {total_pairs}")
print(f"Pairs with N odd:    {total_odd}")
print("Per parity class (m mod 2, n mod 2) -> [count N odd, count N even]:")
for key in sorted(counts):
    print(f"  m%2={key[0]}, n%2={key[1]}: {counts[key]}")

# Also report the two algebraic forms agree on the same range (internal
# consistency of the equivalent expressions, not a genus computation).
agree = 0
for m in range(1, 400):
    for n in range(1, 400):
        N1 = (m - 1) * (n - 1) + 1 - math.gcd(m, n)
        N2 = (m - 1) * n - (m - 2) - math.gcd(m, n)
        agree += (N1 == N2)
print(f"Two algebraic forms agree on 1..399 x 1..399: {agree} / 399^2")

if total_odd == 0 and agree == 399 * 399:
    print("RESULT: INTEGRALITY REPRODUCED — ZERO odd values, both forms agree.")
    sys.exit(0)
else:
    print(f"RESULT: FAILED — see above (first odd: {first_odd})")
    sys.exit(1)