# Correct srg multiplicity via standard formula, verify recorded f(r)/g(s).
# Eigenvalues: r = u, s = -(u+1), a = 2u+1, lam=1, mu=2.
# m_r = 1/2[(v-1) - (2k-(v-1))/a], m_s = 1/2[(v-1) + (2k-(v-1))/a]
import sympy as sp
u = sp.symbols('u')
us = [1,3,4,10,31]
k = sp.Poly(u**2+u+2,u).as_expr()
v = sp.expand(1+k+k*(k-2)/2)
a = 2*u+1
D = sp.expand(2*k - (v-1))
mr = sp.expand((sp.Rational(1,2))*((v-1) - D/a))
ms = sp.expand((sp.Rational(1,2))*((v-1) + D/a))
print("a = 2u+1     ", [sp.nsimplify(a.subs(u,uu)) for uu in us])
print("m_r (u)      ", [sp.nsimplify(mr.subs(u,uu)) for uu in us])
print("m_s (u)      ", [sp.nsimplify(ms.subs(u,uu)) for uu in us])
print("recorded f(r) [4, 54, 132, 3280, 250914]")
print("recorded g(s) [4, 44, 110, 2992, 243104]")
print("sum check m_r+m_s+1 = v: ", [sp.nsimplify((mr+ms+1).subs(u,uu)) for uu in us])
