#!/usr/bin/env python3
"""Verify the n=3 counterexample from memory.md with exact arithmetic,
and reproduce the full n=3 L=160 probability table exactly by sampling
rational speeds (uniform grid) -> count parities. This is the oracle.

Grid: v_j = k/M for k=1..M (uniform). The event logic is exact on Fractions.
p(3,160)=56/135≈0.4148 so MC grid count should approach that as M grows.
"""
from fractions import Fraction as F
from exact_race import simulate_order_exact, outcome_parity_exact
from brute import simulate_order, outcome_parity

# --- counterexample check (exact + float) ---
ce1 = [0.88083, 0.60364, 0.35634]
ce2 = [0.72906, 0.43938, 0.02941]
n, L = 3, 160
for name, sp in (("ce1", ce1), ("ce2", ce2)):
    pf = outcome_parity(n, L, sp)
    pf2 = outcome_parity_exact(n, L, [F(k).limit_denominator(1_000_000) for k in sp])
    print(f"{name}: float-parity={pf} exact-parity={pf2}")

# --- full table reproduction via exact grid count ---
def grid_count(n, L, M):
    even = 0; total = 0
    # iterate v_0,v_1,v_2 in 1..M
    for a in range(1, M+1):
        for b in range(1, M+1):
            for c in range(1, M+1):
                par = outcome_parity_exact(n, L, [F(a), F(b), F(c)])
                if par == 0: even += 1
                total += 1
    return even, total

if __name__ == '__main__':
    for M in (8, 16, 32):
        e, t = grid_count(3, 160, M)
        print(f"grid M={M}: even={e}/{t} = {e/t:.4f}   (exact 56/135 = {56/135:.4f})")