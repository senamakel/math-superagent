"""Canonical cascade for UC families (Moore/closure families), CORRECT version.

A union-closed family F' on k+1 elements (adding element x = bit k) projects
to a UC family pi on k elements (drop x).  F' is determined by (pi, R1, R2):
   R2 = {A in pi : A|xbit in F'}  (members whose x-lift appears)
   R1 = {A in pi : A      in F'}  (members that appear without x)
with  R1 U R2 = pi, and the union-closure conditions:
   (up)   R2 is an up-set of the join-semilattice poset (pi, |)
   (uc1)  R1 is closed under |  (A,B in R1 => A|B in R1)
   (cross) A in R1, B in R2  =>  A|B in R2
Then F' = {A : A in R1} U {A|xbit : A in R2}.  Conversely every valid triple
gives a UC family, and the triple is unique.  So
   #(UC on k+1) = sum over UC pi on k of #valid(R1,R2).

We verify the cascade reproduces A102897 (nonempty counts 3,13,121,4959) and
the profile counts 1,4,18,138, then extend to n=5 (and n=6 if feasible).
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


def profile_of(F, k1):
    counts = [0] * k1
    for s in F:
        for i in range(k1):
            if (s >> i) & 1:
                counts[i] += 1
    return tuple(sorted((c for c in counts if c > 0), reverse=True))


def extend_level(level, k):
    """level: set of frozenset masks on k bits (UC families). Return UC families
    on k+1 bits, plus per-family profile counts."""
    xbit = 1 << k
    next_level = set()
    for pi in level:
        pil = list(pi)
        # enumerate R2: up-sets of poset pi
        for R2 in upsets_of(pi):
            R2s = set(R2)
            # R1 must satisfy: R1 U R2 = pi ; R1 uc-closed ; cross
            # so R1 is a superset of (pi \ R2), subset of pi, satisfying:
            #   (a) A,B in R1 => A|B in R1
            #   (b) A in R1, B in R2 => A|B in R2
            need = set(pi) - R2s            # forced into R1
            rest = R2s                       # may optionally join R1
            # R1 must be a subset of pi containing `need`, and with the two
            # closure conditions. Enumerate all such R1.
            # Since R1 contains need, require need itself is uc-closed &
            # cross-ok; then add optional members of `rest` respecting closure.
            # Simple brute over subsets of `rest`.
            rest_l = list(rest)
            for sub in range(1 << len(rest_l)):
                R1 = set(need)
                for j, a in enumerate(rest_l):
                    if (sub >> j) & 1:
                        R1.add(a)
                # check uc1
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
                # check cross: A in R1, B in R2 => A|B in R2
                for a in R1:
                    for b in R2s:
                        if (a | b) in pi and (a | b) not in R2s:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                # R1 U R2 = pi
                if (R1 | R2s) != set(pi):
                    continue
                fam = frozenset(set(R1) | {a | xbit for a in R2s})
                assert is_uc(fam), "construction must be UC"
                next_level.add(fam)
    return next_level


def count_level(level, k):
    pc = defaultdict(int)
    for F in level:
        pc[profile_of(F, k)] += 1
    return len(level), pc


def main():
    # level 1: UC families on {0} (masks).  These include the trivial family
    # {empty} = {0}, because a family's projection onto k elements can itself
    # be the trivial {empty} (e.g. F = {{x}} on 2 elements projects to {empty}).
    # We only exclude the fully-trivial family at the FINAL level when counting.
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    # count excluding the trivial {empty}
    def nonempty_level():
        return {f for f in level if f != frozenset({0})}
    c, pc = count_level(nonempty_level(), 1)
    print(f"n=1: UC families={c} distinct_profiles={len(pc)}")
    for k in range(1, 5):
        level = extend_level(level, k)
        c, pc = count_level(nonempty_level(), k + 1)
        print(f"n={k+1}: UC families={c} distinct_profiles={len(pc)}")


if __name__ == "__main__":
    main()
