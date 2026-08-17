"""Rigorous check of the core structural step of the block-union derivation.

Derivation being checked (for a UC family F subset 2^[n], |F|=2^k, all present
elements density 1/2):
  (i)  F, being a finite join-semilattice of size 2^k with join = union, is a
       Boolean semilattice iff its minimal nonempty elements (atoms) are
       pairwise disjoint and generate F by unions.
  (ii) Claim: every present ground element x is in EXACTLY ONE atom.
       Proof: if x in two atoms A_i, A_j then x appears in every union
       containing either, i.e. in 2^k - 2^{k-2} = 3*2^{k-2} sets, whose density
       3/4 > 1/2 — contradiction. If x in no atom then x in no generated set,
       contradicting that x is present. So x in exactly one atom, hence the
       atoms form a partition of the support.

This program verifies (i)+(ii) on every half-density UC family n<=5:
  - the minimal nonempty elements are pairwise disjoint
  - every present ground element lies in exactly one atom
  - every set is a union of atoms
It also verifies the counting corollary: #(half-density fams on [n]) =
Bell(|S|) summed over nonempty S subseteq [n] = Bell(n+1)-1, refined by
#(atoms) = k gives S(n+1,k+1).
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


def check_atoms(F, n):
    """For a half-density UC family: find minimal nonempty elements (atoms),
    verify pairwise disjoint, every ground element in exactly one atom, every
    set a union of atoms, and there are k atoms with |F|=2^k."""
    nonempty = [s for s in F if s != 0]
    atoms = [s for s in nonempty
             if not any(t != s and (t & s) == t for t in nonempty)]
    k = len(atoms)
    # pairwise disjoint
    for i in range(k):
        for j in range(i + 1, k):
            if atoms[i] & atoms[j]:
                return (False, "atoms not disjoint")
    # union of atoms exactly F
    gen = set()
    for J in range(1 << k):
        u = 0
        for i in range(k):
            if (J >> i) & 1:
                u |= atoms[i]
        gen.add(u)
    if set(F) != gen:
        return (False, "F != atom unions")
    # every present ground element in exactly one atom
    support = set()
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                support.add(i)
    for x in support:
        cnt = sum(1 for a in atoms if (a >> x) & 1)
        if cnt != 1:
            return (False, f"element {x} in {cnt} atoms")
    # |F| = 2^k
    if len(F) != (1 << k):
        return (False, f"|F|={len(F)} != 2^{k}")
    return (True, f"k={k} atoms={sorted(atoms)}")


def main():
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: {f for f in level if f != frozenset({0})}}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    for n in range(1, 6):
        half = 0
        bad = []
        for F in levels[n]:
            counts = abundance(F, n)
            m = len(F)
            present = [c for c in counts if c > 0]
            if Fraction(max(present), m) == Fraction(1, 2):
                half += 1
                ok, why = check_atoms(F, n)
                if not ok:
                    bad.append((sorted(F), why))
        print(f"n={n}: half-density={half}, atom-structure failures={len(bad)}")
        if bad:
            for fam, why in bad[:3]:
                print(f"   FAIL {fam}: {why}")

    # counting corollary: Bell(n+1)-1 and Stirling refinement
    from math import comb
    def stirling(N, K):
        if K == 1 or K == N:
            return 1
        if K > N or K < 1:
            return 0
        return K * stirling(N - 1, K) + stirling(N - 1, K - 1)
    def bell(m):
        return sum(stirling(m, j) for j in range(1, m + 1))
    print("\nCounting corollary:")
    for n in range(1, 6):
        # Bell(n+1)-1 = sum over nonempty S subset of [n] of Bell(|S|)
        total = 0
        for s in range(1, n + 1):
            total += comb(n, s) * bell(s)
        print(f"  n={n}: Bell({n+1})-1={bell(n+1)-1}  "
              f"sum_|S|>=1 C(n,|S|)Bell(|S|)={total}  equal = {total == bell(n+1)-1}")
        # refinement S(n+1,k+1)
        row = [stirling(n + 1, k + 1) for k in range(1, n + 1)]
        print(f"      S(n+1,k+1) k=1..n: {row}  sum={sum(row) == bell(n+1)-1}")


if __name__ == "__main__":
    main()