#!/usr/bin/env python3
"""Confirm the mod-9 necessity derivation: for every S-root m, m(m-1) == 0 mod 9.
Why: m^2 splittable into blocks summing to m; since 10 == 1 mod 9, m^2 == sum-of-digits(m^2)
== sum of blocks == m (mod 9).  So m^2 == m mod 9, m(m-1) == 0 mod 9, and gcd(m,m-1)=1 forces
m == 0 or 1 mod 9. Check against all 3200 catalogued roots."""
import re
B_FILE = "research/sources/oeis_a038206_b.full.md"
def load_roots(path):
    roots=[]
    with open(path) as f:
        for line in f:
            m=re.match(r"\s*(\d+)\s+(\d+)\s*$",line)
            if m: roots.append(int(m.group(2)))
    return roots
R=load_roots(B_FILE)

# necessary condition: m == 0 or 1 mod 9
bad=[r for r in R if r%9 not in (0,1)]
print("roots violating m in {0,1} mod 9:", len(bad))
# equivalent: m^2 == m mod 9
bad2=[r for r in R if (r*r - r) % 9 != 0]
print("roots violating m^2==m mod 9:", len(bad2))
# And the sufficient-side dot product: how many candidates 2..10^6 pass the filter?
cnt=sum(1 for m in range(2,10**6+1) if m%9 in (0,1))
print("candidates 2..10^6 passing mod-9 filter:", cnt, "of", 10**6-1)
