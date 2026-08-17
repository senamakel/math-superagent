"""Is the n=5 slice quotient 0-dim but my cap (40) too small?

A 0-dim quotient of QQ[a2,a3,a4,a5]/I has every variable nilpotent.  The
grevlex LMs just now showed NO pure a3 power up to the 27-polynomial gb --
but a Groebner basis's leading monomials DO capture nilpotency: if a3^M in I
then LM of some I-element divides a3^M, i.e. a pure a3^e LM with e<=M exists.
The gb has no such LM, so a3 is NOT nilpotent mod I.

So the n=5 traceless slice is genuinely NOT 0-dimensional.  That is a real,
striking degeneracy of the a1=0 slice at n=5 (NOT a counterexample to CA_5,
which is about the FULL scheme with a1 free).  Let me confirm by restricting
to a4=a5=0 and eliminating to see the (a2,a3) locus.
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
sl = [a2, a3, a4, a5]
R = [expand(resultant(f, hasse(f, i), x).subs(a1, 0)) for i in range(1, n)]

# restrict to a4=a5=0: the (a2,a3) "plane" inside the slice
R_rest = [r.subs({a4: 0, a5: 0}) for r in R]
gbr = groebner(R_rest, a2, a3, order="grevlex")
print("GB of (R_1..R_4)|_{a4=a5=0} in (a2,a3):")
for g in gbr.polys:
    print("   ", g.as_expr() if hasattr(g, 'as_expr') else g)
