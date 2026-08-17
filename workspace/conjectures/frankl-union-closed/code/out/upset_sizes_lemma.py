"""Mechanical verification of Lemma 2: every size s in [1, 2^d] is realized by
an up-set (filter) of the Boolean lattice B_d, for d = 1..5 (dedup by DFS over
up-sets; B_5 has 7581 up-sets, trivial).
Also verify Lemma 2's explicit interval construction at d=5 for every s in
1..32: S = rank filter S_k = {A : |A| >= k} plus t (k-1)-sets.
"""
from itertools import combinations


def upsets_of_cube(d):
    F = list(range(1 << d))
    results = set()
    def dfs(present):
        if present in results:
            return
        results.add(present)
        ps = set(present)
        for x in present:
            removable = True
            for y in present:
                if y != x and (y | x) == x:
                    removable = False
                    break
            if removable:
                dfs(frozenset(ps - {x}))
    dfs(frozenset(F))
    return results


def rank_filter_upset(d, s):
    """Explicit up-set of B_d of size s, via the interval construction.
    S_k = {A : |A| >= k}; sizes |S_k| .. |S_{k-1}| attained by adding (k-1)-sets.
    Returns set of bitmasks."""
    pop = [bin(A).count("1") for A in range(1 << d)]
    if s == 0:
        return set()
    if s == 1 << d:
        return set(range(1 << d))
    # find k with |S_k| <= s <= |S_{k-1}|
    Sk = {}
    for k in range(d + 2):
        Sk[k] = sum(1 for p in pop if p >= k)
    k = None
    for kk in range(1, d + 2):
        if Sk[kk] <= s <= Sk[kk - 1]:
            k = kk
            break
    S = {A for A in range(1 << d) if pop[A] >= k}
    t = s - len(S)
    # add t (k-1)-sets (any choice works: they have no superset relations among
    # themselves, and all their proper supersets have rank >= k and are in S)
    cands = [A for A in range(1 << d) if pop[A] == k - 1]
    S |= set(cands[:t])
    return S


def is_upset(d, S):
    return all((A | B) == B and B in S for A in S for B in range(1 << d) if (A | B) == B)


for d in range(1, 6):
    U = upsets_of_cube(d)
    sizes = sorted({len(u) for u in U})
    full = list(range(1, (1 << d) + 1))
    print(f"d={d}: #up-sets={len(U)}, sizes cover 1..2^d: "
          f"{all(s in sizes for s in full)}")

# explicit interval construction, d=5, every s in 1..32:
d = 5
ok = True
for s in range(1, 33):
    S = rank_filter_upset(d, s)
    if len(S) != s or not is_upset(d, S):
        ok = False
        print(f"  construction FAILS at s={s}: len={len(S)}")
print(f"d=5: explicit interval construction realizes every s in 1..32: {ok}")