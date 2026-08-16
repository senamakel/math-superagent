"""Symbolically prove the tight-coclique family identities.

For the family srg(v,k,1,2), k = u^2+u+2, v = 1+k^2/2, s = -(u+1),
Hoffman-bound size alpha = (u*k+2)/2 (report 3 closed form).  A coclique
meeting the bound forces d_C := alpha*(k-s)/v = -s = u+1 and the outside-
restricted blocks form a 2-(alpha, d_C, 2) design with replication
r = 2*(alpha-1)/(d_C-1) = k.

Aim: derive d_C == u+1 and r == k symbolically (no reliance on the 5
member-wise values).
"""
import sympy as sp

u = sp.symbols('u', integer=True)
k = u**2 + u + 2
v = 1 + k**2/2
alpha = (u*k + 2)/2
s = -(u+1)

dC = sp.simplify(alpha*(k - s)/v)
print("d_C symbolic:", sp.factor(dC))
print("d_C == u+1 ?", sp.simplify(dC - (u+1)) == 0)

r = sp.simplify(2*(alpha - 1)/(dC - 1))
print("r symbolic  :", sp.factor(r))
print("r == k      ?", sp.simplify(r - k) == 0)

# block count b = v - alpha
b = sp.simplify(v - alpha)
print("b symbolic  :", sp.factor(b))
