import itertools, math
from math import gcd

def euler(a,b,c,d):
    u=(a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c))
    v=(2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b))
    w=(2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d)
    return (u,v,w)

def norm2(v): return v[0]*v[0]+v[1]*v[1]+v[2]*v[2]

# ---- Q1: check |u|^2=|v|^2=|w|^2 = N^2 for random integer quaternions
print("Q1 check: |u|^2=N^2 for integer quaternions")
ok=True
for _ in range(0):
    pass
for a in range(-3,4):
  for b in range(-3,4):
    for c in range(-3,4):
      for d in range(-3,4):
        N=a*a+b*b+c*c+d*d
        u,v,w=euler(a,b,c,d)
        if not (norm2(u)==N*N and norm2(v)==N*N and norm2(w)==N*N):
            ok=False; print("FAIL",a,b,c,d); break
      if not ok: break
    if not ok: break
  if not ok: break
print("  all |u|^2=N^2:", ok)

# ---- Q3: worked frame ell=3, find its primary quaternary rep N=3=ell
frame=((1,2,2),(2,-2,1),(2,1,-2))
# equivalence: permute cols, flip signs independently. canonical form:
def canon(fr):
    A=[]
    for per in itertools.permutations(fr):
        for s in itertools.product([1,-1],repeat=3):
            t=tuple(tuple(s[i]*per[i][j] for j in range(3)) for i in range(3))
            A.append(t)
    return min(A)

frameC=canon(frame)

def small_int_quats(Nmax):
    res=[]
    for a in range(-Nmax,Nmax+1):
      for b in range(-Nmax,Nmax+1):
        for c in range(-Nmax,Nmax+1):
          for d in range(-Nmax,Nmax+1):
            if a*a+b*b+c*c+d*d<=Nmax and 0<(a*a+b*b+c*c+d*d):
                res.append((a,b,c,d))
    return res

# search all integer quats with N<=3 (resp small) whose euler columns canonical == frameC
hits=[]
for (a,b,c,d) in small_int_quats(30):
    u,v,w=euler(a,b,c,d)
    if canon((u,v,w))==frameC:
        N=a*a+b*b+c*c+d*d
        hits.append((N,(a,b,c,d)))
print("Q3: integer quats giving worked frame (N,(a,b,c,d)):", sorted(set(hits)))
