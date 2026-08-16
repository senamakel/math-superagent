"""Self-consistency of the predicted C3 triangle-graph spectrum at the five
family members: a valid regular graph spectrum must have integer trace 0
and sum of squares = 2*edges = n*d.  Check the C3 spectrum prediction
rt^m_r, st^m_s, (-3)^(nT-v), d^1 is a valid spectrum candidate.

d = 3(k/2 - 1), nT = vk/6, nT vertices.
Exact integer arithmetic.
"""
import math
def fam(u):
    k=u*u+u+2; v=1+k*k//2; return k,v
for u in (1,3,4,10,31):
    k,v = fam(u)
    nT = v*k//6
    a = 2*u+1
    top = 2*k-(v-1)
    m_r = ((v-1) - top//a)//2
    m_s = ((v-1) + top//a)//2
    d = 3*(k//2 - 1)
    rt = k//2 + u - 3
    st = k//2 -(u+1) - 3
    nneg = nT - v
    # spectrum: d (mult1) + rt*m_r + st*m_s + (-3)*nneg
    # total multiplicity must equal nT
    tot = 1 + m_r + m_s + nneg
    trace = d + rt*m_r + st*m_s + (-3)*nneg
    sq = d*d + rt*rt*m_r + st*st*m_s + 9*nneg
    twodeg = nT*d
    print(f"u={u:>2} nT={nT:>6} | vertsum={tot:>7} (==nT {tot==nT}) | "
          f"trace={trace:>6} (==0 {trace==0}) | sq={sq} degsum={twodeg} eq={sq==twodeg}")
