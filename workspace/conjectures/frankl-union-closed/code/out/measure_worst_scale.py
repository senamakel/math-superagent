"""Measure the scale of the WORST(n) class (min present count == 1) at n=5:
how many UC families qualify, how many distinct profiles, max orbit workload.
Reuses the validated projection/up-set cascade that reached n=5."""
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


def extend_level(level, k):
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


def main():
    # build through n=5
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    for k in range(1, 5):
        level = extend_level(level, k)
    fams = [f for f in level if f != frozenset({0})]
    n = 5
    print(f"n={n}: {len(fams)} nonempty UC families")

    worst_profiles = defaultdict(int)   # sorted-desc profile -> count of families
    worst_fams = 0
    nearcube = frozenset(set(range(1 << (n - 1))) | {(1 << n) - 1})
    nc_counts = tuple(sorted([2 ** (n - 2) + 1] * (n - 1) + [1], reverse=True))

    for F in fams:
        counts = [0] * n
        for s in F:
            for i in range(n):
                if (s >> i) & 1:
                    counts[i] += 1
        present = [c for c in counts if c > 0]
        if min(present) == 1:
            worst_fams += 1
            prof = tuple(sorted(counts, reverse=True))
            worst_profiles[prof] += 1

    print(f"families with min present count == 1: {worst_fams}")
    print(f"distinct worst profiles: {len(worst_profiles)}")
    print("profile multiset (sorted by count desc):")
    for prof, cnt in sorted(worst_profiles.items(), key=lambda x: -x[1]):
        print(f"   {prof}: {cnt} families")
    print(f"near-n-cube profile {nc_counts} expected present: "
          f"{worst_profiles.get(nc_counts, 0)}")


if __name__ == "__main__":
    main()
