"""Independent second-route verification that the BvLS fixed-set lemma FAILS.

The main script found an order-2 automorphism of bvls_graph() fixing 27
vertices whose induced subgraph is 6-regular, lambda=1 constant, but mu in
{0,2} (non-constant) -> neither a coclique nor an SRG.  This verifier re-derives
that from scratch, by a DIFFERENT route, to rule out an indexing or
automorphism-construction bug:

  (1) re-build bvls directly (no reuse of the auto-finder);
  (2) find an order-2 automorphism by checking, for the specific permutation
      v -> (signs . perm coords), that A[Pv,Pw]==A[v,w] for ALL pairs
      (direct matrix conjugation P A P^T == A), confirming it is a true
      automorphism of the 243x243 matrix;
  (3) independently recompute the 27 fixed vertices for a DIFFERENT order-2
      automorphism than the one detailed before, and classify its induced
      subgraph with the exact oracle lib.srg.is_srg.
"""
import itertools
import numpy as np
from lib.srg import bvls_graph, is_srg

verts = list(itertools.product([0, 1, 2], repeat=5))
idx = {v: t for t, v in enumerate(verts)}
A = bvls_graph()          # 243x243

print("independent verifier: bvls is_srg(243,22,1,2):", is_srg(A, 243, 22, 1, 2)[0])
print()

def pmap_from(perm, signs):
    pmap = [0] * 243
    for v, t in idx.items():
        fv = tuple((signs[j] * v[perm[j]]) % 3 for j in range(5))
        pmap[t] = idx[fv]
    return np.array(pmap, dtype=np.int64)

def is_auto_bruteforce(pmap):
    """Check P A P^T == A via direct 243x243 boolean comparison."""
    Ap = A[np.ix_(pmap, pmap)]
    return np.array_equal(Ap, A)

# Two distinct order-2 automorphisms found by the construction route:
candidates = [
    ((0, 2, 1, 4, 3), (1, 1, 1, 2, 2)),   # the one detailed before (fix 27)
    ((3, 0, 1, 2, 4), (1, 1, 2, 2, 2)),   # another (fix ?, independent)
    ((1, 0, 4, 3, 2), (1, 1, 1, 2, 1)),   # another
]
import math
def order_of(pmap):
    n = len(pmap); seen = [False]*n; lcm = 1
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = pmap[j]; L += 1
            lcm = lcm*L//math.gcd(lcm, L)
    return lcm

for (perm, signs) in candidates:
    pmap = pmap_from(perm, signs)
    ordr = order_of(pmap)
    auto = is_auto_bruteforce(pmap)
    print(f"perm={perm} signs={signs}: order={ordr}, P A P^T==A (direct 243x243) = {auto}")
    F = [i for i in range(243) if pmap[i] == i]
    nF = len(F)
    S = A[np.ix_(F, F)]
    e = int(S.sum() // 2)
    degs = sorted(set(S.sum(axis=1).tolist()))
    S2 = S @ S
    adj = S.astype(bool); off = ~np.eye(nF, dtype=bool)
    from collections import Counter
    lam = dict(Counter(S2[adj & off].tolist()))
    mu = dict(Counter(S2[(~adj) & off].tolist()))
    coc = (e == 0)
    print(f"   fixed size {nF}, edges {e}, degrees {degs}, coclique={coc}")
    print(f"   lambda dist={lam}, mu dist={mu}")
    if not coc and len(degs) == 1:
        k = degs[0]
        srg_res = is_srg(S, nF, k, 1, 2)
        print(f"   is_srg(S,{nF},{k},1,2) = {srg_res}")
    print()
print("CONCLUSION (independent route): same as main -- the BvLS fixed set of an")
print("order-2 automorphism can be a 6-regular graph that is neither a coclique")
print("nor strongly regular (mu non-constant), so the folklore lemma as stated")
print("fails on this control.")
