"""Exact (sympy) derivation of the C3 triangle-graph spectrum closed forms
over the srg(v,k,1,2) family, k=u^2+u+2, v=1+k^2/2.

C3 eigenvalues (Phillips eq 4.3): rt = k/2 + r - 3, st = k/2 + s - 3,
r=u, s=-(u+1); -3 multiplicity nT - v = vk/6 - v.
Gap: rt - st should be (2u+1) = sqrt(4k-7) = a exactly.
"""
import sympy as sp

u = sp.symbols('u', positive=True, integer=True)
k = u**2 + u + 2
v = 1 + k**2/2
r = u
s = -(u+1)

rt = sp.simplify(k/2 + r - 3)
st = sp.simplify(k/2 + s - 3)
gap = sp.simplify(rt - st)
nminus3 = sp.simplify(v*k/6 - v)

print("rt =", sp.factor(rt))
print("st =", sp.factor(st))
print("rt - st =", sp.factor(gap), "   (should be 2u+1)")

st2 = sp.simplify(nminus3)
print("nT - v (C3 -3 multiplicity) =", sp.factor(st2))

# verify at the five feasible u
for uu in (1,3,4,10,31):
    print(f"u={uu}: rt={rt.subs(u,uu)} st={st.subs(u,uu)} gap={gap.subs(u,uu)} "
          f"nminus3={nminus3.subs(u,uu)}")
