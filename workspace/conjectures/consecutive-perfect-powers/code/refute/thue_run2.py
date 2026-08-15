#!/usr/bin/env python3
import sys
sys.path.insert(0, "/workspace/code")
from refute.thue_descent_check import brute, is_odd_prime

print("Known q=3,m=1:", brute(3, 1, 10))
total = 0
for q in [p for p in range(3, 30, 2) if is_odd_prime(p)]:
    for m in range(1, 8):
        h = brute(q, m, 300)
        ex = [(r, s, sg) for (r, s, sg) in h if not (q == 3 and m == 1 and r == 1 and s == 1)]
        if ex:
            print(f"q={q} m={m}: EXTRAS {ex}")
            total += len(ex)
print("total extras:", total)
