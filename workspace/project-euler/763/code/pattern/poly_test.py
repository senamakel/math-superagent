# Hypothesis: D(N) = 3^(N-1) * P(N), P a polynomial in N of fixed degree.
# Test on exact rationals: does D(N)/3^(N-1) have constant finite differences?
from fractions import Fraction
from sympy import Rational

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
     514419, 1749267, 5949063]

# ratios R(N) = D(N)/3^(N-1) for N>=2
R = [Fraction(D[N], 3**(N-1)) for N in range(2, len(D))]
print("R(N)=D(N)/3^(N-1):")
for k, r in enumerate(R):
    print(f"  N={k+2}: {r} = {float(r):.6f}")

# finite differences of R
diff = list(R)
print("\nFinite differences:")
d = 0
while len(diff) > 1:
    diff = [b-a for a, b in zip(diff, diff[1:])]
    d += 1
    # check if constant
    vals = set(diff)
    print(f"  order {d}: all_equal={len(vals)<=1}, count={len(diff)}, last_val={diff[-1]}")
    if len(vals) <= 1:
        print(f"  => R(N) is a polynomial of degree {d}")
        break

# Also test the implied recurrence: char poly (lambda-3)^(d+1)
# D[n] = sum_{j=1}^{m} binom(m,j)*3^{j}*(-1)^{j+1}... actually for (x-3)^m:
# D must satisfy sum_{j=0}^{m} C(m,j) 3^{m-j} (-1)^? Let's instead directly check
# whether a recurrence with all-char-root-3 holds. Skip; poly test is decisive.
