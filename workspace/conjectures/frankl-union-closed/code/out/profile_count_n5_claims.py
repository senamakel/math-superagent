"""Using the corrected cascade (which exactly reproduces n<=4 oracle), extend
two abundance-profile structural claims to n=5:
  Claim C: no UC family with a degree-1 element lacks an abundant element
           (=> a minimal counterexample has no degree-1 element).
  Claim A: WORST(n) = min min-density = 1/(2^{n-1}+1), attained by near-n-cube;
           every family satisfies min_present_count*(2^{n-1}+1) >= |F|.
Also re-confirm the n=5 distinct-profile count = 2503 and the near-n-cube
profile [2^{n-2}+1 repeated n-1 times, 1].
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


def abundance(F, n):
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def main():
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    def nontrivial():
        return {f for f in level if f != frozenset({0})}
    level = extend_level(level, 1)   # n=2
    level = extend_level(level, 2)   # n=3
    level = extend_level(level, 3)   # n=4
    level = extend_level(level, 4)   # n=5
    fams = nontrivial()
    n = 5
    den = 2 ** (n - 1) + 1   # 17
    claimC_bad = 0
    claimA_fail = 0
    worst = None
    profiles = set()
    near = frozenset(set(range(1 << (n - 1))) | {31})  # 2^[n-1] U {[n]}
    near_counts = tuple(sorted(abundance(near, n), reverse=True))
    print("near-n-cube profile (n=5):", near_counts, "== [2^3+1 x4, 1]?",
          near_counts == (9, 9, 9, 9, 1))
    for F in fams:
        counts = abundance(F, n)
        m = len(F)
        profiles.add(tuple(sorted((c for c in counts if c > 0), reverse=True)))
        present = [c for c in counts if c > 0]
        mn = min(present)
        if worst is None or mn / m < worst:
            worst = mn / m
        if mn * den < m:
            claimA_fail += 1
        if 1 in counts and not any(2 * c >= m for c in counts):
            claimC_bad += 1
    from fractions import Fraction
    print(f"n=5: distinct profiles = {len(profiles)}")
    print(f"n=5: WORST min-density = {worst} == 1/17 ? {abs(worst-1/17)<1e-12}")
    print(f"n=5: claim C (degree-1 without abundant) failures = {claimC_bad}")
    print(f"n=5: claim A (min_count*17 >= |F|) failures = {claimA_fail}")


if __name__ == "__main__":
    main()
