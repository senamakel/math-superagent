from fractions import Fraction

def S(k):
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

# Direct check of the constant-coefficient recurrence of order 4
# derived from the annihilator (E-4)^2 (E-1)^2:
#   S_{k+4} - 10 S_{k+3} + 33 S_{k+2} - 40 S_{k+1} + 16 S_k == 0
bad = []
for k in range(1, 200):
    lhs = S(k+4) - 10*S(k+3) + 33*S(k+2) - 40*S(k+1) + 16*S(k)
    if lhs != 0:
        bad.append((k, lhs))
print("recurrence order-4 constant-coefficient check over k=1..199:")
print("  number of failures:", len(bad))
if bad:
    print("  first failures:", bad[:5])

# Also verify a 2nd order recurrence with polynomial coefficients is impossible;
# but the real claim is just the constant-coefficient one. Print sample.
print("\nSample exact S_k:")
for k in range(1,8):
    print(f"  k={k}: {S(k)}")
