#!/usr/bin/env python3
"""Scholar's own fresh verification of the run's load-bearing computational
claims, run independently of prior cached logs. Exact arithmetic only.

1. Calibration: Moser spindle 7-vertex graph -> 11 exact unit edges, chi=4
   (4-colourable, not 3-colourable).
2. Diamond base case: tips at sqdist 3 are forced-equal under 3 colours.
3. Minkowski-sum distance identity on a fresh exact sample.
4. Eisenstein lattice unit vectors.
"""
from fracs import Fraction
import itertools

# --- exact field Q(sqrt3, sqrt11), basis {1, s3, s11, s33} ---
TAB = {
 (0,0):(Fraction(1),0),(0,1):(Fraction(1),1),(0,2):(Fraction(1),2),(0,3):(Fraction(1),3),
 (1,0):(Fraction(1),1),(1,1):(Fraction(3),0),(1,2):(Fraction(1),3),(1,3):(Fraction(3),2),
 (2,0):(Fraction(1),2),(2,1):(Fraction(1),3),(2,2):(Fraction(11),0),(2,3):(Fraction(11),1),
 (3,0):(Fraction(1),3),(3,1):(Fraction(3),2),(3,2):(Fraction(11),1),(3,3):(Fraction(33),0),
}
def fmul(x,y):
    out=[Fraction(0)]*4
    for i in range(4):
        if x[i]==0: continue
        for j in range(4):
            if y[j]==0: continue
            c,b=TAB[(i,j)]
            out[b]+=x[i]*y[j]*c
    return tuple(out)
def fadd(x,y): return tuple(x[i]+y[i] for i in range(4))
def fsub(x,y): return tuple(x[i]-y[i] for i in range(4))
ONE=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))
def sqdist(p,q):
    dx=fsub(p[0],q[0]); dy=fsub(p[1],q[1])
    return fadd(fmul(dx,dx),fmul(dy,dy))
def pt(x,y):
    def fz(v):
        if isinstance(v,tuple): return v
        return (Fraction(v),Fraction(0),Fraction(0),Fraction(0))
    return (fz(x),fz(y))

# --- Moser spindle, exact coordinates ---
O=pt(0,0)
a1=pt(1,0)
a2=((Fraction(1,2),0,0,0),(0,Fraction(1,2),0,0))
a3=((Fraction(3,2),0,0,0),(0,Fraction(1,2),0,0))
b1=((Fraction(5,6),0,0,0),(0,0,Fraction(1,6),0))
b2=((Fraction(5,12),0,Fraction(-1,12),0),(0,Fraction(5,12),Fraction(1,12),0))
b3=(fadd(b1[0],b2[0]),fadd(b1[1],b2[1]))
pts=[O,a1,a2,a3,b1,b2,b3]
edges=[(i,j) for i in range(7) for j in range(i+1,7) if sqdist(pts[i],pts[j])==ONE]
print("Moser edges:",len(edges),edges)

def colourable(k):
    for c in itertools.product(range(k),repeat=7):
        if all(c[u]!=c[v] for u,v in edges): return True,c
    return False,None
ok4,c4=colourable(4); ok3,_=colourable(3)
print("k=4 colourable",ok4,c4,"| k=3 colourable",ok3)
assert ok4 and not ok3
print("CALIBRATION chi=4 CONFIRMED")

# diamond: tips forced equal under 3 colours
A=pt(0,0); B=pt(1,0)
half=(Fraction(0),Fraction(1,2),Fraction(0),Fraction(0))
C=pt((Fraction(1,2),0,0,0),half); D=pt((Fraction(1,2),0,0,0),(Fraction(0),Fraction(-1,2),0,0))
dpts=[A,B,C,D]
dab=[(i,j) for i in range(4) for j in range(i+1,4) if sqdist(dpts[i],dpts[j])==ONE]
t2=sqdist(dpts[2],dpts[3])
print("diamond edges",dab,"tips sqdist",t2[0])
def dcol(k):
    for c in itertools.product(range(k),repeat=4):
        if all(c[u]!=c[v] for u,v in dab): return c
    return None
print("diamond 3-colourable (no tips edge)", dcol(3) is not None)
tipedge=[(u,v) for u,v in dab]+[(2,3)]
def dcol2(k):
    for c in itertools.product(range(k),repeat=4):
        if all(c[u]!=c[v] for u,v in tipedge): return c
    return None
print("diamond 3-colourable WITH tips edge (False=forced equal)", dcol2(3) is not None)
assert dcol(3) is not None and dcol2(3) is None
print("DIAMOND FORCED-PAIR CONFIRMED (tips sqdist 3, forced equal under 3 cols)")

# Minkowski identity fresh sample
import random; random.seed(11)
ZERO=((0,0,0,0),(0,0,0,0))
for _ in range(3000):
    def rr():
        return (Fraction(random.randint(-6,6)),Fraction(random.randint(-6,6)))
    a1p=(rr(),rr()); a2p=(rr(),rr()); b1p=(rr(),rr()); b2p=(rr(),rr())
    s1=tuple(fadd(a1p[i],b1p[i]) for i in range(2)); s2=tuple(fadd(a2p[i],b2p[i]) for i in range(2))
    va=tuple(fsub(a1p[i],a2p[i]) for i in range(2)); vb=tuple(fsub(b1p[i],b2p[i]) for i in range(2))
    left=sqdist(s1,s2); right=sqdist(tuple(fadd(va[i],vb[i]) for i in range(2)),ZERO)
    assert left==right
print("MINKOWSKI IDENTITY verified on 3000 exact random pairs")

# Eisenstein units
six={(-1,0),(1,0),(0,-1),(0,1),(1,-1),(-1,1)}
for x in range(-15,16):
    for y in range(-15,16):
        n=x*x-x*y+y*y
        assert (n==1)==((x,y) in six)
print("EISENSTEIN units verified over [-15,15]^2")
print("ALL FRESH VERIFICATIONS PASSED")
