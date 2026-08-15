#!/usr/bin/env python3
"""Scholar trust-anchor verification: the oracle generator must reproduce
the five worked rows in problem.md exactly before any claim built on real
rows is trusted."""
import sys
sys.path.insert(0, "/workspace/code")
from lib.gilbreath import primes_up_to, rows_generator

# problem.md expected rows (first 12 entries each)
EXPECTED = {
    1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4],
    2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2],
    3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
    4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
    5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
}

primes = primes_up_to(60)
gen = rows_generator(primes, 5)
rows = [next(gen) for _ in range(6)]  # A_0 .. A_5

ok = True
for k in range(1, 6):
    got = rows[k][:12]
    match = got == EXPECTED[k]
    ok = ok and match
    print(f"A_{k} = {got}  match={match}")
print("ALL:", ok)
