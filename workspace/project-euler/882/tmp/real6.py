#!/usr/bin/env python3
"""Driver: run the real-game minimax oracle (RealSolver) for n=6 only.

Builds RealSolver(6), solves the initial multiset (k copies of k, k=1..6),
prints S(6) and the state count. Strict timeout enforced by the caller.
"""
import sys, time
sys.path.insert(0, "/workspace/code")

from fastbrute import RealSolver, initial_multiset

n = 6
if n >= 7:
    print("Refusing n>=7")
    sys.exit(2)

sys.setrecursionlimit(10 ** 7)
solver = RealSolver(n)
init = initial_multiset(n)
start = time.time()
S = solver.solve(init)
elapsed = time.time() - start
st = solver.stats()

print(f"S(6) = {S}")
print(f"states_memoized = {st['states']}  (One={st['one']}, Zero={st['zero']})")
print(f"move_cache_entries = {st['move_entries']}")
print(f"elapsed_seconds = {elapsed:.3f}")
