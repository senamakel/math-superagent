#!/usr/bin/env python3
"""Print sums of F(d) over proper divisors and the n!-divisor (cyclic subgroup)
to inspect the pattern behind F(d).  Prompts discoveries; the numbers are
exact (plain ints)."""

import sys
from math import factorial

sys.path.insert(0, "/workspace")
from toolkits.f_table import f_table  # noqa: E402


def proper_divisors(x):
    return [d for d in range(1, x) if x % d == 0]


for n in (4, 5, 6):
    nf = factorial(n)
    F = f_table(n)
    props = proper_divisors(nf)
    s_prop = sum(F[d] for d in props)
    s_all = sum(F.values())
    s_nf = F[nf]  # actual value, not an assumed average
    print(f"n={n} n!={nf}")
    print(f"  F(n!)=sum_pi rank(pi^n!): actual {s_nf}, "
          f"assumed-avg {nf*(nf+1)//2}")
    print(f"  proper-divisor sum = {s_prop}")
    print(f"  sum_all_d F(d)        = {s_all}")
    print(f"  suggested G(a)={s_prop//nf}*({nf}+1) -> "
          f"{(s_prop//nf)*(nf+1)}  (ratio {s_prop/(nf*(nf+1)):.6f})")
