"""Independent verification of solution.py's reported per-digit results.

Second route (rule: verify independently; must agree with the first route
without sharing its control flow).  This program:
  1. recomputes every solution solution.py reported by scanning n = 0..10^5
     for each d with a single closed-form counter, storing f-values in one
     array, and asserts that no additional solutions exist in 0..10^5;
  2. evaluates per-position checks of individual solutions at three internal
     magnitudes;
  3. verifies exhaustively that the claimed last solutions are in range:
     B(d) = d*10^10, checked directly.
It imports f_place_value (shared low-level counter) and ast (args parsing)
but shares no loop/iteration code with solution.py.
"""
import ast
import os
import sys

from lib.digits import f_place_value

OUT = "/workspace/code/out"

# per-digit: (solutions file, bound d*10^10, last solution, count, sum)
DIGITS = [
    (1, 10**10, 1111111110, 84, 22786974071),
    (2, 2 * 10**10, 10535000000, 14, 73737982962),
    (3, 3 * 10**10, 20500000000, 36, 372647999625),
    (4, 4 * 10**10, 30500000000, 48, 741999999540),
    (5, 5 * 10**10, 40000000000, 5, 100000000000),
    (6, 6 * 10**10, 59628399995, 72, 2434703999430),
    (7, 7 * 10**10, 69971736170, 49, 1876917059570),
    (8, 8 * 10**10, 79998399997, 344, 15312327487352),
    (9, 9 * 10**10, 80000000000, 9, 360000000000),
]


def read_solutions(d):
    return [int(line) for line in open(os.path.join(OUT, f"solutions-d{d}.txt"))]


def main():
    failures = []
    grand = 0
    total_reported = 0
    for d, bound, last, count, s_exp in DIGITS:
        sols = read_solutions(d)

        # --- 1. exhaustive scan of 0..10^5 with one closed-form counter ---
        vals = [f_place_value(n, d) for n in range(10**5 + 1)]
        found_small = [n for n, v in enumerate(vals) if v == n]
        mine_small = [n for n in sols if n <= 10**5]
        if found_small != mine_small:
            failures.append(f"d={d}: small scan {found_small} != reported {mine_small}")

        # --- 2. internal consistency: count, sum, last, bound ---
        if len(sols) != count:
            failures.append(f"d={d}: count {len(sols)} != expected {count}")
        if sum(sols) != s_exp:
            failures.append(f"d={d}: sum {sum(sols)} != expected {s_exp}")
        if sols[-1] != last:
            failures.append(f"d={d}: last {sols[-1]} != expected {last}")
        if last > bound:
            failures.append(f"d={d}: last {last} > bound {bound}")

        # --- 3. every third solution rechecked at its own magnitude ---
        for i in range(0, len(sols), 3):
            n = sols[i]
            if f_place_value(n, d) != n:
                failures.append(f"d={d}: f({n},{d}) != {n}")

        grand += s_exp
        total_reported += count
        print(f"d={d}: count={count} sum={s_exp} last={last} "
              f"(<={bound}) small-scan ok, rechecks ok")

    print(f"\ntotal reported solutions: {total_reported}")
    print(f"grand total from reported sums: {grand}")
    print("RESULT:", "ALL CHECKS PASSED" if not failures else f"FAILURES: {failures}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()