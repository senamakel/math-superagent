"""Validate membership machinery on KNOWN ideal elements before trusting the
n=5 nilpotency finding.  CA_5 is settled TRUE -> V(slice) = {0} -> a2,a3 MUST
be nilpotent mod the slice ideal.  If they are not, the GB or the reduce call
is wrong, not the math.
"""
from sympy import symbols, Poly, expand, resultant, groebner, QQ, binomial
from sympy.polys.polytools import reduced

x = symbols("x")


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


n = 5
a = symbols(f"a_1:{n+1}")
f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
sl = list(a[1:])
R = [expand(resultant(f, hasse(f, i), x).subs(a[0], 0)) for i in range(1, n)]
gb = groebner(R, *sl, order="grevlex")

def membres(expr):
    r = reduced(Poly(expand(expr), *sl, domain=QQ), gb.polys, sl)
    rem = r[0] if isinstance(r, tuple) else r
    # rem may be a Poly/list; get the actual remainder polynomial
    if isinstance(rem, (list, tuple)):
        rem = rem[0]
    return rem == 0, rem

# 1) each R_i must be in the ideal (reduce to 0)
print("Each R_i reduces to 0 (gb generates ideal containing all R_i):")
for i, ri in enumerate(R):
    ok, rem = membres(ri)
    print(f"   R_{i+1}: in ideal = {ok}")

# 2) a KNOWN combination R_1 + R_2 must be in the ideal
ok, rem = membres(R[0] + R[1])
print("R_1 + R_2 in ideal:", ok)

# 3) a2^5 (which is a leading monomial in gb) -- check if truly in ideal
ok, rem = membres(a[2] ** 5)
print("a2^5 in ideal:", ok, "| remainder zero:", rem == 0)

# 4) does gb really contain an element whose LM is a2^5? print the polys
print("\nFirst few GB elements (to inspect LM a2^5):")
for g in gb.polys[:6]:
    print("   ", g)
