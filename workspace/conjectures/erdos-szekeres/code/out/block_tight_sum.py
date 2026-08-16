#!/usr/bin/env python3
"""Compact statement of the per-block tightness of the ES construction.

For every interior block T_i of X_n (es_block(n,i), 1<=i<=n-3):
    longest_cup(T_i) = n-i-1,  longest_cap(T_i) = i+1
so longest_cup + longest_cap = n.
Endpoints i=0 and i=n-2 are singletons (cup=cap=1).
The bounds are: no (n-i)-cup (cup <= n-i) and no (i+2)-cap (cap <= i+2), so
achieving n-i-1 and i+1 is the maximum possible in each direction at once.
"""
from lib.es_construct import es_block
from lib.es_geom import longest_cup, longest_cap

all_ok = True
for n in range(4, 10):
    row = []
    for i in range(1, n - 2):          # interior blocks 1..n-3
        T = es_block(n, i)
        cu = longest_cup(T)
        ca = longest_cap(T)
        ok = (cu == n - i - 1) and (ca == i + 1) and (cu + ca == n)
        all_ok &= ok
        row.append(f"i={i}: cup={cu}+cap={ca}={cu+ca}(n={n}) {'OK' if ok else 'BAD'}")
    print(f"n={n}: " + "  ".join(row))
print("ALL INTERIOR BLOCKS TIGHT (cup+cap=n) for n=4..9:", all_ok)
