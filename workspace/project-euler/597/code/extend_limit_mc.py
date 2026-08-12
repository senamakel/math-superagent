#!/usr/bin/env python3
"""Extend the large-L limit sequence p(n, inf) = lim_{L->inf} p(n,L) for
n = 2..9 by Monte Carlo over the PURE bump race (no finish line).

With Exp(1) speeds, the race is invariant to common scaling, so normalized
speeds are uniform on the (n-1)-simplex; sampling Exp speeds and running the
pure (no-finish) bump race gives p(n,inf) directly.  No finish events.

Pure bump race: boat j rows until it catches the nearest still-rowing boat
ahead; on a catch the REAR bumper is removed (OUT), the target keeps rowing.
Reproduce the torpids_parity exactly and count even-parity outcomes.
"""
import random, math, sys


def pure_bump_edges(n, speeds):
    """Run pure (no-finish) bump race. speeds is a list of n floats.
    Return parent array: parent[j]=k if j bumped k else None (out-degree<=1)."""
    state = [0] * n          # 0 = rowing, 2 = OUT
    pos = [40.0 * j for j in range(n)]
    parent = [None] * n
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
            if k is None or speeds[j] <= speeds[k]:
                continue
            t = (pos[k] - pos[j]) / (speeds[j] - speeds[k])
            if best is None or t < best[0]:
                best = (t, j, k)
        if best is None:
            break
        t, j, k = best
        for a in rowing:
            pos[a] += speeds[a] * t
        state[j] = 2
        parent[j] = k
    return parent


def forest_chain_parity(n, parent):
    """(number of proper ancestor-descendant pairs in the bump forest) mod 2.
    Equal to the parity (inversion count) of the race order (verified)."""
    children = [[] for _ in range(n)]
    for j in range(n):
        if parent[j] is not None:
            children[parent[j]].append(j)
    total = 0
    for a in range(n):
        stack = list(children[a])
        while stack:
            d = stack.pop()
            total += 1
            stack.extend(children[d])
    return total & 1


def mc(n, N, seed):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        even += (1 - forest_chain_parity(n, pure_bump_edges(n, v)))
    return even


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    for n in range(2, 10):
        # pooled across a few seeds for a tighter estimate
        tot = 0
        ev = 0
        for s in range(4):
            e = mc(n, N, 1000 + s)
            ev += e
            tot += N
        p = ev / tot
        se = math.sqrt(p * (1 - p) / tot)
        print(f"n={n}  p(n,inf) = {p:.8f} +/- {se:.6f}   (num approx = {ev}/{tot})",
              flush=True)


if __name__ == "__main__":
    main()
