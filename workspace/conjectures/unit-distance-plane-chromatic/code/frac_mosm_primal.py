#!/usr/bin/env python3
"""Solve the PRIMAL fractional-colouring LP over ALL independent sets of
Moser+Moser, get total weight (chi_f) and the fractional-colouring witness.
Primal: min sum x_S, A x >= 1 (each vertex covered to >= 1), x >= 0.
"""
import sys
sys.path.insert(0, "/workspace/code")
import scipy.optimize as opt
from lib.unitfield import moser_spindle_points, minkowski_sum, unit_graph
from fractions import Fraction

M=moser_spindle_points()
S=minkowski_sum(M,M)
edges,n=unit_graph(S)
pt_n=len(S)
adj=[set() for _ in range(pt_n)]
for a,b in edges: adj[a].add(b); adj[b].add(a)

all_indep=[]
for mask in range(1<<pt_n):
    # too big (2^26). Use incremental builder instead.
    pass

all_indep=[set()]
for v in range(pt_n):
    new=[]
    for Is in all_indep:
        if all((u not in adj[v]) for u in Is):
            new.append(Is | {v})
    all_indep += new
mI=len(all_indep)
print("independent sets:", mI)

c=[1.0]*mI
A=[]
for v in range(pt_n):
    A.append([1.0 if v in Is else 0.0 for Is in all_indep])
res=opt.linprog(c, A_ub=[[-r for r in row] for row in A], b_ub=[-1.0]*pt_n,
                bounds=[(0,None)]*mI, method='highs')
print("primal optimum (chi_f) =", round(res.fun,6))
xs=[0.0 if res.x[j]<1e-9 else res.x[j] for j in range(mI)]
sup=[(j,xs[j]) for j in range(mI) if xs[j]>0]
print("fractional-colouring support (independent set, weight):")
totalw=0.0
for j,x in sup:
    totalw+=x
    print("  ", sorted(all_indep[j]), Fraction(x).limit_denominator(1000))
print("total weight:", Fraction(totalw).limit_denominator(1000))
# verify coverage
cov=[0.0]*pt_n
for j,x in sup:
    for v in all_indep[j]: cov[v]+=x
print("coverage min:",min(cov),"max:",max(cov))
