"""Extract integer sequences for pattern analysis.

Produce:
  1. the sorted distinct strong repunits up to a bound,
  2. cumulative count and sum as functions of powers of ten,
"""
import math

def strong_repunits(N):
    s = set()
    if N >= 1:
        s.add(1)
    b = 2
    while True:
        if b*b + b + 1 > N:
            break
        pw = b*b*b
        k = 3
        while True:
            val = (pw - 1)//(b - 1)
            if val > N:
                break
            s.add(val)
            pw *= b
            k += 1
        b += 1
    return sorted(s)

if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    sr = strong_repunits(N)
    print("bound:", N)
    print("sequence:")
    print(sr)
    print("count:", len(sr), "sum:", sum(sr))
