#!/usr/bin/env python3
"""Find exactly where the period-7 first-difference pattern [0,1,0,1,0,0,1] of K(n) breaks."""
import math

def K_of_n(n):
    th = math.pi / n
    t = math.tan(th)
    for k in range(0, n + 1):
        val = math.sin(k * th) - (k + n) * t * math.cos(k * th)
        if val < 0:
            return k
    return None

PATTERN = [0, 1, 0, 1, 0, 0, 1]
NMAX = 400
prev = K_of_n(3)
breaks = []
diffs_record = []
for n in range(4, NMAX + 1):
    k = K_of_n(n)
    d = k - prev
    diffs_record.append(d)
    idx = (n - 4) % 7
    if d != PATTERN[idx]:
        breaks.append((n, d, PATTERN[idx]))
    prev = k

print("First break of period-7 difference pattern (up to n=400):")
for b in breaks[:20]:
    print("  n=%d d=%d expected=%d" % b)
print("total breaks up to 400:", len(breaks))

# Also test the order-8 linear recurrence on the full sequence.
Ks = [K_of_n(n) for n in range(3, NMAX + 1)]
rec_ok = True
first_bad = None
for i in range(8, len(Ks)):
    # a(i) = a(i-1) + a(i-7) - a(i-8)
    lhs = Ks[i]
    rhs = Ks[i-1] + Ks[i-7] - Ks[i-8]
    if lhs != rhs:
        rec_ok = False
        first_bad = i + 3  # n value
        break
print("\norder-8 recurrence a(n)=a(n-1)+a(n-7)-a(n-8) holds up to n=", NMAX, "?", rec_ok, first_bad)
