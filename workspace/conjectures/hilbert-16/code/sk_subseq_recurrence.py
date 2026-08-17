from fractions import Fraction

def S(k):
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

# Subsequence a_j = S_{3j} (j>=1). Theoretically:
#   S_{3j} = 4^{3j-1}(3j - 13/6) + (6j-1)/3
#          = (1/4)·64^j·(3j - 13/6) + (6j-1)/3
# so a_j = poly(j)·64^j + poly(j)  -> annihilated by (E-64)^2 (E-1)^2 (order 4).
coeffs = [1, -(64*2+2), (64*64 + 4*64 + 1), -(2*64*64 + 64*64), 64*64]
# (E-64)^2 (E-1)^2 = (E^2 -128E +4096)(E^2 -2E +1)
#                  = E^4 -(2+128)E^3 +(1+256+4096)E^2 -(128+8192)E +4096
c = [1, -130, 4353, -8320, 4096]
bad = []
for j in range(1, 200):
    a = [S(3*(j+i)) for i in range(5)]
    lhs = sum(ci*ai for ci, ai in zip(c, a))
    if lhs != 0:
        bad.append((j, lhs))
print("order-4 recurrence (E-64)^2(E-1)^2 on a_j = S_{3j}, j=1..199:")
print("  failures:", len(bad), bad[:3])
print("  coefficients:", c)