#!/usr/bin/env python3
"""Extract E2 at dyadic boundaries and consecutive terms to test fractal/
self-similar renormalization structure: does E2(2n) relate to E2(n)?"""
import sys, math
data = {}
for line in open("out/excess_seq.txt"):
    n, nu2, e2 = map(int, line.split())
    data[n] = e2
N = max(data)
print("n        E2(n)   E2(2n)-2*E2(n)   E2(2n+1)   (E2(2n+1)+E2(2n))/2   E2(n)")
for n in [3,5,7,9,11,13,15,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097]:
    if n <= N//2:
        r = data.get(2*n, None)
        e = data.get(n, None)
        rr = data.get(2*n+1, None)
        if r is not None and e is not None:
            print(f"{n:5d}  {e:6d}   {('n/a' if r is None else str(r-2*e)):>12s}"
                  f"   {('n/a' if rr is None else str(rr)):>6s}   "
                  f"{(r+rr)/2 if (r is not None and rr is not None) else 0:8.1f}"
                  f"   {e:6d}")
