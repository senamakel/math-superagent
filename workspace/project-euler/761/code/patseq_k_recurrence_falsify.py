#!/usr/bin/env python3
"""Find the exact first n >= 11 where K(n) = K(n-1) + K(n-7) - K(n-8) fails,
using only valid anchors K(3..10) (no K(1),K(2) — those belong to a different,
degenerate indexing). K(n) computed with mpmath at dps=50."""
import mpmath as mp

mp.mp.dps = 50

def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    best = 0
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            best = k
    return best

N = 400
K = {n: K_of_n(n) for n in range(3, N + 1)}

# order-8 recurrence with anchors n=3..10, valid from n=11 onward
first_fail = None
for n in range(11, N + 1):
    if K[n] != K[n - 1] + K[n - 7] - K[n - 8]:
        first_fail = n
        break
print("first n>=11 where order-8 recurrence fails:", first_fail)
if first_fail is not None:
    print(f"  K[{first_fail}]={K[first_fail]} vs K[{first_fail-1}]+K[{first_fail-7}]-K[{first_fail-8}]"
          f"={K[first_fail-1]}+{K[first_fail-7]}-{K[first_fail-8]}="
          f"{K[first_fail-1]+K[first_fail-7]-K[first_fail-8]}")

# also: floor(3n/7) equality range
first_floor_fail = None
for n in range(3, N + 1):
    if K[n] != 3 * n // 7:
        first_floor_fail = n
        break
print("first n where K(n) != floor(3n/7):", first_floor_fail)
print("recurrence held on n=11..60 (the tool's verification window):",
      all(K[n] == K[n-1] + K[n-7] - K[n-8] for n in range(11, 61)))