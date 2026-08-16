#!/usr/bin/env python3
"""Verify the block-tightness conjecture at larger n (first falsifier: n=8).

Conjecture (from n=3..7): for block i of X_n = es_block(n,i):
  * longest_cup(T_i) = n-i-1   (bound is n-i, one more than achievable max)
  * longest_cap(T_i) = i+1     (bound is i+2)
for interior blocks i=1..n-3; endpoint blocks i=0 and i=n-2 are singletons.

Report achieved cup/cap and mark any violation.  This is the smallest n past
the data that suggested the pattern, so a violation here falsifies it.
"""
from lib.es_construct import es_block
from lib.es_geom import longest_cup, longest_cap
from math import comb

for n in (8, 9):
    print(f"=== n={n} (first test beyond suggested data: n=8) ===")
    ok = True
    for i in range(n - 1):
        T = es_block(n, i)
        if len(T) == 1:
            continue  # endpoint singleton, trivial
        cu = longest_cup(T)
        ca = longest_cap(T)
        exp_cu = n - i - 1
        exp_ca = i + 1
        good = (cu == exp_cu) and (ca == exp_ca)
        ok &= good
        flag = "" if good else "  <-- VIOLATION"
        print(f"   block i={i}: |T|={len(T)} cup={cu}(exp {exp_cu}) "
              f"cap={ca}(exp {exp_ca}){flag}")
    print(f"   n={n}: all interior blocks tight = {ok}")
    print()
