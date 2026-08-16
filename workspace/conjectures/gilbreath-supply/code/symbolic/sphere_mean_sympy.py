"""Independent sympy cross-check of the closed form, and the n=8,w=3 anchor.

Task claimed n=8,w=3 'should give 6.846'. We show the true exact value is
25/7 = 3.5714 (mean 0.4464). Note also that 6.846 is IMPOSSIBLE at n=8:
nu2 counts only the 6 cells d in [2,7], so nu2 <= 6 and E[nu2] <= 6 always.
"""
import sympy as sp

def kraw_sym(w, m, n):
    j = sp.symbols('j', integer=True)
    return sp.summation((-1)**j * sp.binomial(m, j) * sp.binomial(n-m, w-j),
                        (j, 0, w))

def popcount(x): return bin(x).count("1")

def E_nu2(n, w):
    C = sp.binomial(n, w)
    total = sp.Integer(0)
    for d in range(2, n):
        md = 2 ** popcount(d)
        P = sp.Rational(1, 2) * (1 - kraw_sym(w, md, n) / C)
        total += P
    return sp.simplify(total)

for (n, w) in [(4, 1), (8, 3)]:
    E = E_nu2(n, w)
    print(f"n={n} w={w}: E[nu2] = {E}  = {float(E):.6f}   nu2/n={float(E)/n:.6f}")
    print(f"   max possible = {n-2} (cells d in [2,{n-1}])")

print()
print("n=8 full w sweep (to bound E, and check the 0.4*8=3.2 crossing):")
for w in range(0, 9):
    E = E_nu2(8, w)
    print(f"  w={w}: E={E} = {float(E):.4f}  nu2/n={float(E)/8:.4f}  crosses0.4? {float(E)>=3.2}")
