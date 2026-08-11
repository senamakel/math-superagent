#!/usr/bin/env python3
"""
Driver for the real-game minimax oracle (Project Euler 882).

Reuses the budget-removed solver logic of fastbrute.py but addresses the
buffering problem that hid progress: stdout is flushed after every n, and each
n is solved in its own solver instance.  Prints S(n) for the requested range.

Usage: python3 run_real.py [n_lo] [n_hi]
"""
import sys
from functools import lru_cache

def bin_deletions_tables(limit):
    one, zero = {}, {}
    for x in range(0, limit + 1):
        if x == 0:
            one[x], zero[x] = [], []
            continue
        s = bin(x)[2:]
        o, z = set(), set()
        for i, ch in enumerate(s):
            t = s[:i] + s[i + 1:]
            y = 0 if t == "" else int(t, 2)
            if ch == "1":
                o.add(y)
            else:
                z.add(y)
        one[x], zero[x] = sorted(o), sorted(z)
    return one, zero


def initial_multiset(n):
    ms = []
    for k in range(1, n + 1):
        ms += [k] * k
    return tuple(sorted(ms))


class RealSolver:
    def __init__(self, n):
        self.one, self.zero = bin_deletions_tables(n)
        self.n_states = 0
        self._memo_moves = {}
        self._f = lru_cache(maxsize=None)(self._need)

    def moves(self, state, who):
        key = (state, who)
        v = self._memo_moves.get(key)
        if v is not None:
            return v
        tbl = self.one if who == "One" else self.zero
        out = set()
        for i, x in enumerate(state):
            for y in tbl[x]:
                lst = list(state)
                lst[i] = y
                out.add(tuple(sorted(lst)))
        v = tuple(sorted(out))
        self._memo_moves[key] = v
        return v

    def _need(self, state, turn):
        self.n_states += 1
        if turn == "One":
            mvs = self.moves(state, "One")
            if not mvs:
                return 0
            return max(self._need(m, "Zero") for m in mvs)
        else:
            mvs = self.moves(state, "Zero")
            best = min(self._need(m, "One") for m in mvs) if mvs else None
            skip = 1 + self._need(state, "One")
            return skip if best is None else min(best, skip)

    def solve(self, state):
        return self._need(state, "One")


def main():
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    import time
    print("=== real-game S(n) optimizer (budget removed) ===", flush=True)
    for n in range(lo, hi + 1):
        t0 = time.time()
        solv = RealSolver(n)
        S = solv.solve(initial_multiset(n))
        dt = time.time() - t0
        print(f"S({n}) = {S}   states={solv.n_states}   move_cache={len(solv._memo_moves)}   t={dt:.1f}s",
              flush=True)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 7)
    main()
