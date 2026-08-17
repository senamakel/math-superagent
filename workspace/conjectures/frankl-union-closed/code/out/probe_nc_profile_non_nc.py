"""Probe: within the near-cube profile (9,9,9,9,1) at n=5, find a NON-near-cube
family with |F|<17 (so identical histogram to the near-cube but NOT the
density-extremal 1/17). Prints it as bitmasks."""
from itertools import permutations


def apply_perm(fam, perm):
    n = len(perm); out = set()
    for m in fam:
        nm = 0
        for i in range(n):
            if (m >> i) & 1:
                nm |= (1 << perm[i])
        out.add(nm)
    return out


def canon_and_orbit(fam, n):
    imgs = set(); rep = None
    for perm in permutations(range(n)):
        t = tuple(sorted(apply_perm(fam, perm)))
        imgs.add(t)
        if rep is None or t < rep:
            rep = t
    return rep, len(imgs)


def abundance(F, n):
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


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
    nc = frozenset(set(range(1 << 4)) | {31})
    nc_canon = canon_and_orbit(nc, n)[0]
    profile = (9, 9, 9, 9, 1)
    for F in fams:
        counts = tuple(sorted(abundance(F, n), reverse=True))
        if counts != profile:
            continue
        c, osz = canon_and_orbit(F, n)
        if c != nc_canon and len(F) < 17:
            print("non-near-cube family with near-cube profile:")
            print("  |F| =", len(F), "counts =", counts)
            print("  sets (bitmasks):", sorted(F))
            print("  canonical:", c)
            print("  orbit size:", osz)
            print("  density = 1/|F| =", f"1/{len(F)}", " (not 1/17)")
            break
    else:
        print("none found")


if __name__ == "__main__":
    main()
