from fractions import Fraction as F
import itertools

n = {1:7, 2:26, 3:70, 4:155, 5:301, 6:532, 7:876, 8:1365, 9:2035, 10:2926, 11:4082}
e = {1:11, 2:69, 3:240, 4:628, 5:1375, 6:2659, 7:4694, 8:7730, 9:12053, 10:17985, 11:25884}

# Independent check: Lagrange-quintic interpolation through k=2..10 of e(k),
# then test that the k^5 coeff is exactly 0 (=> quartic), predicting k=11.
# Then verify out-of-sample at k=11.
from fractions import Fraction

def interpolate_coeffs(xs, ys, deg):
    # solve Vandermonde over Fractions for coefficients low->high
    import sympy
    X = sympy.Matrix([[Fraction(x)**i for i in range(deg+1)] for x in xs])
    Y = sympy.Matrix([Fraction(y) for y in ys])
    sol = X.solve_least_squares(Y) if False else X.LUsolve(Y)
    return [Fraction(v) for v in sol]

xs = list(range(2, 11))          # 2..10
ys = [e[k] for k in xs]
deg = len(xs)-1                   # degree 8 through 9 points
coeffs = interpolate_coeffs(xs, ys, deg)
print("degree-8 interpolation through k=2..10 coeffs low->high:")
for i, c in enumerate(coeffs):
    print(f"  k^{i}: {c}")
print("k^5..k^8 coefficients:", coeffs[5:], "all zero?", all(c==0 for c in coeffs[5:]))

# Now predict k=11 out-of-sample from quartic fit through k=2..10
# fit quartic through k=2..6 (5 points) and test 7..11
xs35 = list(range(2, 7))
ys35 = [e[k] for k in xs35]
q = interpolate_coeffs(xs35, ys35, 4)
print("\nquartic through k=2..6:", q)
def ev(coeffs, k): return sum(F(c)*k**i for i, c in enumerate(coeffs))
ok = True
for k in range(1, 12):
    v = ev(q, k)
    m = (k==1)
    print(f"  e({k}): fit={v} meas={e[k]} match={v==e[k]}{'  <-- k=1 exception' if k==1 and v!=e[k] else ''}")
    if k >= 2 and v != e[k]:
        ok = False
print("out-of-sample (k=7..11) all match:", ok)

# Also: is the quartic exactly (9k^4+16k^3+12k^2+77k-60)/6? check coeffs
print("\nclaimed form coeffs (fracs):", [F(x)/6 for x in [ -60, 77, 12, 16, 9]])
print("fitted coeffs        :", [F(x) for x in q])

# check recurrence order-5 relation implied by quartic
# quartic => 5th finite difference = 0. verify.
d = [F(e[k]) for k in range(2, 12)]
for _ in range(5):
    d = [d[i+1]-d[i] for i in range(len(d)-1)]
print("\n5th finite difference of e over k=2..11:", d, "all zero?", all(x==0 for x in d))
