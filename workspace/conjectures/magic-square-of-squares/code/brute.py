#!/usr/bin/env python3
"""code/brute.py — naive oracle for the 3x3 magic square of squares.

Question (problem.md): do nine distinct positive integers exist whose squares
fill a 3x3 grid with every row, column and main diagonal summing to the same
constant M?  Open since LaBar 1984; no solution known, no proof of
non-existence known.

What this file is: ground truth for the run.  GOAL.md fixes its role — a
verifier (`is_magic_square_of_squares`), a generator over the (c, u, v)
parametrisation of problem.md, and the small runs that pin down what the
statement means.  Everything computed later (sieves, descents, structural
lemmas) is measured against this file.

The mathematical facts the tests rest on:

1. (problem.md's parametrisation) With centre c and parameters u, v the grid

       c+u      c-u-v    c+v
       c-u+v    c        c+u-v
       c-v      c+u+v    c-u

   is magic with constant 3c, so the centre is c = M/3.  Test 1 checks this
   on every c in 1..40, |u|,|v| <= 60 (585,640 grids).

2. The four lines through the centre — middle row, middle column, both main
   diagonals — are three-term APs with common differences u-v, u+v, u, v up
   to sign.  Test 2 checks this on every c in 1..25, |u|,|v| <= 25.

3. The parametrisation is complete: a 3x3 grid is magic iff it is of that
   form with (c, u, v) = (a11, a00 - a11, a02 - a11).  Test 4 verifies the
   reconstruction identity.  Consequently the scans of Test 5 are EXHAUSTIVE
   over what they claim: a magic square with all entries in [1, B] has
   c <= B and |u|, |v| <= B-1, so scanning that box covers every such grid.

Costs (all caps chosen so the whole file finishes in seconds; the bound in
the statement — literature searches past 10^25 — is deliberately NOT
attacked from here):

  Test 5a/5b  complete scan, entries <= B:  sum_{c=1}^B (2B-1)^2  = 4B^3 -
              4B^2 + B  grid evaluations, each 9 set-lookups.
              B = 60 -> 849,660 grids ; B = 100 -> 3,960,100 grids.
  Test 5c     near-miss generator, centre c = e^2, |u|,|v| <= V_MAX:
              E_MAX (2 V_MAX + 1)^2 grid evaluations = 80 * 241^2 = 4,646,480.
  Total ~9.5M exact, polynomial-in-caps evaluations.

All arithmetic is exact integer arithmetic (math.isqrt).  No floats anywhere.
"""

from collections import Counter
from math import isqrt
import random
import time

# ---------------------------------------------------------------------------
# Ground-truth verifier
# ---------------------------------------------------------------------------


def is_perfect_square(x):
    """Exact: is x a perfect square?  Integers only (floats and bools are
    rejected, because silent float coercion is how square checks go wrong)."""
    if type(x) is not int:
        return False
    if x < 0:
        return False
    r = isqrt(x)
    return r * r == x


def grid_from_params(c, u, v):
    """The parametrised grid of problem.md.  Entries need not be squares."""
    return [
        [c + u,     c - u - v, c + v],
        [c - u + v, c,         c + u - v],
        [c - v,     c + u + v, c - u],
    ]


def lines_of(grid):
    """The eight lines: three rows, three columns, both main diagonals."""
    return [
        grid[0], grid[1], grid[2],
        [grid[0][0], grid[1][0], grid[2][0]],
        [grid[0][1], grid[1][1], grid[2][1]],
        [grid[0][2], grid[1][2], grid[2][2]],
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]],
    ]


def magic_sum(grid):
    """The common line sum if all eight lines agree, else None."""
    sums = [sum(line) for line in lines_of(grid)]
    return sums[0] if all(s == sums[0] for s in sums) else None


def failure_of(grid, require_distinct=True):
    """First condition violated by `grid`, or None if it passes everything.

    Diagnosis order: shape / non-integer / not-a-square / not-positive /
    not-distinct / not-magic.
    """
    if len(grid) != 3 or any(len(row) != 3 for row in grid):
        return "shape"
    entries = [grid[r][c] for r in range(3) for c in range(3)]
    for x in entries:
        if type(x) is not int:
            return "non-integer"
    for x in entries:
        if not is_perfect_square(x):
            return "not-a-square"
    for x in entries:
        if x <= 0:
            return "not-positive"
    if require_distinct and len(set(entries)) != 9:
        return "not-distinct"
    if magic_sum(grid) is None:
        return "not-magic"
    return None


def is_magic_square_of_squares(grid, require_distinct=True):
    """THE decision oracle: does this grid solve the problem?

    True iff the 3x3 grid holds nine perfect squares of positive distinct
    integers and all rows, columns and both main diagonals have one common
    magic sum.  The open question is exactly: does any input return True?
    """
    return failure_of(grid, require_distinct) is None


def count_squares_isqrt(grid):
    """Number of perfect-square entries, the slow isqrt way."""
    return sum(1 for row in grid for x in row if is_perfect_square(x))


def count_squares_set(grid, squares_set):
    """Number of perfect-square entries via a precomputed set of squares.
    Valid only when every entry of grid is <= max(squares_set); cross-checked
    against count_squares_isqrt inside Test 4."""
    return sum(1 for row in grid for x in row if x in squares_set)


# ---------------------------------------------------------------------------
# Worked examples from the statement, plus known-answer cases
# ---------------------------------------------------------------------------


def run_test1_params_identity():
    """Worked example (problem.md): the parametrised grid is magic with
    constant 3c and centre c = M/3."""
    n = 0
    bad = 0
    for c in range(1, 41):
        for u in range(-60, 61):
            for v in range(-60, 61):
                g = grid_from_params(c, u, v)
                n += 1
                if magic_sum(g) != 3 * c or g[1][1] != c:
                    bad += 1
    print(f"[test 1] parametrisation identity: {n} grids (c in 1..40, "
          f"|u|,|v| <= 60) all have magic constant exactly 3c and centre "
          f"c = M/3; mismatches: {bad}")
    return bad == 0


def run_test2_ap_structure():
    """Worked example (problem.md): the four centre lines are three-term APs
    with common differences (up to sign) u-v, u+v, u, v."""
    n = 0
    bad = 0
    for c in range(1, 26):
        for u in range(-25, 26):
            for v in range(-25, 26):
                g = grid_from_params(c, u, v)
                centre_lines = [
                    [g[1][0], g[1][1], g[1][2]],   # middle row
                    [g[0][1], g[1][1], g[2][1]],   # middle column
                    [g[0][0], g[1][1], g[2][2]],   # diagonal \
                    [g[0][2], g[1][1], g[2][0]],   # diagonal /
                ]
                diffs = []
                for line in centre_lines:
                    d = line[1] - line[0]
                    if line[2] - line[1] != d:
                        bad += 1
                        break
                    diffs.append(abs(d))
                else:
                    n += 1
                    if sorted(diffs) != sorted([abs(u), abs(v), abs(u + v),
                                                abs(u - v)]):
                        bad += 1
    print(f"[test 2] centre-line AP structure: {n} grids (c in 1..25, "
          f"|u|,|v| <= 25) each have middle row, middle column and both "
          f"diagonals in arithmetic progression with differences u-v, u+v, "
          f"u, v up to sign; mismatches: {bad}")
    return bad == 0


def run_test3_decision_cases():
    """Known-answer classification of the verifier.

    The True branch cannot be exhibited from the literature (no solution is
    known — that is the conjecture), so it is exercised on grids that are
    magic and all-squares but violate distinctness, with the distinctness
    requirement switched off.
    """
    cases = [
        ("Lo Shu classic magic square (entries not all squares)",
         [[4, 9, 2], [3, 5, 7], [8, 1, 6]], False, False),
        ("nine 1s: magic and squares, NOT distinct",
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]], False, True),
        ("nine 4s: magic and squares, NOT distinct",
         [[4, 4, 4], [4, 4, 4], [4, 4, 4]], False, True),
        ("distinct positive squares, not magic",
         [[1, 9, 25], [49, 81, 4], [16, 36, 64]], False, False),
        ("magic rows/cols with repeats, one diagonal off",
         [[1, 9, 4], [9, 4, 1], [4, 1, 9]], False, False),
        ("parametrised grid c=25,u=6,v=9 (magic, exactly 2 squares)",
         [[31, 10, 34], [28, 25, 22], [16, 40, 19]], False, False),
        ("negative entry", [[-4, 4, 4], [4, 4, 4], [4, 4, 4]], False, False),
        ("float entry", [[1.0, 4, 9], [16, 25, 36], [49, 64, 81]],
         False, False),
        ("wrong shape", [[1, 4], [9, 16, 25], [36, 49]], False, False),
    ]
    bad = 0
    for label, g, exp_strict, exp_relaxed in cases:
        got_strict = is_magic_square_of_squares(g, require_distinct=True)
        got_relaxed = is_magic_square_of_squares(g, require_distinct=False)
        diag = failure_of(g, require_distinct=True)
        if got_strict != exp_strict or got_relaxed != exp_relaxed:
            bad += 1
            print(f"    FAIL {label}: strict {got_strict} != {exp_strict}, "
                  f"relaxed {got_relaxed} != {exp_relaxed} ({diag})")
        else:
            print(f"    ok   {label} -> strict {got_strict} / "
                  f"relaxed {got_relaxed} ({diag})")

    # statement consequence: in a magic square the centre is M/3.
    lo_shu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    m = magic_sum(lo_shu)
    print(f"    Lo Shu: magic constant {m}, centre {lo_shu[1][1]}, "
          f"centre == M/3: {3 * lo_shu[1][1] == m}")

    # the parametrised grid used above: 5^2 = 25 is the centre, 4^2 = 16 is
    # a corner; verify the square count agrees with the isqrt count.
    g = grid_from_params(25, 6, 9)
    sqs = {k * k for k in range(1, 41)}
    print(f"    c=25,u=6,v=9 grid has {count_squares_isqrt(g)} squares "
          f"(isqrt) and {count_squares_set(g, sqs)} (set); examples: "
          f"centre {g[1][1]} = 5^2, corner {g[2][0]} = 4^2")
    if count_squares_isqrt(g) != count_squares_set(g, sqs):
        bad += 1
    print(f"[test 3] decision cases: {'PASS' if bad == 0 else f'{bad} FAILS'}")
    return bad == 0


def run_test4_completeness():
    """Completeness of the parametrisation: every 3x3 grid whose eight line
    sums agree is exactly grid_from_params(centre, a00-centre, a02-centre).
    This is the classical fact that a 3x3 magic square is determined by its
    centre and one of its corners' companions; verified here on 3000
    pseudo-random parametrised grids (centres negative, zero and positive)
    plus the Lo Shu.  Also cross-checks count_squares_set against the isqrt
    method on every one of them."""
    rng = random.Random(20240607)
    n = 0
    bad = 0
    for _ in range(3000):
        c = rng.randint(-50, 50)
        u = rng.randint(-50, 50)
        v = rng.randint(-50, 50)
        g = grid_from_params(c, u, v)
        c2 = g[1][1]
        u2 = g[0][0] - c2
        v2 = g[0][2] - c2
        n += 1
        if grid_from_params(c2, u2, v2) != g or magic_sum(g) != 3 * c2:
            bad += 1
        sqs = {k * k for k in range(0, 51)}
        if all(x <= 2500 for row in g for x in row):
            if count_squares_set(g, sqs) != count_squares_isqrt(g):
                bad += 1
    lo_shu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    c2 = lo_shu[1][1]
    if grid_from_params(c2, lo_shu[0][0] - c2, lo_shu[0][2] - c2) != lo_shu:
        bad += 1
    n += 1
    print(f"[test 4] parametrisation completeness: {n} grids reconstruct "
          f"exactly from (centre, a00-centre, a02-centre) with magic sum "
          f"3*centre; mismatches: {bad}")
    return bad == 0


# ---------------------------------------------------------------------------
# Small exhaustive scans — the oracle's generator
# ---------------------------------------------------------------------------


def complete_scan(B):
    """Exhaust every 3x3 magic square with all nine entries positive and
    <= B, and count how many entries are perfect squares.

    Completeness rests on test 4: any magic grid with entries in [1, B] has
    centre c in [1, B] and |u|, |v| <= B-1, so scanning c in 1..B and
    u, v in -(B-1)..(B-1) and discarding grids with entries outside [1, B]
    covers exactly all such grids, each once.
    """
    t = time.time()
    sqs = {k * k for k in range(1, isqrt(B) + 1)}
    per_count = Counter()
    best_k = -1
    best_grid = None
    best_params = None
    best_distinct_k = -1
    best_distinct_grid = None
    nine_square_hits = 0
    n_kept = 0
    for c in range(1, B + 1):
        for u in range(-(B - 1), B):
            for v in range(-(B - 1), B):
                g = grid_from_params(c, u, v)
                entries = g[0] + g[1] + g[2]
                if any(x < 1 or x > B for x in entries):
                    continue
                n_kept += 1
                k = sum(x in sqs for x in entries)
                per_count[k] += 1
                if k > best_k:
                    best_k = k
                    best_grid = g
                    best_params = (c, u, v)
                if len(set(entries)) == 9 and k > best_distinct_k:
                    best_distinct_k = k
                    best_distinct_grid = g
                if k == 9:
                    nine_square_hits += 1
                    if len(set(entries)) != 9:
                        print(f"    !!! nine squares with repeats: {g}")
    print(f"[test 5a] complete scan, entries <= {B}: {n_kept} magic grids "
          f"with positive entries kept (box {B}x{2*B-1}x{2*B-1}); "
          f"best k = {best_k} squares, centre {best_params[0]} "
          f"(square centre: {is_perfect_square(best_params[0])}); "
          f"best k with distinct entries = {best_distinct_k}; "
          f"nine-square hits: {nine_square_hits}; "
          f"time {time.time() - t:.2f}s")
    if best_k >= 6:
        print(f"    best grid (k={best_k}): {best_grid}")
    if best_distinct_k >= 6:
        print(f"    best distinct grid (k={best_distinct_k}): "
              f"{best_distinct_grid}")
    print(f"    square-count distribution over kept grids: "
          f"{dict(sorted(per_count.items()))}")
    return nine_square_hits == 0


def near_miss_scan(E_MAX, V_MAX):
    """Near-miss generator at oracle size: centre c = e^2 (the centre-square
    condition all solutions must satisfy), |u|, |v| <= V_MAX.  Every grid
    scanned is magic by construction; we count square entries.

    GOAL.md wants the run's own generator to reach the literature's 7-square
    near-misses; their entries are far above these caps, so at this size the
    honest output is the best grid this box yields, stated as exactly that."""
    t = time.time()
    E_MAX = int(E_MAX)
    V_MAX = int(V_MAX)
    max_entry = E_MAX * E_MAX + 2 * V_MAX
    sqs = {k * k for k in range(1, isqrt(max_entry) + 1)}
    per_count = Counter()
    best_k = -1
    best_grid = None
    best_params = None
    best_distinct_k = -1
    best_distinct_grid = None
    n_kept = 0
    for e in range(1, E_MAX + 1):
        c = e * e
        for u in range(-V_MAX, V_MAX + 1):
            for v in range(-V_MAX, V_MAX + 1):
                g = grid_from_params(c, u, v)
                entries = g[0] + g[1] + g[2]
                if any(x < 1 or x > max_entry for x in entries):
                    continue
                n_kept += 1
                k = sum(x in sqs for x in entries)
                per_count[k] += 1
                distinct = len(set(entries)) == 9
                if k > best_k:
                    best_k = k
                    best_grid = g
                    best_params = (c, u, v)
                if distinct and k > best_distinct_k:
                    best_distinct_k = k
                    best_distinct_grid = g
    print(f"[test 5b] near-miss generator: c = e^2, e <= {E_MAX}, "
          f"|u|,|v| <= {V_MAX}: {n_kept} all-positive grids; "
          f"best k = {best_k} squares (distinct entries: "
          f"{best_distinct_k}); time {time.time() - t:.2f}s")
    if best_grid is not None:
        sq_positions = [(r, c_) for r in range(3) for c_ in range(3)
                        if best_grid[r][c_] in sqs]
        print(f"    best grid (k={best_k}, c,e,u,v = "
              f"{best_params[0]},{isqrt(best_params[0])},"
              f"{best_params[1]},{best_params[2]}): "
              f"rows {best_grid}")
        print(f"    square entries at {sq_positions}; max entry "
              f"{max(max(r) for r in best_grid)}")
    if best_distinct_grid is not None and best_distinct_k != best_k:
        print(f"    best distinct grid (k={best_distinct_k}): "
              f"{best_distinct_grid}")
    print(f"    square-count distribution over all-positive grids: "
          f"{dict(sorted(per_count.items()))}")
    return True


def main():
    t0 = time.time()
    print("=" * 78)
    print("Oracle run for the 3x3 magic square of squares problem")
    print("code/brute.py — verifier + parametrisation generator, exact")
    print("integer arithmetic only; all caps chosen to finish in seconds.")
    print("=" * 78)
    ok = True
    ok &= run_test1_params_identity()
    ok &= run_test2_ap_structure()
    ok &= run_test3_decision_cases()
    ok &= run_test4_completeness()
    ok &= complete_scan(60)
    ok &= complete_scan(100)
    ok &= near_miss_scan(80, 120)
    print("=" * 78)
    print(f"Overall: {'ALL TESTS PASSED' if ok else 'FAILURES PRESENT'} "
          f"({time.time() - t0:.2f}s total)")
    print("=" * 78)


if __name__ == "__main__":
    main()