#!/usr/bin/env python3
"""Extension of the linear-supply-by-weight threshold column to large n.

GOAL (third pass): decide whether the minimum weight ratio w/n at which
"linear supply becomes typical" (mean nu2/n >= 0.40 AND frac>=0.40 >= 0.5)
tends to 0, or plateaus. Pass-two measured 0.375,0.300,0.250,0.286,0.188,
0.156,0.125,0.125 for n=8..128 and stopped. The tail sat at 0.125 twice.
This pushes to n=4096 and raises sampling to 2000/weight so the column can
support the tends-to-0 vs plateaus verdict.

Method: for each n and each exact weight w on a fine grid, sample S random
weight-w strings, each with a FRESH independent RNG (a sequential RNG makes
near-threshold frac~0.5 draws depend on how many earlier weights were tried,
which caused a spurious 'none' at n=256). Compute nu2(n)=wt(Phi_n h) with a
vectorized submask-product SOC transform over the batch (int8 exact; verified
== s_sos == s_direct on small n). First-typical w = smallest w with
(mean>=0.40 and frac>=0.5).

Oracle  : lib.supply_fold.s_sos (single), batch_sos_ones (vectorized)
Guard   : assert_supply_guard(64) -> nu2(53)==18, nu2(64)==27
Range   : n in {256, 512, 1024, 2048, 4096}, S=2000 per weight

Monte Carlo measurement, not a proof. The verdict inference is labelled.
"""

import numpy as np
from lib.supply_fold import s_sos
from lib.nu2_guard import assert_supply_guard
from weights.linear_supply_threshold_extend import (batch_sos_ones, sample_weight,
                                                   next_pow2, verify_batch)


def threshold_for(n, S, grid_denom=512):
    """Smallest exact weight ratio w/n at which (mean>=0.40 and frac>=0.5),
    each weight sampled with FRESH RNG seeded by (n,w). Returns
    (first_w, w/n, mean, frac) or (None, None, None, None)."""
    best = None
    for k in range(1, grid_denom + 1):
        w = max(1, min(n, round(k * n / grid_denom)))
        rng = np.random.default_rng(4242 + 1000 * n + w)  # fresh per (n,w)
        mean, frac = sample_weight(n, w, S, rng)
        if mean >= 0.40 and frac >= 0.5:
            best = (w, w / n, mean, frac)
            break
    if best is None:
        return (None, None, None, None)
    # refine downward in w from the bracketing w to find the true first-typical
    w0 = best[0]
    lo_w = max(1, int(w0 * 0.6))
    cand = None
    for ww in range(lo_w, w0):
        rng = np.random.default_rng(4242 + 1000 * n + ww)  # same-fresh style
        mean, frac = sample_weight(n, ww, S, rng)
        if mean >= 0.40 and frac >= 0.5:
            cand = (ww, ww / n, mean, frac)
    if cand is not None:
        return cand
    return best


def main():
    out = []
    add = out.append
    add("=" * 78)
    add("PART 0 - ORACLE GUARD")
    add("=" * 78)
    add("oracle = lib.supply_fold.s_sos (single), batch_sos_ones (vectorized)")
    add("guard  = asserted: nu2(53)==18, nu2(64)==27 (canonical prime h)")
    try:
        assert_supply_guard(64)
        add("  assert_supply_guard(64): True")
    except AssertionError as e:
        add(f"  GUARD FAILED: {e}")
        print("\n".join(out))
        return
    batch_ok = True
    for n in [32, 128, 256, 512]:
        try:
            assert verify_batch(n)
        except AssertionError as e:
            batch_ok = False
            add(f"  batch FAILED n={n}: {e}")
    add(f"  batch_sos_ones == s_sos (32,128,256,512): {batch_ok}")
    add("")

    add("=" * 78)
    add("PART 1 - THRESHOLD EXTENSION (fresh-RNG Monte Carlo, S per weight)")
    add("typical := mean nu2/n >= 0.40 AND frac(nu2/n >= 0.40) >= 0.5")
    add("=" * 78)
    add(f"{'n':>6} {'S':>6} {'first_w':>8} {'w/n':>7} {'mean@':>7} {'frac@':>7}")
    results = {}
    S = 3000
    for n in [256, 512, 1024, 2048, 4096]:
        w, ratio, mean, frac = threshold_for(n, S)
        results[n] = (w, ratio, mean, frac)
        if w is None:
            add(f"{n:>6} {S:>6}     (none)      -      -      -")
        else:
            add(f"{n:>6} {S:>6} {w:>8} {ratio:>7.4f} {mean:>7.4f} {frac:>7.3f}")
    add("")

    add("=" * 78)
    add("PART 2 - FULL COLUMN (pass2 exhaustive + this extension)")
    add("=" * 78)
    col = [(8, 3 / 8), (10, 3 / 10), (12, 3 / 12), (14, 4 / 14), (16, 3 / 16),
           (32, 5 / 32), (64, 8 / 64), (128, 16 / 128)]
    for n in [256, 512, 1024, 2048, 4096]:
        w, ratio, _, _ = results.get(n, (None, None, None, None))
        if ratio is not None:
            col.append((n, ratio))
    for n, ratio in col:
        add(f"  n={n:>5}:  w/n = {ratio:.4f}")
    add("")

    # log-log slope estimate of ratio vs n (tends-to-0 check)
    pts = [p for p in col if p[0] >= 64]
    if len(pts) >= 3:
        import math
        lnx = [math.log(p[0]) for p in pts]
        lny = [math.log(p[1]) for p in pts]
        xb, yb = sum(lnx) / len(lnx), sum(lny) / len(lny)
        num = sum((a - xb) * (b - yb) for a, b in zip(lnx, lny))
        den = sum((a - xb) ** 2 for a in range(len(lnx)))
        den = sum((lnx[i] - xb) ** 2 for i in range(len(lnx)))
        slope = num / den if den else float('nan')
        add(f"  log-log slope of (w/n) vs n over tail (n>=64): {slope:.3f}")
        add("  slope < 0 and staying negative => ratio tends to 0, not plateau.")
    add("")
    print("\n".join(out))


if __name__ == "__main__":
    main()
