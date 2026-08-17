"""Verify the derived bijection for half-density UC families.

Derivation: if F ⊆ 2^[n] is union-closed, |F|=2^k, and every present element has
density exactly 1/2 (=2^{k-1}), then F is a Boolean sub-semilattice of rank k
with join-irreducible generators A_1..A_k, and each present ground element lies
in EXACTLY ONE generator (because it must appear in 2^{k-1} of the 2^k unions,
forcing |{i: x in A_i}| = 1). Hence {A_1,...,A_k} is a partition of the support,
and F = {Union of any subset of the blocks}.

Test 1: every half-density UC family on [5] has all present elements with
        density exactly 1/2 (already confirmed) AND is a block-union family.
Test 2: conversely every block-union family on subsets of [5] is half-density.
Thus: half-density UC families on [n]
        <-> (support S, partition of S into k>=1 blocks of nonempty blocks).
Count: sum_{S subset [n]} Bell(|S|), minus the empty+empty (s=0) case
      = Bell(n+1) - 1, refined by |F|=2^k into S(n+1,k+1).
"""
from fractions import Fraction


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


def is_block_union(F, n):
    """Is F a block-union family: F = {union of any subset of a set of disjoint
    nonempty blocks}, i.e. F is a Boolean sub-semilattice. Verify by: F has
    2^k elements for some k, and F is closed under the 'symmetric' completion
    to a Boolean algebra: each element is a disjoint union of atoms.
    Direct check: find minimal nonempty elements (atoms), require they're
    pairwise disjoint, and every member of F is a union of atoms, and every
    union of atoms is in F."""
    nonempty = [s for s in F if s != 0]
    if not nonempty:
        return False  # need at least one present element
    # atoms: minimal nonempty in F under inclusion
    atoms = []
    for s in nonempty:
        if not any(t != s and (t & s) == t for t in nonempty):
            atoms.append(s)
    # require: every member is union of a subset of atoms, atoms pairwise
    # disjoint, and every union of a subset of atoms is in F
    union_of_atoms = set()
    k = len(atoms)
    for J in range(1 << k):
        u = 0
        for i in range(k):
            if (J >> i) & 1:
                u |= atoms[i]
        union_of_atoms.add(u)
    # pairwise disjoint
    for i in range(k):
        for j in range(i + 1, k):
            if atoms[i] & atoms[j]:
                return (False, "atoms not disjoint")
    if set(F) == union_of_atoms:
        return (True, f"atoms={sorted(atoms)} k={k}")
    return (False, "F != unions of atoms")


def main():
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: {f for f in level if f != frozenset({0})}}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    print("Test 1: every half-density UC family is a block-union family")
    for n in range(1, 6):
        notbu = 0
        total_half = 0
        for F in levels[n]:
            counts = abundance(F, n)
            m = len(F)
            present = [c for c in counts if c > 0]
            if Fraction(max(present), m) == Fraction(1, 2):
                total_half += 1
                ok, why = is_block_union(F, n)
                if not ok:
                    notbu += 1
        print(f"  n={n}: half-density={total_half}, not block-union={notbu}")

    print("\nTest 2: every block-union family (support subset, partition) is half-density")
    # enumerate all partitions of all subsets of [n] directly (no oracle needed)
    from math import comb
    def partitions(n_elts):
        # all set partitions of {0..n_elts-1} as list of lists of (mask) blocks
        res = []
        def rec(els, blocks):
            if not els:
                res.append([b for b in blocks])
                return
            x = els[0]
            rest_els = els[1:]
            for i in range(len(blocks)):
                newblocks = [b | (1 << x) if j == i else b for j, b in enumerate(blocks)]
                rec(rest_els, newblocks)
            rec(rest_els, blocks + [(1 << x)])
        rec(list(range(n_elts)), [])
        return res
    for n in range(1, 6):
        half_count = 0
        dist = {}
        # support = subset of [n]; elements labelled by bit position
        for smask in range(1, 1 << n):   # nonempty support
            support_elts = [i for i in range(n) if (smask >> i) & 1]
            s = len(support_elts)
            for part in partitions(s):
                # blocks are masks over the support bit positions
                blocks = []
                for blk in part:
                    b = 0
                    for j in range(s):
                        if (blk >> j) & 1:
                            b |= (1 << support_elts[j])
                    if b:
                        blocks.append(b)
                # block-union family
                k = len(blocks)
                fam = set()
                for J in range(1 << k):
                    u = 0
                    for i in range(k):
                        if (J >> i) & 1:
                            u |= blocks[i]
                    fam.add(u)
                # is it UC? yes by construction; check density
                counts = abundance(fam, n)
                m = len(fam)
                present = [c for c in counts if c > 0]
                assert is_uc(fam)
                if Fraction(max(present), m) == Fraction(1, 2):
                    half_count += 1
                    dist[k] = dist.get(k, 0) + 1
        print(f"  n={n}: block-union families that are half-density = {half_count}, "
              f"by #blocks {sorted(dist.items())}")


if __name__ == "__main__":
    main()
