"""Verify the exact sub-count identity underpinning the proof that
(H x^{a,a'})_w = 0 for a matched pair {a,a'} of N(0), in every one of the four
case categories (w~a? x w~a'?), on bvls (the mu=2 nontrivial control).

(Hx)_w = |{outer u: u~w, u~a}| - |{outer u: u~w, u~a'}|
       =: |A_w| - |A'_w|.

We verify A_w == A'_w as SETS for every outer w and every matched pair.
Then Hx=0 follows; we also print which case-category each (w) falls into.
"""
import numpy as np
from lib.srg import bvls_graph

A = np.asarray(bvls_graph(), dtype=np.int64)
n = A.shape[0]
N0 = [j for j in range(n) if j != 0 and A[0][j] == 1]
outer = [j for j in range(n) if j != 0 and A[0][j] == 0]
# matched edges of N(0)
rem = set(N0); edges = []
while rem:
    a = min(rem); rem.discard(a)
    b = [c for c in N0 if A[a][c] == 1][0]
    rem.discard(b); edges.append((a, b))

ok_all = True
for (a, ap) in edges:
    for w in outer:
        Aw = frozenset(u for u in outer if A[u][w] and A[u][a])
        Awp = frozenset(u for u in outer if A[u][w] and A[u][ap])
        if Aw != Awp:
            ok_all = False
            print(f"  MISMATCH a={a} a'={ap} w={w}: |A_w|={len(Aw)} |A'_w|={len(Awp)}")
print(f"all outer w, all matched pairs: A_w == A'_w  : {ok_all}")
print(f"total matched pairs {len(edges)}, outer {len(outer)}")
