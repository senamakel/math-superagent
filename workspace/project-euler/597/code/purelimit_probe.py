#!/usr/bin/env python3
"""Pure-race parity p(n,inf) vs finite p(n,1800) for PE 597, by Monte Carlo.

Pure race = ballistic aggregation with NO finish line: boats bump only by catch
times, a boat that bumps stops (OUT, passed freely), a bumped boat continues
and may be re-bumped. New-order parity = (# bump-chain pairs) mod 2, exactly the
torpids parity with no finish events.

For each n we estimate p(n,inf) (pure race) and p(n,1800) (the real race with a
finish line at 1800, engine = brute.outcome_parity) on the SAME True Exp(1)
speed draws, reporting each with a binomial SE.

The pure race (no finish) is the large-L limit: as L->inf, finish events never
intervene. Known exact limits for n=2,3,4 are 1/2, 7/18, 19/36; we self-check
n=3,4 against those.

Usage: python3 purelimit_probe.py [trials]
  trials defaults to 200000 for n<=13 and scales down for larger n.
"""
import sys, math
import numpy as np
from brute import outcome_parity


def pure_race_parity(n, speeds):
    """Parity of the new order for the pure bump race (no finish line).

    Speeds are Exp(1) draws indexed j=0..n-1, j=0 lowest. Boats start 40 apart;
    a boat rows at constant speed until it catches the nearest ROWING boat
    ahead (then OUT, passed freely) or everyone is out. Parity =
    (# bump chain pairs) mod 2 = sum over i of |above[i]| mod 2.
    """
    state = [0] * n          # 0 ROWING, 1 OUT
    pos = [40.0 * j for j in range(n)]
    edges = [[] for _ in range(n)]
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            k = None
            for kk in range(j + 1, n):
                if state[kk] == 0:
                    k = kk
                    break
            if k is not None:
                vj, vk = speeds[j], speeds[k]
                if vj > vk:                      # only a faster boat can catch
                    t = (pos[k] - pos[j]) / (vj - vk)
                    if best is None or t < best[0] - 1e-15:
                        best = (t, j, k)
        if best is None:
            break   # no rowing boat can catch the next rowing boat ahead:
                    # speeds along the remaining rowing list are non-decreasing,
                    # so no bump will ever occur -> no further chain pairs
        t, j, k = best
        state[j] = 1
        pos[j] = pos[k]
        edges[j].append(k)
    # above[i] = boats reachable from i via bump edges (placed below i)
    chain_pairs = 0
    for i in range(n):
        seen = {i}
        stack = [i]
        while stack:
            u = stack.pop()
            for w in edges[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        chain_pairs += len(seen) - 1
    return chain_pairs % 2


def mc_estimate(sampler, n, trials, seed):
    """Mean of parity over trials draws of Exp(1) speeds + binomial SE."""
    rng = np.random.default_rng(seed)
    s = 0
    for _ in range(trials):
        v = rng.exponential(size=n)
        s += sampler(v)
    p = s / trials
    se = math.sqrt(p * (1 - p) / trials)
    return p, se


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    base = trials
    results = []
    # self-check pure race at n=3,4 against known exact limits 7/18, 19/36
    known = {2: (1, 2), 3: (7, 18), 4: (19, 36)}
    for n in range(2, 31):
        t = base if n <= 13 else max(20000, base // (n - 12))
        p_inf, se_inf = mc_estimate(
            lambda v, n=n: pure_race_parity(n, v), n, t, seed=100 + n)
        p1800, se1800 = mc_estimate(
            lambda v, n=n: outcome_parity(n, 1800, v), n, t, seed=1000 + n)
        results.append((n, t, p_inf, se_inf, p1800, se1800))
        line = (f"n={n:2d} trials={t:6d}  p(n,inf)={p_inf:.6f}+-{se_inf:.6f}"
                f"  p(n,1800)={p1800:.6f}+-{se1800:.6f}")
        if n in known:
            num, den = known[n]
            ok = abs(p_inf - num / den) <= 4 * se_inf
            line += f"   [pure check {num}/{den}={'OK' if ok else 'FAIL'}]"
        print(line)

    print("\n  pure-race and finite delta near the target (n=13, m=L/40=45):")
    for n, _, p_inf, _, p1800, se1800 in results:
        if 11 <= n <= 15:
            print(f"    n={n}: p(inf)={p_inf:.6f}  p(1800)={p1800:.6f}"
                  f"  diff={p1800 - p_inf:+.6f}")


if __name__ == "__main__":
    main()
