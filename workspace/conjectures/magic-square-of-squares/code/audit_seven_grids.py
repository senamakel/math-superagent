#!/usr/bin/env python3
"""Task B: entry-repeat audit of the oracle's four 7-square grids.

code/out/oracle_output.txt test 5b printed only the best k=9 trivial
grid and the best-distinct k=5 grid; the distribution line records
"7: 4" but the four 7-square grids themselves were not printed.  This
script re-runs code/brute.py's near_miss_scan(80, 120) semantics
byte-for-byte and then audits the four k=7 grids.

Scan semantics replicated from brute.py near_miss_scan(E_MAX=80,
V_MAX=120):
  centre c = e^2, e in 1..80, u, v in -120..120;
  keep grids with EVERY entry in [1, MAX_ENTRY], MAX_ENTRY = 80^2+2*120
  = 6640 (the best-possible maximum entry, so nothing is cut);
  square test = membership in {1^2, ..., 81^2} (isqrt(6640) = 81);
  k = number of square entries (centre e^2 always counts).

Reproduction targets (recorded in oracle_output.txt, test 5b):
  kept 4,052,328 grids; distribution {1:3653312, 2:309896, 3:85360,
  4:1952, 5:748, 6:964, 7:4, 9:92} (no k=0, no k=8 kept);
  best k = 9 (all repeated-entry trivial grids), best distinct k = 5.
Every one of these numbers is asserted; if any disagrees, the scan is
not the recorded scan and the audit aborts rather than reporting.

Then for each of the four k=7 grids:
  * the nine entries,
  * pairwise distinctness (repeating values reported explicitly),
  * true magic square (all 8 line sums equal) vs 7-of-8 near-miss
    (the parametrisation makes every grid magic with constant 3c; the
    check is made explicitly anyway, from lines_of),
  * which entries are squares / non-squares, k recounted by isqrt,
and the mutual distinctness of the four grids (identical matrix / same
entry multiset / same entry set / disjoint).

Cross-check (second route): code/extract_sevens.py re-scans the same
box with an independent sieve (isqrt per entry, distinct-only) and must
agree there are no 7-square or 6-square DISTINCT grids; its output is
appended to the audit file by the run command.
"""
from collections import Counter
from math import isqrt

E_MAX, V_MAX = 80, 120
MAX_ENTRY = E_MAX * E_MAX + 2 * V_MAX          # 6640
SQS = {k * k for k in range(1, isqrt(MAX_ENTRY) + 1)}   # 1..81 squares


def grid_from_params(c, u, v):
    return [
        [c + u,     c - u - v, c + v],
        [c - u + v, c,         c + u - v],
        [c - v,     c + u + v, c - u],
    ]


def line_sums(g):
    return [
        sum(g[0]), sum(g[1]), sum(g[2]),
        g[0][0] + g[1][0] + g[2][0], g[0][1] + g[1][1] + g[2][1],
        g[0][2] + g[1][2] + g[2][2],
        g[0][0] + g[1][1] + g[2][2], g[0][2] + g[1][1] + g[2][0],
    ]


def is_sq(x):
    return x >= 0 and isqrt(x) ** 2 == x


def multiplicity_report(entries):
    """(value, count) for values appearing more than once, sorted."""
    c = Counter(entries)
    return sorted((val, cnt) for val, cnt in c.items() if cnt > 1)


def main():
    print("#" * 78)
    print("# Task B audit: the four 7-square grids of oracle test 5b")
    print(f"# c = e^2, e <= {E_MAX}, |u|,|v| <= {V_MAX}, entries in "
          f"[1, {MAX_ENTRY}], squares = 1^2..81^2")
    print("# exact re-run of code/brute.py near_miss_scan(80,120)")
    print("#" * 78)

    per_count = Counter()
    kept = 0
    best_k = -1
    best_distinct_k = -1
    best_distinct_grid = None
    seven = []                     # (e, u, v, grid) with k == 7
    for e in range(1, E_MAX + 1):
        c = e * e
        for u in range(-V_MAX, V_MAX + 1):
            for v in range(-V_MAX, V_MAX + 1):
                g = grid_from_params(c, u, v)
                entries = g[0] + g[1] + g[2]
                if any(x < 1 or x > MAX_ENTRY for x in entries):
                    continue
                kept += 1
                k = sum(x in SQS for x in entries)
                per_count[k] += 1
                distinct = len(set(entries)) == 9
                if k > best_k:
                    best_k = k
                if distinct and k > best_distinct_k:
                    best_distinct_k = k
                    best_distinct_grid = g
                if k == 7:
                    seven.append((e, u, v, g))

    # ---- reproduction asserts against the recorded oracle output ----
    EXPECT_DIST = {1: 3653312, 2: 309896, 3: 85360, 4: 1952, 5: 748,
                   6: 964, 7: 4, 9: 92}
    problems = []
    if kept != 4052328:
        problems.append(f"kept {kept} != 4052328")
    if dict(per_count) != EXPECT_DIST:
        problems.append(f"distribution {dict(per_count)} != recorded")
    if best_k != 9:
        problems.append(f"best_k {best_k} != 9")
    if best_distinct_k != 5:
        problems.append(f"best_distinct_k {best_distinct_k} != 5")
    print(f"[scan] kept {kept} all-positive grids; distribution "
          f"{dict(sorted(per_count.items()))}")
    print(f"[scan] best k = {best_k} (trivial repeated grids), best "
          f"distinct k = {best_distinct_k}")
    if problems:
        print("!!! SCAN DOES NOT REPRODUCE THE RECORDED ORACLE OUTPUT !!!")
        for p in problems:
            print("    " + p)
        raise SystemExit(1)
    print("[scan] reproduction asserts PASSED: identical kept-count, "
          "square-count distribution, best k, best distinct k")
    print()

    print(f"seven-square grids found: {len(seven)}")
    for i, (e, u, v, g) in enumerate(seven, 1):
        entries = g[0] + g[1] + g[2]
        sums = line_sums(g)
        k_isqrt = sum(1 for x in entries if is_sq(x))
        sq_pos = [(r, c) for r in range(3) for c in range(3)
                  if is_sq(g[r][c])]
        repeats = multiplicity_report(entries)
        magic = len(set(sums)) == 1
        print()
        print(f"--- grid {i}/4: (e, u, v) = ({e}, {u}, {v}), "
              f"c = e^2 = {e * e}")
        for r in g:
            print(f"      {r}")
        print(f"      entries (row-major): {entries}")
        print(f"      entries (sorted):    {sorted(entries)}")
        print(f"      distinct count: {len(set(entries))} of 9; "
              f"repeats: {repeats if repeats else 'none'}")
        print(f"      k = {k_isqrt} square entries (isqrt recount), at "
              f"positions {sq_pos}")
        print(f"      non-square entries: "
              f"{sorted(x for x in entries if not is_sq(x))}")
        print(f"      line sums (8): {sums}")
        print(f"      all 8 line sums equal ({sums[0]} = 3c): {magic} "
              f"=> {'true magic square with 7 square entries' if magic else '7-of-8 near-miss'}")

    print()
    print("mutual distinctness of the four grids:")
    bases = [(e, u, v) for e, u, v, _ in seven]
    for i in range(len(seven)):
        for j in range(i + 1, len(seven)):
            gi = seven[i][3]
            gj = seven[j][3]
            ei = gi[0] + gi[1] + gi[2]
            ej = gj[0] + gj[1] + gj[2]
            if gi == gj:
                rel = "identical grid (same matrix; SAME (e,u,v))"
            elif bases[i] == bases[j]:
                rel = "same (e,u,v) but different matrix (impossible)"
            elif set(ei) == set(ej) and Counter(ei) == Counter(ej):
                rel = "same entry multiset, different arrangement"
            elif set(ei) == set(ej):
                rel = "same entry set, different multiplicities"
            else:
                rel = "different entry sets (mutually distinct)"
            print(f"      grid {i + 1} vs grid {j + 1}: {rel}")


if __name__ == "__main__":
    main()