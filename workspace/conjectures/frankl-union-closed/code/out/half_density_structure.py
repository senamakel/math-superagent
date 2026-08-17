"""Investigate structure of half-density UC families (max element density == 1/2):
1. Is |F| always a power of 2? (rank-uniformity hint)
2. The |F| distribution across half-density families.
3. Do the half-density families have a clean structure (all elements density 1/2,
   or one subset at 1/2 and others above)?
At n=5 via cascade; n<=4 via direct oracle to cross-check.
"""
from fractions import Fraction
from collections import Counter


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


def abundance(F, n):
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def analyze(fams, n):
    half_fams = []
    for F in fams:
        counts = abundance(F, n)
        m = len(F)
        present = [c for c in counts if c > 0]
        top = max(present)
        if Fraction(top, m) == Fraction(1, 2):
            # how many elements at exactly density 1/2, and how many above
            at_half = sum(1 for c in present if 2 * c == m)
            above = sum(1 for c in present if 2 * c > m)
            half_fams.append((m, at_half, above))
    return half_fams


def main():
    # build levels
    levels = {}
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels[1] = {f for f in level if f != frozenset({0})}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    for n in range(1, 6):
        hf = analyze(levels[n], n)
        distr = Counter(m for m, _, _ in hf)
        npow2 = [m for m, _, _ in hf if m & (m - 1) != 0]  # not power of 2
        # any family where some element is strictly above 1/2 while max is 1/2?
        # (i.e. not all-present elements at exactly 1/2) - check
        mixed = [t for t in hf if t[2] > 0]   # above-count > 0
        print(f"n={n}: {len(hf)} half-density fams; |F| distribution={sorted(distr.items())}")
        print(f"     non-power-of-2 |F| count: {len(npow2)}; "
              f"families with an element density>1/2 (mixed): {len(mixed)}")


if __name__ == "__main__":
    main()
