#!/usr/bin/env python3
"""CORRECT refuter verifier for R-uc-upper-semimodular.

The lattice/Poonen form: every finite lattice L is order-isomorphic to a family
of subsets of J(L) (its join-irreducibles) closed under INTERSECTION (meet),
containing 0 (empty) and [m] (top).  A finite intersection-closed family with a
top element is a lattice: meet = intersection, join = intersection of all
common upper bounds (finite, nonempty since top is in it).

Upper semimodular (finite): for all a,b with a,b both covering a^b and
a ≠ b, a∨b covers both a and b.

UC (lattice form): some nonzero join-irreducible j has
#{x : j ≤ x} ≤ |L|/2.

A counterexample = an upper semimodular lattice with no such j.

SCALE FACT: any counterexample to this rung is a counterexample to UC itself;
the run's verified bounds give ground set (here = |J(L)| = m) ≥ 13 and
|L| ≥ 51.  Brute force cannot reach that.  This script checks the small fringe
(m ≤ 4) with a CORRECT (intersection-closed) enumeration and reports exactly
what sizes were covered.
"""

from itertools import combinations


def enumerate_lattices(m):
    """All set-systems on [m] closed under intersection, containing 0 and [m].
    Each is a frozenset of int bitmasks.  This is a finite (meet) lattice."""
    full = (1 << m) - 1
    results = []

    def inters_closed(fam, newset):
        for s in fam:
            if (s & newset) not in fam:
                return False
        return True

    def dfs(fam):
        results.append(frozenset(fam))
        # try to add any not-present mask
        candidates = [x for x in range(1 << m) if x not in fam]
        for mask in candidates:
            if inters_closed(fam, mask):
                nf = set(fam)
                nf.add(mask)
                dfs(frozenset(nf))
    dfs(frozenset([0, full]))
    return results


def _covers(fam, a, b):
    """a is covered by b (a strict below b, nothing between)."""
    if (a & ~b) != 0 or a == b:
        return False
    for x in fam:
        if x == a or x == b:
            continue
        if (a & ~x) == 0 and (x & ~b) == 0:
            return False
    return True


def upper_semimodular(fam):
    faml = list(fam)
    for a in faml:
        for b in faml:
            if a == b:
                continue
            ab = a & b
            if _covers(fam, ab, a) and _covers(fam, ab, b):
                aj = a | b
                # join = meet of common upper bounds; in an intersection-closed
                # family that IS the intersection of the upsets, which contains
                # a|b; but the lattice join is the intersection of all members
                # containing both, = the intersection of {c in fam: c⊇a and c⊇b}.
                join = full_of(fam)  # recompute below
                upper = [c for c in fam if (a & ~c) == 0 and (b & ~c) == 0]
                join = upper[0]
                for c in upper[1:]:
                    join = join & c
                if not (_covers(fam, a, join) and _covers(fam, b, join)):
                    return False
    return True


def full_of(fam):
    # top = intersection of all members (nonempty), or just the max
    return max(fam, key=lambda x: x.bit_count())


def join_irreducibles(fam):
    out = []
    for x in fam:
        if x == 0:
            continue
        covers = [y for y in fam if _covers(fam, y, x)]
        if len(covers) == 1:
            out.append(x)
    return out


def uc_holds(fam):
    L = len(fam)
    if L < 2:
        return True, None
    for j in join_irreducibles(fam):
        above = sum(1 for x in fam if (j & ~x) == 0)
        if 2 * above <= L:
            return True, j
    return False, None


def run(m_max):
    for m in range(1, m_max + 1):
        latts = enumerate_lattices(m)
        usm = 0
        viol = []
        for fam in latts:
            if upper_semimodular(fam):
                usm += 1
                ok, j = uc_holds(fam)
                if not ok:
                    viol.append(fam)
        print(f"m={m}: {len(latts)} set-system lattices, {usm} upper semimodular, "
              f"{len(viol)} UC violations")
        for v in viol[:3]:
            print("   VIOLATION:", [bin(x) for x in v])


if __name__ == "__main__":
    run(4)
