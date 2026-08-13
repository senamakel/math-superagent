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
  (1) finds local minima of b_k (leading-{0,2} block length) and their row k;
  (2) for each minimum, computes depth = k - k_prev_min (previous local-min row);
  (3) checks whether depth is in {2^j, 2^j +/- 1};
  (4) checks whether block-expansion events b_{k+1} >> b_k occur at depths near
      powers of two.

Hypothesis variants (origin: regime-start vs absolute; expansion threshold;
tolerance for 'near power of two') are fanned out with code/lib/parallel.py.

Complexity: O(D) time and space per variant, D = 1000 rows.  Every variant is
one pass over the block record; nothing grows with a search bound.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from lib.parallel import workers, stripes, parallel_map, announce  # noqa: E402

# --- data ------------------------------------------------------------------


def load_record(path="code/out/blocks_depth1000.json"):
    with open(path) as fh:
        return json.load(fh)


# --- local minima -----------------------------------------------------------


def local_minima_indices(b):
    """Indices i (row k = i+1) that are local minima of b, plateaus collapsed.

    i is a local min when b[i] <= both neighbours (boundary-aware); a flat
    plateau of equal values that is below both its outer neighbours is one
    minimum, recorded at its first index.
    """
    n = len(b)
    mins = []
    i = 0
    while i < n:
        left_ok = (i == 0) or (b[i] <= b[i - 1])
        right_ok = (i == n - 1) or (b[i] <= b[i + 1])
        if left_ok and right_ok:
            j = i
            while j + 1 < n and b[j + 1] == b[i]:
                j += 1
            below_left = (i == 0) or (b[i] < b[i - 1])
            below_right = (j == n - 1) or (b[i] < b[j + 1])
            if below_left and below_right:
                mins.append(i)
            i = j + 1
        else:
            i += 1
    return mins


# --- power-of-two predicates -------------------------------------------------


def is_near_power_of_two(depth, tol):
    """(2^j, j, |depth - 2^j|) if |depth - 2^j| <= tol for some j>=0, else None."""
    if depth <= 0:
        return None
    j = 0
    while (1 << j) <= depth + tol:
        p = 1 << j
        if abs(depth - p) <= tol:
            return (p, j, abs(depth - p))
        j += 1
    return None


# --- analysis primitives ------------------------------------------------------


def regime_lengths(b, min_idx):
    """depth of each local min from the previous local-min row (regime start)."""
    out = []
    k_start = 1
    for i in min_idx:
        k_min = i + 1
        out.append((k_start, k_min, k_min - k_start))
        k_start = k_min
    return out


def abs_depths(b, min_idx):
    return [(i + 1, i) for i in min_idx]  # k, depth from absolute origin


def expansion_jumps(b, gt):
    return [(i, i + 1, b[i], b[i + 1], b[i + 1] - b[i])
            for i in range(len(b) - 1) if b[i + 1] - b[i] >= gt]


# --- parallel worker: one variant ---------------------------------------------


def _variant(params):
    """Analyse one hypothesis variant. params = (b, origin, threshold, tol)."""
    b, origin, threshold, tol = params
    min_idx = local_minima_indices(b)

    # depths of minima under the chosen origin
    if origin == "regime":
        depths = [(k_start, k_min, k_min - k_start) for (k_start, k_min, _) in
                  regime_lengths(b, min_idx)]
        n_abs = None
    else:
        depths = [((1 if False else 1), k, k - 1) for k in
                  (i + 1 for i in min_idx)]
        # keep simple: (k_start=1, k_min, depth=k-1)
        depths = [(1, i + 1, i) for i in min_idx]

    min_hits = 0
    min_misses = []
    rows = []
    for (k_start, k_min, depth) in depths:
        near = is_near_power_of_two(depth, tol)
        if near is not None:
            min_hits += 1
            rows.append((k_min, depth, near[0], "YES"))
        else:
            rows.append((k_min, depth, None, "no"))
            min_misses.append((k_min, depth))

    # expansion events
    jumps = expansion_jumps(b, threshold)
    jumps_near = [j for j in jumps if is_near_power_of_two(j[4], tol) is not None]
    jumps_abs_near = []
    for (i, i2, b0, b1, d) in jumps:
        k = i2 + 1  # row where the expanded block first appears
        near = is_near_power_of_two(k - 1, tol)  # absolute depth of jump row
        jumps_abs_near.append((k, d, near[0] if near else None))

    return {
        "origin": origin, "threshold": threshold, "tol": tol,
        "n_minima": len(min_idx),
        "min_hits": min_hits, "min_total": len(depths),
        "min_rows": rows,
        "jumps_count": len(jumps),
        "jumps_magnitude_near_pow2": sum(1 for j in jumps
                                          if is_near_power_of_two(j[4], tol)),
        "jumps_at_abs_near_pow2": jumps_abs_near,
    }


# --- driver -------------------------------------------------------------------


def main():
    rec = load_record()
    b = rec["b"]
    D = rec["D"]

    min_idx = local_minima_indices(b)
    min_rows = [i + 1 for i in min_idx]
    min_vals = [b[i] for i in min_idx]
    print(f"D={D}")
    print(f"local-minima row indices k: {min_rows}")
    print(f"local-minima block lengths b_k: {min_vals}")
    print(f"count: {len(min_rows)}")

    # Serial headline: regime lengths (depths of minima from regime start)
    print("\n=== minimum depths from regime start (prev local-min row) ===")
    hit = 0
    regimes = regime_lengths(b, min_idx)
    print(f"{'regimeStart':>12} {'k_min':>6} {'depth':>8} {'nearest2^j':>10} "
          f"{'close':>6}")
    for (ks, km, depth) in regimes:
        near = is_near_power_of_two(depth, 1)
        if near:
            hit += 1
        print(f"{ks:>12} {km:>6} {depth:>8} "
              f"{str(near[0]) if near else '-':>10} {'YES' if near else 'no':>6}")
    n_regimes = len(regimes)
    print(f"\nregimes: {n_regimes}, near-power-of-2 (tol=1): {hit} "
          f"({100.0*hit/n_regimes:.0f}%)")

    # Parallelised variants
    variants = []
    for origin in ("regime", "absolute"):
        for threshold in (1, 5, 10, 100, 1000, 10000):
            for tol in (0, 1, 2, 4):
                variants.append((b, origin, threshold, tol))
    announce("rule90-depth variants", f"{len(variants)} variants x D={D}",
             workers() if len(variants) > 1 else 1)
    results = parallel_map(_variant, variants, label="rule90-depth",
                           space=f"{len(variants)} variants",
                           count=workers() if len(variants) > 1 else 1)

    print("\n=== variant table ===")
    print(f"{'origin':>9} {'thr':>5} {'tol':>3} {'minHit/tot':>11} "
          f"{'jumpMag^2':>10} {'jumpAtAbs^2':>12}")
    for r in results:
        mag = r["jumps_magnitude_near_pow2"]
        atabs = sum(1 for (k, d, near) in r["jumps_at_abs_near_pow2"] if near is not None)
        print(f"{r['origin']:>9} {r['threshold']:>5} {r['tol']:>3} "
              f"{r['min_hits']}/{r['min_total']:>6} {mag:>10} {atabs:>12}")

    # detail for a few headline variants
    print("\n=== expansion-jump rows and jump magnitudes (threshold 5, tol=4) ===")
    for r in results:
        if r["origin"] == "regime" and r["threshold"] == 5 and r["tol"] == 4:
            for (k, d, near) in r["jumps_at_abs_near_pow2"]:
                print(f"  jump to row k={k}: magnitude {d}, "
                      f"absolute depth k-1={k-1} "
                      f"{'near 2^j' if near is not None else 'NOT near'}")

    # write machine-readable summary
    out = {
        "D": D,
        "minima_rows": min_rows,
        "minima_vals": min_vals,
        "regimes": [{"start": ks, "k": km, "depth": d, "near_pow2": near}
                    for (ks, km, d) in regimes
                    for near in [is_near_power_of_two(d, 1)[0]
                                 if is_near_power_of_two(d, 1) else None]],
        "regime_near_pow2_count": hit,
        "regime_total": n_regimes,
        "variants": [{"origin": r["origin"], "threshold": r["threshold"],
                      "tol": r["tol"], "min_hits": r["min_hits"],
                      "min_total": r["min_total"]} for r in results],
    }
    with open("code/out/rule90_depth_results.json", "w") as fh:
        json.dump(out, fh, indent=2)
    print("\nwrote code/out/rule90_depth_results.json")


if __name__ == "__main__":
    main()
