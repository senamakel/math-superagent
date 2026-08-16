"""Clean numeric table + simplified multiplicity closed forms for C3 spectrum."""
import sympy as sp
u = sp.symbols('u', positive=True, integer=True)
k = u**2 + u + 2
v = 1 + k**2/2     # exact: v-1 = k^2/2 (k even)
a = 2*u + 1
top = 2*k - (v - 1)              # 2k + (v-1)(lam-mu)
rt = sp.factor(k/2 + u - 3)
st = sp.factor(k/2 - (u+1) - 3)
gap = sp.factor(rt - st)
m_r = sp.factor(((v-1) - top/a)/2)
m_s = sp.factor(((v-1) + top/a)/2)
nneg = sp.factor(v*k/6 - v)

print("rt  =", rt)
print("st  =", st)
print("gap = rt-st =", gap, "= a = sqrt(4k-7) = 2u+1")
print("m_r =", sp.factor(m_r))
print("m_s =", sp.factor(m_s))
print("nneg=", nneg)
print()
print("   u |  rt   st   gap  |   m_r      m_s   |  nT-v(-3)")
for uu in (1,3,4,10,31):
    rt_v = int(rt.subs(u,uu)); st_v = int(st.subs(u,uu))
    mr = int(m_r.subs(u,uu)); ms = int(m_s.subs(u,uu))
    nn = int(nneg.subs(u,uu))
    print(f"  {uu:>2} | {rt_v:>4} {st_v:>4} {int(gap.subs(u,uu)):>4} | {mr:>8} {ms:>8} | {nn:>9}")
