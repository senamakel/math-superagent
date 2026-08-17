"""Test conjecture g(n,m) = min over UC families F on [n] with |F|=m of
(min present-element count) = max(1, m - 2^{n-1}).

g is the least "rare-element" count achievable among UC families of size m.
Data at n<=4 (from profile_scan.captured.txt) exactly matches max(1, m-2^{n-1}):
  n=3 (2^{n-1}=4): m=1..5->1, 6->2, 7->3, 8->4
  n=4 (2^{n-1}=8): m=1..9->1, 10->2, 11->3, ..., 16->8

We extend to n=5 and n=6 via the canonical cascade (projection + (R2,R1) lift).
Exact integers throughout.

For each level we compute, over every UC family of size m, the minimum of the
min-present-element count, and compare with max(1, m - 2^{k-1}) where k=n.

To keep n=6 cheap we avoid storing full family lists where possible, but we
need abundance per family; families are small (<= 64 sets) motifs on k<=6 bits.
"""
from collections import defaultdict


def is_uc(F):
    F = list(F)
    for a in F:
        for b in F:
            if (a | b) not in F:
                return False
    return True


def upsets_of(F):
    F = list(F)
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
    return list(results)


def abundance_counts(F, k):
    counts = [0] * k
    for s in F:
        for i in range(k):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def extend_level(level, k):
    """level: set of frozenset masks on k bits (UC families on [k]).
    Return level of UC families on k+1 bits."""
    xbit = 1 << k
    next_level = set()
    for pi in level:
        for R2 in upsets_of(pi):
            R2s = set(R2)
            need = set(pi) - R2s
            rest = R2s
            rest_l = list(rest)
            for sub in range(1 << len(rest_l)):
                R1 = set(need)
                for j, a in enumerate(rest_l):
                    if (sub >> j) & 1:
                        R1.add(a)
                ok = True
                for a in R1:
                    for b in R1:
                        if (a | b) not in R1:
                            ok = False; break
                    if not ok: break
                if not ok: continue
                for a in R1:
                    for b in R2s:
                        if (a | b) in pi and (a | b) not in R2s:
                            ok = False; break
                    if not ok: break
                if not ok: continue
                if (R1 | R2s) != set(pi):
                    continue
                fam = frozenset(set(R1) | {a | xbit for a in R2s})
                next_level.add(fam)
    return next_level


def scan_level(level, n):
    """gd[n][m] = min over families of min present count; also factor by how
    many families (for cross-check with catalogue count)."""
    gd = {}
    famcount = 0
    for F in level:
        famcount += 1
        m = len(F)
        counts = abundance_counts(F, n)
        present = [c for c in counts if c > 0]
        mn = min(present)
        gd[m] = min(gd.get(m, 1 << 60), mn)
    return gd, famcount


def main():
    maxn = 5
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    nontriv = lambda: {f for f in level if f != frozenset({0})}

    for n in range(1, maxn + 1):
        gd, famcount = scan_level(nontriv(), n)
        print(f"n={n}: #UC families (nonempty) = {famcount}")
        pred = lambda m: max(1, m - 2 ** (n - 1))
        ok = all(gd[m] == pred(m) for m in gd)
        print(f"   g(n,m) matches max(1, m-2^{n-1}) for every size reached: {ok}")
        # show a few rows
        rows = sorted(gd.items())
        if n <= 4:
            print("   rows (m -> g):", rows[:25])
        else:
            print("   rows (m -> g):", rows)
        if n < maxn:
            level = extend_level(level, n)


if __name__ == "__main__":
    main()
