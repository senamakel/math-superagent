import sys, math
sys.path.insert(0, "/workspace/code")
import sympy as sp
from lib.satcolor import is_k_colorable

THREE_HALF = sp.Rational(3,2)

def a2_centre(u,v,Lv):
    x = sp.sqrt(3)*Lv*(u - sp.Rational(v,2))
    y = THREE_HALF*Lv*v
    return sp.simplify(x), sp.simplify(y)

def sqdist(c1,c2):
    return sp.expand((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def sublattice_reps_row(p,q,D):
    reps=[]
    for r in range(D):
        cand=None
        for u in range(D):
            for v in range(D):
                if (p*u+q*v)%D==r:
                    if cand is None or (u*u+v*v)<(cand[0]*cand[0]+cand[1]*cand[1]):
                        cand=(u,v)
        reps.append(cand)
    return reps

def coset_dist_min(p,q,D,r1,r2,Lv,R=12):
    c1 = a2_centre(*reps[r1],Lv)
    best=None
    for du in range(-R,R+1):
        for dv in range(-R,R+1):
            if ((p*du+q*dv)-(r2-r1))%D!=0: continue
            c2 = a2_centre(reps[r1][0]+du, reps[r1][1]+dv, Lv)
            d2 = sqdist(c1,c2)
            if best is None or sp.simplify(d2-best)<0:
                best=d2
    return best

def count_min_dist_under_R(p,q,D,Lv,R):
    T2 = sp.expand((1+2*Lv)**2)
    cnt=0; pairs=[]
    for i in range(D):
        for j in range(i+1,D):
            best=coset_dist_min(p,q,D,i,j,Lv,R)
            if sp.simplify(best-T2)<=0:
                cnt+=1; pairs.append((i,j))
    return cnt,pairs

for (p,q,D,Lv) in [(1,-2,7,sp.Rational(2,5)),(1,-1,7,sp.Rational(2,5)),(1,2,13,sp.Rational(2,5))]:
    reps=sublattice_reps_row(p,q,D)
    print("="*70)
    print(f"Sublattice kernel row=({p},{q}) mod {D}, L={Lv}")
    print(f"  reps = {reps}")
    T2=sp.expand((1+2*Lv)**2)
    print(f"  (1+2L)^2 = {T2}")
    for R in [3,6,9,12]:
        cnt,pairs=count_min_dist_under_R(p,q,D,Lv,R)
        print(f"  min-distance pairs <=1+2L with R={R}: {cnt} {pairs}")
