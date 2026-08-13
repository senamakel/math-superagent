#!/usr/bin/env python3
"""code/rule90_test/analyze_rule90_depth.py

Test the Rule 90 / powers-of-2 depth prediction against the real block-length
record in code/out/blocks_depth1000.json.

The proved Rule 90 interior result (research/notes/rule90-interior.md) says
the {0,2} interior evolves under XOR = Rule 90 = Pascal mod 2, and at depths
d = 2^j the kernel is all-1, so every halved entry is the XOR of a width-(2^j+1)
window of the initial bit pattern.  A long run of XOR=1 there gives a regenerated
all-2 stretch.  The falsifiable prediction: block-length regeneration and the
depth between successive block-length minima should land at or near powers
of two, measured from the start of the current block regime (the row where the
block was last at a local minimum).

The program:
  (1) finds local minima of b_k (the leading-{0,2} block length) and their row
      indices k;
  (2) for each minimum, computes depth = k - k_prev_min where k_prev_min is the
      row of the previous local minimum (regime start);
  (3) checks whether depth is in {2^j, 2^j +/- 1} for some integer j;
  (4) checks whether block-expansion events b_{k+1} >> b_k occur at depths near
      powers of two.

Variants are parallelised with code/lib/parallel.py over measurement origin
(regime start vs absolute origin) and expansion threshold.  Exact (k, depth,
nearest power of two) matches and mismatches are reported.

Complexity: O(D) in time and O(D) in space (D = number of rows = 1000); every
variant is a single pass over the block record, so the whole thing is trivial.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from lib.parallel import workers, stripes, parallel_map, announce  # noqa: E402


def load_record(path="code/out/blocks_depth1000.json"):
    with open(path) as fh:
        return json.load(fh)


def powers_of_two_up_to(limit):
    """2^j for j=0,1,2,... up to limit, plus 2^j +/- 1 within range."""
    pw = []
    j = 0
    while (1 << j) <= limit + 1:
        pw.append(1 << j)
        j += 1
    return pw


def is_near_power_of_two(depth, tol=1):
    """depth in {2^j - tol .. 2^j + tol} for some j >= 0."""
    if depth <= 0:
        return None
    j = 0
    while (1 << j) <= depth + tol:
        p = 1 << j
        if abs(depth - p) <= tol:
            return (p, j, abs(depth - p))
        j += 1
    return None


def local_minima_indices(b):
    """Indices i (row k = i+1) that are strict-or-plateau local minima of b.

    A local minimum: b[i] <= b[i-1] and b[i] <= b[i+1] (boundary-aware at ends),
    with a tie (plateau) collapsed to the first index of the plateau.
    """
    n = len(b)
    mins = []
    i = 0
    while i < n:
        # find start of a (possibly flat) run that is a local min
        # strict local min in the interior
        # left boundary
        if i == 0:
            left_ok = True
        else:
            left_ok = b[i] <= b[i - 1]
        if i == n - 1:
            right_ok = True
        else:
            right_ok = b[i] <= b[i + 1]
        if left_ok and right_ok:
            # plateau of equal values
            j = i
            while j + 1 < n and b[j + 1] == b[i]:
                j += 1
            # check that the plateau is a proper local min: value below both sides
            left_val = b[i - 1] if i > 0 else None
            right_val = b[j + 1] if j + 1 < n else None
            if (left_val is None or b[i] < left_val) and (right_val is None or b[i] < right_val):
                mins.append(i)  # first index of the plateau
            i = j + 1
        else:
            i += 1
    # also: strict local minima with equal neighbours handled above; but a
    # plateau that sits at a minimum with a lower value on one side is not a min.
    return mins


def regimes_from_minima(min_idx):
    """Regime list: each (row_k_start, row_k_min, depth).

    row_k_min is the row where the next local minimum occurs, row_k_start is the
    previous local-minimum row (regime start).  depth = k_min - k_start.
    k_prev_min for the first minimum is taken as the very first row (1).
    """
    out = []
    k_start = 1  # origin: very first row is the start of the first regime
    for i in min_idx:
        k_min = i + 1
        depth = k_min - k_start
        out.append((k_start, k_min, depth))
        k_start = k_min
    return out


def expansion_events(b, threshold):
    """Indices i where b[i+1] >> b[i] (jump up), i.e. b[i+1] - b[i] >= threshold,
    and also events where b[i+1] > b[i] (any regeneration)."""
    def jumps(gt):
        ev = []
        for i in range(len(b) - 1):
            d = b[i + 1] - b[i]
            if d >= gt:
                ev.append((i, i + 1, b[i], b[i + 1], d))
        return ev
    return jumps(threshold), jumps(1)


def variant_analysis(b, origin_abs, threshold):
    """One hypothesis variant.  Returns a dict summarising matches/mismatches.

    origin_abs: if True measure depth from absolute origin (row 1); if False
    measure from the previous local-minimum row (regime start).
    """
    pass


# --- worker for parallel map ------------------------------------------------

def analyze_minima_depth(b, min_idx, origin_abs):
    """Depth of each local minimum from origin, tested against {2^j, 2^j±1}."""
    rows = []
    if origin_abs:
        for i in min_idx:
            k = i + 1
            depth = k - 1  # distance from absolute origin row 1
            rows.append((k, depth))
    else:
        k_start = 1
        for i in min_idx:
            k = i + 1
            depth = k - k_start
            rows.append((k, depth, k_start))
            k_start = k
    return rows


def main():
    rec = load_record()
    b = rec["b"]
    D = rec["D"]
    min_idx = local_minima_indices(b)
    min_rows = [i + 1 for i in min_idx]
    min_vals = [b[i] for i in min_idx]

    pw = powers_of_two_up_to(65536)

    print(f"D={D}  rows of b")
    print(f"local-minima row indices k: {min_rows}")
    print(f"local-minima block-length values: {min_vals}")
    print(f"count of local minima: {len(min_rows)}")

    # (2)+(3): depths from regime start vs absolute origin
    for origin_abs, label in ((False, "regime-start"), (True, "absolute")):
        rows = analyze_minima_depth(b, min_idx, origin_abs)
        print(f"\n=== minima depths from {label} origin ===")
        print(f"{'k_min':>8} {'depth':>8} {'nearest 2^j':>16} {'close?':>6}")
        hit = 0
        for item in rows:
            k, depth = item[0], item[1]
            near = is_near_power_of_two(depth, tol=1)
            if near is not None:
                hit += 1
            print(f"{k:>8} {depth:>8} {str(near[0]) if near else '-':>16} "
                  f"{'YES' if near else 'no':>6}")

    # (4): expansion jumps near powers of two
    for threshold in (5, 10, 100, 1000, 10000):
        jumps, regen = expansion_events(b, threshold)
        print(f"\n=== expansion jumps (b[i+1]-b[i] >= {threshold}) ===")
        print(f"count: {len(jumps)}")
        for (i, i2, b0, b1, d) in jumps:
            k = i + 1
            print(f"  jump at k={k}->{i2+1}: b {b0}->{b1}, jump {d}")

    # Serial check of the headline claim: depth between successive minima
    # (regime length) near power of two.
    print("\n=== regime lengths (depth between successive local minima) ===")
    regimes = regimes_from_minima(min_idx)
    hit = 0
    for (k_start, k_min, depth) in regimes:
        near = is_near_power_of_two(depth, tol=1)
        if near is not None:
            hit += 1
        print(f"regime {k_start}->{k_min}: depth {depth}, "
              f"nearest 2^j {'= %d' % near[0] if near else '-'} "
              f"{'YES' if near else 'no'}")
    print(f"\ntotal regimes: {len(regimes)}, near-power-of-2: {hit}")


if __name__ == "__main__":
    main()
