"""Correct C3 triangle-graph spectrum closed forms over the srg(v,k,1,2)
family, with the RIGHT multiplicity pairing (checked against the actual
BvLS C3 spectrum: rt=12 carries 132, st=3 carries 110).

k = u^2+u+2, v = 1+k^2/2, eigenvalues r=u, s=-(u+1).
C3 eigenvalues (Phillips 4.3):  rt = k/2+r-3, carries m_r (mult of graph eig r);
                                st = k/2+s-3, carries m_s (mult of graph eig s);
                                -3 carries nT-v.
SRG multiplicity formulas (exact):
  m_r = (1/2)[(v-1) - (2k-(v-1))/(r-s)]
  m_s = (1/2)[(v-1) + (2k-(v-1))/(r-s)],  r-s = 2u+1
Exact integer arithmetic.
"""
import math

def fam(u):
    k = u*u+u+2; v = 1 + k*k//2; return k, v

rows = []
for u in (1,3,4,10,31):
    k,v = fam(u)
    nT = v*k//6
    a = 2*u+1
    top = 2*k - (v-1)          # 2k + (v-1)(lam-mu), lam-mu=-1
    m_r = ( (v-1) - top//a )//2
    m_s = ( (v-1) + top//a )//2
    rt = k//2 + u - 3
    st = k//2 - (u+1) - 3
    nneg = nT - v
    rows.append((u,k,v,rt,m_r,st,m_s,nneg))
    print(f"u={u:>2} k={k:>3} v={v:>6}  C3: rt={rt:>4} x {m_r:>6}   st={st:>4} x {m_s:>6}   -3 x {nneg:>8}   gap={rt-st}")

print()
print("rt family:", [r[3] for r in rows])
print("m_r family:", [r[4] for r in rows])
print("st family:", [r[5] for r in rows])
print("m_s family:", [r[6] for r in rows])
print("-3 mult (nT-v) family:", [r[7] for r in rows])
