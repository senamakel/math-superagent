#!/usr/bin/env python3
"""Study structure of g(k). Test candidate recurrences:
- g(2k) vs g(k), g(2k+1) vs ...
- block self-similarity at powers of two.
"""
from fractions import Fraction
import sys
sys.path.insert(0, '.')
from gtable import eval_g

g = eval_g(4096)

# test g(2k) = g(k)/2 ?
print("g(2k) vs g(k)/2  (first failures):")
cnt=0
for k in range(1,2048):
    if g[2*k] != g[k]/2:
        print(f"  k={k}: g(2k)={g[2*k]}, g(k)/2={g[k]/2}")
        cnt+=1
        if cnt>10: break

print("\ng(2k+1) vs g(2k)?  (first 20 odd)")
for k in range(1,21):
    print(f"  k={k}: g(2k+1)={g[2*k+1]}, g(2k)={g[2*k]}, g(k)={g[k]}")
