#!/usr/bin/env python3
"""Probe RealSolver(6) with periodic progress output to see how far it gets
before the timeout. Strictly n=6 only. Patches RealSolver._need at class level
so the lru_cache wrapper wraps the probing wrapper.
"""
import sys, time
sys.path.insert(0, "/workspace/code")
import fastbrute
from fastbrute import RealSolver, initial_multiset

n = 6
if n >= 7:
    sys.exit(2)
sys.setrecursionlimit(10 ** 7)

start = time.time()

_orig_need = RealSolver._need
def probe(self, state, turn):
    r = _orig_need(self, state, turn)
    if self.n_states % 200000 == 0:
        print(f"t={time.time()-start:7.1f}s states={self.n_states} "
              f"one={self.n_one} zero={self.n_zero} turn={turn}", flush=True)
    return r
RealSolver._need = probe

solver = RealSolver(n)
init = initial_multiset(n)
S = solver.solve(init)
elapsed = time.time() - start
st = solver.stats()
print(f"\nS(6) = {S}")
print(f"states_memoized = {st['states']} (One={st['one']}, Zero={st['zero']})")
print(f"elapsed_seconds = {elapsed:.3f}")
