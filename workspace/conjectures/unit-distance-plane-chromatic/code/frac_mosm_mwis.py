#!/usr/bin/env python3
"""chi_f(Moser+Moser) via the dual LP with cutting planes.
Dual of fractional colouring:  max sum_v w_v   s.t.  sum_{v in S} w_v <= 1
for EVERY independent set S, w >= 0.   chi_f = this optimum (strong duality).
Only 26 variables (vertices); we separate violated stable sets by a branch-and-
bound maximum-weight-independent-set (MWIS) oracle. Exact-ish (scipy double,
but rounded and cross-checked) — good enough to see whether chi_f moved from
the Moser's 7/2 = 3.5 toward 4.
"""
import sys
sys.path.insert(0, "/workspace/code")
import scipy.optimize as opt
from lib.unitfield import moser_spindle_points, minkowski_sum, unit_graph

def adj_from_edges(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    return adj

def mwis(adj, w, best=0.0):
    """Maximum weight independent set via branch & bound. Returns max weight of
    a stable set (not the set). w: vertex weights (list)."""
    n=len(adj)
    order=sorted(range(n), key=lambda v: -w[v])  # heuristic: heavy first
    # recursive branch on a remaining vertex
    import sys as _sys
    _sys.setrecursionlimit(100000)
    state=[0.0]
    def rec(cand, total):
        # candidate vertices still allowed (set), total weight of chosen so far
        if not cand:
            state[0]=max(state[0], total); return
        # upper bound: total + sum of weights of all remaining (optimistic)
        if total + sum(w[v] for v in cand) <= state[0]:
            return
        v=next(iter(cand))
        # branch 1: include v
        nb=adj[v]
        rec(cand - {v} - nb, total + w[v])
        # branch 2: exclude v
        rec(cand - {v}, total)
    rec(set(range(n)), 0.0)
    return state[0]

# Build Moser+Moser points and unit graph
M=moser_spindle_points()
S=minkowski_sum(M,M)
n,edges=unit_graph(S)
print("Moser+Moser: n =",n," edges =",len(edges))
adj=adj_from_edges(n,edges)

# Cutting-plane dual: maximize sum w s.t. MWIS(w) <= 1, w>=0
# Solve LP over generated stable-set constraints iteratively.
constraints=[]  # list of (set_tuple) whose weight must be <=1
# warm start: add all singleton and all known small stable sets? start empty
for it in range(200):
    A=[]; b=[]
    for S in constraints:
        row=[1.0 if v in S else 0.0 for v in range(n)]
        A.append(row); b.append(1.0)
    if not A:
        # no constraints yet: just need a feasible start; use w=0 trivial, but
        # LP needs at least something. Give an artificial large box first pass.
        c=[-1.0]*n
        res=opt.linprog(c,A_ub=A,b_ub=b,bounds=[(0,None)]*n,method='highs')
    else:
        c=[-1.0]*n
        res=opt.linprog(c,A_ub=A,b_ub=b,bounds=[(0,None)]*n,method='highs')
    w=[max(0.0,res.x[i]) for i in range(n)]
    mw=mwis(adj,w)
    if mw <= 1.0 + 1e-9:
        val=sum(w)
        print("converged at iteration",it," chi_f(Moser+Moser) ~",round(val,6))
        # reconstruct supporting stable set of max weight for reporting
        print("sum w =",round(sum(w),6), "MWIS check =",round(mw,6))
        break
    # find the heavy stable set (re-run mwis to return the actual set)
    # we just re-seed constraints with a violated set; to keep simple, add the
    # full vertex support as constraints
    else:
        # add the set achieving weight > 1 (we only have its weight; rebuild set)
        # conservative: add constraint for the max stable set by recovering it
        added=False
        for Sidx in range(1,1<<n):
            pass
        # Instead of recovering, add constraint that every induced pairing? Too slow.
        # Add the dominant violated set found by a second mwis that returns set.
        # We'll approximate: re-derive the set with a modified bnb that returns a set.
        best_set=mwis_with_set(adj,w)
        if best_set is not None and sum(w[v] for v in best_set) > 1+1e-9:
            constraints.append(tuple(best_set))
    if it%20==0:
        print("  iter",it,"violating stable set weight",round(mw,3))
print("done")

def mwis_with_set(adj,w):
    best=[0.0]; bestset=[set()]
    def rec(cand,total,chosen):
        if not cand:
            if total>best[0]+1e-12:
                best[0]=total; bestset[0]=set(chosen)
            return
        if total+sum(w[v] for v in cand)<=best[0]: return
        v=next(iter(cand)); nb=adj[v]
        rec(cand-{v}-nb,total+w[v],chosen|{v})
        rec(cand-{v},total,chosen)
    rec(set(range(len(adj))),0.0,set())
    return sorted(bestset[0]) if best[0]>0 else None
