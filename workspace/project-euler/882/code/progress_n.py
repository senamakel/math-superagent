#!/usr/bin/env python3
"""n=6 with per-budget progress reporting (budgeted real-game solver)."""
import sys, time
INF = float("inf")

def one_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]; out = set()
    for i, ch in enumerate(s):
        if ch == "1":
            t = s[:i] + s[i + 1:]; out.add(0 if t == "" else int(t, 2))
    return sorted(out)

def zero_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]; out = set()
    for i, ch in enumerate(s):
        if ch == "0":
            t = s[:i] + s[i + 1:]; out.add(0 if t == "" else int(t, 2))
    return sorted(out)

def initial_multiset(n):
    ms = []
    for k in range(1, n + 1):
        ms += [k] * k
    return tuple(sorted(ms))

def moves(state, who):
    tbl = one_deletions if who == "One" else zero_deletions
    out = set()
    for i, x in enumerate(state):
        for y in tbl(x):
            lst = list(state); lst[i] = y
            out.add(tuple(sorted(lst)))
    return sorted(out)

class Solver:
    def __init__(self):
        self.memo = {}
        self.states = 0
    def need(self, state, turn, used, budget):
        key = (state, turn, used, budget)
        if key in self.memo: return self.memo[key]
        self.states += 1
        if turn == "One":
            mvs = moves(state, "One")
            v = 0.0 if not mvs else max(self.need(m, "Zero", used, budget) for m in mvs)
        else:
            mvs = moves(state, "Zero")
            opts = [r for r in (self.need(m, "One", used, budget) for m in mvs) if r < INF]
            if used < budget:
                r = self.need(state, "One", used + 1, budget)
                if r < INF: opts.append(r + 1.0)
            v = min(opts) if opts else INF
        self.memo[key] = v
        return v

sys.setrecursionlimit(10**6)
n = int(sys.argv[1])
init = initial_multiset(n)
t0 = time.time()
for k in range(0, 100):
    solv = Solver()
    v = solv.need(init, "One", 0, k)
    print(f"budget={k}: need={v}  states={solv.states}  t={time.time()-t0:.0f}s", flush=True)
    if v < INF:
        print(f"S({n}) = {k}", flush=True)
        break
