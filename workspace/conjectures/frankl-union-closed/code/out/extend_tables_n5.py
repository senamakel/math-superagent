"""Extend four previously-computed integer tables from n<=4 to n=5, exactly,
using the validated canonical cascade (profile_count_cascade machinery).

Tables (all over UC families; semantics copied verbatim from the source runs):
  T1 degree1 : # UC families with some element in exactly one set
               (source: combine_constraints.py claim D counts 2,10,56,590)
  T2 eq3     : # empty-free UC families with f == min{n, 2k-n+1}, f = #
               elements with strict abundance 2*c > |F|, k = min set size,
               n = max set size  (source: kpt_thm5_verify.py, 1,5,16,43)
  T3 emptyfree : # empty-free UC families  (source: 1,6,60,2479)
  T4 A-satisfying : # empty-free UC families with n_max >= 2*k_min + 1
               (source: combine_constraints.py (A) 0,0,37,2041)

Guards: level counts must reproduce A121921 minus the trivial family
(2, 12, 120, 4958, 2771102 nonempty UC families on n=1..5), the same guard the
cascade was validated against.

Exact integer arithmetic only. No floats.
"""
import sys
import time
from collections import defaultdict


def is_uc(F):
    F = list(F)
    for a in F:
        for b in F:
            if (a | b) not in F:
                return False
    return True


def upsets_of(F):
    """All up-sets of the poset (F, |) with A<=B iff A|B==B, as frozensets."""
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
    """level: set of frozenset masks on k bits (UC families). Return UC families
    on k+1 bits."""
    xbit = 1 << k
    next_level = set()
    for pi in level:
        pil = list(pi)
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
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                for a in R1:
                    for b in R2s:
                        if (a | b) in pi and (a | b) not in R2s:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                if (R1 | R2s) != set(pi):
                    continue
                fam = frozenset(set(R1) | {a | xbit for a in R2s})
                assert is_uc(fam), "construction must be UC"
                next_level.add(fam)
    return next_level


def abundance(F, n):
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def popcount(x):
    return bin(x).count("1")


def main():
    t0 = time.time()
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: level}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = level

    expected = {1: 2, 2: 12, 3: 120, 4: 4958, 5: 2771102}  # nonempty UC counts
    print("extend four UC-family tables to n=5 via validated cascade")
    print("oracle: profile_count_cascade (validated vs A121921 minus trivial)")
    print("range : n=1..5, ALL union-closed families, exact integers")
    guards_ok = True
    for n in range(1, 6):
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        got = len(nonempty)
        exp = expected[n]
        ok = (got == exp)
        guards_ok = guards_ok and ok
        print(f"guard n={n}: {got} (expected {exp}) {'OK' if ok else 'FAIL'}")
    if not guards_ok:
        print("GUARD FAILED — cascade not validated, aborting")
        return 1

    T1, T2, T3, T4 = [], [], [], []
    for n in range(1, 6):
        d1 = 0
        eq3 = 0
        emptyfree = 0
        a_sat = 0
        for F in levels[n]:
            if F == frozenset({0}):
                # trivial {empty} family: no present element, not empty-free
                continue
            counts = abundance(F, n)
            # degree-1: some present element in exactly one set
            if any(c == 1 for c in counts):
                d1 += 1
            if 0 in F:
                continue  # KPT and (A) use the empty-free convention
            emptyfree += 1
            m = len(F)
            f = sum(1 for c in counts if 2 * c > m)  # strict abundance
            ks = [popcount(s) for s in F]
            k = min(ks)
            nn = max(ks)
            if f == min(nn, 2 * k - nn + 1):
                eq3 += 1
            if nn >= 2 * k + 1:
                a_sat += 1
        T1.append(d1)
        T2.append(eq3)
        T3.append(emptyfree)
        T4.append(a_sat)
        print(f"n={n}: degree1={d1}  eq3={eq3}  emptyfree={emptyfree}  "
              f"A-sat={a_sat}")
    print("T1 degree1     :", T1)
    print("T2 eq3         :", T2)
    print("T3 emptyfree   :", T3)
    print("T4 A-sat       :", T4)
    print(f"elapsed {time.time() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())