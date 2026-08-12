#!/usr/bin/env python3
"""Extract integer sequences for the pattern tools: K(n), and the
integer-ordered V(n)^2 related quantities where they are exactly quadratic."""
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

N = 60
Ks = [K_of_n(n) for n in range(3, N + 1)]
print("K(3..%d):" % N)
print(Ks)

# K(n)+n auxiliary appearing in alpha
print("(K+n)(3..%d):" % N)
print([K_of_n(n)+n for n in range(3, N+1)])

# 2K? print K increments (difference) to see near-periodicity
diffs = [Ks[i]-Ks[i-1] for i in range(1, len(Ks))]
print("diff K(3..%d):" % N)
print(diffs)
