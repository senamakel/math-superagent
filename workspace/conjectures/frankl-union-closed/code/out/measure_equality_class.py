"""Measure the TRUE equality class at n=5: families with
min_present_count * (2^{n-1}+1) == m  (Nagel/Das-Wu bound, equality forces
min_count==1 and m==2^{n-1}+1==17, since min_count>=2 would need m>=34>32).
Also report the true minimum-density families."""
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
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    for k in range(1, 5):
        level = extend_level(level, k)
    fams = [f for f in level if f != frozenset({0})]
    n = 5
    den = 2 ** (n - 1) + 1   # 17
    eq = 0
    worst_density = None
    worst_profiles = defaultdict(int)
    for F in fams:
        counts = [0] * n
        for s in F:
            for i in range(n):
                if (s >> i) & 1:
                    counts[i] += 1
        m = len(F)
        present = [c for c in counts if c > 0]
        mn = min(present)
        if mn * den == m:
            eq += 1
            if eq <= 40:
                pass
        # true min-density: minimize mn/m (as exact fraction)
        from fractions import Fraction
        d = Fraction(mn, m)
        if worst_density is None or d < worst_density:
            worst_density = d
    print(f"n={n}: true equality class (min_count*{den}==m) size = {eq}")
    print(f"true minimum density WORST = {worst_density} = 1/{den}? "
          f"{worst_density == Fraction(1, den)}")


if __name__ == "__main__":
    main()
