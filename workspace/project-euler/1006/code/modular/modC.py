"""TASK C - structure of factor values, exact.

Loads code/out/factors_k40.json (dict k -> sorted list of the k+1 distinct
length-k Fibonacci subwords). For k=1..12 prints each factor and its exact
decimal value V (leading zeros ignored), plus V mod M.

Also computes N(i;k) = number of the k+1 factors with a '1' at string position
i (0 = leftmost), for k up to 40, and tests the conjectured closed form

    N(i;k) = floor((k-i)*a + c)

with a = 1/phi^2 = (3-sqrt(5))/2, fitting the constant c empirically and
checking whether a single c works for all k<=40 (i.e. the count is
Sturmian/balanced, floor((k-i)a + c) in the position variable).

All arithmetic exact (exact rationals for a is not possible — a is irrational,
so we check with high-precision Decimal and report the fitted empirical c).
The counts N(i;k) themselves are exact integers from the JSON data.
"""

import json
import os
from decimal import Decimal, getcontext, ROUND_FLOOR

MOD = 101001001
getcontext().prec = 60
ALPHA = Decimal(3) - Decimal(5).sqrt()  # = 1/phi^2 ... wait (3-sqrt5)/2
ALPHA = (Decimal(3) - Decimal(5).sqrt()) / Decimal(2)
ONE = Decimal(1)


def floor_dec(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def main():
    base = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
    with open(base) as fh:
        data = json.load(fh)  # keys are strings "1".."40"

    out = []
    out.append(f"Factor table, k=1..12.  V = exact decimal value (leading zeros ignored).")
    out.append(f"MOD = {MOD}\n")
    for k in range(1, 13):
        factors = data[str(k)]
        out.append(f"===== k={k} (count={len(factors)}) =====")
        for j, fac in enumerate(factors):
            V = int(fac)
            out.append(f"  k={k} j={j} factor={fac} V={V} V mod M={V % MOD}")
        out.append("")
    out.append("")

    # Per-position one-counts N(i;k) for k=1..40
    out.append("Per-position one-counts N(i;k) (i=0 = leftmost), k=1..40:")
    pos_counts_per_k = {}
    for k in range(1, 41):
        factors = data[str(k)]
        pc = [0] * k
        for s in factors:
            for i, ch in enumerate(s):
                if ch == "1":
                    pc[i] += 1
        pos_counts_per_k[k] = pc
    for k in range(1, 41):
        out.append(f"  k={k:2d}: " + " ".join(f"{c:2d}" for c in pos_counts_per_k[k]))
    out.append("")

    # Fit N(i;k) = floor((k-i)*a + c). For a Sturmian factor set, per-position
    # counts are balanced. Compute floor((k-i)*a + c) for various c and check
    # agreement. We search a rational-ish c by testing multiples of small step
    # against ALL k<=40, i in 0..k-1. Report the best constant.
    out.append("Testing closed form N(i;k) = floor((k-i)*a + c), a=(3-sqrt5)/2,")
    out.append("against exact counts for all k<=40.\n")
    # For a purely Sturmian/periodic-beatty position, the count N(i;k) should
    # equal the number of factors with a 1 at position i. We test a grid of c.
    best = None
    for num in range(-200, 200):
        c = Decimal(num) / Decimal(100)  # c grid
        # we will refine; first quick scan
        matches = 0
        total = 0
        for k in range(1, 41):
            pc = pos_counts_per_k[k]
            for i in range(k):
                pred = floor_dec(Decimal(k - i) * ALPHA + c)
                if pred == pc[i]:
                    matches += 1
                total += 1
        if best is None or matches > best[0]:
            best = (matches, total, c)
    out.append(f"best grid constant c={best[2]} with {best[0]}/{best[1]} positions matching.")
    out.append("")

    # Report explicit agreement per k for the best c found in a finer search.
    # Refine c around the best grid value.
    c0 = best[2]
    best2 = None
    for num in range(-400, 400):
        c = c0 + Decimal(num) / Decimal(1000)
        matches = 0
        total = 0
        for k in range(1, 41):
            pc = pos_counts_per_k[k]
            for i in range(k):
                pred = floor_dec(Decimal(k - i) * ALPHA + c)
                if pred == pc[i]:
                    matches += 1
                total += 1
        if best2 is None or matches > best2[0]:
            best2 = (matches, total, c)
    out.append(f"refined constant c = {best2[2]}, matches {best2[0]}/{best2[1]}.")
    out.append("")
    out.append("Per-k agreement for refined c:")
    c = best2[2]
    for k in range(1, 41):
        pc = pos_counts_per_k[k]
        bad = []
        for i in range(k):
            pred = floor_dec(Decimal(k - i) * ALPHA + c)
            if pred != pc[i]:
                bad.append((i, pc[i], pred))
        status = "OK" if not bad else f"MISMATCHES {bad[:5]}"
        out.append(f"  k={k:2d}: {status}")

    text = "\n".join(out) + "\n"
    print(text)
    with open("code/out/mod_C.txt", "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
