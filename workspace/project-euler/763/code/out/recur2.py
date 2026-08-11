import sympy as sp
import math

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263, 514419, 1749267, 5949063]
N = len(D)
n = sp.symbols('n')

# ---------- Verify the order-7 recurrence found, in integer form ----------
# Order-7 form: sum_j c[j] D[i+j] = D[i+7]  with c = (0, 21, -31/3, -10, -17/3, 4, 3)
c = [sp.Rational(0), sp.Rational(21), sp.Rational(-31,3), sp.Rational(-10), sp.Rational(-17,3), sp.Rational(4), sp.Rational(3)]
print("Order-7 recurrence D[n+7] =", " + ".join(f"({c[j]})*D[n+{j}]" for j in range(7)))
# integer form: multiply by 3
print("x3 integer form: 3*D[n+7] = 63*D[n+1] - 31*D[n+2] - 30*D[n+3] - 17*D[n+4] + 12*D[n+5] + 9*D[n+6]")

# verify all 8 relations
ok = True
for i in range(N-7):
    lhs = D[i+7]
    rhs = sum(c[j]*D[i+j] for j in range(7))
    if sp.simplify(sp.Rational(lhs) - rhs) != 0:
        ok = False
        print(f"FAIL at i={i}")
print("Order-7 recurrence verified over all", N-7, "relations:", ok)

# ---------- Characteristic polynomial & roots ----------
x = sp.symbols('x')
# char poly: x^7 - c6 x^6 - c5 x^5 - c4 x^4 - c3 x^3 - c2 x^2 - c1 x - c0
cp = x**7 - c[6]*x**6 - c[5]*x**5 - c[4]*x**4 - c[3]*x**3 - c[2]*x**2 - c[1]*x - c[0]
print("\nCharacteristic polynomial:", sp.factor(cp))
roots = sp.nroots(cp, n=15, maxsteps=200)
print("Roots (numeric):")
for r in roots:
    print("  ", r)
realpos = [abs(r) for r in roots]
realpos.sort(reverse=True)
dominant = [r for r in roots if abs(r)==max(abs(x) for x in roots)]
print("Dominant root magnitude:", max(abs(x) for x in roots))
print("All magnitudes sorted desc:", sorted([abs(x) for x in roots], reverse=True))

# ---------- Asymptotic regression D(N) ~ C r^N N^alpha ----------
# Fit: log D(N) = log C + N log r + alpha log N over later terms
import numpy as np
from numpy.polynomial import polynomial as P
# Use terms i0..N-1
Y = np.array([math.log(D[k]) for k in range(N)])
for i0 in [8, 9, 10, 11]:
    kk = np.arange(i0, N)
    Xn = kk.astype(float)
    yy = Y[i0:]
    # model yy = a + b*N + alpha*log n
    A = np.column_stack([np.ones(len(kk)), Xn, np.log(Xn)])
    coef, res, rank, sv = np.linalg.lstsq(A, yy, rcond=None)
    a, b, alpha = coef
    r_val = math.exp(b)
    C_val = math.exp(a)
    print(f"\nfit from n={i0}: r={r_val:.8f}, alpha={alpha:.6f}, C={C_val:.6f}")

# ratios limit estimate
print("\nlast few ratios:")
for i in range(N-5, N):
    print(f"  D[{i}]/D[{i-1}] = {D[i]/D[i-1]:.8f}")
