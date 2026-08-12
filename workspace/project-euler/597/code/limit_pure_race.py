#!/usr/bin/env python3
"""Fast pure-race (no finish line) parity MC for the large-L limit L_n = p(n,inf).
Pure race: bump nearest rowing boat ahead, bumper removed, bumped keeps rowing.
Reuse the chronology logic but skip finish events (no finish line)."""
import random, sys, math

def pure_race_parity(n, v):
    # edges: bumper->bumped
    state = [0]*n      # 0 rowing, 2 OUT
    pos = [40.0*j for j in range(n)]
    edges = []
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if len(rowing) <= 1:
            break
        best = None
        for j in rowing:
            k = None
            for kk in range(j+1, n):
                if state[kk] == 0:
                    k = kk; break
            if k is None: continue
            if v[j] > v[k]:
                t = (pos[k]-pos[j])/(v[j]-v[k])
                if best is None or t < best[0]:
                    best = (t, j, k)
        if best is None:
            break
        t, j, k = best
        for a in rowing:
            pos[a] += v[a]*t
        state[j] = 2
        edges.append((j,k))
    # chain pairs = number of ancestor-descendant pairs in bump forest
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
    total = 0
    for i in range(n):
        seen = set(); stack = [i]
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        total += len(seen - {i})
    return total % 2

def mc(n, N, seed):
    rng = random.Random(seed)
    e = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        if pure_race_parity(n, v) == 0:
            e += 1
    p = e/N
    se = math.sqrt(p*(1-p)/N)
    return p, se

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 500000
    for n in range(2, 13):
        p, se = mc(n, N, seed=100+n)
        print(f'n={n}  L_inf={p:.8f}  se={se:.6f}')
