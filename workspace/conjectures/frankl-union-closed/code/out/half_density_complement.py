"""Complement check: among union-closed families on [n], n<=5, if ANY element has
density exactly 1/2, the family is a Boolean subalgebra (block-partition family).
I.e. the half-density families from the earlier survey are EXACTLY the Boolean
subalgebras, so the characterization is not an artifact of Max-only selection.

Also check the logically stronger statement: "some element at density 1/2"
(coordinate-wise, not max only) on UC families => Boolean subalgebra, and that
no non-Boolean UC family has ANY element at density exactly 1/2.
"""
from fractions import Fraction
from lib.uc import abundance


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
            rest_l = list(R2s)
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
                next_level.add(fam)
    return next_level


def is_boolalg(F):
    F = list(F)
    return all((a ^ b) in F for a in F for b in F)


def main():
    levels = {}
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels[1] = {f for f in level if f != frozenset({0})}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    for n in range(1, 6):
        # families with ANY element at density exactly 1/2
        any_half = 0
        # among them, how many are Boolean subalgebras (should be ALL)
        any_half_bool = 0
        # non-Boolean UC families with an element at density 1/2 (should be 0)
        nonbool_with_half = 0
        for F in levels[n]:
            counts = abundance(F, n)
            m = len(F)
            present = [c for c in counts if c > 0]
            if any(Fraction(c, m) == Fraction(1, 2) for c in present):
                any_half += 1
                if is_boolalg(F):
                    any_half_bool += 1
                else:
                    nonbool_with_half += 1
        print(f"n={n}: families with ANY element at density 1/2 = {any_half}, "
              f"of which Boolean subalgebras = {any_half_bool}, "
              f"non-Boolean with a half element = {nonbool_with_half}")


if __name__ == "__main__":
    main()