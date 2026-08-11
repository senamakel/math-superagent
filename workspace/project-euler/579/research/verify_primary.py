import itertools, math
from math import gcd
from functools import cmp_to_key

def euler(a,b,c,d):
    u=(a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c))
    v=(2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b))
    w=(2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d)
    return (u,v,w)

def norm2(v): return v[0]*v[0]+v[1]*v[1]+v[2]*v[2]

# Q1: |u|^2=|v|^2=|w|^2 = N^2 ; edge length = N
print("Q1:", end=" ")
bad=0
for a in range(-2,3):
  for b in range(-2,3):
    for c in range(-2,3):
      for d in range(-2,3):
        if a==b==c==d==0: continue
        N=a*a+b*b+c*c+d*d
        u,v,w=euler(a,b,c,d)
        if not (norm2(u)==N*N and norm2(v)==N*N and norm2(w)==N*N):
            bad+=1
print("|u|^2=|v|^2=|w|^2=N^2 for all tested, fails:",bad)

def canon_frame(fr):
    # frame = set of 3 vectors, each up to sign. Canonical form.
    # each vector -> normalized by sign: lexicographic positive first nonzero
    def sign_norm(vec):
        for x in vec:
            if x<0: return tuple(-y for y in vec)
            if x>0: return vec
        return vec
    vs=[sign_norm(v) for v in fr]
    vs.sort()
    return tuple(vs)

def is_primary(a,b,c,d):
    # primary: a (real part) has parity different from b,c,d  AND a+b+c+d ≡1 mod4
    par_diff = ((a-b)%2==1 and (a-c)%2==1 and (a-d)%2==1)
    return par_diff and ((a+b+c+d)%4==1)

# Q3: for each odd N, compare:
#  (i) all primitive frames from ALL integer quats with N(alpha) odd, gcd=1 (dedup)
#  (ii) frames from PRIMARY primitive integer quats only (dedup)
def all_int_quats(Nmax):
    res=[]
    for a in range(-Nmax,Nmax+1):
      for b in range(-Nmax,Nmax+1):
        for c in range(-Nmax,Nmax+1):
          for d in range(-Nmax,Nmax+1):
            nn=a*a+b*b+c*c+d*d
            if 1<=nn<=Nmax and nn%2==1:
                res.append((a,b,c,d,nn))
    return res

qs=all_int_quats(30)
from collections import defaultdict
frames_all=defaultdict(set)     # N -> canonical frames (ALL primitive, no N constraint counting)
frames_primary=defaultdict(set)
count_all=defaultdict(int)
count_primary=defaultdict(int)
N_of_frame_primary={}
for (a,b,c,d,N) in qs:
    if gcd(gcd(gcd(a,b),c),d)!=1: continue
    fr=canon_frame(euler(a,b,c,d))
    frames_all[N].add(fr)
    count_all[N]+=1
    if is_primary(a,b,c,d):
        frames_primary[N].add(fr)
        count_primary[N]+=1

print("\nN | #primitive quats(gcd1) | #primary prim quats | #distinct frames(all)  | #distinct frames(primary) | equal?")
for N in sorted(set([q[4] for q in qs])):
    if N>30: continue
    A=frames_all.get(N,set()); B=frames_primary.get(N,set())
    print(f"{N:3d} | {count_all.get(N,0):22d} | {count_primary.get(N,0):20d} | "
          f"{len(A):22d} | {len(B):24d} | {A==B}")

# Also: does N equal edge length of the frame?
print("\nCheck N == edge length for a primary frame:")
def edgelen(fr):
    from math import isqrt
    u=fr[0]
    return isqrt(u[0]*u[0]+u[1]*u[1]+u[2]*u[2])
ok=True
for N in sorted(frames_primary):
    for fr in frames_primary[N]:
        if edgelen(fr)!=N:
            print("  MISMATCH N=",N,"frame",fr,"edgelen",edgelen(fr)); ok=False
print("  N==edgelen for all primary frames:",ok)
