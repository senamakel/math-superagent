#!/usr/bin/env python3
"""Verify the G-cupcap characterization (Erdos-Szekeres 1935) exactly.

Claim (G-cupcap): a planar point set X in general position with distinct
x-coordinates contains n points in convex position iff there exist k in {2..n},
a k-cup C and an (n+2-k)-cap D in X that share their leftmost and rightmost
points (by x) and whose union is exactly n points in convex position.

Method (all exact arithmetic, integer coords):
  * is_cup / is_cap from lib.cupcap -- exact Fraction slope comparisons.
  * independent reference is_cup_ref / is_cap_ref recomputed here with Fraction
    from the raw definition, to validate the lib helpers.
  * oracle side: largest_convex_subset(X) >= n  (from lib.es_geom, exact
    hull test).
  * cupcap side: exists_cupcap(X, n)  (from lib.cupcap, exactly as the claim
    states: k-cup + (n+2-k)-cap sharing left and right extremes, union convex).

For EVERY set and EVERY n in 3..|X| we require both directions to agree.  Any
mismatch is reported with full coordinates.

Additionally, shared_extreme_nonconvex_pairs is exercised to show that 'sharing
extremes' alone does NOT force convexity: there are pairs of a cup and cap that
share both x-extremes whose union is n points but not convex, which is exactly
why the claim states the union must be in convex position.

Output is written to code/out/cupcap_verify.txt.
"""
import random
from fractions import Fraction
from itertools import combinations

from lib.cupcap import (
    is_cup,
    is_cap,
    exists_cupcap,
    shared_extreme_nonconvex_pairs,
)
from lib.es_geom import (
    in_general_position,
    largest_convex_subset,
    in_convex_position,
)

random.seed(1935)


# ---------------------------------------------------------------------------
# independent Fraction reference for cup/cap, straight from the definition
# ---------------------------------------------------------------------------

def _ref_slopes(sub):
    pts = sorted(sub, key=lambda p: Fraction(p[0]))
    out = []
    for i in range(len(pts) - 1):
        dx = Fraction(pts[i + 1][0]) - Fraction(pts[i][0])
        assert dx != 0
        out.append((Fraction(pts[i + 1][1]) - Fraction(pts[i][1])) / dx)
    return out


def is_cup_ref(sub):
    sl = _ref_slopes(sub)
    return all(sl[i] < sl[i + 1] for i in range(len(sl) - 1)) if sl else (len(sub) >= 2)


def is_cap_ref(sub):
    sl = _ref_slopes(sub)
    return all(sl[i] > sl[i + 1] for i in range(len(sl) - 1)) if sl else (len(sub) >= 2)


def distinct_x(pts):
    xs = [Fraction(p[0]) for p in pts]
    return len(set(xs)) == len(xs)


# ---------------------------------------------------------------------------
# set generators
# ---------------------------------------------------------------------------

def grid_subsets():
    grid = [(x, y) for x in range(3) for y in range(3)]
    for mask in range(1, 1 << len(grid)):
        sub = [grid[i] for i in range(len(grid)) if mask & (1 << i)]
        yield sub


def random_sets(min_size, max_size, count, coord=6):
    seen = set()
    made = 0
    while made < count:
        n = random.randint(min_size, max_size)
        pts = [(random.randint(0, coord), random.randint(0, coord)) for _ in range(n)]
        key = tuple(sorted(pts))
        if key in seen:
            continue
        seen.add(key)
        yield pts
        made += 1


# ---------------------------------------------------------------------------
# main check
# ---------------------------------------------------------------------------

def run():
    lines = []
    def log(s=""):
        lines.append(str(s))

    log("=" * 78)
    log("G-cupcap verification (Erdos-Szekeres 1935) -- exact arithmetic")
    log("=" * 78)

    total_sets = 0
    total_cases = 0
    agree = 0
    mismatch = []
    lib_ref_bad = []          # is_cup/is_cap disagree with reference
    seen_diag = [0]           # nonzero shared-extreme-nonconvex seen on any set

    for label, sub_iter in [
        ("grid {0,1,2}^2 all subsets", grid_subsets()),
        ("random small sets size 3..8", random_sets(3, 8, 1200, coord=6)),
        ("random small sets size 3..7 (wider coords)", random_sets(3, 7, 600, coord=20)),
    ]:
        used = 0
        for pts in sub_iter:
            # only sets with distinct x and in general position
            if not distinct_x(pts) or not in_general_position(pts):
                continue
            # validate lib cup/cap against reference on every subset
            for r in range(2, len(pts) + 1):
                for combo in combinations(range(len(pts)), r):
                    sub = [pts[i] for i in combo]
                    if is_cup(sub) != is_cup_ref(sub) or is_cap(sub) != is_cap_ref(sub):
                        lib_ref_bad.append((pts, sub))
                        break
            used += 1
            total_sets += 1
            m = len(pts)
            lcs, _ = largest_convex_subset(pts)
            for n in range(3, m + 1):
                total_cases += 1
                oracle = lcs >= n
                cupcap = exists_cupcap(pts, n)
                if oracle == cupcap:
                    agree += 1
                else:
                    mismatch.append((pts, n, oracle, cupcap))
            # diagnostic: does 'sharing extremes' alone fail convexity anywhere?
            for n in range(3, m + 1):
                bad, tot = shared_extreme_nonconvex_pairs(pts, n)
                if bad:
                    seen_diag[0] += 1
                    log(f"  [diag] set {pts} n={n}: {bad} cup/cap pairs share "
                        f"extremes but union of {n} points NOT convex ({tot} total pairs)")
                    break
        log(f"  {label}: {used} valid (general-position, distinct-x) sets")

    log("")
    log(f"sets checked        : {total_sets}")
    log(f"cases (set, n)      : {total_cases}")
    log(f"agreement           : {agree}")
    log(f"mismatches          : {len(mismatch)}")
    log(f"lib-vs-ref cup/cap  : {len(lib_ref_bad)} disagreements on any subset")

    for pts, n, o, cc in mismatch[:10]:
        log(f"  MISMATCH set={pts} n={n} oracle(conv)={o} cupcap={cc}")

    log("")
    log("Diagnostic: a cup and a cap can share both x-extreme points while")
    log("their union (of exactly n points) is NOT convex -- which is why the")
    log("claim states the union must be convex.  Such nonconvex shared-extreme")
    log(f"pairs were observed on {seen_diag[0]} of the sets.")
    log("")

    ok = (len(mismatch) == 0 and len(lib_ref_bad) == 0)
    log(f"RESULT: {'PASS -- characterization holds on every case' if ok else 'FAIL'}")
    return lines, ok


if __name__ == "__main__":
    lines, ok = run()
    text = "\n".join(lines)
    with open("code/out/cupcap_verify.txt", "w") as f:
        f.write(text + "\n")
    print(text)
    print()
    print("wrote code/out/cupcap_verify.txt")
    raise SystemExit(0 if ok else 1)
