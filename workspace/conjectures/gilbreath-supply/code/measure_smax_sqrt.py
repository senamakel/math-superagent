#!/usr/bin/env python3
"""Measure max|S(n)|/sqrt(n) (=max|E2|/sqrt(n)) at dyadic prefixes through N.
S(n)=E2(n) up to sign. If this ratio stays bounded (<=~4) the excess follows a
sqrt-n 'walk'; if it diverges the increment mean-reversion is decaying."""
import sys, math
sys.path.insert(0, "/workspace/code")
from lib.nu2 import fold_nu2
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)
    print(f"n       |S|     |S|/sqrt(n)   cumulative max of |S|/sqrt(n)")
    cum = 0.0
    for n in range(50, N + 1):
        v = fold_nu2(n, h)
        S = n - 2 - 2 * v if False else abs(2 * v - (n - 2))
        r = abs(2*v - (n-2)) / math.sqrt(n)
        if r > cum:
            cum = r
            cum_at = n
        if n % (N // 8) == 0 or n in (100, 1000, 4000):
            print(f"{n:6d}  {abs(2*v-(n-2)):5d}   {abs(2*v-(n-2))/math.sqrt(n):7.3f}   "
                  f"{cum:7.3f} @n={cum_at}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20000)
