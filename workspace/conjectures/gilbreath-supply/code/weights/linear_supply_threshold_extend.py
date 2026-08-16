#!/usr/bin/env python3
"""Extend the linear-supply-by-weight threshold column to larger n.

GOAL (third pass): decide whether the minimum weight ratio w/n at which
"linear supply becomes typical" (mean nu2/n >= 0.40 AND frac>=0.40 >= 0.5)
tends to 0, or plateaus near a constant (the measured tail sat at 0.125 for
n=64 and n=128).

Method: for each n we sample, per exact Hamming weight w, a batch of random
weight-w strings and compute nu2(n)=wt(Phi_n h) via the canonical floored
submask fold. To afford many more samples than the 300/weight used before,
the SOS is vectorized over the batch (the submask-product g entries are ±1,
so int8 suffices). We find the smallest ratio w/*n* at which typical holds,
with a dense grid then a local refinement, and raise the sample count
(default 2000) well above 300 so the frac column can support the claim.

Oracle  : lib.supply_fold.s_sos (floored d in [2,n-1]); batch form below is
          the same submask-product transform, verified equal to s_sos on a
          per-string spot check, and against s_direct.
Range   : n in {256, 512, 1024, 2048, 4096} (sampled), with the guard
          nu2(53)==18, nu2(64)==27 asserted on the canonical oracle first.

This is a measurement (Monte Carlo), not a proof. The bound reported is the
threshold per n with its sample count; the tends-to-0 vs plateaus verdict is
an inference from that column and is labelled as such.
"""

import numpy as np
from lib.supply_fold import s_sos, s_direct
from lib.nu2_guard import assert_supply_guard, prime_h


def next_pow2(k):
    p = 1
    while p < k:
        p <<= 1
    return p


def batch_sos_ones(n, hbatch):
    """Vectorized submask-fold weight over a batch.

    hbatch: (M, n) int array of 0/1. Returns array of nu2 = number of
    d in [2,n-1] with T(n,d)=1, via the submask-product transform.
    Values are ±1 (tau products), so int8 is exact.
    """
    M = n
    # b_t = tau_{n-1-t}; tau_j = (-1)^{h[j]}. Reverse columns: barray[:,t]=tau[n-1-t]
    barray = np.where(hbatch[:, ::-1] == 1, -1, 1).astype(np.int8)  # h=1 -> tau=-1
    size = next_pow2(n)
    g = np.ones((hbatch.shape[0], size), dtype=np.int8)
    g[:, :M] = barray
    bit = 1
    while bit < size:
        # for each x with bit set: g[x] *= g[x ^ bit]
        idx = np.arange(size)
        sel = (idx & bit) != 0
        g[:, sel] = g[:, sel] * g[:, ~sel]
        bit <<= 1
    # d in 2..n-1
    cols = np.arange(2, n)
    terms = g[:, cols]  # (M, n-2)
    return np.count_nonzero(terms == -1, axis=1)


def verify_batch(n, samples=8):
    """Assert batch_sos_ones agrees with s_sos / s_direct on random strings."""
    rng = np.random.default_rng(12345)
    for w in [1, 3, n // 4, n // 2]:
        if w > n:
            continue
        for _ in range(samples):
            h = rng.integers(0, 2, size=n)
            hb = h.reshape(1, n)
            b = batch_sos_ones(n, hb)[0]
            _, o = s_sos(n, h.tolist())
            if b != o:
                raise AssertionError(f"batch/s_sos mismatch n={n} w={w}: {b} vs {o}")
    return True


def sample_weight(n, w, S, rng):
    """S random weight-w strings -> (mean nu2/n, frac(nu2/n>=0.40))."""
    hb = np.zeros((S, n), dtype=np.int8)
    for i in range(S):
        pos = rng.choice(n, size=w, replace=False)
        hb[i, pos] = 1
    nu2 = batch_sos_ones(n, hb)
    mean = nu2.mean() / n
    frac = np.count_nonzero(nu2 / n >= 0.40) / S
    return mean, frac


def find_threshold(n, S, rng, grid_denom=256):
    """Find the smallest ratio w/n (over an exact-weight grid, then refine)
    at which (mean>=0.40 and frac>=0.5). Returns (first_w, w/n, mean, frac)
    or None."""
    # dense grid first: w = round(k*n/grid_denom)
    best = None
    # crude scan to bracket
    ratios_tried = []
    for k in range(1, grid_denom + 1):
        w = max(1, round(k * n / grid_denom))
        mean, frac = sample_weight(n, w, S, rng)
        ratios_tried.append((k / grid_denom, w, mean, frac))
        if mean >= 0.40 and frac >= 0.5:
            # found first at this grid granularity; refine locally in w
            hi_w = w
            # refine downward from hi_w over previous w's and in-between
            lo_w = max(1, round((k - 3) * n / grid_denom)) if k > 3 else 1
            for ww in range(lo_w, hi_w + 1):
                mean2, frac2 = sample_weight(n, ww, S, rng)
                if mean2 >= 0.40 and frac2 >= 0.5:
                    return ww, ww / n, mean2, frac2
            return None
    return None


def main():
    out = []
    add = out.append

    add("=" * 78)
    add("PART 0 - ORACLE GUARD")
    add("=" * 78)
    add("oracle = lib.supply_fold.s_sos (single), batch_sos_ones (vectorized)")
    add("guard  = asserted: nu2(53)==18, nu2(64)==27 (canonical prime h)")
    guard_OK = True
    try:
        assert_supply_guard(64)
    except AssertionError:
        guard_OK = False
    add(f"  assert_supply_guard(64): {guard_OK}")
    if not guard_OK:
        add("  GUARD FAILED — aborting (cannot trust oracle).")
        print("\n".join(out))
        return

    # batch cross-check
    batch_ok = True
    for n in [32, 128, 256, 512]:
        try:
            assert verify_batch(n)
        except AssertionError as e:
            batch_ok = False
            add(f"  batch check FAILED at n={n}: {e}")
    add(f"  batch_sos_ones == s_sos on spot checks (32,128,256,512): {batch_ok}")
    add("")

    add("=" * 78)
    add("PART 1 - THRESHOLD EXTENSION (Monte Carlo, S samples per weight)")
    add("typical := mean nu2/n >= 0.40 AND frac(nu2/n >= 0.40) >= 0.5")
    add("=" * 78)
    add(f"{'n':>6} {'S':>6} {'first_w':>8} {'w/n':>7} {'mean@':>7} {'frac@':>7}")

    S = 2000
    grid_denom = 256
    results = {}
    for n in [256, 512, 1024, 2048, 4096]:
        rng = np.random.default_rng(2024 + n)
        r = find_threshold(n, S, rng, grid_denom)
        results[n] = r
        if r is None:
            add(f"{n:>6} {S:>6}    (none)      -      -      -")
        else:
            w, ratio, mean, frac = r
            add(f"{n:>6} {S:>6} {w:>8} {ratio:>7.4f} {mean:>7.4f} {frac:>7.3f}")
    add("")

    add("=" * 78)
    add("PART 2 - FULL COLUMN (exhaustive from pass2 + this extension)")
    add("=" * 78)
    add("n : ratio = first_w/n")
    col = [(8, 3 / 8), (10, 3 / 10), (12, 3 / 12), (14, 4 / 14), (16, 3 / 16),
           (32, 5 / 32), (64, 8 / 64), (128, 16 / 128)]
    for n in [256, 512, 1024, 2048, 4096]:
        r = results.get(n)
        if r is not None:
            col.append((n, r[1]))
    for n, ratio in col:
        add(f"  n={n:>5}:  w/n = {ratio:.4f}")
    add("")
    add("  The tail was 0.125, 0.125 at n=64,128. READ: does it keep falling")
    add("  (tends to 0) or flatten (plateaus at a constant)?")
    add("")

    print("\n".join(out))


if __name__ == "__main__":
    main()
