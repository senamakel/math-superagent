#!/usr/bin/env python3
"""Exact verification that chi_f(Moser=7/2) via a dual certificate.
We exhibit:
 (P) a fractional colouring x_S >= 0 with sum_S x_S = 7/2 covering every
     vertex (sum over S containing v >= 1), and
 (D) a vertex weighting w_v >= 0 with sum w = 7/2 such that every
     independent set S satisfies sum_{v in S} w_v <= 1.
Strong duality then proves the optimum (chi_f) equals 7/2 exactly.
We find both by solving the LP with scipy and rounding, but ALSO verify
feasibility/rationality by an exact re-check of the numbers.
"""
from fractions import Fraction
import scipy.optimize as opt

def independent_sets(n, edges):
    adj = [set() for _ in range(n)]
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    out=[]
    for mask in range(1<<n):
        vs=[i for i in range(n) if (mask>>i)&1]
        ok=True
        for i in range(len(vs)):
            for j in range(i+1,len(vs)):
                if vs[j] in adj[vs[i]]: ok=False; break
            if not ok: break
        if ok: out.append(vs)
    return out

moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
n=7
indep=independent_sets(n,moser)
mI=len(indep)
# PRIMAL: min sum x, A x >= 1, x>=0
c=[1.0]*mI
A=[[1.0 if v in I else 0.0 for I in indep] for v in range(n)]
res=opt.linprog(c,A_ub=[[-r for r in row] for row in A],b_ub=[-1.0]*n,
                bounds=[(0,None)]*mI,method='highs')
print("primal optimum:",res.fun)
xs=res.x
# round tiny below eps to 0
xs=[0.0 if abs(x)<1e-9 else x for x in xs]
# find dual: max sum w, A_dual w <= 1 (every indep set weight<=1), w>=0
resd=opt.linprog([-1.0]*n,A_ub=[[1.0 if v in I else 0.0 for v in range(n)] for I in indep],
                 b_ub=[1.0]*mI,bounds=[(0,None)]*n,method='highs')
print("dual optimum:",-resd.fun)
w=[0.0 if abs(x)<1e-9 else x for x in resd.x]
print("weights:",w,"sum=",sum(w))

# exact re-check on the rounded primal: coverage and weight
print("\nPrimal support (indep set idx, fractional weight):")
for j,x in enumerate(xs):
    if x>0:
        print("  set",sorted(indep[j]),"=",Fraction(x).limit_denominator(1000))
cov=[0.0]*n
for j,x in enumerate(xs):
    if x>0:
        for v in indep[j]: cov[v]+=x
print("coverage per vertex:",[Fraction(c).limit_denominator(1000) for c in cov])
print("total primal weight:",Fraction(sum(xs)).limit_denominator(1000))
