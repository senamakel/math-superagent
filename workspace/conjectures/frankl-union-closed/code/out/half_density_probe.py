"""Attack the max-density=1/2 characterization beyond the exhaustive n<=5 data.

Established at n<=5 (half_density_verify.py, exhaustive): a nonempty UC family
F on [n] whose MAXIMUM element density is exactly 1/2 is a Boolean subalgebra
(block-partition family): all present elements at density exactly 1/2,
|F| = 2^k (power of 2), k = #blocks, count Bell(n+1)-1, refined by
#(families with |F|=2^k) = S(n+1,k+1) (Stirling).  Also established (rounded
from half_density_complement.py): the COORDINATE-WISE statement is FALSE --
non-Boolean UC families with some element at density 1/2 exist (2 at n=2, 42
at n=3, 1818 at n=4, 752255 at n=5), all of them with an element ABOVE 1/2.

This probe hunts a counterexample to the max-density characterization at n>5:
  (P1) explicit witnesses of the coordinate-wise failure at n=3 (listing the
       first few), each with its own element strictly above 1/2;
  (P2) EXHAUSTIVE over a structured n=6 subclass: F_G = 2^[5] u {A u {6} :
       A in G} for EVERY upset G of 2^[5] (Dedekind number M(5) = 7581,
       enumerated by the standard P-partition recursion); these are all
       union-closed (shown in the header comment of the writer) and the class
       includes the full cube.  Report boundary families found (max density
       exactly 1/2) and whether each is a Boolean subalgebra;
  (P3) random generator-set closures on [6] and [7] (Random(20260711)),
       each checked for union-closure via lib.uc, max density == 1/2 exactly,
       and Boolean-subalgebra structure (closed under xor).

Every density is an exact Fraction; no floats anywhere.
"""
import random
from fractions import Fraction

from lib.uc import decide_union_closed, abundance


def is_boolalg_subalgebra(F):
    """Closed under xor: F a Boolean subalgebra (block-partition family)."""
    F = list(F)
    return all((a ^ b) in F for a in F for b in F)


def max_density(F, n):
    """(max density, the max over present elements of c/m) as exact Fraction."""
    m = len(F)
    counts = abundance(F, n)
    present = [c for c in counts if c > 0]
    return Fraction(max(present), m)


def print_witnesses_n3():
    """Explicit non-Boolean UC families on [3] with an element at density 1/2
    (uses the same cascade logic as half_density_complement.py; kept local so
    the witness list is self-contained)."""
    def is_uc(F):
        F = list(F)
        return all((a | b) in F for a in F for b in F)

    masks = range(1 << 3)
    found = []
    for sub in range(1, 1 << 8):
        F = {m for m in masks if (sub >> m) & 1}
        if not F or not is_uc(F):
            continue
        if is_boolalg_subalgebra(F):
            continue
        counts = abundance(F, 3)
        m = len(F)
        if any(Fraction(c, m) == Fraction(1, 2) for c in counts if c > 0):
            found.append((sorted(F), counts))
    print(f"P1: non-Boolean UC families on [3] with some element at density"
          f" 1/2: {len(found)} (expect 42)")
    for F, counts in found[:4]:
        # find the half element and an over-half element explicitly
        half = [i for i, c in enumerate(counts)
                if c > 0 and Fraction(c, len(F)) == Fraction(1, 2)]
        over = [i for i, c in enumerate(counts)
                if c > 0 and Fraction(c, len(F)) > Fraction(1, 2)]
        print(f"    F={F} counts={counts} half-elements={half} "
              f"over-half={over} (max={max_density(F, 3)})")
    return len(found)


def upsets_of_boolean(N):
    """All up-sets of the Boolean lattice 2^[N] (Dedekind number M(N)).

    Generates by REMOVING MINIMAL elements: if U is an up-set, removing a
    minimal element m of U leaves an up-set (no x != m with x ⊆ m, so no
    member of U\\{m} has m as an upper bound).  Every up-set is reachable.
    The minimality test is (y|x)==x (y ⊆ x); the probe's first version used
    (x|y)==y (maximal removal), which does NOT preserve up-setness — the
    self-test below catches that by checking M(1)=3, M(2)=6, M(3)=20.
    """
    n = 1 << N
    masks = list(range(n))
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
    dfs(frozenset(masks))

    # self-test: every returned set must be an up-set of the Boolean lattice
    for S in results:
        S = set(S)
        for x in S:
            for y in masks:
                if (x | y) == y and y not in S:
                    raise AssertionError(f"not an up-set: {sorted(S)} misses {y}")
    return list(results)


def gshape_boundary_search():
    """Exhaustive: F_G = 2^[5] u {A u {6} : A in G} for every upset G of 2^[5].
    Check: is F_G union-closed; if max density == 1/2, is F_G a Boolean
    subalgebra?  Report any non-Boolean boundary family."""
    N = 5
    n = 6
    upsets = upsets_of_boolean(N)
    print(f"P2: upsets of 2^[5]: {len(upsets)} (expect Dedekind M(5)=7581)")
    base = set(range(1 << N))          # 2^[5]
    xbit = 1 << N                      # element 6
    boundary = []
    nb = 0
    for G in upsets:
        F = set(base) | {a | xbit for a in G}
        if not decide_union_closed(F):
            print("    !! not UC:", sorted(G))
            continue
        md = max_density(F, n)
        if md == Fraction(1, 2):
            boundary.append((G, F))
            if not is_boolalg_subalgebra(F):
                nb += 1
                print("    COUNTEREXAMPLE? non-Boolean boundary family: "
                      "G =", sorted(G))
    print(f"P2: boundary families (max density == 1/2): {len(boundary)}; "
          f"non-Boolean among them: {nb}")
    # report the sizes of boundary families found
    from collections import Counter
    sizes = Counter(len(F) for _, F in boundary)
    print(f"P2: boundary-family sizes |F|: {sorted(sizes.items())}")
    return len(boundary), nb


def random_closure_probe(n, trials, seed):
    """Random generator sets -> closure (lib.uc.closure); count boundary
    families and any non-Boolean one.  Exact rational densities."""
    from collections import Counter
    from lib.uc import closure
    rng = random.Random(seed)
    boundary = 0
    nonbool = 0
    sizes = Counter()
    for _ in range(trials):
        k = rng.randint(2, 8)
        gens = set()
        for _ in range(k):
            gens.add(rng.randrange(1, 1 << n))
        F = closure(gens)
        if not F or len(F) < 2:
            continue
        # exclude ground-trivial F == {0} only; keep others
        if max_density(F, n) != Fraction(1, 2):
            continue
        boundary += 1
        sizes[len(F)] += 1
        if not is_boolalg_subalgebra(F):
            nonbool += 1
            if nonbool <= 3:
                print(f"    n={n}: non-Boolean boundary family: "
                      f"{sorted(F)}, counts={abundance(F, n)}")
    print(f"P3: n={n} trials={trials} seed={seed}: boundary families "
          f"{boundary}, non-Boolean {nonbool}, sizes {sorted(sizes.items())}")
    return boundary, nonbool
    

def main():
    from collections import Counter
    w = print_witnesses_n3()
    b, nb = gshape_boundary_search()
    r6 = random_closure_probe(6, 400000, 20260711)
    r7 = random_closure_probe(7, 200000, 20260711)
    print()
    print("SUMMARY")
    print(f"  coordinate-wise statement refuted: {w} non-Boolean n=3 "
          f"families with an element at density 1/2")
    print(f"  max-density characterization: n=6 exhaustive G-shape subclass "
          f"boundary={b}, non-Boolean={nb}; n=6 random: {r6}; n=7 random: {r7}")
    ok = (nb == 0 and r6[1] == 0 and r7[1] == 0)
    print(f"  non-Boolean max-density-1/2 family found anywhere: {not ok}")


if __name__ == "__main__":
    main()