#!/usr/bin/env python3
from code.refute.bivariate_diagonal_oracle import search
from code.refute.fib_block_state_counterexample import first_collision
from code.brute import brute_psi
print("oracle Psi(3) =", brute_psi(3))
print("oracle Psi(10) mod 101001001 =", brute_psi(10) % 101001001)
print("bivariate diagonal oracle =", search())
print("corrected block-state oracle =", first_collision())
