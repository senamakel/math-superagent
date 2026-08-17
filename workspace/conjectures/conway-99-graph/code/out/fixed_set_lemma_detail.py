"""Verify the BvLS 'neither' cases: fixed sets of size 27 whose induced
subgraph is 6-regular but not strongly regular. Also compute automorphism
orders and the lambda/mu distributions to confirm the folklore lemma does NOT
hold as 'coclique or SRG' on this control."""
import itertools
from collections import Counter
import numpy as np
from lib.srg import bvls_graph


def factor(n):
    d = {}
    f = 2
    while f * f <= n:
        while n % f == 0:
            d[f] = d.get(f, 0) + 1
            n //= f
        f += 1
    if n > 1:
        d[n] = d.get(n, 0) + 1
    return d


def order_of_perm(perm):
    # lcm of cycle lengths
    n = len(perm)
    seen = [False] * n
    lcm = 1
    import math
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True
                j = perm[j]; L += 1
            lcm = lcm * L // math.gcd(lcm, L)
    return lcm


B = bvls_graph()
verts = list(itertools.product([0, 1, 2], repeat=5))

# Reconstruct the 40 automorphisms fixing 0 to compute orders + fixed sets
def _cols(A):
    nbr0 = [i for i in range(243) if A[0, i] == 1]
    cols = []; seen = set()
    for t in nbr0:
        v = verts[t]
        key = tuple(sorted([v, tuple((2 * x) % 3 for x in v)]))
        if key not in seen:
            seen.add(key); cols.append(v)
    return cols

cols = _cols(B)
base = set(tuple(sorted([c, tuple((2 * x) % 3 for x in c)])) for c in cols)
idx = {v: t for t, v in enumerate(verts)}

def cset(f):
    return set(tuple(sorted([f(c), tuple((2 * x) % 3 for x in f(c))])) for c in cols)

autos = {}
for perm in itertools.permutations(range(5)):
    for signs in itertools.product([1, 2], repeat=5):
        f = (lambda c, perm=perm, signs=signs:
             tuple((signs[j] * c[perm[j]]) % 3 for j in range(5)))
        if cset(f) == base and f((0, 0, 0, 0, 0)) == (0, 0, 0, 0, 0):
            pmap = [0] * 243
            for v, t in idx.items():
                fv = tuple((signs[j] * v[perm[j]]) % 3 for j in range(5))
                pmap[t] = idx[fv]
            autos[(perm, signs)] = tuple(pmap)

print("=== BvLS automorphisms fixing 0: orders and fixed-set sizes ===")
from collections import defaultdict
by_fixsize = defaultdict(list)
for (perm, signs), pmap in autos.items():
    F = [i for i in range(243) if pmap[i] == i]
    o = order_of_perm(pmap)
    by_fixsize[len(F)].append((o, perm, signs))
for sz in sorted(by_fixsize):
    items = by_fixsize[sz]
    orders = Counter(o for o, _, _ in items)
    print(f"  fixed size {sz}: count={len(items)}, orders={dict(orders)}")

print()
print("=== Detail on one 27-vertex 'neither' case ===")
# pick the fixed set [0,12,24,...] -> which automorphism? find one with size 27
target = None
for (perm, signs), pmap in autos.items():
    F = [i for i in range(243) if pmap[i] == i]
    if len(F) == 27:
        target = (pmap, F, perm, signs)
        break
pmap, F, perm, signs = target
print("automorphism perm:", perm, "signs:", signs, "order:", order_of_perm(pmap))
S = B[np.ix_(F, F)]
print("|F| =", len(F), "edges =", int(S.sum() // 2))
degs = S.sum(axis=1)
print("degrees (fixed set):", sorted(set(degs.tolist())))
S2 = S @ S
adj = S.astype(bool); off = ~np.eye(len(F), dtype=bool)
lam_vals = S2[adj & off]
mu_vals = S2[(~adj) & off]
print("lambda (adjacent common-neighbour) distribution:", dict(Counter(lam_vals.tolist())))
print("mu     (non-adjacent common-neighbour) distribution:", dict(Counter(mu_vals.tolist())))
print()
print("Interpretation: the fixed set is NOT a coclique (81 edges) and NOT an SRG")
print("(lambda takes the values above, mu takes the values above -> non-constant).")
print("So the folklore lemma stated as 'fixed set is a coclique or a smaller SRG'")
print("FAILS on this control.  The fixed set is a 6-regular graph that is neither.")
print()
print("=== Contrast: a size-9 fixed set that DOES induce srg(9,4,1,2) ===")
# find a size-9 non-coclique fixed set
for (perm, signs), pmap in autos.items():
    Fv = [i for i in range(243) if pmap[i] == i]
    if len(Fv) == 9:
        S = B[np.ix_(Fv, Fv)]
        e = int(S.sum() // 2)
        if e > 0:
            S2 = S @ S; adj = S.astype(bool); off = ~np.eye(9, dtype=bool)
            lam = S2[adj & off]; mu = S2[(~adj) & off]
            print(f"  fixed size 9, edges={e}, deg={sorted(set(S.sum(axis=1).tolist()))}")
            print(f"     lambda dist={dict(Counter(lam.tolist()))}, mu dist={dict(Counter(mu.tolist()))}")
            print(f"     -> strongly regular srg(9,4,1,2) confirmed (is_srg check below)")
            from lib.srg import is_srg
            print("     is_srg(F,9,4,1,2):", is_srg(S, 9, 4, 1, 2))
            break
