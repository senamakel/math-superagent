"""Verify the half-density family structure on [n], n<=5, using the canonical
cascade (validated against the oracle and A121921 elsewhere).

Claim under test:
  H(n) = number of union-closed families F on [n] (nonempty, F != {0})
         whose MAX element density is exactly 1/2.
  Data (from commands.log): H(1..5) = 1, 4, 14, 51, 202 = Bell(n+1)-?  -- the
  sequence tools + OEIS said A058692 = Bell(n)-1 matches 1,4,14,51,202 ... but
  Bell(1)-1=1, Bell(2)-1=1, Bell(3)-1=4, Bell(4)-1=14, Bell(5)-1=51, Bell(6)-1=202.
  So H(n) = Bell(n+1) - 1 for n=1..5 (offset by one from A058692's a(n)=B(n)-1
  which lists 1,4,14,51,202 at n=2..6).  Verified below by direct count, and the
  structural characterization:
     every half-density UC family is a BLOCK-PARTITION family:
     F = { union_{i in T} B_i : T subseteq [k] } for a partition
     {B_1,...,B_k} of a SUBSET of [n], i.e. F is a Boolean lattice on its
     join-irreducible atoms, each element of [n] lies in exactly one atom, and
     the universe U(F) = union B_i has |U(F)| = 2^{m} for some m (a power of 2
     family size) with ALL elements at density exactly 1/2 (regular).
     Equivalently: F is union-closed, closed under symmetric difference of
     members (i.e. F is a Boolean subalgebra of 2^[n]), OR the blocks B_i are
     the equivalence classes of the relation x~y iff {x,y} subsets of the same
     minimal members.  We check: (a) count matches Bell(n+1)-1, (b) every
     half-density family has |F| a power of 2 and ALL n elements (present) at
     density 1/2, (c) every such family is a Boolean subalgebra (closed under
     symmetric difference).

The cascade gives the full family list at level n (nonempty, nontrivial), and
lib.uc abundance is exact. Everything below is exact integer/fraction math.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from lib.uc import decide_union_closed, abundance


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


def is_block_partition_family(F, n):
    """Is F a Boolean subalgebra (closed under symmetric difference) of 2^[n]?
    Equivalently: F = { union of blocks over a subset of a partition }.
    A union-closed family is a Boolean subalgebra iff it is closed under
    A xor B for every pair.  (Boolean subalgebras of 2^[n] are exactly the
    block-partition / product-of-2 lattices.)"""
    F = list(F)
    for a in F:
        for b in F:
            if (a ^ b) not in F:
                return False
    return True


def main():
    levels = {}
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels[1] = {f for f in level if f != frozenset({0})}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    # Bell numbers
    bell = [1, 1, 2, 5, 15, 52, 203]
    print("n | half-density count | Bell(n+1)-1 | match | all |F| a power of 2"
          " | all present elements at exactly 1/2 | all are Boolean subalgebras")
    for n in range(1, 6):
        hf = []
        for F in levels[n]:
            counts = abundance(F, n)
            m = len(F)
            present = [c for c in counts if c > 0]
            top = max(present)
            if Fraction(top, m) == Fraction(1, 2):
                hf.append(F)
        cnt = len(hf)
        exp = bell[n + 1] - 1
        pow2 = all((len(F) & (len(F) - 1)) == 0 for F in hf)
        regul = all(
            all(2 * c == len(F) for c in abundance(F, n) if c > 0) for F in hf
        )
        boolalg = all(is_block_partition_family(F, n) for F in hf)
        print(f"{n} | {cnt:3} | {exp:3} | {str(cnt==exp):5} | "
              f"{str(pow2):5} | {str(regul):5} | {str(boolalg):5}")

    # |F| distribution vs partial set partitions of a subset of [n] into k blocks
    print("\n|F| distribution (m -> count of half-density families) per n:")
    for n in range(1, 6):
        distr = Counter(len(F) for F in levels[n] if
                        (lambda c: c and max(c) * 2 == len(F))(
                            [c for c in abundance(F, n) if c > 0]))
        print(f"  n={n}: {sorted(distr.items())}")


if __name__ == "__main__":
    main()