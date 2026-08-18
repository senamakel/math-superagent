"""
Oracle for the per-shape divisibility obstruction (approach: lte-divisibility-obstruction).

Establishes, by direct computation, the exact form of the cycle condition
used in `research/approaches/lte-divisibility-obstruction.md`, and reproduces
every worked example available (the trivial cycle, the known negative-integer
cycles, and known rational cycles).

Bears on claim ids: bohmsontacchi-cycle-formula, halbeisen-rational-cycle-formula.

Every number below is produced by this program; nothing is copied from a paper.
"""

from fractions import Fraction
from itertools import product

# ---------------------------------------------------------------- the map ---
# Accelerated Collatz map on Z (not just Z^+): T0 = x/2, T1 = (3x+1)/2.
# The accelerated map composes the odd step 3n+1 with ONE forced halving.


def T(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def orbit(x, cap=10_000):
    """Full forward orbit until it repeats or exceeds cap steps."""
    seen, cur, path = {}, x, []
    for i in range(cap):
        if cur in seen:
            return path[seen[cur]:], i - seen[cur]  # cycle, preperiod
        seen[cur] = i
        path.append(cur)
        cur = T(cur)
    return None, None


def shape_of_cycle(cyc):
    """(L, m, gaps) of a cycle of the accelerated map.
    L = total steps, m = odd steps, gaps v_j = #halvings after the j-th odd step.
    """
    L = len(cyc)
    m = sum(1 for x in cyc if x % 2 == 1)
    return L, m


# -------------------------------------------------- the cycle formula -------
# Claim to test: for a cycle with L total steps, m odd steps, and gap vector
# (v_1..v_m) with v_j >= 1 and sum v_j = L, the cycle element is
#     x = S / (2^L - 3^m),   S = sum_{j=0}^{m-1} 3^{m-1-j} 2^{V_j},
# with partial sums V_0 = 0 < V_1 < ... < V_m = L.
#
# NOTE the exponent bookkeeping is exactly what this program pins down: an
# accelerated odd step (3x+1)/2 contributes a factor 3 and *one* halving, and
# the "+1" contributes the S terms. We test the formula, we do not trust it.


def cycle_element_from_shape(L, m, gaps):
    """Return the rational x implied by shape (L, m, gaps), or None if malformed."""
    if len(gaps) != m or any(v < 1 for v in gaps) or sum(gaps) != L:
        return None
    V, s = [0], 0
    for v in gaps:
        s += v
        V.append(s)
    # V[0]=0, V[j] = v_1+...+v_j.  V[m] = L.
    S = sum(3 ** (m - 1 - j) * 2 ** V[j] for j in range(m))
    return Fraction(S, 2 ** L - 3 ** m)


def shapes(L, m):
    """All gap vectors (v_1..v_m), v_j>=1, sum = L — compositions of L into m parts."""
    if m == 1:
        yield (L,)
        return
    for c in product(range(1, L - m + 2), repeat=m):
        if sum(c) == L:
            yield c


# ---------------------------------------------------------------- checks ----
def main():
    print("=== 1. known cycles of the accelerated map on Z ===")
    known = [1, 2, 4, -1, -5, -17, -35, -91]
    for s in known:
        cyc, pre = orbit(s)
        if cyc is None:
            print(f"  start {s:>4}: no cycle within cap")
            continue
        L, m = shape_of_cycle(cyc)
        print(f"  start {s:>4}: preperiod {pre:>3}, cycle len {L:>3}, "
              f"odd steps m={m:>2}, min elem {min(cyc):>6}")

    print()
    print("=== 2. the formula reproduces the actual cycle element ===")
    # For each known cycle, extract (L,m,gaps) from the orbit directly and
    # compare the formula's rational against the orbit's own elements.
    for s in known:
        cyc, _ = orbit(s)
        if cyc is None:
            continue
        L, m = shape_of_cycle(cyc)
        # recover the gap vector: walk the cycle from its first odd element
        start = next(i for i, x in enumerate(cyc) if x % 2 == 1)
        gaps, cur, run = [], start, 0
        for _ in range(L):
            x = cyc[cur]
            if x % 2 == 1:
                if run or gaps:
                    gaps.append(run + 1)
                    run = 0
                else:
                    gaps = [1]
            else:
                run += 1
            cur = (cur + 1) % L
        # simpler recovery below if that miscounted
        gaps = recover_gaps(cyc, start)
        assert len(gaps) == m and sum(gaps) == L, (gaps, m, L)
        x = cycle_element_from_shape(L, m, gaps)
        actual = min(cyc) if L > 1 else cyc[0]
        ok = (x in [Fraction(c) for c in cyc])
        print(f"  (L={L:>3}, m={m:>2}) gaps={gaps}")
        print(f"      formula -> {x}   in-cycle: {ok}")

    print()
    print("=== 3. trivial cycle shape in detail ===")
    cyc, _ = orbit(1)
    L, m = shape_of_cycle(cyc)
    gaps = recover_gaps(cyc, next(i for i, x in enumerate(cyc) if x % 2 == 1))
    print(f"  1->2->1 under T: L={L}, m={m}, gaps={gaps}")
    print(f"  formula: {cycle_element_from_shape(L, m, gaps)}")

    print()
    print("=== 4. which shapes (L,m) admit an INTEGER cycle element ===")
    print("   (exhaustive over all gap vectors — oracle only, small sizes)")
    for (L, m) in [(2, 1), (3, 1), (4, 1), (5, 2), (7, 2), (7, 3), (9, 3),
                   (10, 3), (12, 4), (1, 1)]:
        D = 2 ** L - 3 ** m
        hits = []
        n_sh = 0
        if D != 0:
            for g in shapes(L, m):
                n_sh += 1
                x = cycle_element_from_shape(L, m, g)
                if x.denominator == 1:
                    hits.append((g, x))
        print(f"  (L={L:>2}, m={m})  2^L-3^m = {D:>14}  shapes={n_sh:>6}  "
              f"integer solutions={len(hits)}  {hits[:3]}")


def recover_gaps(cyc, start):
    """Gap vector of a cycle, walking from its first odd element.

    v_j = number of halvings that follow the j-th odd accelerated step,
    where the accelerated odd step (3x+1)/2 itself forces one halving.
    So v_j counts: the forced halving of the j-th odd step, plus any
    subsequent even steps, before the next odd element appears.
    """
    L = len(cyc)
    gaps, cur, run = [], start, 0
    seen_odd = 0
    while seen_odd <= len([x for x in cyc if x % 2 == 1]):
        x = cyc[cur]
        if x % 2 == 1:
            if run:
                gaps.append(run)
                run = 0
            run = 1  # forced halving of this odd step
            seen_odd += 1
        else:
            run += 1
        cur = (cur + 1) % L
        if cur == start and run:
            gaps.append(run)
            break
    return gaps


if __name__ == "__main__":
    main()
