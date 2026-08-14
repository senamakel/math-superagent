"""Task C: structure of factor values.

- Load code/out/factors_k40.json (sorted k+1 factors per k).
- For k=1..12 print the k+1 factors and their decimal values V (exact ints).
- Look for a closed recurrence among consecutive V in the given order.
- Print table (k, factor index j, factor, V, V mod M).
- Compute per-position one-counts N(i;k) for k=1..40 and try to fit
  N(i;k) = floor((k-i)*a + const) with a = 1/phi^2 etc.

Exact integer arithmetic throughout.
"""
import json
import os
from fractions import Fraction

MOD = 101001001
SQRT5 = 5 ** Fraction(1, 2)  # not exact; we'll use rational approx for fitting


def value(bits):
    return int(bits, 2)  # interprets as binary? NO - we need decimal digit reading!
    # but int(bits) reads as decimal. Fix below.


def decimal_value(bits):
    return int(bits)  # reads the 0/1 string as a decimal number, ignoring leading zeros


def main():
    data = json.load(open(os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")))
    # data keys are strings "1".."40"; each value is a list of factor strings in sorted order.

    print("=" * 70)
    print("TASK C: factor values k=1..12 and per-position one-counts")
    print("=" * 70)

    # ---- C1: k=1..12 factors and decimal values ----
    print("\n[C1] factors and decimal values V (in the given sorted order)")
    for k in range(1, 13):
        facs = data[str(k)]
        vals = [decimal_value(f) for f in facs]
        print(f"\nk={k} (count={len(facs)}):")
        for f, v in zip(facs, vals):
            print(f"    {f!r:>22}  V={v}")

    # ---- C2: consecutive-value closed form check ----
    print("\n[C2] consecutive values: is V of consecutive factors related simply?")
    print("     We test: V_j+1 vs V_j, and the value's bit structure.")
    for k in [3, 4, 5, 6, 7, 8, 10]:
        facs = data[str(k)]
        vals = [decimal_value(f) for f in facs]
        print(f"  k={k}: values = {vals}")
        # diff of consecutive
        diffs = [vals[j + 1] - vals[j] for j in range(len(vals) - 1)]
        print(f"        consecutive diffs = {diffs}")

    # The string structure: factors are length k binary. Print as bit lists and
    # look at how each string shifts from the previous (right-extension?).
    print("\n[C2b] string transitions (what one factor shares with the next):")
    for k in [6, 7, 8, 10]:
        facs = data[str(k)]
        print(f"  k={k}:")
        prev = None
        for f in facs:
            if prev is not None:
                # longest common suffix of prev == prefix relation
                for m in range(len(prev), -1, -1):
                    if f[:m] == prev[len(prev) - m:]:
                        common = m
                        break
                print(f"    {prev!r} -> {f!r}   (shares {len(f)}-bit; first {len(prev)} kept?)", )
            prev = f

    # ---- C3: per-position one-counts N(i;k) ----
    print("\n[C3] per-position one-counts N(i;k), i=0..k-1 from left")
    rows = {}
    for k in range(1, 41):
        facs = data[str(k)]
        N = [0] * k
        for f in facs:
            for i, ch in enumerate(f):
                if ch == '1':
                    N[i] += 1
        rows[k] = N
    # print k=8..15 like the existing dump
    for k in range(8, 16):
        print(f"  k={k:2d}: N = {rows[k]}")
    # full k=1..40 saved
    print("\n  (all N(i;k), k=1..40, saved below)")

    # ---- C4: candidate closed form N(i;k) = floor((k-i)*a + c) ----
    print("\n[C4] candidate closed form for N(i;k)")
    # a = 1/phi^2 = (3-sqrt5)/2. We want to relate N(i;k) to (k-i).
    # Empirical observation (HORIZONTAL): N(i;k) is the number of factors with a 1
    # at position i. A known result: for a Sturmian word of slope a, position i has
    # the letter pattern; the count of 1s at position i across all length-k factors
    # is the number of factors whose i-th bit is 1.
    # We'll fit N(i;k) = floor(const + (k-1-i)*something) empirically.
    print("  Fit attempt: N(i;k) = floor(A*(k-i) + B) for a candidate A.")
    print("  Try A ~ 1 - (3-sqrt5)/2 * ... ")

    # Instead of guessing multipliers, directly look at increment of N when k grows.
    # Stable hypothesis from data (k=13..40): values hover between floor(k*a)-1..+1
    # region. Print a sample to build intuition:
    for k in [10, 15, 20, 25, 30, 35, 40]:
        print(f"  k={k:2d}: N = {rows[k]}")


if __name__ == "__main__":
    main()
