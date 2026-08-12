#!/usr/bin/env python3
"""Sharper MC of the large-L limit sequence p(n,inf) for n=5..24, to test the
hypothesis that p(n,inf) -> 1/2 as n grows (parity becomes asymptotically
balanced).  Pure no-finish bump race over Exp(1) speeds (uniform on simplex)."""
import random, math, sys
sys.path.insert(0, ".")


def pure_bump_edges(n, speeds):
    state = [0] * n
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
        v = [-math.log(rng.random()) for _ in range(n)]
        even += (1 - forest_chain_parity(n, pure_bump_edges(n, v)))
    return even


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 800_000
    for n in range(5, 25):
        tot, ev = 0, 0
        for s in range(4):
            e = mc(n, N, 5000 + s)
            ev += e
            tot += N
        p = ev / tot
        se = math.sqrt(p * (1 - p) / tot)
        dev = (p - 0.5) / se if se > 0 else 0
        print(f"n={n:2d}  p(n,inf)={p:.6f} +/- {se:.5f}  (dev from 0.5: {dev:+.2f} SE)",
              flush=True)


if __name__ == "__main__":
    main()
