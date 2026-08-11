import re, sys
from collections import Counter

# Parse each level_N.txt: "a0 a1 ... aM | M | dx dy dz"
# Extract max level M (the number right after the first pipe).
def hist(N):
    with open(f"data/level_{N}.txt") as f:
        lines = f.read().splitlines()
    c = Counter()
    for ln in lines:
        parts = ln.split("|")
        M = int(parts[1].strip())
        c[M] += 1
    return c, len(lines)

for N in range(2, 13):
    c, n = hist(N)
    assert n == sum(c.values())
    print(f"N={N} total={n} maxM_hist={dict(sorted(c.items()))}")
