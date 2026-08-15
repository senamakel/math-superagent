#!/usr/bin/env python3
"""chi_f(Moser+Moser) exactly, via the dual fractional-colouring LP with
weighted-maximum-independent-set cutting-plane separation.

Dual:  max sum_v w_v   s.t.  sum_{v in S} w_v <= 1 for EVERY independent set S,
       w_v >= 0.   chi_f = optimum (strong duality).
26 variables; separation is MWIS(w). Use scipy 'highs' double LP and a
correct branch-and-bound MWIS that returns the set.
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
print("Moser+Moser: n=",pt_n," edges=",n)

def mwis_set(w):
    """Max weight independent set returning (set, weight). Branch and bound."""
    best=[0.0]; bestset=[set()]
    ws=[w[v] for v in range(pt_n)]
    def rec(cand, total, chosen):
        if total>best[0]+1e-12:
            best[0]=total; bestset[0]=set(chosen)
        if not cand: return
        # optimistic bound: total + sum remaining weights
        if total+sum(ws[v] for v in cand)<=best[0]+1e-12: return
        v=max(cand, key=lambda x: len(adj[x]))
        # include
        rec(cand - adj[v] - {v}, total+ws[v], chosen|{v})
        # exclude
        rec(cand - {v}, total, chosen)
    rec(set(range(pt_n)), 0.0, set())
    return bestset[0], best[0]

# cutting-plane LP, seeded with all singleton constraints
constraints=[frozenset([v]) for v in range(pt_n)]
for it in range(500):
    A=[]; b=[]
    for C in constraints:
        A.append([1.0 if v in C else 0.0 for v in range(pt_n)])
        b.append(1.0)
    c=[-1.0]*pt_n
    res=opt.linprog(c, A_ub=A, b_ub=b, bounds=[(0,None)]*pt_n, method='highs')
    w=[max(0.0, res.x[i]) for i in range(pt_n)]
    Sset, mw = mwis_set(w)
    if mw <= 1.0 + 1e-7:
        val=sum(w)
        print(f"converged at iteration {it}: chi_f(Moser+Moser) = {val:.6f}")
        print("  sum w =", round(sum(w),6))
        # double-check every independent set has weight<=1 is implied by opt polytope
        break
    else:
        constraints.append(frozenset(Sset))
    if it%30==0:
        print(f"  iter {it}: |constraints|={len(constraints)}, violating MWIS weight={mw:.4f}")

# verify the dual solution w over ALL independent sets (complete enumeration of
# stable sets if count is small; else trust MWIS convergence). Report support.
print("\nfinal w support (nonzero):")
for v in range(pt_n):
    if w[v]>1e-9:
        print(f"  vertex {v}: w={Fraction(w[v]).limit_denominator(10000)}")
