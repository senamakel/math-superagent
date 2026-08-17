"""Debug the n=5 slice ideal.  CA_5 settled true => V(slice)={0}.  But GB shows
a4^10, a5^1 in I (so a4=a5=0 on V), while a2,a3 appear free -> contradiction
with CA_5.  Suspect: the resultant construction.  Restrict to a4=a5=0 and see
what V looks like in (a2,a3).  Also sanity-check one resultant by evaluating.
"""
from sympy import symbols, Poly, expand, resultant, groebner, QQ, binomial

x = symbols("x")
a1, a2, a3, a4, a5 = symbols("a_1 a_2 a_3 a_4 a_5")
a = [a1, a2, a3, a4, a5]


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


n = 5
f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))

# ---- test that f really is what we think ----
print("f =", expand(f))

# ---- check the sharing condition directly at a hand point: f2 = x^5 - x^2?
#       a monic degree-5; check if it shares root with derivatives ----


def shares(f, g):
    return sp_resultant(f, g, x) if False else None

# Print Hasse derivatives of a generic f
for i in (1, 2, 3, 4):
    print(f"H_{i}(f) =", expand(hasse(f, i)))
