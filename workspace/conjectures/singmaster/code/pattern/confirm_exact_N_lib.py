#!/usr/bin/env python3
"""Use the trusted library oracle (lib.binom_multiplicity) to confirm the exact
N(a_i) for the infinite N>=6 family i=1..5, matching the covention of
CONTEXT.md (both mirrors + trivial pair).

i=5 (a ~ 10^9688) is slow (~330s, 28 workers) and its exact capture is
code/out/extend_exact_N_family_i5.captured.txt; here we run the same trusted
oracle for i=1..4 (fast) and, time permitting, i=5.
"""
from lib.binom_multiplicity import multiplicity, canonical_reps


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


for i in range(1, 5):
    n = fib(2 * i + 2) * fib(2 * i + 3) - 1
    k = fib(2 * i) * fib(2 * i + 3) - 1
    a = __import__("math").comb(n + 1, k + 1)
    assert __import__("math").comb(n, k + 2) == a
    N = multiplicity(a, a)
    reps = sorted(canonical_reps(a, a))
    print("i=%d  a digits=%d  N(a)=%d  canonical reps=%s" % (i, len(str(a)), N, reps))
print("DONE (trusted oracle = lib.binom_multiplicity)")