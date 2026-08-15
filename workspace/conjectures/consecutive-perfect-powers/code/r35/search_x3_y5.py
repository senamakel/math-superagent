"""Exact-integer search for x^3 - y^5 = 1, R-35.

For x in [1, XMAX], compute m = x^3 - 1 and test whether m is an exact 5th
power using integer Newton 5th-root (no floats).  Report every (x,y) found.

Exact integer arithmetic throughout.  Complexity O(XMAX) 5th-root calls, each
O(log m) Newton steps on big ints: O(XMAX log^2 XMAX) time, O(1) space.
"""
from lib.perfectpow import perfect_qth_power
import sys, time


def main(XMAX):
    t0 = time.time()
    found = []
    for x in range(1, XMAX + 1):
        m = x ** 3 - 1
        y = perfect_qth_power(m, 5)
        if y is not None:
            found.append((x, y))
    dt = time.time() - t0
    found_pos = [(x, y) for (x, y) in found if y > 0]
    print(f"X_MAX={XMAX}")
    print(f"solutions (x,y) with x in [1,{XMAX}]: {found}")
    print(f"any y>0 solution: {bool(found_pos)}")
    print(f"runtime: {dt:.2f}s")


if __name__ == "__main__":
    XMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    main(XMAX)
