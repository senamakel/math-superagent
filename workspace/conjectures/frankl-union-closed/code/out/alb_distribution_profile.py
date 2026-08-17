"""Compute the distribution of |Alb(F)| — the NUMBER of abundant elements —
over all nonempty union-closed families on [n], n=1..5, via the validated
projection/up-set cascade. Exact integer counts.

A family F has |Alb| = k when exactly k elements satisfy 2*c_x >= |F|
(sum over present and absent; absent elements have c=0 so never abundant).

This extends the |Alb| distribution first tabulated (n=1..4) in
mroof_enum.captured.txt:
  n=1: {0:1, 1:2}
  n=2: {0:1, 1:6, 2:6}
  n=3: {0:1, 1:18, 2:60, 3:42}
  n=4: {0:1, 1:64, 2:942, 3:2460, 4:1492}

Output sequence of interest: # UC families with EXACTLY ONE abundant element
(= the "marginal" families, closest to being candidates for a counterexample).
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


def alb_counts(F, n):
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    m = len(F)
    return sum(1 for c in counts if 2 * c >= m)


def main():
    levels = {}
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels[1] = {f for f in level if f != frozenset({0})}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    for n in range(1, 6):
        fams = levels[n]
        distr = defaultdict(int)
        for F in fams:
            distr[alb_counts(F, n)] += 1
        total = len(fams)
        print(f"n={n}: total nonempty UC = {total}, |Alb| distribution = "
              f"{dict(sorted(distr.items()))}")

    print("\nSequence: # nonempty UC families with EXACTLY ONE abundant element,")
    print("n=1..5:")
    for n in range(1, 6):
        fams = levels[n]
        c = sum(1 for F in fams if alb_counts(F, n) == 1)
        print(f"  n={n}: {c}")


if __name__ == "__main__":
    main()
