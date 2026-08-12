"""Look for structure in m-1, and in the fraction of values sharing 41/59 form."""
from fractions import Fraction
import sympy

pairs = [
(1476,1475),(60,59),(902,885),(3321,3245),(41,40),(123,118),(63,59),(328,295),
(533,472),(738,649),(1353,1180),(205,177),(1722,1475),(697,590),(492,413),(1066,885),
(287,236),(1230,1003),(369,295),(615,472),(1599,1180),(80,59),(81,59),(82,59),
(2460,1711),(861,590),(615,413),(451,295),(369,236),(492,295),(205,118),(738,413),
(108,59),(574,295),(123,59)]

vals = [Fraction(p,q) for p,q in pairs]
sorted_vals = sorted(vals)

# m-1 values (as fractions) -- look for pattern
print("=== m-1 for the smallest six ===")
for v in sorted_vals[:6]:
    print(f"   m-1 = {v-1}  denom factors {sympy.factorint((v-1).denominator)}")

print("\n=== m-1 for the largest six ===")
for v in sorted_vals[-6:]:
    print(f"   m-1 = {v-1}")

# how many m equal 41*x/(59*y) type with reduction
ones = [1 for _ in pairs]

# check numerators of the form: is every numerator divisible by 41? 
# largest=123=3*41, but many aren't. Instead check: how many m have 59 in denominator.
cnt59 = sum(1 for _,q in pairs if q%59==0)
print("\ndenominators divisible by 59:", cnt59, "of", len(pairs))

# The answer 123/59. Show each m as (decimal) to see clustering near top.
print("\n=== top 6 by value with decimals ===")
for v in sorted_vals[-6:]:
    print(f"   {v} = {float(v):.6f}")

# confirm 123/59 > all others and its ratio to second largest
print("\n123/59 - 574/295 =", Fraction(123,59)-Fraction(574,295))
