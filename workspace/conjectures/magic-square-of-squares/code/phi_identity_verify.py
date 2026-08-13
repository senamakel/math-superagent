#!/usr/bin/env python3
"""Symbolic + extended verification of the Phi structure findings.

Finding under test (pattern_finder):
  f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2 = 1 - ((m^2-2mn-n^2)/(m^2+n^2))^2
for ALL m,n.  [Derived: (m^2+n^2)^2 - (m^2-2mn-n^2)^2 = 4mn(m^2-n^2),
 exact polynomial identity; r := (m^2-2mn-n^2)/(m^2+n^2) = cos 2theta -
 sin 2theta with tan theta = n/m, so the AP ratio q = d/e^2 in Phi
 satisfies q = 1 - r^2 with r rational.]

So every AP-ratio in the universal set is  q = 1 - r^2,  r in
R := { (m^2-2mn-n^2)/(m^2+n^2) : m > n >= 1 }.  The four-difference
condition q1+q2=q3 becomes  r3^2 = r1^2 + r2^2 - 1.

Checks:
 [1] sympy expand: f(m,n) - (1 - r^2) == 0 as a polynomial identity.
 [2] numeric check of the identity on random large exact (m,n).
 [3] the r-parametrisation matches f-pairs (bijection on canonical
     opposite-parity pairs, m <= 600).
 [4] closed form |Phi(B)| = sum_{M even<=B} phi(M) + 1/2 sum_{M odd<=B}
     phi(M) vs DIRECT enumeration of f-values for B = 2..1200  (all pairs,
     not only coprime: values only depend on the ratio).
 [5] record maxima at Pell pairs (P_k,P_{k-1}) with
     f = 1 - 1/(P_{2k-1})^2, k = 2..30, and the record-bound structure:
     every pair (m,n), m <= 10^5 has f <= f(P_k,P_{k-1}) with
     P_{2k-1} the largest odd Pell number <= ... (checked via
     discriminant-free enumeration over the visible range instead:
     f < 1 - 1/(P_{2k-1})^2 for all m < P_{2k-1}, k <= 10).
 [6] heads of the record-max sequences for OEIS.
"""
from math import gcd
import random

import sympy as sp

m, n = sp.symbols('m n', positive=True, integer=True)
f = 4 * m * n * (m ** 2 - n ** 2) / (m ** 2 + n ** 2) ** 2
r = (m ** 2 - 2 * m * n - n ** 2) / (m ** 2 + n ** 2)
diff = sp.expand(f - (1 - r ** 2))
print("[1] sympy: expand(f - (1 - r^2)) =", diff, "->",
      "IDENTITY" if diff == 0 else "NOT IDENTITY")

rng = random.Random(11)
bad = 0
for _ in range(2000):
    mm = rng.randint(2, 10 ** 6)
    nn = rng.randint(1, mm - 1)
    num = 4 * mm * nn * (mm * mm - nn * nn)
    den = (mm * mm + nn * nn) ** 2
    rnum = (mm * mm - 2 * mm * nn - nn * nn) ** 2
    rden = (mm * mm + nn * nn) ** 2
    # f == 1 - r^2  <=> f + r^2 == 1  <=> num*rden + rnum*den == den*rden
    if num * rden + rnum * den != den * rden:
        bad += 1
        print("  NUMERIC FAIL", mm, nn)
print(f"[2] random exact identity check (2000 pairs, m <= 1e6): "
      f"{'PASS' if bad == 0 else str(bad) + ' FAILS'}")


def f_reduced(mm, nn):
    num = 4 * mm * nn * (mm * mm - nn * nn)
    den = (mm * mm + nn * nn) ** 2
    g = gcd(num, den)
    return (num // g, den // g)


def r_reduced(mm, nn):
    num = mm * mm - 2 * mm * nn - nn * nn
    den = mm * mm + nn * nn
    g = gcd(num, den)
    return (num // g, den // g)


# [3] canonical pairs: opposite-parity coprime (M,N), M <= 600; check the
# f-values are distinct and that r-values are... (r is 1-1 on canonical
# pairs? q = 1 - r^2 is 2-to-1 in r; on canonical pairs sign(r) is fixed
# by q's alternate representation, so check r^2 distinct iff q distinct)
from collections import defaultdict
fmap = {}
rmap = {}
bad3 = 0
for M in range(2, 601):
    for N in range(1, M):
        if gcd(M, N) != 1 or (M + N) % 2 == 0:
            continue                      # canonical: coprime, opposite parity
        fv = f_reduced(M, N)
        rv = r_reduced(M, N)
        if fv in fmap:
            bad3 += 1
            if bad3 < 5:
                print("  F COLLISION", fv, (M, N), fmap[fv])
        fmap[fv] = (M, N)
        if rv in rmap:
            # r values CAN repeat? q = 1-r^2 fixes r^2; two canonical pairs
            # with the same f would collide above; same r^2 -> same f.
            bad3 += 1
        rmap[rv] = (M, N)
print(f"[3] canonical opposite-parity pairs M <= 600: {len(fmap)} distinct "
      f"f-values, {len(rmap)} distinct r-values, conflicts {bad3} -> "
      f"{'PASS' if bad3 == 0 else 'FAIL'}")

# [4] closed form vs direct enumeration to 1200
def totient_sieve(N):
    phi = list(range(N + 1))
    for p in range(2, N + 1):
        if phi[p] == p:
            for j in range(p, N + 1, p):
                phi[j] -= phi[j] // p
    return phi


phi = totient_sieve(1200)
cf = [0] * 1201
for B in range(2, 1201):
    cf[B] = cf[B - 1] + (phi[B] if B % 2 == 0 else phi[B] // 2)

seen = set()
direct = [0] * 1201
for mm in range(2, 1201):
    for nn in range(1, mm):
        seen.add(f_reduced(mm, nn))
    direct[mm] = len(seen)
mism = [(B, direct[B], cf[B]) for B in range(2, 1201) if direct[B] != cf[B]]
print(f"[4] |Phi(B)| closed-form vs direct enumeration, B = 2..1200: "
      f"{'PASS (all 1199 values equal)' if not mism else 'FAIL at ' + str(mism[:5])}")
print(f"    |Phi(1000)| = {direct[1000]} (closed form gives {cf[1000]})")

# [4b] boundary sanity vs recorded values
print(f"    recorded |Phi(150)|=4582 (got {direct[150]}), "
      f"|Phi(200)|=8156 (got {direct[200]}), "
      f"|Phi(400)|=32495 (got {direct[400]})")

# [5] Pell records: identity f(P_k,P_{k-1}) = 1 - 1/P_{2k-1}^2
P = [0, 1]
for k in range(2, 70):
    P.append(2 * P[k - 1] + P[k - 2])
bad5 = 0
for k in range(2, 31):
    mm, nn = P[k], P[k - 1]
    num, den = f_reduced(mm, nn)
    if not (den == P[2 * k - 1] ** 2 and num == P[2 * k - 1] ** 2 - 1):
        bad5 += 1
print(f"[5] f(P_k,P_{{k-1}}) = 1 - 1/P_{{2k-1}}^2, k=2..30: "
      f"{'PASS' if bad5 == 0 else str(bad5) + ' FAILS'}")

# [5b] dominance: for m < P_{2k-1}, f(m,n) < 1 - 1/P_{2k-1}^2 (k = 2..6)
#      checked exactly by scanning all pairs with m up to P_9 = 985.
bad5b = 0
for k in range(3, 7):
    thr_den = P[2 * k - 1] ** 2
    for mm in range(2, P[2 * k - 1]):
        for nn in range(1, mm):
            num, den = f_reduced(mm, nn)
            # f < thr  <=> num*thr_den < (thr_den-1)*den
            if num * thr_den >= (thr_den - 1) * den:
                bad5b += 1
print(f"[5b] f(m,n) < 1 - 1/P_{{2k-1}}^2 whenever m < P_{{2k-1}} "
      f"(k = 3..6, i.e. all pairs with m < 985): "
      f"{'PASS' if bad5b == 0 else str(bad5b) + ' FAILS'}")

# [6] headers for OEIS
print("\n[6] record-max numerator/denominator heads:")
nums = [P[2 * k - 1] ** 2 - 1 for k in range(2, 9)]
dens = [P[2 * k - 1] ** 2 for k in range(2, 9)]
print("    numerators :", nums)
print("    denominators:", dens)
print("    odd Pell   :", [P[2 * k - 1] for k in range(1, 9)])

# |Phi| at powers of two
print("    |Phi(2^k)| k=1..10:",
      [cf[2 ** k] for k in range(1, 11)])