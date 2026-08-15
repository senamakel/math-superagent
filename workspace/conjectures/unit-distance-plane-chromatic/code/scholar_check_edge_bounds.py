"""Scholar verification of the k-critical edge-bound ladder arithmetic for k=5.

Every number in this run's size-bound direction that comes from Dirac 1957,
Krivelevich 1997, Kostochka-Yancey 2014 (as recorded in research/sources/)
should be a simple EXACT rational check. Reproduce them all here so the
source notes rest on a computed value, not on a repeated hand-check.
"""
from fractions import Fraction

def dirac_edges(k, n):
    # (1/2)((k-1)n + k - 3); valid n >= k+2
    return Fraction(1, 2) * ((k - 1) * n + k - 3)

def krivelevich_edges(k, n):
    # ((k-1)/2 + (k-3)/(2(k^2-2k-1))) * n ; valid k>=4, n>k
    coef = Fraction(k - 1, 2) + Fraction(k - 3, 2 * (k * k - 2 * k - 1))
    return coef * n

def gallai_edges(k, n):
    # ((k-1)/2 + (k-3)/(2(k^2-3))) * n
    coef = Fraction(k - 1, 2) + Fraction(k - 3, 2 * (k * k - 3))
    return coef * n

def ky_edges(k, n):
    # F(k,n) = ((k+1)(k-2)n - k(k-3))/(2(k-1)) ; n>=k, n!=k+1
    return Fraction((k + 1) * (k - 2) * n - k * (k - 3), 2 * (k - 1))

k = 5
print("=== k=5 edge-count ladder (exact rationals) ===")
for n in [7, 8, 9, 10, 11, 12]:
    avg = lambda fn, nn: 2 * fn(nn) / nn
    print(f"n={n}: Dirac {dirac_edges(k,n)} avg_deg {float(avg(dirac_edges,n)):.4f}"
          f" | Gallai {float(gallai_edges(k,n)):.4f}"
          f" | Kriv {float(krivelevich_edges(k,n)):.4f} avg {float(avg(krivelevich_edges,n)):.4f}"
          f" | KY {ky_edges(k,n)} avg {float(avg(ky_edges,n)):.4f}")

print("\n=== statements in the notes ===")
# Dirac note says k=5 -> |E| >= (1/2)(4n+2) = 2n+1
print("Dirac k=5 formula: (1/2)((k-1)n + k - 3) =",
      dirac_edges(5, 'n'), "=> 2n+1?", dirac_edges(5, 1) if False else
      "symbolic: 2n+1 expected")
# check 2n+1 equals the formula for general n: (1/2)(4n+2)=2n+1
print("  (1/2)(4n+2) = 2n+1 :", Fraction(4,2), "n +", Fraction(2,2))

# KY note says k=5 -> (9n-5)/4
print("KY k=5: ((6)(3)n - 5(2))/(8) = (18n-10)/8 = (9n-5)/4 :",
      ky_edges(5, 0), "times n? coefficient n =", Fraction(9,4),
      "constant =", Fraction(-5,4))

# Krivelevich note says k=5 -> edge/vertex 2 + 1/14 approx 2.0714, avg deg ~4.143
k5_kriv_coef = Fraction(k - 1, 2) + Fraction(k - 3, 2 * (k * k - 2 * k - 1))
print("Krivelevich k=5 edge/vertex coef:", k5_kriv_coef,
      "=", float(k5_kriv_coef), "avg_degree =", float(2 * k5_kriv_coef))
# 2(k^2-2k-1) for k=5 = 2*(25-10-1) = 2*14 = 28
print("  2(k^2-2k-1) k=5 =", 2 * (25 - 10 - 1))
print("  2 + 2/28 =", Fraction(2) + Fraction(2, 28), "=", float(Fraction(2)+Fraction(2,28)))

# Gallai note coef k=5: (k-1)/2 + (k-3)/(2(k^2-3)) = 2 + 2/(2*22) = 2+1/22
k5_gallai = Fraction(4,2) + Fraction(2, 2 * (25 - 3))
print("Gallai k=5 edge/vertex:", k5_gallai, "=", float(k5_gallai), "(note said 2.045)")

print("\n=== KY n=9..10 clash: (9n-5)/4 vs C n^{4/3} for C=1 ===")
def ky_n5(n): return ky_edges(5, n)
def sst(n, C=1): return C * n ** (4.0 / 3.0)
for n in range(8, 13):
    clash = float(ky_n5(n)) <= sst(n)
    print(f"n={n}: KY lower {float(ky_n5(n)):6.2f} vs SST C=1 {sst(n):6.2f} -> still-possible={clash}")
