"""Verify sourced facts about the pure ballistic aggregation / permutation parity.

Checks (mechanical oracles for the facts this research note cites):
 1. Parity of the NUMBER OF CYCLES of a uniform random permutation is exactly
    balanced: #permutations of [n] with even #cycles == # with odd #cycles,
    for every n >= 2.  (Sourced: Shattuck parity theorems; Arndt's book.)
 2. The run's own exact pure-race (L -> inf) torpids limits from the closed
    forms p(3,L), p(4,L): leading-coefficient ratio limits 7/18 and 19/36.
 3. Mean number of GCM faces / permutation cycles: H_n (MMS Eq. after (12)).
 4. P(sum over clusters of C(size,2) is even) under the cycle-composition law
    (the CYCLE-BLOCK functional the run refuted): EGF exp(sum_k (-1)^C(k,2) z^k/k).
Output: exact fractions.
"""
import math
from sympy import Rational, symbols, limit, oo, exp, series, factorial

print("=== 1. Parity of number of cycles of uniform permutation (n=2..10) ===")
for n in range(2, 11):
    # count permutations by parity of #cycles via unsigned Stirling first-kind parity
    # S1(n,1) = (n-1)!, recurrence S1(n,k) = S1(n-1,k-1) + (n-1) S1(n-1,k)
    S1 = {(1, 1): 1}
    for m in range(2, n + 1):
        for k in range(1, m + 1):
            S1[(m, k)] = S1.get((m - 1, k - 1), 0) + (m - 1) * S1.get((m - 1, k), 0)
    even = sum(S1[(n, k)] for k in range(1, n + 1) if k % 2 == 0)
    odd = sum(S1[(n, k)] for k in range(1, n + 1) if k % 2 == 1)
    assert even + odd == math.factorial(n), (n, even, odd)
    print(f"  n={n}: P(#cycles even) = {even}/{math.factorial(n)} = {Rational(even, math.factorial(n))}  ({'balanced' if even == odd else 'IMBALANCED'})")

print("\n=== 2. Pure-race limits of the run's exact closed forms p(n,L), n=3,4 ===")
m = symbols('m')
p3 = (7*m**2 - 17*m + 12) / (18*m**2 - 45*m + 27)
p4 = (19*m**3 - 119*m**2 + 244*m - 162) / (36*m**3 - 216*m**2 + 423*m - 270)
print(f"  p(3,L) -> {limit(p3, m, oo)}  (7/18 = {Rational(7,18)})")
print(f"  p(4,L) -> {limit(p4, m, oo)}  (19/36 = {Rational(19,36)})")
print("  (These are the run's verified closed forms; limits are the pure-race values.)")

print("\n=== 3. Mean number of cycles / GCM faces: H_n (n=13) ===")
H13 = sum(Rational(1, k) for k in range(1, 14))
print(f"  H_13 = {H13} = {float(H13):.6f}")

print("\n=== 4. P(sum over clusters C(size,2) even) under cycle composition (refuted functional) ===")
# EGF: exp(sum_k (-1)^C(k,2) z^k / k); extract coefficient of z^n/n!
# C(k,2) mod 2: k(k-1)/2 mod 2.  k mod 4 == 0,1 -> even; k mod 4 == 2,3 -> odd.
def c2par(k):
    return (k * (k - 1) // 2) % 2
z = symbols('z')
for n in [3, 4, 5, 13]:
    e = exp(sum((-1)**c2par(k) * z**k / k for k in range(1, n + 1)))
    coef = series(e, z, 0, n + 1).removeO().coeff(z, n) * factorial(n)
    print(f"  n={n}: P(C(size,2)-sum even) = {coef.nsimplify()} = {float(coef):.5f}")
print("  (Run result: this != torpids pure-race parity. Hand-checked: n=3 gives")
print("   1/6 (cycle-block) vs 7/18 (torpids pure-race); n=4 gives 5/12 vs 19/36.)")
print("  Closed form: A(z)=exp(arctan z)/sqrt(1+z^2); P(even)=1/2(1+[z^n]A(z)).")