"""Naive oracle for Frankl's union-closed sets conjecture.

Obviously correct, exact integer arithmetic. A family is a set of bitmasks over
ground set [n]: set s is a row of bits, bit i == 1 means element i (0-indexed)
is in s. Element abundance is an exact integer count.

This file exists to pin down what the statement MEANS. It is the oracle that
every faster method is later checked against. It is deliberately not fast.

Functions
---------
is_union_closed(fam)      -> bool
abundance(fam, n)         -> list[int]  exact counts per element
abundant_elements(fam, n) -> list[int]  elements in >= |fam|/2 sets
powerset(n)               -> frozenset[int]  the family 2^[n]
guard_tests()             -> runs the guards from problem.md, prints results
"""


def is_union_closed(fam):
    """Exact test: for all A, B in fam, A | B is in fam."""
    for a in fam:
        for b in fam:
            if (a | b) not in fam:
                return False
    return True


def abundance(fam, n):
    """Exact integer count, per element, of how many sets contain it."""
    counts = [0] * n
    for s in fam:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def abundant_elements(fam, n):
    """Elements present in at least |fam|/2 of the sets (exact comparison)."""
    half_num = len(fam)  # compare count * 2 >= len(fam) via count >= len/2
    counts = abundance(fam, n)
    out = []
    for i, c in enumerate(counts):
        # c >= |fam|/2  <=>  2*c >= |fam|
        if 2 * c >= len(fam):
            out.append(i)
    return out


def powerset(n):
    """The family 2^[n]: every subset of [n] as a bitmask."""
    fam = set()
    for mask in range(1 << n):
        fam.add(mask)
    return fam


def guard_tests():
    print("=== GUARD SET (the statement's worked examples) ===\n")

    # (1) Power set 2^[n]: union-closed, every element at density exactly 1/2.
    for n in (0, 1, 2, 3, 4):
        fam = powerset(n)
        uc = is_union_closed(fam)
        counts = abundance(fam, n)
        density_ok = all(2 * c == len(fam) for c in counts)
        print(f"2^[{n}]: |F|={len(fam)}, union-closed={uc}, "
              f"every element exactly half={density_ok}")
        assert uc, "power set must be union-closed"
        assert density_ok, "power set: every density must be exactly 1/2"
    print()

    # (2) A family containing a singleton {x} is union-closed => x abundant.
    #     2^[n] n=2, family = F containing {0} and all sets containing 0.
    #     i.e. the principal filter above {0}, union-closed.
    n = 2
    one = 1 << 0
    fam = {a | one for a in powerset(n)}  # all sets containing element 0
    uc = is_union_closed(fam)
    abund = abundant_elements(fam, n)
    print(f"all sets containing {{0}} (n={n}): |F|={len(fam)}, "
          f"union-closed={uc}, abundant={abund}")
    assert uc
    assert 0 in abund, "singleton {0} forces element 0 abundant"
    print()

    # (3) A family containing a 2-element set {x,y}: union-closed => one of
    #     x,y abundant.  Family = all sets containing {0,1} (principal filter
    #     above a 2-set), plus make it union-closed.
    n = 3
    two = (1 << 0) | (1 << 1)  # {0,1}
    fam = {a | two for a in powerset(n)}
    uc = is_union_closed(fam)
    abund = abundant_elements(fam, n)
    print(f"all sets containing {{0,1}} (n={n}): |F|={len(fam)}, "
          f"union-closed={uc}, abundant={abund}")
    assert uc
    assert (0 in abund) or (1 in abund), "a 2-set forces one of its pts abundant"
    print()

    # (4) A 3-element set does NOT always force abundance. Probe:
    #     principal filter above a 3-set {0,1,2}; check whether any of the 3
    #     is abundant.
    n = 4
    three = (1 << 0) | (1 << 1) | (1 << 2)  # {0,1,2}
    fam = {a | three for a in powerset(n)}
    uc = is_union_closed(fam)
    abund = abundant_elements(fam, n)
    print(f"all sets containing {{0,1,2}} (n={n}): |F|={len(fam)}, "
          f"union-closed={uc}, abundant={abund}")
    assert uc
    # UC still holds here (family is a filter, always has abundant elements),
    # but the three specific elements need not all be abundant.
    assert len(abund) >= 1, "UC must hold; some element is abundant"
    print(f"  (element 0 among the vast: {0 in abund})")
    print()

    # (5) NEGATIVE CONTROL: a NON-union-closed family with NO abundant element
    #     must be constructible, and the closure check must reject it.
    #     3 pairwise-disjoint 3-sets on a 9-element ground set: every element
    #     is in exactly 1 of the 3 sets, and |F|/2 = 1.5, so no element is
    #     abundant (1 < 1.5). Pairwise unions escape the family, so it is not
    #     union-closed. This is the cleanest element-scarce non-UC family:
    #     scarcity here is genuine (no averaging fluke), and it shows the
    #     closure requirement is what UC actually needs.
    n = 9
    fam = {
        0b111,           # {0,1,2}
        0b111000,        # {3,4,5}
        0b111000000,     # {6,7,8}
    }
    uc = is_union_closed(fam)
    abund = abundant_elements(fam, n)
    print(f"antichain (n={n}): |F|={len(fam)}, union-closed={uc}, "
          f"abundant={abund}")
    assert not uc, "this antichain is not union-closed, must be rejected"
    assert len(abund) == 0, "antichain of large sets: no abundant element"
    print("  -> closure check rejected a non-union-closed family; "
          "negative control passes")
    print()

    print("=== ALL GUARD TESTS PASSED ===")


if __name__ == "__main__":
    guard_tests()
