import sympy
from math import gcd

pairs = [
(1476,1475),(60,59),(902,885),(3321,3245),(41,40),(123,118),(63,59),(328,295),
(533,472),(738,649),(1353,1180),(205,177),(1722,1475),(697,590),(492,413),(1066,885),
(287,236),(1230,1003),(369,295),(615,472),(1599,1180),(80,59),(81,59),(82,59),
(2460,1711),(861,590),(615,413),(451,295),(369,236),(492,295),(205,118),(738,413),
(108,59),(574,295),(123,59)]

nums = [p for p,q in pairs]
dens = [q for p,q in pairs]

def pf(n):
    return sympy.factorint(n)

print("=== numerators prime factorized ===")
for i,(p,q) in enumerate(pairs):
    print(f"{i:2d}  {p}/{q} = {pf(p)} / {pf(q)}")

print()
print("nums:", nums)
print("dens:", dens)
