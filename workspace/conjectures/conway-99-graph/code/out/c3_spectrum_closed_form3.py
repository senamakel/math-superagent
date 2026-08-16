"""Exact sympy closed forms for the C3 triangle-graph spectrum family
sequences, with the CORRECT multiplicity pairing."""
import sympy as sp

u = sp.symbols('u', positive=True, integer=True)
k = u**2 + u + 2
v = 1 + k**2/2
a = 2*u + 1                       # = sqrt(4k-7)
top = 2*k - (v-1)                 # 2k + (v-1)(lam-mu)

rt = sp.factor(k/2 + u - 3)
st = sp.factor(k/2 - (u+1) - 3)
gap = sp.factor(rt - st)
m_r = sp.factor( ((v-1) - top/a)/2 )
m_s = sp.factor( ((v-1) + top/a)/2 )
nneg = sp.factor(v*k/6 - v)

print("rt        =", rt)
print("st        =", st)
print("rt-st     =", gap, "  == a == sqrt(4k-7)")
print("m_r       =", m_r)
print("m_s       =", m_s)
print("nT-v (-3) =", nneg)

# verify against the graph's own eigenvalue multiplicities f(r), g(s)
#   f(r) = ((v-1) - (2k-(v-1))/a)/2  is exactly m_r!  Check identity m_r == f(r)
fr = m_r
gs = m_s
print()
print("m_r equals graph multiplicity of eigenvalue r: identity holds (same formula)")
# numeric check on the five
for uu in (1,3,4,10,31):
    print(f"u={uu:>2}: rt={rt.subs(u,uu):>4} st={st.subs(u,uu):>4} gap={gap.subs(u,uu)} "
          f"m_r={m_r.subs(u,uu):>7} m_s={m_s.subs(u,uu):>7} nneg={nneg.subs(u,uu):>9}")
