"""Pin down which oracle m-values carry 'extra' primes and confirm extremes/gaps."""
from fractions import Fraction
import sympy

pairs = [
(1476,1475),(60,59),(902,885),(3321,3245),(41,40),(123,118),(63,59),(328,295),
(533,472),(738,649),(1353,1180),(205,177),(1722,1475),(697,590),(492,413),(1066,885),
(287,236),(1230,1003),(369,295),(615,472),(1599,1180),(80,59),(81,59),(82,59),
(2460,1711),(861,590),(615,413),(451,295),(369,236),(492,295),(205,118),(738,413),
(108,59),(574,295),(123,59)]

sv = sorted((Fraction(p,q), p, q) for p,q in pairs)

# Which values carry primes outside the 'core' {2,3,5} plus 41 (num) / 59 (den)?
core = {2,3,5}
print("=== values with numerator prime outside {2,3,5,41} ===")
for v,p,q in sv:
    extra = set(sympy.factorint(p)) - core - {41}
    if extra:
        print(f"  {p}/{q} = {p} extra-num-primes {sorted(extra)}")
print("=== values with denominator prime outside {2,3,5,59} ===")
for v,p,q in sv:
    extra = set(sympy.factorint(q)) - core - {59}
    if extra:
        print(f"  {p}/{q} = {q} extra-den-primes {sorted(extra)}")

print("\n=== denominator not divisible by 59 ===")
for v,p,q in sv:
    if q % 59 != 0:
        print(f"  {p}/{q}")
print("count of denom-div-by-59:", sum(1 for _,p,q in sv if q%59==0), "of", len(sv))

print("\n=== every m > 1 ===")
print(all(v>1 for v,_,_ in sv))
print("\nlargest: %d/%d = %s" % (sv[-1][1], sv[-1][2], sv[-1][0]))
print("second largest: %d/%d = %s" % (sv[-2][1], sv[-2][2], sv[-2][0]))
print("gap largest vs 2nd:", float(sv[-1][0]-sv[-2][0]))
print("smallest: %d/%d = %s" % (sv[0][1], sv[0][2], sv[0][0]))
