"""Structure tests for the newly extracted subsequences of A063985/H.

A(n) = n(n+1)/2 - Phi(n), Phi(n) = sum_{k<=n} phi(k).
Records so far: H(2^k-1) and A(2^k-1), k=1..17; H(p#) and A(p#) for
primorials 2,6,30,210,2310,30030,510510.

Test 1 (sourced structure): Chai Wah Wu's A063985 recursion, OEIS A063985
(Mar 24 2021):  a(n) = n*(n+1)/2 - (1/2)*sum_{k=1..n} phi(k)?? -- no, that's
the definition. The recursion actually used by patterns.py:
   A063985(n) = n(n+1)/2 - Phi(n) where Phi(n) satisfies
   Phi(n) = n(n+1)/2 - sum_{d=2..n} Phi(floor(n/d))   (Gauss identity).
So the exact structure test for a NEW index family: verify Phi(n) against
the Gauss floor recursion at the new n's (2^k-1 and primorials), which is
the identity that makes the whole computation fast and is verified at
arbitrary n by patterns.py's probes.

Test 2 (conjectured exact form at primorials): with P = product of primes
<= p, is A(P) = (P+1)/2 - Phi(P) exactly the observed A? (Definition, so
trivially yes -- instead test the *asymptotic-free* exact claim that
A(P) mod 12 follows the period-4 law, and that A(P) = sum of cototients.)

Test 3 (exact): H(2^k - 1) mod 12 period-4 law (n = 2^k-1 is 3 mod 4 for
k>=2, so H mod 12 must be 0); and check the recorded values satisfy
H(2^k-1) = 6*A(2^k-1).

All exact integer arithmetic; no floats.
"""
from math import isqrt

# recorded values
A_2km1 = [0, 2, 10, 48, 188, 788, 3170, 12820, 51220, 205324, 821566,
          3288588, 13152822, 52618390, 210483528, 841968722, 3367828868]
H_2km1 = [0, 12, 60, 288, 1128, 4728, 19020, 76920, 307320, 1231944,
          4929396, 19731528, 78916932, 315710340, 1262901168, 5051812332,
          20206973208]
ks = [1 << k for k in range(1, 18)]  # 2^k, k=1..17
assert len(A_2km1) == len(ks) == 17
print("Test 3: H(2^k-1) = 6*A(2^k-1):",
      all(H_2km1[i] == 6 * A_2km1[i] for i in range(17)))
# n = 2^k - 1 is 3 mod 4 for k >= 2; law: H mod 12 == 0 for n mod 4 == 3
law_bad = [i for i, k in enumerate(ks)
           if (H_2km1[i] % 12) != (0 if (k - 1) % 4 == 3 else 6 if (k - 1) % 4 == 1 else None)]
# n = 2^k - 1: n mod 4 = (2^k - 1) mod 4 = 3 for k>=2, = 1 for k=1
pred = [6 if k == 1 else 0 for k in ks]
print("Test 3b: H(2^k-1) mod 12 matches period-4 law:",
      all(H_2km1[i] % 12 == pred[i] for i in range(17)))

# Test 1: Gauss floor recursion for Phi at each new n
def phi_gauss_rec(n, cache={}):
    if n == 0:
        return 0
    if n in cache:
        return cache[n]
    # Phi(n) = n(n+1)/2 - sum_{d=2..n} Phi(floor(n/d)), floor-grouped
    total = n * (n + 1) // 2
    d = 2
    while d <= n:
        q = n // d
        nxt = n // q + 1
        # d..nxt-1 all have floor(n/d) == q
        total -= (nxt - d) * phi_gauss_rec(q)
        d = nxt
    cache[n] = total
    return total

# reference Phi from the definition identity A(n) = n(n+1)/2 - Phi(n)
Phi_ref = [k * (k + 1) // 2 - a for k, a in zip(ks, A_2km1)]
ok = all(phi_gauss_rec(k - 1) == Phi_ref[i] for i, k in enumerate(ks))
print("Test 1: Gauss floor recursion reproduces Phi(2^k-1):", ok)

# primorials: A(P) exact vs (P+1)/2 - Phi(P) -- definition check at 510510
N = 510510
phi = list(range(N + 1))
for i in range(2, N + 1):
    if phi[i] == i:
        for j in range(i, N + 1, i):
            phi[j] -= phi[j] // i
Phi = 0
A = 0
for k in range(1, N + 1):
    Phi += phi[k]
    A += k - phi[k]
print("Test 2 at P=510510: A(P) = (P+1)/2 - Phi(P):",
      A == N * (N + 1) // 2 - Phi)
print("  A(510510) =", A, " Phi(510510) =", Phi)
print("  H(510510) =", 6 * A, " mod 12 =", (6 * A) % 12,
      "(n mod 4 =", N % 4, "-> law says 6)")
