#!/usr/bin/env python3
"""Refuter verifier for the R-uc-upper-semimodular rung.

Statement attacked (lattice / Poonen form of Frankl's conjecture restricted to
upper semimodular lattices):

  Every finite upper semimodular lattice L with |L| >= 2 has a nonzero
  join-irreducible j with #{x in L : j <= x} <= |L|/2.

This is OPEN in general.  A counterexample would be an upper semimodular
lattice with NO join-irreducible below at most half its elements.

Every finite lattice is isomorphic to a family of subsets of its
join-irreducibles closed under union and intersection (Birkhoff: x -> {j in
J(L): j<=x}; the image is closed under union=join and intersection=meet and
contains empty and full set).  So to enumerate all finite lattices with m
join-irreducibles we enumerate set-systems on [m] closed under both union and
intersection, containing the empty set and [m]; the lattice order is inclusion,
join = union, meet = intersection, |L| = #sets, join-irreducibles = sets with a
unique maximal proper subset in the family, and join-irreducible j is "below at
most half the elements" iff #{x : x superset j} <= |L|/2.

Upper semimodularity: a finite lattice is upper semimodular iff for all a,b
distinct with both a and b covering their meet a^b, the join avb covers both a
and b.  Equivalently: for every element c and every pair a,b both covering c
with avb != c, avb covers a and avb covers b.  (Standard characterization for
finite lattices.)

EXACT integer arithmetic throughout.  This is a brute-force oracle over small
m (number of join-irreducibles); complexity is worst-case but the bounds kept
small, mirroring the verified ranges (UC is already known for |F|<=50 and
ground set n<=12, so any counterexample has m>=13 and |L|>=51 -- far above what
exhaustive enumeration reaches here).
"""

from itertools import combinations


def set_systems_closed(m):
    """Enumerate all families of subsets of [m] closed under union and
    intersection, containing the empty set and the full set [m].
    Each family is a frozenset of frozensets (subsets as bitmasks ints)."""
    full = (1 << m) - 1
    all_masks = list(range(1 << m))
    results = []
    # A lattice of sets must contain 0 and full.  Recursively add sets such
    # that closure under intersection/union is preserved.
    must_contain = {0, full}

    def closed_with(newset, fam):
        # check adding newset keeps union&intersection closure
        for s in fam:
            if (s | newset) not in fam and (s | newset) != newset:
                pass
            if (s & newset) not in fam and (s & newset) != newset:
                pass
        # need the closure test against the *current* fam including possible
        # new pairs; do a full closure check when a family is complete instead.
        return True

    def dfs(fam, idx):
        results.append(frozenset(fam))
        for i in range(idx, 1 << m):
            mask = all_masks[i]
            if mask in fam:
                continue
            new = set(fam)
            new.add(mask)
            # check closure of new with existing members
            bad = False
            for a in fam:
                if (a | mask) not in new or (a & mask) not in new:
                    bad = True
                    break
            if bad:
                continue
            dfs(new, i + 1)

    dfs(must_contain, 0)
    return results


def covers_relation(fam, a, b):
    """True if a is covered by b (a<b and no c strictly between)."""
    if not (a & ~b) == 0:  # a subset of b
        return False
    if a == b:
        return False
    for x in fam:
        # a < x < b
        if (a & ~x) == 0 and (x & ~b) == 0 and x != a and x != b:
            return False
    return True


def upper_semimodular(fam):
    """Finite lattice upper semimodular iff: for all a,b in fam with a^b
    covered by both a and b (a,b distinct), avb covers both a and b."""
    faml = list(fam)
    for a in faml:
        for b in faml:
            if a == b:
                continue
            ab = a & b
            if covers_relation(fam, ab, a) and covers_relation(fam, ab, b):
                aj = a | b
                if aj in fam:
                    if not (covers_relation(fam, a, aj) and covers_relation(fam, b, aj)):
                        return False
                # aj must be in fam since closed under union
    return True


def join_irreducibles(fam):
    """Join-irreducibles = nonempty sets (in fam) with a unique maximal proper
    subset in fam (and not the empty set)."""
    out = []
    faml = list(fam)
    for x in faml:
        if x == 0:
            continue
        covers = [y for y in faml if covers_relation(fam, y, x)]
        if len(covers) == 1:
            out.append(x)
    return out


def uc_holds_lattice(fam):
    """Lattice-form UC: some nonzero join-irreducible j with
    #{x in fam : j subset x} <= |L|/2."""
    L = len(fam)
    if L < 2:
        return True, None
    for j in join_irreducibles(fam):
        above = sum(1 for x in fam if (j & ~x) == 0)
        if 2 * above <= L:
            return True, j
    return False, None


def small_known_examples():
    """Hand-check degenerate cases and a few named upper semimodular lattices.

    - |L|=2: the two-element chain (B2 or C2).  Join-irreducible = the top
      element; it is above only itself -> 1 <= |L|/2=1.  Holds.
    - The diamond M3 (Boolean algebra B2 with a middle element): upper
      semimodular (indeed modular).  Join-irreducibles are the two atoms, each
      above itself and the top but not the middle -> count 2 <= |L|/2=2. Holds.
    - A small non-modular upper semimodular lattice would be the interesting
      one; brute force over m<=4 hunts it below.
    """
    results = {}
    # two-element chain as a family {empty, {0}}: elements = bit 0 = atom
    fam2 = frozenset([0, 1])
    ok, j = uc_holds_lattice(fam2)
    results['2-chain'] = (ok, j, upper_semimodular(fam2))
    # 3-element chain 0 < a < 1: {0},{0,1},{0,1,2}? let's do subsets {},{a},{a,b}
    fam3 = frozenset([0, 1, 3])
    ok, j = uc_holds_lattice(fam3)
    results['3-chain(U 3-elt set)'] = (ok, j, upper_semimodular(fam3))
    # M3 diamond: elements {},{a},{b},{a,b} plus a middle {x}: 5 elements
    # as subsets of {0,1,2}: 0={}, A={0},B={1}, top={0,1}, middle={2}
    fam5 = frozenset([0, 1, 2, 7, 4])  # 0,{0},{1},{0,1},{2}
    ok, j = uc_holds_lattice(fam5)
    results['M3-diamond'] = (ok, j, upper_semimodular(fam5))
    return results


def brute_force(m_max):
    total = 0
    upper_sm_count = 0
    violations = []
    for m in range(2, m_max + 1):
        for fam in set_systems_closed(m):
            total += 1
            if not upper_semimodular(fam):
                continue
            upper_sm_count += 1
            ok, j = uc_holds_lattice(fam)
            if not ok:
                violations.append((m, fam))
    return total, upper_sm_count, violations


if __name__ == "__main__":
    print("=== hand-check degenerate / known examples ===")
    for name, (ok, j, usm) in small_known_examples().items():
        print(f"  {name:16s} UC={ok}  upper_semimodular={usm}")
    print()
    for m_max in (2, 3, 4):
        total, usm, viol = brute_force(m_max)
        print(f"m<={m_max}: {total} lattices-of-sets total, {usm} upper "
              f"semimodular, {len(viol)} UC violations")
        for v in viol[:5]:
            print("    VIOLATION:", v)
