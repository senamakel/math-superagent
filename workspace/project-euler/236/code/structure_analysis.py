"""Pattern analysis of the 35 oracle m values for PE236.

Checks, exactly:
 1. All 35 distinct, m>1, sorted strictly increasing by value.
 2. Denominator divisibility by 59 (and other primes).
 3. Prime support of numerators / denominators.
 4. The largest few m and what separates them.
 5. Relationship between m = p/q and the structure-theorem quantities.
"""
from fractions import Fraction
from math import gcd
import sympy

pairs = [
(1476,1475),(60,59),(902,885),(3321,3245),(41,40),(123,118),(63,59),(328,295),
(533,472),(738,649),(1353,1180),(205,177),(1722,1475),(697,590),(492,413),(1066,885),
(287,236),(1230,1003),(369,295),(615,472),(1599,1180),(80,59),(81,59),(82,59),
(2460,1711),(861,590),(615,413),(451,295),(369,236),(492,295),(205,118),(738,413),
(108,59),(574,295),(123,59)]

vals = [Fraction(p,q) for p,q in pairs]

# ---- 1. distinct & increasing ----
print("count:", len(vals))
print("distinct:", len(set(vals)) == len(vals))
print("sorted strictly increasing:",
      all(vals[i] < vals[i+1] for i in range(len(vals)-1)))
print("smallest:", vals[0], "largest:", vals[-1])

# ---- 2. denominator divisibility by 59 ----
not59 = [(p,q) for p,q in pairs if q % 59 != 0]
print("\ndenominators NOT divisible by 59:", not59)

# ---- 3. prime support ----
alln = set(); alld = set()
for p,q in pairs:
    alln |= set(sympy.factorint(p))
    alld |= set(sympy.factorint(q))
print("prime support of all numerators:", sorted(alln))
print("prime support of all denominators:", sorted(alld))

# ---- 4. gaps between largest few ----
sv = sorted(vals)
print("\nlargest 8 m values:")
for v in sv[-8:]:
    print("   ", v, "=", v.numerator, "/", v.denominator)
gaps = [float(sv[i+1]-sv[i]) for i in range(len(sv)-1)]
print("max gap:", max(gaps), "at index", gaps.index(max(gaps)))
print("second largest:", sv[-2], "  largest:", sv[-1])

# ---- structure-theorem quantities for the largest (123/59) ----
A = [5248,1312,2624,5760,3936]
B = [640,1888,3776,3776,5664]
SA, SB = sum(A), sum(B)
p,q = 123,59
print("\n=== largest m = %d/%d structure ===" % (p,q))
for i in range(5):
    g = gcd(A[i]*q, B[i]*p)
    c = A[i]*q//g; d = B[i]*p//g
    K = g//max(p,q)
    w = q*SB*c - p*SA*d
    print(f"  i={i} a={A[i]} b={B[i]}: g={g} (thr {max(p,q)}), c={c} d={d}, K={K}, w={w}")

# What is the tightest constraint that would bound m above 123/59?
# largest possible m = 246/295 * max ratio... check the bound any m must satisfy
print("\nSA=",SA,"SB=",SB,"SB/SA=",Fraction(SB,SA))
