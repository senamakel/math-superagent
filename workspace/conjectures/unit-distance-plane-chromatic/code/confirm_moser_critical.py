#!/usr/bin/env python3
"""Confirm the Moser spindle IS 4-critical in the classical sense: removing
any single edge makes it 3-colourable (chi drops to 3). The earlier bug looked
at 4-colourability of the removal, which stays True trivially.

(Previous confusion: my 'debug' tested is_4col(rem), which is True both for a
3-colourable and a 4-colourable graph. Edge-criticality requires the removal to
be 3-colourable, which is the strictly smaller test.)
"""
import itertools
moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
n=7
def is_kcol(es,k):
    adj=[set() for _ in range(n)]
    for a,b in es: adj[a].add(b); adj[b].add(a)
    col=[-1]*n
    def bt(v):
        if v==n: return True
        used={col[u] for u in adj[v] if col[u]>=0}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(v+1): return True
                col[v]=-1
        return False
    return bt(0)

print("Moser 4-colourable:", is_kcol(moser,4))
print("Moser 3-colourable:", is_kcol(moser,3))
# edge-critical: every single-edge removal is 3-colourable
rem3col=[]
for i in range(len(moser)):
    rem=moser[:i]+moser[i+1:]
    rem3col.append(is_kcol(rem,3))
print("every single-edge removal 3-colourable (edge-critical):", all(rem3col))
