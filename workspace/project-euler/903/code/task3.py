#!/usr/bin/env python3
"""task3.py — assess extending f_n(k) rows to n=12,13 via verify_f_method2.py.

Reuse candidate f_n_method2 (verify_f_method2.py) enumerates ALL n!
permutations per n with ~O(per-perm) work over the small k range, so wall
time scales as n! (no re-aggregation possible without a genuinely different
algorithm, e.g. conjugacy-class / cycle-type counting which is not written).

This script MEASURES per-perm cost at a reachable n (n=12 = 479M perms is ~12x
n=11) and extrapolates linearly in n! to report the wall for n=11,12,13.  It
does NOT run n=12/13: n=12 is ~54 min and n=13 ~12 h, far beyond the
"few minutes" budget.
"""
import math
import sys
import time

sys.path.insert(0, "/workspace/code")
from verify_f_method2 import f_n_method2


def extrapolate(t_measured, n_measured):
    per_perm = t_measured / math.factorial(n_measured)
    print("Extrapolation (linear in n!, same per-perm cost):")
    for n in (11, 12, 13):
        secs = per_perm * math.factorial(n)
        print(f"  n={n}: {math.factorial(n):,d} perms -> "
              f"{secs:.0f} s = {secs/60:.1f} min")


def main():
    n = 10
    print(f"Measuring method2 per-perm cost at n={n} ...")
    t0 = time.time()
    row = f_n_method2(n)
    dt = time.time() - t0
    print(f"n={n} computed in {dt:.2f}s (row head {row[:3]} ...)")
    extrapolate(dt, n)
    print()
    print("Verdict: n=12 (~54 min) and n=13 (~12 h) both exceed the "
          "'few minutes' budget -> SKIP, report wall.")


if __name__ == "__main__":
    main()
