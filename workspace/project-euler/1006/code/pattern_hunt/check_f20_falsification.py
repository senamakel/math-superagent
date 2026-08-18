#!/usr/bin/env python3
"""PE1006: find the exact first falsification at k = F_20 = 6765.

k = F_19 = 4181 (odd m) verified + at upper Wythoff.
k = F_20 = 6765 (even m) FAILS: minus count 4180, expected F_19 = 4181
lower-Wythoff positions.

Locate the exact missing/extra position and characterise the discrepancy.
Also check k = F_21 - 1 = 10945 (should be balanced dev=0).
"""
from math import isqrt
import sys
sys.path.insert(0, 'code/pattern_hunt')
from check_wythoff_balance_final import dev_digits, wyth, c1

SCALE = 4 ** 120
SQRT5 = isqrt(5 * SCALE * SCALE)


def floor_phi(n):
    return (n * SCALE + n * SQRT5) // (2 * SCALE)


def floor_phi2(n):
    return (3 * n * SCALE + n * SQRT5) // (2 * SCALE)


def main():
    k = 6765
    dev = dev_digits(k)
    minus = [j for j, d in enumerate(dev) if d == -1]
    plus = [j for j, d in enumerate(dev) if d == 1]
    wl = wyth(k, 'lower')
    wu = wyth(k, 'upper')
    miss = sorted(set(wl) - set(minus))
    extra = sorted(set(minus) - set(wl))
    print(f"k={k}: |minus|={len(minus)} |lowerWythoff|={len(wl)} |plus|={len(plus)}")
    print("missing lower-Wythoff positions:", miss[:20], "..." if len(miss) > 20 else "")
    print("extra (minus not in lowerWythoff):", extra[:20], "..." if len(extra) > 20 else "")
    print("counts: miss", len(miss), "extra", len(extra))

    # What is the missing position? print its value and the neighbouring Wythoff values
    if miss:
        m0 = miss[0]
        print("first missing:", m0)
        # lower Wythoff around m0
        lows = [floor_phi(t) for t in range(max(1, int(m0 / 1.618) - 2), int(m0 / 1.618) + 3)]
        print("lower Wythoff values around", m0, ":", lows)
        print("is m0 in upper Wythoff?", m0 in wu)

    # where do minus positions actually sit? distribution of gaps
    gaps = [minus[i+1] - minus[i] for i in range(len(minus) - 1)]
    from collections import Counter
    print("gap histogram of actual minus positions:", Counter(gaps).most_common(6))

    # balanced check at k = F_21 - 1 = 10945 (feasible? k^2 ~ 1.2e8 big-int ops; maybe slow but try)
    k2 = 10945
    print("\nk=10945 (F_21 - 1): computing dev (may take a while)...")
    dev2 = dev_digits(k2)
    print("max|dev|:", max(abs(d) for d in dev2), "(expect 0 for F_n-1 balance)")


if __name__ == '__main__':
    main()
