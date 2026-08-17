from fractions import Fraction
from math import comb

def S(k):
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

# ---- The integer-level recurrence derives from the annihilator (E-4)^2 (E-1)^2
# because 4^{k-1}(k-13/6) is 4^k times a linear-in-k polynomial:
#   polynomial(k) * r^k is annihilated by (E - r)^{deg+1}
# here deg=1 => (E-4)^2; plus the (2k-1)/3 constant-linear term => (E-1)^2.
# Product => order 4: (E-4)^2 (E-1)^2 = E^4 -10E^3 +33E^2 -40E +16.
coeffs = [1, -10, 33, -40, 16]  # S_{k+4}, S_{k+3}, ...
bad = []
for k in range(1, 400):
    lhs = sum(c*S(k+4-i) for i,c in enumerate(coeffs))
    if lhs != 0:
        bad.append(k)
print("Constant-coefficient order-4 recurrence (E-4)^2(E-1)^2 check, k=1..399 failures:", len(bad), bad[:3])

# ---- Which k give S_k integer? Compute denominator structure.
print("\nk with S_k integer up to k=200:  (6 S_k must be divisible appropriately)")
intks = [k for k in range(1,201) if S(k).denominator == 1]
print("  integers:", intks)

# Determine closed form of whether 6·S_k is divisible by 6 -> integer.
# 6 S_k = 4^{k-1}(6k-13) + 2(2k-1) = 4^{k-1}(6k-13) + (4k-2)
# integer iff 4^{k-1}(6k-13) + (4k-2) ≡ 0 mod 6
print("\ninteger k up to 40:", [k for k in range(1,41) if S(k).denominator==1])

# ---- Verify ceil(S_k) equals the explicit integer for all k (monotone structure)
from math import ceil
bad_ceil = [k for k in range(1,50) if ceil(S(k)) != int(S(k)) if S(k).denominator != 1]
print("sum over k=1..49 (guaranteed count added, i.e. sum S_k):", sum(int(S(k)) for k in range(1,50) if S(k).denominator==1))
