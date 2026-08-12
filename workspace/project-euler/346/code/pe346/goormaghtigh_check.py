"""Confirm the structural identification: the dedup=2 result at 10^12
corresponds to the two known solutions of Goormaghtigh's equation
  (x^m - 1)/(x - 1) = (y^n - 1)/(y - 1),  x,y>1, m,n>2.

The two strong repunits below 10^12 representable as length>=3 repunits in
two distinct bases should be exactly
  31  = (2^5 -1)/(2-1) = (5^3 -1)/(5-1)    [11111_2 = 111_5]
  8191 = (2^13-1)/(2-1) = (90^3-1)/(90-1)  [13 ones in base 2 = 111_90]

Enumerate all distinct values (b^k-1)/(b-1), b>=2, k>=3, <10^12, and report
every value that has two distinct (b,k) representations.
"""
N = 10**12
from collections import defaultdict
seen = defaultdict(list)
b = 2
while True:
    if b*b + b + 1 >= N:   # smallest k=3 value must be < N to matter
        break
    k = 3
    while True:
        v = (pow(b, k) - 1)//(b - 1)
        if v >= N:
            break
        seen[v].append((b, k))
        k += 1
    b += 1

dups = {v: reps for v, reps in seen.items() if len(reps) > 1}
print("double-repunit values below 10^12:", len(dups))
for v in sorted(dups):
    print(f"  {v} = " + " = ".join(f"(base {b}, len {k})" for b, k in dups[v]))

# Confirm the two Goormaghtigh forms explicitly.
print()
print("31  check: (2^5-1)/(2-1) =", (2**5-1)//(2-1), " (5^3-1)/(5-1) =", (5**3-1)//(5-1))
print("8191 check: (2^13-1)/(2-1) =", (2**13-1)//(2-1), " (90^3-1)/(90-1) =", (90**3-1)//(90-1))
