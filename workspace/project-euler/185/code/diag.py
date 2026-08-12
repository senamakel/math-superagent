#!/usr/bin/env python3
"""Diagnostic: how many nodes does the two-sided-pruning backtracking visit,
and does a different column order beat the natural one? Counts nodes and
reports where time goes. Run with a per-position node budget so we can
measure growth rather than hang forever.
"""
import sys, time

FULL = """
5616185650518293 ;2
3847439647293047 ;1
5855462940810587 ;3
9742855507068353 ;3
4296849643607543 ;3
3174248439465858 ;1
4513559094146117 ;2
7890971548908067 ;3
8157356344118483 ;1
2615250744386899 ;2
8690095851526254 ;3
6375711915077050 ;1
6913859173121360 ;1
6442889055042768 ;2
2321386104303845 ;0
2326509471271448 ;2
5251583379644322 ;2
1748270476758276 ;3
4895722652190306 ;1
3041631117224635 ;3
1841236454324589 ;3
2659862637316867 ;2
"""

def parse(text):
    out=[]
    for line in text.strip().splitlines():
        s,c=line.split(";")
        out.append((s.strip(), int(c.strip())))
    return out

def solve(guesses, order, budget):
    length=len(guesses[0][0]); n=len(guesses)
    results=[]
    assignment=[None]*length
    nodes=[0]
    def backtrack(idx, m):
        nodes[0]+=1
        if nodes[0]>budget:
            raise TimeoutError
        if idx==length:
            if all(m[i]==guesses[i][1] for i in range(n)):
                results.append("".join(assignment))
            return
        pos=order[idx]
        r=length-idx
        for d in "0123456789":
            ok=True
            nm=m[:]
            for i in range(n):
                g,c=guesses[i]
                if g[pos]==d: nm[i]+=1
                if nm[i]>c: ok=False; break
                if nm[i]+(r-1)<c: ok=False; break
            if ok:
                assignment[pos]=d
                backtrack(idx+1,nm)
                assignment[pos]=None
    backtrack(0,[0]*n)
    return results, nodes[0]

g=parse(FULL)

# natural order
try:
    t=time.time()
    res,nodes=solve(g,list(range(16)),10**8)
    print("natural order: nodes",nodes,"sols",res[:5],"len",len(res),"time",time.time()-t)
except TimeoutError:
    print("natural order: exceeded budget")

# Try order that prioritizes columns where the 0-count guess differs... no info.
# Try each column ordering: greedy by "most guesses constrain". We'll just do a
# heuristic: order columns by diversity of digits across guesses (fewer distinct
# digits seen => more constrained? actually more same digits).
from collections import Counter
col_diversity=[]
for pos in range(16):
    col=[g2[pos] for g2,_ in g]
    col_diversity.append(len(set(col)))
print("distinct digits per column:", col_diversity)
# reorder: increasing diversity (fewer choices) first
order=sorted(range(16), key=lambda p: col_diversity[p])
print("order by diversity:", order)
try:
    t=time.time()
    res,nodes=solve(g,order,10**8)
    print("diversity order: nodes",nodes,"sols",res[:5],"len",len(res),"time",time.time()-t)
except TimeoutError:
    print("diversity order: exceeded budget")
