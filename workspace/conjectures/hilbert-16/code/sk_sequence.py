from fractions import Fraction

# S_k = 4^{k-1} (k - 13/6) + (2k-1)/3 : number of limit cycles of the
# Christopher-Lloyd (corrected by Li et al.) polynomial systems PH_k of
# degree 2k-1. Source: Buzzi-Novaes 2411.09594, citing [5] Section 3 and
# Han-Li [4].
def S(k):
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

print("k  S_k (exact)                     S_k (float)   ceil  degree=2k-1  H lower bound")
for k in range(1, 16):
    s = S(k)
    from math import ceil
    print(f"{k:2d}  {str(s):30s} {float(s):15.4f} {ceil(s):8d}  {2*k-1}")

# integer sequence: the minimum guaranteed number of limit cycles (ceil of lower bound)
import math
ceilseq = [int(math.ceil(S(k))) for k in range(1, 16)]
print("\nceil(S_k) for k=1..15:", ceilseq)

# also the count at specific degrees 2k-1
print("\nThe degrees and the guaranteed-count sequence (k=1..15):")
for k in range(1,16):
    print(f"  degree {2*k-1}: >= {ceilseq[k-1]}")
