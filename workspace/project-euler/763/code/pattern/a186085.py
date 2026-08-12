#!/usr/bin/env python3
"""Compute OEIS A186085 (1D sandpiles / smooth compositions) prediction.

Recurrence (Alois P. Heinz): b(n,i) with b(0,1)=1; b(n,i)= sum_{j=-1..1} b(n-i, i+j), n>0, b<0 or i<1 ->0.  a(n)= (n==0?1 : b(n-1,1)).
This is exactly the "number of compositions of n with first part 1, up-steps <=1".
We want a(12),a(13),a(14) (index equals N) to test vs distinct-histogram counts
at N=12,13,14.  Data gives N=12 -> 100; predict a(13), a(14), a(15).
"""
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

@lru_cache(maxsize=None)
def b(n, i):
    if n == 0:
        return 1 if i == 1 else 0
    if n < 0 or i < 1:
        return 0
    return b(n - i, i - 1) + b(n - i, i) + b(n - i, i + 1)

def a(n):
    if n == 0:
        return 1
    return b(n - 1, 1)

for n in range(0, 16):
    print(f"a({n}) = {a(n)}")
